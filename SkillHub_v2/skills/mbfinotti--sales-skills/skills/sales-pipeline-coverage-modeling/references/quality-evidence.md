# Quality evidence behind the credibility adjustment

Quantified, sourced evidence for why raw - and even stage-weighted - coverage lies when the pipeline is stale, single-threaded, padded, or indecision-heavy. Cite these as evidence for making quality adjustments; none is a universal constant, and the exact magnitudes vary by dataset.

## The headline arithmetic

**A 4x ratio with 30% stale deals is really 2.8x.** The prescription: compute a third number beyond raw and weighted, **adjusted coverage**, which strips stale, out-of-period, repeatedly slipped, and single-threaded late-stage deals from the total before dividing by quota. Act on that one.

The phantom-pipeline gap between raw and credible coverage is directionally consistent across independent measurements, but varies in magnitude:

- One benchmark pair puts median raw at ~3.4x against median weighted at ~1.8x for the same population. Teams that hit plan and teams that miss carry similar _raw_ coverage; the split shows up in weighted, ~2.1x+ for hitters vs ~1.2x for missers.
- ORM Technologies' starker rule of thumb: **four turns of nominal ≈ one turn of credible**.
- A worked comparison elsewhere collapses $4M unweighted to $1.2M weighted.

Treat "raw materially exceeds weighted" as the universal diagnostic, and the specific multiple as a property of whichever pipeline was sampled.

## Stale / zombie deals

- Deals parked in one stage for months inflate coverage with dollars that will not close. Common staleness thresholds: no activity in 14-21 days (some orgs 30-45+).
- A threshold-free diagnostic: in most pipelines, **the age of deals won is about half the age of deals lost** - an old open deal is usually dying, not maturing.
- The perverse incentive: a flat coverage mandate itself incentivizes reps to hoard zombies to hit the number - the metric manufactures the fake pipeline it was meant to prevent. Manage to the adjusted number to break the loop.

## Single-threading

Two independent large-sample analyses converge:

- **Gong** (~1.8M opportunities):
  - Winning deals carry roughly twice the buyer contacts of losing ones.
  - Multi-threading lifts win rate by an average of **130%** on deals over $50K.
  - Strategic enterprise deals average 17 contacts.
- **UserGems** (ML analysis of 500 closed opportunities): a single-threaded deal carries roughly a **5%** win probability versus **30%** with five engaged people.

Implication: on a late-stage deal, engaged-contact count is often a better health signal than the CRM stage label. Flag any late-stage deal with fewer than ~3 engaged contacts as at-risk in the adjustment, regardless of rep optimism.

## No-decision and indecision

_The JOLT Effect_ (Dixon & McKenna, 2022; 2.5M recorded sales conversations): **40-60% of deals stall in "no decision"** rather than being lost to a competitor.

Win rate by buyer indecision level:

- Low indecision: 45-55%.
- Moderate indecision: ~25-30%.
- High indecision: **below 5%**.

A pipeline concentrated in indecision-prone deals is structurally near-unwinnable at any raw coverage level - a large share of visible "open pipeline" was never going to convert.

## Slips and pushes

- A slipped deal is _less_ likely to close than a comparable deal that never moved.
- Strong teams convert ~80% of committed deals on time; weaker teams convert ~60% (Clari).
- Roughly 60% of forecasted B2B deals slip to the next quarter (CSO Insights).
- Mechanics: increment a push counter on every close-date move, require a slip reason, and **discount twice-pushed deals** in the adjustment rather than carrying them at full weight.

## Sandbagging detection

Reps banking deals for future periods or holding commit-quality deals in "best case" corrupt the model in both directions. Audit deals that jump to closed-won from an early stage, and deals closing right at period-end: in one quarter Kellogg reviewed, 25 of 56 closed deals had been pulled in from future quarters - a create-and-close pattern that "suggests close dates are being sandbagged." Sandbagging signals a comp or culture problem, not a data problem; fixing the CRM field won't fix the incentive.
