# Building the seasonal index

Seasonality is a factor built from the org's own closed-won history - never a universal constant copied from a blog. The index exists to stop a specific false alarm: a flat weekly creation target structurally reads "behind plan" in month 1 of every quarter and "ahead" in month 3, triggering pipeline-generation panic when nothing is wrong.

## The sourced shape (a starting hypothesis, not a law)

One forecasting vendor (ORM Technologies) reports this shape across its B2B SaaS customer base - a single-vendor pattern, so validate it against your own multi-year history before trusting it:

- **Across the year:** Q4 > Q2 > Q3 > Q1. Buyer-side "use-it-or-lose-it" budget flush drives the Q4 strength; Q1 stays the weakest stretch year after year.
- **Within any quarter:** month 3 > month 2 > month 1. A Q4-month-3 window compounds both effects.

## Fiscal-calendar variants

The shape follows the _buyers'_ fiscal years, not the calendar:

- A US-federal-heavy customer base surges in August-September, ahead of the September 30 federal year-end.
- UK- and Japan-heavy customer bases surge around March.

Build the index from your own customer mix - a calendar-quarter index applied to a March-fiscal-year customer base misreads its strongest month as an anomaly.

## Build method

1. Pull **4-8 quarters** (roughly two full annual cycles) of closed-won by month.
2. Compute each month's share of its year's total; average across the years to get a monthly index (average month = 1.00).
3. Apply the index to weekly/monthly pipeline-creation targets: target for month _m_ = flat target × index(_m_), shifted earlier by one median sales cycle (pipeline that closes in a strong month must be _created_ a cycle before it).
4. Refresh annually; rebuild when the customer mix shifts (new geography, new vertical, a government segment added).

## Worked example (illustrative arithmetic, not sourced data)

**Input:** two years of closed-won for a calendar-fiscal B2B team, quarterly shares averaging Q1 18%, Q2 26%, Q3 24%, Q4 32% (matching the Q4 > Q2 > Q3 > Q1 shape). A $12M annual new-pipeline-creation plan.

**Output:**

- Quarterly indices: 0.72 / 1.04 / 0.96 / 1.28.
- Q1 creation target: $2.16M (not $3M flat).
- Q4-equivalent creation target: $3.84M, in the window shifted one cycle earlier.

In month 1 of any quarter, the same logic expects roughly a quarter, not a third, of that quarter's closings. A dashboard comparing month-1 actuals to a flat monthly target would flag a ~25% "miss" that the index shows is the normal shape of the year.

## The deliberate buffer is separate

Experienced leaders run coverage above the mathematical minimum (1 ÷ conversion rate) specifically to absorb slippage, competitive losses, and quarter-end push-outs. That buffer is a deliberate management choice layered on top of the formula - additive to the seasonal index, not a substitute for it, and not an error in the formula.
