# Metric Decomposition

How to localise the failing link before naming a cause. The outcome metrics (CPA, ROAS) are outputs, not levers - decompose them first, then read direction.

## The identity

Pigeon Digital's decomposition: ROAS is an output of four levers.

```
impressions × CTR              = clicks
clicks      × CVR              = conversions
conversions × AOV              = revenue
spend        = impressions × CPM / 1000
=> ROAS  ≈ (CTR × CVR × AOV) / (CPM / 1000)      - impressions cancel
   CPA   = spend / conversions = (CPM / 1000) / (CTR × CVR)
```

Three levers push ROAS up (CTR, CVR, AOV), one pushes it down (CPM). A ROAS or CPA move _must_ be expressible as a move in at least one of the four - find which one(s) actually moved vs the account's own history before any layer talk. Judge against economics, not vanity: break-even ROAS ≈ 1 / gross-margin rate (AdDogs), so a "drop" that stays above break-even is a different conversation from one below it.

## Sequential elimination down the chain

Walk impression → click → conversion → revenue and stop at the first broken link (Pigeon Digital's chaining logic):

1. **CPM moved, CTR held** → the auction changed: external pressure, seasonality, saturation, or relevance decay. Run the uniformity test (below).
2. **CTR fell, CPM held** → the ad is losing the click: creative layer (Metamktgagency). Distinguish all-clicks CTR from link/outbound CTR - engagement can mask falling intent clicks.
3. **CVR fell, CTR and CPM held** → "points past the ad, onto the page and the offer" (Pigeon Digital) - offer & downstream layer - _unless_ tracking broke (a tag failure looks exactly like a CVR collapse; the reconciliation gate must already have passed) or targeting shifted the traffic mix to lower-intent clickers.
4. **AOV/value fell, all else held** → mix shift, promo, pricing - usually not an ad-account problem at all.

Two links moving together is information, not noise:

- CPM up _and_ CTR down is the classic creative-decay signature.
- Everything down simultaneously on one date is the classic tracking signature.

## Direction table

| Observation (vs own history)             | First reading                   | Layer to check first                     |
| ---------------------------------------- | ------------------------------- | ---------------------------------------- |
| CPM up uniformly, everywhere             | Auction/seasonality             | External                                 |
| CPM up in one ad set only                | Audience saturating or narrowed | Targeting                                |
| CPM up + CTR down together               | Relevance decay                 | Creative                                 |
| CTR down, CPM flat                       | Ad losing the click             | Creative                                 |
| CTR fine, CVR down                       | Post-click or signal            | Offer/downstream - after tracking passed |
| CVR down across all channels at once     | Broken conversion signal        | Measurement/tracking                     |
| CPA up slowly over months, no break date | Erosion, fragmentation          | Structure                                |
| CPA up sharply from a known date         | Whatever changed that date      | Edit log first                           |
| Volume down, efficiency stable           | Delivery constrained            | Bidding/budget (lost-IS split)           |
| Revenue down, conversions stable         | AOV/mix shift                   | Offer - often not the account            |

## Lost impression share: budget vs rank

Search impression share = impressions won / impressions eligible. Its loss splits into two numbers with opposite fixes (Adalysis; Workshop Digital):

- **Lost IS (budget)** - delivery stopped because the budget capped out. More budget genuinely buys more of the same delivery _only if_ efficiency at the margin holds.
- **Lost IS (rank)** - the ad lost the auction on rank (bid × quality). "Simply increasing your budget won't guarantee a 100% search impression share if your ad rank is insufficient" (Workshop Digital) - budget does nothing here.

Trustworthy Digital's reference points:

- Lost-to-budget above 50%: the constraint is money, and often the right move is _reducing_ bids to buy more clicks at the same spend.
- Lost-to-rank above 50%: the constraint is rank.
- 60-80% impression share: where diminishing returns typically begin for mid-market non-brand terms.

All three are practitioner reference points to test against the account, not laws.

## Frequency

Frequency is a lagging, confirming signal - an average over a window, at ad-set level, not the marginal effect of the next impression. AdStellar's reference point:

- Frequency above roughly 3 with declining CTR supports a creative/saturation read.
- Frequency climbing while unique reach flattens month over month is the earlier saturation tell.

Never build a verdict on a frequency number alone, and never compare cold-audience frequency against retargeting frequency - tolerated exposure differs by an order.

## Learning-phase mechanics

Automated delivery recalibrates after significant edits (targeting, placement, optimization event, creative, bid strategy, meaningful bid/budget changes - and budget moves beyond roughly 20% in one step are widely treated as significant, per practitioner interpretation relayed by Modern Marketing Institute and Grow With Sakib). During recalibration, performance is volatile by design: ROAS swings of 20-50% day to day are normal (Niblin), and CPAs run 20-50% above post-learning levels (Grow With Sakib).

Reference exit points:

- Roughly 50 optimization events in 7 days on Meta (Meta Business Help Center, as relayed by AdStellar).
- Up to three weeks or 1-2 conversion cycles for Google Smart Bidding (Google Ads Help).

Diagnostic consequences:

- Date every edit before reading any trend: a "collapse" that starts at an edit date is a reset, not a root cause.
- Data from inside a learning window fails the Evidence Gate.
- A unit that never accumulates the exit volume is a _structure_ finding (consolidate the signal), not a bidding finding.

## Breakdown-and-compare

The localisation move that separates internal from external: pull the failing metric by campaign, then ad set, then ad, and compare each against its own historical baseline (AdStellar; The HQ Digital).

- **Uniform elevation** across every branch → the cause is above the account: auction, season, market. The HQ Digital's discriminator: costs rising while the whole category was bidding is external; costs rising while competitors stayed flat is internal.
- **Concentrated** in one branch → the cause lives in that branch; drill one level down and repeat until the smallest failing unit is found.

Comparability rules, non-negotiable:

- Equal window lengths.
- Equal attribution-lag maturity (recent days under-report - a trailing window always looks like decline).
- Matched day-of-week composition.
- Known outages excluded.
- Never sum or compare conversion counts across differing attribution windows, counting methods, or models - report side by side until definitions reconcile.

Breaking any of these manufactures a phantom root cause.
