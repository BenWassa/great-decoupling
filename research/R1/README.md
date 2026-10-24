# R1 — Productivity and compensation: independent evidence pack

**Research run:** R1 only · **State:** research evidence / not a claim ledger · **Reviewed:** 2026-10-24 · **Owner issue:** [#8](https://github.com/BenWassa/great-decoupling/issues/8).

## Question and constraints

What diverged from what, when, and under which operational definitions? This is a **descriptive measurement audit** of U.S. labor productivity, hourly worker compensation, and earnings; it does not explain the causes of an observed difference, make policy recommendations, or join evidence from R2/R3.

Decision [#1](https://github.com/BenWassa/great-decoupling/issues/1) (geography, time coverage, preselected breakpoints) and [#2](https://github.com/BenWassa/great-decoupling/issues/2) (typical worker/middle class) are **pending**. U.S. calculations are exploratory, not an approval of U.S.-only scope; neither 1973 nor a single concept of middle class has been adopted.

## Index

| File | Purpose |
| --- | --- |
| [sources.csv](sources.csv) | Annotated, individually traceable source inventory; primary versus contextual sources, access, limitations, review state |
| [definitions.md](definitions.md) | Scope, statistical unit, compensation, productivity, deflators and exclusions |
| [methods.md](methods.md) | Transformations, alignment, validation, benchmark sensitivity and descriptive breakpoint method |
| [exhibits/observations-q1.csv](exhibits/observations-q1.csv) | Manually checked BLS/FRED quarterly anchor observations (2017=100, Q1 only) |
| [exhibits/price-checkpoints-q1.csv](exhibits/price-checkpoints-q1.csv) | January–March CPI-U and PCE indexes at verified anchors |
| [exhibits/sensitivity-q1.csv](exhibits/sensitivity-q1.csv) | Recalculated Q1-to-Q1 growth, including output-price, BLS historical real comp, raw CPI-U and PCE |
| [exhibits/README.md](exhibits/README.md) | Exhibit provenance, data quality checks, results and interpretation limits |
| [scripts/r1_analysis.py](scripts/r1_analysis.py) | Stdlib-only offline reproduction and optional online full-series extraction, annual aggregation and break diagnostics |
| [scripts/test_r1_analysis.py](scripts/test_r1_analysis.py) | Deterministic fixture, missingness and breakpoint tests |
| [uncertainty.md](uncertainty.md) | Active disagreements, counterevidence, revision risks, rejected comparisons and outstanding reviews |
| [review-status.md](review-status.md) | Research-plan coverage, completed verification and outstanding gates |

## Independently checked descriptive observations

All figures below are **Q1-to-Q1** and are based on the same five-decimal formulas applied to original BLS indices distributed by FRED; figures are rounded **only for display**. They are *not* annual averages, representative-worker inferences, or breakpoint tests. See exhibits for input values and calculation output.

- **1973 Q1 → 2025 Q1:** Nonfarm-business output/hour increased **151.1%**. BLS real hourly compensation (wages **plus** benefits, historical BLS consumer deflator) increased **62.3%**. Nominal hourly compensation deflated with the **nonfarm-business output price index** increased **120.8%**. Using the **BEA PCE price index** on the same nominal hourly compensation instead gives **91.6%**. These are four different series/price concepts; the percentage-point gaps to output/hour differ materially.
- **1979 Q1 → 2025 Q1:** Corresponding growth was **134.2%** for productivity, **55.2%** for BLS real compensation, **106.9%** for output-price-deflated compensation, and **78.9%** for PCE-deflated compensation.
- **2000 Q1 → 2025 Q1:** Productivity **63.1%**, BLS real compensation **24.2%**, output-price-deflated compensation **41.5%**.
- **2019 Q1 → 2025 Q1:** Productivity **13.5%**, BLS real compensation **5.9%**, output-price-deflated compensation **9.6%**.

These comparisons are *gross* nonfarm-business labor productivity against **mean** nonfarm-business hourly compensation, not **median** hourly compensation or net productivity. Historical BLS real compensation is **not** reproduced by mechanically dividing nominal compensation by published CPIAUCSL; its CPI-U-RS historical construction makes that an invalid equality test. BLS’s missing-October-2025 CPI notice is documented in [uncertainty.md](uncertainty.md).

### Wage / median countercheck (different units; not a gap estimate)

The official CPS median **usual weekly** real earnings for full-time wage-and-salary workers 16+ are 332 (1979), 334 (2000), 359 (2019), and 374 (2025), in **1982–84 CPI-adjusted dollars**. This is a *weekly median* of a different sample and excludes benefits; it must not be treated as the median hourly compensation of all nonfarm-business workers or subtracted from the productivity index. Original BLS CPS annual series: [LEU0252881600A](https://fred.stlouisfed.org/data/LEU0252881600A).

### Other inspected benchmarks, not converted to claims

BLS [2026 Q2 revised release, Table 2](https://www.bls.gov/news.release/prod2.t02.htm) gives **2025 annual** nonfarm-business indexes: labor productivity 117.8, nominal hourly compensation 144.6, BLS real hourly compensation 109.7, and output price deflator 127.2, all 2017=100. Its 2025 annual growth rates are 2.1%, 4.3%, and 1.6% for productivity, nominal compensation and real compensation. These are a **different aggregation** from the Q1 exhibit.

BLS [total factor productivity](https://www.bls.gov/news.release/prod3.htm) shows 2025 private nonfarm-business total factor productivity growth of 0.8% and labor productivity growth of 2.2%. TFP is not interchangeable with labor productivity and does not answer this R1 pay comparison directly.

## Coverage boundary

**Directly checked:** BLS/FRED historical quarterly series metadata and selected numeric observations (1947–2025), BLS’s published 2025 annual crosscheck, BEA PCE monthly data for selected periods, BLS CPS median usual weekly earnings, benefit coverage, BLS historical deflator methods, several opposing interpretations. **Reproducible, not fully executed here:** online fetch of entire series, full annual start-year grid, statistical changepoint diagnostics; the historical break year remains unestimated. No finding about the statistically preferred breakpoint is asserted.

For the explicit unresolved review gates and evidence status, see [review-status.md](review-status.md).