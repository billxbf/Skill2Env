# Worked Examples

Every number below is illustrative - invented to show the expected level of specificity, not a benchmark. Replace all of them with the user's own targets and floors.

## Example 1 - transacting reseller scorecard

Partner: mid-tier reseller, ~$40K average deal, 12-month rolling revenue window, activity metrics scored per quarter.

| Dimension (weight)      | KPI                                    | Target                | Red flag             | Window      | Source                   | Owner           | Actual          | Score           |
| ----------------------- | -------------------------------------- | --------------------- | -------------------- | ----------- | ------------------------ | --------------- | --------------- | --------------- |
| Revenue (40%)           | Partner-sourced revenue                | $800K                 | $400K                | Rolling 12m | CRM (approved deal regs) | Partner ops     | $650K           | 32/40           |
| Pipeline (20%)          | Deal-reg approval rate                 | ≥85%                  | <60%                 | Quarter     | PRM                      | PAM             | 90%             | 11/20           |
|                         | Registered pipeline value              | $500K                 | $200K                | Quarter     | PRM                      | PAM             | $260K           | (blended above) |
| Capability (15%)        | Certified headcount                    | 4 current             | <2                   | Quarter     | LMS                      | Enablement lead | 3               | 11/15           |
| Engagement (15%)        | Portal activity + MDF utilization      | Active + ≥70% claimed | Inactive 60d or <30% | Quarter     | PRM + MDF ledger         | PAM             | Active, 55% MDF | 10/15           |
| Customer outcomes (10%) | Retention of partner-sourced customers | ≥90%                  | <75%                 | Rolling 12m | Billing/CS system        | Finance         | 93%             | 10/10           |

**Composite: 74/100.** Status bands (user-set): ≥80 healthy, 60-79 stable, 40-59 at-risk, <40 critical. Reading: revenue and retention solid; thin registered pipeline is the leading warning - raise it at the next check-in before it becomes a revenue miss. No red-flag floor crossed, so the ladder does not fire.

## Example 2 - non-transacting ISV/tech partner scorecard

Partner: integration ISV; no resold revenue, so revenue-track KPIs would score it blank. Its own track:

| Dimension (weight) | KPI                                           | Target    | Red flag | Window      | Source                  | Owner             | Actual | Score |
| ------------------ | --------------------------------------------- | --------- | -------- | ----------- | ----------------------- | ----------------- | ------ | ----- |
| Influence (35%)    | Influenced revenue (capped)                   | $300K     | $100K    | Rolling 12m | CRM opportunity tags    | Partner ops       | $340K  | 35/35 |
| Adoption (25%)     | Integration attach rate on closed deals       | ≥15%      | <5%      | Quarter     | CRM + product telemetry | Partner ops       | 11%    | 17/25 |
| Health (20%)       | Active shared customers using the integration | 60        | <25      | Quarter     | Product telemetry       | PAM               | 58     | 19/20 |
| Capability (10%)   | Joint-solution certifications                 | 2 current | 0        | Quarter     | LMS                     | Enablement lead   | 2      | 10/10 |
| Co-marketing (10%) | Qualified leads from joint campaigns          | 25        | <5       | Quarter     | Marketing automation    | Partner marketing | 12     | 6/10  |

**Composite: 87/100 - healthy.** The partner never resells a dollar yet gets a real, defensible score - the point of per-type tracks.

## Example 3 - a worked underperformance sequence

Partner: reseller from Example 1's program, one year later.

1. **Q1 trigger.** Sourced revenue falls below its $400K floor for a full window; deal registrations stop; portal quiet 70 days. Two red flags → formal review per the trigger table. PAM logs it in the PRM within the program's stated response time.
2. **Diagnostic call.** Scorecard presented first - data, not accusation. Diagnosis: the partner's champion (their partnerships lead) left; nobody picked up the vendor's line.
3. **Corrective action plan (90 days, checkpoints at 30/60/90 - durations user-set).** Partner commits:
   - Name a new partnership owner within 30 days.
   - Re-certify 2 sellers by day 60.
   - Register $150K of pipeline by day 90.

   Vendor commits: a re-onboarding enablement session and 5 qualified leads. Consequence stated in writing: de-tier at the next tier review if the day-90 checkpoint fails. Both sides sign.

4. **Day-60 checkpoint.** New owner named, 1 of 2 certifications done, $60K registered. Partial - plan continues, escalated one step to the channel manager lead for visibility.
5. **Day-90 outcomes - two branches.**
   - _Recovery_: both certifications current, $170K registered. Plan closed as recovered; partner returns to normal cadence; the episode and outcome stay logged in the PRM.
   - _Failure_: registrations stall at $70K. The documented plan has failed - de-tier proceeds under the tier structure's demotion and appeals rules, communicated by the channel chief, with the paper trail attached.
