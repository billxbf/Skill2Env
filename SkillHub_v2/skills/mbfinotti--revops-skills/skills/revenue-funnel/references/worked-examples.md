# Worked Examples

Three shapes of the engagement: a mid-touch B2B design showing the candidate-comparison step, a PLG design showing the unit switch, and one design done wrong. Structures and figures follow the sourced tables in the other references; per-company numbers below are illustrative placeholders to show the artifact shape, and a real engagement derives them from the user's own history.

## Example 1: Mid-Touch Series B SaaS (candidate comparison)

Interview findings:

- SDR-to-AE motion
- Subscription revenue
- 2-3 stakeholders per deal
- ~20% of new ARR from existing customers
- 6 quarters of CRM history
- Planning is the primary purpose
- Hard deadline at the annual plan

Prior decisions settled:

- Model: planning
- Unit: lead, switching to opportunity at qualification
- Boundary: commit for finance, plus time-to-first-value tracked separately

Candidates presented:

- **A. Compressed 5-stage (2012 Demand Waterfall vocabulary):** Inquiry -> Marketing-Qualified -> Sales-Qualified -> Opportunity Validated -> Commit. Optimizes for clean planning math on thin data; lowest admin cost. Post-sale left to a renewal date field.
- **B. 6-stage with post-sale skeleton (Bowtie-leaning):** adds Onboarded/Adopting after Commit. Optimizes for the expansion share the company expects to grow; costs product-telemetry instrumentation it does not have yet.
- **C. 7-stage buying-group model (Demand Unit vocabulary):** qualification at the account level. Rejected in the write-up, not just demoted: at 2-3 stakeholders per deal the migration cost buys little (below the 3-4 threshold).

Recommendation: A now, with B's post-sale stages as the register's first trigger-based extension once expansion share or telemetry justifies them. The deadline promoted the low-admin candidate; the compounding mandate got a scheduled upgrade path instead of being silently dropped.

Register excerpt (shape, not gospel):

```
transition          rate   basis    n      source                 refresh trigger
MQL -> SQL          22%    cohort   1,840  own data, 6 quarters   quarterly council
SQL -> Opp          48%    cohort     405  own data, 6 quarters   quarterly council
Opp -> Won          24%    cohort     194  own data, 6 quarters   quarterly council
close-rate lag      55/30/15% in/1st/2nd quarter, 6 cohorts       monthly recompute
```

Bottom-up plan from these rates landed 8% short of the top-down target; the gap was named in the funnel model with two closure options (MQL volume vs SQL-to-Opp improvement), not averaged away.

## Example 2: PLG Moving Sales-Assisted

Interview findings:

- No-touch self-serve core
- A new sales-assist motion for teams
- Usage-based pricing
- Thousands of signups monthly

Design: two connected constructs, not one funnel. Self-serve side measured with cohort/event analytics (signup -> activation -> paid conversion), no per-deal stage state. From the product-qualified gate onward, a 4-stage pipeline at the _account_ unit: PQA identified -> Sales-assist engaged -> Commit -> Ramp-to-steady-state (usage revenue makes the post-commit ramp a first-class stage with its own conversion and time metrics).

PQLs bucketed three ways, hand-raisers routed first. The written model states explicitly where the unit switches from user to account and which side of the gate each metric lives on.

## Example 3: Done Wrong (negative example)

A seed-stage company shipped a 10-stage pipeline copied from an enterprise template, stage probabilities left at CRM defaults, one blended "conversion rate" reported weekly, and an SLA that obligated only sales.

What failed, mapped to the rules it broke:

- Ten stages at pre-PMF is premature complexity - half the stages saw no operational use, and reps parked deals in stage 2 until close, corrupting every rate.
- CRM default probabilities are deleted-menu items: nobody derived them from this business, and multiplied against optimistic deal values the error compounded exactly in the middle stages where most pipeline sat.
- The blended weekly "conversion rate" mixed a period win rate with a cohort close rate depending on who pulled it - the same business read three different numbers in one leadership meeting, and no register existed to say which basis was which.
- The one-sided SLA made marketing the defendant and sales the judge; it was ignored within a quarter because nothing enforced it and no consequence was documented.

The fix followed this skill's workflow: purpose and unit settled first, stage count cut to 4 with guesses labeled as guesses, a register with basis and provenance columns, and the SLA rebuilt bilaterally with a paper-mapping session as the first step.
