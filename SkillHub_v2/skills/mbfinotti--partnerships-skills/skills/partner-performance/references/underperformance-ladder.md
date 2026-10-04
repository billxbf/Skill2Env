# The Underperformance Ladder

## Design note

Every number in this ladder, trigger values, response times, plan durations, notice periods, is the user's design decision. Anything that can de-tier or terminate a partner needs legal review against the signed partner agreement before it ships.

The structure combines a trigger table with timelines and an escalation chain (adapted from carrier/supplier scorecarding practice in freight logistics, a structural parallel), and adds the coaching-first framing: flag at-risk partners in real time and intervene before formal ladder action starts.

## The staged structure

Never jump from a bad quarter to termination. Four stages, each documented - and they are also ranked, by partners recovered per unit of effort and irreversibility:

- efficiency: at-risk outreach > diagnostic conversation > corrective action plan > de-tier > exit
- value: de-tier > exit > corrective action plan > diagnostic conversation > at-risk outreach
- effort: exit > de-tier > corrective action plan > diagnostic conversation > at-risk outreach
- compliance cost: exit - notice terms in the signed agreement, legal sign-off, an outcome the partner can contest and nobody can undo - > de-tier, which may collide with tier commitments already promised in writing > corrective action plan, which becomes evidence for whichever side is right > diagnostic conversation == at-risk outreach, neither of which carries any

The stages:

1. **Trigger** - a KPI crosses its red-flag floor for a full measurement window, or a defined disengagement signal fires (deal registrations stop, portal goes quiet, certifications lapse).
2. **Intervention** - the PAM runs a diagnostic conversation within the stated response time: lead with the scorecard data, not accusation; diagnose cause (lost champion, capacity, competing vendor, product gap) before prescribing.
3. **Corrective action plan** - a written, signed plan (shape below) with checkpoints and a stated consequence.
4. **De-tier or exit** - only after the documented plan has failed at its final checkpoint.

De-tier outranks exit on value rather than tying with it: both reclaim the PAM's hours, but de-tiering leaves the partner's existing customers and pipeline in place and can be walked back if the diagnosis was wrong, where exit buys certainty and forfeits everything else permanently. They do not tie on any other axis either - exit costs more effort and carries the heavier compliance exposure.

Default rung: the diagnostic conversation, plus at-risk outreach ahead of the formal trigger wherever the scorecard recalculates often enough to see a partner drifting. The only condition that moves a partner up a rung is a dated checkpoint missed with a named owner - never a second bad quarter on its own, and never impatience.

The efficiency order starves the top two rungs: they carry the most value on the list and the most cost, so a ratio always finds another quarter of coaching cheaper, which is how a program accumulates partners nobody has ever removed. Promote de-tier the moment a signed corrective plan fails at its final checkpoint - at that point further coaching spends PAM hours the scorecard has already said are better spent elsewhere.

The order is a default, not a law. Re-rank against the program:

- A compliance breach or fraud skips every coaching rung by design (see the trigger table's carve-out).
- A partner with no signed tier commitments makes de-tiering cheap and reversible.

Where a PAM carries too many partners to notice drift, at-risk outreach is deleted from the ladder for that program and named as deleted - the ladder starts at the diagnostic conversation, rather than listing a rung nobody has the coverage to run.

## Trigger table

Deliver this as a table: trigger → action → timeline. Illustrative rows (values are examples for shape, not benchmarks):

| Trigger                                                                         | Action                                                                    | Timeline                                             |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ---------------------------------------------------- |
| Any KPI below its red-flag floor for one full window                            | PAM diagnostic call; findings logged in PRM                               | Within the program's stated response time (user-set) |
| Two or more KPIs red-flagged in the same period                                 | Formal performance review meeting; corrective plan drafted                | User-set, faster than a single flag                  |
| Disengagement signal: no deal registrations plus no portal activity in a period | PAM outreach - treat as at-risk, not yet as failing                       | User-set                                             |
| Corrective plan checkpoint missed                                               | Escalate one step up the chain; consequence restated in writing           | At the checkpoint date                               |
| Compliance breach, fraud, or brand damage                                       | Escalate directly to channel chief and legal - bypass the coaching stages | Immediately                                          |

## Escalation chain

Name a role at every step so no trigger dies in an inbox:

1. **PAM** - owns triggers, diagnostics, and the corrective plan day-to-day.
2. **Partner/channel manager lead** - owns repeated flags and missed checkpoints.
3. **Channel chief** - owns de-tier decisions and any plan touching a strategic partner.
4. **Channel chief + legal** - jointly own exit; termination follows the agreement's notice terms, never an ad-hoc email.

## Corrective action plan shape

- Cite the specific below-floor KPIs from the scorecard - data, not opinion.
- Set measurable recovery goals with dates; stage checkpoints across the plan (a 30/60/90-style staging is the analog's pattern - the actual lengths are the user's choice).
- State what the vendor commits in return: enablement session, leads, MDF, executive attention. A one-sided plan reads as a punishment memo.
- State the consequence of missing the final checkpoint - de-tier or exit - explicitly, in writing.
- Have both sides sign; log the plan and every checkpoint outcome in the PRM. The document trail is what makes a later exit defensible.

## De-tier vs exit

- **De-tier**: the partner stays in the program at a lower tier; apply the tier structure's own demotion, grace, and appeals rules (`mbfinotti/partnerships-skills@partner-tiering` owns those).
- **Exit**: termination under the partner agreement - gated on the documented corrective action having failed, except for the compliance/fraud carve-out, which still goes through legal.
- Record the reason and the evidence trail either way; an undocumented exit invites dispute and poisons the partner community's trust in the program.
