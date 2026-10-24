# TEMPLATE — Run-specific source inventory / extraction card

**Run:** R1 | R2 | R3 (choose exactly one)  
**Research question:** [copy run question from researchplan.md]  
**Owner / reviewer:** [ ]  **Inventory updated UTC:** [YYYY-MM-DDTHH:MM:SSZ]  
**Scope (geography/time; issue #1):** UNRESOLVED  
**Target definition (issue #2):** UNRESOLVED where applicable

> One source-series-vintage per card. A linked PDF summary is not the underlying source. Clone this file into a run workspace; never put R1, R2 and R3 observations on the same sheet.

## A. Source identity and access

| Field | Required input |
| --- | --- |
| Source ID | Rn-S000 |
| Originating lead, if any | Legacy PDF ID and p. / source list; or direct discovery |
| Full title; table/series/variable ID | [ ] |
| Publisher / dataset steward; named author | [ ] |
| Source classification | Primary original record / peer-reviewed secondary analysis / secondary report / tertiary |
| Publication date; dataset release/vintage | [YYYY-MM-DD] / [ ] |
| Revision / replacement date and status | [ ] |
| Stable direct URL; DOI; archived permalink | [ ]; never cite a mutable landing page alone |
| Access/retrieval date (UTC) | [ ] |
| License / copyright / permitted reuse / citation requirements | [ ] or UNKNOWN; no auto-approval |
| Original file path, hash, or archive reference | [ ] |
| Review disposition; reviewer/date | not reviewed / reviewed / corroborated / contested / rejected; [ ] |

## B. Observable / definition contract

| Field | Required input |
| --- | --- |
| Named variable and exact definition | [ ] |
| Unit of observation / statistical unit | Worker / job / hour / person / tax unit / family / household / firm / area / period; be exact |
| Denominator and numerator | [ ]; include age, working status and exclusions |
| Geography and coverage; weights / frame | [ ] |
| Sample/population and collection method | [ ] |
| Measure units | Dollars, dollars/hour, %, p.p., index (base year), share of which income |
| Nominal or real, currency/dollar base year | [ ] |
| Deflator and index vintage (CPI-U / CPI-U-RS / PCE / other) | [ ] |
| Household equivalence / local cost adjustment | [ ] or N/A |
| Wage/compensation inclusions: benefits, bonuses, hours | [ ] or N/A |
| Survey vs administrative / seasonally adjusted | [ ] |
| Start/end and period frequency | [ ] |
| Known series revisions / benchmark changes | [ ] / measurement-change ID |
| Contested definitions and comparability limits | [ ] |
| Disallowed comparisons / proxy restrictions | [ ] |

## C. Extraction and transformation audit

| Field | Required input |
| --- | --- |
| Raw file, table number, cells, query/API endpoint, page or figure | [ ] |
| Retrieval command, script, manual steps, or screenshot locator | [ ] |
| Sampling filters, missing-period treatment, deduplication | [ ] |
| Units conversion, rebasing, deflation, weighting, transforms | [ ] |
| Formulas and rounding; raw/processed checksum | [ ] |
| Reviewer reproduction / reconciliation date | [ ] |
| Observations and evidence-review IDs | [Rn-E...] |
| Measurement-change log IDs | [Rn-M...] |
| Alternative legitimate method / sensitivity needed | [ ] |
| Known disagreements / linked contested-finding IDs | [Rn-C...] |

## D. Open items / release control

- Missing original primary table / technical note: [ ] — retrieve by [owner/date].
- Data rights unknown / re-use restriction: [ ] — verify with [publisher/owner].
- Incompatible observation unit or series splice: [ ] — **do not compare**.
- Quality/provisional flag and why: [ ].
- Decision dependencies: #1 geography/time; #2 middle-class/worker-household definitions; other [ ].
- Decision or observation **not** authorized by this form: [ ].
