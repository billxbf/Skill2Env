# Signal Reference

Every signal is read against the creative's own trailing baseline (see SKILL.md workflow step 3), never against an industry number. "Alone?" states whether a move in that signal, by itself, justifies any conclusion. Evidence tiers for the reference points at the bottom: **platform-documented**, **published research**, **practitioner heuristic** (no traceable primary source - always label it when quoting).

Which signals to pull first, when you cannot pull them all:

- diagnostic value per unit of effort to obtain: link CTR > hook rate > spend share within the ad set > first-time impression ratio > hold rate > CPM > CVR > frequency > CPA/ROAS
- effort, lightest first: link CTR == CPM == frequency == CPA (a real tie - all four sit in the same rows of the same default export, so pulling any one of them hands you the other three) > hook rate == hold rate (also a real tie - one video-retention breakdown produces both) > CVR (reconcile tracking first) > spend share (compute per creative from the export) > first-time impression ratio (Meta breakdown, or a new-user-reach proxy elsewhere)

The two orders disagree on purpose: the numbers that cost nothing to pull are the ones that mislead alone, which is what the two-signal rule exists to stop. Re-rank for the account before pulling anything - no video deletes hook and hold rate outright, a B2B account with single-digit weekly conversions demotes CVR and CPA below every engagement signal, and a non-Meta account demotes first-time impression ratio to whatever proxy the platform offers.

## Delivery and exposure signals

**Frequency** - average impressions per person reached in the period: `impressions / reach`.

- Class: lagging, confirming. Alone? No - the most misused signal in the field. Meta's own analytics team notes two structural flaws: it is reported at ad/ad-set/campaign level while fatigue happens at creative level, and it is a period average, not the marginal effect of the next impression. A creative at frequency 3.0 can be spent while another at 5.0 is healthy.
- Read: rising frequency plus decaying response confirms exposure pressure; rising frequency with stable response means nothing is wrong yet. Always split cold vs warm - warm audiences tolerate several times the cold-audience exposure.
- Platforms: all major platforms report it; only Meta exposes anything near creative-level granularity via breakdowns.

**Reach vs impressions** - unique people vs total deliveries; their ratio is frequency, but their _trends_ are separately useful.

- Class: leading for saturation. Alone? Directional only.
- Read: impressions climbing while reach flattens means the platform is recycling the same pool - the account is running out of new people before any creative wears out. Rolling month-over-month reach falling is an early saturation tell that moves before frequency looks alarming.
- Platforms: Meta, LinkedIn, TikTok natively; Google Display/YouTube via reach reports; not meaningful on search.

**First-time impression ratio** - share of the period's impressions that are someone's first exposure to the ad.

- Class: leading, primarily for saturation onset. Alone? Good early warning, still needs a response signal beside it.
- Read: falling ratio means deliveries are increasingly repeats. Practitioner interpretation of healthy prospecting sits around 65-80%, with below ~50% read as saturation approaching (Triple Whale; Flighted) - heuristic bands derived from Meta's Delivery Insights metric, not platform rules. On retargeting the ratio is low by design; do not read it there.
- Platforms: Meta (Delivery Insights). Elsewhere, approximate with new-user reach (TikTok reports daily new-user reach directly).

**Spend share within the ad set** - the creative's share of its ad set's spend, trended.

- Class: leading. Alone? Suggestive, needs confirmation.
- Read: under algorithmic delivery, a creative silently losing budget share with no manual change means the platform's own models are deprioritising it - an implicit fatigue read that arrives before your dashboards show it. Also check the mirror image: a sibling launch can take share from a still-healthy creative (that is mix shift, not decay - see the confounder file).
- Platforms: computable everywhere from per-creative spend; no platform labels it.

## Response signals

**Link CTR (outbound CTR)** - `link clicks / impressions`. Use link/outbound clicks, not "all clicks": all-clicks CTR counts reactions, comments, profile taps, and expands, which can hold steady or rise while actual intent collapses - it flatters a dying ad.

- Class: leading - usually the first response signal to move, high-volume enough to be statistically stable daily on most budgets. Alone? The cleanest single signal, but still needs a partner: a dip has many non-fatigue causes (placement mix, one bad day), and a _naturally low_ CTR (weak creative from day one) is not a _declining_ CTR (proven creative losing steam).
- Platforms: all. On Meta explicitly separate link CTR from CTR (all).

**Hook rate (3-second rate)** - `3-second video views / impressions` (Dara Denney's definition; Ben Heath frames it as the share watching past the first 3 seconds).

- Class: leading - on video it moves before clicks, and on TikTok it is typically the first thing to move. Alone? Strong for diagnosing _where_ decay lives: hook rate down with hold rate stable means the opening is tired, not the ad - rung 1 of the action ladder, its highest return per hour spent. Ben Heath reports that for many advertisers over 90% of viewers drop off before the four-second mark, which is why the opening carries so much of the fatigue load.
- Platforms: Meta, TikTok, YouTube, LinkedIn video - computed from 3-second (or platform-equivalent) view counts.

**Hold rate** - viewers still watching at a mid-point checkpoint over those who started; Denney uses viewers reaching 15 seconds; completion quartiles (25/50/75/100%) serve the same role.

- Class: leading/secondary - confirming, not primary. Alone? No.
- Read: hook rate stable with hold rate decaying points at the body/on-ramp, not the opening. Both decaying together is generic wear-out.
- Platforms: any platform with video quartile or watch-time reporting.

**Thumbstop** - static-ad and feed shorthand for the same construct as hook rate: the share of impressions that stop scrolling (3-second views on video, sometimes engagement-based proxies on statics).

- Class: leading. Alone? Same caveat as hook rate - a great thumbstop is not a great ad; clickbait shows high thumbstop with collapsed downstream metrics, so read the whole funnel.
- Platforms: computed, mainly Meta/TikTok vocabulary.

**CPM** - `cost per 1,000 impressions`.

- Class: leading but ambiguous. Alone? Misleading - CPM is set by the auction, not by your creative alone. Rising CPM with flat CTR is auction competition or seasonality (Q4, elections), not fatigue. Diagnostic only when paired with falling CTR: the platform pricing your deliveries up _while_ response falls is consistent with the system downgrading the creative.
- Platforms: all.

**CPC** - `spend / link clicks`. Arithmetic composite of CPM and CTR: CPC rising decomposes into "auction got pricier" (CPM up) or "creative stopped earning clicks" (CTR down). Always decompose before reading it.

- Class: derived. Alone? No - read its components instead.
- Platforms: all.

**Conversion rate (CVR)** - `conversions / link clicks`.

- Class: lagging, and the key _separator_. Alone? Its stability is the information.
- Read:
  - Costs rising with CVR stable is the fatigue pattern (people who still click still buy).
  - CVR degrading alongside engagement suggests saturation (the remaining pool is lower-intent).
  - CVR collapsing while CTR holds is a landing-page/offer/tracking problem that no creative refresh will touch.
- Platforms: all, subject to tracking integrity - screen tracking first.

**CPA / ROAS drift** - `spend / conversions`, `conversion value / spend`.

- Class: lagging - last to move; by the time CPA spikes the decay has been building for days. Alone? Never - low conversion volume makes daily CPA the noisiest number on the dashboard, and attribution lag makes trailing windows under-report recent days structurally.
- Read: confirmatory only, on lag-matched windows, after the leading signals have made the case.
- Platforms: all; B2B accounts should demote it below engagement signals entirely (see SKILL.md, B2B vs B2C).

## Platform rating systems

**Meta delivery statuses - "Creative fatigue" / "Creative limited"** - platform-documented statuses; industry sources (Jon Loomer; AdSights) report the fatigue status firing around a doubling of cost per result vs history, with "Creative limited" the milder tier.

- Class: lagging by construction. Read: useful as a backstop, not a detector - if these fire routinely, detection upstream is too slow.

**Google RSA / PMax asset labels - Learning / Low / Good / Best** - platform-documented, performance-based per-asset ratings. Read: the legitimate freshness signal on Google; replacing persistent "Low" assets is standard practice (the common 2-4 week cadence is practitioner advice, not a Google rule).

**Google Ad Strength (Poor-Excellent)** - measures asset diversity and completeness, **not performance**. Optmyzr's analysis found "Average"-strength ads with the best CPA/CVR and "Poor" with the best ROAS. Never treat Ad Strength movement as a fatigue signal.

## Attributed reference points

Quote these only as attributed starting references; the account's own baseline overrides all of them.

**Platform-documented**

- Meta "Creative fatigue"/"Creative limited" delivery statuses exist (Meta Business Help Center); the ~2x cost-per-result trigger is as reported by Jon Loomer and AdSights, Meta's page being closed to automated verification.
- Meta learning phase: roughly 50 optimization events per week per ad set for stable delivery; significant edits reset it (Meta Business Help Center).
- LinkedIn official guidance: rotate the lowest-engagement ad every 1-2 weeks; run 4-5 ads per campaign (LinkedIn Marketing Solutions, Sponsored Content best practices).
- TikTok guidance: refresh on the order of every 7 days / when delivery trends consistently down.

**Published research**

- Meta 2023 creative-repetition study (Analytics at Meta, Medium): mean exposure 4.2 per creative; ~45% drop in conversion likelihood at 4 exposures; click likelihood decaying as (N+1)^-0.43; adding a new creative in high-fatigue cases produced an average ~8% conversion-rate improvement; **no wear-in effect found for direct-response objectives**.
- Wear-in/wear-out lineage: Pechmann & Stewart (1988) - effectiveness rises, peaks, declines. Les Binet's wear-in effect (via Motion, motionapp.com/blog/why-ads-resist-creative-fatigue): some brand ads gain effectiveness with exposure.

**Practitioner heuristics (label as such every time)**

- Ben Heath: results drop-off often starts around frequency 2.0-2.5 on cold Meta audiences, with warm audiences commonly fine at 10+ (heathmedia.co.uk/facebook-ad-frequency/); "ad fatigue is usually hook fatigue", and over 90% of viewers drop before the 4-second mark for many advertisers (heathmedia.co.uk/scale-meta-ads-faster-by-testing-hooks/).
- AJ Wilcox / B2Linked: LinkedIn's delivery caps exposure by creative count - up to "7 in 48 hours" with 7+ creatives, roughly one per 24h with 1-3 creatives (b2linked.com/blog-page/linkedin-ads-frequency-caps-how-often-can-someone-see-your-ads).
- Baseline methods: 3-day moving average vs the creative's own trailing 14-day baseline (AdSights); rolling 7-day vs 30-day (Segwise). Sustained ~20-25% decline as the action band and 10-20% as watch-list (AdSights et al.) - adjustable defaults, not laws.
- Widely repeated but with no traceable primary source: frequency 2.5-3.0 prospecting flag, 4-6 retargeting tolerance, 20-30% CTR-drop band, ~18-25% CPM inflation, first-time-impression ratio <50%. Treat every one as folklore-grade until the account's own data confirms or replaces it.
