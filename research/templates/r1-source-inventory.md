# R1 independent inventory — Productivity and Compensation

**Core question:** What exactly decoupled from what, when, and under which definitions?  
**Status:** **NOT REVIEWED / source candidates only**; this is *not* a result.  
**Owner / last audit:** Unassigned / 2026-10-24. **Scope #1:** UNRESOLVED. **Terminology #2:** UNRESOLVED where typical worker applies.

The existing PDFs contain **no usable productivity-vs-median-total-compensation aligned time series**. P-E pp. 2–3 has short-run wage / CPI leads; P-D pp. 2–4 discusses decoupling without original productivity data. Do not copy their interpretations.

| Source ID | Proposed direct primary source / location | Observation & intended use | Originating PDF lead | Review / rights status | Required action |
| --- | --- | --- | --- | --- | --- |
| R1-S001 | [BLS Labor Productivity and Costs](https://www.bls.gov/productivity/) | Output per hour, business/nonfarm business sectors | **Missing** direct data in PDFs | **not reviewed**; rights unknown | Pin table, series IDs, vintage and output/hours definitions. |
| R1-S002 | [BLS Employment Cost Index / compensation](https://www.bls.gov/eci/) | Wages vs benefits and total hourly compensation | P-E wage reference is **not equivalent** | **not reviewed** | Check population, sector, employment weights and period. |
| R1-S003 | [Census CPS ASEC](https://www.census.gov/programs-surveys/cps.html) | Median earnings / worker universe | P-M definitions and P-E household data caution | **not reviewed** | Distinguish hourly/annual wage, workers/households and imputation. |
| R1-S004 | [BEA data and NIPA](https://www.bea.gov/data) | PCE deflator and compatible accounts context | P-E macro lead | **not reviewed** | Obtain actual series/revisions; no assumption of comparability. |
| R1-S005 | [BLS Consumer Price Index](https://www.bls.gov/cpi/) | CPI-U/CPI-U-RS deflator alternatives | P-E CPI section pp. 3–4 | **not reviewed** | Fix date, base and history; compare PCE separately. |

## Run-only definitions and review registers

- Definition IDs [R1-D...] to fill from [definitions.md](definitions.md): productivity/TFP; wage/benefits/median/mean; worker universe; hourly denominator; real deflator. **None selected**.
- Evidence rows [R1-E...] to fill from [evidence-review.md](evidence-review.md); currently **no verified R1 series**. P-E rates are audited separately in [source-audit.md](../source-audit.md).
- Uncertainty [R1-U...]: source-vintage breaks, overtime/hours, selection, CPI/PCE; currently **open**.
- Measurement-change [R1-M...]: vintage, rebasing, sample break; currently **open**.
- Contested findings [R1-C...]: breakpoint 1973 vs data-driven alternatives, benefits inclusion, productivity scope; **not adjudicated**.
- Disallowed comparison: BEA GDP-per-capita growth vs BLS output-per-hour and Census household median as if identical; mean nominal AHE versus real median total worker pay without units/deflator.
- Exclusions: causal explanation, household burden, R3 surplus allocation. Owner [#1](https://github.com/BenWassa/great-decoupling/issues/1) must choose geography/time horizon before final series.
