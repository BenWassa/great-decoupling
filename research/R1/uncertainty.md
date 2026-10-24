# R1 uncertainty, disagreements and rejected comparisons

Evidence statuses: **checked** = original table or agency methods independently opened; **calculated/checkpoint** = deterministic arithmetic from transcribed checkpoints; **not yet established** = requires new full-series extraction or validation. No claim adjudication.

## Disagreements explicitly retained

| ID | Measurement dispute | Evidence / what follows | Status and unresolved check |
| --- | --- | --- | --- |
| U01 | **Median vs mean.** | BLS mean nonfarm-business comp counts wage+benefit cost and imputed proprietor labor; CPS median full-time weekly earnings excludes employer benefit costs and differs by population and hours. | Both verified *as definitions*. Matched sector/median hourly **not computed**; do not claim differences are all wage inequality. |
| U02 | **CPI-U vs R-CPI-U-RS.** | The BLS historical real-compensation index uses CPI-U-RS in older periods; raw CPIAUCSL deflation is a separate sensitivity. See [BLS methods](https://www.bls.gov/opub/hom/msp/calculation.htm). | Verified. For 1973Q1–2025Q1, raw CPI-U-adjusted nominal compensation growth differs from BLS COMPRNFB; not a transcription error. |
| U03 | **CPI vs PCE vs output prices.** | Consumer purchase basket CPI/PCE and output price index IPDNBS differ. Output-matched real compensation has much stronger cumulative growth than BLS real compensation under older CPI-RS. | Q1 anchor calculations reproduced; full historical index and alternate PCE annual time paths pending full extraction. |
| U04 | **Gross vs net output/hour.** | Productivity OPHNFB is gross value-added output/hour; subtracting depreciation requires aligned BEA NIPA components and hours. | **Net series not constructed**. Reject applying an arbitrary depreciation haircut to gross productivity. |
| U05 | **Sector/personal denominator.** | Nonfarm-business hours of all persons differ from all employed persons and from private CES employees; proprietors' labor compensation estimated. | Sources checked. No sector-to-economy splice; compare only with explicit coverage changes. |
| U06 | **1973 breakpoint.** | BLS business-cycle charts use 1973 Q4 as cycle end; this is not a structural-break test for the pay-productivity gap. | Open: full-series hinge scans 1973, 1979, 1990, 2000, 2008 vs all admissible candidates, other endpoints, formal inference. |
| U07 | **Historical price-series revisions.** | BLS says CPI-U-RS methods are approximate and historical adjustments incomplete; website reports an incorrect 2026-03-31 R-CPI-U-RS file corrected after April 1. | Original [CPI notice](https://www.bls.gov/cpi/research-series/r-cpi-u-rs-home.htm) checked. Do not use unversioned saved R-CPI-U-RS downloads blindly. |
| U08 | **Oct 2025 CPI missing observation.** | Original [BLS special notice](https://www.bls.gov/productivity/notices/2026/productivity-program-treatment-of-missing-october-2025-source-data.htm) explicitly discusses BLS estimation for 2025Q4. Published CPIAUCSL source displays "." for October 2025. | Full-series script excludes incomplete quarter rather than manufacture Oct price. BLS published COMPRNFB 2025Q4 remains a distinct official measure. |
| U09 | **Revision vintage.** | BLS 2025 preliminary annual OP index 118.1 became 117.8 by Sep 3, 2026; historical tables also revise earlier levels on 2017-base rebenchmarking. | Checked from [March release](https://www.bls.gov/news.release/archives/prod2_03052026.htm) and [September release](https://www.bls.gov/news.release/prod2.t02.htm). No splice across vintages. |
| U10 | **Benefits not constant across time.** | June 2026 ECEC private compensation is $46.89, split $32.82 salary/wages and $14.07 benefits. | A one-quarter aggregate share cannot be back-applied to 1973 or to the CPS median. |
| U11 | **Cyclical endpoint bias.** | 1973Q1, 1979Q1, 2000Q1, 2019Q1, 2025Q1 are anchors only; pre- and post-recession, pandemic employment composition vary. | Q1 sensitivities calculated; yearly-mean vs Q4 vs business-cycle endpoints not all run. |
| U12 | **Cross-national scope.** | OECD producer-deflated compensation/hour uses employee-hour and national-account conventions unlike all-person BLS US nonfarm. | Method read; cross-country numeric exhibits explicitly held pending #1. |

## Counterevidence and incompatible interpretations

1. **Martin Feldstein, 2008** ([NBER 13953](https://www.nber.org/papers/w13953)): emphasized near-matching *average* compensation and productivity growth over **1970–2006** with a common output deflator. Our matched-output-price **mean** measure is the appropriate conceptual sensitivity, not grounds for dismissing the CPI-adjusted *consumption wage* or median-worker question.
2. **Anna Stansbury and Lawrence Summers, 2017** ([NBER 24165](https://www.nber.org/papers/w24165)): reported strong positive correlations in *growth* of pay and productivity even while discussing divergence in cumulative *levels*. Such linkage and divergence are not mutually exclusive; neither is a causal identification.
3. **Greenspon, Stansbury and Summers, 2021** ([NBER 29548](https://www.nber.org/papers/w29548)): preserved large price-deflator and country-scope sensitivity; producer/consumer and mean/median comparisons change the outcome. Numbers require independent re-extraction before reuse as original calculations.
4. **Economic Policy Institute, 2015** ([working paper](https://www.epi.org/publication/understanding-the-historic-divergence-between-productivity-and-a-typical-workers-pay-why-it-matters-and-why-its-real/)): median compensation is a constructed distributional series, with nonfarm adjustment, net-productivity adjustment and deflator methodology. It cannot be treated as official BLS aggregate compensation or primary statistical data. EPI’s causal assertions are **not adopted** here.

## Rejected or withheld as direct evidence

- **Reject:** Comparing nominal compensation index growth to real output per hour (different inflation treatment).
- **Reject:** Calling COMPRNFB the median wage or CPS weekly median an all-worker hourly benefit-inclusive measure.
- **Reject:** Estimating a historical median compensation series using a uniform ECEC benefit fraction.
- **Reject:** Using TFP in place of labor productivity as an identical output-hour comparator.
- **Reject:** Describing output-price real compensation as *consumer purchasing power*.
- **Reject:** Using **1973** as a prespecified statistically proven changepoint, or claiming a breakpoint without full observations/model validation.
- **Reject:** Interpolating raw missing October 2025 CPI data without publishing an imputation rule, uncertainty, and vintage.
- **Withhold:** Full net/gross sensitivity until BEA depreciation treatment harmonized.
- **Withhold:** OECD cross-country numerical estimates until owner scope decision #1.
- **Withhold:** Long-run official median **hourly total compensation** until a defensible constructed distributional microdata method is reviewed.

## Measurement change log / subsequent work

| Recorded | Series | Change / issue | Action |
| --- | --- | --- | --- |
| 2026-10-24 | BLS historical prices | R-CPI-U-RS vs CPI-U and 2026 source corrections | Keep both separate; archive vintage before extending |
| 2026-10-24 | BLS 2025 annual | March preliminary vs September revised indexes differ | Use Sep vintage for crosscheck; no mixing |
| 2026-10-24 | Raw CPI Oct 2025 | No value in CPIAUCSL; BLS modeled estimate | Missing in raw path; exclude affected quarter |
| 2026-10-24 | FRED BLS underlying data | OPHNFB metadata update differs from Sep COMPNFB/COMPRNFB | Cite original series update dates; record downloads and hashes in full run |
| 2026-10-24 | Concepts | Net productivity, median total hourly comp not built | Document unresolved; no surrogate claim |

**Review standard:** distinct published methods are not errors; disagreements stay unresolved until measurement harmonization or supporting microdata review.