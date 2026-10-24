#!/usr/bin/env python3
"""R1 reproducibility: offline frozen-anchor audit; optional full primary-series retrieval.

Requires Python 3.9+ standard library only. Do not treat a fitted breakpoint as
a causal estimate, a statistical significance test, or a preapproved historical date.
"""
from __future__ import annotations
import argparse
import csv
import hashlib
import io
import math
from pathlib import Path
from urllib.request import Request, urlopen

HERE = Path(__file__).resolve().parents[1]
BLS = ("OPHNFB", "COMPNFB", "COMPRNFB", "IPDNBS")
MONTHLY = ("PCEPI", "CPIAUCSL", "AHETPI")
SERIES = BLS + MONTHLY + ("LEU0252881600A",)
LENSES = (
    "BLS_published_historical_consumer_deflated",
    "matched_nonfarm_output_price",
    "BEA_PCE_price",
    "BLS_raw_CPIU_price",
)
FIELDS = ("start", "end", "compensation_lens", "productivity_growth_pct",
          "compensation_growth_pct", "cumulative_growth_difference_pp",
          "productivity_2025_rebased_to_start100",
          "compensation_2025_rebased_to_start100", "source_transform")


def read_csv(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write_csv(path, fields, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def finite_positive(value):
    number = float(value)
    if not math.isfinite(number) or number <= 0:
        raise ValueError("Expected finite positive index, got: " + str(value))
    return number


def grow(end, start):
    return 100.0 * (finite_positive(end) / finite_positive(start) - 1)


def read_anchor_observations(path):
    out = {}
    required = ("OPHNFB_index_2017_100", "COMPNFB_index_2017_100",
                "COMPRNFB_index_2017_100", "IPDNBS_index_2017_100")
    for row in read_csv(path):
        if not row["period"].endswith("-01-01"):
            raise ValueError("Not a Q1 quarterly observation: " + row["period"])
        year = int(row["period"][:4])
        if year in out:
            raise ValueError("Duplicate observation year: " + str(year))
        out[year] = dict(zip(BLS, (finite_positive(row[k]) for k in required)))
    return out


def read_anchor_prices(path):
    out = {}
    for row in read_csv(path):
        if not row["period"].endswith("Q1"):
            raise ValueError("Expected Q1 price checkpoint")
        year = int(row["period"][:4])
        if year in out:
            raise ValueError("Duplicate price year")
        item = {}
        for name, prefix in (("PCEPI", "PCEPI"), ("CPIAUCSL", "CPIAUCSL")):
            values = [finite_positive(row[prefix + "_" + m])
                      for m in ("Jan", "Feb", "Mar")]
            mean = sum(values) / 3
            if abs(mean - float(row[prefix + "_Q1_mean"])) > .00051:
                raise ValueError("Inconsistent quarterly price mean: " + str(year))
            item[name] = mean
        out[year] = item
    return out


def pay_level(bls, prices, lens):
    if lens == LENSES[0]:
        return bls["COMPRNFB"]
    if lens == LENSES[1]:
        return bls["COMPNFB"] / bls["IPDNBS"]
    if lens == LENSES[2] and prices is not None and "PCEPI" in prices:
        return bls["COMPNFB"] / prices["PCEPI"]
    if lens == LENSES[3] and prices is not None and "CPIAUCSL" in prices:
        return bls["COMPNFB"] / prices["CPIAUCSL"]
    return None


def anchor_rows(observations, prices, end_year=2025):
    if end_year not in observations:
        raise ValueError("Missing comparison end observation")
    output = []
    for year in sorted(observations):
        if year >= end_year:
            continue
        b, e = observations[year], observations[end_year]
        pg = grow(e["OPHNFB"], b["OPHNFB"])
        for lens in LENSES:
            base_price = pay_level(b, prices.get(year), lens)
            end_price = pay_level(e, prices.get(end_year), lens)
            if base_price is None or end_price is None:
                continue
            comp = grow(end_price, base_price)
            notes = "original_BLS_FRED_quarterly_index_Q1"
            if lens in LENSES[2:]:
                notes += "_monthly_quarter_average"
            output.append(dict(zip(FIELDS, (
                str(year) + "Q1", str(end_year) + "Q1", lens,
                "%.5f" % pg, "%.5f" % comp, "%.5f" % (pg - comp),
                "%.5f" % (100 + pg), "%.5f" % (100 + comp), notes))))
    return output


def offline(out):
    obs = read_anchor_observations(HERE / "exhibits/observations-q1.csv")
    prices = read_anchor_prices(HERE / "exhibits/price-checkpoints-q1.csv")
    rows = anchor_rows(obs, prices)
    saved = read_csv(HERE / "exhibits/sensitivity-q1.csv")
    if len(rows) != len(saved):
        raise ValueError("Number of calculated rows differs from committed exhibit")
    for calc, frozen in zip(rows, saved):
        for key in FIELDS:
            if calc[key] != frozen[key]:
                raise ValueError("Frozen exhibit mismatch for %s at %s: %s != %s"
                                 % (key, calc["start"], calc[key], frozen[key]))
    write_csv(out / "sensitivity-q1-reproduced.csv", FIELDS, rows)
    print("PASS: %d frozen rows recalculated; saved %s" %
          (len(rows), out / "sensitivity-q1-reproduced.csv"))


def remote_csv(series, raw_dir):
    url = "https://fred.stlouisfed.org/graph/fredgraph.csv?id=" + series
    req = Request(url, headers={"User-Agent": "R1-evidence-replication/1.0"})
    with urlopen(req, timeout=60) as reply:
        payload = reply.read()
    raw_dir.mkdir(parents=True, exist_ok=True)
    (raw_dir / (series + ".csv")).write_bytes(payload)
    sha = hashlib.sha256(payload).hexdigest()
    rows = list(csv.DictReader(io.StringIO(payload.decode("utf-8-sig"))))
    if not rows:
        raise ValueError("Empty remote data for " + series)
    date_col = "observation_date" if "observation_date" in rows[0] else "DATE"
    if date_col not in rows[0] or series not in rows[0]:
        raise ValueError("Unexpected CSV columns for " + series)
    data = {}
    for row in rows:
        day = row[date_col]
        val = row[series]
        if not val or val in (".", "NaN"):
            continue
        number = finite_positive(val)
        if day in data:
            raise ValueError("Duplicate date " + day)
        data[day] = number
    if not data:
        raise ValueError("No valid values for " + series)
    return data, {"series": series, "source_url": url,
                  "sha256": sha, "bytes": len(payload),
                  "observations": len(data),
                  "first_available": min(data), "last_available": max(data)}


def month_quarter(months, year, quarter):
    """Returns None unless all three month dates have distinct, positive values."""
    start = 3 * (quarter - 1) + 1
    dates = ["%04d-%02d-01" % (year, mon) for mon in range(start, start + 3)]
    if any(day not in months for day in dates):
        return None
    return sum(months[day] for day in dates) / 3.0


def annual_from_quarters(series, years=range(1947, 2026)):
    """Annual means of exactly four complete quarterly index observations."""
    output = {}
    for year in years:
        dates = ["%04d-%02d-01" % (year, month) for month in (1, 4, 7, 10)]
        if all(day in series for day in dates):
            output[year] = sum(series[d] for d in dates) / 4.0
    return output


def solve(matrix, right):
    """Gauss-Jordan with partial pivot; raises on rank deficiency."""
    n = len(right)
    aug = [list(matrix[i]) + [right[i]] for i in range(n)]
    for col in range(n):
        pivot = max(range(col, n), key=lambda i: abs(aug[i][col]))
        if abs(aug[pivot][col]) < 1e-10:
            raise ValueError("Singular design")
        aug[col], aug[pivot] = aug[pivot], aug[col]
        divider = aug[col][col]
        aug[col] = [v / divider for v in aug[col]]
        for r in range(n):
            if r != col:
                factor = aug[r][col]
                aug[r] = [x - factor * y for x, y in zip(aug[r], aug[col])]
    return [row[-1] for row in aug]


def fit_rss(features, targets):
    if len(features) != len(targets) or len(targets) < len(features[0]):
        raise ValueError("Incompatible regression observations")
    size = len(features[0])
    gram = [[sum(row[i] * row[j] for row in features) for j in range(size)]
            for i in range(size)]
    rhs = [sum(row[i] * y for row, y in zip(features, targets))
           for i in range(size)]
    coeff = solve(gram, rhs)
    return sum((y - sum(b * x for b, x in zip(coeff, row))) ** 2
               for row, y in zip(features, targets))


def break_diagnostics(observations, min_years=10, fixed=(1973, 1979, 1990, 2000, 2008)):
    """Descriptive hinged trends only; not inference / significance / causality."""
    if not observations:
        return []
    years = sorted(observations)
    first, last = years[0], years[-1]
    n = len(years)
    if n < 2 * min_years + 1:
        return []
    response = [observations[y] for y in years]
    t = [float(y - first) for y in years]
    baseline = [[1.0, x] for x in t]
    raw0 = fit_rss(baseline, response)
    if raw0 <= 0:
        return []
    bic0 = n * math.log(raw0 / n) + 2 * math.log(n)
    candidates = []
    for k in range(first, last + 1):
        if sum(y <= k for y in years) < min_years or sum(y > k for y in years) < min_years:
            continue
        features = [[1.0, x, max(0.0, y - k)] for x, y in zip(t, years)]
        try:
            rss = fit_rss(features, response)
        except ValueError:
            continue
        if rss <= 0:
            continue
        bic1 = n * math.log(rss / n) + 3 * math.log(n)
        candidates.append({"candidate_year": k, "n": n, "bic_no_break": bic0,
                           "bic_one_hinge": bic1, "bic_improvement": bic0 - bic1,
                           "is_fixed_sensitivity": k in fixed})
    candidates.sort(key=lambda d: (d["bic_one_hinge"], d["candidate_year"]))
    for rank, row in enumerate(candidates, 1):
        row["bic_rank"] = rank
    return candidates


def full(out):
    raw = out / "raw"
    retrieved = {}
    log = []
    for series in SERIES:
        data, meta = remote_csv(series, raw)
        retrieved[series] = data
        log.append(meta)
    write_csv(out / "source_hashes.csv",
              ("series", "source_url", "sha256", "bytes", "observations",
               "first_available", "last_available"), log)

    bq = {}
    qp = {"PCEPI": {}, "CPIAUCSL": {}}
    for year in range(1947, 2026):
        for q in range(1, 5):
            date = "%04d-%02d-01" % (year, 3 * (q - 1) + 1)
            if all(date in retrieved[series] for series in BLS):
                bq[(year, q)] = {s: retrieved[s][date] for s in BLS}
            for src in qp:
                price = month_quarter(retrieved[src], year, q)
                if price is not None:
                    qp[src][(year, q)] = price

    annual = {}
    for year in range(1947, 2026):
        bqs = [bq.get((year, q)) for q in range(1, 5)]
        if any(row is None for row in bqs):
            continue
        one = {name: sum(x[name] for x in bqs) / 4 for name in BLS}
        price = {}
        for src in qp:
            quarters = [qp[src].get((year, q)) for q in range(1, 5)]
            if all(value is not None for value in quarters):
                price[src] = sum(quarters) / 4
        annual[year] = (one, price)

    fields = ("year", "OPHNFB", "COMPNFB", "COMPRNFB", "IPDNBS",
              "CPIAUCSL_mean", "PCEPI_mean")
    annual_rows = []
    for year, (bls, price) in sorted(annual.items()):
        annual_rows.append({"year": year, **bls,
                            "CPIAUCSL_mean": price.get("CPIAUCSL", ""),
                            "PCEPI_mean": price.get("PCEPI", "")})
    write_csv(out / "annual_index_means.csv", fields, annual_rows)

    compare_fields = ("start_year", "end_year", "lens", "productivity_growth_pct",
                      "compensation_growth_pct", "cumulative_growth_difference_pp")
    comparison = []
    for start in (1947, 1973, 1979, 1990, 2000, 2008, 2010, 2019):
        for end in (2019, 2025):
            if start >= end or start not in annual or end not in annual:
                continue
            bp, ep = annual[start], annual[end]
            pg = grow(ep[0]["OPHNFB"], bp[0]["OPHNFB"])
            for lens in LENSES:
                start_value = pay_level(*bp, lens)
                end_value = pay_level(*ep, lens)
                if start_value is None or end_value is None:
                    continue
                wage_growth = grow(end_value, start_value)
                comparison.append(dict(start_year=start, end_year=end, lens=lens,
                                       productivity_growth_pct="%.5f" % pg,
                                       compensation_growth_pct="%.5f" % wage_growth,
                                       cumulative_growth_difference_pp="%.5f" % (pg - wage_growth)))
    write_csv(out / "annual_start_end_sensitivity.csv", compare_fields, comparison)

    bfields = ("lens", "sample_start", "sample_end", "candidate_year", "n",
               "bic_no_break", "bic_one_hinge", "bic_improvement",
               "bic_rank", "fixed_candidate")
    breaks = []
    for start in (1947, 1973, 1979, 1990, 2000):
        for end in (2019, 2025):
            for lens in LENSES:
                sample = {}
                for year, (bls, price) in annual.items():
                    if start <= year <= end:
                        wage = pay_level(bls, price, lens)
                        if wage is not None:
                            sample[year] = math.log(bls["OPHNFB"]) - math.log(wage)
                # A continuous time sample: no joining across unavailable years.
                if not sample or sorted(sample) != list(range(min(sample), max(sample) + 1)):
                    continue
                for item in break_diagnostics(sample):
                    breaks.append({"lens": lens, "sample_start": start,
                                   "sample_end": end, "candidate_year": item["candidate_year"],
                                   "n": item["n"], "bic_no_break": "%.8f" % item["bic_no_break"],
                                   "bic_one_hinge": "%.8f" % item["bic_one_hinge"],
                                   "bic_improvement": "%.8f" % item["bic_improvement"],
                                   "bic_rank": item["bic_rank"],
                                   "fixed_candidate": item["is_fixed_sensitivity"]})
    write_csv(out / "descriptive_breakpoint_diagnostics.csv", bfields, breaks)

    cash = {}
    for year in range(1964, 2026):
        dates = ["%04d-%02d-01" % (year, m) for m in range(1, 13)]
        if all(date in retrieved["AHETPI"] for date in dates):
            cash[year] = sum(retrieved["AHETPI"][d] for d in dates) / 12.0
    write_csv(out / "cash_hourly_earnings_annual.csv",
              ("year", "AHETPI_average_nominal_USD_hour", "CPI_deflated_index_unrebased"),
              [{"year": year, "AHETPI_average_nominal_USD_hour": cash[year],
                "CPI_deflated_index_unrebased":
                (cash[year] / annual[year][1]["CPIAUCSL"]
                 if year in annual and "CPIAUCSL" in annual[year][1] else "")}
               for year in sorted(cash)])
    print("PASS: full source downloads + hashes %d; annual years %d; "
          "comparisons %d; descriptive break fits %d"
          % (len(log), len(annual), len(comparison), len(breaks)))
    print("Note: source vintages change; inspect missing CPI 2025Q4; "
          "no inferential breakpoint claim is permitted.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--offline", action="store_true", help="Reproduce frozen Q1 exhibit")
    mode.add_argument("--full", action="store_true", help="Retrieve FRED and analyze entire history")
    parser.add_argument("--out", required=True, type=Path)
    args = parser.parse_args()
    if args.offline:
        offline(args.out)
    else:
        full(args.out)


if __name__ == "__main__":
    main()
