# Rotation runbook

Worked mechanics behind step 4 of the workflow: the runbook itself, the named vendor implementations it copies, and the cadence table.

## The worked runbook (routine rotation, dual-key overlap)

Precondition: storage supports two simultaneously valid keys per identity (an `expires_at` column and no unique-active-key constraint), and last-used telemetry exists. Without both, build them first - this runbook is unexecutable otherwise.

1. **Roll atomically.** One operation creates the new key and sets the old key's expiry (the caller picks the window). Never expose create-new and expire-old as two manual steps - the observed failure is that creation succeeds, expiry scheduling is forgotten, and the key never actually rotates.
2. **Notify the consumer** with the new key (shown once, on the irretrievable rung), the old key's exact expiry timestamp, and a link to this key's last-used telemetry so they can verify their own cutover.
3. **Cut over consumers**: staging first, then production, then agent fleets and queued workloads - the slowest movers, since they pick up config on their own cadence and queued jobs must drain.
4. **Watch old-key traffic until it hits zero.** Last-used telemetry is the signal a migration _completed_, not just started. Fire an expiry-approaching alert if traffic persists near the window's end - extend the window rather than break a live consumer.
5. **Deactivate before deleting.** Disable the old key, wait 24-48 hours as a final safety margin (the AWS-documented step), then delete. Deactivation is reversible; deletion is not.
6. **Log every step** - who initiated, when, grace window chosen, cutover confirmed - as the audit evidence step 7 of the workflow requires.

Two invariants, worth restating because each half-followed version is worse than nothing: never delete before last-used shows zero (that is a rotation-caused outage), and never create a new key without scheduling the old one's revocation (that merely doubles the attack surface).

## Compromise variant

On suspicion or confirmation of compromise, or on employee offboarding, revoke immediately: zero grace, accept the downtime, and running sessions do not get to finish. Then issue the replacement through the routine path. PCI-DSS 4.0 mandates compromise-triggered rotation regardless of whatever cadence policy is in force.

## Named vendor mechanics

- **Stripe**: "Rotating an API key revokes it and generates a replacement key that's ready to use immediately." Rolling in the Dashboard keeps both keys valid for up to 7 days ("This lets you migrate gradually without downtime"). The user picks the expiration from a dropdown; choosing "Now" deletes the old key immediately, and choosing a time shows the remaining countdown under the key's name. Rotation requires two-factor verification. Stripe's documentation describes the dropdown only by these two boundary behaviors and does not itemize preset values anywhere in the text - the intermediate values (1 hour / 24 hours / 3 days, etc.) circulating in third-party guides have no corroboration in Stripe's own documentation; confirming whether a preset list exists in the dropdown itself would require a logged-in Dashboard session.
- **AWS IAM**: each user holds a **maximum of two active access keys** - the hard cap is the design choice that forces old/new overlap instead of N-key sprawl. Documented sequence: create second key → update all consumers → verify via `aws iam get-access-key-last-used` (zero traffic on the old key) → deactivate, not delete → wait 24-48 hours → delete. AWS recommends rotating at least every 90 days - and, better, replacing static keys with IAM roles / temporary STS credentials so there is no long-lived secret to rotate at all.
- **Azure**: dual-key (Key 1 / Key 2, primary/secondary) across many services - structurally the same swap-then-cutover pattern, framed as primary/secondary rather than old/new.

## Grace-period and cadence table

Practitioner conventions, not standards - no universal rotation frequency exists, and risk-based cadence is replacing fixed schedules. Adjust every number against the platform's deploy cadence and risk profile in the interview.

| Scenario                                                | Overlap window / cadence                                                                                                             |
| ------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| Routine scheduled rotation                              | 24 hours to 7 days, by deploy cadence; up to 14 days for large organizations with slow release trains                                |
| Confirmed compromise or offboarding                     | Zero - immediate revocation, accept the downtime                                                                                     |
| Agent-heavy / automated consumers                       | Longer than the human default - fleets pick up config slowly, queues must drain                                                      |
| Production / highest-blast-radius keys (payment, cloud) | 30-90-day rotation baseline                                                                                                          |
| Third-party SaaS integration keys                       | ~90 days                                                                                                                             |
| Service-to-service / database credentials               | ~30 days - or replace with dynamic short-TTL secrets (e.g. 1-hour TTL from a secrets manager) so nothing long-lived exists to rotate |

Compliance note: these figures are convention defaults, not compliance floors - PCI-DSS 4.0 Requirement 8.6.3 requires the cadence to be justified by a documented targeted risk analysis rather than meeting any fixed interval (step 7 of the workflow).

## Why rotate absent a breach

GitGuardian's State of Secrets Sprawl finding: 64% of valid secrets leaked in 2022 were still valid and exploitable years later. An undetected leak is the base case, not the edge case - scheduled rotation is the only control that bounds it.

## Offboarding sequence (ownership tie-in)

1. From the admin view, enumerate every user-owned key the departing person created or could see.
2. Revoke each with zero grace (compromise variant above); rotate any shared or org credential they had access to.
3. Migrate any production integration found running on their personal key to a service-account key - and treat that discovery as a standing process failure, not a one-off.
4. Log every action; the offboarding trail is exactly what a SOC 2 access-review asks for.
