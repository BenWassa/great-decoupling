#!/usr/bin/env python3
"""R3 observation audit and optional FRED-source refresh. Standard library only.

This program validates a frozen source-linked observation seed; it does not claim
to independently reproduce confidential microdata, SEC aggregates or modelled
Federal Reserve balance-sheet allocations.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen

HERE = Path(__file__).resolve().parent
SOURCES = HERE / "source-inventory.csv"
OBSERVATIONS = HERE / "data" / "verified-observations.csv"
FRED_ALLOWLIST = frozenset({
    "WFRBST01134", "WFRBSB50215", "PRS85006173", "BOGZ1FA096121073Q",
})
SOURCE_COLUMNS = {
    "source_id", "source_title", "publisher", "primary_or_secondary", "url",
    "release_vintage", "retrieved_date", "geography", "unit_of_observation",
    "population", "measure", "denominator", "units_deflator",
    "time_coverage", "extraction_path", "revisions_or_breaks",
    "license_or_rights", "method_disagreement_uncertainty", "evidence_status",
}
OBS_COLUMNS = {
    "observation_id", "source_id", "period", "frequency", "measure_id",
    "population", "numerator", "denominator", "unit", "value", "vintage",
    "source_url", "status_note",
}


class AuditError(ValueError):
    """Validation failure requiring source review."""


def read_csv(path: Path, required: set[str]) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None or not required.issubset(reader.fieldnames):
            raise AuditError(f"{path}: missing headers {required - set(reader.fieldnames or [])}")
        rows = list(reader)
    if not rows:
        raise AuditError(f"{path}: empty CSV")
    for number, row in enumerate(rows, start=2):
        if None in row:
            raise AuditError(f"{path}:{number}: extra columns")
        if any(not (row.get(field) or "").strip() for field in required):
            raise AuditError(f"{path}:{number}: blank mandatory field")
    return rows


def validate() -> None:
    inventory = read_csv(SOURCES, SOURCE_COLUMNS)
    obs = read_csv(OBSERVATIONS, OBS_COLUMNS)
    by_source = {}
    for item in inventory:
        sid = item["source_id"]
        if sid in by_source:
            raise AuditError(f"duplicate source id {sid}")
        if not item["url"].startswith("https://"):
            raise AuditError(f"non-HTTPS source URL {sid}")
        by_source[sid] = item

    unique_obs = set()
    invariant = {}
    keys = {}
    for item in obs:
        sid = item["source_id"]
        if sid not in by_source:
            raise AuditError(f"unknown source {sid}")
        ident = item["observation_id"]
        if ident in unique_obs:
            raise AuditError(f"duplicate observation id {ident}")
        unique_obs.add(ident)
        key = (sid, item["measure_id"], item["period"], item["vintage"])
        if key in keys:
            raise AuditError(f"duplicate source/measure/period/vintage {key}")
        keys[key] = item
        if item["frequency"] not in {"annual", "quarter"}:
            raise AuditError(f"invalid frequency: {ident}")
        if (("Q" in item["period"]) != (item["frequency"] == "quarter")):
            raise AuditError(f"frequency-period mismatch: {ident}")
        if not item["source_url"].startswith("https://"):
            raise AuditError(f"non-HTTPS observation URL: {ident}")
        try:
            value = float(item["value"])
        except ValueError as error:
            raise AuditError(f"non-numeric observation: {ident}") from error
        if not math.isfinite(value):
            raise AuditError(f"non-finite observation: {ident}")
        if item["unit"] == "percent" and not 0 <= value <= 100:
            raise AuditError(f"out of range percent: {ident}")
        # The same explicitly named series cannot silently change scope or
        # denominator within a vintage. Alternate vintages are distinct.
        signature = (item["population"], item["numerator"],
                     item["denominator"], item["unit"], item["frequency"])
        group = (sid, item["measure_id"], item["vintage"])
        if group in invariant and invariant[group] != signature:
            raise AuditError(f"incompatible measure within vintage: {group}")
        invariant[group] = signature

    sp = {
        row["measure_id"]: float(row["value"]) for row in obs
        if row["source_id"] == "SP-BB" and row["period"] == "2025Q3"
    }
    needed = {"gross_repurchases_q", "dividends_q", "gross_payouts_q"}
    if not needed.issubset(sp):
        raise AuditError("S&P 2025 Q3 payout components missing")
    components = sp["gross_repurchases_q"] + sp["dividends_q"]
    reported = sp["gross_payouts_q"]
    if abs(components - reported) > 0.15:
        raise AuditError(f"S&P gross payout mismatch {components} vs {reported}")

    print(json.dumps({
        "validation": "passed",
        "source_records": len(inventory),
        "observation_records": len(obs),
        "distinct_measure_ids": len(set(row["measure_id"] for row in obs)),
        "snp_2025q3_sum_usd_billions": round(components, 2),
        "snp_2025q3_reported_usd_billions": reported,
        "note": "Only internal invariants and published figure arithmetic are checked, "
                "NOT original microdata reconstructions or causal validity.",
    }, indent=2))


def fetch_fred(series: str, output_dir: Path, from_date: str) -> None:
    if series not in FRED_ALLOWLIST:
        raise AuditError(f"FRED series not allowlisted: {series}")
    if len(from_date) != 10 or from_date[4] != "-" or from_date[7] != "-":
        raise AuditError("from-date must be YYYY-MM-DD")
    url = "https://fred.stlouisfed.org/graph/fredgraph.csv?" + urlencode({
        "id": series, "cosd": from_date,
    })
    request = Request(url, headers={
        "User-Agent": "GreatDecoupling-R3-evidence-audit/1.0",
    })
    with urlopen(request, timeout=30) as response:
        body = response.read(10_000_001)
    if len(body) > 10_000_000 or not body.startswith(b"DATE,"):
        raise AuditError(f"unexpected FRED CSV response for {series}")
    output_dir.mkdir(parents=True, exist_ok=True)
    # Deliberately refuse to overwrite; a refreshed series may have changed.
    target = output_dir / f"{series}.csv"
    with target.open("xb") as handle:
        handle.write(body)
    sha = hashlib.sha256(body).hexdigest()
    (output_dir / f"{series}.sha256").write_text(
        f"{sha}  {target.name}\n", encoding="utf-8"
    )
    print(json.dumps({
        "download": str(target), "series": series, "origin": url,
        "sha256": sha, "bytes": len(body),
        "warning": "Live latest-vintage FRED mirror, not an archived original "
                   "vintage or independent raw dataset reconstruction.",
    }, indent=2))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    subcommands = parser.add_subparsers(dest="command", required=True)
    subcommands.add_parser("validate", help="Validate checked-in published-value seed")
    fred = subcommands.add_parser("fred", help="OPTIONAL: fetch latest FRED CSV to output folder")
    fred.add_argument("--series", choices=sorted(FRED_ALLOWLIST), required=True)
    fred.add_argument("--output-dir", type=Path, required=True)
    fred.add_argument("--from-date", default="1989-01-01")
    args = parser.parse_args()
    try:
        if args.command == "validate":
            validate()
        else:
            fetch_fred(args.series, args.output_dir, args.from_date)
    except (AuditError, OSError) as error:
        parser.exit(1, f"R3 audit failed: {error}\n")


if __name__ == "__main__":
    main()
