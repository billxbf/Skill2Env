# Routines - dry-run format, anchoring, cleanup

Applies only where the harness supports scheduled routines. Otherwise: one recurring calendar reminder ("Advertising check-in - re-run the advertising kickoff") is the whole fallback - do not simulate a scheduler.

## Dry-run format

Show every proposed routine in this shape and get explicit approval before creating anything:

```
Routine:    <name>
Runs:       <trigger  -  anchored, see below>
Does:       <one line  -  which skill it invokes, on what input>
Outputs to: <explicit channel  -  team chat, issue tracker, document, email>
First run:  <date> (dry run  -  produces the output, creates nothing recurring yet)
```

Create the recurring version only after the user approves the dry-run output. A routine approved on its description alone still surprises on its first real output.

## Trigger anchoring

Anchor to the media calendar, not arbitrary dates, whenever the routine's value depends on timing. Listed in the rung order of the skill's § 7 so the two never disagree - this section fixes each routine's timing, never its priority:

- Spend health check → monthly or quarterly, before the allocation decision it feeds - never after
- Pacing check → weekly, on the day the team reviews spend; tighten to daily during a flight's final week
- Kickoff re-invocation → monthly or quarterly, whichever matches the project's pace from the git log
- Search term mining → monthly, after the month-end budget reset
- Creative wear-out check → weekly or biweekly, aligned to the creative refresh cadence in `advertising-context.md`
- Seasonal-peak routines → computed from the flight dates in the artifact's constraints (e.g. peak-start minus 14 days), removed after the flight ends

Prefer an event trigger over a schedule when the harness offers one and it fits better. For example, run the pacing check when a fresh ad-account export lands, or the wear-out check when a new creative batch goes live, rather than on a clock that may fire against stale data.

## Output channels

Every routine names exactly one channel its result lands in. "Notify me" is not a channel.

Good channels:

- a named team-chat channel
- an issue in the project tracker
- a section appended to a standing document

If no channel can be named, the routine is not ready to exist.

## Cleanup

Before adding routines, list the existing ones and remove the obsolete:

1. List all scheduled routines the harness reports for this project.
2. Flag any anchored to an ended flight, a past seasonal peak, a paused channel, or a skill/process no longer in use.
3. Show the flagged list; delete only with approval.
4. Record surviving and new routines in `advertising-context.md` under in-flight work, so the next warm start knows what is already running.

Stale routines from a finished flight fire noise; noise trains the user to silence notifications, which buries the one routine that mattered.
