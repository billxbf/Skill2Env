# Strategy Archetypes

This file covers:

- the four structural axes
- the archetypes ranked by return per unit of effort, with the goal and evidence each one requires
- the documented eligibility thresholds (dated)
- the platform-label translation table

## The four axes

Every bid strategy on every platform is one combination of four choices:

| Axis                      | Options                                                                        | What it decides                                   |
| ------------------------- | ------------------------------------------------------------------------------ | ------------------------------------------------- |
| 1. Optimization objective | clicks/traffic · impressions/visibility · conversion volume · conversion value | What the algorithm is rewarded for                |
| 2. Constraint             | uncapped (maximize) · capped (target)                                          | Whether efficiency bounds the maximizer           |
| 3. Control type           | average-based goal · hard per-auction ceiling                                  | Whether individual auctions may exceed the number |
| 4. Signal scope           | single-campaign · shared/portfolio                                             | Whose data feeds the model                        |

**Axis 3 is the one people get wrong.** An average-based cost goal (target cost, cost-per-result goal, target return) holds the _average_ near the number - individual conversions can and will cost more.

A hard ceiling (bid cap, max cost-per-click) never bids above the cap in any single auction; it gives maximum control and carries the highest under-delivery risk, which is why platforms position it as expert-only. A user complaining "my cost cap was exceeded on this conversion" is almost always describing an average-based control working as designed, not a malfunction.

## Archetypes, ranked - goal, effort, return, evidence

Rows are ordered by efficiency: what the archetype returns per unit of effort, best ratio first. That ordering answers "which archetype is worth standing up", never "which one fits your goal" - the goal column and the evidence column both gate every row, and a goal the account actually has beats any ratio.

| #   | Archetype - what it does                                                                                       | Goal it serves                                           | Effort to stand up                                                                                                                                                                                                  | What it returns                                                                                                | Evidence required before recommending it                                                                                                   |
| --- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| 1   | **Cost-goal** - volume-maximizing constrained by an average cost target                                        | Hold an average acquisition cost                         | About an hour of derivation, once, plus a standing review cadence                                                                                                                                                   | Cost control at the efficiency the account already achieves - the most available without building anything new | Target derived from economics AND trailing actuals; tracked event predicts revenue                                                         |
| 2   | **Volume-maximizing** - spends the full budget for maximum conversion count, no cost constraint                | Most conversions within a fixed budget                   | Near-zero: no target to derive                                                                                                                                                                                      | Signal accumulation and a fully spent budget; no cost control at all                                           | Primary conversion event is valid; budget and conversion lag understood; worst-case efficiency affordable                                  |
| 3   | **Return-goal** - value-maximizing constrained by an average return floor; the most data-hungry archetype      | Hold an average return                                   | Highest: value pass-back built first (about a week where a values feed exists, a quarter where it does not), plus margin derivation and a volume gate; the only archetype whose setup crosses ads, data and finance | Margin-aware spend - the largest return of any archetype, once it is standing                                  | Value evidence in row 4, PLUS volume clearing the documented minimums below, PLUS margin-derived break-even return                         |
| 4   | **Value-maximizing** - spends the full budget for maximum total value; prefers fewer, higher-value conversions | Most conversion value within a fixed budget              | The same value pass-back build as row 3, without the margin derivation                                                                                                                                              | Mix shift toward high-value conversions; no margin control                                                     | Values complete, differentiated (two or more distinct values), timely, net of refunds where material                                       |
| 5   | **Delegated (AI-default campaign type)** - the platform chooses bidding, targeting and placement jointly       | None - delegate the whole policy                         | Near-zero to switch on; the real work is guardrails, exclusions and an exit criterion                                                                                                                               | Platform-wide inventory access, bought with control and diagnosability                                         | Treat adoption as delegating the bidding policy: clean conversion signal, exclusions/guardrails configured, an exit criterion written down |
| 6   | **Manual/exploratory** - you set per-unit bids; no conversion-probability adjustment                           | Price discovery, tiny audiences, strict per-unit control | Cheap to start, a standing weekly job to run                                                                                                                                                                        | Per-unit control and price discovery on a narrow surface                                                       | An owner for weekly review; a written stop condition or graduation criterion                                                               |
| 7   | **Visibility** - bids to appear a chosen share of the time in a chosen position                                | Share of voice / brand defense                           | About an hour                                                                                                                                                                                                       | Presence, not efficiency - there is no acquisition outcome to rank                                             | Outcome is genuinely visibility; placement and frequency constraints explicit                                                              |

The other axes disagree with that order, so read them separately instead of blending them into one rank:

- effort: **3 > 4 > 1 > 6 > 5 == 2 == 7**
- value: **3 > 1 > 4 > 2 > 5 > 6 > 7**
- compliance cost: **3 == 4 > 5 > 1 == 2 == 6 == 7**
  - Rows 3 and 4 send customer or deal values to a platform: they trigger consent, data-processing and residency review before a single bid changes, and sharing that data is hard to walk back.
  - Row 5 hands placement choice to the platform: an ad-policy and brand-safety review rather than a data one.
  - The rest move no data and need no sign-off.

**Default rung: cost-goal (row 1)**, as soon as the tracked event is valid. What moves you up one is evidence, not ambition: real differentiated values flowing back, clearing whatever the platform currently documents as its return-goal minimum. Losing that evidence moves you back down.

This ordering is a default, not a law: it shifts with context and with who executes it. Re-rank it against what you already know about the user before recommending anything.

- An in-house data team that can ship value pass-back in days collapses the effort of rows 3 and 4.
- An agency retainer with a standing analyst makes row 6 cheap.
- An account whose transaction values already flow back has paid row 3's setup cost and should read it as near-zero effort.
- A privacy regime or a legal team that will not approve sending deal values to a platform deletes rows 3 and 4 outright, whatever their return.
- A brand-defense or compliance mandate makes row 7 the only admissible rung regardless of its ratio.

Manual bidding is a durable strategy, not only a bootstrapping phase. Legitimate long-term manual homes include:

- brand-defense terms, where automation overpays for near-certain clicks
- very small high-intent audiences, where automated delivery underspends or inflates prices
- accounts whose approval chain forbids untargeted spend

## Documented eligibility thresholds

The critical correction, from vendor documentation read directly:

> "Advertisers can start using Target CPA with no conversion history, and Target CPA is effective for campaigns of all sizes." - Google Ads Help, About Target CPA bidding

- The **cost-goal** strategy (Google Target CPA) has **no documented conversion-volume minimum**. The only stated prerequisite is working conversion tracking.
- The widely repeated "15 conversions in 30 days for Target CPA" is a conflation: that figure is real Google documentation, but it belongs to **Target ROAS** (the return-goal strategy).
- "Measure over 30+ conversions" is an **evaluation sample** (judging whether it works), not an **enablement gate** (being allowed to turn it on). Merging those two kinds of number is the single most common source of threshold folklore.
- "50 conversions" figures are reliability recommendations (Meta's ~50 optimization events per ad set per rolling 7 days; a Google Demand Gen recommendation) - guidance, not gates.

Documented return-goal (Target ROAS) minimums by Google campaign type:

| Campaign type     | Documented minimum                                                     |
| ----------------- | ---------------------------------------------------------------------- |
| Search / Shopping | 15 conversions in past 30 days                                         |
| Display           | 15 conversions with valid values in past 30 days, across all campaigns |
| App               | 10 conversions/day, or 300 in 30 days                                  |
| Demand Gen        | 50 conversions in past 35 days, 10 of them in the past 7               |
| Video Action      | 30 conversions in past 30 days                                         |
| Hotel / Travel    | ~50 conversions per week                                               |

Learning-phase figures documented elsewhere:

- Meta: ~50 optimization events per ad set per rolling 7 days (framed as guidance, "not a penalty")
- TikTok: volatility declines after ~25 results or 7 days; ~50 conversions is the "most significant indicator" of exit
- LinkedIn: direct fetch of LinkedIn's own bid-strategy help page confirms a named "learning phase" exists for maximum delivery bidding ("the ad set enters a learning phase, which allows Campaign Manager to gather auction data... results might fluctuate during the learning phase"), but no minimum conversion count or duration is published anywhere - only cost cap and manual bidding have no learning phase mentioned at all. The absence of a numeric threshold, not the absence of the concept, is why tiny-volume B2B accounts still function there.

These numbers drift within a year (strategy renamings, consolidation of standalone target strategies into maximize-with-optional-target, behavior changes for budget-limited target campaigns all happened across 2025-2026). Cite them with the as-of date and re-verify against the live help page when the harness can browse.

## Platform-label translation - an observed capability, not a translation

Identically-named strategies on different platforms are not mechanically identical, and labels change yearly. Use this table to _locate_ the archetype in a given account UI, never to assume equivalent auction behavior:

| Archetype                      | Google Ads                                                                | Microsoft Ads                       | Meta                                         | LinkedIn                                | TikTok                                          | Amazon Ads                        |
| ------------------------------ | ------------------------------------------------------------------------- | ----------------------------------- | -------------------------------------------- | --------------------------------------- | ----------------------------------------------- | --------------------------------- |
| Volume-maximizing              | Maximize conversions                                                      | Max Conversions                     | Highest Volume (was Lowest Cost)             | Maximum delivery                        | Maximum Delivery                                | Dynamic bids up-and-down          |
| Cost-goal                      | Target CPA                                                                | Target CPA (inside Max Conversions) | Cost Per Result Goal (was Cost Cap)          | Cost cap                                | Target CPA (was Cost Cap, renamed 2026)         | Target-ACOS via rules/tools layer |
| Value-maximizing / Return-goal | Maximize conversion value / Target ROAS                                   | Max Conversion Value / Target ROAS  | Highest Value / ROAS Goal (was Minimum ROAS) | - (not offered)                         | Value optimization / Target ROAS (was Min ROAS) | not native                        |
| Hard ceiling                   | Portfolio bid limits only (min/max on portfolio strategies, not standard) | Max CPC                             | Bid Cap                                      | Manual bidding (max CPC)                | Bid Cap                                         | Fixed bids                        |
| Visibility                     | Target impression share                                                   | Target Impression Share             | Reach/frequency (CPM)                        | Maximum delivery on awareness objective | Reach/CPM                                       | Placement modifiers               |
| Manual                         | Manual CPC (Enhanced CPC retired for Search/Display, 2025)                | Manual CPC; Enhanced CPC retained   | Bid Cap is the closest                       | Manual bidding                          | Bid Cap                                         | Fixed; Dynamic down-only          |

Notes worth keeping:

- **Renaming churn is constant.**
  - Google folded Target CPA/ROAS into Maximize-with-optional-target, then reverted the labels (June 2026).
  - Meta renamed Cost Cap and Minimum ROAS.
  - TikTok renamed Cost Cap/Min ROAS to Target CPA/ROAS.
  - The archetype survives; the label does not.
- **Delegated campaign types** (Google Performance Max, Meta Advantage+, TikTok Smart+) use automated bidding exclusively - adopting one _is_ the bidding decision.
- **ROAS unit conventions differ**: web platforms report a multiplier (4.2x); mobile-UA tooling often reports a percentage (150%+). Normalize before comparing, or a 100x misread is possible.
- Amazon layers placement adjustments _before_ dynamic bidding - order of operations differs from search platforms.
