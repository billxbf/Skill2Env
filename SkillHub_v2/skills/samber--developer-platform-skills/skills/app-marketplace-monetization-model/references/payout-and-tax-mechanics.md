# Payout mechanics and the tax layer

Payout schedules and tax rules change - re-verify before publishing a timeline or a tax split. **Nothing here is tax advice**: state-by-state and country-by-country rules vary, and sellers frequently retain filing or nexus obligations even when a platform remits the tax; route the published split through qualified counsel.

## Seven-platform payout comparison

Payout speed tracks the merchant-of-record choice: platform-as-MoR stores hold funds longest; direct managed-rails configurations pay fastest.

| Platform                         | Frequency                                                                           | Minimum                     | Holds/reserves                                                                                                                                           | Time to bank                                                                                                             |
| -------------------------------- | ----------------------------------------------------------------------------------- | --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| Apple App Store                  | Monthly (per fiscal month)                                                          | ~$150 (region-dependent)    | Fiscal-month-close tax/refund netting                                                                                                                    | Within 45 days of fiscal-month close (documented); ~33 days typical, up to ~68 days from sale (community-reconstructed)  |
| Google Play                      | Monthly, starts the 15th                                                            | $1 most regions             | None published                                                                                                                                           | EFT 2-3 business days after the 15th → ~30-45 days from sale                                                             |
| Microsoft Commercial Marketplace | Monthly                                                                             | $50 combined                | 30-day credit-card escrow on top of the cycle; future payouts withholdable to recover write-offs                                                         | Cycle + 30-day escrow (credit card); 30 days post customer invoice (EA)                                                  |
| Atlassian (Paid via Atlassian)   | Monthly                                                                             | No published dollar minimum | 30-day refund/chargeback window (31-60 at Atlassian's discretion)                                                                                        | ~30 days after month-end, max 60; only for sales where Atlassian received final payment                                  |
| Shopify App Store                | Rides the merchant's ~30-day invoice cycle                                          | None separate               | Shopify absorbs chargeback handling                                                                                                                      | Same cycle as the merchant's Shopify invoice; payout at partner-account level, not per app                               |
| Salesforce AppExchange Checkout  | Not published - governed by the partner's own connected Stripe account              | Not published               | Stripe's standard new-account hold (inferred, not Salesforce-confirmed)                                                                                  | Stripe standard rolling (~T+2). A documentation gap, not a withheld commitment - never quote a fixed Salesforce schedule |
| Stripe Connect (build-your-own)  | Daily rolling default; configurable daily/weekly/monthly; Instant ~30 min for a fee | Platform-configurable       | Fixed reserves (to a release date) or rolling reserves (% on a rolling window, e.g. 30 days); 7-14 day new-seller hold is a common platform-added policy | Fastest of the seven - entirely platform-configured                                                                      |

**How to read it for a design**: minimum thresholds cluster in a $50-$150 range - small enough that active developers clear them every cycle. The cash-flow lever developers actually feel is the multi-week hold/escrow period. Working-capital modeling should use the real lag (~33-68 days at the slowest archetype; cycle-plus-30-day escrow at another), not the headline "monthly" or "within 45 days" language. The operator's published timeline should state the honest end-to-end number.

**Cross-border**: every platform-as-MoR store converts payouts to the developer's bank-account currency and absorbs FX conversion and payment-rail choice; the developer never picks a rail. An operator adopting the marketplace-billed posture inherits that same role - budget it as part of the posture.

## US: marketplace-facilitator statutes

_South Dakota v. Wayfair_ (2018) let states tax remote sellers on economic nexus; states responded with marketplace-facilitator laws shifting the calculate/collect/remit obligation - and liability for errors - from individual sellers to the marketplace itself. The Tax Foundation counts 38 dedicated facilitator regimes among the 45 sales-tax states; all sales-tax states have some form of economic nexus for facilitators. It is a state-by-state framework, not federal:

- Some states exclude local taxes.
- Some still require sellers to file informational returns.
- Marketplace sales may still count toward a seller's own nexus thresholds even when the marketplace remits.

## EU: the deemed-supplier rule

Since July 1, 2021, the EU's e-commerce VAT package (Article 14a) treats an electronic interface facilitating certain **B2C** supplies as if it bought and resold them itself, making the platform liable to collect and remit VAT: one commercial sale splits into a B2B leg (seller → platform) and a B2C leg (platform → consumer). Three mechanics apply:

- OSS lets a business file one VAT return covering all 27 member states.
- IOSS covers imports ≤€150.
- A €10,000 distance-selling threshold applies, below which home-country VAT can still be charged.

The 2025 ViDA package extends deemed-supplier treatment to more platform categories: scope is widening, not narrowing. B2B cross-border VAT is typically reverse-charged to the business buyer instead, which is why a purely B2B-buyer marketplace faces a lighter version of this layer.

## The split is never a binary toggle

- **Microsoft** splits by country: in Microsoft-Managed countries it is agent/commissionaire and calculates/collects/remits; in Publisher/Developer-Managed countries the publisher carries sole responsibility for registration, collection, remittance, and tax invoices.
- **Salesforce** splits by tax regime: Checkout calculates, collects, and remits **US sales tax** on the partner's behalf, but is deliberately not the general MoR for VAT. "You're responsible for VAT registration, maintaining required data, and distributing the taxes that you collect" holds internationally, even though Checkout can collect the VAT amount at the point of sale.
- **Apple, Google, Atlassian** (platform-as-MoR): the legal requirement and the commercial choice point the same direction - the platform collects and remits in most jurisdictions.

A well-designed marketplace publishes its split explicitly - which tax, which country, whose obligation - rather than leaving developers to discover it jurisdiction by jurisdiction.

## Mechanics under managed rails, and the silent-failure trap

Stripe Tax assigns liability explicitly (`automatic_tax.liability`: `self` for the platform, `account` for the developer), and the practical determination follows the charge type - direct charges make the developer MoR, destination charges usually the platform. A platform passing tax liability to developers must also give each developer its own registration surface, not just flip a flag on its own account.

The trap worth engineering around: enabling automatic tax calculation with **no active registration** in a jurisdiction returns no error and silently collects $0 tax - and under-collected past transactions cannot be retroactively corrected. Payout mechanics and tax mechanics are two independently failure-prone systems; neither's health is visible from watching the other, so verify tax collection with its own monitoring.
