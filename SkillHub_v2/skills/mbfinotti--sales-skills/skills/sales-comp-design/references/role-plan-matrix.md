# Role-plan matrix

One plan per role shape - never one plan stretched across roles with different influence over the sale. Pay mixes below are published-benchmark ranges to _calibrate_ an influence-derived mix, not to copy (see SKILL.md step 3).

## The matrix

| Role                    | Typical pay mix (base/variable) | Paid measures (max 3)                                    | Core mechanics                                                       | Crediting                                  |
| ----------------------- | ------------------------------- | -------------------------------------------------------- | -------------------------------------------------------------------- | ------------------------------------------ |
| SDR (inbound)           | 65/35 to 70/30                  | Qualified opportunities (focus); held meetings secondary | Shorter ramp than AE; SPIF-prone; monthly/quarterly payout           | Sourced-credit to SDR on closed-won kicker |
| BDR (outbound)          | 55/45 to 60/40                  | Qualified opportunities; sourced pipeline                | Higher variable than inbound - the rep creates the opportunity       | Same as SDR                                |
| AE (SMB/velocity)       | 50/50 to 60/40                  | New ARR (focus)                                          | Accelerator curve; shorter ramp                                      | Standard single credit                     |
| AE (mid-market)         | 50/50 to 55/45                  | New ARR (focus); optional strategic mix measure          | Accelerator curve                                                    | Standard single credit                     |
| AE (enterprise)         | 55/45 to 60/40                  | New ARR (focus)                                          | Windfall clause matters most here; longest ramp                      | Split rules for multi-territory deals      |
| First-line manager      | ~60/40                          | Team attainment (focus); MBOs allowed                    | Collective or individual override; over-assigned team quota          | Rollup, no individual deal credit          |
| SE / overlay specialist | 70/30 to 85/15                  | Supported team's product quota                           | 70-80% of variable on the supported team, 20-30% on the broader team | **Double credit** with the primary rep     |
| AM (expansion)          | 60/40 to 65/35                  | NRR/expansion (focus); GRR gate                          | GRR floor gates expansion pay                                        | Credit on expansion, not renewal-only      |
| CSM (retention)         | 70/30 to 80/20                  | GRR (focus); NRR bonus tier                              | Never paid on new-logo bookings                                      | Book-of-business, not per-deal             |

## SDR/BDR design notes

- Pay on **qualified opportunities or held/accepted meetings, never booked meetings** - pay-on-booking pays for spam and pollutes the AE pipeline with meetings booked to trigger the payout. A hybrid weighting more on qualified opportunities than on appointments is a recommended middle ground (OpenView: 40% appointments / 60% qualified opportunities).
- A sourced-pipeline variant (used by roughly a third of SaaS startups) requires the SDR to source ~10x-15x their own OTE in pipeline instead of counting SQLs.
- SDR turnover is structurally high (Bridge Group: median annual turnover 32-40%, median tenure 14-18 months) - a direct reason SDR plans carry a higher, more predictable base share than AE plans, and why SDR ramp (2-3 months) is much shorter than AE ramp.
- AI-driven prospecting automation is compressing the raw-activity side of the role; comp design is shifting further toward qualified-opportunity quality gates - reinforcing, not changing, the pay-on-qualified rule.

## Manager design notes

- **Collective override:** manager paid on aggregate team attainment (a share of team revenue, gated on team quota).
- **Individual override:** a small share of each rep's own payout summed upward.

Collective is simpler and keeps the manager coaching the whole team.

- Team quota rollup includes deliberate over-assignment - the sum of rep quotas exceeds the manager's number, buffering expected attrition and misses.
- Manager plans are the standing exception to the anti-MBO rule: a manager's job genuinely includes non-output responsibilities.

## Overlay design notes

- The dominant crediting rule is **double credit** - both the primary rep and the specialist credited fully. The simpler "no overlays, no double credit" preference (Alexander Group's stated default) concedes that technical selling genuinely requires specialists, for whom double credit is the accepted answer.
- Tie overlay quota to the supported team's product quota; weighting most of the overlay's variable there and the remainder on the broader team keeps the specialist coordinating rather than optimizing a narrow assignment.

## CSM/AM design notes

- Keep **GRR and NRR as two separate paid metrics** - a single blended number lets one large expansion mask real churn elsewhere in the same book. A GRR floor (e.g. 90%) gates whether expansion pay releases at all.
- One cited weighting bridges the two: 75% of incentive weight on churn mitigation, 25% on expansion.
- Rollout practice: track NRR/GRR per individual for two full quarters with no variable attached to establish an honest baseline, then set targets as a 5-10% improvement over it.

## Hunter/farmer crediting

When the org splits new-logo from expansion ownership (the split decision is mbfinotti/sales-skills@sales-org-structure's): cap the hunter's credited tail - commonly 12 months - so the hunter neither loses in-flight credit nor slow-rolls the handover, and run the farmer base-heavy on retention/expansion. Expect the hunter side's turnover to run structurally higher; that asymmetry is a comp-cost input, not a management failure.

## Draws and ramp

- **Non-recoverable draw** (an advance not repaid from later commission) is the standard ramp-support mechanic - it cuts early-tenure anxiety and attrition without changing post-ramp expectations. Recoverable draws create negative-balance disputes at separation.
- The ramp-relief _quota_ schedule beside the draw belongs to mbfinotti/sales-skills@sales-quota-setting.
- Written multi-rep split rules before any deal closes; territory and named-account crediting disputes are a leading source of plan exceptions.

## Benchmark citations (calibration only - never design targets)

US B2B SaaS reference points, all secondary-relayed survey data; verify currency before quoting in a deliverable:

- Bridge Group 2026 AE data: median OTE $200K, median quota $960K, a 4.6x quota:OTE ratio.
- Bridge Group 2025 SDR data: median OTE $80K ($55K base / $25K variable, ~69/31).
- Bridge Group 2024 AE edition: median OTE $190K at 53:47, commission ~11.5% of ACV at quota.
- Quota:OTE band: 4x-6x with 5x as the steady-state default; SMB/inbound-heavy 3x-4x, enterprise 5x+ (SaaStr, ICONIQ, multiple vendor surveys).
- Role OTE ranges (Bridge Group, RepVue, WorldatWork, various):
  - SDR: ~$76K-80K.
  - SMB AE: $140K-200K.
  - Mid-market AE: $180K-250K.
  - Enterprise AE: $240K-320K.
  - First-line manager: $200K-280K OTE at 60/40.
  - CSM: ~$140K OTE at ~75/25.
  - SE: median ~$175K at 70/30, with an AE:SE support ratio around 1.44:1.
- SDR component economics (ICONIQ, vendor sources):
  - Per-qualified-meeting bonuses: $20-50.
  - Per-accepted-opportunity: $100-250.
  - Closed-won kickers: 1-3% of SDR-sourced revenue.
  - Enterprise SDRs book ~5 SQLs/month vs ~20 for mid-market.
- Europe/Canada comp runs roughly 20% below equivalent US roles (ICONIQ) - a benchmarking adjustment, not a legal one.
- Attainment equilibrium (Bridge Group): the classic well-calibrated norm was roughly two-thirds of reps hitting quota, with a healthy full distribution of:
  - ~60% of reps at 50-100% attainment.
  - ~15% above 100%.
  - ~25% below 50%.

  Attainment has structurally declined since 2022: re-baseline against current data via mbfinotti/sales-skills@sales-quota-setting before grading a plan on the folk figure.

Commission-heavy B2C reference points (directional, uneven trade-source rigor):

- **Insurance:** commissions 10-20% of first-year P&C premium plus 2-15% renewals.
- **Solar:** 5-20% or flat per-sale/per-kW, heavy draw usage.
- **Auto:** ~20-25% of front-end gross plus back-end products and manufacturer SPIFFs.
- **Real estate:** income spread is extreme by tenure (NAR 2026: newest agents' median income is a small fraction of 16+-year agents').

Insurance three-year turnover ~89% and auto annual turnover 40-70% are the attrition figures behind the B2C design warnings in SKILL.md.
