# Worked examples

Illustrative cases written for this skill. All figures are example values, not benchmarks - never reuse them as defaults for a real deal.

## Example 1 - B2B mid-market: invoice-automation purchase

Deal frame: 8-person accounts-payable team, mid-market, CFO will review. Artifact: one-page value summary plus light model.

Driver choice: labour time saved plus error/rework reduction. Error/rework normally ranks fifth on efficiency because its cost per error takes a week or more to source. Here the buyer's Q2 ops report already carries both the baseline rate and the cost per error, which is the promotion condition, so it moves up beside labour time.

### Input ledger

| #   | Input                       | Value   | Unit        | Source                                                | Provenance                   |
| --- | --------------------------- | ------- | ----------- | ----------------------------------------------------- | ---------------------------- |
| 1   | Invoices processed          | 4,200   | /month      | Buyer's ops dashboard (champion shared)               | buyer-supplied               |
| 2   | Manual touch time           | 6       | min/invoice | Champion's time study                                 | buyer-supplied               |
| 3   | Error rate requiring rework | 1.8%    | of invoices | Buyer's Q2 ops report                                 | buyer-supplied               |
| 4   | Cost per rework             | $41     | /error      | Buyer's Q2 ops report                                 | buyer-supplied               |
| 5   | AP clerk base salary        | $52,000 | /year       | Champion (HR-confirmed)                               | buyer-supplied               |
| 6   | Fully loaded multiplier     | 1.3x    | ratio       | Standard finance range 1.25-1.35, source named in doc | benchmark                    |
| 7   | Post-automation touch time  | 1       | min/invoice | Rep estimate from other deployments, unconfirmed here | rep-assumed                  |
| 8   | Post-automation error rate  | 0.6%    | of invoices | Rep estimate, unconfirmed                             | rep-assumed                  |
| 9   | Subscription                | $30,000 | /year       | Written quote #Q-1142                                 | quoted (rep-owned cost side) |
| 10  | Implementation (one-time)   | $8,000  | one-time    | Written quote #Q-1142                                 | quoted (rep-owned cost side) |
| 11  | Internal effort             | 120     | hours       | Champion's estimate                                   | buyer-supplied               |

Loaded hourly cost: $52,000 x 1.3 = $67,600/year; / 2,080 h = $32.50/h.

### Arithmetic (expected case)

```
Driver 1: Labour time saved                                  hard
  (6 - 1) min x 4,200/mo x 12 = 252,000 min = 4,200 h/yr
  4,200 h x $32.50 = $136,500 gross
  x 0.65 realization haircut  = $88,725/yr

Driver 2: Error/rework reduction                             hard
  (1.8% - 0.6%) x 50,400 invoices/yr x $41 = $24,797/yr

Soft (separate): capacity freed absorbs invoice growth without a
  9th hire; potential avoidance $67,600/yr - NOT in headline.

Total annual hard value : $113,522
Year-1 investment (TCO) : $30,000 + $8,000 + (120 h x $32.50 = $3,900)
                        = $41,900
Annual net value        : $113,522 - $30,000 = $83,522
ROI (Year 1, net-benefit): (113,522 - 41,900) / 41,900 = 171%
Payback                 : 12 x 41,900 / 113,522 = 4.4 months
```

### Scenarios (conservative first)

| Case         | Changed inputs                                  | Annual hard value             | ROI (Y1) | Payback |
| ------------ | ----------------------------------------------- | ----------------------------- | -------- | ------- |
| Conservative | Time saved 3 min not 5; error rate only to 1.2% | $53,235 + $12,398 = $65,633   | 57%      | 7.7 mo  |
| Expected     | As above                                        | $113,522                      | 171%     | 4.4 mo  |
| Optimistic   | Full 5 min, no haircut; errors to 0.4%          | $136,500 + $28,930 = $165,430 | 295%     | 3.0 mo  |

Sensitivity: the result hinges on inputs 7 and 8 (both rep-assumed). Disclosure line required:

> Headline figures rest in part on rep-assumed inputs (post-automation touch time, post-automation error rate); they have not been confirmed by the buyer. The pilot's first measurement replaces them.

### One-page narrative (condensed)

```
1. HEADLINE: Cutting invoice-cycle cost in support of "Project
   Streamline" (FY close-acceleration initiative).
2. PROBLEM: The 8-person AP team spends 4,200 hours/year on manual
   matching, and 1.8% of 50,400 invoices need $41 rework - a
   ~$137K/yr gross cost by the team's own time study and Q2 ops
   report. Doing nothing for 12 more months costs that again, plus
   a 9th hire as volume grows.
3. APPROACH: Shift from manual three-way matching to
   exception-only review.
4. OUTCOMES: touch time 6 -> 1 min; rework 1.8% -> 0.6%;
   conservative-case value $65,633/yr (math attached).
5. INVESTMENT: $41,900 Year 1 ($30K/yr + $8K setup + 120 internal
   hours). Buyer side: process owner 2 h/wk for 6 weeks, data
   access by [date]. Conservative payback: 7.7 months.
```

Next steps delivered with it: two edit rounds with the champion, written sign-off on inputs 7-8 (or a pilot to measure them), then the forward ask.

## Example 2 - high-ticket B2C: residential solar

Framework mapping to consumer sales is a structural analogy rather than established practice; the regulatory constraints are real law and stricter than B2B norms. State both in the output.

- **Economic buyer** (by analogy): the couple jointly, plus the lender whose financing approval gates the purchase.
- **Champion**: the spouse who requested the quote; the document must convince the skeptical spouse without the salesperson present - same forward test as B2B.
- Ledger discipline unchanged:
  - Last-12-months utility bills $2,760/yr (buyer-supplied - their own bills)
  - Financing payment $148/mo (lender terms - documented)
  - Production offset 85% (installer model - label it vendor-data/rep-assumed until substantiated)
- Conservative case leads: offset 70%, zero utility-price inflation -> monthly savings $161 vs. payment $148 - the case barely clears, and the document says so. Optimistic case (85% offset, 3% utility inflation) is shown, never headlined.
- Regulatory constraints (US):
  - Savings claims must be substantiated (FTC Act Section 5)
  - Financing terms fully disclosed under lending-disclosure law
  - Door-to-door sale carries a 3-business-day cooling-off right
  - State solar-disclosure statutes may add cancellation rights and mandatory disclosure documents

  Present a payback range with disclosed assumptions - never a single "you'll save $X" headline.

- Identical to B2B, explicitly:
  - The ledger
  - The provenance labels
  - No invented numbers
  - Hard/soft separation (comfort and home-value hopes are soft; bill offset is hard)
  - Three cases conservative-first
  - The quality gate

## Example 3 - negative example (what failing the gate looks like)

> "This saves your team 20 hours a week (industry data), so ROI is 400% and it pays for itself in 3 months."

Gate failures:

- No ledger (fails check 1)
- "industry data" unsourced, so the 20 hours is rep-assumed but unlabelled (fails 2)
- Headline rests entirely on it with no disclosure (fails 3)
- No TCO - subscription price only (fails 7)
- Single point estimate (fails 8)
- No narrative, no cost of inaction (fails 9)
- A conveniently clean payback with invisible math (fails 6)

This is exactly the rep-built case buyers discount on sight.
