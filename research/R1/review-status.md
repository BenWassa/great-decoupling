# R1 research-plan evidence review and open gates

**As at 2026-10-24.** R1 independent and confined to `research/R1/`; shared issue #7 templates and R2/R3 files unchanged. #1/#2 remain pending.

| Research-plan requirement | Evidence completed | Status / unfinished check |
| --- | --- | --- |
| Major-sector labor productivity | BLS 1947–2025 Q1 primary snapshots, 2025 annual BLS release, TFP contrast | **Checked selected rows**, full timeseries export pending |
| Wage versus total compensation | BLS mean hourly total, CES cash hourly metadata, ECEC current benefit split | **Partial**: cash vs benefits **full historic series** not calculated |
| Median versus mean | CPS median weekly full-time vs BLS all-person mean, populations/denominators recorded | **Partial**: no harmonized median hourly total compensation |
| Deflator distinctions | Output IPDNBS, historical BLS CPI-RS real comp, BEA PCE Q1, raw CPI-U Q1 | **Computed Q1**; full annual grid pending online replay |
| Historical start sensitivity | 1973/1979/2000/2019 Q1-to-2025 Q1 reproducible data | **Computed**, not representative of all annual/end quarters |
| Alternative 1973 breakpoints | Prespecified descriptive 1-hinge BIC scan and 1973/79/90/2000/08 checks coded | **Not executed** on entire series; significance/robustness not established |
| Source audit | Annotated primary/secondary sources, URLs/dates, limitations, revision notes | **Checked** each linked page's substantive metadata; original XLSX datasets not directly archived |
| Counterevidence | Feldstein 2008; Stansbury/Summers 2017; Greenspon et al. 2021; EPI method | **Reviewed abstracts/method descriptions**, quantitative independent replication open |
| Nonfarm vs whole economy | Sector boundaries and denominator hazards documented | **Definitions checked**, no economy-wide constructed series |
| Gross versus net | Distinction explicit | **Not completed**, requires net measure + matched depreciation |
| Cross-country | OECD methods inspected | **Held** pending #1 |
| Uncertainty / rejected measures | `uncertainty.md` open questions, measurement changes, disallowed substitutions | **Documented** |
| No causal inference / Claim Ledger | No causal interpretation or shared synthesis included | **Met** |
| Hostile-reading completion gate | Source-by-source numeric history, benefits decomposition, robustness and model inference remain to be tested | **NOT MET**; do **not** close issue #8 as fully complete |

## What was directly verified

- Primary FRED display tables (BLS original series OPHNFB, COMPNFB, COMPRNFB, IPDNBS) checked at frozen first quarters 1973, 1979, 2000, 2010, 2019 and 2025.
- Primary BEA PCE and BLS CPI monthly Jan–Mar levels checked for 1973, 1979 and 2025; derived quarterly averages and ratios computed, without extrapolation.
- BLS 2026-09-03 productivity release provides independent rounded 2025 annual crosscheck.
- CPS BLS nominal vs real and full-time median weekly definitions checked against official annual source; 1979/2000/2019/2025 numbers checked.
- BLS handbook documents the R-CPI-U-RS history, benefit inclusion, and proprietor imputation; BLS notice documents missing CPI October 2025; ECEC original table documents wages/benefits in June 2026.
- All **numeric** claims are reproducible to rounded primary-source table values by the stdlib-only offline script.

## Validation run notes

The **frozen arithmetic** is deterministically recalculated in `exhibits/sensitivity-q1.csv`. Executable Python self-tests are supplied, but the network-isolated current research environment could not download complete source exports; consequently full-series/changepoint calculations are provided as *reproducible planned tests*, **not claimed as executed**. Users with an internet-connected Python 3 interpreter can run `python3 scripts/r1_analysis.py --full --out /tmp/r1-live` and record source hashes. Inputs may have changed due to the providers' revisions.

### Owner and #7 coordination

Use the `sources.csv` header as a proposed R1-compatible record rather than edit any shared blank template. Issue #7 can map `unit_population_price`, `measurement_change_log`, `uncertainty_or_dispute`, `review_state`, and `disallowed_comparison` to the common schema. R1 source records remain separate. Any future approved changes to #1/#2 should be recorded as later methodological decisions **not silently applied** to this evidence vintage.

No Claim Ledger, merged findings, public-facing narrative, R2/R3 work, or GH merge were created.