# Public postmortem structure

Structure, filtering rules, and a skeleton for step 5 of the workflow.

## The publish decision

Internal and external postmortems serve different jobs, not just different detail levels: the internal version optimizes for deep technical accuracy across engineering, product, and support; the external version optimizes for clarity, reassurance, and accountability toward users and partners. The decision to publish affects legal exposure, customer trust, and long-term reliability culture - make it deliberately per incident (against the ladder in SKILL.md step 5), never as an unexamined default in either direction.

The sourced case for leaning toward publication comes from the Google SRE workbook: the value of a postmortem is proportional to the learning it creates, so sharing it as widely as possible - "perhaps even with your customers" - multiplies that value. The workbook also calls a thoughtful and honest postmortem "a key tool in restoring shaken trust." Hand that argument to a team hesitant to publish.

## Channel choice

- **Status page** - suits active users monitoring uptime in the moment; the right home for the default summary postmortem attached to the incident.
- **Engineering blog** - suits the deeper technical write-up, and is the better channel specifically for API/developer-audience incidents: that audience is largely technical and reads the deep version for trust-building, not just resolution confirmation. Link it from the incident entry so both audiences find it.

## The three-question structure

Frame the external document around the three questions a customer actually has (Google's Customer Reliability Engineering framing):

1. **Why did this happen?** - the root cause and trigger section.
2. **Could it have been worse?** - a "where we got lucky" section. Transfer this from the internal version close to as-is, reworded only for clarity; its honesty is the section readers trust most.
3. **How do we make sure it won't happen again?** - the action-items table.

## What transfers from the internal document

Sections that move from internal to external well, with light rewording:

- **Quantified impact** - users/requests affected, error rate, duration; include SLO or error-budget burn where you publish those.
- **A UTC timeline** from first alert to resolution. Timestamps anchor credibility; vagueness reads as concealment.
- **2-5 systemic contributing factors**, framed blamelessly (see below).
- **Action items**, split into **mitigative** (fixes this specific gap) and **preventative** (fixes the class of failure). Publishing the split shows you distinguish patching from learning.

What gets filtered out on the way to public:

- Internal system names and architecture detail beyond what the explanation needs.
- Individual names and team attributions.
- Security-sensitive specifics.
- Any speculation that didn't survive the internal review.

This filtering step is the one internal postmortem processes skip entirely - add it explicitly to your pipeline.

## Blameless, concretely

- **Never name an individual human.** Write "a network engineer", not the person's name - this is what blameless concretely means in the document itself, not just in tone.
- Reframe every "who caused this" instinct as "what condition allowed this". The trigger is a condition; the cause is systemic.
- Run the internal review timeline-first, analysis-second: establish the facts before assigning cause.
- Use 5-Whys with cited evidence at each step, ending in a root cause with named systemic fixes - never ending at a person.

## Follow-through is part of the artifact

Postmortems without follow-through are theater - written to satisfy a process, not to change anything; one source pins the theater threshold at an action-item completion rate below 50%. Treat action-item tracking as part of this skill's own success metric (see SKILL.md Measurement): give every public action item an owner and a status, and when the promised items complete, say so - an update on a months-old postmortem is a cheap, high-credibility trust signal.

## Skeleton

```markdown
# [Plain-language incident title] - [date]

## Summary

One paragraph: what broke, who was affected, for how long, and the one-sentence cause.

## Impact

Quantified: affected share of requests/users, error rates, duration, regions/components.

## Timeline (all times UTC)

- HH:MM - first alert fired
- HH:MM - incident opened publicly (Investigating)
- HH:MM - cause identified
- HH:MM - mitigation deployed (Monitoring)
- HH:MM - resolved

## Why this happened

Root cause and trigger, plus 2-5 systemic contributing factors, blamelessly framed.

## Where we got lucky / could it have been worse

Honest assessment of the blast radius that almost was.

## What we are doing about it

| Action | Type         | Status             |
| ------ | ------------ | ------------------ |
| ...    | mitigative   | done / in progress |
| ...    | preventative | in progress        |

We will update this table as items complete.
```
