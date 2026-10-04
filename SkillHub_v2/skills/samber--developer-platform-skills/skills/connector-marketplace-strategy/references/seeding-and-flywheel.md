# Seeding the two-sided network and measuring the flywheel

## The problem, named twice

The academic literature frames marketplace bootstrapping as a chicken-and-egg problem: a marketplace needs both complementors (app/connector builders) and consumers (customers who'll use those apps) to have a valid value proposition, but neither joins while the other side is empty. Reaching "critical mass" is likened to igniting an auto-catalytic reaction - below the threshold nothing sustains itself, above it the network feeds its own growth.

Andrew Chen's _The Cold Start Problem_ (2021) is the practitioner counterpart, with a five-stage arc: cold start, tipping point, escape velocity, hitting the ceiling, the moat. Two of his concepts transfer directly to a connector marketplace:

- **Atomic network** - the smallest self-sustaining unit of the network, not the eventual scale. "Start as small as your product will allow" and prioritize network _density_ over total size. For a connector marketplace, launch success is one tight, mutually-reinforcing cluster of complementors and users in a single use case - not a broad but thin catalog.
- **The hard side** - in any two-sided network, one side is naturally harder to attract, and that side determines whether the network survives. Chen names app-store developers explicitly as a hard-side example: "for app stores, these are the developers that actually create the products." Solve the hard side's problem first - win developers with a compelling reason to build (tooling, docs, revenue potential, audience reach) - and the easy side follows once real apps exist.

A related named tactic, credited to Chris Dixon: "come for the tool, stay for the network" - attract the hard side with a single-player-useful tool, then layer network value once volume exists (Instagram: photo filters first, social feed second).

## Naming the partner-mix axis

No framework was built specifically for app-marketplace partner tiers, but two named, citable ones map onto parts of the long-tail-builder vs. anchor-ISV vs. reseller split named in SKILL.md's operating-model bundle:

- Iansiti and Levien's keystone / dominator / niche-player typology (_The Keystone Advantage_, Harvard Business School Press, 2004) casts the platform owner as the keystone (later "landlord") and small complementors as niche players - academic grounding for the long-tail end, though it names no distinct anchor-ISV category.
- Sangeet Paul Choudary's orchestrator / non-orchestrator split - aggregator, integrator, and infrastructure roles versus niche producer, value-added reseller, and scale-supplier roles (Choudary, 2022) - is the closer conceptual match: niche producer reads as the long-tail builder, value-added reseller as the reseller tier. It comes from a newsletter, not peer-reviewed research, so weight it accordingly.

Neither replaces the platforms' own partner-program tiers, which formalize ISV vs. reseller as a category but split long tail from anchor only informally, through revenue thresholds or quality badges: Salesforce's ISV maturity ladder, Atlassian's Silver/Gold/Platinum tiers, Shopify's "Built for Shopify" badge.

## Four seeding strategies

Ranked in SKILL.md. Detail behind each rung:

1. **Seed with first-party complements.** The platform owner builds a handful of connectors itself before opening to partners, so day-one customers see value with zero external dependency. Near-zero coordination effort, limited scale - it cannot fill a catalog, only prove the category.
2. **Sequential one-side-first / "Trojan horse."** Ship a stand-alone tool that benefits the harder-to-attract side before any demand exists. Sourced case: Eventbrite launched as a ticketing SaaS for organizers alone, seeding supply before ever seeding buyer demand. Moderate effort, the most broadly applicable strategy.
3. **Subsidies / negative pricing.** Formal economic models solve the cold start by literally paying the initial cohort to join - build-fund grants, guaranteed revenue floors, zero take-rate windows. Moderate-to-high cost, fast if funded.
4. **Social mechanisms (hackathons).** Research found hackathons drive adoption through social contagion "over and above the effect of economic subsidies" - a compounding, slower-acting lever layered on top of the others, never a replacement for them.

## Two independent business cases - argue them separately

A connector marketplace has two distinct justifications, and a platform can act on the second even where the first doesn't yet apply at its scale:

1. **Ecosystem/distribution value.** More complements bring more platform value, compounding into the flywheel: the marketplace as a genuine multi-sided business.
2. **Retention/expansion value.** Customers who adopt multiple integrations churn less. One cited threshold: integrating 4+ tools into a workflow is where switching cost meaningfully rises, because customers who invest in learning an ecosystem are reluctant to rebuild that investment elsewhere. G2 buyer research puts integration capability at 86% importance in SaaS purchase decisions - marketplace breadth feeds sales-cycle conversion, not just post-sale retention.

A strategy document that blends the two cases can't be falsified. One that states which case carries the decision names what evidence would kill it.

## Flywheel measurement

No published industry thresholds exist for marketplace health at launch scale. The anchors below are single-platform data points, labeled as such. Baseline your own metrics in the first quarter and measure direction against yourself.

Demand side:

- Share of customers with ≥1 installed app/connector. Mature-platform anchor, not a target: 91% of Salesforce's 150,000+ customers use at least one AppExchange app (mid-2026).
- Installed integrations per account, watching the 4+ cluster (the cited switching-cost threshold) - the retention case made measurable.
- Retention/expansion delta between accounts above and below that cluster: the direct test of business case 2.

Supply side (the hard side - lead with these):

- Active partners with a live listing.
- Time from partner signup to first live listing.
- Share of catalog updated in the last two quarters - a stale catalog is the "expensive partner directory" failure becoming visible.
- Partner revenue concentration (share of GMV in the top few partners) - the trigger for the pooled-scale governance mechanism.

Flywheel coupling:

- Marketplace-attributed influence on new deals (integration capability cited in wins) and on churn saves. Direction matters more than precision. Attribution here is inherently soft - say so in the document rather than inventing a hard number.
