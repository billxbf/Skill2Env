# Routines

Propose 2 to 4 routines, never more. Each one costs the user attention every time it fires, so it has to earn its slot against the one routine that actually matters.

## Dry-run format

Show every proposed routine in this shape and get approval before creating anything:

```
Routine: pre-release docs pass
Trigger: on push of a tag matching v* (fallback: Thursdays 09:00, the usual release day)
Runs: samber/developer-relations-skills@changelog-writing
Output channel: a draft pull request on the release branch
Cost: one review pass per release
First fire: 2026-09-04
```

A routine with no output channel is noise the user silences within a week. If you cannot name where the result lands, drop the routine.

## Anchoring to the DevRel calendar

Prefer a real date the project already has over an arbitrary schedule:

- Release train dates → release notes, migration guides, docs freshness.
- CFP deadlines → proposal drafting, typically weeks before the deadline, not on it.
- Conference dates → talk outline, demo rehearsal, follow-up content window after the event.
- Quarter start → content calendar, budget review.
- Community rituals (meetup nights, office hours) → promotion before, artifacts after.
- Budget or board review dates → metrics read.

Two lead times are systematically underestimated: reviews by people who do not report to the owner, and anything requiring working code. Set the trigger earlier than feels necessary for both.

## Event triggers beat schedules

Where the harness can react to events, use them:

- A tag push.
- A merged pull request touching `docs/`.
- A new issue with a given label.
- A release published.

An event trigger fires exactly when the work exists. A schedule fires whether or not it does, which is how routines lose credibility.

Keep a schedule for anything with no natural event: the quarterly kickoff re-invocation, the monthly metrics read.

## Cleanup

Before adding routines, list the ones already installed and retire what no longer applies:

- Routines tied to a conference that already happened.
- Routines tied to a launch that shipped.
- Routines whose target skill was renamed or removed from the collection.
- Routines that have fired more than three times without producing an action.

Retire them explicitly and say so; a silently abandoned routine keeps consuming attention.

## Kickoff re-invocation

Always include one: a monthly or quarterly re-run of the kickoff itself. It resummarizes state from the artifact and re-routes, which is what keeps the artifact from going stale between projects. If the harness has no scheduled routines at all, fall back to a single recurring calendar reminder and stop there - do not simulate scheduling with reminders inside the artifact.
