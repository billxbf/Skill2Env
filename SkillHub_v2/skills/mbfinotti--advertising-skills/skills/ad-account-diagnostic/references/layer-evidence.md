# Layer Evidence

One section per diagnostic layer, in the fixed order. Each gives the evidence that confirms the layer as the root cause, the evidence that rules it out, and the single check that settles the call.

Every comparison is against the account's own history, never an industry benchmark. All named thresholds are attributed practitioner reference points, not universal constants.

## 1. Measurement / tracking

- **Confirms**: conversions drop across every campaign and channel simultaneously on the same date (a real market does not turn everything off at once - a tag change does); reported-vs-backend gap above roughly 40% (OnlyDeb's reference point), or a reconciliation ratio that swings week to week instead of holding stable; duplicate or inactive conversion actions; conversion events firing on button click instead of confirmed outcome; a site release, consent-banner change, or tag-manager publish dated at the break.
- **Rules out**: the drop is isolated to one campaign, ad set, or segment while siblings hold (Clixtell - an isolated drop points at targeting, creative, or the page, not tracking); the backend confirms the decline at the same magnitude; the reconciliation ratio is unchanged from the account's historical norm.
- **Settling check**: trace one real test event end-to-end - action → browser/server request → platform receipt → deduplication → report → CRM record - and reconcile a lag-mature 7+ day window against backend truth by both event date and processing date. Ratio stability, not exact equality, is the pass criterion. A recent-days-only gap is attribution lag, not breakage.
- **Handoff**: `mbfinotti/advertising-skills@ad-conversion-tracking` for the fix; `mbfinotti/advertising-skills@ad-attribution-gap` when the finding is cross-platform disagreement rather than a broken pipe.

## 2. Structure

- **Confirms**: CPA drifting up steadily over months with no single break date (Precisionly); many campaigns or ad sets each starving below the conversion volume automated bidding needs (reference points: roughly 15-30 conversions/month per campaign, OnlyDeb; Google recommends ≥30 for Target CPA evaluation); overlapping ad sets bidding on the same users; efficient campaigns capped by budget while inefficient ones spend freely; the account optimising to an event the business does not value; hyper-segmentation fragmenting the learning signal (Perpetual Traffic ep. 804 reports removing state-level geo splits cut CAC 20-25% within a week).
- **Rules out**: a prior period of good performance under the identical structure with a more recent break date (Foxwell) - structure did not change, so something else did; per-unit volume comfortably above the learning thresholds.
- **Settling check**: map spend, conversion volume, and optimization event per campaign/ad set. If most units sit below the volume gates, or two units serve the same audience with separate budgets, structure FAILs.
- **Handoff**: diagnosis only - the merge/consolidation plan belongs to `mbfinotti/advertising-skills@ad-campaign-consolidation`.

## 3. Targeting

- **Confirms**: audience overlap warnings; narrow cold audiences saturating as spend competes with itself (AdStellar); frequency climbing while reach flattens; CPM rising in specific ad sets while the account's other audiences hold; healthy CTR but traffic that never converts anywhere (wrong intent, not wrong ad).
- **Rules out**: broad, healthy-sized audience with normal frequency but poor CVR - that points past the ad to the page or offer (Pigeon Digital); decline uniform across unrelated audiences (points external or to tracking).
- **Settling check**: per-ad-set frequency and reach trend vs the account's own history, plus overlap inspection. Saturation shows exposure concentrating; mis-targeting shows engagement without downstream quality.
- **Handoff**: `mbfinotti/advertising-skills@ad-audience-targeting` for redesign; `mbfinotti/advertising-skills@ad-negative-keywords` when search terms show the mismatch.

## 4. Creative

- **Confirms**: CTR falling while CPM holds flat (Metamktgagency - the auction is unchanged; the ad is losing the click); relevance/engagement diagnostics below the account's norm; decline concentrated in the oldest creatives while newer ones hold; frequency above roughly 3 with declining CTR (AdStellar's reference point).
- **Rules out**: stable CTR with rising CPM (auction/external, not creative - Metamktgagency); decline equally present in a fresh creative launched into the same window; CVR collapse with healthy CTR (downstream of the click).
- **Settling check**: per-creative CTR trend against each creative's own baseline. This skill only _names_ the layer - the full differential (baseline, confounder screen, decay measurement) runs in `mbfinotti/advertising-skills@ad-creative-fatigue`, which hands back here if the confounders point elsewhere.

## 5. Bidding / budget

- **Confirms**: bid strategy mismatched to conversion volume (a target-based strategy fed too few conversions never exits learning); a recent significant edit dating the volatility (budget/bid/target changes reset learning - CPAs run 20-50% higher during learning, Grow With Sakib); lost impression share concentrated in lost-to-budget with strong efficiency (genuinely capped); or lost-to-rank while budget goes unspent (bids/quality, not money - Workshop Digital); targets moved repeatedly without waiting out the recalibration window.
- **Rules out**: impression share stable vs history; no significant edits in the window; delivery smooth and budgets pacing normally.
- **Settling check**: the lost-IS split (budget vs rank) plus the edit log against the volatility dates. Trustworthy Digital's decision reference: lost-to-budget above 50% argues the constraint is money; lost-to-rank above 50% argues it is rank - and above roughly 60-80% impression share, diminishing returns make more budget the wrong buy either way.
- **Handoff**: `mbfinotti/advertising-skills@ad-bidding-strategy`, `mbfinotti/advertising-skills@ad-budget-pacing`, `mbfinotti/advertising-skills@ad-spend-allocation`, `mbfinotti/advertising-skills@paid-media-scaling`. This skill makes no budget or bid recommendation itself.

## 6. Offer & downstream

- **Confirms**: CPM and CTR healthy but CVR down (Pigeon Digital - "points past the ad, onto the page and the offer"); the drop dating to a price change, promo end, page release, or checkout change; the problem reproducing on a direct walk through the funnel; healthy CVR but poor revenue outcome (AOV/mix shift, not the account at all).
- **Rules out**: CVR stable while upstream metrics moved; backend conversion rate from other traffic sources unchanged is _not_ a full rule-out (paid traffic can hit a different page or geo) - check the paid path specifically.
- **Settling check**: CVR by landing page and by date against the site's change log. If the failing link is post-click, this skill stops: flag it, with the evidence, and hand everything past the click - message match, friction, the fix list - to `mbfinotti/advertising-skills@paid-landing-page-audit`.

## 7. External

- **Confirms**: the cost metric elevated evenly across every campaign and audience (AdStellar - "if CPM is elevated across every campaign evenly, the issue is likely external"); timing aligned with known seasonality or market events; The HQ Digital's test - the account's CPM rose during a period when every advertiser in the category was bidding, versus competitors flat while the account's costs rose (internal); competitor entry visible in auction-insight-style reports.
- **Rules out**: elevation concentrated in one branch of the account; competitors' pressure flat while the account's costs rose; any unresolved FAIL in layers 1-6 - external is a diagnosis of exclusion and cannot be claimed over an unchecked internal layer.
- **Settling check**: the uniformity test from the breakdown-and-compare step, corroborated by at least one external signal (seasonality calendar, auction insights, category evidence). Verdict `external` carries the account's realistic floor for the period - the finding is "wait, or re-set targets to the market", never "spend through it" without incrementality evidence.
