# R2 reproducible exhibits

Frozen primary-source observations, retrieved 2026-10-24; calculations from the accompanying CSV files.
**No population inference from constructed scenarios.** See definitions-methods.md and evidence-pack.md.

## E1 — Historical exposures and measurement sensitivity

| Diagnostic | Earlier observation | Later observation | Recomputed quantity | What this is NOT |
| --- | ---: | ---: | ---: | --- |
| New-home price / all-HH income (Census via FRED S05 + CPS S01) | 1984-Q1: 3.49× | 2025-Q1: 4.84× | change +1.35× | Not same buyers or mortgage-payment burden |
| 2024 national median gross rent / all-HH median income (ACS S02/S03) | $1,487/month rent | $81,604/year household income | 21.9% | NOT median renter burden; different denominators |
| KFF S09/S10 family coverage: worker share of premium | 1999: 26.6% | 2026: 26.4% | -0.2 pp | Not amount deducted as % household income |
| SIPP S12 paid childcare mean (2011-dollar weekly) | 1985: $84 | 2011: $143 | 70.2% change in reported real average | Not 2026 childcare price or all-family mean |
| IPEDS S15 public four-year in-state tuition/fees (constant 2023 USD) | 2014-15: $10,209 | 2023-24: $9,016 | -11.7% | Not net attendance cost or student debt |

## E2 — Expenditure shares, composition and financial-shock survey observations

| Series | Earlier | Later | Change | Unit / source |
| --- | ---: | ---: | ---: | --- |
| Housing spending share | 33.8% | 33.4% | -0.4 pp | CE CU 2021→2024 S07 |
| Health spending share | 8.1% | 7.9% | -0.2 pp | CE CU 2021→2024 S07 |
| Food spending share | 12.4% | 12.9% | +0.5 pp | CE CU 2021→2024 S07 |
| Would use cash-equivalent for $400 hypothetical | 50.0% | 63.0% | +13.0 pp | SHED adults 2013→2025 S16 |
| Married-couple share of all households | 66.0% | 47.0% | -19.0 pp | Census households 1975→2025 S18 |
| One-person share of all households | 20.0% | 29.0% | +9.0 pp | Census households 1975→2025 S18 |

Additional uncombined observations: 2024 CE mean CU spending $78,535, mean CU pretax income $104,207, mean CU health spending $6,197. SHED 2025: 55.0% adults report 3-month rainy-day savings; 30.0% cannot cover three months of expenses by the surveyed alternative means.

## E3 — Illustrative household commitments (2026 USD; NOT survey household medians)

| Scenario | Gross wages/yr | Effective tax (assumed) | Cash commitments/mo | Surplus or deficit/mo | Annual margin |
| --- | ---: | ---: | ---: | ---: | ---: |
| one_60k | $60,000 | 18.0% | $4,873 | -$773 | -$9,271 |
| dual_100k | $100,000 | 22.0% | $6,423 | $77 | $929 |
| one_100k | $100,000 | 22.0% | $4,873 | $1,627 | $19,529 |
| dual_low_cost | $100,000 | 20.0% | $5,273 | $1,394 | $16,729 |
| dual_high_cost | $100,000 | 24.0% | $8,773 | -$2,439 | -$29,271 |

Commitments = rent + paid childcare + other essentials + worker-paid family coverage premium/12 + debt/12. Tax is a synthetic fraction of gross wages; employer share of premium is excluded. All cases have $10,000 starting liquid savings. Childcare assumptions depend on earner arrangement.

## E4 — Liquidity and earner-loss stress (2026 USD; deterministic)

| Scenario | $6k shock shortfall* | $15k shock shortfall* | 3mo loss of earner 1 gap** | 3mo loss of earner 2 gap** |
| --- | ---: | ---: | ---: | ---: |
| one_60k | $0 | $7,318 | $4,618 | n/a |
| dual_100k | $0 | $4,768 | $1,468 | $0 |
| one_100k | $0 | $118 | $4,618 | n/a |
| dual_low_cost | $0 | $818 | $0 | $0 |
| dual_high_cost | $3,318 | $12,318 | $8,718 | $4,918 |

*Shock after three months of modelled baseline monthly surplus/deficit; savings plus net flows used before new borrowing. A zero shortfall does not imply a tolerable loss of savings.
**Gross wages of one earner cease for three months; wage-tax deduction proportionately reduced, all specified living costs unchanged. The gap is remaining negative cash after using $10k liquid savings; unemployment benefits and job-linked insurance loss are not modeled.

## E5 — Matched-income 2024 renter burden (ACS B25070, S04)

| Geography | All renter units | Not computed (excluded) | Computable units | Units at ≥30% income on gross rent | ≥30% share | ≥50% share |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| United States | 46,101,640 | 3,147,163 | 42,954,477 | 22,237,262 | 51.8% | 26.1% |
| Washington state | 1,175,739 | 56,522 | 1,119,217 | 567,874 | 50.7% | 23.8% |

Burden shares = sum of B25070 bins 007–010 divided by (001 minus 011); severe is 010 over the same denominator. These are sample-weighted 1-year ACS estimates, not household microdata reproductions. The published per-cell 90% margins of error do not directly supply a confidence interval for these derived ratios.

## Checks / non-comparability

- New-home medians and household medians describe different populations. Housing mixes, geography and mortgage rates are uncontrolled.
- Both childcare endpoints are reported in **constant 2011 dollars** for a restricted population. The post-2013 SIPP redesign is not spliced.
- BLS CE percentage changes are percentage-point differences of aggregate average-spending shares, not median-family expenses.
- KFF historical and current firm eligibility differs; 1999 vs 2026 dollar amounts are nominal; no inflation-adjusted comparison appears.
- Synthetic scenario rent, childcare, other living costs, tax rates, and savings are **assumptions**, not observed cost distributions.
- No missing periods filled, no regression/changepoint, no causal inference.
