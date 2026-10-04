# Partner-Type Economic Models and Money Flows

Pick the model that matches how money actually moves; the margin math is not interchangeable across types. Range figures below are mostly vendor or practitioner estimates - carry the source label into any memo that quotes them.

## Money flow by partner type

| Partner type                  | How money flows                                                                | Typical margin / fee range                                                                 | Evidence class                                        |
| ----------------------------- | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ----------------------------------------------------- |
| Referral / agency             | Referral fee as % of first-year ACV, one-time or recurring                     | 10-15% typical for software; 30-50% outliers exist                                         | Vendor/practitioner                                   |
| Reseller / VAR                | Discount off list; front-end margin + back-end rebate + MDF                    | 25-35% VAR gross margin; ~40% traditional on-prem discount; ~10% for a registered referral | Vendor/practitioner                                   |
| Distributor / two-tier        | Margin stacks across vendor → distributor → reseller → customer                | 8-15% distributor margin on top of reseller margin                                         | Vendor/practitioner                                   |
| MSP                           | Margin on wrapped managed services, recurring                                  | 45-60% managed-services gross margin best-in-class; 18-20% EBITDA top quartile             | Analyst + vendor benchmark (Service Leadership Index) |
| OEM / embed / white-label     | Royalty or revenue share, per unit or per customer                             | Royalty commonly 1-10% of license revenue; splits vary widely                              | Vendor/practitioner                                   |
| ISV / tech alliance / co-sell | Influenced revenue; marketplace listing fees; private offers; commit burn-down | Listing fee ~3% public SaaS; 1.5-3% private offers                                         | Platform documentation (primary source)               |
| Affiliate / creator           | CPA flat per action, or revenue share on recurring                             | SaaS 20-30% recurring; ecommerce 10-15% first order; fintech $50-200 CPA                   | Vendor benchmark                                      |

## Margin stacking and its fix

- Root cause is double marginalization (Spengler 1950, _J. Political Economy_): when successive firms with market power each add a markup, the end price exceeds what an integrated channel would charge and total output falls.
- Every added tier compounds the stack until the end price is uncompetitive or the economics stop supporting the value each party adds. Model the full stack for any two-tier structure, never one tier at a time.
- The peer-reviewed coordination fix is the two-part tariff (Jeuland & Shugan 1983; McGuire & Staelin 1983): supply near marginal cost plus a fixed fee, so no tier has an incentive to over-mark-up. Use it as a term-design lens when the stack breaks.

## Cloud marketplace mechanics

- Listing fees are the best-documented numbers in partner economics: ~3% for public SaaS offers, 1.5-3% on private offers (AWS primary source, 2024; Azure and GCP sit in the same ~3% band after both cut fees from far higher rates). Verify current schedules before quoting - they change.
- Committed-spend drawdown is the dominant enterprise buying motive: a marketplace purchase retires spend the buyer already committed to the cloud provider (AWS PPA/EDP, Azure MACC, GCP CUD), which is use-it-or-lose-it money.
- Model the drawdown nuance: a $1M qualifying marketplace purchase retires $1M of commit but costs the buyer $1M - versus roughly $800K for $1M of directly consumed services at a 20% discount. The buyer's calculus is not free money.
- Eligibility rules move: effective May 2025, AWS restricted commit retirement to SaaS hosted entirely on AWS, stranding vendors who relied on it. Check eligibility for the specific product, not the category.
- The win discount usually matters more than the fee: the discount conceded to close a marketplace or channel deal frequently dwarfs the 3% listing fee. Model both in the same stack.

## Services multiplier - handle with care

Vendor-commissioned analyst studies report partners earning $6.40-$7.13 in services per $1 of AWS sold, and up to ~$7 per $1 on other platforms (Canalys/Omdia, commissioned by the platform vendors). Useful for arguing the PARTNER's side of a Bech-style P&L - why the partnership is worth the partner's investment - but label it vendor-commissioned, never treat it as a neutral benchmark.

## Mode check before economics

Before modeling any of the above, confirm a partner channel is even the right mode for the synergy sought: ally-vs-acquire (Dyer, Kale & Singh 2004, HBR) and the transaction-cost make-vs-buy channel test (Anderson & Schmittlein 1984; confirmed by the 2006 AMJ meta-analysis). A wrong-mode relationship fails regardless of how the unit economics pencil out.
