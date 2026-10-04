# Event qualification scorecard

Contents: evidence request → scoring grid → worked examples → portfolio plan template.

## Evidence request

Send this before discussing price. What comes back - and how fast - is itself a signal.

> Subject: Sponsorship evaluation - [event name] [year]
>
> We are evaluating [event] for our [year] developer-event plan and need a few things to price it internally:
>
> 1. Attendee breakdown by role, seniority and company size for the last edition (actuals, not projections).
> 2. Regional split of attendees.
> 3. Last edition's post-event report, including returning-sponsor rate.
> 4. Number of sponsors at each level, and the floor plan.
> 5. The full package sheet: booth or table specification, passes included, what contact data sponsors receive and under which consent, how session and workshop slots are allocated, and which surfaces are sold separately.
> 6. Contract and add-on deadlines, payment terms.
> 7. Code of conduct and the sponsor-specific rules attached to it.
>
> Happy to sign an NDA if any of it is confidential.

Missing answers are not neutral. No demographic actuals means nobody measured; no post-event report means no sponsor asked last year.

## Scoring grid

Score each row 0-5 against **the objective chosen in step 1**, not in the abstract. Weights below suit a pipeline or adoption objective; for an awareness objective, raise Reach to 3 and lower Decision access to 1.

| Criterion                   | Weight | 0-1                                                   | 3                            | 5                                                                |
| --------------------------- | ------ | ----------------------------------------------------- | ---------------------------- | ---------------------------------------------------------------- |
| ICP overlap                 | 3      | audience holds a different problem                    | adjacent roles, some overlap | the exact role you named in the interview dominates              |
| Decision access             | 2      | students or pure hobbyists (for a pipeline objective) | practitioners who influence  | practitioners plus their budget holders                          |
| Hands-on path               | 2      | logo only                                             | booth demo possible          | workshop, prize track or integration inside what attendees build |
| Organizer track record      | 2      | first edition, no data                                | 2-3 editions, partial data   | long history, actuals published, sponsors return                 |
| Sponsor density             | 1      | crowded hall, competitors entrenched                  | typical density              | few sponsors, or a niche you own                                 |
| Staffing feasibility        | 2      | nobody credible can travel                            | reachable with strain        | local team or an easy trip for the right people                  |
| Cost per reachable attendee | 2      | far above your other options                          | comparable                   | clearly below, after full costs                                  |
| Compounding                 | 1      | one-off event                                         | annual, audience turns over  | annual, same audience returns and remembers                      |

Max 75. Read the total as a rank, never as a verdict: an event scoring 60 with no staffing available is still a no, and any 0 on ICP overlap ends the evaluation regardless of total.

## Worked examples

**Strong - regional cloud-native conference, 900 attendees, third edition.** Platform and SRE audience with published role actuals (62% engineers, 18% architects, 12% managers); the product is a platform tool they already have the problem for. ICP 5×3, decision access 4×2, hands-on 4×2 (workshop slot offered), track record 5×2, density 3×1, staffing 5×2 (two-hour train ride, three engineers available), cost 4×2, compounding 4×1 → **63/75**. Decision: sponsor at a mid tier plus the workshop add-on; skip the party sponsorship.

**Weak - 6,000-attendee general developer expo, first edition in a new city.**

- Attendance projected, not measured
- Role mix unknown
- 80 sponsors
- A booth costs more than the regional event's entire package
- The only staff who could go are two field marketers

ICP 2×3, decision access 2×2, hands-on 2×2, track record 1×2, density 1×1, staffing 1×2, cost 1×2, compounding 2×1 → **27/75**. Decision: decline, and record the reason so it is not rebought next year on the strength of the headcount.

The gap between the two is not size. It is that the first event can answer questions about its audience and the second cannot.

## Portfolio plan template

```markdown
# Developer event sponsorship plan - [year]

## Objective and budget

Primary objective: [awareness | adoption | pipeline | ecosystem | recruiting]
Total budget (fully loaded): [amount] · Allocated: [amount] · Reserve: [amount, 15-25%]
Staffing ceiling: [people × days available across the year]

## Committed events

| Event | Date | Deadline | Objective | Model / tier | Fully loaded cost | Threshold (cost per qualified conversation, min count) | Owner |
| ----- | ---- | -------- | --------- | ------------ | ----------------- | ------------------------------------------------------ | ----- |

## Declined, with reason

| Event | Score | Reason declined |
| ----- | ----- | --------------- |

## Reserve policy

[What the unallocated share is for, and who can release it.]

## Review cadence

[Post-event review within two weeks; portfolio review at the budget date.]
```
