# R3 independent inventory — Distribution and Surplus Capture

**Core question:** Where did economic surplus flow if not to typical workers?  
**Status:** **NOT REVIEWED / source candidates only**, despite selected publisher spot-checks documented separately in [source-audit.md](../source-audit.md).  
**Owner / last audit:** Unassigned / 2026-10-24. **Scope #1:** UNRESOLVED. **Terminology #2:** UNRESOLVED for income-tier units.

P-D (7 pages) is a **secondary and partly causal narrative**: it cannot substitute for primary NIPA/CBO/Fed/IRS/BLS/S&P series. P-M adds income-group definitions; P-E short-run Gini context. No causal conclusions carried forward.

| Source ID | Candidate original publisher / direct entry | Observable required | Legacy lead | Review disposition; retrieval |
| --- | --- | --- | --- | --- |
| R3-S001 | [BEA NIPA / industry accounts](https://www.bea.gov/data) | Labor/capital shares, self-employed/proprietor allocation | P-D p. 1 / [Aum & Shin 2020](https://www.stlouisfed.org/publications/review/2020/10/22/why-is-the-labor-share-declining) (secondary paper) | **not reviewed**; locate exact BEA line, vintage and method. |
| R3-S002 | [CBO income distribution](https://www.cbo.gov/topics/income-distribution) | Before/after-tax income distribution and government transfers | P-D pp. 1, 5 | **not reviewed**; exact distribution tables, tax unit, date and deflator. |
| R3-S003 | [Fed Distributional Financial Accounts](https://www.federalreserve.gov/releases/z1/dataviz/dfa/) | Stocks and wealth by household group | P-D p. 3 | **not reviewed**; equity definition, top shares and vintage. |
| R3-S004 | [EPI CEO pay](https://www.epi.org/publication/ceo-pay/) | CEO vs typical worker compensation / stock-option treatment | P-D p. 2 | **not reviewed**; secondary methodology, raw firm sample and exact edition. |
| R3-S005 | [BLS Union Membership](https://www.bls.gov/news.release/union2.toc.htm) | Union membership density / earnings, time and sector | P-D p. 4 / [2024 archived BLS Table 2](https://www.bls.gov/news.release/archives/union2_01282025.htm) | **not reviewed for series**; original annual tables, historical breaks and wage-composition caveat. |
| R3-S006 | [IRS SOI](https://www.irs.gov/statistics) / [Tax Policy Center historical tables](https://www.taxpolicycenter.org/statistics) | Statutory vs effective tax rates and policy effective dates | P-D p. 5 | **not reviewed**; original tax-year schedules and noncomparable policy bases. |
| R3-S007 | [S&P DJI Indices](https://www.spglobal.com/spdji/en/research-insights/) | Stock buyback totals, capex, dividends | P-D p. 3 | **not reviewed**; underlying licensed index data, file rights, dollar basis. |
| R3-S008 | [Census Income in the United States 2022](https://www.census.gov/library/publications/2023/demo/p60-279.html) | Pretax household money-income Gini | P-E p. 3 | **not reviewed for R3 series**; different population from CBO/Fed WID. |

## Run-only review controls

- Definitions [R3-D...]: gross domestic income vs value added, proprietor income, wealth vs income, tax unit, capital gains, CEO realized pay, union coverage, taxes; **none adopted**.
- Evidence [R3-E...]: **zero complete reviewed multi-period R3 datasets**. Legacy PDF numbers individually triaged in [source-audit.md](../source-audit.md).
- Uncertainty [R3-U...]: vintage, proprietor imputation, tail modeling, compensation sample bias, CBO vs WID disagreement, stock distribution ownership, historical union sampling; **open**.
- Measurement change [R3-M...]: BEA revisions, CBO definitions, Fed DFA vs SCF breaks, CEO firm sample, index universe, tax-code effective dates; **open**.
- Contested [R3-C...]: alternative labor share denominators; CEO grant-vs-realized ratios; pretax vs after-tax top-income growth; buyback/capex boundary; **open, do not resolve**.
- Disallowed: infer a causal effect of tax reform/union change/buybacks on any observed series; equate top wealth share with top income share; copy a derivative chart under unknown licensing.
- Non-goals: no intent, conspiracy, moral attribution, or policy prescriptions.
