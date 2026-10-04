# Take-rate benchmarks: four architectures (2026 snapshot)

Every figure below is a dated snapshot of one platform's published terms, not an industry norm. Use the architectures and the ratios they imply. Re-verify any exact figure before quoting it in a strategy document, since marketplace terms change on announcement cycles measured in months.

## Zero take-rate - HubSpot Marketplace (2026 terms)

HubSpot charges no revenue share and no listing or certification fee. Quality gating (its listed/certified two-tier ladder) and monetization are fully separated design choices: the marketplace is funded as a retention and ecosystem asset for the core product, not as a revenue line.

Read: take-rate zero is a real architecture used at scale, not a transitional state a marketplace must grow out of.

## Volume-tiered take-rate - Shopify App Store

- 0% revenue share on a developer's first $1,000,000 USD in annual gross App Store revenue (in effect since January 1, 2025), then 15% above that - down from a flat 20% previously.
- Exception: developers earning $20M+ through the store in the prior year, or with $100M+ total company revenue, pay 15% on all revenue with no free tier, re-assessed annually.
- A flat 2.9% payment-processing fee applies to all billing, charged separately from revenue share.
- Theme developers keep 85% of Theme Store revenue - a materially better split than the post-threshold app tier.

Shopify explicitly markets its 15% ceiling as better than Apple/Google's 30%, positioning take-rate generosity as a developer-acquisition lever for the marketplace itself. The volume tier subsidizes small developers (the hard side of the network) while still monetizing the winners.

Enforcement note: apps that routed billing through Stripe directly to dodge the revenue share violated Shopify's terms. Several high-revenue apps reversed course under delisting threat. Circumvention pressure is proportional to the take-rate - see the failure modes in SKILL.md.

## Flat percentage plus fee stack - Salesforce AppExchange (2026 terms)

- 15% of net revenue for standard ISV partners, 25% for OEM partners.
- One-time $999 security-review fee per paid app, plus a $150 annual listing fee.
- Free apps (about 40% of the marketplace) pay no revenue share.
- A non-percentage flat-annual-fee contract exists for apps that don't fit the percentage model, priced by org/user count.

Scale context (mid-2026): 6,233+ apps listed. 91% of Salesforce's 150,000+ customers use at least one AppExchange app. A marketplace can become the procurement gate most enterprise deals route through - which is what makes a 15-25% take sustainable there and unaffordable for a marketplace still fighting for supply.

2026 strategic move: Salesforce rebranded/expanded the marketplace into "AgentExchange," adding AI agents and experts alongside apps while keeping the partner program and security review unchanged - repositioning an existing marketplace around a new complement type rather than rebuilding.

## Differential take-rate as a migration lever - Atlassian Marketplace

Atlassian ran two opposite revenue-share moves in the same 2026 cycle:

- Legacy Connect app commission scheduled to rise to 20%, then 25% - with the increase later delayed three months (January 1 to April 1, 2026).
- Its modern Forge hosting framework got a temporary 0% commission (100% of revenue to the partner) up to $1M in lifetime Forge revenue, replacing an earlier "5% commission in year one" incentive - and this favorable change was accelerated ahead of schedule.

Both moves ran under Atlassian's stated 6-months'-notice commitment for standard-rate changes. Read: take-rate can differ by hosting/architecture choice, pricing partner migration toward the platform's preferred technical model the way a cloud vendor prices egress. Favorable changes were sped up and unfavorable ones deferred - the notice discipline is part of the lever.

## What the four architectures imply for a new marketplace

- Take-rate is at least three-dimensional: level (0-25%), tier axis (volume, hosting model, partner type), and the fee stack around it (review fees, listing fees, payment processing).
- The mature, high-take platforms earn their rate through distribution the partner cannot replicate (AppExchange as procurement gate). A marketplace without that leverage charging the same rate selects against the supply it needs most.
- Every platform above pairs its rate with an enforcement mechanism (delisting) and, where the rate changed, a notice commitment. A take-rate without both is a number partners will route around or churn over.
