# R1 methods: reproducibility and statistical boundaries

## Data and time resolution

**Input anchors** are original BLS major-sector indexes distributed by FRED: [OPHNFB](https://fred.stlouisfed.org/data/OPHNFB), [COMPNFB](https://fred.stlouisfed.org/data/COMPNFB), [COMPRNFB](https://fred.stlouisfed.org/data/COMPRNFB), [IPDNBS](https://fred.stlouisfed.org/data/IPDNBS). BLS [2026-09-03 Table 2](https://www.bls.gov/news.release/prod2.t02.htm) crosschecks the latest annual levels. BEA PCEPI and BLS CPIAUCSL are monthly, averaged over three months in a quarter **only when all three months exist**. All BLS quarterly indexes are seasonally adjusted. The frozen extract in `exhibits/` uses **Q1** of each selected year for a clean reproducible, same-season anchor; it must not be described as a full-year comparison.

Reproducibility modes:

```sh
cd research/R1
python3 scripts/r1_analysis.py --offline --out exhibits/reproduced
python3 -m unittest discover -s scripts -p "test_*.py" -v
# Optional: internet-enabled full history, captures source CSVs, their SHA256 hashes,
# and writes diagnostics; do not treat a moving data vintage as frozen:
python3 scripts/r1_analysis.py --full --out exhibits/live
```

The script uses the Python standard library (no pip/API key). **Offline** runs from frozen original-source checkpoints and reproduces the Q1 exhibit. **Full** explicitly downloads the series CSV files from FRED into `<out>/raw/`, produces file hashes and full-series diagnostics, and requires a working network: it was **not run** in the restricted research environment. Re-run results can differ after BLS benchmark, seasonal, or CPI retroactive revisions. Record retrieval date, SHA hashes, and changed observations when rerunning.

## Transformations

Let `P_t` = OPHNFB, `N_t` = COMPNFB, `B_t` = COMPRNFB, `O_t` = IPDNBS, `C_t` = quarterly mean CPIAUCSL, `F_t` = quarterly mean PCEPI.

Four compensation lenses: `B_t` (BLS historical consumer deflator), `N_t / O_t` (matched output price), `N_t / C_t` (official CPI-U), `N_t / F_t` (PCE). Index scales cancel when comparing ratios of the *same series* across endpoints.

For any series `X`, base `b`, end `e`:
- Cumulative growth percentage: `100*(X_e/X_b - 1)`.
- Independently rebased level at time `t`: `100*(X_t/X_b)`.
- **Gap** in cumulative percentage points: `100*(P_e/P_b - X_e/X_b)`. Percentage-point gap is **not** an estimated value of foregone wages.
- Annualized log growth: `100*ln(X_e/X_b)/(elapsed years)`; annualized growth difference requires explicit units.

**Validate with published BLS real compensation** but do **not** set `COMPRNFB == COMPNFB/CPIAUCSL`: BLS historical real compensation uses R-CPI-U-RS for the older segment. Avoid nominal index-level comparisons between BLS and BEA except through relative-change ratios. Numerators/denominators for product-price and consumer-price adjusted comparisons remain **the same nominal average compensation**.

## Mean–median and benefits

- The principal matched-sector calculation measures **average employer cost per hour**, not the median employee's wage.
- Report BLS CPS median usual **weekly** earnings as a *parallel observation only*. It reflects full-time employment selection, changes in composition, and excludes benefits. No composite ‘median total compensation’ has been calculated by multiplying a CPS median by an ECEC benefits factor: that would be unverified.
- Cash-only earnings can be computed using CES AHETPI, *but* sector coverage, worker type and frequency differ. Exhibit separate and do not interpret the level difference as solely a benefit effect.
- The official ECEC June 2026 private-industry split is total $46.89/hour, wages/salaries $32.82 and benefits $14.07; this current cross section is not a longitudinal adjustment.

## Historical break tests: predeclared, not yet executed on full observations

An illustrative descriptive diagnostic works on **annual means of four complete quarterly BLS observations**, not annualized rates or interpolation; use years with complete observations and at least ten years on **both** sides of a break. For each price lens separately and each full historical span allowed by availability:

1. Construct `g_y = ln(P_y) - ln(X_y)`; shifts in index normalization affect only intercept.
2. Fit ordinary least squares `g_y = a + b*(year-first_year) + error` (no breakpoint).
3. For every admissible candidate `k`, fit **continuous** broken slope `g_y = a + b*t + d*max(0,year-k) + error`; report RSS, BIC `n*ln(RSS/n)+p*ln(n)` (p=2 baseline; p=3 hinged). Sort by BIC; compare specific 1973, 1979, 1990, 2000, 2008 **if admissible**.
4. Repeat by 1947/1973/1979/1990/2000 entry dates and with endpoints 2019/2025 where available; report every unavailable test as `NA`, not a zero gap.
5. Label any minimum-BIC candidate **descriptive fit only**. Serial correlation, multiple testing, data revisions, recession/sector composition effects, and endpoint dependence preclude conventional statistical-significance statements from these fits. A formal structural-break study would require covariance/inference design, model stability checks, and pre-specified sampling decisions.

1973's relevance as a **business-cycle endpoint** is documented by BLS, but this does not make it the econometrically best breakpoint for the pay/productivity gap. Neither decision #1 nor #2 is overridden.

## Source vetting and provenance

Inventory rows use project #7-compatible fields: source ID, title, primary status, original publisher URL/DOI, access date, coverage, unit, price, extraction, licensing, evidence state, methodological caveats and measurement-change log. Other streams and shared templates are **untouched**. Quoted older academic studies are used only to log *contested measurements*, not as substitute observations. OECD comparison is on hold until owner decision #1.

## Validation gates

- Positive levels and nonzero denominators; no silent infinite/missing results.
- Exact first-of-quarter dates for quarterly series and three **distinct** monthly observations per complete quarter.
- Never mix Q1 endpoints with annual-average claims.
- Historical published COMPRNFB and raw CPI calculation are *separate*.
- Frozen checkpoints and generated CSV checked against source tables; full series and changepoint choice remain open.
- Changes in base-year normalization do not change growth calculations.

See [uncertainty.md](uncertainty.md) for methodological disagreements and rejection reasons.