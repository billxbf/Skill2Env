# Sizing Recoverable Revenue

Size only confirmed real leaks - never healthy disqualifications, never data-capture gaps (those get an instrumentation fix, not a dollar figure).

## The formula

```
recoverable $ = leaked record count
              x average value per record
              x onward conversion rate from the leak point
```

- **Leaked record count** - from the reconciliation residual, after classification, each record counted once at its first unexplained exit.
- **Average value per record** - deal value for pipeline leaks; subscription value (per period, times the periods realistically recoverable) for billing/renewal/churn leaks. Use the cohort's own average, not the company-wide one - leaked records often skew smaller or larger than the mean.
- **Onward conversion rate** - the probability a record at that funnel point would still have converted had it not leaked. This is what separates recoverable from gross; omitting it is the classic credibility failure.

## Estimating onward conversion

These four are a fallback chain, not a menu to rank by efficiency: each rung fires only when the rung above it has no data, and the ordering axis is evidence strength. Ranking them by effort would be false precision - a weaker method is never the efficient choice, only the available one.

1. Best: compute it from the funnel's own history - the conversion-to-close rate of records that passed the same point in a prior healthy cohort.
2. If history is thin, chain the step-to-step rates the user provided in the Interview from the leak point forward.
3. Apply an age haircut: a record that leaked months ago converts worse than a fresh one at the same point. Derive the decay from the user's own reactivation or re-engagement outcomes when any exist; otherwise state the haircut as an assumption and tag confidence accordingly. Do not import a published response-decay multiplier as the haircut (see the warn-off in SKILL.md Ground Rules).
4. Involuntary-churn leaks: recoverable = failed-payment revenue x (achievable recovery rate - current recovery rate). Derive the achievable rate from the user's own recovery history where it exists; a vendor benchmark may be quoted only as a labeled vendor figure, never as the assumption driving the number.

## Confidence tags

These are a data-quality gate, not a menu of options - they qualify a figure, they do not compete for the same job, so no efficiency ordering applies to them.

Tag every recoverable figure:

- **measured** - all three factors from the funnel's own data.
- **estimated** - count and value measured; onward conversion chained or haircut from stated assumptions.
- **assumed** - any factor guessed. An "assumed" figure may appear in the register but must never drive the ranking on its own; upgrade it or flag the leak as needing instrumentation.

Report the recoverable total by confidence band, not as one blended number.

## Ranking the register

Rank by recoverable dollars per unit of fix effort, never by recoverable dollars alone: a mid-sized leak fixed by wiring one alert outranks a larger one needing a process redesign. State the adjustment on every entry it moved; never silently reorder.

Recoverable dollars are the value axis and stay in dollars. Effort never is - it is analyst hours, engineering work, cross-team coordination, and how hard the fix is to reverse.

Fix classes, in default order:

```
efficiency (recoverable $ per unit of effort, highest first)
  alert/escalation == routing fallback > recovery sequence > one-off rework > process redesign

value (recoverable $ unlocked, largest first)
  process redesign > recovery sequence > alert/escalation == routing fallback > one-off rework

effort (heaviest first)
  process redesign > recovery sequence > one-off rework > alert/escalation == routing fallback

compliance cost (review triggered, heaviest first)
  recovery sequence > rework of invoiced or recognized revenue
```

- **alert/escalation** - a threshold alert or escalation on an event the funnel already emits (unaccepted past the handoff window, stalled past dwell time). Near-zero effort, one config change, switched off to reverse; the value recurs every cycle.
- **routing fallback** - a fallback owner or reassignment rule closing an ownership vacuum. An hour, same system, same reversibility.
- **recovery sequence** - a retry or dunning path wired to an existing failure event. A day of billing configuration; in self-serve funnels this is usually the single largest recurring recoverable number.
- **one-off rework** - working the records that already leaked. An hour of analyst or rep time and no system touched, but the value is bounded by that record set and never recurs.
- **process redesign** - rebuilding the handoff, contracting, or renewal motion itself. A quarter, cross-team, and hard to reverse once teams have re-learned it.

Ties: alert/escalation `==` routing fallback on all three dollar axes, because both are one configuration change in a system that already holds the data. Both recur every cycle, and which of the two recovers more depends on which site leaks more in this funnel, not on the class.

Compliance cost is the review a fix triggers and the reversibility it costs:

- Retry and dunning changes need a payment-rules and subscriber-notification review before shipping.
- Re-issuing or backdating an invoice needs revenue-recognition sign-off from finance and is not silently reversible.
- Alerts, routing fallbacks, and a sales-handoff redesign trigger none, so they carry no compliance cost at all.

**What this order starves: process redesign.** It carries the biggest recoverable number and the worst ratio, so it loses every round and never gets done when the register is only ever read top-down.

Promote it out of the register into its own dated workstream with its own owner as soon as any of these holds:

- the same structural leak returns in consecutive re-runs after the cheap fixes were applied
- its recoverable figure exceeds the rest of the register combined
- no cheap fix is even possible because the step emits no event to alert on

Instrumentation is deliberately absent from these lines. A capture gap carries no dollar figure by rule, so a dollar ratio would rank it last by construction. It ranks in its own section instead, by which instrumentation unlocks the most currently-unmeasurable funnel volume.

This order is a default, not a law - it shifts with the funnel and with who executes the fix. Re-rank it against what the Interview already established about this user before presenting the register:

- Engineering capacity available -> promote recovery sequence, and promote instrumentation inside its own section.
- An analyst who owns the data and nothing else -> promote one-off rework; alerts and routing fallbacks hold their lead only where they are configuration rather than code.
- A billing system nobody will touch this quarter -> delete the recovery-sequence and invoice-rework fixes and name the constraint that deleted them. The leak itself stays in the register, marked blocked with no fix owner. A ruled-out fix demoted to the bottom instead of deleted silently reappears as scope next quarter.
- A hard date from the Interview -> delete process redesign from this round and lead with rework of the records that already leaked.

Then, whatever the resulting order:

1. Every entry names one owner for the fix - a process or system owner, not a blamed individual.
2. Every entry carries its fix class, so the trade-off behind its rank is readable in the row itself.
3. Cap the register at the leaks that together cover the large majority of the sized total; a 30-row register buries the three that matter.

## What never to do

- Never sum gross pipeline value of stalled deals and present it as recoverable.
- Never double-count a record across two leak sites - first unexplained exit wins.
- Never size an untracked step. No records, no number; instrument first.
- Never blend measured and assumed figures into a single headline total.
