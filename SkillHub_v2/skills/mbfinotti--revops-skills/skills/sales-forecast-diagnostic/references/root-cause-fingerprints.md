# Root-cause fingerprints

One block per cause: the signals to pull, the fingerprint pattern, a confirming second signal, the data-vs-behavior discriminator, the fix, and what the fix costs. The two-signal evidence rule applies to every block - one signal raises a suspicion, two confirm a cause.

Blocks run in the register order from SKILL.md - fix effort ascending, which is the efficiency order only while the attributed dollars are unknown. Detection order is not delivery order: run every fingerprint, then rank every confirmed cause by dollars divided by the fix effort tier recorded here, and show the adjustment. There is exactly one ordering across this skill; this file does not carry a second one.

## Zombie / duplicate opportunities

- Pull: last-activity date and age per open deal; duplicate candidates by account plus similar amount/contact.
- Fingerprint: open forecast-weighted deals with no activity beyond the team's derived staleness threshold; the same buying intent recorded as two opportunities and counted twice.
- Second signal: reps privately concede the deal is dead ("keeping it open just in case"); win rate looks artificially low because the denominator is padded with corpses.
- Discriminator: almost always data - the record outlived reality. It becomes behavior only when zombies are kept deliberately to fake coverage.
- Fix: close or archive with reason codes; then hand recurring prevention to the sales-pipeline-hygiene audit - a one-time purge without an entry-standard fix regrows.
- Fix effort: an hour of bulk admin, then a standing sweep. Nobody's judgment is constrained and the purge is reversible, so it needs no negotiation; coverage stops being fiction in the same cycle.

## Stale / mass-pushed close dates

- Pull: close-date field history per deal - number of pushes, edit timestamps, edit sizes.
- Fingerprint: push counts accumulating without a logged reason; edits clustering on a single day near period end - the bulk-update fingerprint of a rep or manager sweeping dates the night before the forecast call.
- Second signal: close dates piling up on the last day of the period; deals whose date has been pushed more times than the team's derived threshold (below).
- Discriminator: a push with a buyer-side reason logged is a forecast update; repeated silent pushes are a data-integrity failure; mass same-day pushes are process theater.
- Fix: no silent pushes - every date move carries a reason; repeated pushes trigger a category review, not just a new date.
- Fix effort: an hour of CRM admin for the reason requirement, then a standing review of what the reasons say. It only bites at the next push, so allow one full cycle before the dates mean anything.

## Wrong forecast-category assignment

- Pull: category field history; category vs. stage vs. evidence cross-tab; contents of the omitted/excluded category.
- Fingerprint: category contradicts stage and evidence (commit with no activity for weeks); the omitted/excluded category used as a soft delete to dodge a formal closed-lost; categories set at creation and never updated.
- Second signal: conversion by category diverges wildly from the team's own trailing baseline per category.
- Discriminator: if reps articulate different definitions of "commit", the definition is ambiguous - a methodology finding to report at the boundary, not a rep failing. If definitions are shared and the assignment still contradicts evidence, it is behavior.
- Fix: category changes logged with reasons; omitted entries audited for disguised losses; per-category conversion tracked as the honesty check.
- Fix effort: an hour of admin to log changes, plus one conversation with the people whose calls the logging exposes. Jumps to a week when the ambiguity finding is real and the definitions must be re-agreed - and at that point it is a methodology question at the scope boundary, not a fix this skill ships.

## Stage inflation / happy ears

- Pull: field history of stage changes; activity log; contact roles; win rate by stage from trailing history.
- Fingerprint: late-stage deals with no buyer-side evidence - no economic-buyer contact logged, no next meeting booked, single-threaded; or stage skips (discovery straight to negotiation) in field history.
- Second signal: actual conversion from that stage runs far below whatever probability the stage implies; deals carrying a close date within days while sitting in an early stage.
- Discriminator: ask the rep what the buyer did last, not what the rep did. A confident seller-side answer with no buyer-side action is inflation; "the field was auto-advanced by a workflow" is data.
- Fix: buyer-verifiable evidence required to enter commit-eligible stages; review questions shift from "when will it close" to "what did the buyer do this week". If the stage definitions themselves have no verifiable exit criteria, hand off to the stage-definition audit.
- Fix effort: a week to define the gate and rewrite the review questions, sales leadership's agreement to enforce it, then a standing inspection. The forecast call gets honest one cycle later; the win-rate evidence takes two.

## Missing / unverifiable evidence

- Pull: required-field completeness on forecast-category deals; the field values themselves, not just non-blank counts.
- Fingerprint: fields filled with placeholders - "unknown", "TBD", the rep's own name as champion. A filled field is not evidence; systems that only check non-blank count "unknown" as complete.
- Second signal: nobody in the deal review can state the buyer's last verifiable action; qualification-framework scores (MEDDICC/MEDDPICC or whatever the team uses) all green with no artifacts behind them.
- Discriminator: if the rep can supply the evidence verbally but never recorded it, it is data (capture burden); if the evidence does not exist anywhere, it is behavior (the deal was never qualified).
- Fix: evidence-based entry criteria for commit categories; spot-check field values, not fill rates.
- Fix effort: the same week, the same gate, and the same owner as stage inflation - one intervention answers both, so never bill them as two efforts or ship one without the other.

## Late-created deals

- Pull: created date vs. close date per won deal; creation stage.
- Fingerprint: deals created and closed within days, or created directly in a late stage. The revenue is real; the forecast never saw it coming - coverage math and early-quarter calls were fiction.
- Second signal: a large share of the period's won revenue carries a creation date inside the period's final weeks.
- Discriminator: data/process - reps work deals outside the system and book them at signature. Not dishonesty; invisibility.
- Fix: log opportunities at first qualified conversation; measure created-to-closed interval per rep and set a floor consistent with the real sales cycle.
- Fix effort: a week to set the rule and the measurement, but the change itself is a rep habit - expect a cycle or two of partial compliance before coverage math can be trusted again.

## Manager roll-up override

- Pull: submitted number at each roll-up level vs. the sum of the level below, across periods; override reasons if logged.
- Fingerprint: the manager number diverges from the rep sum in a consistent direction with no logged reason.
- Second signal: compare override accuracy vs. raw roll-up accuracy over trailing periods. A manager whose overrides beat the raw sum is adding judgment - keep it, require a logged reason. A manager whose overrides underperform the sum is adding bias - that divergence is itself a quantified cause.
- Discriminator: the override is behavior by construction; the question is only whether it is informed judgment or padding/haircutting habit. The accuracy comparison answers it with data.
- Fix: overrides stay allowed but logged with a reason and scored per manager per period.
- Fix effort: an hour to capture the reason, but the score is meaningless until a quarter of overrides has accumulated, and managers have to accept being scored before any of it is honest. Cheap to ship, slow to pay.

## Rep sandbagging

- Pull: rep-level forecast submissions vs. actuals across 4+ periods; origin category of every won deal.
- Fingerprint: the same rep beats commit by a wide margin repeatedly, with wins closing from deals never placed above the lowest category despite late-stage activity visible in history.
- Second signal: large deals surfacing into commit only in the final days of the period, already fully evidenced; quarter-start commit consistently a fixed fraction of quarter-end actual.
- Discriminator: one strong quarter is noise. Require the pattern across at least two consecutive periods for the same person before naming it - and check the comp plan first, because sandbagging is usually a rational response to cliffs, not a character flaw.
- Fix: score rep calibration openly against their own history - per-rep forecast-vs-actual across the last 4+ periods, published to the team; adjust incentives that reward hiding upside; never punish accuracy misses in comp.
- Fix effort: a week to build the scorecard, and 2+ periods of history before the cause can even be named. Naming an individual is the one verdict here with employment consequences, so it carries a review the other fixes do not. Anything touching the incentive itself is the comp-driven bias fix, at that fix's cost - do not price it as part of this one.

## Comp-driven bias

- Pull: comp plan mechanics (cliffs, accelerators, quarter-end discount authority); timing distribution of closes and slips around period boundaries.
- Fingerprint: slips clustering just past a quota cliff once the number is made; buyers trained by predictable quarter-end discounts to wait, making every quarter back-loaded and every mid-quarter forecast soft.
- Second signal: the same reps' behavior flips with their attainment position - sandbagging when ahead, inflating when behind.
- Discriminator: this is the root behind most behavior-class causes. Fixing surface behavior while the incentive stays is temporary.
- Fix: report the incentive-to-bias link explicitly; propose measuring forecast accuracy separately from attainment; flag discount-timing predictability as a pricing decision for leadership.
- Fix effort: a quarter at best, since plan amendments usually land only at the next plan period, need finance, HR and legal sign-off, and are barely reversible once issued to reps. This is the cause the efficiency order starves - biggest impact, worst ratio, and it stays unfixed forever if the register is read by ratio alone. Promote it anyway on the conditions named in SKILL.md; when it is ruled out, say which behavior causes will regrow rather than quietly listing it last.

## Deriving thresholds from the team's own history

No universal day-count or push-count exists - published ones are tool defaults or folklore. Derive each threshold from the team's own trailing data (4+ periods where available). These are not ranked and should not be: each one serves exactly one fingerprint, so deriving a threshold for a fingerprint that never flagged is wasted work regardless of its cost - derive only what the flagged causes need.

1. Staleness: compute median time-in-stage per stage; flag deals beyond 2x their stage median.
2. Push count: compute the push-count distribution for won vs. lost/slipped deals; set the flag where the lost/slipped population separates from the won one (often the top decile).
3. Category conversion baselines: trailing conversion per category per segment; a period deviating far from its own baseline is the anomaly to explain.
4. Late-creation floor: compare created-to-closed intervals against the measured sales cycle; flag intervals implausibly short for the motion.
5. Recompute every few periods - thresholds drift as the team, product, and market change.
