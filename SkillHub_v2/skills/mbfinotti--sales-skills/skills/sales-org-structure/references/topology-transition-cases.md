# Topology transition cases and capacity math

Three worked cases, each built from the triggers and benchmarks this skill's other reference file (`ratio-span-benchmarks.md`, linked from SKILL.md) documents in full. The figures are illustrative applications of sourced medians and thresholds - replace them with the org's own numbers before deciding anything.

## Case 1 - Island to Assembly Line at 8 reps

**Situation:** ~$8M ARR B2B SaaS, 6 full-cycle AEs plus 2 founders still closing, ~$25K ACV, mixed inbound/outbound. AEs report 6 hours/week self-prospecting; calendar audit puts actual selling time near 25% of the week.

**Trigger check:** both SDR-split triggers have fired (self-prospecting > ~4 h/week, selling time < ~30%). ACV is well above the ~$4K floor, and AE calendars are not full - no blocker deletes the move.

**Ratio derivation (never copy a benchmark):**

1. Each AE needs ~4 new qualified opportunities/month to sustain quota (from the org's own win rate and deal size - here 6 AEs × 4 = 24 SQLs/month needed).
2. Inbound plus marketing already source about half (12 SQLs/month). Bridge Group's median context: 74% of AE pipeline comes from marketing, inbound SDRs and outbound SDRs combined - the AE self-sourcing share is the minority everywhere.
3. Remaining 12 SQLs/month ÷ 6 SQLs per SDR per month (Bridge Group 2025 global median) = **2 SDRs**, a 1:3 ratio.
4. Sanity check: 1:3 sits at the thin edge of the mixed-SaaS band (1:2-1:2.5) and inside the enterprise-inbound band (1:3-1:4) - plausible for a half-inbound motion. Had inbound been near zero, the same math yields 4 SDRs (1:1.5), inside the SMB/outbound band. The inbound share, not a published headline, is what moves the answer.

**Transition plan:**

1. Hire 2 SDRs over one quarter.
2. Write the SDR→AE handoff definition (what "qualified" means, in fields) _before_ the first SDR starts. The handoff is the highest-loss point an assembly line creates.
3. Add the first SDR manager only at ~6 SDRs, not at 2.

**Negative variant (what not to do):** the same company at 4 AEs and $3.5K ACV hires 2 SDRs because a board member's other company has them. Below ~10 reps that is "just overhead and handoff friction," and below ~$4K ACV the deal value cannot fund the role - the correct design was no move.

## Case 2 - The hunter/farmer decision at 25 AEs

**Situation:** ~$40M ARR, 25 AEs who own their accounts post-sale, expansion now ~30% of new revenue and visibly under-worked - AEs chase new logos because that is what their comp accelerates.

**Trigger check:** at ~25 AEs the Lemkin/Queener threshold is met; expansion revenue is material. At maturity only ~26-27% of companies still leave expansion with the AE - the split is the norm this org is late to, not an exotic move.

**Design:**

- Stand up an AM/CS-owned expansion role.
- Cap the hunter's credited tail at 12 months so AEs neither lose in-flight credit nor slow-roll handovers.
- Pay the farmer base-heavy on retention/expansion (mechanics → sales-comp-design).

Expect the attrition profiles to diverge by design: the hunter side carries structurally higher turnover than the farmer side, independent of management quality - budget backfill accordingly.

**Negative variant:** the same split attempted at 8 AEs forces arbitrary quota-credit rules, and reps slow-roll expansion conversations to stay inside their credited window - the split manufactures the behavior it was meant to fix. Below the threshold, delete the move rather than shrink it.

## Case 3 - Assembly Line to hybrid with an enterprise pod at ~30 reps

**Situation:** ~$60M ARR, assembly line running well for mid-market, now selling a genuine enterprise tier: 6-12-month cycles, buying committees of 11-20+ stakeholders, and a mid-market-tuned funnel losing those deals. The single AE-stage manager cannot hold conversion accountability across both segments.

**Trigger check:** ~20+ reps and multi-segment complexity - the pod trigger has fired for the enterprise segment only.

**Design:** keep the assembly line untouched for mid-market; stand up one enterprise pod (e.g. 3 SDR + 2 AE + 1 CS) owning a named book of enterprise accounts. Accept the pod's known costs deliberately: duplicated management overhead, and individual contribution harder to isolate - mitigate with per-role metrics inside the pod, not by abandoning the shape. This hybrid (assembly line for volume, pod for complexity) is where most mature B2B SaaS orgs land, not a way-station.

**Negative variant:** converting the entire 30-rep org to pods because enterprise is exciting. The mid-market segment had no fired trigger; it loses its working stage-conversion visibility and gains only overhead.

## TAM-to-headcount sizing math

Use this to bound total AE headcount before designing the structure around it:

- A rep carrying a $2M quota, targeting ~10% penetration of a $200M serviceable market, implies roughly **10 quota-carrying reps** - before adding management, SDR support, and ramp backfill on top.
- Set quotas on a conservative fraction of the TAM a rep can realistically address, adjusted for win rate and cycle length.
- Vary comp accelerators by territory potential rather than assuming every patch is equal.
- Converting this nominal headcount into effective capacity (ramp-adjusted) is mbfinotti/sales-skills@sales-quota-setting's job - hand it the role mix and the per-role ramp/attrition figures.
