# R2 independent inventory — Household Costs and Viability

**Core question:** How did the cost structure of middle-class life change relative to wages?  
**Status:** **NOT REVIEWED / source candidates only**; no budgets or viability stress tests have been run.  
**Owner / last audit:** Unassigned / 2026-10-24. **Scope #1:** UNRESOLVED. **Terminology #2:** UNRESOLVED.

P-M provides **definitions**, not longitudinal costs. P-E offers a context-only inflation/household-income snapshot; it has no primary housing/childcare/healthcare/education/time-use cost data. Preserve household, family, individual and worker distinctions.

| Source ID | Proposed source (direct primary source where possible) | Measure / status | Legacy PDF lead | Required retrieval/uncertainty |
| --- | --- | --- | --- | --- |
| R2-S001 | [Census ACS](https://www.census.gov/programs-surveys/acs) / [CPS](https://www.census.gov/programs-surveys/cps.html) | Size-adjusted income & metro/housing cost; **not reviewed**, rights unknown | P-M p. 1–3; P-E p. 2 | Select year/population/metro; original microdata and weights. |
| R2-S002 | [Pew State of the American Middle Class 2024](https://www.pewresearch.org/race-and-ethnicity/2024/05/31/the-state-of-the-american-middle-class/) | **Secondary analysis** of CPS/ACS income bands; **not reviewed for R2 outcomes** | P-M pp. 1–4 | Reproduce definition and household size/cost adjustment before use. |
| R2-S003 | [Census American Housing Survey](https://www.census.gov/programs-surveys/ahs.html) | Ownership/rent/recurring housing cost; **not reviewed** | **Missing** | Confirm city samples, housing unit vs household and availability. |
| R2-S004 | [BLS Consumer Expenditure Surveys](https://www.bls.gov/cex/) | Budget shares, categories, household composition; **not reviewed** | **Missing** | Consistent expenditure unit & historical item breaks. |
| R2-S005 | [MEPS](https://meps.ahrq.gov/mepsweb/) / [KFF](https://www.kff.org/) | Premiums, cost-sharing, OOP; **not reviewed** | **Missing** | Define payer, covered population, plan type, after-tax cost. |
| R2-S006 | [NCES Digest](https://nces.ed.gov/programs/digest/) | Tuition/fees and population; **not reviewed** | **Missing** | Net vs sticker tuition, public/private, cohort/dollar basis. |
| R2-S007 | [BLS American Time Use Survey](https://www.bls.gov/tus/) | Paid work, childcare and household time; **not reviewed** | **Missing** | Survey-year comparability and one/two earner household definitions. |
| R2-S008 | [BLS CPI](https://www.bls.gov/cpi/) / [BEA PCE](https://www.bea.gov/data/consumer-spending/main) | Category price adjustment, **not budget share by itself**; **not reviewed** | P-E pp. 3–4 | Distinguish expenditure share from price change; basket shifts. |

## Run-only methods / open records

- Definitions [R2-D...]: household income, family structure, relative-vs-absolute bands, equivalized median, price-to-income ratio, fixed/discretionary spending; **none approved**.
- Evidence [R2-E...]: **zero verified R2 cost observations**; record eventual cells with [evidence-review.md](evidence-review.md).
- Uncertainty [R2-U...]: survey undercoverage, regional prices, tax/insurance transfers, missing child ages and pre-1970 series, no one-income test parameters; **open**.
- Measurement changes [R2-M...]: ACS/AHS/CEX item definitions, housing boundaries, deflator, household-size scale; **open**.
- Contested [R2-C...]: cost burden vs simple price/income, ownership vs renting, household-size changes; **open**.
- Disallowed: use “middle class” size-adjusted **people share** as a worker-wage level; infer housing affordability from national CPI alone.
- Non-goals: no social-change blame, individual psychological mechanism or causal attribution. Await [#1](https://github.com/BenWassa/great-decoupling/issues/1) and [#2](https://github.com/BenWassa/great-decoupling/issues/2).
