# Merchant-of-record postures and billing rails

Marketplace monetization mechanics vary across platform implementations. Platform rates and dates shift - re-verify before quoting them in a live design.

## The one upstream fork

"Who bills the end customer" is not one choice among several - it is the single fact that determines four downstream systems at once:

|                              | Marketplace-billed (platform-as-MoR)             | Developer-billed (vendor-as-MoR)                    |
| ---------------------------- | ------------------------------------------------ | --------------------------------------------------- |
| Merchant of record           | The marketplace operator                         | The app developer                                   |
| Tax liability default        | Platform                                         | Developer                                           |
| Chargeback/dispute ownership | Platform absorbs and manages                     | Developer's own responsibility                      |
| Pricing models offerable     | Capped by what the marketplace checkout supports | Whatever the developer's own billing stack supports |
| Take-rate collection         | Netted at source before payout                   | Self-reported/audited, owed separately              |
| Payout                       | Platform pays out net revenue on its schedule    | Developer collects gross directly                   |

The marketplace-billed branch earns its complexity by being the only one that lets the operator bundle tax compliance, chargeback handling, licensing/entitlement automation, and revenue reporting into one developer-facing promise - "we handle the business-operations toil, you handle the product." Developer-billed is cheaper for the operator (it builds less) but pushes every one of those systems onto each developer individually, a real adoption-friction cost to weigh against the take-rate charged.

## Charge patterns under managed rails (Stripe Connect)

The charge pattern is what technically decides merchant of record:

| Pattern                      | MoR                               | Platform fee                                | Use                                                                                                       |
| ---------------------------- | --------------------------------- | ------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| Direct charges               | The developer (connected account) | `application_fee_amount`                    | Developer-billed; developer's name on the customer statement, developer handles own disputes              |
| Destination charges          | The platform                      | `application_fee_amount` or transfer amount | Marketplace-billed default; auto-pays the developer on payment success - not for hold-and-release         |
| Separate charges & transfers | The platform                      | Manual (transfer less than charge)          | Marketplace-billed with delayed/gated/split payouts - required whenever payout isn't "instant on payment" |

Stripe's own guidance: do **not** use `on_behalf_of` for marketplace use cases - it keeps the charge on the platform while making the developer MoR, a mismatch most operators don't actually want.

## Account-configuration dials and the two bundles

Stripe's Connect Accounts v2 replaced fixed account types with three independent dials:

- Dashboard access (`express`/`full`/`none`)
- Fee collection (`stripe`/`application`)
- Loss liability (`stripe`/`application`)

The compatibility matrix collapses them into two coherent bundles:

- **Marketplace-shaped**: express dashboard, platform collects fees, platform carries losses, destination or separate charges. Hard rule, not preference: any non-direct charge pattern **requires** the platform to carry losses - combining them with `losses_collector: 'stripe'` is blocked, and near-miss combinations silently shift liability onto the platform.
- **SaaS-shaped**: full dashboard, Stripe bills the developer, Stripe carries losses, direct charges only.

Cost of the marketplace bundle to model per active developer: roughly £1.60/month per active express-dashboard account, plus 0.25% and £0.20 per payout (Stripe UK pricing, varies by region), on top of standard processing. At low per-developer volume, the flat fees can exceed the percentage collected.

## Per-platform postures (2026 landscape)

- **Apple App Store, Google Play**: pure platform-as-MoR (agent/commissionaire); platform owns tax, chargebacks, pricing ceiling. Neither natively supports usage-based billing.
- **Microsoft Commercial Marketplace**: platform-as-MoR agency model, and the one platform-billed archetype here that natively supports usage-based/metered billing - proof "marketplace-billed" and "no usage pricing" are separate constraints.
- **Shopify App Store**: marketplace-billed one step beyond destination charges. App charges consolidate onto the merchant's existing ~30-day Shopify invoice ("charges are directly added to the merchant's Shopify invoice"), and Shopify "handles all chargeback-related processes" plus billing, trials, proration, upgrades/downgrades. Supports recurring, usage-based, and one-time charge types. This invoice-consolidation shape requires already being the customer's primary biller - the precondition most operators lack but can approximate with destination charges.
- **Salesforce AppExchange Checkout**: marketplace checkout branding over Stripe rails underneath; supports one-time and subscription plans plus coupons and trials - **no usage-based pricing**, the sourced case of rails capping the developer pricing menu. Pairs the payment rails with two separable systems: the License Management App (entitlement provisioning) and Checkout Management App (partner revenue reporting) - a monetization stack is at least three systems (payment, entitlement, reporting), and a design covering only payment leaves two unspecified.
- **Atlassian Marketplace**: runs the full fork as internal policy - "Paid via Atlassian" (platform-as-MoR: Atlassian bills, licenses, handles tax and refunds, pays out net) versus "Paid via Vendor" (vendor-as-MoR, vendor keeps 100% but carries payment, tax, and disputes). Cloud apps can no longer list as Paid via Vendor except narrow requested exceptions - the configurable posture exists as a closing legacy branch, not an open choice. Independently of that fork, the Forge-vs-Connect hosting choice sets the _rate_, not the MoR: "who bills" and "what rate" are two separable dials.

## Tax status is not MoR

Stripe's documentation distinguishes marketplace-facilitator/deemed-supplier status (tax law) from merchant of record (card-network status): the two "are legally distinct and don't always coincide." The charge pattern determines the card-network MoR; tax liability can attach to a different entity by statute regardless - the legal frameworks are covered in this skill's payout-and-tax reference, linked from SKILL.md.
