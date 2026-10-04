# Routines - dry-run format, anchoring, cleanup

Applies only where the harness supports scheduled routines. Otherwise: one recurring calendar reminder ("RevOps check-in - re-run the revops kickoff") is the whole fallback - do not simulate a scheduler.

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

Anchor to the revenue calendar, not arbitrary dates, whenever the routine's value depends on timing. Listed in the same install order as `mbfinotti/revops-skills@revops-kickoff` § 7 - highest value per unit of standing effort first - so there is only ever one order to follow:

- Forecast diagnostic → the week before each close (compute from the fiscal calendar in `revops-context.md` constraints); anchor it to the board meeting date instead when that meeting, not the close, is what the number feeds
- Kickoff re-invocation → monthly or quarterly, whichever matches the project's pace from the git log
- Pipeline hygiene pass → weekly, on the team's pipeline-review day
- CRM field-governance review → monthly, after month-end close
- Source refresh via `mbfinotti/revops-skills@revops-radar` → quarterly

Prefer an event trigger over a schedule when the harness offers one and it fits better - e.g. run the hygiene pass when a fresh CRM export lands, rather than on a clock that may fire against stale data.

## Output channels

Every routine names exactly one channel its result lands in. "Notify me" is not a channel.

Good channels:

- A named team-chat channel.
- An issue in the project tracker.
- A section appended to a standing document.

If no channel can be named, the routine is not ready to exist.

## Cleanup

Before adding routines, list the existing ones and remove the obsolete:

1. List all scheduled routines the harness reports for this project.
2. Flag any anchored to a past quarter, a shipped project phase, or a skill/process no longer in use.
3. Show the flagged list; delete only with approval.
4. Record surviving and new routines in `revops-context.md` under in-flight work, so the next warm start knows what is already running.

Stale routines from a previous quarter fire noise; noise trains the user to silence notifications, which buries the one routine that mattered.
