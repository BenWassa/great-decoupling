# Validation and reproducibility status — 2026-10-24

## Procedure
Run from repository root:
- python3 research/R3/reproduce.py validate
- python3 research/R3/reproduce.py fred --series WFRBST01134 --output-dir /tmp/r3-fred --from-date 1989-01-01
- python3 research/R3/reproduce.py --help

The first command uses only Python standard library, no credentials or network. It verifies CSV field completeness, unique observation keys, referential integrity against source inventory, finite numeric values, consistent denominators and units by measure/vintage, and gross S&P Q3 payout arithmetic. The second command is **optional**, requires network, fetches a FRED/Board redistributed CSV and records a SHA-256 hash; it does not alter frozen original observations in this repository. See code for errors/validation limits.

## What is validated
The report contains directly traceable **published** primary-source observations and distinct model and nongovernmental estimates. The data audit file is an **observation seed**, not comprehensive machine-ingested historical series. Simple arithmetic checks do not validate underlying proprietary or microdata collection. Distinct revisions and provisional model years are labelled.

## Not validated; not claimed as done
- Full downloadable BLS/BEA historical shares and decompositions, CBO historical supplemental workbook computation, weighted SCF implicate/replicate variance or person-level IRS SOI records.
- Original EDGAR firm-level census, gross/net SEC buyback reconciliation, current-vintage full Z.1 F.103 / F.223 transaction panels, primary-source state labor/tax law inventory.
- Independent statistical break search, hypothesis tests, causality, country peer harmonization or historical 1973 selection.
- Source refresh success from the restricted authoring environment or all future GitHub CI checks. No raw table downloads or reproducible upstream package lock have been stored. These are explicit blockers to an unqualified 'fully independently replicated' assessment.

## Reviewer gates
- Every source ID in the observation file must map to one inventory record; numeric observations require source URL, period and label of numerator, denominator, unit and vintage.
- Full-year, quarterly period, SAAR, stock and flow must not be summed or silently rebased.
- CBO household, IRS filing unit, BEA household equivalence, SEC company employee, CPS worker, Federal Reserve family and national corporate-business income must not be equated.
- Preliminary/nowcast and missing-survey-month or population-classification changes must remain visible.
- All changes remain exclusively under research/R3/ and must not decide issues #1 or #2 or write shared template documents of #7.

If future downloads change figures, retain the original observation and its dated vintage; add another row with the new vintage rather than overwriting history. Rights to redistribute S&P and scholarly authors' underlying tables must be checked first. 
