# Capacity Math and Measurement

The arithmetic that keeps a cadence executable, and the metrics committed before launch. Benchmarks here are vendor-published unless labeled platform policy.

## Capacity math

A cadence's width is capped by three things:

- Rep time for manual touches.
- Per-mailbox sending limits for automated ones.
- The complaint tolerance of mailbox providers.

Run the arithmetic before launch, and shrink the cadence or the cohort until it fits.

**Manual-touch load per rep per day:**

> active prospects × manual touches per sequence ÷ sequence length in working days

Worked example on Example A (4 manual touches over 18 days): 300 active prospects × 4 ÷ 18 ≈ 67 manual touches/day - beyond a realistic call-block for one rep (practitioner ranges cluster around 10-30 dials plus social touches per day). Skipped manual steps do not just lose touches - they corrupt the measurement, because the sequence being run is no longer the sequence being tested.

**When the plan does not fit, buy the fix in this order:**

**stagger cohort entry > cut the active cohort > drop the heaviest manual touch > add mailboxes or reps**

- value (pipeline preserved): add mailboxes or reps > stagger cohort entry > cut the active cohort > drop the heaviest manual touch
- effort (heaviest first): add mailboxes or reps > drop the heaviest manual touch > cut the active cohort > stagger cohort entry

On the worked example that means staggering entry until the steady-state load fits one call block, and only then cutting the active cohort to ~120-150. Staggering leads because it is a sequencer setting that costs near-zero and changes nothing about the sequence under test. Dropping a touch ranks below cutting the cohort even though both take about an hour: cutting the cohort keeps the design comparable to the last cohort, while dropping a touch forfeits that comparison for a cycle.

What this order starves: adding mailboxes or reps. It is the only fix that keeps the whole design and the whole list, and it loses every round on effort - a quarter to hire, weeks of warm-up ramp for a new domain.

- Promote it when the list is a fixed commitment that cannot be cut and the date is fixed too.
- Never let it short-circuit the warm-up ramp; a new domain pushed to volume is the fastest route to a blocked one.

**Automated-send load per mailbox per day:**

> active prospects × automated touches per sequence ÷ sequence length in working days ÷ mailboxes

Constraints on that number:

- Keep cold sends per mailbox well under 100/day (practitioner ceiling, widely repeated, not a law).
- New mailboxes and domains need a warm-up ramp measured in weeks before full volume (practitioner guidance).
- Platform policy (the hard numbers): major mailbox providers apply bulk-sender rules from 5,000 messages/day to their users, and require spam-complaint rates below 0.3% with below 0.1% recommended. Breaching these blocks the domain wholesale, regardless of legal compliance.
- Everything deeper - authentication, domain setup, warm-up execution, placement testing - goes to `mbfinotti/sales-skills@cold-email-deliverability`. This skill only sizes the plan to fit.

**Cohort staggering:** enroll in daily batches rather than one launch. It smooths manual-task load, spreads sends under mailbox caps, and limits the blast radius of a bad list segment.

**B2C:** capacity is consent- and fatigue-bound, not rep-bound. Enforce per subscriber:

- A frequency cap across all flows (vendor guidance clusters around a handful of marketing sends per week).
- One SMS per flow.
- Quiet hours per jurisdiction.
- One active flow per person at a time.

## KPI definitions, ranked by decisions bought per unit of instrumentation

Instrument in this order, and commit the first one that is actually measurable:

**reply rate > positive-reply rate > meetings per 100 prospects > connect rate > completion rate**

- value (settles the next revision): meetings per 100 prospects > positive-reply rate > reply rate > connect rate > completion rate
- effort (instrumentation plus wait before it reads, heaviest first): meetings per 100 prospects > connect rate > positive-reply rate > reply rate == completion rate

Reply rate and completion rate tie on effort because the sequencer emits both from the same report with no extra plumbing - what separates them is value, not cost.

- **Reply rate** - unique prospects replying ÷ prospects who received ≥1 touch. The primary B2B decision metric and the default pass threshold.
- **Positive-reply rate** - replies expressing interest or a referral ÷ prospects touched. Costs minutes of manual tagging per reply, and it is what separates a working sequence from a complaint generator: roughly half of replies are positive in vendor-published data, and a high reply rate full of "unsubscribe" is a failing sequence.
- **Meetings per 100 prospects sequenced** - the cleanest cross-channel outcome metric. (A per-100-touches variant exists; prefer per-prospect, since touch counts differ by design across patterns.)
- **Connect rate** - calls reaching a human ÷ dials. Worth instrumenting only where calls are actually staffed. Vendor numbers conflict badly (~5% to ~18%); establish your own baseline before setting a threshold.
- **Sequence completion rate** - prospects reaching the final touch without exiting. Diagnostic, never a target: completion rate is a function of your own sequence length and exit rules, so it only means anything against your own baseline, never against a borrowed threshold.
- **Opt-out rate** and **spam-complaint rate** - guardrails, not goals, and outside this ranking. Ceilings below.

What the order starves: meetings per 100 prospects, top on value and top on effort, so an efficiency ranking defers it forever. Promote it the moment the cadence is compared against another channel's investment - reply rate does not compare across channels, and that comparison is usually what the budget conversation turns on.

Deleted, not ranked: open rate. Mail-privacy proxies register phantom opens, so it is not a decision metric wherever any downstream number exists - and it exists here. Use it only when literally nothing else is measurable, and say the number is inflated when you do.

Judge at sequence/flow level: exit metrics count as success, and a touch-3 reply is the sequence working.

## Calibration (vendor-published; direction, not magnitude)

| Metric                                      | Reported average                      | Reported good                                          |
| ------------------------------------------- | ------------------------------------- | ------------------------------------------------------ |
| B2B cold reply rate                         | 4-5.8% - and declining year over year | 5-10%                                                  |
| Positive replies as share of replies        | ~48%                                  | 55%+                                                   |
| Meetings booked (per 100 emailed prospects) | 0.5-1                                 | 1-2                                                    |
| Bounce rate                                 | -                                     | under 3%; hard bounces removed immediately             |
| Opt-out / unsubscribe                       | -                                     | under 0.5%                                             |
| Spam complaints                             | -                                     | under 0.1% target, 0.3% hard ceiling (platform policy) |

Cold Calling 2.0-style referral sequences report 9-15% cumulative response - a different motion (referral ask above the buyer), not comparable to direct cold-email rates.

## Pre-commitment template

Complete every line before launch and store it with the plan:

- **Decision metric:** e.g. reply rate (B2B) or conversion rate (B2C) - the one the Interview confirmed is measurable.
- **Pass threshold:** e.g. "cumulative reply rate ≥ 4% at sequence level" - anchored to the user's own baseline when one exists, to the calibration table (labeled vendor-published) when not.
- **Guardrail ceilings:** opt-out < 0.5%, spam complaints < 0.1%, bounces < 3%. A sequence that hits its reply threshold while breaching a guardrail fails.
- **Secondary reads:** positive-reply share, connect rate, completion rate.
- **Review date:** after the first full cohort completes the sequence - never mid-flight on touch-1 data.
- **Planned response:** if below threshold, the single variable to revise first (length, spacing, channel mix, targeting, or personalization depth - pick one in advance).

One variable per revision. A cadence where length, copy, and list all changed at once teaches nothing.
