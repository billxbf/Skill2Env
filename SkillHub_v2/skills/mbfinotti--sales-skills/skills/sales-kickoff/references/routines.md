# Routines - dry-run format, anchoring, cleanup

Applies only where the harness supports scheduled routines. Otherwise: one recurring calendar reminder ("Sales check-in - re-run the sales kickoff") is the whole fallback - do not simulate a scheduler.

## Dry-run format

Show every proposed routine in this shape and get approval before creating anything:

```
Routine:    <name>
Runs:       <trigger  -  anchored, see below>
Does:       <one line  -  which skill it invokes, on what input>
Outputs to: <explicit channel  -  team chat, issue tracker, document, email>
First run:  <date> (dry run  -  produces the output, creates nothing recurring yet)
```

Create the recurring version only after the user approves the dry-run output - a routine approved on its description alone still surprises on its first real output.

## Trigger anchoring

Anchor to the sales calendar, not arbitrary dates, whenever the routine's value depends on timing. Listed in the same install order as `mbfinotti/sales-skills@sales-kickoff` § 7 - highest value per unit of standing effort first:

- Deal inspection with `mbfinotti/sales-skills@deal-red-flags` → the day before the weekly forecast or pipeline call, on the deals in the current commit
- Sequence checkpoint → at the touch count committed in the cadence plan, not on a clock
- Kickoff re-invocation → monthly or quarterly, whichever matches the project's pace from the git log
- Sending-setup check → monthly, and always before a planned sequence volume increase
- Tape review of one recorded call → weekly, on the team's coaching or cadence-review day
- Source refresh via `mbfinotti/sales-skills@sales-radar` → quarterly

Prefer an event trigger over a schedule when the harness offers one, rather than on a clock that may fire against stale data.

- Deal inspection: run it when a fresh CRM export lands.
- Sequence checkpoint: run it when the sequencer reports the committed touch count reached.

## Output channels

Every routine names exactly one channel its result lands in. "Notify me" is not a channel.

Good channels:

- A named team-chat channel
- An issue in the tracker
- A section appended to a standing document

If none can be named, the routine is not ready to exist.

## Cleanup

Before adding routines, list existing ones and remove the obsolete:

1. List all scheduled routines the harness reports for this project.
2. Flag any anchored to a past quarter, a retired sequence or campaign, or a skill/process no longer in use.
3. Show the flagged list; delete only with approval.
4. Record surviving and new routines in `sales-context.md` under in-flight work, so the next warm start knows what is already running.

Stale routines from a previous quarter fire noise; noise trains the user to silence notifications, which buries the one routine that mattered.
