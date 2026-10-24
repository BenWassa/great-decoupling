# R2 validation record — 2026-10-24

## Checks performed against the research branch

- Confirmed direct original-source links, units and populations in 21 per-run inventory entries (17 labelled reviewed for selected displayed facts; 4 identified but not yet extracted thoroughly).
- Retrieved repository versions of all R2 files via GitHub after writing; observed 51 numerical observation rows, five synthetic scenario rows, 21 inventory entries.
- Independently parsed all three CSVs as RFC-style quoted fields using a separate JavaScript checker, confirmed all records have the same column count, unique observation keys, nonnegative finite numbers, permitted 0–1 effective tax rates, and source IDs resolvable to the source inventory. **Observed: zero structural/provenance failures.**
- Independently recomputed renter-occupied ACS 2024 US matched denominator: 46,101,640 − 3,147,163 = 42,954,477; burden ≥30% = 4,056,945 + 2,966,608 + 4,012,728 + 11,200,981 = 22,237,262; 51.8%. Washington: 567,874 / (1,175,739 − 56,522) = 50.7%; published cell MOEs do not directly imply derived-rate intervals.
- Independently recalculated benchmark mixed-universe new-home price/income multiple (3.49× 1984-Q1, 4.84× 2025-Q1), Census/FRED real income change (+41.3%), and five scenario and shock arithmetic entries. These were placed in the frozen exhibits file using the documented formulas.
- Inspected the committed Python 3 code structure, source links, formulas, source-to-observation references, and the frozen exhibit rendering outline. Seven regression test cases cover provenance and values, same-gross family comparison, stress monotonicity, matched-rent denominator, real-vintage observations and output determinism.
- All committed paths are within **research/R2/**. No shared formatting, R1/R3, Claim Ledger or strategy-decision files were changed.

## Execution environment limitation and exact validation commands

The connected GitHub repository interface in this chat permits reading and committing UTF-8 files and opening PRs but does **not** provide a repository checkout/execute command. Therefore the following **have not been executed** against the committed Python files in this environment; static arithmetic/CSV checks **are not** a substitute for actual Python runtime execution or CI:

    python3 research/R2/reproduce.py
    python3 -m unittest discover -s research/R2 -p 'test_*.py' -v
    python3 research/R2/reproduce.py --check

Execute these from the repository root on the PR branch before merging or presenting the exhibits as computationally verified. If the --check command reports a difference, run with --write and review the diff (including rounding/newline differences) before committing. Do not assume green checks from this note.

## Status boundaries

- Research evidence **reviewed** at selected source-table level, not complete longitudinal census/survey microdata recomputation.
- Long series, owner cost-burden matched history, education net price/loan cohort, local childcare, alternative inflation baskets, complete regional strata and household size/earner-equivalence panels remain evidence gaps.
- The modeled household cash outputs are synthetic illustrations and cannot be used for population estimates.
- Owner decisions #1 and #2 remain unresolved; #7 owns shared audit templates. No causal inference or Claim Ledger in R2.
