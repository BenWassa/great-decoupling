# Source audit: pre–Claim Ledger research assets

**Audit date:** 2026-10-24  
**Scope:** Existing repository assets only; this is a provenance, measurement, and gap review, **not** a research run or synthesis.  
**Governance:** [researchplan.md](researchplan.md), [WORKFLOWPLAN.md](../WORKFLOWPLAN.md), issues [#6](https://github.com/BenWassa/great-decoupling/issues/6), [#7](https://github.com/BenWassa/great-decoupling/issues/7), with scope decisions [#1](https://github.com/BenWassa/great-decoupling/issues/1) and [#2](https://github.com/BenWassa/great-decoupling/issues/2) **unresolved**.

## Audit protocol and evidence-status meanings

- **verified** = the *specific reported datum* was checked against a dated, independently accessible publisher table or methodology on 2026-10-24. This is a **source-match**, not independent replication, current-series approval, or permission to infer causality.
- **needs verification** = a document mentions a source or statistic, but the original table/series, vintage, units, calculation, or comparability was not independently checked. This is the default; a plausible citation is not verification.
- **not usable** = the exact formulation has a demonstrated inconsistency, unsupported causal leap, denominator mismatch, or invalid comparison. Original data may remain retrievable; do not propagate the formulation.

**Source review** is a separate workflow from datum verification: source statuses are *not reviewed / reviewed / corroborated / contested / rejected*. A source can be **reviewed** yet most assertions derived from it still **need verification**. No PDF has been admitted as a primary source.

**Methods:** inspected the text and source lists in all PDF pages, compared the [research plan](researchplan.md) and [workflow plan](../WORKFLOWPLAN.md), and spot-checked explicitly identified figures against original publisher pages. No raw data were downloaded, series reconstructed, image rights cleared, statistical tests run, or internal footnote-number-to-claim mapping independently validated. The remaining inventory is deliberately exhaustive at the level of *distinct published numeric statements*, including bundled ranges whose constituents share the same status; broad qualitative/counterfactual and causal assertions are listed as methodological flags, not converted to observations. Page references are PDF page numbers, not source-publisher pages.

## Asset inventory / provenance

| ID | Asset; extent | Origin, author, date, source type | Applicable run / permissible use | Independently traceable? |
| --- | --- | --- | --- | --- |
| P-M | [Defining the “Middle Class”: Multiple Perspectives and Implications](<Defining the “Middle Class”_ Multiple Perspectives and Implications.pdf>), 4 pp. | ChatGPT-branded research export; **author, creation date, retrieval date, research protocol not stated**. Unreviewed secondary/tertiary compilation. | **R2 definitions support only**, not an R2 housing/childcare/healthcare dataset; **R3** income-tier concepts contextual; **R1** worker-versus-household caution. | Named Pew, Urban, Brookings, Business Insider, SmartAsset, Dallas Observer URLs; some publisher pages independently accessible. No saved source tables, transformation scripts, or complete claim-level footnote key. |
| P-D | [Major Trends Reshaping U.S. Income Distribution (1940s–2020s)](<Major Trends Reshaping U.S. Income Distribution (1940s–2020s).pdf>), 7 pp. | ChatGPT-branded research export; author/date/research protocol not stated. Secondary compilation with advocacy/opinion and tertiary links. | **R3 primary candidate map** for labor share, income shares, executive pay, payouts, unions and taxes. **Not R1** productivity/pay series. | St. Louis Fed, Brookings, EPI, BLS, CBO cited by name; linked Wikipedia, Inequality.org, image-only Tableau, interview. Source-to-exact-number links largely absent; underlying tables and vintages missing. |
| P-E | [U.S. Economic and Labor Market Trends (2020–2025)](<U.S. Economic and Labor Market Trends (2020–2025).pdf>), 6 pp. | ChatGPT-branded research export; author/date/research protocol not stated; body refers to **early 2026** (p. 4), so do not date from filename alone. Secondary compilation. | **R1** nominal/real wage and inflation context, not long-run productivity; **R3** household-income inequality context; **R2** inflation context only. Outside much of the historical scope. | BEA, BLS, Census, Fed, OECD named; some stable dated releases, but live `/news.release/` URLs can change and international rates are not harmonized. |
| A-PLAN | [research/researchplan.md](researchplan.md) | Repo-authored governing research protocol; no independent numeric evidence. | Defines separate R1/R2/R3 and prohibits causal writing and early synthesis. | Fully reviewable in repo. |
| A-WORK | [WORKFLOWPLAN.md](../WORKFLOWPLAN.md) | Workflow / future site specification; **not evidence**. | The suggested Claim Ledger is **downstream** of completing all runs; not authorized in this PR. | Fully reviewable; ordering is superseded for this phase by the research plan's transition rule. |
| A-VIS | [visuals/components/infographi_v1.png](../visuals/components/infographi_v1.png) | Legacy PNG (6,467,151 bytes), creator/date/data licensing not established. | **Not evidence**; separate future claim-by-claim audit against data and image license required. | Repository artifact traceable; its plotted numbers and rights **not validated** in this scope. |

**Original materials vs derivative:** Source URLs in the PDFs are candidate references, not an archived source pack. A peer-reviewed/official publisher page is a source; a ChatGPT export containing a quotation of it is not. Page references and selective fact checks below do not validate every graph or qualitative sentence in the export. No PDF contains a reproducible data-extraction workflow, complete denominator crosswalk, or an independently collected time series.

## P-M: “Middle Class” definitions, R2 support (secondary R1/R3 boundary)

**Coverage:** Relative median-income thresholds, percentile bands, occupational and self-identification approaches; illustrative 2022 U.S. metros. Does **not** supply R2 fixed-cost series, time-use, household shock tests or regional budgets. Pew's analysis uses people *living in* size-adjusted middle-income households; do not relabel these as independent middle-class workers. ACS metro thresholds and CPS historical shares involve different sources and adjustments.

| ID / PDF page | Numeric statement in PDF (retain exact unit and year) | Status | Check / required action |
| --- | --- | --- | --- |
| M01 p1 | Pew middle-income tier = **2/3 to 2×** median size-adjusted household income | **verified** | [Pew methodology](https://www.pewresearch.org/race-and-ethnicity/2024/05/31/the-state-of-the-american-middle-class/); distinguishes persons from households. |
| M02 p1 | 2022 national band **$56,600–$169,800**, household of three | **verified** | [Pew 2024 calculator](https://www.pewresearch.org/short-reads/2024/09/16/are-you-in-the-american-middle-class/); 2022 ACS, 2022 dollars, household-size adjustment. |
| M03 p1 | “about $85k” adjusted national median underlying M02 | **needs verification** | Retrieve Pew calculator methodology and clarify whether the median is household-head size-adjusted, not official unadjusted median. |
| M04 p1 | Krueger alternative **50%–150%** of median | **needs verification** | Retrieve original article, exact population and reference median. |
| M05 p1 | Brookings review: **a dozen** definitions, cutoffs **$13k–$230k**, many **$50k–$125k** | **needs verification** | [Brookings definition review](https://www.brookings.edu/research/defining-the-middle-class-cash-credentials-or-culture/); underlying studies use unlike years and units. Do not compare ranges without crosswalk. |
| M06 p1 | Illustrative fixed income bracket **$50k–$150k** | **not usable** | Example bracket, not observed population statistic, date-specific validated threshold, or recommended working definition. |
| M07 p2 | 2022 San Jose MSA **$99,300–$297,800** | **needs verification** | Retrieve original area income source and metro boundaries; table may omit Pew cost-of-living adjustment. |
| M08 p2 | 2022 NYC MSA **$61,000–$183,100** | **needs verification** | Same metro-source / income-adjustment check as M07. |
| M09 p2 | 2022 Chicago MSA **$55,300–$165,800** | **needs verification** | Same check. |
| M10 p2 | 2022 Pine Bluff MSA **$29,500–$88,500** | **needs verification** | Same check; national/metro medians cannot be interchanged. |
| M11 p3 | 2022 U.S. household median **~$74,600** | **verified** | [Census Income in the United States: 2022, Table A-1](https://www.census.gov/library/publications/2023/demo/p60-279.html): $74,580 in 2022, real 2022 dollars; **not** the adjusted Pew median. |
| M12 p3 | San Francisco **~$66,700**, Jackson TN **~$49,200** to meet nominal national-band floor | **needs verification** | Retrieve Pew geographic cost-of-living calculator release/method. Do not merge with M07–M10 metro-income bands. |
| M13 p3 | **51% in 2023 vs 61% in 1971** | **not usable as worded** | Numerals match [Pew 2024](https://www.pewresearch.org/race-and-ethnicity/2024/05/31/the-state-of-the-american-middle-class/), **but PDF says “U.S. adults”** whereas cited headline reports *Americans living in middle-income households*. Re-enter only with publisher's population definition and survey/income reference years. |
| M14 p3 | Subjective middle/working-class self-ID **“close to 90%”** | **needs verification** | Retrieve dated survey question, response categories, weighting, and include/exclude “working class” explicitly. |
| M15 p3 | Middle-tier share in CA/NY **“under 45%”** | **needs verification** | Locate state-specific numerator, year and size/area adjustment; not necessarily same as Pew national statistic. |
| M16 p4 | Narrative claim of shrinking middle *wealth* and hollowed-out occupations since **1970** | **not usable** | No matching quantified wealth or occupation measure in this PDF; separate R3 distributions from middle-income household shares. |

**Source classes and licensing:** [Pew](https://www.pewresearch.org/race-and-ethnicity/2024/05/31/the-state-of-the-american-middle-class/) and [Brookings](https://www.brookings.edu/research/defining-the-middle-class-cash-credentials-or-culture/) are analyses with stated methods; Census CPS/ACS/IPUMS are underlying datasets to retrieve. [Urban](https://www.urban.org/urban-wire/how-we-define-middle-class-has-broad-implications) provides methodological commentary. Business Insider, SmartAsset and Dallas Observer are **secondary reporting/tools**, not substitutes for original tables. Each publisher's reuse conditions and graph permissions **not checked**; link and paraphrase without copying charts/large text.

## P-D: Distribution trends, R3 candidate evidence

**Coverage:** Labor share, top shares, CEO pay, buybacks, stock ownership, unionization, tax rates. Many passages explain *causes*, assign motivations, or make distributional moral judgments: **out of bounds** under R3 even where a descriptive statistic can be sourced. Do not reuse the document's “conclusion” or claims that buybacks mechanically raise prices, that globalization explains a quantified share, or that tax changes caused the reported outcome without causal identification. Distinguish labor's share of **gross domestic income** from employees' compensation share of GDP and adjusted proprietor labor income.

| ID / PDF page | Numeric statement / derived comparison | Status | Check / required action |
| --- | --- | --- | --- |
| D01 p1 | Labor-share peak about **1970**, decline since **1980s**, steeper around **2000** | **verified** | [Aum & Shin, St. Louis Fed Review (2020)](https://www.stlouisfed.org/publications/review/2020/10/22/why-is-the-labor-share-declining), DOI 10.20955/r.102.413-28; their NIPA-adjusted measure, not one universal breakpoint. |
| D02 p1 | Labor share **57.1% in 1948–87 vs 53.3% in 2010–12**, **~4 pp** | **needs verification** | Retrieve original study table, proprietors' adjustment, period averaging and denominator. |
| D03 p1 | Import competition explains **3.3 of 3.9 pp** | **not usable as causal certainty** | Retrieve [Elsby, Hobijn & Şahin](https://www.brookings.edu/articles/the-decline-of-the-u-s-labor-share/) identification and robustness; do not present decomposition as demonstrated universal causal share. |
| D04 p1 | Top **0.01% +~1,000% 1979–2021**, **27×** bottom 20% growth | **needs verification** | Recover CBO distributional series, pre/after-tax basis and denominator; arithmetic and endpoint vintage must match. |
| D05 p1 | Top **1% ~10% in 1970s, >20% today**, **+10 pp** | **needs verification** | WID/Piketty-Saez/CBO income definitions differ; record capital gains/taxes/household vs tax unit. |
| D06 p2 | Top 0.1% vs bottom 90% ratio “late 2000s = late 1920s” | **needs verification** | Locate actual ratio plot and income definition; visual resemblance ≠ measured equality. |
| D07 p2 | Official poverty down **~1–2 pp** over “several decades” | **not usable** | Unspecified endpoints / official vs supplemental poverty; cannot reproduce this interval. |
| D08 p2 | CEO-to-worker ratio **~40:1 (1980), 324:1 (2021), >500:1 late 1990s** | **needs verification** | EPI vs AFL-CIO vs S&P 500 methods not interchangeable; include realizations of stock options, company sample and worker denominator. |
| D09 p2 | CEO pay **>1,000% 1978–2024**, worker pay **~26%**, “~40× faster” | **needs verification** | Retrieve a single dated [EPI CEO pay](https://www.epi.org/publication/ceo-pay/) release with identical sample, deflator and window; no cross-edition splice. |
| D10 p3 | Corporate profits **~8% GDP (1980), ~12–13% recent** | **needs verification** | BEA profits with IVA/CCAdj vs without, net vs gross, GDP denominator; dates not specified. |
| D11 p3 | D10 described as “**doubling**” | **not usable** | 8% to 12–13% is a 50–62.5% increase, **not a doubling**; arithmetic contradicts adjacent values. |
| D12 p3 | **2018** S&P 500 buybacks exceeded all capital expenditures | **needs verification** | Retrieve index-universe definitions, capex and buyback totals from same period/source; a single year does not establish trend. |
| D13 p3 | S&P 500 repurchases **$882 billion in 2021** | **needs verification** | Retrieve original S&P Dow Jones Indices release/table and gross vs net repurchase definition. |
| D14 p3 | Top **10% own >80%** of stock market wealth; top **1% ~40%** | **needs verification** | Fed Distributional Financial Accounts vs SCF; determine direct vs indirect equities and observation year. |
| D15 p4 | Union density **>30% 1940s/1950s**, **~10% 2022**, private **~6%** | **needs verification** | Historical and recent BLS population/coverage differ; verify 2022 archive and pre-1983 comparability explicitly. |
| D16 p4 | **2024 union women $1,232/week**, **>$200** above nonunion women | **verified** | [BLS 2024 union release Table 2](https://www.bls.gov/news.release/archives/union2_01282025.htm): union women $1,232; nonunion $1,016 (difference $216), **unadjusted composition**. |
| D17 p4 | D16 described as pay advantage “even after controlling for job types” | **not usable** | [BLS technical note](https://www.bls.gov/news.release/archives/union2_01282025.htm) explicitly cautions the broad comparison **does not control** for occupation, industry, etc. |
| D18 p4 | Top **1% nearly 20%** of 2022 income | **needs verification** | Identify Treasury paper, pre/post tax incomes, population and fiscal year. |
| D19 p5 | Top statutory individual rate **91% early 1960s**, **70% mid-1960s**, **28% in 1988**, **37% in 2018** | **needs verification** | Use IRS/Tax Policy Center dated historical statutory table; top marginal is **not** effective average tax rate. |
| D20 p5 | Corporate federal statutory rate **52% in 1950s**, **35% pre-2018**, **21% after 2017 act** | **needs verification** | IRS statutory effective-date and surtax details; state taxes/exemptions distinct. |
| D21 p5 | Long-term capital gains/qualified dividends top statutory rate **20%** | **needs verification** | Tax year and NIIT/state-tax treatment unspecified. |
| D22 p5 | After-tax incomes: top **0.01% >1,000%**, bottom fifth **~130%** 1979–2021, **7.6×** | **needs verification** | Original CBO table and arithmetic on same 1979–2021 vintage; distinguish from D04 (before-tax comparison). |
| D23 p5 | Tax-policy causal “principal engine,” tax cuts → inequality, buybacks and CEO pay | **not usable** | Source-specific empirical identification not provided; prohibited by [R3 non-goals](researchplan.md). |
| D24 p6 | Policy prescriptions/“intentional systems” conclusion | **not usable** | Synthesis/intent/policy conclusions explicitly outside this pre-ledger phase. |

**Reference integrity:** P-D cites [St. Louis Fed](https://www.stlouisfed.org/publications/review/2020/10/22/why-is-the-labor-share-declining) (independently located), [Brookings](https://www.brookings.edu/articles/the-decline-of-the-u-s-labor-share/), [EPI](https://www.epi.org/publication/ceo-pay/), and BLS by name. It also supplies a [Tableau image-only URL](https://public.tableau.com/static/images/CE/CEO-WorkerPayGapAlmost6TimesasLargeasin1980-2022/Dashboard2/1_rss.png), [Inequality.org](https://inequality.org/facts/income-inequality/), [Wikipedia](https://en.wikipedia.org/wiki/Labor_unions_in_the_United_States), and an interview; these are **not original machine-readable tables**. BLS Table 2 contains the counterexample D17. Licensing for EPI, Federal Reserve, historical graphs, and linked image **unresolved**.

## P-E: 2020–2025 U.S. economic/labor context (partial R1 and R3)

**Coverage:** GDP, employment, wages, CPI, income Gini and international macro context; lacks productivity–compensation differential definitions, R2 fixed-cost series, R3 long-run capital/labor distribution, and complete statistical vintages. “Conclusion,” recovery-policy attribution and “soft landing” labels are interpretations, not run output. The PDF contains a 2025 snapshot relying in part on releases published **January 2026**; freeze vintage before analysis.

| ID / PDF page | Numeric statement / measure | Status | Check / required action |
| --- | --- | --- | --- |
| E01 p1 | Real GDP **−3.4% 2020, +5.7% 2021, +1.9% 2022, +2.5% 2023** | **needs verification** | BEA original 2024 advance vs revised NIPA series, real annual % change; do not silently mix releases. |
| E02 p1 | Q4 2023 GDP “back to pre-pandemic trend” and peers below trend | **needs verification** | [Federal Reserve note (2024-05-17)](https://www.federalreserve.gov/econres/notes/feds-notes/why-is-the-u-s-gdp-recovering-faster-than-other-advanced-economies-20240517.html); trend counterfactual and method not reproduced. |
| E03 p1 | Eurozone **~0.5%**, UK **~0.3%** GDP growth in 2023 vs U.S. **~2.5%** | **needs verification** | Obtain OECD/Eurostat/ONS matched revisions, time basis and GDP per-capita sensitivity. |
| E04 p1 | U.S. unemployment **14.7% April 2020**, **3.4% Jan 2023** | **needs verification** | Retrieve historical BLS CPS archived releases, seasonally adjusted unemployment series. |
| E05 p2 | Dec 2025 unemployment **4.4%** | **verified** | [BLS archived December 2025 release, 2026-01-09](https://www.bls.gov/news.release/archives/empsit_01092026.htm), CPS seasonally adjusted. |
| E06 p2 | Dec 2025 long-term unemployed **1.9m, +~400k** yr/yr | **verified** | Same [BLS archive](https://www.bls.gov/news.release/archives/empsit_01092026.htm): +397k. |
| E07 p2 | Dec 2025 LFPR **62.4%**; employment-population **59.7%** | **verified** | Same BLS archived release; seasonally adjusted civilian population measures. |
| E08 p2 | Early 2020 LFPR **63.4%**, 2019 employment/pop ratio **~61%** | **needs verification** | Compare consistent CPS vintages, age coverage and 2025 population controls. |
| E09 p2 | Dec 2025 part-time economic reasons **5.3m, +~1m** | **verified** | Same BLS archive: +980k; seasonally adjusted, definition in CPS technical note. |
| E10 p2 | 2025 payroll growth **~49k/month** vs 2024 **168k/month** | **needs verification** | Verify annual average change and benchmark revisions in same CES vintage; distinguish 2025 release timing. |
| E11 p2 | 2025 unemployment comparators Canada **7.1%**, OECD **~4.9%**, Germany **3–3.5%**, UK **4–4.5%**, France **~7%**, Japan **~2.5%** | **needs verification** | Harmonized OECD release by **same month**; nationally reported series are not directly interchangeable. |
| E12 p2 | Nominal AHE growth **~5% 2021–22**, CPI **~8% in 2022** | **needs verification** | Specify 12-month versus calendar-year inflation and worker universe. |
| E13 p2 | Real median household income **$76,300 2021 / $74,600 2022**, **−2.3%** | **verified** | [Census P60-279 (2023)](https://www.census.gov/library/publications/2023/demo/p60-279.html): $76,330 / $74,580 in **2022 dollars**; PDF rounded. Not median worker wage. |
| E14 p3 | Real hourly earnings **+1.2% Jun 2022–Jun 2023**, **+0.7% Aug 2024–Aug 2025** | **needs verification** | Retrieve BLS real earnings series with exact CPI deflator and vintage; validate each linked TED release. |
| E15 p3 | Household money-income Gini **0.494 2021 / 0.488 2022** | **verified** | [Census P60-279 (2023), Table A-3](https://www.census.gov/library/publications/2023/demo/p60-279.html), *pre-tax money income*, not equivalized disposable-income OECD Gini. |
| E16 p3 | Western Europe post-tax Ginis **~0.30–0.35** vs U.S. Census Gini | **not usable as comparison** | Different income concepts (post-tax vs U.S. pretax money income), units, years and equivalization; rebuild on harmonized OECD data. |
| E17 p3 | June 2022 U.S. CPI peak **9.1% y/y**, Dec 2025 CPI **2.7%**, core **~2.6%** | **needs verification** | Retrieve the **archived** BLS 2022/2025 CPI releases; headline CPI is not Fed's 2% **PCE** target measure. |
| E18 p3 | “CPI 2.7% effectively **on target** (2% Federal Reserve goal)” | **not usable** | Fed target is **PCE** inflation, not CPI; 2.7% is also numerically above 2%. |
| E19 p3–4 | Eurozone Oct 2022 inflation **10.6%**, UK **>11%**; 2023 UK **6.8%**, EU **6.3%**, US **4.1%** | **needs verification** | Eurostat/HICP vs ONS/CPI vs U.S. CPI methods, annual averages versus month peaks. |
| E20 p4 | Japan inflation **~3–4% 2022–23**; eurozone **~3%**, UK **~5%** “late 2025” | **needs verification** | Dates not consistently given; check releases and whether late-2025 values actually match. |
| E21 p4 | U.S. debt **~97% of GDP mid-2023**; Fed policy rate **>5% 2023** | **needs verification** | CBO debt-held-by-public vs gross federal debt denominator; FOMC target upper vs effective fed funds rate. |
| E22 p4 | U.S. outperformance **caused by** fiscal intervention/flexible labor market; “policy success” | **not usable** | Causal policy evaluation not established, outside [R1/R3 non-goals](researchplan.md). |

**Provenance trap:** The PDF links to [BLS live employment release PDF](https://www.bls.gov/news.release/pdf/empsit.pdf) and [live CPI page](https://www.bls.gov/news.release/cpi.nr0.htm). These now refer to the *latest* releases, not necessarily December 2025. Always cite a dated [BLS employment archive](https://www.bls.gov/news.release/archives/empsit_01092026.htm) / appropriate dated CPI archive instead. Its Wikipedia inflation page is orientation, not a primary data source; BEA advance release and Federal Reserve comparative note have their own dated vintages.

## Cross-document collisions and disallowed merges

| Collision / constraint | Specific examples | Handling before any claims |
| --- | --- | --- |
| Household vs person vs worker | M13 Pew share of *people* living in middle-income **households** vs E13 median **household** income vs D09 typical **worker** compensation | Retain as different units, never splice into a single “middle-class wage” series; issue #2 awaits choice. |
| Baseline, price index and dollar year | M02 ACS/Pew local adjustment; M11/E13 Census CPS 2022 dollars; D09 real CEO pay; E12 AHE/CPI | Record household size, geography, price deflator, base year, population and compensation concept per dataset. |
| Top-share denominators and overlaps | D04 vs D22 top 0.01% pre/post-tax; D05 vs D18 1% top share; M13 51% people vs class share of income | Label purported duplicate claims for independent adjudication; no averaging or premature harmonization. |
| Labor share methods | D01–D03 NIPA-adjusted self-employment labor income vs R1 productivity per hour, median pay | Do not equate national labor share, labor productivity and median hourly compensation. |
| Date vintage | E01 advance GDP vs revised series; E05–E10 December 2025 BLS data; E17 rolling CPI link | Archive publisher releases with retrieval date; log revisions and data discontinuities. |
| Geography | M07–M10 MSA boundaries / Pew adjustment; E03/E11/E19 mixed countries and CPI concepts | Cross-national comparisons require common definitions under undecided issue #1. |
| R2 absence | P-M defines groups but offers no longitudinal **housing, healthcare, education, childcare, budget, time-use** costs | R2 primary research remains substantially unstarted; no cost outcomes inferred from definition thresholds. |

## Source retrieval queue (not a synthesized research agenda)

**R1:** Retrieve BLS productivity and total/median compensation tables, definitions of all-employees vs production/nonsupervisory compensation, benefits, work hours, and CPI-U/CPI-U-RS/PCE deflators; identify long-series breakpoints *after* checking splices. [BLS Labor Productivity and Costs](https://www.bls.gov/productivity/); [BEA NIPA](https://www.bea.gov/data); [Census CPS](https://www.census.gov/programs-surveys/cps.html).

**R2:** Obtain Census ACS/AHS household incomes and housing cost-burden/rents, BEA PCE and BLS CE shares, KFF/MEPS premiums and out-of-pocket costs, NCES tuition/student debt, childcare price surveys, BLS ATUS time use, regional variation, income-shock and one-/two-earner scenario inputs. Explicitly log denominators, public-use restrictions and comparability. [Census ACS](https://www.census.gov/programs-surveys/acs); [BLS Consumer Expenditure](https://www.bls.gov/cex/); [BLS ATUS](https://www.bls.gov/tus/).

**R3:** Retrieve BEA NIPA labor shares with proprietor allocation, CBO income-distribution tables, Fed Distributional Financial Accounts / Survey of Consumer Finances, S&P buyback and dividend data under applicable licenses, EPI original executive pay tables, BLS historical/archived union member data, and dated IRS/CBO tax tables. [Fed DFA](https://www.federalreserve.gov/releases/z1/dataviz/dfa/); [CBO](https://www.cbo.gov/topics/income-distribution); [BLS Union Membership](https://www.bls.gov/news.release/union2.toc.htm).

**All runs:** Record source title, institution, stable URL/DOI, original table/series IDs, publisher date, retrieved date, licensing status, population and observation unit, denominators, rounding, transformations, full time coverage, revisions, alternative measures, known critiques, numeric source excerpts under permitted quotation rights, and uncertainty. Preserve competing estimates; do not collapse disagreements into a single preferred result.

## Unresolved strategic choices (owner decision; no selection made)

1. **[#1](https://github.com/BenWassa/great-decoupling/issues/1):** U.S.-only vs U.S. with limited comparable OECD context vs fully comparative; historical full-series coverage and change-point rule (1973 is a testable hypothesis, not an assumed breakpoint).
2. **[#2](https://github.com/BenWassa/great-decoupling/issues/2):** one income-band definition vs multiple transparent lenses vs worker-centered approach; size adjustment, nominal/real basis and clear R1-worker vs R2-household outcomes.
3. **Licensing and archival policy:** repo PDF/infographic author provenance, graphic reproduction permission, use of licensed third-party databases and stable snapshots are not yet approved. Do not assume repository's empty `LICENSE` file grants rights to embedded source material.
4. **Quantified “verified” gate:** current status records publisher source-matching only; final data-run release criteria, independent replication requirements and which series vintages to freeze need explicit approval after issues #1/#2.

## Validation / handoff

- **Audited:** three original PDFs, their embedded source lists, research plan, workflow plan, v1 PNG's repository identity; populated M01–M16, D01–D24 and E01–E22 status rows (62 distinct audit entries). This is **not** a complete list of every incidental year in prose; it covers each distinct empirical numeric proposition and the consequential derived/causal comparisons.
- **External spot checks (2026-10-24):** [Pew income definition and population](https://www.pewresearch.org/race-and-ethnicity/2024/05/31/the-state-of-the-american-middle-class/); [Pew calculator band](https://www.pewresearch.org/short-reads/2024/09/16/are-you-in-the-american-middle-class/); [Census P60-279](https://www.census.gov/library/publications/2023/demo/p60-279.html); [Aum & Shin 2020](https://www.stlouisfed.org/publications/review/2020/10/22/why-is-the-labor-share-declining); [BLS union 2024 archive](https://www.bls.gov/news.release/archives/union2_01282025.htm); [BLS December 2025 employment archive](https://www.bls.gov/news.release/archives/empsit_01092026.htm).
- **Not performed:** PDF image-by-image chart reproduction, statistically independent re-estimation, every URL's license/access check, data download and CI (repository currently has no applicable research-doc pipeline). Remaining entries explicitly retain status **needs verification**.
- **Downstream boundary:** this audit and the run-specific inventories in [templates/](templates/) are **inputs** to research, **not** evidence that R1, R2 or R3 is complete. No Claim Ledger, conclusions or production infographic changes.
