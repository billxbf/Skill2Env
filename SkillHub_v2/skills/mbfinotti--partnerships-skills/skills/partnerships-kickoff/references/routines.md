# Routines - dry-run format, anchoring, cleanup

Applies only where the harness supports scheduled routines. Otherwise the recurring calendar reminder is the whole fallback - do not simulate a scheduler.

## Dry-run format

Show every proposed routine in this shape and get explicit approval before creating anything:

```
Routine:    <name>
Runs:       <trigger - anchored, see below>
Does:       <one line - which skill it invokes, on what input>
Outputs to: <explicit channel - team chat, issue tracker, document, email>
First run:  <date> (dry run - produces the output, creates nothing recurring yet)
```

Create the recurring version only after the user approves the dry-run output. A routine approved on its description alone still surprises on its first real output.

## Trigger anchoring

Anchor to the partnership calendar, not arbitrary dates, whenever timing carries the routine's value. The kickoff's § 7 states each candidate's own anchor; here are the mechanics behind them.

- Compute a date-derived trigger from a field in `partnerships-context.md`, never from a fixed calendar date:
  - Payout-run review, from the payout date.
  - Contract-renewal check, from the renewal and auto-renewal dates (e.g. renewal minus 30 days).
  - Campaign routines, from a live creator campaign's flight dates.
- Delete a derived routine when its source date is gone - a renegotiated contract, an ended flight - rather than letting it fire against a dead anchor.
- Anchor an integrity routine inside the window that makes it actionable: holds must land before money moves, and flagged commissions must still sit inside the validation window.
- Anchor a reporting routine before the decision it feeds, never after it.
- Marketplace listing reviews follow the cadence each marketplace imposes, not one of your own.

Prefer an event trigger over a schedule when the harness offers one and it fits better, rather than a clock that may fire against stale data. For example: run the payout audit when a fresh commission-run export lands, or the abuse sweep when a referral-reward spike fires an alert.

## Output channels

Every routine names exactly one channel its result lands in. "Notify me" is not a channel; a named team-chat channel, an issue in the project tracker, or a section appended to a standing document is. If no channel can be named, the routine is not ready to exist.

## Cleanup

Before adding routines, list the existing ones and remove the obsolete:

1. List all scheduled routines the harness reports for this project.
2. Flag any anchored to an ended campaign flight, a terminated partner contract, a sunset program or motion, or a skill/process no longer in use.
3. Show the flagged list; delete only with approval.
4. Record surviving and new routines in `partnerships-context.md` under in-flight work, so the next warm start knows what is already running.

Stale routines from a finished campaign or a dead partner contract fire noise; noise trains the user to silence notifications, which buries the one routine that mattered.
