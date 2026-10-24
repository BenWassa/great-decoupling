# R2 — Household costs, affordability, and financial resilience

**Research-only evidence pack · snapshot 2026-10-24 · issue #9 · independent of R1 and R3**

## Navigation

- [Evidence pack](evidence-pack.md): descriptive observations, comparisons, disagreements, exclusions, and follow-up tests.
- [Source inventory](source-inventory.csv): source-level audit records with direct primary URLs, vintages, units, extraction routes, uncertainty and prohibited comparisons.
- [Definitions and methods](definitions-methods.md): worker/earner/family/household/consumer unit crosswalk; sampling, deflators, estimands, historical constraints and scenario formulas.
- [Measurement and uncertainty register](measurement-uncertainty.md): breaks, sampling and construct uncertainty, rejected or unresolved interpretations.
- [Data extract](data/observations.csv): small **transcribed, provenance-linked benchmark extract**, not a harmonized panel or a microdata sample.
- [Scenarios](data/scenarios.csv): separately flagged *illustrative input assumptions*, not observed national costs.
- [Calculator](reproduce.py): Python 3 standard-library computation; [unit tests](test_reproduce.py).
- [Reproducible exhibits](exhibits.md): frozen calculations traceable to the two input CSV files.

## Reproduction

From the repository root:

    python3 research/R2/reproduce.py
    python3 -m unittest discover -s research/R2 -p 'test_*.py' -v
    python3 research/R2/reproduce.py --check

The script reads only checked-in CSVs, uses no network or third-party packages, emits all numeric exhibits to stdout and, under --check, compares generated output byte-for-byte to exhibits.md. To refresh after deliberate data review, run with --write, inspect changes, and retain the cited source vintage.

## Scope and gates

This package holds multiple measures side-by-side rather than naming a single representative middle-class household. Geography is **US primary-data exploratory**, not a decision for the full project. Earliest available ranges vary substantially by series. No imposed 1973 starting year or changepoint. Owner decisions [#1](https://github.com/BenWassa/great-decoupling/issues/1) (geography/time) and [#2](https://github.com/BenWassa/great-decoupling/issues/2) (middle-income definition) remain **pending**.

Do not treat modeled household examples as population incidence, infer a historical representative family from unrelated marginal medians, equate consumer units with Census households, or combine cash premium contributions with full employer premium as an additional household payment. Neither a causal account nor a Claim Ledger is present. No conclusion about direction of an overall affordability index is made.

## Source-audit coordination

Issue [#7](https://github.com/BenWassa/great-decoupling/issues/7) owns the shared templates, **not this branch**. The per-run CSV includes that issue's requested attributes (publisher, provenance, geography, population/unit, measurement, denominator, price basis, vintage, extraction, uncertainty, comparability, status, rights). Its final template can be mapped into this workspace later without modifying shared files. Every path in this PR must begin with research/R2/.

## Audit state

Primary publisher pages were inspected on 2026-10-24; a limited number of point observations were transcribed and checked against direct tables. These are **reviewed at the displayed-table level**, not independently replicated from confidential survey microdata. Sources without transcribed numbers remain **identified, not fully extracted**. In particular, complete longitudinal ACS, CE, NCES and CMS panels, matched longitudinal samples, and measured local childcare budgets remain further-work items. See evidence-pack.md for the distinction.

## Licensing

Numerical excerpts and original paraphrases are included with attribution. US-government datasets are generally public-domain works; individual hosted data, KFF survey material, and Federal Reserve Bank presentation can have distinct terms. Do not mirror third-party PDFs or redistribute an entire series without reviewing its terms.
