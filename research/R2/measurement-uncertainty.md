# R2 — Measurement changes, uncertainty, contested findings and exclusions

**Snapshot 2026-10-24; owned by issue #9 only.** This log documents observational inconsistencies rather than resolving pending owner decisions #1 and #2. Source IDs identify the exact original publishers and URLs in [source inventory](source-inventory.csv); direct numeric inputs are in [observations](data/observations.csv).

## Measurement-change and definition log

| ID | Source and periods | Change / population mismatch | R2 handling and necessary follow-up |
| --- | --- | --- | --- |
| MC01 | Census CPS ASEC 1984–2025 (S01/S21) | Historical income questionnaire, weights, population controls and annual income processing changed. Median of all households does not hold composition constant. | Use same latest Census-vintage nominal or real series as labelled; no individual wage inference. Audit detailed income methodology and fixed-household-type histories. |
| MC02 | Census real income 1984–2025 (S21) | FRED uses **R-CPI-U-RS pre-2000**, **C-CPI-U 2000–2025**, 2025 base. A composite deflator is not a single unchanged price index. | Describe explicit composite and maintain alternative CPI-U/PCE sensitivities; not comparable directly to independent price-basket conversions. |
| MC03 | CPS 2024 across releases (S01/S21) | The 2026 Census/FRED vintage lists **$83,160 nominal** for 2024 and **$85,210 in 2025 dollars**, which are different estimands; older release estimates can also be revised. | Show nominal versus real, report vintage and base year; no cross-vintage growth calculations without bridge. |
| MC04 | 2024 ACS vs CPS (S02/S01) | 2024 ACS B19013 **$81,604** in survey-year dollars; 2024 Census/FRED CPS **$83,160 nominal** in the current vintage. Survey sampling universes, time periods and income constructs differ. | Keep as different household surveys; do not quietly average or splice. |
| MC05 | ACS 1y versus 5y (S02/S03/S04) | ACS 1-year and 5-year are distinct reference populations with different small-area availability and precision, and estimates can change with sampling and weighting. | 2024 US and WA renter estimates use only **ACS 2024 1-year**. Future metros must use one coherent release, with geography and MOEs. |
| MC06 | ACS B25070 2024 (S04) | 2024 US **3,147,163** renter units in “not computed” category. A derived ratio has sampling covariance not recoverable from individual published MOEs. | Rent burden (bins 007–010)/(001−011) and severe burden 010/(001−011); list exclusions explicitly; no invented confidence intervals. |
| MC07 | Census/HUD new-home median price 1963+ (S05) | Quarterly sold-new-home transactions, not repeated same-property price, mortgage costs, existing-home stock, or income-matched homebuyers. Composition by home type and geography varies. | Price-to-all-HH-income diagnostic explicitly mixed-population, not a median buyer affordability estimate. |
| MC08 | Freddie Mac mortgage PMMS 1971+ (S06) | Survey design changed in **November 2022** and lender quotes are not each borrower's realized cost. | Identified for future mortgage-cashflow analyses; no spliced historical model in this pack. |
| MC09 | BLS CE (S07/S08) | CE is **consumer units**, not Census households; weighted average annual spending and shares are not median-family budgets. Diary/interview data, reporting, imputation and group mix vary over time. | Reproduce internally consistent 2021–2024 spending shares, never divide CE mean spend by CPS/ACS median income; 1984+ historical reclassification audit pending. |
| MC10 | KFF family-premium surveys (S09/S10) | 2026 employer sampling covers firms **10+ workers**; older employer-size universe differs. Mean family premiums describe enrolled covered employees, not all workers or households; plan and job mix change. | Show 1999 and 2026 nominal premium components separately; no inference about real or wage-relative premium trend without controls. |
| MC11 | CMS NHEA / BLS CE / KFF (S11/S07/S09) | CMS is national payer expenditure, CE consumer-unit outlays, KFF total and worker insurance premiums. Together they can double-count funding or combine distinct groups. | Do not add NHEA totals, CE healthcare expenditures and full employer premium into one family cash ledger. Only worker contributions enter modeled cash expenses. |
| MC12 | Census SIPP childcare 1985–2011 (S12) | Family with employed mother, children under age 15, childcare payments and provider participation; historical means in **constant 2011 dollars**; cash-payer composition changes. | +70.2% only within indicated sample/deflator; no current universal childcare price estimate. |
| MC13 | Redesigned SIPP childcare from 2014 (S13) | Changed questionnaire and collection/reporting means pre-2013 and redesigned post-2013 series cannot be assumed equivalent. | No splicing 1985–2011 means to current provider quotations; bridging study review pending. |
| MC14 | NCES Digest long-run postsecondary (S14) | Institution classification, Title IV eligibility, tuition/fees versus room/board and inflation adjustments differ across historical coverage. | Table identified; no forced homogeneous 1963–2023 paid-cost panel. |
| MC15 | NCES IPEDS 2014–2023 (S15) | Public four-year in-state institutional mean charges (constant 2023 USD) differ from net price, enrollment aid and loan repayment. | Selected same-table −11.7% real benchmark retained as counterevidence; document institution/FTE weighting on extension. |
| MC16 | Federal Student Aid loan portfolio (S20) | Federal loan balance is loan stock, excludes private liabilities and is not average debt per graduate or annual family debt service. | Primary source identified only; no unverifiable debt trend extracted. |
| MC17 | Federal Reserve SHED since 2013 (S16/S17) | Nominal $400 emergency has changing real value; cash-equivalent hypothetical response differs from all-sources ability to pay; the survey unit is **an adult**, not a household. | Separate 2013/2021/2025 responses and 2025 three-month savings answers; question wording and sample controls needed for longitudinal claim. |
| MC18 | Census families/living arrangements 1975–2025 (S18) | Share denominator = **all households**, not married couples or all people. Elderly, single, unrelated and childless household mix varies. | All-household share labels, no direct attribution to wage growth or work incentives. |
| MC19 | BLS ATUS 2003–2025 (S19) | Adult diary primary childcare vs secondary supervision and household totals; annual 2020 data disrupted. | 2025 mean hours are a cross-section, not full continuous historical caregiver burden. |
| MC20 | Constructed scenario budget (no survey estimator) | Effective tax fractions, nominal wages, paid care, rent, family coverage eligibility, other essentials, available savings and job-loss adjustments are researcher-chosen inputs. | Expose five cases and formulas; deterministic output cannot be extrapolated to household incidence. |

## Competing readings to retain

| Question | Reading A | Reading B / counterevidence | Disposition |
| --- | --- | --- | --- |
| Housing affordability trend | New-home price divided by CPS all-HH income changes from 3.49× (1984-Q1) to 4.84× (2025-Q1) | 2024 **renter** burden is separately measured by matched ACS B25070. Owners face different mortgage and tenure costs. | Different populations/time windows. No universal housing burden inference or 1973 boundary. |
| “National renter costs are 22% of income” | ACS median rent divided by **all-HH** median income yields ~21.9% | Matched ACS US 2024 computable renter units: **51.8%** at ≥30% gross rent-to-income; WA **50.7%** | **Reject** unpaired medians as actual renter burden. |
| Is healthcare burden all employer premiums? | KFF $28,303 total annual family coverage in 2026 | Worker-paid $7,471 contribution plus separate medical OOP; CMS national payer spending different | Separate full resource cost, payroll cash cost, OOP and net incidence. |
| Does childcare always rise? | SIPP payer mean increases in real 2011 USD 1985–2011 | Same population's payer participation, number/age of children and paid/unpaid care vary; later survey breaks | Narrow historic observation; all-family and current comparisons open. |
| Did public tuition rise in every era? | Long-run institutional series across earlier intervals | IPEDS recent public four-year in-state real institutional charge **decreased** 2014–2023 | Keep both definitions and coverage windows. |
| Did spending shares rise? | CE 2023→2024 housing **33.0→33.4%** | CE 2021→2024 housing **33.8→33.4%**; not an income share | Source-consistent endpoint dependence, not selective one-breakpoint story. |
| Is hypothetical $400 unaffordable for 37%? | 2025 SHED 63% choose cash-equivalent | Remaining respondents may use borrowing or another instrument; inability by *any means* is a distinct question | Reject complement-to-hardship translation. |
| Is one- or two-earner family more resilient? | One $100k-earner model has no paid care and positive flow | $60k+$40k-earner case retains remaining wage when one job is lost but has paid care in this model | Depends on tax, care, savings, insurance loss; no population-level directional statement. |
| Did median household real incomes improve? | Census S21 published real median 1984→2025 **+41.3%** | Family size, number of earners, composition, posttax and regional costs are different metrics | Specific result valid; broader viability change not established. |

## Uncertainty taxonomy

**Sampling.** Published ACS B19013 2024 US 90% MOE ±$128, B25064 ±$3, B25070 total renter units ±154,221 and ≥50% burden category ±70,576. Derived rent-burden ratios require joint covariance or replicate-weight procedures; treating category uncertainties as independent is not justified. CPS, CE, SIPP, KFF and SHED each use their own weighting and survey variance designs, not a common independent sample.

**Non-sampling.** Self-reported household income and spending, survey nonresponse, missing wages, imputation and recall; changing KFF employer responses; IPEDS classification and residency; changing new-home mix; SHED hypothetical wording.

**Unit and construct.** A worker may not live alone; a Census household may have zero, one or multiple earners; a BLS consumer unit is not necessarily an ACS household. A KFF “family coverage” holder is not necessarily a Census “family”. A renter **unit** is not an adult respondent; a school **institution** is not a student borrower. “Essential”, “discretionary” and “fixed” depend on observation horizon.

**Geography.** US/WA matched 2024 renter rent/income fractions show two differently composed geographies; one is not a counterfactual for the other. No 2024 state distribution proves historical regional changes. Rent and childcare synthetic scenario tiers are not attributed to specific cities or rural regions.

**Time and prices.** Nominal endpoints from different years cannot be treated as real levels. CPS composite adjusted-income series uses an explicit joined deflator. SIPP childcare constant 2011 dollars and IPEDS constant 2023 dollars are separate bases; no conversion or summing them. Historical start dates: new-home/MSPUS 1963, family arrangements 1975, CPS selected series 1984, SIPP childcare 1985–2011, KFF 1999+, ATUS 2003+, ACS 1-year matched burden modern era, SHED 2013+. No uniformly observed 1973 household budget.

**Simulation.** Models have exact arithmetic but synthetic inputs with no credible statistical confidence interval. An insurance premium change after job loss or childcare substitution can change the result substantially; neither is represented in the static three-month base stress.

## Disallowed calculations and rejected interpretations

- **Reject:** median ACS gross rent / median income among **all** US households as estimated median burden among renters.
- **Reject:** “middle-income family” defined using a 2026 national all-household median without a size, earners and tenure adjustment.
- **Reject:** full employer + worker KFF premium added to CE medical expenditures as household health cash cost.
- **Reject:** total annual BLS CE mean expenses subtracted from CPS median money income as “the median family's savings”.
- **Reject:** nominal 1999-to-2026 health premium growth quoted as inflation-adjusted or as workers' wage share.
- **Reject:** post-2013 SIPP redesign childcare prices appended to 1985–2011 payer means as though the instruments were equivalent.
- **Reject:** aggregate federal student loan stock as college price, median graduate debt, or net tuition.
- **Reject:** SHED hypothetical payment mechanism complement as proof of actual insolvency.
- **Withhold:** any empirical cross-era uniform one-earner and two-earner household budget without matched wages, actual taxes, benefits, childcare and region.
- **Withhold:** any claim that historical owner mortgages are affordable or unaffordable without matched buyer and payment data.
- **Withhold:** any causal statement linking the measured trends or assigning individual or institutional motives.

## Review and change control

Source inventory **reviewed** means selected displayed primary-table observations were inspected, not original microdata reweighted. Current **identified** sources requiring deeper extraction include mortgage PMMS (S06), full CE history (S08), redesigned childcare SIPP (S13) and federal student debt portfolio (S20). Further panels, metro stratification, expenditure-quintile data, family-type comparability and robust uncertainty estimates are **not yet independently replicated**. The 20+ source inventory is annotated, not an assertion that every observation on each primary site has been extracted.

To revise a result: verify its original table, geography, time, denominator, units, vintage and confidence method; update the relevant source inventory row and raw observation; rerun the Python stdlib model with --write, inspect the exhibits diff, run unit tests and --check. Never fill missing years with unsupported values. Owner issues #1 (scope and period), #2 (middle-income definition and equivalence) remain pending. Issue #7 owns shared template files; any schema coordination must map **within research/R2/**, without editing other project streams.
