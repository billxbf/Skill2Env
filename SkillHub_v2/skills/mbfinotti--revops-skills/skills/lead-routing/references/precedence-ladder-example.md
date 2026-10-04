# Worked precedence ladder and routing matrix

Two worked examples of the same structure, one per motion, plus a negative example. Adapt the tiers to the attributes the team actually populates - a tier reading a field that is blank half the time is not a tier.

## B2B account-based variant

Company: 40 reps, four segment pools (Enterprise, Mid-Market, SMB, Partner), EMEA and NA coverage, named-account list maintained quarterly by sales leadership.

Routing matrix, in precedence order. First match wins; evaluation stops there.

| #   | Criteria                                                           | Assignee                                        | SLA               |
| --- | ------------------------------------------------------------------ | ----------------------------------------------- | ----------------- |
| 1   | Contact record resides in a data-residency-restricted region       | In-region pool, in-region infrastructure only   | 1 business day    |
| 2   | Company on the named-account list                                  | Named-account owner from the list               | 4 business hours  |
| 3   | Matched account has an open opportunity                            | Opportunity owner                               | 2 business hours  |
| 4   | Matched account has an existing owner                              | Account owner                                   | 4 business hours  |
| 5   | Matched account is a subsidiary whose parent has a different owner | Conflict queue (human-owned, 1-day dwell timer) | 1 business day    |
| 6   | Active partner deal registration on the account                    | Channel manager for review                      | 24 hours          |
| 7   | Employee count >= 1000                                             | Enterprise pool                                 | 4 business hours  |
| 8   | Employee count 100-999                                             | Mid-Market pool                                 | 4 business hours  |
| 9   | Employee count < 100, country in coverage                          | SMB pool                                        | 1 business day    |
| 10  | Requested language not covered by tiers 7-9                        | Language-eligible sub-pool                      | 1 business day    |
| 11  | Anything else                                                      | Triage queue, named owner                       | Same business day |

Within tiers 7-10, distribution is capacity-based (fewest open leads) with an availability check that skips reps who are out of office, past their open-lead cap, or outside business hours. That is rung 2.

This company earns rung 2:

- 40 reps across four pools
- an open-lead field already maintained
- a documented definition of when a lead stops counting as open

A ten-rep team with none of those ships rung 1 instead.

Two behaviours worth stating explicitly in the deliverable:

- All contacts from one account land on one owner. A buying committee submitting three forms in a quarter is one relationship, not three rotations.
- Tiers 1-6 are eligibility overrides driven by relationships and contracts. Tiers 7-10 are eligibility by attribute. Distribution only picks a person inside whatever pool those tiers produced.

## B2C / high-volume / PLG variant

Company: self-serve signup product, three shift-based pools (Americas, EMEA, APAC), a specialist team for the paid tier, no named accounts.

| #   | Criteria                                                                                         | Assignee                                           | SLA                             |
| --- | ------------------------------------------------------------------------------------------------ | -------------------------------------------------- | ------------------------------- |
| 1   | Contact record resides in a data-residency-restricted region                                     | In-region pool                                     | 1 business day                  |
| 2   | User belongs to a workspace with an existing paying account                                      | Existing account owner                             | 4 business hours                |
| 3   | Product-qualified signal fired (usage threshold, teammates invited, paid-tier feature activated) | Product-led sales pool                             | 24 hours from trigger           |
| 4   | Self-reported deal size below the sales-touch floor                                              | No human touch; self-serve nurture                 | not applicable                  |
| 5   | Requested language has a dedicated sub-pool                                                      | Language sub-pool for the current shift            | 15 minutes in-hours             |
| 6   | Business hours in the contact's timezone                                                         | Regional pool for the current shift                | 15 minutes                      |
| 7   | Outside business hours everywhere                                                                | After-hours queue plus instant auto-acknowledgment | Next open hours, first in queue |
| 8   | Anything else                                                                                    | Triage queue, named owner                          | Same business day               |

Within tiers 5-6, distribution is availability-aware round-robin over reps currently on shift - rung 1, unchanged, because shift membership already does the workload narrowing a capacity field would otherwise buy. Note tier 4: the no-touch floor is the cheapest tier in this ladder and the one that shrinks every tier below it. Pass the triggering signal to the rep alongside the assignment - a bare score with no context is the documented reason sales teams distrust product-qualified leads.

Tiers 1-2 are identical in shape to the B2B ladder. The catch-all, testing method and measurement are identical for both motions. Only the routing key and the coverage model change.

## Negative example: a ladder that misroutes

```
1. Round-robin across all reps
2. Enterprise leads -> Enterprise pool
3. Named accounts -> named-account owner
4. Existing account owner
```

Every lead matches tier 1, so tiers 2-4 never execute. First match wins means the most general rule at the top swallows everything beneath it. Even reordered as 3, 4, 2, 1 the design still has two defects worth naming:

- No catch-all with a named owner. Tier 1 as a bare rotation hides no-match leads inside normal volume, so a lead with a blank country looks routed and is never investigated.
- Distribution sits in the same list as eligibility. Once a rotation entry can win against an ownership entry, an enterprise lead can land on an SMB rep and an existing customer can be assigned to a rep who has never spoken to them.

Order most specific to most general, keep eligibility above distribution, and terminate with a monitored triage queue rather than a rotation.
