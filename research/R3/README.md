# R3 — US distribution and institutions: independent evidence pack
**Evidence snapshot:** 2026-10-24. **Owner:** issue [#10](https://github.com/BenWassa/great-decoupling/issues/10). **Status:** research-only; not a Claim Ledger, causal model, synthesis or publication-ready interpretation.

## Scope and decision boundaries
US-centered descriptive inventory (pending [#1](https://github.com/BenWassa/great-decoupling/issues/1)); longest *comparable* period available separately for each measure, never a presumed 1973 break. No single 'middle class' definition (pending [#2](https://github.com/BenWassa/great-decoupling/issues/2)). R3 measures (i) the **functional** distribution of production income among compensation and other components, (ii) **personal** income flows, (iii) ownership of wealth **stocks**, (iv) listed-company CEO compensation and capital distributions, and (v) relevant descriptive institutional changes. These are non-equivalent populations.

**Research question in [researchplan.md](../researchplan.md):** Where did economic surplus flow if not to typical workers? That wording does **not** establish that there is a single measurable 'surplus', that all residual income belongs to shareholders, or that its location has been causally identified. R3 documents alternative measurements, not an answer to a causal question.

## Contents and reading order
1. [evidence.md](evidence.md) — source-linked evidence by domain, periods, boundaries and counterobservations.
2. [source-inventory.csv](source-inventory.csv) — machine-readable provenance: original publisher vs derived estimates; exact geography, populations, denominators, units, periods, extraction paths, revision/rights and confidence status.
3. [definitions-methods.md](definitions-methods.md) — operations, data separation, equations, decisions, extraction recipe and prohibited joins.
4. [competing-measures.md](competing-measures.md) — live methodological disputes, rejected measures, counterevidence, missing tests.
5. [institutions.md](institutions.md) — descriptive policy and labor-history chronology with original government citations.
6. [data/verified-observations.csv](data/verified-observations.csv) — deliberately small, dated transcription of official **published** values, not an interpolated time series.
7. [reproduce.py](reproduce.py) — standard-library data validation and explicitly optional Federal Reserve/FRED refreshed-series download; [VALIDATION.md](VALIDATION.md) — limitations, validation and outstanding work.

## Six independently reviewed domains
| Domain | Principal original production system | Reference periods | Key distinction |
|---|---|---|---|
| Labor share | BLS productivity program; BEA NIPA | 1947–2026 Q2; BEA annual | Nonfarm-business imputed proprietor labor vs total-economy employee compensation |
| Income distribution | CBO historical tax+survey income; BEA distribution of personal income; Census CPS; IRS SOI | CBO 1979–2023; BEA 2000–2024 and 2025 experimental nowcast | Household vs tax unit; pre- vs post-transfers/taxes; realized gains |
| Wealth distribution | Fed Distributional Financial Accounts; SCF | 1989 Q3–2026 Q2 DFA; 1989–2025 SCF | Net worth stock vs annual income flow; modeled quarter vs sampled survey |
| Executive pay | SEC corporate proxy reports; EPI constructed long-run series (secondary) | SEC company-by-company 2017+ pay ratios; EPI 1965–2025 | Grant-date vs realized option awards; differing worker denominators |
| Corporate payouts | Fed Z.1 F.103 and F.223; S&P Dow Jones Indices company statements | Z.1 annual/quarterly; Q3 2024–Q3 2025 benchmark | Gross repurchases vs net issuance; net dividends vs index cash dividends |
| Bargaining and tax institutions | BLS CPS unions; NLRB; IRS; CBO | CPS 1983–2025; laws by effective date | Membership vs contract coverage; statutory vs realized/effective rates |

## Evidence statuses
- **Corroborated published figures**: transcribed values directly visible in original government or data-producer release, with period and units; see observation CSV. **Not independently replicated from raw microdata.**
- **Reviewed methodology**: official statistical documents read, series constraints recorded; data may require archived vintages and additional microdata for hostile-reading readiness.
- **Contested / provisional**: scholarly distributional national accounts, revisions of tax-return data, BEA 2024 provisional or 2025 nowcast; kept distinct.
- **Not reviewed fully**: thousands of individual firm 10-K/proxy observations, Census/SCF public microdata weighted estimates, cross-border look-through ownership. These are documented gaps, not silently counted as validated.

## Central non-identity
A decline in a **particular sector's gross labor share** does not establish that an equal dollar amount was received as dividends by a defined set of wealthy households. Gross nonlabor output includes depreciation, taxes, mixed proprietors' income and other components depending on denominator. Capital gains are valuation changes, not national-account current production. Buybacks trade shares for cash and do not mechanically equal current profit or add to GDP. Workers may also own securities directly or via pension funds. See [definitions-methods.md](definitions-methods.md).

## External source hierarchy and citation conventions
Original government tables, disclosure filings and originating statistical producers take priority; independently authored economic papers are recorded with their competing models; stakeholder/think-tank reconstructions receive their own status, not government-source status. Every observation records a source ID. Hyperlinks to official releases are primary citations in the inventory. Retrieval date: 2026-10-24 unless noted. Dataset revision timestamps are not archival locks: regenerate to compare current vintages, never overwrite frozen observations without logging.

## Coordination and limits
Issue [#7](https://github.com/BenWassa/great-decoupling/issues/7) controls future **shared** format templates. This R3-local inventory provides the requested fields without editing its files; adjust this subtree to match its eventual schema in a subsequent R3-only change. Issues #1–#2 remain open; neither geographic cross-country comparisons nor a 'typical worker' cutoff is selected here.

**No claim ledger. No causal attribution, moral conclusion, proposed policy, or inference about anyone's motives.**
