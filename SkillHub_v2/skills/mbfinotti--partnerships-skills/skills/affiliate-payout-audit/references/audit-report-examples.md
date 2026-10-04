# Audit Report Examples

Two worked reports - one B2B SaaS recurring revenue-share, one B2C ecommerce order-level CPA - and one negative example. Program names and figures are illustrative; the structure and the reasoning per finding are the load-bearing parts.

## Worked example 1 - B2B SaaS recurring revenue-share

```
PAYOUT AUDIT - NimbusStack partner program, run 2026-03A, period 2026-02-01..2026-03-01 (UTC, billing-event date)
Scope     : 412 lines, proposed total $48,712.40 USD; sources: platform commission export vs billing-system settled invoices
Structure : 20% recurring rev-share, 12-month cap, marginal tier to 25% above $5,000 referred MRR/month
Checks    : 1 scope frozen: pass | 2 exports pulled: pass | 3 comparability: pass (same event = settled invoice, same window, UTC, USD)
            4 totals: FAIL ($496.70 over) | 5 exceptions: 2 one-sided | 6 dedup: pass | 7 rate/tier: FAIL (2 findings)
            8 lifecycle: FAIL (9 lines in window) | 9 currency/tax: FAIL (1 payee) | 10 sampling: 100% top-5 partners + 40 random
Findings  :
  F-1 | blocker       | $1,912.00 | 9 lines   | Referred trials converted <30 days ago - validation window not elapsed. HOLD lines to run 2026-04A.
  F-2 | material      |   $312.50 | 1 partner | Tier applied retroactively to full volume; structure specifies marginal. CORRECT and re-run.
  F-3 | material      |   $148.20 | 3 lines   | Commission on pre-downgrade MRR; invoices settled at downgraded amount. CORRECT to settled base.
  F-4 | minor         |    $36.00 | 2 lines   | Commission on list price; customers paid discounted invoices. CORRECT to discounted base.
  F-5 | blocker (payee-scoped) | $841.10 | 1 payee | W-8BEN expired 2026-01-31. HOLD this payee's payout until re-collected.
Exceptions: 1 in-platform-not-in-billing ($97, invoice voided post-tracking) - held, over-credit.
            1 in-billing-not-in-platform ($203 invoice, no tracked referral) - untracked; expect partner dispute; credit policy: manual review.
Variance  : recomputed $48,215.70 vs proposed $48,712.40 = $496.70; F-2 $312.50 + F-3 $148.20 + F-4 $36.00 = $496.70. Unexplained $0.00. PASS.
Cleared   : 402 lines, $45,462.60 at corrected values (excludes F-1 held lines and F-5 payee).
Sign-off  : preparer J. Ortiz (partner ops) | checker M. Lund (finance) - roles differ | 2026-03-04 | RELEASE cleared lines only.
```

Why it passes: every line is reconciled or on the exception list, the three corrections account for the gross variance to the cent, and both blockers are resolved by holding - not by releasing with a note.

Note the variance line shows its working: gross difference, the findings that explain it, residual. A residual is either zero or it is a finding with its own line - report 2's F-4 books $3.87 of rounding drift exactly that way. "Unexplained $X, below materiality, PASS" is the habit the negative example below exists to condemn; materiality decides whether a residual blocks release, never whether it gets written down.

## Worked example 2 - B2C ecommerce order-level CPA

```
PAYOUT AUDIT - Alder & Vine affiliate program, run 2026-03B, period 2026-01-01..2026-02-01 (UTC, transaction date; 45-day validation window elapsed)
Scope     : 2,184 lines, proposed total $31,406.18 USD; sources: network transaction export vs order database
Structure : flat 10% of net order value, new-customer only, 45-day validation sized to the apparel return curve
Checks    : 1 pass | 2 pass | 3 comparability: FAIL then normalized (network export was validation-date basis; re-pulled on transaction date)
            4 totals: FAIL ($2,252.14 over) | 5 exceptions: 12 one-sided | 6 dedup: FAIL (2 findings) | 7 rate: pass on sample
            8 lifecycle: FAIL (reversals missing) | 9 currency/tax: pass | 10 sampling: 100% of lines >$100 + top-3 affiliates + 60 random
Findings  :
  F-1 | blocker  | $1,742.30 | 61 order IDs | Same orders in network export AND in-house tracker, both summed into the proposed total.
                                              COLLAPSE to network as canonical source, re-run totals.
  F-2 | material |   $509.84 | 38 lines     | Orders refunded inside the 45-day window but reversals never applied - data came from
                                              a pre-validation export. APPLY reversals.
  F-3 | material | unknown   | 17 lines     | Empty transaction IDs collapsed into one analytics record; per-line value unverifiable.
                                              QUARANTINE; resolve keys manually before release.
  F-4 | minor    |     $3.87 | run-wide     | Per-step rounding drift. RECOMPUTE rounding at the end; below materiality, fix forward.
  F-5 | informational | $148.22 | 4 payees  | Below $50 threshold - verify carry-forward to next run; not payable now, must not vanish.
Exceptions: 12 in-orders-not-in-network (gift-card orders, non-commissionable per terms) - documented, no credit.
Variance  : recomputed $29,154.04 vs proposed $31,406.18; after F-1/F-2 corrections, unexplained $0.00. PASS pending F-3.
Cleared   : 2,106 lines, $28,896.71 at corrected values (excludes F-3 quarantine and F-5 carry-forward).
Sign-off  : preparer R. Okafor (affiliate mgr) | checker T. Devine (controller) | 2026-03-16 | RELEASE cleared lines; F-3 to 2026-04B.
```

Why it passes: the comparability failure was fixed by re-pulling on the declared date basis instead of adjusting numbers by hand, the double-count was collapsed to one canonical source, and the unverifiable quarantine lines were held rather than estimated.

## Negative example - what a bad audit looks like

```
PAYOUT REVIEW - Alder & Vine, March run
Network says 1,904 conversions (7-day window), our tracker says 1,671 (30-day window) -> total 3,575 conversions, looks healthy.
Proposed payout $31,406.18; our own estimate came to $28,500 - difference is only ~$2,900, close enough given tracking noise. APPROVED.
Order #88412 was refunded on Feb 19 but the commission already locked Feb 10, so nothing to do - leaving the line as paid.
Sign-off: affiliate manager (calculated and released).
```

Why every line of it fails:

- **Summing incomparable sources**: the two counts have different attribution windows and dedup identities - they are two claims about overlapping conversions, not additive populations. The comparability gate exists precisely to stop this total from being computed.
- **"Close enough" variance**: $2,900 of unexplained variance is a silent gap, far above any sane materiality threshold, and each dollar in it is either an overpay or an underpay to a real partner. Unexplained variance must be driven to or below materiality line by line, or the run holds.
- **Ignoring the post-lock refund**: locked means "cannot reverse on-platform", not "no longer owed". The refund becomes a forward-period negative adjustment carried against the affiliate's future earnings; dropping it converts a recoverable correction into a permanent overpay.
- **No maker-checker**: the same person calculated and released. There is no independent gate to catch any of the above - which is exactly how all of the above shipped.
