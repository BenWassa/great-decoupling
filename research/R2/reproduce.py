#!/usr/bin/env python3
"""R2 deterministic descriptive exhibits + constructed household scenarios.

Run:
  python3 research/R2/reproduce.py
  python3 research/R2/reproduce.py --check
  python3 research/R2/reproduce.py --write

No external APIs, interpolation, causal inference or microdata claims.
"""
import argparse
import csv
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

HERE = Path(__file__).resolve().parent
ZERO = Decimal("0")
D = Decimal


def read_csv(file, required):
    with (HERE / file).open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        if not set(required).issubset(reader.fieldnames or []):
            raise ValueError("Missing columns from " + str(file))
        data = list(reader)
    if not data:
        raise ValueError("Empty input: " + str(file))
    return data


def inputs():
    sources = read_csv("source-inventory.csv", ["id", "direct_url"])
    ids = {r["id"] for r in sources}
    if len(ids) != len(sources):
        raise ValueError("Duplicate source id")
    obs = read_csv("data/observations.csv", ["key", "source_id", "value", "locator"])
    o = {}
    for row in obs:
        key = row["key"]
        if key in o or row["source_id"] not in ids or not row["locator"].startswith("https://"):
            raise ValueError("Duplicate key or invalid provenance for " + key)
        value = D(row["value"])
        if not value.is_finite() or value < ZERO:
            raise ValueError("Invalid observation value for " + key)
        o[key] = value
    sc = read_csv("data/scenarios.csv",
                  ["id", "earner1_gross_annual_usd", "earner2_gross_annual_usd",
                   "effective_tax_rate_assumption", "monthly_housing_usd",
                   "annual_worker_family_premium_usd", "monthly_paid_childcare_usd",
                   "monthly_other_essentials_usd", "annual_debt_service_usd",
                   "starting_liquid_savings_usd"])
    keys = ["earner1_gross_annual_usd", "earner2_gross_annual_usd",
            "effective_tax_rate_assumption", "monthly_housing_usd",
            "annual_worker_family_premium_usd", "monthly_paid_childcare_usd",
            "monthly_other_essentials_usd", "annual_debt_service_usd",
            "starting_liquid_savings_usd"]
    names = set()
    for r in sc:
        if r["id"] in names:
            raise ValueError("Duplicate scenario " + r["id"])
        names.add(r["id"])
        for key in keys:
            value = D(r[key])
            if not value.is_finite() or value < ZERO:
                raise ValueError("Negative/nonfinite scenario input: " + key)
        if D(r["effective_tax_rate_assumption"]) >= 1:
            raise ValueError("Tax fraction must be below 1")
        if D(r["annual_worker_family_premium_usd"]) != o["kff_worker_family_2026"]:
            raise ValueError("KFF reference worker premium does not match observation")
    return o, sc


def usd(x):
    n = D(x).quantize(D("1"), rounding=ROUND_HALF_UP)
    return ("-$" if n < 0 else "$") + f"{abs(n):,.0f}"


def pct(x):
    return f"{D(x):.1f}%"


def pp(x):
    return f"{D(x):+.1f} pp"


def scenario(s):
    n1, n2 = D(s["earner1_gross_annual_usd"]), D(s["earner2_gross_annual_usd"])
    tax = D(s["effective_tax_rate_assumption"])
    gross = n1 + n2
    housing = D(s["monthly_housing_usd"])
    care = D(s["monthly_paid_childcare_usd"])
    other = D(s["monthly_other_essentials_usd"])
    prem = D(s["annual_worker_family_premium_usd"])
    debt = D(s["annual_debt_service_usd"])
    savings = D(s["starting_liquid_savings_usd"])
    net_month = gross * (1 - tax) / 12
    monthly_commitments = housing + care + other + (prem + debt) / 12
    margin = net_month - monthly_commitments
    annual_margin = margin * 12
    monthly_commitments_ratio = monthly_commitments * 12 / gross * 100
    return dict(id=s["id"], first=n1, second=n2, gross=gross, tax=tax,
                monthly_commitments=monthly_commitments, margin=margin,
                annual_margin=annual_margin, share=monthly_commitments_ratio,
                savings=savings)


def shock_shortfall(result, shock, months=3):
    """Shock at end of 3 months, after modeled surpluses/deficits; no new borrowing."""
    resources = max(ZERO, result["savings"] + D(months) * result["margin"])
    return max(ZERO, D(shock) - resources)


def lost_earner_shortfall(result, earner):
    """Three-month job-loss cash deficit after initial savings; static costs/premium."""
    lost_gross = result[earner] / 4
    remaining = result["savings"] + 3 * result["margin"] - lost_gross * (1 - result["tax"])
    return max(ZERO, -remaining)


def render():
    o, cases = inputs()
    out = ["# R2 reproducible exhibits", "",
           "Frozen primary-source observations, retrieved 2026-10-24; calculations from the accompanying CSV files.",
           "**No population inference from constructed scenarios.** See definitions-methods.md and evidence-pack.md.", "",
           "## E1 — Historical exposures and measurement sensitivity", "",
           "| Diagnostic | Earlier observation | Later observation | Recomputed quantity | What this is NOT |",
           "| --- | ---: | ---: | ---: | --- |"]
    old = o["new_home_q1_1984"] / o["cps_income_1984"]
    new = o["new_home_q1_2025"] / o["cps_income_2025"]
    out.append(f"| New-home price / all-HH income (Census via FRED S05 + CPS S01) | 1984-Q1: {old:.2f}× | 2025-Q1: {new:.2f}× | change {new-old:+.2f}× | Not same buyers or mortgage-payment burden |")
    rent = 12 * o["acs_gross_rent_2024"] / o["acs_hh_income_2024"] * 100
    out.append(f"| 2024 national median gross rent / all-HH median income (ACS S02/S03) | {usd(o['acs_gross_rent_2024'])}/month rent | {usd(o['acs_hh_income_2024'])}/year household income | {pct(rent)} | NOT median renter burden; different denominators |")
    prior, later = 1999, 2026
    p1 = o["kff_worker_family_1999"] / o["kff_total_family_1999"] * 100
    p2 = o["kff_worker_family_2026"] / o["kff_total_family_2026"] * 100
    out.append(f"| KFF S09/S10 family coverage: worker share of premium | {prior}: {pct(p1)} | {later}: {pct(p2)} | {pp(p2-p1)} | Not amount deducted as % household income |")
    growth = (o["sipp_childcare_mean_2011"] / o["sipp_childcare_mean_1985"] - 1) * 100
    out.append(f"| SIPP S12 paid childcare mean (2011-dollar weekly) | 1985: {usd(o['sipp_childcare_mean_1985'])} | 2011: {usd(o['sipp_childcare_mean_2011'])} | {pct(growth)} change in reported real average | Not 2026 childcare price or all-family mean |")
    ip = (o["ipeds_instate_2023"] / o["ipeds_instate_2014"] - 1) * 100
    out.append(f"| IPEDS S15 public four-year in-state tuition/fees (constant 2023 USD) | 2014-15: {usd(o['ipeds_instate_2014'])} | 2023-24: {usd(o['ipeds_instate_2023'])} | {pct(ip)} | Not net attendance cost or student debt |")
    out.extend(["", "## E2 — Expenditure shares, composition and financial-shock survey observations", "",
                "| Series | Earlier | Later | Change | Unit / source |",
                "| --- | ---: | ---: | ---: | --- |"])
    for label,k0,k1,src in [
        ("Housing spending share","ce_housing_share_2021","ce_housing_share_2024","CE CU 2021→2024 S07"),
        ("Health spending share","ce_health_share_2021","ce_health_share_2024","CE CU 2021→2024 S07"),
        ("Food spending share","ce_food_share_2021","ce_food_share_2024","CE CU 2021→2024 S07"),
        ("Would use cash-equivalent for $400 hypothetical","shed_cash_2013","shed_cash_2025","SHED adults 2013→2025 S16"),
        ("Married-couple share of all households","census_married_share_1975","census_married_share_2025","Census households 1975→2025 S18"),
        ("One-person share of all households","census_oneperson_share_1975","census_oneperson_share_2025","Census households 1975→2025 S18")]:
        v0,v1 = o[k0],o[k1]
        out.append(f"| {label} | {pct(v0)} | {pct(v1)} | {pp(v1-v0)} | {src} |")
    out.extend(["", "Additional uncombined observations: 2024 CE mean CU spending "
                + usd(o["ce_mean_expenses_2024"]) + ", mean CU pretax income "
                + usd(o["ce_mean_income_2024"]) + ", mean CU health spending "
                + usd(o["ce_health_expenses_2024"]) + ". SHED 2025: "
                + pct(o["shed_rainy_day_2025"]) + " adults report 3-month rainy-day savings; "
                + pct(o["shed_cannot3mo_2025"]) + " cannot cover three months of expenses by the surveyed alternative means.",
                "", "## E3 — Illustrative household commitments (2026 USD; NOT survey household medians)", "",
                "| Scenario | Gross wages/yr | Effective tax (assumed) | Cash commitments/mo | Surplus or deficit/mo | Annual margin |",
                "| --- | ---: | ---: | ---: | ---: | ---: |"])
    computed = [scenario(s) for s in cases]
    for r in computed:
        out.append(f"| {r['id']} | {usd(r['gross'])} | {pct(r['tax']*100)} | {usd(r['monthly_commitments'])} | {usd(r['margin'])} | {usd(r['annual_margin'])} |")
    out.extend(["", "Commitments = rent + paid childcare + other essentials + worker-paid family coverage premium/12 + debt/12. "
                + "Tax is a synthetic fraction of gross wages; employer share of premium is excluded. "
                + "All cases have $10,000 starting liquid savings. Childcare assumptions depend on earner arrangement.",
                "", "## E4 — Liquidity and earner-loss stress (2026 USD; deterministic)", "",
                "| Scenario | $6k shock shortfall* | $15k shock shortfall* | 3mo loss of earner 1 gap** | 3mo loss of earner 2 gap** |",
                "| --- | ---: | ---: | ---: | ---: |"])
    for r in computed:
        loss1 = usd(lost_earner_shortfall(r, "first"))
        loss2 = usd(lost_earner_shortfall(r, "second")) if r["second"] > 0 else "n/a"
        out.append(f"| {r['id']} | {usd(shock_shortfall(r, 6000))} | {usd(shock_shortfall(r, 15000))} | {loss1} | {loss2} |")
    out.extend(["", "*Shock after three months of modelled baseline monthly surplus/deficit; savings plus net flows used before new borrowing. "
                + "A zero shortfall does not imply a tolerable loss of savings.",
                "**Gross wages of one earner cease for three months; wage-tax deduction proportionately reduced, all specified living costs unchanged. "
                + "The gap is remaining negative cash after using $10k liquid savings; unemployment benefits and job-linked insurance loss are not modeled.",
                "", "## Checks / non-comparability", "",
                "- New-home medians and household medians describe different populations. Housing mixes, geography and mortgage rates are uncontrolled.",
                "- Both childcare endpoints are reported in **constant 2011 dollars** for a restricted population. The post-2013 SIPP redesign is not spliced.",
                "- BLS CE percentage changes are percentage-point differences of aggregate average-spending shares, not median-family expenses.",
                "- KFF historical and current firm eligibility differs; 1999 vs 2026 dollar amounts are nominal; no inflation-adjusted comparison appears.",
                "- Synthetic scenario rent, childcare, other living costs, tax rates, and savings are **assumptions**, not observed cost distributions.",
                "- No missing periods filled, no regression/changepoint, no causal inference.", ""])

    # E5: matched-renter income/rent categories, *not* a ratio of two medians.
    rent_rows = []
    for suffix,label in (("us", "United States"), ("wa", "Washington state")):
        total = o["acs_rent_total_" + suffix + "_2024"]
        unknown = o["acs_rent_notcomputed_" + suffix + "_2024"]
        eligible = total - unknown
        if eligible <= 0:
            raise ValueError("Invalid matched-renter denominator")
        over30 = sum(o["acs_rent_" + k + "_" + suffix + "_2024"]
                     for k in ("30_34", "35_39", "40_49", "50plus"))
        severe = o["acs_rent_50plus_" + suffix + "_2024"]
        if over30 > eligible or severe > over30:
            raise ValueError("Burden bins exceed denominator")
        rent_rows.append(f"| {label} | {total:,.0f} | {unknown:,.0f} | {eligible:,.0f} | {over30:,.0f} | {pct(over30 / eligible * 100)} | {pct(severe / eligible * 100)} |")
    check_index = out.index("## Checks / non-comparability")
    out[check_index:check_index] = [
        "## E5 — Matched-income 2024 renter burden (ACS B25070, S04)", "",
        "| Geography | All renter units | Not computed (excluded) | Computable units | Units at ≥30% income on gross rent | ≥30% share | ≥50% share |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: |",
        *rent_rows, "",
        "Burden shares = sum of B25070 bins 007–010 divided by (001 minus 011); severe is 010 over the same denominator. "
        "These are sample-weighted 1-year ACS estimates, not household microdata reproductions. "
        "The published per-cell 90% margins of error do not directly supply a confidence interval for these derived ratios.", ""
    ]
    return "\n".join(out)


def main():
    p = argparse.ArgumentParser()
    group = p.add_mutually_exclusive_group()
    group.add_argument("--check", action="store_true")
    group.add_argument("--write", action="store_true")
    args = p.parse_args()
    output = render()
    target = HERE / "exhibits.md"
    if args.write:
        target.write_text(output, encoding="utf-8")
        print("Wrote", target)
    elif args.check:
        if not target.exists() or target.read_text(encoding="utf-8") != output:
            raise SystemExit("Exhibit mismatch; run --write then audit the diff")
        print("R2 exhibits match observations + scenarios")
    else:
        print(output, end="")


if __name__ == "__main__":
    main()
