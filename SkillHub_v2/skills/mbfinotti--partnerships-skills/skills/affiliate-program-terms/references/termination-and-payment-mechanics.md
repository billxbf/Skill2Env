# Termination & Payment Mechanics

The lifecycle and exit clauses generate more disputes than any other part of the agreement. If the terms do not explicitly address what happens to earned commissions at termination, expect a dispute every time - including small-claims filings over tiny balances.

## The commission lifecycle

Draft the pipeline explicitly, stage by stage:

```
referred transaction → PENDING commission
  → validation / locking window (merchant approves, declines, or reverses)
  → CLEARED → held until minimum payout threshold met
  → PAID → still reversible inside the clawback window
```

- Set a validation/locking window during which each commission can be approved, declined, or reversed. Real network reference points: a 75-day validation period at one major network; fixed monthly locking dates at another.
- Set the clawback window knowing it cannot fully cover chargeback exposure. 120 days from the transaction is the standard Visa/Mastercard filing limit. Services-not-received, delayed-delivery and not-as-described codes instead run 120 days from the _expected delivery date_, capped at **540 days** from the transaction - so an annual subscription disputed in month 14 is still in play.
- The common SaaS range is 30–90 days, chosen for affiliate trust rather than full coverage; carry the uncovered tail in the reserve and negative-balance clauses below, not by stretching the window. A 30–60 day hold on an affiliate's first commissions is a recognized defensive pattern.
- Enumerate reversal grounds narrowly: fraud, product returns, order cancellations, chargebacks, statutory consumer withdrawal. Avoid open-ended "at our discretion" reversals - unexplained reversals are the top affiliate complaint.
- State the minimum payout threshold, payment method, and schedule; unpaid sub-threshold balances roll forward, they are not forfeited.

Window lengths are deliberately unranked here. Validation, clawback and first-commission-hold durations are commission mechanics decided by the commission-structure skill, and a duration on a continuum has no menu to order - putting 30 days ahead of 90 would be precision this skill cannot carry. The terms cite whatever was decided.

## Chargeback reserve and negative balances

Because the clawback window closes long before chargeback exposure does, protection has to keep working after it expires.

**Clawback authority is the gate, not a ranked option.** Draft it wherever commissions are paid before the transaction is chargeback-safe: an express right to reverse a paid commission when the underlying transaction is refunded, cancelled, charged back, or found fraudulent, tied to the enumerated grounds above and never to open discretion. Without it there is no reversal right to collect on, so nothing below it matters.

The two controls that make that right collectable are a real choice, ranked by what each recovers per unit of drafting, ongoing reconciliation and affiliate goodwill:

- efficiency: negative-balance carry-forward > chargeback reserve
- effort: chargeback reserve (a week to set the share, the release schedule, the rate threshold and the termination treatment, then a standing job reconciling releases, plus a recruiting conversation with every affiliate who reads the clause) > negative-balance carry-forward (near-zero - one sentence, self-executing against future payouts)
- value: chargeback reserve (cash actually held against the long tail, and the only thing collectable from an affiliate who stops earning) > negative-balance carry-forward (collects only from affiliates who keep earning, which is most of them but not the ones who leave after a bad month)
- compliance cost: chargeback reserve (withheld money is an earned-but-unpaid commission, so it inherits the escheatment question and needs its termination treatment cleared before publication; releasing it late is the next dispute) > negative-balance carry-forward (an offset against future earnings, cleared once)

Lead with the carry-forward: it costs a sentence and covers every affiliate still active, which is where most reversals land. The reserve is what this order starves - top of the value axis, bottom of the ratio.

Promote it when:

- Affiliates are paid before the chargeback tail closes and a material share churn out of the program after being paid.
- The product's chargeback rate is already known to be high.
- The sibling fraud skill's audit flags the uncovered tail as a blocking finding.

Delete it where every commission clears only after the merchant's own refund window closes: there is no tail to reserve against, and withheld money costs recruiting for nothing.

Drafting the reserve: withhold a stated share of commissions (10–15% is the common band), released on a stated schedule (quarterly is typical) while the affiliate's chargeback rate stays below a named threshold. State the percentage, the release schedule, the threshold, and - explicitly - whether the reserve survives termination and for how long, or it becomes the next dispute. `[LEGAL REVIEW]`

## Termination

- **For convenience**: at-will termination by either party is near-universal; 30 days' notice is typical. EU/UK business users require 30 days plus a statement of reasons wherever P2B applies - workflow step 7 layers that jurisdiction overlay and settles the in-scope question.
- **For cause**: immediate, tied to material breach - which is why the prohibited-tactics clause must deem violations material breaches.
- **Survival**: keep confidentiality (commonly multi-year), indemnity, IP restrictions, and payment/clawback mechanics alive after termination; list survived clauses by name.

## Pending commissions at termination

The single most commonly omitted clause. Draft the split explicitly:

- Non-fraud termination (convenience, program shutdown, quality): pay all validly earned commissions accrued to the termination date, on the normal schedule, still subject to the validation window.
- Fraud/for-cause termination: forfeit commissions attributable to the violation; state whether unrelated earned commissions are still paid. `[LEGAL REVIEW]`
- Blanket forfeiture of all earned commissions on any termination is legally contested and sits in tension with US state escheatment law (unpaid commissions can be reportable to the state after a 1–5 year dormancy period). Prefer narrow reversals; take counsel advice before any forfeiture broader than fraud. `[LEGAL REVIEW]`

## Dormancy and small balances

- Dormancy forfeiture clauses exist in the wild (e.g. full-balance forfeiture after 180 consecutive days of inactivity at one large publisher program) but collide with the same escheatment concern.
- If the user wants one: require prior notice to the affiliate, a reactivation path, and counsel review. `[LEGAL REVIEW]`

## Brand-licence revocation

- Revoke the trademark/creative licence automatically on any termination - no separate notice step.
- Require destruction or removal of brand assets within a short fixed window (~5 business days) and cessation of all use in domains, handles, and ads.

## Amendment

- Notify changes by electronic means (email or in-dashboard).
- Continued participation after the notice period constitutes acceptance.
- The affiliate's alternative is termination.
- EU/UK business users: at least 15 days' notice on a durable medium, never retroactive, with an explicit right to terminate before the change takes effect. Non-compliant amendment clauses are null and void there.
- Version the document: dated versions and a change record - frequent amendment is normal in this genre, silent amendment is the failure mode.
