# Detection Rules - Computation and Fallbacks

How to derive the baselines and run each rule family. Label every output number with its provenance:

- Derived from the user's own data.
- A named practitioner source.
- A convergent practitioner range.

## Meaningful Activity - Define Before Anything Else

- **Field-change definition (default)**: a deal showed meaningful activity when its Stage, Close Date, or Amount changed. Logged calls and emails are activity in the CRM sense but do not indicate the deal moved - a staleness rule built on them can be satisfied without any progression, which is how stale pipeline survives review after review (ORM).
- **Last-activity definition (secondary)**: days since the last logged touch. Many hygiene programs and vendor tools key on this; it is a genuine practitioner disagreement, not a settled question.
- Run both as independent triggers: field-change age catches the deal that is "worked" but never moves; last-activity age catches the deal nobody has touched at all. A deal tripping both is the strongest stale signal.

## Deriving Per-Segment Baselines

1. Pull stage-change history for deals closed (won and lost) over the last 12-18 months. Open deals bias time-in-stage downward - a deal still sitting in a stage hasn't finished sitting there.
2. **Exclude the stale layer before computing anything** - a deal group carrying a large dead tail produces a longer, flatter close curve than its live deals actually have (ORM). First bucket the book by days since last meaningful change (<90 / 90-180 / 180-365 / >365), then compute medians on the live layer.
3. Per stage per segment (SMB / mid-market / enterprise at minimum; add region, source, or deal type where velocity genuinely differs), compute the median days from entry to exit. Median, not mean: a few zombies drag the mean until the threshold flags nothing. Company-wide averages mask the velocity difference between an SMB and an enterprise motion (Umbrex, Outreach).
4. Volume floor: Gong's guidance for reliable modeling is 400+ created opportunities including 150+ closed-won across at least four quarters. Below that, use internal top-quartile medians rather than external benchmarks, and label the baseline low-confidence.
5. Also compute the typical activity interval on closed-won deals (calibrates the last-activity window) and historical close-date accuracy within the chosen tolerance.

**When no history exists**:

- Approximate a per-stage prior by splitting the known full-cycle length across stages weighted by the team's judgment.
- Mark every baseline "low-confidence prior".
- Schedule replacement after one full cycle of real data.

## Stale-Deal Rules

Multiplier and window are segment-dependent - convergent across Umbrex, Outreach, and DealHub, so likely real operating numbers rather than one vendor's marketing:

| Segment              | Discovery/Qualified median | Evaluation/POC median | Proposal/Negotiation median | Stale multiplier | Inactivity flag |
| -------------------- | -------------------------- | --------------------- | --------------------------- | ---------------- | --------------- |
| SMB / high-velocity  | 5-10 days                  | short                 | 3-10 days                   | ~1.5x median     | 14-21 days      |
| Mid-market           | 7-14 days                  | 14-30 days            | 7-14 days                   | 1.5-2.0x         | 30-45 days      |
| Enterprise / complex | 14-30 days                 | 30-90 days            | 14-30+ days                 | 2.0x median      | 60-90 days      |

Medians: Umbrex. Inactivity rule of thumb: DealHub - with **legal and procurement reviews explicitly exempt** from stale flags. Worked example (Umbrex, Outreach state the identical rule): Proposal median 12 days → stale at 18-24 days.

Additional triggers, all VERIFIED practitioner rules:

- No activity in 14 days on mid/late-stage deals (Umbrex, Outreach).
- Next step dated in the past, or no scheduled future meeting at all.
- **12-month rule** (ORM): no meaningful change in 12 months marks the truly dead layer - close curves rarely carry meaningful expectation past 52 weeks. ORM's customer aggregate: more than 10% of open pipeline typically sits untouched past 12 months.

Distinguish _stale_ (no recorded motion - a data question this audit answers) from _dead_ (buyer evidence says it's over - a judgment the review conversation makes).

## Push-Count Rules

Track pushes as a field, not a memory (ORM): count close-date changes per deal from field history, snapshot deltas, or a dedicated counter field, and sort late-stage pipeline by that count - the deals at the top are the forecast risk.

| Trigger                          | Action                                                                | Provenance                                                                                                                                           |
| -------------------------------- | --------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Second push**                  | Escalate to manager deal inspection                                   | ORM - the best single predictor of slippage; a quarter-to-quarter slip lowers close odds even in commit. Umbrex flags "repeat pushers" at >= 2 moves |
| Push crossing a quarter boundary | Worse than an in-quarter nudge; require a stated reason on the change | ORM structural fix for close-date stuffing                                                                                                           |
| 3+ slips                         | Disqualification-warranting                                           | SalesOpsClub                                                                                                                                         |
| Close date already past          | Automatic flag                                                        | Common practice, uncontroversial                                                                                                                     |

**Slipping vs dead - stacked evidence, not the date field.** Open with "what has to happen before this date becomes realistic?", then stack the signals:

- Mutual-action-plan progress with dated owners.
- Multi-threading depth.
- Economic-buyer engagement.
- Entry into procurement/legal.
- Champion responsiveness.

A delayed next step alone may be harmless; combined with a pushed close date, single-threading, and budget hesitation it becomes a stronger, explainable case for intervention (AskElephant). Context on why multi-threading is a real signal: Ebsta x Pavilion's 2024 benchmarks (4.2M+ opportunities) found multi-threading lifts win rates 130% on deals over $50k.

Once a slip is confirmed, update the CRM close date immediately with a note on the evidence and the revised plan - the worst outcome is intervening on the deal but leaving the forecast untouched.

**When the CRM retains no field history**: push counts cannot be reconstructed.

- Add a push-counter field incremented on every close-date change starting now.
- Report the metric as "collecting - first readable next audit".
- Never estimate a historical push count.

## Field-Completeness Rules

1. Start from the forecast-critical set, not the whole schema:
   - Next step and next-step date, close date, amount, stage, forecast category, loss reason on closed-lost.
   - The qualification fields the forecast actually reads (champion, economic buyer, paper process in enterprise motions).

   Amount, stage, and close date are the highest-value validation targets - they are the meaningful-activity fields themselves (ORM).

2. Report completeness per field as % of open deals populated against the 90-95% target (80% floor - Saber; Komo/DAMA), next to the decision that field feeds.
   - **Do**: "37% of deals have no next step, so Monday prioritization runs blind."
   - **Don't**: "field X is 63% complete."
3. Remediate in efficiency order - **stage-gated validation rule > owner nudge > auto-capture** - reading the axes below before deviating from it. The distinction underneath the order: a required field checks that something was entered; a validation rule checks that what was entered makes sense (ORM).

   - effort: auto-capture > owner nudge > stage-gated validation rule. Auto-capture is an integration project - a quarter of work, and hard to unwind once email and calendar data is flowing. A nudge takes an hour to configure and then levies a standing tax on every rep who receives it. A validation rule takes about the same hour, then costs seconds and only on advancement to a late stage; switching it off reverses it completely.
   - value: auto-capture > stage-gated validation rule > owner nudge. Auto-capture fills the fields whether anyone cooperates or not; the validation rule protects exactly the fields the forecast reads, at the moment they start mattering; a nudge only improves the odds someone acts.
   - compliance cost: auto-capture > stage-gated validation rule == nudge. Capturing email and calendar content triggers a consent and data-processing review in several jurisdictions, and ingested history cannot be put back. The tie is a genuine nil on both sides - neither a rule nor a nudge reads anything from outside the CRM - so this axis exists only to separate auto-capture from the other two.

   More required fields is deleted from this menu rather than ranked last: heavy requirement breeds the fabricated placeholders of step 4, so the skill's own constraint rules it out. Hold the cap at 5-7 required fields per object (AskElephant).

   What this order starves is auto-capture: highest value and highest effort, so a ratio never selects it. Promote it anyway when an activity-capture tool is already deployed (the integration cost is already paid, leaving configuration), or when reps sit at their friction limit and every cheaper option spends friction the team does not have.

   Treat the order as a default that shifts with context and with who executes it. Re-rank it against the Interview answers:
   - A result due this week leaves auto-capture unbuilt.
   - A recurring mandate is what pays for it.
   - A manager who already runs a weekly pipeline review can carry a nudge's follow-up as review time instead of rep friction.

4. Check populated fields for **fabricated placeholders**, which heavy requirement breeds:
   - Sentinel values ("TBD", ".", "123", "n/a n/a n/a", "999999").
   - Identical boilerplate next steps across many deals.
   - Next-step dates always exactly N days out.
   - Amounts that never vary off a round default.

   Count fabricated as empty. If placeholders cluster on required fields, the remediation is fewer requirements plus validation rules, not policing harder.

## Dibs-Deal Detection

Claim-only deals - opened to reserve an account, never worked - hide from single rules because they are "new". Flag the combination:

- Early-stage, at or near the entry stage since creation;
- No meaningful change and no activity logged since the week of creation;
- No contact attached, or no next step ever set;
- The same owner holds a cluster of similar records.

Route these to their own disposition path: the question is account ownership (a territory and routing decision), not deal quality. Closing them without settling ownership just makes the rep open new ones. Provenance: named failure mode from RevOps Co-op - claim-only records rot, block marketing from targeting the account, and create friction in territory moves.
