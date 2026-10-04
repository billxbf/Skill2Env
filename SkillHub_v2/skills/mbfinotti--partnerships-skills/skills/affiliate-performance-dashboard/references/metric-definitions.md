# Metric Definitions

The catalogue to pick spec rows from, ranked. A dashboard that shows everything shows nothing, so the question is never which metrics exist but which three to add after the floor.

The incrementality vocabulary (Incrementality, Baseline Conversions, Model Validation) and the ROAS/ROI split (ROAS = Attributed Revenue / Media Cost; ROI = Attributed Revenue / (Media Cost + COGS)) come from platform glossaries [VENDOR]. They are foundational because they are explicit and internally consistent, not because a program runs on that platform - apply them whatever the tooling.

Provenance tags:

- [VENDOR]: platform/network/agency figure.
- [TRADE]: trade-body study.
- [SYNTH]: multi-source synthesis without published raw data.
- [DERIVE]: compute from the program's own history.

For every metric, resolve the competing definitions explicitly in the spec row: the disagreements below are exactly where cross-source comparison breaks.

## Table of Contents

- [The floor - not part of the menu](#the-floor---not-part-of-the-menu)
- [The menu, ranked by efficiency](#the-menu-ranked-by-efficiency)
- [New-to-file / new-customer rate](#new-to-file-new-customer-rate)
- [Reversal / return / chargeback rate](#reversal-return-chargeback-rate)
- [AOV (average order value)](#aov-average-order-value)
- [Click-to-conversion rate](#click-to-conversion-rate)
- [Active-affiliate rate](#active-affiliate-rate)
- [Time-to-first-conversion](#time-to-first-conversion)
- [EPC (earnings per click) - B2C only](#epc-earnings-per-click---b2c-only)
- [B2B only: trial-to-paid rate](#b2b-only-trial-to-paid-rate)
- [Partner-sourced vs partner-influenced revenue - B2B](#partner-sourced-vs-partner-influenced-revenue---b2b)
- [B2B only: churn-adjusted partner LTV](#b2b-only-churn-adjusted-partner-ltv)

## The floor - not part of the menu

These are not options. The Pass Threshold cannot be met without them, so they go on the spec before any ranking is consulted.

**Cost of sale / commission-to-revenue.**

- Formula: `(validated commission + network fees + agency fees + placement/tenancy fees + bonuses) / attributed net revenue`.
- Dispute: what sits inside the numerator. Most casual reporting excludes network fees (2-30% of commission value [VENDOR]) and agency fees (20-25% of budget [VENDOR]), understating true cost.
- Rule: include them all. An excluded fee is the single most common way a program reports itself cheaper than it is.

**Attributed ROAS vs attributed ROI.**

- Formula: ROAS = `attributed revenue / media cost`; ROI = `attributed revenue / (media cost + COGS)` [VENDOR - impact.com glossary].
- Rule: the same platform distinguishes them. Never use the terms interchangeably, and state whether COGS is in the denominator.
- Calibration only: 12:1 network-average ROAS [TRADE, 2018]; travel $19:1, retail $11:1 [TRADE, 2025]. Trade-body figures still come from member networks.

**Net program contribution.**

- Formula: `attributed net revenue - (validated commission + network fees + agency fees + placement fees)`.
- This is the headline profitability number; keep it on the top view.

**Top-N partner concentration.**

- Method: rank partners by validated attributed revenue for the period; top-N% share = revenue from the top N% of _active_ partners / total program revenue.
- Use the spec's active definition for the denominator population, and put the top-partner share on the executive view: concentration is a board-level risk, not an operator detail.

**B2B only: partner-sourced MRR/ARR.**

- Formula: MRR/ARR from partner-sourced accounts, normalized by billing interval (annual / 12, quarterly / 3), tracked separately from overall revenue.
- Reversals recur: churn and downgrades adjust it every cycle, so the number is only stable on validated billing events.
- Contribution is derived from it, which is why it sits on the floor rather than in the menu.

## The menu, ranked by efficiency

Effort here is analyst hours, data availability, reconciliation burden and standing maintenance - never a tooling price. Value is the decision the metric actually changes; a metric that changes no decision scores zero however cheap it is.

B2C ecommerce:

- efficiency: `new-to-file share > reversal rate > AOV by partner type > click-to-conversion > active-affiliate rate > time-to-first-conversion > EPC`
- value: `new-to-file share > reversal rate > AOV by partner type > active-affiliate rate > time-to-first-conversion > click-to-conversion == EPC`
- effort (most first): `time-to-first-conversion > new-to-file share > active-affiliate rate > AOV by partner type > reversal rate == click-to-conversion == EPC`

B2B SaaS:

- efficiency: `reversal rate > trial-to-paid by partner > new-to-file share > active-partner rate > click-to-conversion by stage > time-to-first-conversion > influenced-revenue split > churn-adjusted partner LTV`
- value: `churn-adjusted partner LTV > trial-to-paid by partner > new-to-file share > reversal rate > influenced-revenue split > time-to-first-conversion > active-partner rate > click-to-conversion by stage`
- effort (most first): `churn-adjusted partner LTV > influenced-revenue split > new-to-file share > trial-to-paid by partner > time-to-first-conversion > active-partner rate > reversal rate == click-to-conversion by stage`

Ties are real, not hedges. EPC and click-to-conversion answer the same question - is this partner's traffic worth its clicks - from the two sides of one fraction, so neither adds a decision the other missed. Reversal rate, click-to-conversion and EPC all read straight off an export the platform already produces: what they cost is agreeing the counting convention, not running the query, and that cost is identical for all three.

Why new-to-file leads in B2C and falls to third in B2B: in B2C it is computable from the orders database alone once the partner ID is stamped on the order, because "first-ever customer" is already in the customer's own order history. In B2B the same number needs a CRM join and survives cross-device identity loss, which is a quarter of work rather than a week.

**What the efficiency order starves: churn-adjusted partner LTV.** It is the only metric here that can settle a commission-architecture argument, and it loses every ratio round - a 24-month horizon means the program has to be old enough to have one, and the churn-adjusted revenue join is a standing job. Promote it anyway when a rate change or a recurring-commission cap is a live decision, or when finance disputes the program's payback. The same pattern in miniature applies to time-to-first-conversion: cheap-looking until you find the platform never retained link-activation timestamps.

Deleted, not demoted:

- **Average commission per active partner.** The mean hides exactly the skew that matters, and concentration is already on the floor - top-decile share and median answer the same question honestly. Reporting both invites the reader to quote the flattering one.
- **EPC in B2B.** Recurring commission accrues over a 21-60 day conversion lag, so the number moves for reasons unrelated to partner quality and no two people compute it the same way. It stays in the B2C menu.
- Any metric whose data the Interview says does not exist. Name it under Open items with what would make it computable; never park it in the spec as a wish.

Re-rank before proposing:

- A network that exports partner-type classification cleanly moves AOV-by-partner-type and the type mix up a rung.
- A warehouse already carrying billing and CRM collapses new-to-file's effort to near-zero.
- No analyst at all deletes everything below the third rung.

Entries below run in the B2C efficiency order, then the B2B-only metrics in theirs; on a B2B program read the shared entries against the B2B line above.

## New-to-file / new-customer rate

- Formula: `conversions from customers not previously in the customer file / total partner conversions`.
- Decides: whether checkout-adjacent partner types get repriced or reviewed - the largest money decision most programs have open.
- Costs: a week in B2C (stamp the partner ID at order creation, read first-ever-customer from order history); a quarter in B2B (CRM join, plus identity resolution).
- Limits: identity resolution and cross-device loss make the join imperfect - store the originating partner ID in billing/CRM metadata at order creation, not only in the tracking platform.
- High new-to-file with a weak repeat rate signals discount-driven one-off buyers, not durable acquisition [VENDOR].
- Doubles as the cheap incrementality proxy, with one hard limit worth stating on the tile: new-to-file proves the customer was not already yours, never that the partner caused the purchase. A coupon, cashback, or brand-search partner intercepting a buyer already heading to checkout scores as new-to-file. Treat it as the cheapest rung of the incrementality instruments, and climb to a holdout or geo-lift test only as far as the live decision needs.

## Reversal / return / chargeback rate

- Formula: `reversed conversions / total conversions` per period, on the validation-date basis.
- Decides: whether to hold a partner's payout, and whether a period is comparable at all - every trend on the dashboard inherits this.
- Costs: near-zero. The platform's own pending -> approved -> declined state machine already carries it; the work is declaring which state each metric counts.
- A period is comparable only after its validation window fully elapses.
- Above ~10% signals a quality problem [VENDOR]; band to the program's own history [DERIVE].

## AOV (average order value)

- Formula: `total order revenue / orders`. Disagreements: gross vs net of returns; tax and shipping in or out - rarely specified [SYNTH]. Spec net of returns, excluding tax/shipping, and say so.
- Decides: which partner types to recruit into and which to cap - sliced by partner type it separates discount-driven buyers from premium buyers [VENDOR]. Unsliced it decides nothing.
- Costs: an hour, plus the returns join.
- B2C-native. B2B analogue: initial contract value or first-year ACV per referred account.

## Click-to-conversion rate

- Formula: `conversions / clicks x 100`. Prefer unique clicks in the denominator and say so.
- Decides: whether one partner is shipping junk traffic. Diagnostic only - never a headline.
- Costs: near-zero from the existing export, once the click definition is declared.
- Published ranges run 0.5-3% [SYNTH] largely because "a click" (raw, unique, deduplicated, bot-filtered) varies per source.
- B2B variant: name which conversion - trial/demo signup and trial-to-paid are two separate rates, never one blended number.

## Active-affiliate rate

- Formula: `active affiliates / total enrolled x 100`.
- Decides: whether the next hours go to recruiting or to activating the partners already signed.
- Costs: an hour to compute, then a standing argument over the definition - that argument is the real cost.
- Disagreements on both terms [VENDOR]: what counts as active (a click, a sale, a live placement, a lead) and the window (30/60/90 days). Require a meaningful action - a conversion or live placement - within a fixed window, not a signup or lone click.
- Calibration only: 10-30% typical, over a third of programs below 20% [VENDOR survey]. Baseline from own history [DERIVE].

## Time-to-first-conversion

- Formula: median days from partner link activation to first validated conversion.
- Decides: where activation effort lands, and when to stop spending it on a partner.
- Costs: a week if link-activation timestamps are retained, a quarter if they must be reconstructed - check before promising the metric.
- Calibration only [SYNTH, directional]: ~14-day cross-program median; 1-4 days ecommerce vs 21-60 days B2B SaaS; a partner with no conversion in 60 days has ~3.7% lifetime probability of ever converting.

## EPC (earnings per click) - B2C only

- Formula: `validated commission / clicks`, in currency per click.
- Decides: little on its own. It ranks partners the leaderboard already ranks; keep it because partners themselves negotiate on it.
- Costs: near-zero, once the click convention is declared.
- Disagreements [VENDOR]: per-click vs per-100-clicks (some networks display per-100 because per-click is fractions of a cent; others per-single-click) vs per-visitor (commission / unique visitors, absorbing multi-click visitors). Declare which.
- Blended network EPC averages across all of a program's affiliates and predicts no individual affiliate's EPC - never set a partner target from it.
- Whether the click denominator is deduplicated or bot-filtered is rarely disclosed anywhere [SYNTH]; state the program's own click definition in the spec row.

## B2B only: trial-to-paid rate

- Formula: `referred trials converting to paid / referred trials started`, per cohort.
- Decides: which partners to keep paying - a partner with high trial volume and low trial-to-paid is shipping unqualified traffic, and no other metric on this list catches that.
- Costs: a week to a quarter, depending on whether product analytics already carries the partner ID at trial start.
- Published product benchmarks diverge materially by methodology and are not partner-channel-specific [VENDOR, conflicting] - derive per-partner-type baselines from own cohorts [DERIVE].

## Partner-sourced vs partner-influenced revenue - B2B

The sourced number is floor. The menu option is whether to add the influenced number at all.

- Sourced: the partner originated the deal/order. Influenced: the partner touched a deal originated elsewhere.
- Decides: how partner contribution is argued to an executive - and nothing operational, which is why it ranks low against its cost.
- Costs: a quarter. A CRM influence model has to exist, and the precedence rule has to survive a political argument before the tile is trustworthy.
- Report as two separate, capped numbers, never summed; sourced takes precedence when a deal qualifies for both [VENDOR consensus].
- Survey context: 67% of partner teams measure sourced revenue (the most-measured KPI); influenced ranks third at 54% [survey of 500+ partnership professionals, 2023].

## B2B only: churn-adjusted partner LTV

- Formula: `revenue from a partner's referred accounts over a fixed horizon (e.g. 24 months), net of churn / total payout to that partner over the matching period`.
- Decides: the commission architecture itself - what a partner is worth paying, and for how long.
- Costs: a standing job, and the program must be old enough for the horizon to exist. This is the starved rung; promote it on the conditions above, not by default.
- Calibration only: B2B SaaS LTV-to-payout ratios of 4.2x-9.5x are published [SYNTH]; derive the program's own horizon and ratio [DERIVE].
- Never substitute signup counts - churn-adjustment is the whole point.
