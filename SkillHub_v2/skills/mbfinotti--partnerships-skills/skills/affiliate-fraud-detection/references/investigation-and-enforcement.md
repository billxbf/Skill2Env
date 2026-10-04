# Investigation and Enforcement

The operating procedure attached to every delivered rule set: cadence, evidence, escalation, money mechanics, due process.

## Monitoring cadence

- Daily: tracking health (pixel/postback fires, reconciliation jobs, alert backlog); new-affiliate application review.
- Weekly: anomaly triage against baselines; randomized spot-check of 10-15 affiliate campaigns; fraud summary to the affiliate team.
- Monthly/quarterly: performance audit, risk-profile refresh, denied-affiliate and reversed-commission report for finance.

## The audit loop

1. Baseline 90 days of per-affiliate conversion-rate, timing, and chargeback/refund data.
2. Watchlist outliers (2 SD from program norms - agency workflow, tune to taste).
3. Cross-reference watchlisted affiliates against IP, device-fingerprint, and geo checks - under a stated lawful basis and retention period, never ad hoc. These are personal-data processing operations, and fingerprinting in particular may require consent even outside advertising under the UK regulator's published position. Route the design to counsel before first use. `[LEGAL REVIEW]`
4. Decide the band per SKILL.md § Output Shape, which defaults to Hold & Investigate and states what moves a case up or down.
5. Feed confirmed cases back into the rules; retire rules that only ever produce false positives.

## Evidence collection

Every enforcement action stands on reproducible evidence, collected before the affiliate is contacted:

- Cookie-drop reproduction: clean browser, visit the suspect property, record whether an affiliate cookie is set without a click.
- Redirect-chain capture with timestamps; tracking URLs and ad copy.
- Timestamped screenshots of ads, landing pages, and branded SERPs (multiple geos for brand-bidding cases).
- Server-log review for hidden iframe loads and referrer patterns; signed (HMAC) postback records.
- Test purchases where warranted; CRM outcome export for B2B lead cases.

Maintain the audit trail from first flag - network compliance teams and courts act on evidence dossiers, not suspicions.

## Escalation ladder

Who owns each band and how fast they move. Rows run in the same efficiency order as SKILL.md's Output Shape, which carries the triggers, costs and default assignment; the tier number is the ladder position, not the priority.

| Band                        | Owner                                                                | Timeline                                            |
| --------------------------- | -------------------------------------------------------------------- | --------------------------------------------------- |
| Hold & Investigate (tier 2) | Cross-functional review (affiliate manager + finance; legal on call) | Within 24-48h; commissions throttled to zero        |
| Watch (tier 1)              | Affiliate ops analyst                                                | Weekly triage                                       |
| Suspend & Escalate (tier 3) | Program owner + legal                                                | Immediate suspension; dossier to network compliance |

Enforcement ladder within Tier 3, run in order:

1. Suspend.
2. Reverse/void violation-period commissions.
3. Clawback paid amounts.
4. Terminate.
5. Network report.
6. Legal: wire-fraud referral, FTC reportfraud.ftc.gov / FBI ic3.gov for significant cases.

Severity is proportionate: a missing disclosure is a warning; deliberate trademark hijacking or stuffing with technical evidence is Tier 3. In-house staff are empirically better at borderline judgment calls, outside specialists at clear violations (Edelman & Brandi, _JMR_ 2015) - keep judgment calls in-house even when tooling is outsourced.

## Money mechanics - the part that actually protects the program

Implementation detail for three of the four controls ranked in SKILL.md § Control Leverage; the rows below run in that same order.

- **Validation/hold window**: 30-90 days before a commission locks - subscription and high-chargeback verticals at the long end.
- **New/high-risk partners**: longer payout terms (net-60/net-90) and stricter application filters until a track record exists.
- **The chargeback trap**: two filing-limit clocks apply, and the second one outlasts any realistic hold window.
  - Standard Visa/Mastercard filing limit: 120 days from the transaction.
  - Services-not-received, delayed-delivery and not-as-described codes: 120 days from the expected delivery date, capped at 540 days from the transaction - an annual subscription disputed in month 14 is still in play.

  Cover the gap contractually or accept the loss: clawback authority, negative-balance carry-forward (deduct from future payouts until offset), and a chargeback reserve (10-15% of commissions held, released quarterly while the chargeback rate stays below threshold). These clauses belong in the program terms - flag their absence before tuning any rule.

## Due process and communication

- Appeals: a published dispute path, roughly a 14-day window, evidence submitted in writing, reviewed by someone who is not the detecting analyst. Licensed verticals treat this as a regulator expectation; everywhere it doubles as a false-positive control.
- External communication stays neutral and factual - "your commissions are under review pending a routine quality check; expect an update by <date>". Never use the word "fraud" with the flagged partner. Internal documentation carries the real reasoning and the evidence.
- A useful behavioral tell during review: legitimate partners accept rejection reports and self-correct; fraudsters argue (vendor observation, not a rule - never enforce on it alone).

## Network and platform escalation

Networks earn a percentage of commission volume: their compliance teams are reactive, acting on evidence-backed complaints, and run cross-client blacklists rather than per-brand surveillance. Send the dossier (publisher ID, evidence artifacts, timestamps, financial exposure); request suspension and cross-program flagging. Expect nothing unprompted.
