# Preliminary independent research gate review — 2026-10-24

**Issue:** [#11](https://github.com/BenWassa/great-decoupling/issues/11) · **Disposition:** **REVISE — research gate not passed** · **Status:** initial review, subject to revision after reproducibility CI and deeper source extraction.

This record does not replace the research plan's mandatory transition rule. **No Claim Ledger, long-form narrative, policy interpretation, explanatory synthesis, or published infographic** is authorized. Decisions [#1](https://github.com/BenWassa/great-decoupling/issues/1) and [#2](https://github.com/BenWassa/great-decoupling/issues/2) remain with the owner.

## Reviewed changes and integration

| Scope | PR and exact reviewed head | Status | Review finding |
| --- | --- | --- | --- |
| Legacy PDF audit and shared source-review forms (#6, #7) | [#21](https://github.com/BenWassa/great-decoupling/pull/21), `adb67aaff68980757bb90787980cf4ece8142b80` | **Merged**, issues #6–#7 closed | Documentation-only infrastructure accepted after spot-checks; not approval of legacy numeric claims |
| R1 productivity/pay (#8) | [#22](https://github.com/BenWassa/great-decoupling/pull/22), `c21ab70890059531f470ee1243904ee4ac3b5322` | Open draft, **revise** | Selected anchor series and method sensitivity useful; incomplete full historical/source validation |
| R2 household costs/resilience (#9) | [#24](https://github.com/BenWassa/great-decoupling/pull/24), `377e7424a77a801612f242d85d8e37abee8daaee` | Open, **revise** | Source and sample-scenario separation good; representative historical budget/region coverage incomplete |
| R3 distribution/institutions (#10) | [#23](https://github.com/BenWassa/great-decoupling/pull/23), `0058422aab2e36148782e2e84f3f32a1dfe32ab5` | Open draft, **revise** | Stock/flow definitions sound; historical source panels and distributional reconciliation incomplete |
| Offline reproducibility automation | [#25](https://github.com/BenWassa/great-decoupling/pull/25), merged on main | Installed, **runtime status unverified** | Matrix checks out three separate research branches and runs committed offline scripts; no success claim without workflow run logs |

All PRs #21–#24 changed only the assigned folders. No shared-file merge conflicts surfaced from changed-file lists. Each research PR is analytically independent of the others.

## Independent checks actually completed

1. **Audit inventory:** Re-parsed 62 dated M/D/E audit rows in `research/source-audit.md`: 11 **verified** *source-matches*, 39 **needs verification**, 12 **not usable**. Checked shared template coverage, restricted folder ownership, and internal documentation navigation. The word *verified* does **not** mean original-series statistical replication.
2. **Primary external spot-checks:** Directly consulted [Pew's 2024 middle-class report](https://www.pewresearch.org/race-and-ethnicity/2024/05/31/the-state-of-the-american-middle-class/), [Pew's 2022 calculator band](https://www.pewresearch.org/short-reads/2024/09/16/are-you-in-the-american-middle-class/), [Census 2022 income report](https://www.census.gov/library/publications/2023/demo/p60-279.html), [Federal Reserve PCE target](https://www.federalreserve.gov/economy-at-a-glance-inflation-pce.htm), and [St Louis Fed Aum/Shin labor share study](https://www.stlouisfed.org/publications/review/2020/10/22/why-is-the-labor-share-declining). These support selected definitions and the treatment of some legacy claims as invalid or contestable.
3. **R1 read-only check:** Parsed its 22-source CSV, eight Q1 productivity/compensation observations, three price-anchor rows, and 18 sensitivity comparisons without malformed CSV rows. Recomputed 14 independent mean-pay/deflator growth transformations: maximum absolute residual below 0.00001 percentage points. This tests **frozen arithmetic**, not original FRED vintage downloads or unexecuted break-inference code.
4. **R2 read-only check:** Parsed 21 source records, 51 observation rows, and five synthetic scenarios without CSV-shape errors; all observed source IDs exist, recorded values finite. Recomputed ACS 2024 matched U.S. renter burden = `(4,056,945+2,966,608+4,012,728+11,200,981)/(46,101,640−3,147,163)=22,237,262/42,954,477=51.77%`. This is gross-rent burden among **computable renter units**, not a population of all households. Original [KFF 2026 employer coverage survey](https://www.kff.org/health-costs/2026-employer-health-benefits-survey/) reports $28,303 total covered-family premium versus $7,471 worker contribution, separate accounting quantities.
5. **R3 read-only check:** Parsed 24 sources and 40 observation anchors with valid CSV shape, source-ID relationships, finite observations, and unique source/measure/period/vintage keys. Original [BLS September 2026 article](https://www.bls.gov/opub/ted/2026/labor-share-at-its-lowest-level-52-8-percent-in-second-quarter-2026.htm) gives 65.5% for 1947Q1 and 52.8% for 2026Q2 **nonfarm-business** labor share; [S&P Dow Jones Indices Q3 2025 release](https://www.spglobal.com/spdji/en/corporate-news/article/sp-500-q3-2025-buybacks-post-modest-62-gain-to-249-0-billion-after-declining-20-1-amidst-uncertainty-in-q2/) confirms $249.0bn repurchases + $168.1bn dividends = $417.1bn in that **index universe**.

These independent checks were implemented as *read-only source and CSV/arithmetic inspections*. **Python tests and complete source downloads were not executed by this reviewer.** The added workflow on main enables future independent execution; obtain linked successful run/job logs before converting any verification row into a CI-pass status. Actions activity may not be visible through the current connector's pull-request-only workflow listing; do not infer a pass or failure from a missing listing.

## Remaining gate blockers by run

| Run | Required before PASS under `research/researchplan.md` |
| --- | --- |
| **R1 — REVISE** | Run and inspect offline tests; reproduce archived complete historical BLS/BEA/FRED series with hashes; test alternate start periods/break candidates on full data; address historic wage versus total-benefit compensation, average versus median hourly compensation, net/gross measures, deflator and population sensitivity. Cross-country analysis only within owner-approved #1 scope. |
| **R2 — REVISE** | Run Python scenario/exhibit checks and tests; reconstruct additional internally matched historical cost and income panels (rather than mixing marginal medians), regional owner/renter and household-structure comparisons, childcare-survey break handling, alternative budgets, and uncertainty ranges. Five scenario budgets are **hypothetical**, not estimated representative families. |
| **R3 — REVISE** | Run offline source-ID/data validator; extract and archive continuous BLS/BEA/CBO/Fed data where relevant; reconcile self-employed labor in gross/net share denominators, tax/household income-ranking methods, survey wealth implicates, gross vs net corporate payout sources and original source vintages. Counterevidence disputes must stay visible; no surplus-capture causal claim. |

### Cross-run and technical blockers

- Owner decisions #1/#2 remain unapproved. Research alternatives may remain separate in evidence work but a final declared analytic scope needs those decisions.
- No CI jobs previously existed for research PRs. Workflow added by #25 requires **observed** completed runs; documentation is not a substitute.
- Original government/publisher source matching and selected arithmetic are **not** representative dataset reconstruction, independent microdata replication, or inferential confidence.
- Restrict PR edits to `research/R1/`, `research/R2/`, and `research/R3/` respectively. Shared templates are now on main from #21; map local formats into them, don't overwrite findings.
- Do **not** close #8, #9, #10, or #11 based on the current audit or on green offline fixtures alone.

## Sign-off rule and next review

Issue #11 remains **open / revise** until each run is independently checked against the research plan's “no major sources unreviewed / methods explicit / uncertainty documented / hostile reading” criteria. A second dated record should include exact successful workflow run links, downloaded-source hashes, validated disputed measures, exceptions, and a separate PASS or REVISE for each stream. **Only three PASS dispositions together authorize issue #12**. No reviewer sign-off of research completion is given in this preliminary report.
