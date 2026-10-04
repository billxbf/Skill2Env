# Lifecycle and Clawback

Every commission record moves through the same generic state machine, whatever the platform calls the states:

```
pending -> approved/validated -> locked -> paid
                 |                  |
                 v                  v
             reversed        (post-lock: forward-period
          (in-window)         negative adjustment)
```

- **Pending**: tracked, not yet payable; fully reversible.
- **Approved/validated**: passed review or the validation window elapsed; on most platforms still reversible until lock.
- **Locked**: no further edits or reversals on-platform; queued for payment.
- **Paid**: money moved; corrections only via negative balance or off-platform recovery.

## How real platforms name and time the gates

Platform documentation; verify against the live program before relying on a number.

| Platform                               | Reversal buffer         | Lock/payment timing                                                                 | After lock/payment                                                                                                                                 |
| -------------------------------------- | ----------------------- | ----------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| impact.com                             | "action locking period" | Default: locks ~27th of the following month, pays ~20th of the month after locking  | "You cannot modify or reverse actions after they lock" - remedy is a make-good transfer                                                            |
| CJ Affiliate                           | "locking cycle"         | Prior-month transactions lock the 10th; custom cycles 7-60 days from post date      | Locked transactions "can no longer be edited or voided"; corrections via full-reversal-plus-new-record restatement                                 |
| Awin                                   | "validation period"     | Auto-validation up to 67 days on the entry tier; average approval 30-45 days        | On the entry tier, "Approved transactions cannot be reversed"; amendments require pending status                                                   |
| PartnerStack                           | 7-day invoice review    | Commissions withdrawable the following month                                        | "Once you have paid out commissions to a partner, under no circumstances can they be taken back"                                                   |
| Rewardful / FirstPromoter / Tapfiliate | "due period" / net-30   | Pending becomes due after ~30 days by default (configurable to the refund policy)   | Refunds auto-apply as negative commissions; a disapproved paid commission drives the balance negative (e.g. -$10) and nets against future earnings |
| Amazon Associates                      | ~30-day return window   | Commission disqualified when "a cancellation, return, or refund has been initiated" | Reserves the right to offset "any excess payment" against subsequent commission income                                                             |

## What releases each transition

- Pending → approved: expiry of the validation window (auto-approval is the common default - unreviewed lines approve themselves) or explicit manual approval.
- Approved → locked: the platform's locking date or cycle.
- Locked → paid: the payment schedule, minimum threshold, and tax-form status.
- The audit checks that no line skipped a state (paid without approved, approved while still inside its window) and that the window length actually matches the program's refund/return policy.

## Reversal triggers by model

- **B2C order-level CPA**: return, chargeback, cancellation, partial refund (amend the sale amount and recompute at the original transaction's rate), non-qualifying coupon.
- **B2B SaaS revenue-share**: trial-to-paid failure, refund, downgrade (reduce the base), mid-period or annual-contract churn, failed payment.
- Reversal rates are the ceiling on payout accuracy. Planning bands from vendor benchmarks (not audited data): 2-8% for CPA, under 3% for revenue-share; some verticals run far hotter - hosting programs have been reported reversing 50-80% of transactions. Above band → lengthen the validation window or tighten qualification before payout.
- Size the window to the reversal curve, not the calendar: high-return verticals (apparel returns run roughly 25%+) need 30+ days; SaaS needs refund policy plus the trial-to-paid window. Geno Prussakov's documented reversal SOP: locking periods sized to the return/cancellation window - "affiliates don't get any certainty on their earnings until that commission locks."

## The post-lock refund problem

- A refund arriving after lock (or after payment) cannot be reversed on-platform on most systems - which is what moves the line out of the correction path and into the remediation ranking in `SKILL.md`.
- Establish three facts before recommending a rung there:
  - Whether the platform carries negative partner balances at all - offset is unavailable where it does not.
  - Whether the published terms authorize reclaiming a paid commission - several platforms in the table above state flatly that they do not.
  - Whether the partner is still earning enough for an offset to land.
- A partner who churns out with a negative balance is an unrecoverable loss - report it as absorbed, never as recovered, and quantify it.
- Reserves/holdbacks (retaining a slice of each payout against future reversals) are the usual form the fix-it-forward rung takes here; note their absence as a program-level observation when post-lock refunds recur.

## Reason codes

- Require a documented reason on every reversal. Prussakov's SOP lists these reason codes, and networks use similar correction-reason lists:
  - invalid card
  - return/cancellation
  - duplicate order
  - customer fraud
  - affiliate fraud
  - non-qualified lead
  - test transaction
- Uncoded reversals are unauditable and fuel partner disputes; flag any reversal without a reason as a finding.
- A reversal coded "affiliate fraud" leaves this skill's scope - escalate to fraud review; the audit only verifies the arithmetic of the reversal.
