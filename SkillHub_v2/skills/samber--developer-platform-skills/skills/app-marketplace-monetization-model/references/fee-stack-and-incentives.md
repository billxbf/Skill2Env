# Fee stacks and incentive programs - named benchmarks

Figures and effective dates go stale - re-verify any number before publishing it in a live fee schedule. Take-rate _level and tier architecture_ (which percentage, which tiers, zero-take-or-not) belongs to `samber/developer-platform-skills@connector-marketplace-strategy`; this file covers the instruments and incentive programs that implement it.

## Named fee stacks

- **Salesforce AppExchange** - the full-stack archetype: 15% of net revenue for standard ISV partners (25% OEM), plus a one-time $999 security-review fee per paid app and a $150 annual listing fee. Free apps (~40% of the marketplace) pay no revenue share; a flat-annual-fee contract exists for apps that don't fit the percentage model. Every instrument type appears in one stack: revenue share, review fee, listing fee, and flat-fee fallback.
- **Shopify App Store** - the low-friction stack:
  - One-time $19 partner-registration fee.
  - 0% revenue share on the first $1M of **lifetime** gross App Store revenue, 15% above.
  - A flat 2.9% payment-processing fee, charged as a separate labeled line, not folded into the share.

  Very large developers ($20M+/year through the store, or $100M+ company revenue) pay 15% on everything, reassessed annually.

- **Atlassian Marketplace** - the differential-rate stack: within Paid via Atlassian, the rate depends on hosting framework - Forge stepping 15% → 16% → 17%, Connect stepping 15% → 20% → 25% (steps extended to April 1 and October 1, 2026). Only apps exclusively on Forge modules, Forge auth, and Forge UI get Forge rates; any Connect module present gets Connect rates.
- **HubSpot App Marketplace** - the zero-take contrast: no revenue share at all; the marketplace is funded as a retention asset. Zero-take is an architecture, not a transitional embarrassment - and it needs no collection instrument, which is why the monetization build should wait for a non-zero rate.
- **Apple App Store / Google Play** - the consumer-store baseline the B2B stacks position against: 30% headline, 15% small-developer tiers (below). Shopify explicitly markets its 15% ceiling against this 30% - take-rate generosity used as a developer-acquisition lever.

## Waiver and incentive programs, by shape

Fee waivers are a standard menu item across major marketplaces, not an exceptional discount. The programs cluster around a **$1M revenue threshold** as the near-universal cutoff - an operator picking its own threshold has strong precedent to anchor there rather than invent a number.

**Revenue-exemption tiers:**

- Apple Small Business Program (since Jan 1, 2021):
  - 30% → 15% for developers with ≤$1M prior-calendar-year proceeds.
  - Crossing $1M mid-year reverts to 30% for the rest of the year.
  - Associated accounts aggregate toward the cap.
  - **Enrollment is manual.**
- Google Play (since July 1, 2021): 15% on the first $1M of earnings, resetting annually; subscriptions at 15% from Jan 1, 2022. A March 2026 restructuring moves toward a 10% base service fee on the first $1M plus a separate 5% billing fee (rollout from June 30, 2026 in US/EEA/UK), keeping the effective rate near 15% for most developers. **Enrollment is manual.**
- Shopify: the 0%-under-$1M tier became a **lifetime** cap as of Jan 1, 2025 (previously an annual reset; earnings before that date don't count toward the threshold) - a one-way tightening, and the one exception to the annual-reset pattern. Deciding annual-vs-lifetime is a real design choice, not a detail.

The enrollment lesson: on both manual-enrollment programs, a qualifying developer who misses the paperwork silently pays the full rate. An operator's own program should default eligible developers in if the waiver is meant to change behavior rather than exist on paper.

**Migration incentives:**

- Atlassian's Forge 0% incentive: 0% revenue share on eligible Forge apps up to $1M lifetime Forge revenue (aggregated per partner company), replacing an earlier 5%-in-year-one incentive; an accelerated "Runs on Atlassian" variant lets qualifying apps keep 100% up to the same cap. Paired with the Connect rate _increases_ above - favorable changes accelerated, unfavorable deferred, both under a stated six-months-notice commitment.
- Microsoft's renewal discount: 50% off the marketplace transaction/agency fee on private-offer and multiparty renewals via self-attestation, explicitly covering migrations of existing paid agreements onto the marketplace - a retention lever aimed at deals the platform didn't originally win.

**Behavior-based discounts:**

Each pays for a named pricing, packaging, or architecture choice rather than a revenue level.

- Google's subscription-vs-one-time split (subscriptions get the lower rate)
- Atlassian's framework split (Forge cheaper than Connect)
- Atlassian's solution-partner reseller discounts off list price

## Enforcement precedents

- **Anti-circumvention with a delisting path**: several high-revenue Shopify apps routed billing through an external processor to dodge the revenue share, violating the partner terms, and reversed course under delisting threat. "Pay through us" is a governance rule enforced by removal, not a pricing preference - and circumvention pressure rises with the rate.
- **Notice-period commitment**: Atlassian's standard-rate changes carry a stated six-months-notice commitment; its 2026 Connect increases were deferred three months while the Forge benefit was accelerated. Adopt the notice period before the first rate change, and publish it with the fee schedule.
- **Compliance delisting**: Salesforce's May 2026 mandatory security controls for connected apps, with non-compliant apps delisted - a mature marketplace uses delisting as its enforcement lever for security and for revenue rules alike.
