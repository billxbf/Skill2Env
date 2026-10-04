# Incident response runbook

Contents: runbook template · deadline clock · intake · report-taking checklist · recusal · decision · notification templates · negative example · closure · case record · transparency report.

Produce this as a private document for the response team - separate from the public code of conduct, which only summarizes it. Publish a reporter-facing "what to expect when you report" page instead of the playbook itself, and say in it that internal guidelines exist and change. A published step-by-step procedure gets used to argue that the team failed to follow its own process, which is a cheap way to stall any enforcement action.

## Table of Contents

- [Runbook template](#runbook-template)
- [Team](#team)
- [Intake](#intake)
- [Handling](#handling)
- [Outcomes](#outcomes)
- [Communication](#communication)
- [Records](#records)
- [Review](#review)
- [Deadline clock](#deadline-clock)
- [Intake](#intake)
- [Taking a report in person or in chat](#taking-a-report-in-person-or-in-chat)
- [Recusal](#recusal)
- [Investigation and decision](#investigation-and-decision)
- [Notification templates](#notification-templates)
- [Case record](#case-record)
- [Transparency without exposure](#transparency-without-exposure)

## Runbook template

```
# <Community> conduct response runbook

## Team
Members, terms, contact alias, escalation body above the team.

## Intake
Channels, anonymous path, alternate path, acknowledgment target.

## Handling
Recusal rules, evidence collection, interview order, decision rule.

## Outcomes
The ladder, the non-ladder outcomes, who executes each action on each platform.

## Communication
Templates: acknowledgment, reported-person notice, reporter closure, team-internal note.

## Records
Where cases live, who has access, retention period, what is deleted when.

## Review
Statistics cadence, transparency report cadence, ladder review trigger.
```

## Deadline clock

The clock starts when the team receives the report, not when it starts working. Write the two deadlines into the case record immediately and put them in calendars: acknowledgment (published bands in use: one business day at Django, three business days at CNCF) and decision (Aurora and Gardiner's worked example is 10 business days). This is the one commitment to hold literally - the dominant enforcement failure is a team that never quite decides, not a team that decides too fast.

For an incident many people witnessed, post a short holding note early: the team has the report, is working on it, and here is where to send more information. It also gives you somewhere to redirect the pile-on.

## Intake

- Acknowledge every report, including the ones filed only for the record. Send a lighter acknowledgment when the reporter says the incident is already resolved.
- Ask for: who was involved (name, handle, role, affiliation), what happened with dates and links, where it happened, the reporter's relation to the events, whether they want to remain anonymous, and whether anyone is in immediate danger.
- Safety first: if a report describes physical danger, point to local emergency services before anything procedural.
- Preserve evidence immediately. Chat messages disappear when deleted, so screenshot and archive before removing anything; forge comments keep an audit trail when hidden rather than deleted.
- Assign a random case code, and code names for the people involved, so the case can be discussed in team notes without identities.

## Taking a report in person or in chat

Give this to everyone likely to receive a report first-hand - event volunteers, channel moderators, maintainers. Adapted from Mary Gardiner and Valerie Aurora's report-taking checklist (CC BY-SA 4.0), so keep the attribution if you ship it as a handout.

1. Move somewhere others cannot overhear, and have somewhere to write.
2. Ask whether they want to make a formal report. Promise nothing on the team's behalf beyond doing its utmost to protect their confidentiality and safety. If you are legally obliged to report certain disclosures, say so before they start.
3. If they do not want to file, you may decline to hear it - particularly if you are already absorbing more than your share of this work.
4. Ask them to describe what happened: who the reported person is, their own name and contact, time, date, place, what occurred, who else was involved. Respect anything they will not share.
5. On any sign of immediate physical danger, act on the safety plan first and note that action in the report.
6. Offer concrete help for right now - fetching a friend, a private room, an escort out.
7. Thank them.
8. Send the report to the response team by the documented route.

Never:

- share it outside the team
- ask the reporter or the harmed person to propose the remedy
- push them toward police or medical help they have not asked for

Do not assume they trust you, or any given staff member, by default.

## Recusal

Members declare a conflict in writing as soon as they are involved in the incident, close to a party, share an employer, hold biasing private information, or simply cannot be impartial. Two grades, because treating them identically either paralyses a small team or lets a conflicted member vote:

- **Hard conflict** (accused, close personal or professional relationship, personal stake): excluded from discussion, from the vote, and from the confidential material.
- **Soft conflict** (same employer without a close relationship, appearance of conflict): may take part in discussion, may not vote.

Record the conflict and its grade in the case notes before the investigation starts. Recusal takes effect the moment the member realises it applies - including mid-read of the report - and someone else is assigned to execute it: remove them from the documents, open a channel without them. When every eligible member is conflicted, the case goes to the escalation body named in the runbook.

## Investigation and decision

1. Read the evidence before talking to anyone.
2. Interview the reporter, then witnesses, then the reported person. Take notes in neutral language.
3. Decide with a rule fixed in advance, covering ties and absences - a workable default for a small team is: at least two non-conflicted members must agree, consensus is the target, a two-thirds majority is the fallback, and an unresolvable case escalates. Pick a rule that leans toward acting: across observed cases the common error is taking no action or taking too long on a valid complaint, not overreacting.
   Judge impact before intent. What did the behaviour do to the person and the room, how do you stop it recurring, what makes people safer now. Intent matters only as a predictor: someone who meant no harm _and_ recognises it, takes responsibility and changes is low risk; someone who meant no harm and refuses all three is not.
4. For severe or legally exposed cases, an external investigator or mediator is a legitimate option.
5. A team may open a case proactively when there is a serious ongoing safety risk and no formal report.

## Notification templates

Order: show the harmed person the proposed response privately first - to catch a fact you missed or a retaliation risk you did not see, not to ask permission - then notify the reported person, whose only required answer is whether they will comply. The decision takes effect immediately, even while an appeal is being considered.

**To the reported person** - four parts, in this order:

```
1. Behaviour: on <date>, in <space>, you <specific behaviour, neutral wording>.
2. Impact: this <effect on the affected person / on the community>.
3. Expected change: <specific, observable behaviour going forward>.
4. Consequence: <rung>, effective <date>, ending <date or "permanent">.
   <How to respond, and to whom, if they believe this is factually wrong.>
```

Never name the reporter. Do not argue the case in this message; it states a decision that has already been made.

**To the reporter, before enacting the resolution:**

```
Thank you for the report (case <code>). We have reviewed it and propose <resolution>.
We are telling you before we act, and welcome your view  - we are not bound to act on it,
and we will not share your identity with anyone outside the response team.
```

**To the reporter, at closure:**

```
Case <code> is now closed with <resolution, at the level of detail you can share>.
If new information comes to light, tell us and we will reopen it.
```

Detail limits: the reporter learns the outcome that affects them, not the full private correspondence with the reported person.

### Negative example: the conciliatory notice

Almost every first draft of a decision notice looks like this one, because it feels kind:

> Hi Sam - we've had a complaint about the thread in #core yesterday. I'm sure there was no bad intent on your side and it's probably a misunderstanding. Could you send an apology in the channel, and maybe the two of you could hop on a call with me to clear the air? In the meantime please just steer clear of Alex. Thanks for understanding!

Six defects, each one sourced to a documented failure:

1. **Prejudges intent** ("no bad intent") and volunteers the team's excuse before hearing anything - the discussion is now about Sam's feelings.
2. **Names the other party**, which identifies the reporter.
3. **Requests an apology**, destroying the only useful signal: whether Sam would have apologised unprompted.
4. **Proposes mediation in place of a decision**, before either party consented, reframing a conduct violation as two people who don't get along.
5. **Imposes a stay-away condition** instead of a decision, leaving the question of whether Sam is a risk unanswered.
6. **States no consequence, no date, no route to contest it** - so nothing is actually decided.

The same facts, written as a decision:

> Sam - on 12 May in #core you told Alex to "stop wasting everyone's time with beginner questions", and repeated it after another member asked you to stop. Newcomers stopped posting in that channel for the rest of the day.
>
> Going forward: no dismissive comments about another member's experience level, anywhere in the community.
>
> This is a formal warning under the code of conduct, effective today, recorded in our case log. A further incident moves to a temporary suspension. If you believe the facts above are wrong, reply to conduct@example.org within 14 days and the team will review; the warning stands while we do.

It names the behaviour, the impact, the change, and the consequence - and it takes four sentences.

## Case record

One record per case, with these fields, kept where only the response team can read it:

`case_code` · `report_date` · `surface` · `person_codes` · `neutral_summary` · `scope_determination` (in scope / out of scope / other body) · `safety_risk` · `harassment_risk` · `conflicts_declared` · `investigation_notes` · `decision` · `decision_rule_met` · `rung_applied` · `effective_date` · `end_date` · `communications_sent` · `closure_date` · `follow_up`

Retain under the organization's data-retention policy and applicable privacy law. Restrict access to the team, and treat leaking a case as grounds for removal from the team. Keep prior violations findable - the ladder is meaningless if nobody can tell that this is the third warning.

Schedule the restoration of every time-boxed sanction the day it is applied. Suspensions that outlive their stated end date are one of the fastest ways to lose the community's trust in the process.

## Transparency without exposure

- Publish a faithful reporter-facing summary of the process - what to expect, in what order, by when. Process transparency costs nothing and is what makes reporting feel safe. Keep the operational playbook internal and revisable.
- Everyone who witnessed a violation should learn that it was answered. A case handled entirely in private messages leaves the room believing nothing happened, and that belief is what makes people leave.
- Publish aggregate statistics on a fixed cadence - every six months is a proven rhythm - and an annual anonymized trends report.
- Never discuss an individual case publicly. When a public statement is unavoidable, it comes from the escalation body, not from the response team.
- Default to describing the behaviour without naming the person: a statement from the team carries far more weight than the same words from a member, and naming is often read as disproportionate whatever the facts. Name someone only when people need it to stay safe - a known repeat offender attending an event. Decide the stance in advance; an ad-hoc decision under pressure is not defensible.
