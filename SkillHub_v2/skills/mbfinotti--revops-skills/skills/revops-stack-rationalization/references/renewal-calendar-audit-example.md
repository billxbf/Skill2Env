# Worked Example: Renewal-Calendar Audit

The renewal calendar is the review's binding constraint: the average org manages ~211 SaaS renewals a year, and renewals carry ~87% of software spend (Zylo, 2026 edition). Most of the money only becomes movable at a renewal - so the calendar, not the scoring, decides when a verdict can act.

## Calendar schema

One row per contract (a vendor can hold several):

| Field                        | Why it exists                                                                             |
| ---------------------------- | ----------------------------------------------------------------------------------------- |
| Tool / contract              | The unit is the contract, not the vendor - terms differ per contract                      |
| Named owner                  | The accountable person per tool; committee ownership means nobody answers for the renewal |
| Annual cost + payment terms  | From the contract or AP data, never estimated                                             |
| Term end date                | The anchor everything else is computed from                                               |
| Auto-renew flag              | Auto-renew plus a missed notice window locks in a full extra term                         |
| Notice window                | Typically 30-90 days before term end; read it from the contract, never assume             |
| Verdict (from the TIME pass) | Links the calendar to the register                                                        |
| Action deadline              | Computed - see below                                                                      |
| Recertification date         | Access/ownership/need recheck scheduled before auto-renew fires - the governance link     |

## Action-deadline arithmetic

```
notice-window opens = term end - notice period
action deadline     = notice-window opens - negotiation lead time
```

Set negotiation lead time by stakes, not a constant:

- An Eliminate needs days: confirm nothing breaks, give notice.
- A renegotiation or Migrate needs a quarter or more of lead.

Direction to keep, magnitude to drop: one procurement vendor's own data (Vertice) claims starting more than 90 days out saves materially more than starting inside 30 days - treat as directional support for early starts, never cite the percentage.

## Worked mini-calendar (today = March 1)

| Contract                       | Cost | Term end        | Notice | Auto-renew | Verdict   | Window opens | Action deadline                                                                                      |
| ------------------------------ | ---- | --------------- | ------ | ---------- | --------- | ------------ | ---------------------------------------------------------------------------------------------------- |
| Sales-intelligence database    | high | May 31          | 90d    | Yes        | Migrate   | Mar 2        | now - window opens tomorrow; renegotiate to a bridge term or the migration runs against a live meter |
| ABM display platform           | mid  | Jun 30          | 60d    | Yes        | Eliminate | May 1        | Apr 15 - confirm no live campaigns, then notice inside the window                                    |
| Conversation-intelligence tool | mid  | Feb 28 (passed) | 30d    | Yes        | Tolerate  | closed       | none this term - it just renewed; schedule re-score + recertification for Nov, before next window    |
| Dedupe service                 | low  | Dec 15          | 30d    | No         | Invest    | Nov 15       | Oct 1 - renew early only if a multi-year discount is on the table; no urgency, no auto-renew         |

Reading the table: urgency comes from the window column, not the cost column. The cheapest contract can be the most urgent row, and the row whose window already closed (conversation-intelligence) produces a scheduled future action, not a shrug - that scheduling is what converts a one-time audit into a renewal-triggered operating cadence.

## Failure case - the wasted verdict

A portfolio sweep finishes in April and scores the sales-intelligence database Eliminate: solid evidence, duplicate function, clear replacement path. Its contract auto-renewed March 2 with a 90-day notice window that opened the previous December - while the review was being scoped. The verdict is correct and worthless for twelve months, and the spend line the review promised to move doesn't move.

The prevention is structural, not analytical:

- Build the calendar **first** (Workflow step 4 precedes scoring).
- Sort the review's own working order by window-opens date.
- Route every future window into a standing trigger: review fires per tool per window, with the annual synthesis layered on top for portfolio patterns.

## Recertification linkage

Tie each renewal to a recertification pass before auto-renew fires. Confirm three things:

- The named owner still exists.
- The business need still stands.
- Access/integration tokens are still warranted.

An unused tool keeps licenses, admin access, and live tokens long after the need has passed, making a missed renewal a privilege-persistence problem, not only a cost problem. This single linkage is what prevents re-sprawl between cycles instead of re-discovering it at the next audit.
