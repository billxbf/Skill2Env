# Worked Examples

Two complete bidding policies - one B2B, one B2C - and one negative example annotated line by line. Numbers are illustrative; every real policy derives its own.

## Table of Contents

- [Brainstorming example - B2B account, three candidates](#brainstorming-example-b2b-account-three-candidates)
- [Example 1 - B2B SaaS, search platform, lead generation](#example-1-b2b-saas-search-platform-lead-generation)
- [Example 2 - B2C e-commerce, paid social, revenue](#example-2-b2c-e-commerce-paid-social-revenue)
- [Negative example - what not to do](#negative-example-what-not-to-do)

## Brainstorming example - B2B account, three candidates

Example shape, for a B2B account with ~25 conversions/month and no offline imports - candidates listed in efficiency order, best ratio first:

- **(a) Cost-goal at trailing actual.**
  - Buys: cost control at the efficiency the account already achieves.
  - Costs: about an hour of derivation plus a standing review cadence; some volume; variance at this conversion count makes target diagnosis slow.
  - Must be true: the tracked event predicts revenue; the target sits at trailing actual, not the aspirational number.
- **(b) Volume-maximizing, no target.**
  - Buys: maximum signal accumulation, no delivery-choke risk.
  - Costs: near-zero to stand up, but zero cost control - efficiency drifts with the auction.
  - Must be true: budget is genuinely fixed and affordable at worst-case efficiency.
- **(c) Manual/exploratory, time-boxed.**
  - Buys: per-unit control and price discovery on a narrow surface.
  - Costs: a standing weekly job; no conversion-probability adjustment.
  - Must be true: someone owns weekly review; a stop condition and graduation criterion are written down.

The other axes disagree with that order, so state them separately rather than blending them:

- effort: **(c) > (a) > (b)**
- value: **(a) > (c) > (b)**

None of these three sends customer or deal data to a platform, so there is no compliance cost to weigh here. Add that axis the moment a candidate needs value pass-back or a CRM import.

Recommend one, say why, and argue the strongest case against your own recommendation before the user decides. The ordering above is a default, not a law: it shifts with context and with who executes it. Re-rank it against the interview answers, and name which answer moved which candidate:

- a hard deadline promotes (a) and (b) over anything needing new plumbing
- a compounding-asset mandate promotes value-based work despite its setup
- an effort ceiling of a few hours a month deletes (c)
- an in-house analyst who owns weekly review makes (c) far cheaper than it looks
- an existing CRM-to-platform pipeline collapses the effort of anything value-based
- an approval chain that forbids untargeted spend deletes (b) outright

## Example 1 - B2B SaaS, search platform, lead generation

Context from the interview: mid-market SaaS, $12,000 average first-year contract at ~80% contribution margin (≈ $9,600 contribution), 4% lead-to-close, ~70-day sales cycle, ~45 leads/month from the campaign, CRM outcomes not yet imported to the platform, trailing cost per lead $310. Sales flags lead quality as inconsistent.

```
BIDDING POLICY  -  search / B2B lead generation
Objective        : cost efficiency (volume secondary)
Archetype        : cost-goal on the lead event, NOT return-goal.
                   Why: values don't flow back yet, so a return target would optimize
                   noise. Runner-up (volume-maximizing) rejected: budget is affordable
                   only at bounded cost.
Evidence         : event = qualified-lead form submit. Depth check: PARTIAL  -  sales
                   flags quality; offline import of SQL/closed-won is the top action,
                   owned by ops, due before any value-based migration.
                   Volume 45/month. Lag: lead in days; deal in ~70 days.
Target           : $310 cost per lead (= trailing actual).
                   Economics: break-even CPL = $9,600 × 4% = $384. Buffer = $74 (19%).
                   History: trailing 60-day actual $310.
                   Refresh: re-derive close rate from CRM quarterly; next 2026-11.
Evaluation       : 2 conversion cycles ≈ 3 weeks for the lead event.
                   Lead-to-SQL rate reviewed monthly against CRM  -  the platform
                   number alone is not a verdict at this lag.
Change rules     : ±10% per step (practitioner-convergent, not documented), one
                   evaluation window between steps, all pending tracking fixes
                   batched into a single change. Approver: growth lead.
Rollback trigger : spend < 60% of budget for a full evaluation window with impression
                   share lost to rank rising → raise target back to trailing actual.
Switch triggers  : SQL/closed-won imports live with deal values + ≥ the platform's
                   documented value-based minimum (re-verify live) → propose
                   return-goal on the imported deep-funnel event.
                   Lead-to-SQL collapses while CPL holds → event is wrong; stop
                   tightening, fix measurement.
```

Why this is a good policy:

- the archetype is justified _and_ the runner-up is named
- the target starts at actual with the buffer computed and dated
- the known measurement weakness is carried as an explicit action with an owner instead of being ignored
- the switch trigger makes the value-based migration an evidence event, not a calendar event

## Example 2 - B2C e-commerce, paid social, revenue

Context: DTC brand, AOV $95, contribution margin 42% blended but ranging 25-60% across lines, purchase values flow back server-side, ~400 purchases/week account-wide, trailing return 2.9x, goal is profitable scaling.

```
BIDDING POLICY  -  paid social / e-commerce revenue
Objective        : value-return
Archetype        : return-goal on purchase value. Why: real differentiated values
                   flow, volume clears every documented minimum by an order of
                   magnitude. Runner-up (value-maximizing, uncapped) rejected:
                   margin discipline is the stated constraint.
Evidence         : event = purchase, server-side, values net of refunds monthly.
                   Volume ~400/week. Lag < 2 days.
                   Margin variance flag: 25% vs 60% lines under one blended target
                   averages a high-margin and a break-even order into one
                   meaningless number → split policies (or campaign structure) by
                   margin band before tightening.
Target           : 2.9x (= trailing actual).
                   Economics: blended break-even = 1 ÷ 0.42 = 2.4x; with 10% net
                   goal = 1 ÷ 0.32 = 3.1x. Buffer to break-even = 0.5x.
                   History: trailing 30-day actual 2.9x.
                   Refresh: margin re-derived quarterly or on any pricing change.
Evaluation       : 2 conversion cycles ≈ 1 week at this lag.
Change rules     : raise the target ~10% per step toward 3.1x, one window per step;
                   never during a promo window. Approver: head of growth.
Rollback trigger : delivery < 70% of budget for a full window after a tighten →
                   revert one step.
Switch triggers  : a holdout/geo test on retargeting shows near-zero lift →
                   restructure before scaling this policy's budget.
                   Modeled-value share rises materially → widen the buffer.
```

Why this is a good policy:

- it earns the return-goal with evidence rather than defaulting to it
- the blended-margin trap is caught structurally instead of papered over with one average target
- the profit-goal version of the economics sets the tightening destination
- scaling is gated on incrementality, not platform-reported return

## Negative example - what not to do

The launch-meeting version that causes most delivery collapses, annotated:

```
BIDDING POLICY  -  search / lead gen            ← no goal stated anywhere
Archetype        : Target CPA, because that's what we used at my last company
                   ← platform label as reasoning; no archetype logic, no runner-up
Target           : $150  -  that's the CPA we need to hit our plan
                   ← aspirational number. Trailing actual is $310. The bidder will
                     not "work harder"; it will stop bidding. Symptom will be
                     under-delivery with great-looking reported CPA.
                   ← no economics derivation either: break-even was never computed,
                     so nobody can say whether even $310 is affordable.
Evidence         : "we get plenty of conversions"
                   ← unquantified; form-fills unvalidated against sales; a cost
                     target pointed at junk leads optimizes junk efficiently.
Evaluation       : check daily, adjust when CPA looks high
                   ← calendar-days panic loop. Every adjustment restarts learning;
                     the instability it causes will justify the next adjustment.
Change rules     : (none)                     ← unbounded step size, no approver
Rollback trigger : (none)                     ← the collapse has no defined exit
Also proposed    : "auto-pause anything above $300 CPA"
                   ← hardcoded automation rule: with a 70-day lag and thin daily
                     samples, this pauses winners on noise. A spike is a question,
                     not a verdict.
```

The repair path, in order:

1. Quantify volume and lead quality.
2. Derive break-even from deal economics.
3. Set the target at trailing actual ($310).
4. Define the window in conversion cycles.
5. Move toward $150 only if the economics say $150 is affordable; if they do not, escalate it as a unit-economics problem, not a bidding assignment.
