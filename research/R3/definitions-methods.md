# R3 definitions and reproducible methodology
**Version:** 2026-10-24; **unit of analysis:** specified separately for every series. This local format may be adjusted to match #7's eventual template, but no shared file may be edited.

## Observable constructs — never collapse them
| Construct | Numerator | Denominator / population | Units / coverage | Do not infer |
|---|---|---|---|---|
| BLS nonfarm-business labor share | Employee compensation + imputed proprietor labor pay | Nonfarm business sector output, BLS productivity programme | Quarterly share of gross sector output; since 1947 | Residual equals dividends or income of top percentile |
| BEA compensation / national income | BEA compensation of **employees** (wages + supplements) | BEA NIPA national income | Annual dollars/dollars, whole national income | Includes all self-employed labor (it does not) |
| BEA compensation / gross domestic income | BEA compensation of employees paid (domestic coverage) | GDI | Annual; includes CFC, production taxes | Identical to net national income or BLS share |
| CBO pre-transfer/tax top share | Income of highest-ranked CBO households incl. market income and social insurance | All CBO household income before means-tested transfers/federal taxes, plus stated handling of negative-income groups | Percent annual 1979–2023 | Before *all* transfers, national income, IRS AGI or an adult percentile |
| CBO after-transfer/tax share | Ranked household income after means-tested transfers and federal taxes | CBO total household income after transfers/taxes | Percent annual 1979–2023 | Includes state/local taxes comprehensively |
| IRS top income/AGI share | AGI of returns ranked by AGI | AGI of income-tax filing units under SOI coverage rules | Percent annual; methodology break circa 2010 | Household or individual share |
| BEA PI quintile | Distributionally allocated NIPA personal income | Sum of distributed personal income to size-adjusted household income classes | Percent, 2000–2024, 2025 nowcast | Same totals or hierarchy as CBO pre/post tax |
| Fed DFA top net worth share | Assets less liabilities of wealth-percentile group | Net worth across all DFA household units | Quarterly percent of total net worth since 1989 Q3 | Annual income share, household count, % total assets |
| Fed SCF share | Weighted/survey-imputed family assets less liabilities | SCF sampled families; correct weights and implicates | Triennial stock, interval estimates | Exact same quarter/uncertainty as DFA |
| CEO-to-worker: EPI | Realized equity or grant-date CEO total pay among selected large firms | Compensation of production/nonsupervisory workers (comparison sample depends on vintage) | Ratio, nominal/real dollars cancel when same deflator | Typical SEC registrant CEO / firm's median |
| SEC registrant CEO ratio | Total annual PEO remuneration under SCT | Annual compensation of *median employee* using registrant method | Per-firm annual ratio from fiscal 2017+ | Cross-firm or historic-national mean without sample design |
| S&P 500 gross repurchases | Cash spent buying own common shares by index firms | Specific constituent universe; optional earnings/market capitalization denominator | $/quarter or trailing 12 months | Profits, net shares retired, aggregate wealth, household receipts |
| Fed F.103 net dividends | Corporate net dividends as defined in Flow of Funds | Nonfinancial domestic corporate-business sector | Billions annual or SAAR quarterly | Same as S&P index dividends |
| Union density | Union member wage/salary workers in CPS | All eligible wage and salary workers employed | Percent annual; 1983 comparable start | Coverage, all employed persons, causal bargaining effect |
| Union coverage | Members + nonmembers with union contracts | Eligible wage/salary employed CPS universe | Percent annual | Union membership |
| Top statutory federal rate | Highest marginal rate on taxable income beyond bracket threshold | Tax schedule; filing status and year | Percent per tax year | Average/effective rate or tax share |

## Accounting bridge
BLS-L = (employee compensation + estimated proprietor labor compensation) / BLS-sector current-dollar output.

An **alternative** national-income compensation ratio C_NI = BEA employee compensation / BEA national income. To estimate all-worker share at the NI level, an explicit allocation of mixed proprietors' income to labor must first be defined. An alternative net share must handle CFC and gross-vs-net adjustments consistently. The residual of a selected gross share, 1-L, is **not** synonymous with shareholder income: besides business net operating surplus it may contain depreciation (consumption of fixed capital), production taxes less subsidies, financing and other sector components as defined.

For sensitivity, construct separate named variants rather than smoothing: (a) BLS nonfarm-business all-worker labor share, (b) BLS nonfinancial corporate share, (c) BEA employees/national income, (d) BEA employees/GDI, (e) allocated proprietors' income at employee hourly pay, (f) alternative imputation and net value added. Each variation needs a *matched numerator and denominator* and historical start/end, with any growth decomposition labelled a **measurement decomposition**.

## Valuation and stock-flow bridge
Net worth W_t = market value of assets A_t minus liabilities D_t. Its change includes **saving/net investment**, **realized and unrealized capital gains**, **revaluations**, **inheritances and transfers**, and **other volume changes/reclassifications**. Flow F(t_0,t_1) is an amount *over an interval* (e.g., one quarter's stock repurchases), not W at a point. A negative net issuance value does not estimate gross cash buybacks.

For index payout cross-check, S&P Q3 2025 reported 249.0 ($bn) gross repurchases + 168.1 ($bn) dividends = 417.1 ($bn) combined, subject to rounding. Trailing 12-month September 2025: 1020.27+664.90=1685.17 ($bn), rounded to $1.685 trillion. **Do not** append overlapping quarters or add TTM and quarter observations.

## Selection / deflators / high earners
Ranks are recomputed in each source year and can change membership across time. Shares are current-dollar ratios; a price deflator cancels only if the same aggregate index is applied to both numerator and denominator for the same period. It does **not** cancel for real-dollar comparisons across income brackets with different price exposure, and does not resolve stocks vs flows. If CEO pay is compared across time in 2025 dollars, lock a deflator and explicitly value vested/granted equity consistently. Distinguish top *income tax returns* from top *households*, and from top *wealth units*, and **workers** (CPS employed) from **earners** (tax and survey incomes). Do not assign a personal net-worth percentile to a payroll worker without linked microdata.

## Extraction protocol
1. In [source-inventory.csv](source-inventory.csv) record primary source, release/vintage, publisher, original URL, population, unit and denominator, years, revisions and use limitations; record screenshot or archive only when lawful and needed.
2. Download directly from origin. For FRED-hosted Board series, a user without API key can use the FRED Graph 'Download CSV' interface; [reproduce.py](reproduce.py) implements an optional URL-based refresh. **Network retrieval was not possible in the authoring environment**, so no claim of successfully executed live download is made.
3. Save retrieved files unmodified with retrieval date and SHA-256 checksum **outside the checked-in frozen observations**; publish only derived values that can be traced to a source. Verify Q2 2026 vs older DFA vintages rather than silently replacing.
4. Parse stated frequencies: annual for CBO; Q + seasonally adjusted annual rate for Fed F.103; Q raw percent for DFA; no linear interpolation of missing years; no axis read-off when tabular original exists.
5. Build an event-time table with legal enactment date, effective date and relevant measured observation date separately. Do not regress legal events directly on outcomes without an identified comparison/counterfactual.
6. Label all outputs exactly as units (percent vs percentage-point difference; $billions actual quarter vs annualized rate, index base); check aggregation identities only within the same dataset, unit, period and vintage.
7. Compare pre/post-transfer and stock/flow series side by side **only**, with labels, until an explicit compatible model exists.

## Quality and uncertainty
**Measurement:** misallocated mixed income; employer benefits; retained/undistributed profits; untaxed business income; 2010 IRS population changes; 1986 tax incentives and income shifting; changes in Census CPS questionnaire/population controls; 2025 union missing October and industry classification; Fed SCF survey weights/implicates; DFA quarterly model allocation; changing S&P issuer universe; option exercise timing; share-issuance netting.

**Sampling:** Census CPS and SCF estimates require standard errors; DFA is a constructed model, not a literal complete individual census. Do not report confidence intervals not calculated. A statistically insignificant Census 2024–25 Gini change is not a zero change.

**Revisions:** [CBO 2022 publication](https://www.cbo.gov/publication/62300) vs [CBO 2023 edition](https://www.cbo.gov/publication/62792); [2025 SEC/EPI comparative vintages](https://www.epi.org/publication/ceo-pay/); Fed DFA June vs September 2026; Fed F.103 annual rebenchmarkings; BEA national-account updates. Never treat releases as permanent fixed truth.

**Copyright and redistribution:** Direct links used; no bulk republishes of third-party source datasets. Federal government-origin tables generally cite their own usage conditions; S&P DJI figures are *originating private data producer* material, rights to republish full tables not presumed. Every source row marks license/rights or 'verify before redistribution'.

## Testing and explicit limits
[reproduce.py](reproduce.py) checks input types, period/measure/source uniqueness, source lineage, denominator compatibility for registered comparisons, and the within-S&P arithmetic identity. It does **not** reproduce BLS's sector/accounting estimates, CBO's confidential tax microdata, full weighted SCF estimates or S&P proprietary repurchase universe from company filings. These need separately approved/full-access stages. See [VALIDATION.md](VALIDATION.md).

## Rejected transforms (nonexhaustive)
- PRS85006173 index 2017=100 as percent labor share.
- Net equity issuance as buybacks; equity market gain as distributed operating profit.
- Dividends from domestic all-corporate SAAR plus index gross dividends as a consistent total.
- Top 1% ranked by income as top 1% ranked by wealth.
- SEC pay ratio of one issuer vs EPI CEO-to-worker ratio of selected large issuers.
- Headline 1973 before test of breaks and sensitivity.
- An 'average worker' figure from labor-share arithmetic as a **median worker** experience.
- S&P top-20 buyback concentration as the equity ownership share of the top 20 households.
