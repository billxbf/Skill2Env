# Worked example

Every name, company, and detail below is fictional, written to illustrate the method.

## Table of Contents

- [Input: six weeks of messy notes, pasted by the user](#input-six-weeks-of-messy-notes-pasted-by-the-user)
- [Output: the review](#output-the-review)
- [Negative example: the evidence rule in action](#negative-example-the-evidence-rule-in-action)

## Input: six weeks of messy notes, pasted by the user

```
Deal: Halvern Logistics - routing platform - ~$80K/yr - stage: Proposal
Aiming to close end of Q3.

Apr 2 - intro call w/ Dana (Ops Director). Great energy. Their dispatch process
is "a mess" her words. She wants to move fast. Demo booked.
Apr 9 - demo. Dana + 2 of her team. Went really well, they loved the
multi-stop view. Dana said "this would save us so much time."
Apr 16 - follow-up. Dana says budget shouldn't be a problem, finance will
sign off once she recommends. Mentioned IT raised something about our API
security, she'll handle it.
Apr 24 - Dana pushed our check-in to next week, busy week on her end.
May 1 - call w/ Dana. Asked about timing - she said "hopefully this quarter,
maybe early next." Their contract with RouteMinder ends Sept 30, they have
to decide before that. Sent proposal after the call per her request.
May 13 - emailed Dana re: proposal. No reply yet.
May 20 - Dana replied, apologized, said she's presenting it internally "soon."
Moved close date from Jun 30 to Jul 31 in the system.
```

## Output: the review

```
DEAL RED-FLAG REVIEW - Halvern Logistics, reviewed May 21, notes covering Apr 2 - May 20
Snapshot   : ~$80K/yr, stage Proposal, ~7-week cycle so far, B2B mid-market
Timeline   : Apr 2 intro (Dana) - Apr 9 demo (Dana +2 team) - Apr 16 follow-up -
             Apr 24 buyer reschedule - May 1 call, proposal sent - May 13 no
             reply - May 20 reply, close date pushed Jun 30 -> Jul 31.
             Record thins after May 1: two entries in three weeks.

Red
- Economic buyer never met - HIGH - "budget shouldn't be a problem, finance
  will sign off once she recommends" (Apr 16). Second-hand relay; no logged
  contact with any budget owner in seven weeks, at Proposal stage.
  Play: draft the forwardable business-outcome note for Dana to send to the
  budget owner; a meeting before the internal presentation, not after.
  Response: work it. Not escalate - Dana has not been asked for this door
  even once; escalation is earned after two refusals, not before the first.

Amber
- Blocker mentioned but never addressed - HIGH (Assumed) - "IT raised
  something about our API security, she'll handle it" (Apr 16). Never
  mentioned again; no evidence it was handled.
  Play: ask Dana what IT's actual objection was, in their words, and book a
  direct technical conversation this week. Response: work it.
- Happy-ears language - MED (Verified) - "Went really well, they loved the
  multi-stop view"; "this would save us so much time" (Apr 9). Enthusiasm
  recorded, no commitment of time, people, or data anywhere in the notes.
  Play: attach a small concrete ask to the internal presentation (their
  dispatch volume data for a sized value case); the response is the signal.
  Response: trade it - Dana's own presentation funds the ask.
- Unprompted proposal request - MED (Verified) - "Sent proposal after the
  call per her request" (May 1), before any decision process appears in the
  notes. Play: trade one structured conversation about how the proposal will
  be evaluated, and by whom, for the internal presentation date.
  Response: trade it.

Watch
- Response latency growing - "emailed Dana re: proposal. No reply yet"
  (May 13), reply after a week (May 20), against same-week replies in April.
  Two data points - a pattern is forming, not formed. Confirms it: another
  widening gap. Clears it: cadence back to April's norm.
- Close date pushed - one push, Jun 30 -> Jul 31 (May 20), no external
  reason recorded. One push is Watch; a second without a new external cause
  is Red.

Gaps (Unknown) - in chase order
- Single-threaded / stakeholder coverage - DESK CHECK - two team members
  attended one demo, unnamed, never heard from again; their names are in the
  rep's own calendar invite, not in the notes. Ask: "Who besides Dana is
  affected by this decision, and when do we meet them?"
- Champion test unresolved - ONE QUESTION - Dana is engaged, but the notes
  show no act of internal selling yet ("presenting soon" is intent, not
  action). Ask: "What has Dana done for this deal in rooms we were not in?"
- Decision process undocumented - ONE QUESTION - "presenting it internally
  soon" is the only process visible. Ask: "What are the steps, and the
  names, between Dana's recommendation and a signed agreement?"
- No quantified impact - ONE QUESTION - "a mess" and "save us so much time"
  carry no number. Ask: "What number does Dana's team put on the current
  dispatch problem?"
- No mutual action plan - ACCESS ASK - no shared dated milestones; a plan
  Dana co-owns costs her real capital. Ask: "Which upcoming steps does
  Halvern own, by name and date?"

Cleared
- No compelling event - CLEARED - "Their contract with RouteMinder ends
  Sept 30, they have to decide before that" (May 1). Dated, buyer-owned,
  external. Note: the Jul 31 close date is the seller's, not tied to it.

Risk check
- Past stages: risk in HOW - the deal reached Proposal on one relationship
  and a relayed budget assurance; stage criteria were felt, not evidenced.
- Next stages: risk in the PLAN - the plan is "Dana presents soon": no date,
  no economic buyer, an unaddressed IT objection, no agreed process.

Verdict
Evidenced: a real compelling event (Sept 30), a real engagement risk
(economic buyer unmet, IT blocker unaddressed, enthusiasm without
commitment). Merely absent: process, plan, quantified impact, coverage -
gaps to ask about, not reasons to panic. Single next action: the economic-
buyer meeting before Dana's internal presentation - it converts the two
largest risks at once. That promotes an access ask over the cheaper desk-
check and one-question rungs; the fact that moved it is the imminent
internal presentation, after which no cheap read clears a budget veto.
Not a win-probability score.
```

## Negative example: the evidence rule in action

Wrong - a finding stated without evidence, graded as if confirmed:

```
Red - Champion cannot reach power - HIGH - Dana is clearly being blocked
from getting us to leadership.
```

Nothing in the notes says this. No fragment is quoted because none exists; "clearly" is doing the evidencing. This is the reviewer's inference presented as the buyer's reality - exactly what the review exists to catch in the rep's own notes.

Right - the same territory, graded honestly:

```
Gaps (Unknown) - Champion's reach to power - the notes never show Dana
attempting or failing to escalate; there is no evidence either way.
Ask: "Who does Dana report to, and what stops an introduction this month?"
```

And for contrast, the Apr 16 budget line shows the Assumed grade working correctly: "finance will sign off once she recommends" is quotable - so it is not Unknown - but it is a second-hand relay of someone else's authority, so it can never be graded Verified.

The three confidence states, restated:

- A finding with no quote is Unknown.
- A finding whose only quote is hearsay is at most Assumed.
- Verified is reserved for the buyer's own first-hand words.
