# R1 source-anchored, reproducible exhibits (2026-10-24 checkpoint)

The `*-q1.csv` files are **frozen transcriptions from official underlying source tables** plus computed arithmetic, **not** downloadable complete historical series, annual averages, or a changepoint study. Observations are quarterly **seasonally adjusted first quarters (Q1)** and source indexes are rounded by the data provider to three decimals. The source series in FRED reproduce original BLS/BEA publications and credit the respective primary statistical agency; the FRED web view is a distribution channel.

## Table E1: source quarterly indexes

`observations-q1.csv`, from the quarterly FRED original-series data displays:

| Index | Meaning | Source URL |
| --- | --- | --- |
| OPHNFB | Nonfarm business labor productivity (output/hour, 2017=100) | https://fred.stlouisfed.org/data/OPHNFB |
| COMPNFB | Mean **nominal total compensation** / all-person hour, 2017=100 | https://fred.stlouisfed.org/data/COMPNFB |
| COMPRNFB | Official BLS mean **real total compensation**/all-person hour, historical consumer-deflated, 2017=100 | https://fred.stlouisfed.org/data/COMPRNFB |
| IPDNBS | BLS nonfarm business output price deflator, 2017=100 | https://fred.stlouisfed.org/data/IPDNBS |

Anchors: 1947, 1973, 1979, 1990, 2000, 2010, 2019 and 2025, *Q1 only*. Source values independently checked in original page display. No interpolation/annualizing. All source series cover at least the indicated anchors.

## Table E2: additional price checkpoints

`price-checkpoints-q1.csv` stores **original monthly seasonally adjusted indices** and separately the arithmetic `mean(January, February, March)` for each of **1973, 1979, 2025**. BEA [PCEPI](https://fred.stlouisfed.org/data/PCEPI), 2017=100; BLS [CPIAUCSL](https://fred.stlouisfed.org/data/CPIAUCSL), 1982–84=100. The different base-year scales cancel in **ratio-of-ratios**, so they are never compared at face value. The frozen sample *does not* cover 1990, 2000, 2010, or 2019 monthly price checkpoints: a PCE/CPI estimate for those base years therefore does **not** appear in E3.

## Table E3: price-definition and beginning-year sensitivity

`sensitivity-q1.csv` uses **2025Q1 as common end**, every historical E1 Q1 start, and only those price concepts with valid start and end observations. The output-price and published real BLS comparisons have **1947** coverage; the PCE and CPI raw comparisons are supported by **1973** and **1979** frozen price checkpoints only. Missing cells are **not inferred**.

```text
Prod growth = 100 * (OPHNFB_end / OPHNFB_start − 1)
BLS real compensation growth = 100 * (COMPRNFB_end / COMPRNFB_start − 1)
Output-price real comp growth = 100 * ((COMPNFB_end/IPDNBS_end) / (COMPNFB_start/IPDNBS_start) − 1)
PCE real comp growth = 100 * ((COMPNFB_end/PCEPI_Q1_mean_end) / (COMPNFB_start/PCEPI_Q1_mean_start) − 1)
Raw CPI real comp growth = same as PCE expression, substituting CPIAUCSL_Q1_mean
Cumulative growth difference (percentage points) = productivity growth − compensation growth
```

**Numerical checkpoints (growth 2025Q1 vs respective start; rounded only for display):**

| Start | Productivity | BLS historical consumer-real mean comp | Output-price real mean comp | PCE-real mean comp | Raw CPI-real mean comp |
| --- | ---: | ---: | ---: | ---: | ---: |
| 1973Q1 | 151.10% | 62.27% | 120.83% | 91.55% | 48.60% |
| 1979Q1 | 134.18% | 55.15% | 106.90% | 78.85% | 44.04% |
| 2000Q1 | 63.13% | 24.18% | 41.51% | n/a (monthly checkpoint not frozen) | n/a (monthly checkpoint not frozen) |
| 2019Q1 | 13.53% | 5.91% | 9.64% | n/a (monthly checkpoint not frozen) | n/a (monthly checkpoint not frozen) |

The **difference is a difference in cumulative index growth**, not a dollar-value transfer nor a share of gross domestic income. BLS historical real compensation **does not equal** COMP / raw published CPI-U historically because BLS used research-retroactive CPI-U-RS.

## Offline verification

```sh
cd research/R1
python3 scripts/r1_analysis.py --offline --out /tmp/r1-q1
python3 -m unittest discover -s scripts -p "test_*.py" -v
```

`--offline` validates and independently reproduces E3 from E1 + E2. The online `--full` mode downloads complete current source-series data with SHA-256 for reproducibility and conducts **descriptive**, **not inferential**, sensitivity/breakpoint diagnostic scans. The full-mode outputs have **not** been generated for the present evidence vintage; no statistical breakpoint is asserted in this pack.

## Traceability and limitations

FRED third-party delivery pages embed the source agency on each series. The source list records exact URLs and agency. The frozen values are original statistical-agency measures but transcribed from FRED rather than archived source datasets; full reproducibility requires an explicit retrieval vintage and raw CSV hashes from `--full`.

- **Mean BLS comp includes benefits** and imputed labor-income component for the self-employed. It is not typical-worker wage.
- **Matching sector** for productivity and mean comp does not remove other differences between productivity and pay.
- The comparison **switches price concept**, not just a single statistical line. CPI/PCE-based consumer pay and IPDNBS-based “product wage” answer different price questions.
- No annual / within-year view can be inferred from isolated Q1 values. A 1973 break is deliberately **not preselected**.
- Official BLS published historical CPI-RS-adjusted COMPRNFB and raw CPI-U are intentionally separate methods.
