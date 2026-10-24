# Independent research run templates (pre–Claim Ledger)

These forms implement [researchplan.md](../researchplan.md) and issues [#6](https://github.com/BenWassa/great-decoupling/issues/6) and [#7](https://github.com/BenWassa/great-decoupling/issues/7). They do **not** set research conclusions or approve decisions [#1](https://github.com/BenWassa/great-decoupling/issues/1) and [#2](https://github.com/BenWassa/great-decoupling/issues/2).

## Folder contract

| File | Function |
| --- | --- |
| [source-inventory.md](source-inventory.md) | Blank common source/series schema and data lineage fields. |
| [definitions.md](definitions.md) | Operational concepts, populations, denominators and disallowed comparisons. |
| [uncertainty.md](uncertainty.md) | Coverage, sampling, missingness, uncertainty and rejected measures. |
| [evidence-review.md](evidence-review.md) | Per-observation status and reviewer form, including contested findings. |
| [measurement-change-log.md](measurement-change-log.md) | Series vintages, methodology changes, breaks and transformation record. |
| [r1-source-inventory.md](r1-source-inventory.md) | R1 **only**: productivity and compensation candidate inputs and run logs. |
| [r2-source-inventory.md](r2-source-inventory.md) | R2 **only**: household costs and viability candidate inputs and run logs. |
| [r3-source-inventory.md](r3-source-inventory.md) | R3 **only**: distribution and surplus-capture candidate inputs and run logs. |

## Usage and state discipline

1. Copy the blank forms **inside each run's own workspace** and use prefixed IDs (R1-S001, R1-D001, R1-E001; R2-...; R3-...). Do not share finding IDs or mix source tables across runs. The three seed inventories under this directory are **independent starting points**, not measured results.
2. Make a separate **source row per original publisher/series/vintage**, not one row per descriptive PDF; record any PDF as a *lead* with page and exact quotation location. Preserve immutable copies and access metadata where permitted.
3. For each numeric observation, record a datum status: **verified** (matched to original source and documented), **needs verification**, or **not usable**. These statuses describe the **datum**, not review depth or truth across competing sources.
4. Review source/evidence independently using **not reviewed / reviewed / corroborated / contested / rejected**. **Reviewed** means a reviewer inspected a source and method, not merely that a web page opened. **Corroborated** requires a genuinely independent comparator; the same dataset repeated in a commentary site is *not* independent corroboration.
5. Preserve exact source transformations, raw vs revised release, unknowns, original source definitions, endpoints, sampling frames, disallowed comparisons, missing periods, and rights. Link to evidence-review and measurement-change entries by IDs.
6. Do **not** backfill substantive results into empty places as assumptions. Use **UNRESOLVED** or **NOT REVIEWED** explicitly, with a retrieval/decision action and owner. No stitched lines without a recorded and defensible bridge.
7. Keep all research descriptive. Contradictions and negative results stay visible. No Claim Ledger, cross-run synthesis, causal proof, narrative, infographic specification, or policy recommendations in these templates.

## Minimal review gate per run

- Each source has a stable URL/DOI, publisher/date, retrieval time, rights status, raw table/series ID, unit/denominator, coverage and extraction route or **unknown** flag.
- Each retained observation has a primary-data source locator, units, status, exact method, independent reviewer/date and audit trail; if not, it remains **needs verification**.
- Run definitions, excluded measures, disputed estimates, historical breaks, sampling and uncertainty logs are filled.
- Owners of issues #1 and #2 have approved scope/terminology before a *final* methodological baseline is declared.
- Only after **all three independent runs** pass the [research-plan transition gate](../researchplan.md) may later work consider a Claim Ledger.

**Audit pointer:** [source-audit.md](../source-audit.md), which classifies the legacy PDFs' statements. The seed inventories below do not assert evidence verification or completion.
