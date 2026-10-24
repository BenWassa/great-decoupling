# R3 — Competing measures, counterevidence, rejected joins
**Snapshot:** 2026-10-24. Descriptive methodological register; no causal adjudication.

## Comparability disputes

### Labor share
BLS nonfarm-business labor share includes imputed proprietor labor, while BEA NIPA national income reports employee compensation separately from proprietor income. Gross sector output, GDI and *net* national income all have different denominators. The BLS sector excludes important government and nonprofit activities. Consequently a labor-share decline does not map dollar-for-dollar into distributable profits or shareholder dividends. [BLS estimation](https://www.bls.gov/opub/mlr/2017/article/estimating-the-us-labor-share.htm) · [BEA NIPA](https://apps.bea.gov/iTable/?categories=survey&isuri=1&reqid=19&step=2).

Sensitivity still needed: proprietor labor imputation (employee-equivalent wage vs alternative allocation), fixed industry shares versus compositional change, corporate vs noncorporate sector, net vs gross denominator, healthcare/pension benefits inclusion, and alternative windows. Neither 1973 nor another breakpoint has been established by a prespecified test.

### Income concentration: four competing populations
**CBO** estimates income of *households*, including capital gains and social insurance in before-transfers/taxes income; after-transfers/taxes subtracts federal taxes and adds means-tested transfers. [CBO](https://www.cbo.gov/publication/62792). **IRS SOI** ranks *tax returns* by AGI; joint filers are one return, income reporting changes across law changes, and the agency notes a 2010 percentile-method change. [IRS SOI](https://www.irs.gov/statistics/soi-tax-stats-individual-income-tax-rates-and-tax-shares). **BEA distributional personal income** allocates NIPA personal income to size-adjusted households; 2024 is provisional and 2025 is experimental nowcast. [BEA](https://www.bea.gov/data/special-topics/distribution-of-personal-income). **Census** CPS ASEC cash income excludes substantial noncash amounts and has sampling/population-control uncertainty; Census reports 2024–2025 Gini change is not statistically significant. [Census](https://www.census.gov/library/publications/2026/demo/p60-289.html).

**Distributional national accounts scholarly dispute.** Piketty–Saez–Zucman estimate incomes after allocating all national income to adults, including untaxed income; Auten–Splinter use competing allocations of non-taxed business income, pension accruals, taxes and transfers. They report meaningfully different top-income paths, particularly after taxes and transfers. These are primary research models, **not federal statistical series**. Compare both with sensitivity and model-data documents; do not select one without reconciliation. [PSZ 2020](https://www.aeaweb.org/articles?id=10.1257/jep.34.4.3); [Auten–Splinter JPE 2024](https://www.journals.uchicago.edu/doi/10.1086/728741); [PSZ 2024 reply](https://gabriel-zucman.eu/files/PSZ2024.pdf). An authors' 2019 comparison reports illustrative differing 2014 top-percentile shares under separate conventions; treating those as three independent observations of one identical quantity would be a methodological error. [Auten–Splinter 2019](https://www.aeaweb.org/articles?id=10.1257/pandp.20191038).

### Wealth stocks and high executive pay
Federal Reserve DFA models market-valued quarterly **net worth** from Financial Accounts and SCF survey distribution; 2025 SCF is sampled **families** with weights and multiple imputations. Income percentiles differ from wealth percentiles; net worth differs from total assets and gross financial assets. Apparent annual capital gains do not necessarily enter national-account income. [Fed DFA](https://www.federalreserve.gov/releases/z1/dataviz/dfa/) · [2025 SCF](https://www.federalreserve.gov/econres/scfindex.htm).

SEC Item 402(u) reports a registrant's CEO-to-median-company-employee compensation ratio, fiscal 2017 onward, with choices about estimation and employee population. EPI historically estimates ratios for selected large public companies using production/nonsupervisory comparator workers and separately reports option-granted versus realized equity. EPI is a **nongovernmental reconstruction**. One company's pay ratio is not the national CEO median nor the EPI ratio. [SEC rule](https://www.sec.gov/rules-regulations/2015/08/pay-ratio-disclosure) · [EPI dataset](https://www.epi.org/publication/ceo-pay/).

### Payouts, taxes, union coverage
S&P Dow Jones' S&P 500 cash **gross** repurchases/dividends do not equal Fed Financial Accounts net equity issuance or dividends of the US nonfinancial corporate sector; they cover different universes, with gross/net and stock/flow differences. Dividend claims can belong to pensions, institutions or foreigners. [S&P origination](https://press.spglobal.com/2025-12-18-S-P-500-Q3-2025-Buybacks-Post-Modest-6-2-Gain-to-249-0-Billion-After-Declining-20-1-Amidst-Uncertainty-in-Q2-Q4-2025-Expenditures-Expected-to-Post-Similar-Growth%2C-As-2025-Anticipates-a-Record-1-Trillion) · [Fed F.103](https://www.federalreserve.gov/releases/z1/20260319/html/f103.htm).

BLS union *membership* excludes nonmembers under union contracts who are included in the representation/coverage measure; CPS 1983 is not a universal comparable pre-1983 series. [BLS](https://www.bls.gov/news.release/union2.htm). A *top statutory marginal* tax rate is not the *average effective tax rate* or the **share of all federal tax** paid by a group. In CBO's distinct measure, top 1%'s share of all federal taxes rose from 14% in 1979 to 26% in 2023. [CBO](https://www.cbo.gov/publication/62792).

## Rejected-measure register
| Ref | Tempting shortcut | Status and reason |
|---|---|---|
| RJ01 | FRED PRS85006173 index quoted as percent labor share | REJECT: 2017=100 index, not share level |
| RJ02 | 100% minus BLS share interpreted as top households' profits | REJECT: mixed income, fixed capital consumption and sector denominators |
| RJ03 | BLS sector output share joined to BEA employee national-income share | REJECT equivalent-series claim: sectors and imputation differ |
| RJ04 | CBO household top-1 share appended to IRS AGI tax-return share | REJECT: statistical unit and income concept differ |
| RJ05 | CBO 1979 endpoint joined to PSZ national-income 2018 endpoint | REJECT: adult model vs households |
| RJ06 | BEA 2025 experimental nowcast treated as observed IRS top incomes | REJECT: modelled extrapolation |
| RJ07 | Top-1% assets share labelled net-worth share | REJECT: assets exclude liabilities |
| RJ08 | Unrealized stock appreciation labelled corporate annual profit distributed | REJECT: asset valuation stock vs income flow |
| RJ09 | Fed negative net equity issuance used as gross stock buybacks | REJECT: issuance/redemption and merger components |
| RJ10 | S&P dividends summed with F.103 dividends | REJECT: overlapping populations and definitions |
| RJ11 | Quarterly SAAR Fed corporate dividends treated as actual quarterly amount | REJECT: annualized rate |
| RJ12 | EPI CEO ratio labelled SEC registrant median-employee ratio | REJECT: different numerator samples/denominators |
| RJ13 | One SEC pay ratio generalized to all US CEOs | REJECT: selection bias |
| RJ14 | Union member density equated to union contract coverage | REJECT: covered nonmembers |
| RJ15 | Statutory top income tax rate presented as effective paid tax rate | REJECT: tax base/bracket/tax categories |
| RJ16 | Historical 1973 breakpoint accepted without alternative dates or tests | REJECT pending formal tests |
| RJ17 | Buybacks + dividends called extractable 'surplus' | REJECT: financing and counterfactual costs undefined |
| RJ18 | Co-moving union and capital shares as evidence union decline caused labor share movement | REJECT: confounding and simultaneity |

## Concrete counterobservations and untested alternatives
1. CBO pretax and posttax top 1% shares move differently and year-to-year gains are **non-monotonic** (capital gains and fiscal intervention sensitive). The 2022 and 2023 CBO reports are different revisions, not drop-in annual neighbours.
2. Gross labor shares may move with depreciation and the cost of new equipment; labor-intensive to capital-intensive industry mix may shift without equal change **within** every industry.
3. Changing incorporation, pass-through entity status, owner-manager payments and tax law can reclassify one person's income between employee wages, proprietors, corporate profits and gains.
4. Company-level buybacks could finance retirement of shares, employee-stock dilution, or mergers; S&P is a nonrepresentative set of large listed firms.
5. Pensions, retirement vehicles, nonprofits and international shareholders receive different fractions of the distributions. Ultimate beneficial ownership is not identified by issuer-level payout statements.
6. Rising compensation **benefits** can mitigate a cash-wage-only comparison; this belongs to R1's independent worker-compensation definitions, not a presumed reconciliation in R3.
7. Technology, market power, sector shift, demographics, trade, monopsony, union-bargaining changes, globalization and taxes are possible explanations; these results have no identifying counterfactual.
8. Different tax-rate schedules coexist with greater top-percentile **share of total federal taxes**, contradicting a simple one-metric description of falling tax burden. It does not decide whether effective rates increased or fell.

## Unresolved empirical work
Compute primary NIPA/BLS gross-vs-net/sector shares; weighted SCF 1989–2025 confidence intervals; CBO historical supplements under fixed vintage; independent SEC sample and EPI option-valuation reconciliation; Z.1 cash flows versus F.223 securities flows and issuer statements; geography/sector composition of CPS representation; BEA/IRS aftertax measure crosswalk. Distinguish evidence published by authors from numbers independently re-estimated. No statistical breakpoint or causal model is run here.
