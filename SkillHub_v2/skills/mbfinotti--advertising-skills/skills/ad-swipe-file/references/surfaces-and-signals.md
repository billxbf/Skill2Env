# Public transparency surfaces and signal inference

## What a public ad transparency surface is

Most major ad platforms now publish a public, searchable surface listing ads they serve: the creative, the advertiser's identity, and usually run dates. These surfaces exist mainly because regulation forces them to, which shapes exactly what they show. Three durable facts hold across all of them:

1. **Coverage is uneven.** Some surfaces list all ads. Others list only political/advocacy ads, only verified advertisers, only certain regions, or only _active_ ads with no archive. Never assume a surface's coverage: check what the specific surface claims, and record `unknown` when coverage can't be confirmed.
2. **EU-served ads disclose far more.** The EU Digital Services Act (Article 39) obliges very large platforms to publish, for ads shown in the EU, the advertiser and payer, run period, targeting parameters, and reach per member state - fields hidden everywhere else. This creates a two-tier internet: the same global campaign reveals targeting and reach in its EU view and nothing elsewhere.

   **Set the surface's country filter to an EU member state deliberately, even when researching a non-EU market.** This is the highest-value free signal available and the most underused.

3. **Historical depth is bounded.** Disclosure obligations lapse roughly one year after an ad last runs, and non-political ads often vanish the moment they are paused. A swipe file is the only durable archive you will have - which is why dated pulls are never overwritten.

What no public surface exposes for commercial ads outside the EU: spend, bids, targeting, clicks, conversions, CPA, ROAS. Everything about performance is inference.

## The longevity signal

Advertisers cut losing ads quickly, so run duration is the one defensible public proxy for an ad paying for itself. Practitioner bands (heuristics, not facts - sources disagree):

- Under 14 days: testing, or failing.
- 21-45 days: likely performing.
- 45+ days on a cold audience: almost certainly strong.
- 60+ days in a competitive vertical: likely a winner.
- 3-6+ months: probably working well.

**The heuristic is breaking, and this is the most important thing to know about it.** Under cost-cap and bid-cap buying, advertisers load an ad set with 10-20 ads, let the auction decide, and never prune. One or two ads take all the spend while the rest sit "active" with almost no delivery for months.

**Age now often measures neglect, not success.** A single long-running ad surrounded by many stale ones is neglect. Use longevity to prioritize which ads to _study_, never as proof of performance.

## Corroborating signals - stack them, none is sufficient alone

Chase them in order of evidence added per minute of lookup. The axes disagree, so all three are given:

- value: `cross-competitor repetition > variant duplication > relaunch recency > geographic and placement breadth > landing-page changes`
- effort (highest first): `relaunch recency > landing-page changes > cross-competitor repetition > variant duplication == geographic and placement breadth`
- efficiency: `variant duplication > geographic and placement breadth > cross-competitor repetition > landing-page changes > relaunch recency`

Variant duplication and geographic breadth tie on effort because both are read off the same listing already on screen: no click, no second pull, no query. They separate on value, which is what orders them on efficiency.

What the efficiency order starves is **cross-competitor repetition** - top of the value axis, third on the ratio, and unavailable at all until the classification pass is done. Schedule it as the last step of every session rather than expecting the ratio to reach it.

1. **Variant duplication**: several distinct executions of the same concept means the advertiser is scaling a winner, not testing a hunch. Visible in the listing you are already reading.
2. **Geographic and placement breadth**: 20 ads across 15 countries signals far more committed spend than 3 ads in one market. Also free in the same listing, and richest in the EU view.
3. **Cross-competitor repetition**: the same angle appearing across independent advertisers - the strongest corroborator there is, because it cannot be one advertiser's neglect. Costs a query across the whole classified file, so it only becomes available once the classification pass is done.
4. **Landing-page changes**: a competitor testing a new landing page is often testing a new angle - a signal the previous one is fatiguing. Costs a click plus a snapshot of the previous version to compare against.
5. **Relaunch recency**: an ad paused and brought back is stronger evidence than one that simply never stopped. Last only because it is unavailable in a first session - it needs two dated pulls to compare.

Re-rank from the second dated pull onward: relaunch recency becomes near-zero effort and moves up behind variant duplication. A user who already maintains a tagged archive of competitor ads gets cross-competitor repetition for free too, and should lead with it.

Filtering to active ads is a precondition, not a corroborator - set it before reading any of the five, or killed tests inflate the apparent format mix.

## Failure modes of the inference - state them wherever the inference is used

- **Budget-blind**: a $50/day test and a $50,000/day scaled winner look identical on a public surface.
- **Volume bias**: 50 video ads doesn't mean video works. Volume tells you effort. Longevity and duplication tell you outcome.
- **Objective-blind**: the surface cannot distinguish a brand-awareness campaign (which runs indefinitely regardless of direct response) from a performance campaign.
- **Inflated variant counts**: dynamic creative and automated placements make surfaces count "creatives" differently from what the advertiser considers a variant.
- **Survivorship**: you only see what is still live. Every killed test - the failures you would learn most from - is invisible.
- **Ad-object dating**: surfaces date the ad object, not the creative. Editing an existing ad can preserve the original start date.
- **Advertiser size**: a large advertiser can afford to leave a mediocre ad running. The longevity signal is stronger the smaller the advertiser.
- **Wear-in**: some ads genuinely get more effective with age, so longevity is partly a property of the ad's category, not its performance.

## B2B note

For B2B, the EU view of professional-network ad surfaces is uniquely valuable: it can expose targeting criteria like "IT decision-makers, Germany, company size 200+" - direct evidence of which buying-committee roles a competitor pays to reach. No other public signal reveals this.

## Integration note (optional - vendor names, current as of mid-2026, verify before asserting)

Surface details drift. Re-check before stating any of this as fact.

Known surfaces:

- Meta Ad Library: broad coverage, richer EU fields, non-political ads vanish when paused.
- Google Ads Transparency Center: verified advertisers only, ~1-year retention, variation counter.
- TikTok Commercial Content Library: EEA/Switzerland/UK only.
- LinkedIn Ad Library: active ads only, EU targeting criteria - the key B2B surface.
- Snapchat: political globally, commercial EU-only.
- Pinterest/Amazon/Apple: EU repositories.
- X: inconsistently maintained.

Where coverage differs between a surface's UI and its API, assert neither as universal.
