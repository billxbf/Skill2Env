# Worked reconciliation examples

Two complete examples of the deliverable shape defined in SKILL.md. All figures are illustrative - realistic in shape and direction, not benchmarks.

Do not reuse these numbers as expectations for a real account. Derive every amount from the account's own data.

## Example 1 - B2C/ecommerce, one month

### 1. Headline

Anchor: order system, net revenue basis. Anchor count: **1,240 paid orders, $96,400 net revenue**.

Verdicts:

- Platform A vs orders: structural and explained.
- Analytics vs orders: structural and explained.
- Platform A + Platform B jointly claim 1,590 conversions against 1,240 orders: overlapping claims, not extra orders. Do not sum.

### 2. Normalization basis

- Grain: calendar month, single reporting timezone (the order system's).
- Date basis: order-event date. Platform A raw numbers (interaction-dated) re-pulled with a window wide enough to cover all interaction dates feeding this month's orders.
- Conversion definition: paid order (pending and cancelled excluded), dated definition v2 (in force since the 1st of the prior month).
- Counting rule: Platform A set to "every", order system counts orders - difference carried as a definitional line.
- Windows/models: platform windows as currently configured (read from settings, not assumed), analytics uses its cross-channel model - difference carried as definitional.
- Revenue basis: net revenue excluding tax and shipping, refunds deducted in-month.
- Lag maturity: last 5 days of the month flagged immature for Platform A's window. Estimated open-window share carried as timing.

### 3. Variance table

| Source pair                          | Metric                       | Amount   | % of gross gap | Bucket       | Cause                                                                                                                     | Direction check                         | Evidence                                 | Owner          | Status             |
| ------------------------------------ | ---------------------------- | -------- | -------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------- | --------------------------------------- | ---------------------------------------- | -------------- | ------------------ |
| Platform A (1,468) vs orders (1,240) | conversions                  | +96      | 42%            | Definitional | View-through included by platform                                                                                         | platform high - passes                  | platform data segmented by click/view    | Media buyer    | Documented         |
| same pair                            | conversions                  | +54      | 24%            | Definitional | Modeled conversions included by platform                                                                                  | platform high - passes                  | platform's modeled-conversions breakdown | Media buyer    | Documented         |
| same pair                            | conversions                  | +31      | 14%            | Definitional | "Every" counting: repeat orders on one click                                                                              | platform high - passes                  | 31 multi-order clicks in export join     | Analyst        | Documented         |
| same pair                            | conversions                  | +28      | 12%            | Timing       | Window still open on last 5 days                                                                                          | platform grows later - passes           | prior-month lag curve                    | Analyst        | Re-check next pull |
| same pair                            | conversions                  | +19      | 8%             | **Residual** | Unexplained                                                                                                               | -                                       | dedup event-ID spot-check pending        | Analytics eng. | **Investigate**    |
| Analytics (1,082) vs orders (1,240)  | conversions                  | −103     | 65%            | Definitional | Consent + ad-blocker loss at expected baseline                                                                            | analytics low - passes                  | consent-rate data                        | Analyst        | Documented         |
| same pair                            | conversions                  | −38      | 24%            | Definitional | Cross-device journey breaks                                                                                               | analytics low - passes                  | new-user rate by browser                 | Analytics eng. | Documented         |
| same pair                            | conversions                  | −17      | 11%            | **Residual** | Channel-level only: "direct" share up 4 pts, total intact - suspect stripped parameters / AI-referral no-referrer traffic | mix shift, no total change - consistent | direct-share trend                       | Analyst        | Monitor            |
| Orders, revenue                      | gross $109,900 → net $96,400 | −$13,500 | n/a            | Definitional | Tax + shipping + discounts + $2,900 refunds                                                                               | gross high - passes                     | order-system finance data                | Finance        | Documented         |

### 4. Residual statement

- Platform A vs orders: gross gap 228 conversions, explained 209 (92%), residual 19 (8%). Stable vs prior month (7%), same direction. **Passes** the ≥ 80% threshold and the judgment test, with the residual documented and the event-ID spot-check queued.
- Analytics vs orders: gross gap 158 conversions, explained 141 (89%), residual 17 (11%), confined to channel mix. **Passes**, with monitoring on direct share.

### 5. Defects and handoffs

None confirmed this period. If the event-ID spot-check finds unshared IDs between browser and server purchase events, open a defect (double-counting, platform high) and hand off to `mbfinotti/advertising-skills@ad-conversion-tracking`.

### 6. Known deltas to carry forward

Known deltas, re-derive each period rather than subtracting as a fixed correction:

- Platform A ≈ +14–19% vs orders, from view-through + modeled + counting rule.
- Analytics ≈ −11% vs orders, from consent and cross-device loss.
- Revenue: net = gross − ~12% (tax/shipping/discounts/refunds).

## Example 2 - B2B, one quarter cohort

### 1. Headline

Anchor: CRM. Cohort: **leads created in Q1** (not deals closed in Q1 - close-date pulls mix cohorts the platforms saw months apart). Anchor count: **412 leads, 47 closed-won, $588,000 closed revenue**.

Verdict: platform vs CRM - structural and explained after the offline-import match rate is accounted for. One capture defect found.

### 2. Normalization basis

- Cohort basis: lead creation date. Closed-won revenue followed to close regardless of close date.
- Conversion definition: CRM-accepted lead (spam and duplicates removed), dated definition.
- Bridge: offline conversion import keyed on the platform click ID stored on the lead, import lag ≈ weekly batch.
- Volume caveat: small denominators - absolute units reported alongside every percentage.

### 3. Variance table

| Source pair                        | Metric  | Amount      | % of gross gap | Bucket                | Cause                                                           | Direction check                    | Evidence                                                      | Owner         | Status                         |
| ---------------------------------- | ------- | ----------- | -------------- | --------------------- | --------------------------------------------------------------- | ---------------------------------- | ------------------------------------------------------------- | ------------- | ------------------------------ |
| Platform (341 leads) vs CRM (412)  | leads   | −44         | 62%            | Definitional          | Click-ID match rate 78% - unmatched leads invisible to platform | platform low - passes              | import logs: 89 unmatched, 44 net of overlap with lines below | RevOps        | Documented                     |
| same pair                          | leads   | −18         | 25%            | Timing                | Weekly import batch lag at quarter edge                         | platform low, lands later - passes | import timestamps                                             | RevOps        | Re-check                       |
| same pair                          | leads   | −9          | 13%            | **Residual → Defect** | Click ID not saved on one landing-page form variant             | platform low - passes              | form audit: hidden field missing on variant C                 | Marketing ops | **Handoff**                    |
| Platform closed-value vs CRM $588k | revenue | −$96k       | 100%           | Timing                | 8 deals closed after the platform's import-acceptance window    | platform low - passes              | close dates vs documented window                              | Analyst       | Documented as structural floor |
| Contact vs account view            | credit  | 12 accounts | n/a            | Definitional          | Form-filler credited instead of buying group                    | n/a                                | account rollup                                                | RevOps        | Documented                     |

### 4. Residual statement

Platform vs CRM leads: gross gap 71, explained 62 (87%) as definitional plus timing, residual 9 (13%). The residual did not resist classification, though: the form audit attributed it to a missing hidden field, converting it to a **defect**, not an accepted residual. Post-fix, expect the match rate to recover toward the 75–85% practitioner range from its variant-C-weighted low.

### 5. Defects and handoffs

Ranked by revenue at stake per unit of fix effort, with the adjustment shown:

| #   | Defect                                                                 | Revenue at stake                                            | Fix effort                                                                         | Position after adjustment                                                                                      |
| --- | ---------------------------------------------------------------------- | ----------------------------------------------------------- | ---------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| 1   | Missing click-ID capture on form variant C                             | est. −$27k pipeline/quarter at cohort close rate (−9 leads) | an hour: restore the hidden field on one form variant, fully reversible, one owner | first - smaller number than the import-window floor below, but the only one that is actually fixable this week |
| -   | Closed revenue falling outside the platform's import-acceptance window | −$96k/quarter                                               | not a defect: structural floor, no fix at any effort                               | excluded from the ranking, carried forward as a known delta                                                    |

Defect 1 owner: marketing ops. Hand off to `mbfinotti/advertising-skills@ad-conversion-tracking`. Annotate the history at fix date - the post-fix step-up is a discontinuity, not organic lift.

### 6. Known deltas to carry forward

Known deltas, re-derive both each quarter:

- Platform structurally under-reports closed revenue by whatever share of deals closes after its import-acceptance window (this cohort: $96k, 16%).
- Platform lead counts ≈ −20% vs CRM at current match rate.

## Negative example - what not to ship

> "Platform reported 1,468, orders show 1,240. After adjustments the numbers reconcile exactly to 1,240. Gap: 0%."

This is the bank-reconciliation instinct misapplied. An attribution reconciliation that ties to zero has hidden or invented at least one adjustment - there is always a residual, because consent loss, modeling, and identity gaps cannot be enumerated to the last unit. Ship the explained share and the residual, with the judgment-test verdict, instead of a tie-out.
