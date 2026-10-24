# Definitions, estimands and methods (R2)

**Status:** exploratory multi-definition research; owner choices #1–#2 unapproved.

## 1. Statistical units (not interchangeable)

| Unit | Meaning | Examples | Forbidden shortcut |
| --- | --- | --- | --- |
| Worker | Individual who performed work; may be part-time, part-year, or self-employed depending on survey | CPS earnings, BLS worker | Not a household or full-time annual salary |
| Earner | Person receiving labor earnings in a period, including some people not currently employed | One-/two-earner constructed examples | Not equivalent to number of employed adults or incomes |
| Family | Census: two or more persons living together related by birth, marriage or adoption; other surveys may differ | Family health plan; SIPP childcare families | Not necessarily all household members; family health plan may include several people |
| Household | All persons occupying one housing unit; family and nonfamily households | CPS ASEC household median; ACS B19013 | Not identical to a family, wage, or average consumer unit |
| Consumer unit (CU) | BLS CE spending decision unit: people related or pooling major living expenses under its CU rules | CE 2024 mean spending | Not a household; CE mean income is not Census median household income |
| Adult respondent | Sampled person age 18+ in Federal Reserve SHED | 400-dollar emergency response | Not a count of distressed households |
| Housing unit | Occupied renter or owner unit; ACS B25064 uses *cash-rent* renter-occupied units | Median gross rent | Not equivalent to income median of tenant households |
| Institution/student | NCES IPEDS reporting institutions, weighted by full-time-equivalent enrollment in Digest | Tuition/fees | Sticker price is not student net price or debt |
| Enrolled covered worker | Employee enrolled in employer plan, not all workers | KFF EHBS contribution | Not population healthcare expenses |

### Middle-income alternatives left open

- M1: median Census money-income household (includes transfers as defined; before taxes; no in-kind benefits).
- M2: households in a **stated** relative band of size-adjusted disposable income; thresholds and equivalence scale **not approved**.
- M3: full-time year-round individual labor earnings; only valid for individual wage comparisons, not direct replacement for household cash.
- M4: income-quintile CE consumer units (mean within quintile; CU family/earner mix changes).
- M5: fixed-type exemplars (e.g., two adults with young child, one earner vs two) with synthetic income and expenditure inputs; **no claim of typicality**.

## 2. What each statistic estimates

- *Median* is an order statistic. Median rent divided by median total household income is **not** the median of tenant rent-to-income ratios. Numerators and denominators are from different populations even within ACS. Genuine renter burden requires matched responses / ACS B25070.
- *Mean* BLS spending of all CUs is weighted across ages, renters, owners, earners, and families. Do not divide the mean by a Census median, label a resulting number as a budget, or infer expenditure share for a typical household.
- A price-to-income *exposure index* may divide the quarterly **median new-home sale price** by annual CPS median household money income. This is a deliberately mixed-population, mixed-frequency index: not a mortgage-payment burden, not the median house price of all transactions, not an approved affordability estimate. Q1 observation is used, not a hypothetical annual median.
- EHBS total family premium = employer contribution + employee contribution, rounded. Only the **worker contribution** is a direct wage-deduction cash outflow in household stress tests; the full premium is a separate resource-cost lens, not a second cash expense. Coverage excludes people without that job/plan.
- CMS National Health Expenditure Accounts spending is **system-wide payer outlay**; it is not the sum paid by a representative family. CE healthcare is consumer-unit spending according to CE scope; OOP CMS is payer classification. They cannot be added.
- NCES Digest tuition and fees are *average institutional charges*, enrollment-weighted as specified; IPEDS net price, residency-specific charges and Title IV borrowing differ. Historical classification and student mix vary.
- SHED hypothetical 400-dollar response is *adult survey self-report* about one hypothetical shock and payment mechanism. The complement includes people who would borrow despite available savings; not synonymous with inability to afford an expense.
- ATUS diaries measure primary versus secondary care separately. Household joint schedules and time under constraints are not identified from aggregate person averages.

## 3. Price, calendar, geography and survey treatment

- CSV observation amounts are **nominal source-year USD** unless explicitly tagged constant-2011-USD (SIPP). Ratios within each nominal observation year need no deflator. Do **not** compare nominal dollar levels across 1984 and 2026 as real purchasing power.
- Candidate inflation comparators (not selected): CPI-U (urban household consumption), CPI-U-RS (research-series changes), PCE (national accounts), and category-specific CPI. Differences affect level comparisons. Recalculate all data in a single selected base year rather than multiply by an undocumented factor. NCES publishes its own constant-dollar figures using its documented deflator.
- 2025 CPS ASEC report (published Sep 2026) **revised prior-year levels** from earlier vintages. Specifically 2024 real income was restated in the 2025 report; do not mix the 2024 report's figure with a new-vintage ratio and call it a revision-free trend.
- ACS B19013 is in the survey year's inflation-adjusted reference dollars; within the single 2024 cross-section the value represents a current-year amount. The 2024 ACS estimate ($81,604) is **not** the 2024 CPS ASEC estimate ($85,210 revised vintage). They have different methodologies, timing, weighting and income constructs.
- Geographic spread: national all-household medians suppress metro, state, urban/rural, and tenure heterogeneity. Reproduce ACS B19013/B25064/B25070 by metro or state in a *single release* and maintain margin of error. ACS one-year estimates should not be silently mixed with five-year estimates.
- 1984 CPS/Q1 home price exposure uses quarterly new-home sale transactions vs annual all-household median earnings **only as an illustration of series alignment**. It is not regional household capability.

## 4. Cash flow scenario specification

Constructed example inputs are recorded in data/scenarios.csv. Each row is a **counterfactual** annual calendar-year household budget in 2026 nominal USD. Household type remains two adults and one preschool-aged child (except a no-child sensitivity row where explicitly specified), but the **number of earners and healthcare coverage assumptions vary**.

Terms:

- G = earner 1 gross annual wages + earner 2 gross annual wages.
- T = effective composite deduction fraction × G. This is **scenario assumption** (approximate aggregate income/payroll taxes; may be wrong given filing status, location and credits), not tax code execution.
- H = annual cash housing payments (12 × monthly rent incl. assumed utilities where noted).
- P = direct *worker* annual insurance premium contribution; 2026 KFF family-average $7,471 is a reference input for covered workers only.
- C = monthly out-of-pocket paid childcare × 12; synthetic value, not an observed sector average. C=0 does not imply unpaid care has no time cost.
- O = monthly other essential expenditures × 12; synthetic pooled transport, food, utilities if not bundled, and recurrent out-of-pocket health; mutually exclusive from rent and premium by construction.
- D = other committed annual debt/student payments; illustrative.
- Disposable cash after selected commitments B = G − T − H − P − C − O − D.
- Shock reserve R = initial liquid savings; one-off shock S at year-end; uncovered shock = max(0,S−max(0,R+B)); if B<0 the household has a baseline deficit even without shock.
- A three-month lost-earner stress reduces G by 3/12 of that earner's gross and reduces assumed tax withholding proportionately. Housing, childcare, insurance, O and debt remain fixed as a **conservative static-cost case**. It does **not** model benefit loss, unemployment insurance, taxes recalculated on real brackets, employment recovery, or childcare substitution. A second variant may turn off childcare explicitly and is labelled.

The central test compares single-earner gross $60k and dual-earner $60k+$40k, **not** household median income. We report a lower/higher rent, care, tax and medical-shock grid, and loss of each earner to expose model dependence. Do not infer which family structure fares better empirically without matched representative data.

## 5. Reproduction and integrity

Python script uses Decimal for cent accounting; percentages rounded only for display. No stochastic estimation and no missing-year interpolation. The CSV fields contain source identifier, unit, year, nominal/constant basis, source locator, scope and extracted statistic. The script explicitly validates required observations and rejects duplicate keys, negative spending inputs, fractional earned-count inconsistencies, and missing input columns. Fixed external citations make the snapshot auditable, but changes at publishers' tables may occur after this retrieval date.

**Evidence labels:** reviewed = checked displayed original table/report; identified = source available but no entire microdata/longitudinal extraction; contested = cannot directly compare or measurement discrepancy; modeled = arithmetic using stated user-defined assumptions. These are *not* statistical confidence probabilities.
