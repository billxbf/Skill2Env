# Escalation and Adjudication

## The ladder

Design the escalation path as a tiered table: adapt tiers to org size, but keep every column:

| Tier                   | Trigger                                                               | Adjudicator                                                               | SLA                                                           | Required evidence                                                                |
| ---------------------- | --------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| 0: Automated           | Duplicate registration or CRM overlap detected at submission          | System rule (first-approved wins; later claims rejected with reason)      | Real time                                                     | Registration timestamps                                                          |
| 1: Working level       | A party disputes the automated outcome, or overlap surfaces mid-cycle | Partner manager + direct manager together                                 | 48h acknowledgment, decision target within the 48h convention | Registration timestamp, first-engagement timeline, activity logs from both sides |
| 2: Neutral adjudicator | Tier 1 deadlocks, or deal value crosses a stated threshold            | Named neutral seat: Head of Channel Ops or deal desk                      | 48h decision from escalation                                  | Tier 1 record plus written statements from both parties                          |
| 3: Executive           | High-value or precedent-setting disputes; appeals                     | Channel chief, with CRO consulted; formal disputes within 5 business days | 5 business days                                               | Full case file; decision logged as precedent                                     |

The 48-hour decision and 5-business-day formal-dispute figures are the field's convention, vendor-published rather than independently validated: treat them as the ceiling, not a scientific target. Predictability matters more than raw speed.

## The evidence standard

Decide on evidence, never seniority: the registration timestamp, the timeline of who engaged the customer first, and activity logs of what each party actually did. Write this standard into the RoE so every party knows in advance what wins a dispute: that knowledge prevents more disputes than it resolves.

The most common structural cause of disputes is information asymmetry: the direct rep genuinely doesn't know a partner is engaged because the portal and CRM are disconnected. Conflict from ignorance is a systems defect, not a behavior problem: fix the system of record before blaming either side.

## The neutral adjudicator seat

Name one adjudicator, and never seat the direct sales leader there. The perennial complaint across the field is that when conflicts escalate, direct sales wins. Once partners believe that, they stop registering and stop escalating, which reads as "less conflict" while the channel quietly disengages.

The commonly cited neutral seat is the Head of Channel Ops. The deal desk is the alternative where channel ops doesn't exist yet.

## Process discipline

- **Hear both sides separately before deciding**: separate statements first, then objective analysis from registration records and communication logs. A joint confrontation first hardens positions.
- **Document every decision** with the evidence relied on. Logged decisions become precedents that make the next adjudication faster and more predictable.
- **Provide one appeal**: to the tier above, on new evidence only.
- **Define remediation for the losing side.** This is what preserves the relationship: a partner who loses a claim fairly can still get compensated influence credit, priority on the next comparable opportunity, or a documented margin accommodation. A direct rep who loses keeps quota retirement under the neutrality policy so the loss costs nothing personal. A ruling with no remediation turns every adjudication into a zero-sum fight.

## RACI

| Role                   | RACI                                              | Owns                                                                                           |
| ---------------------- | ------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| Channel chief          | Accountable                                       | The policy itself; ratifies with legal/finance; final backstop for high-value disputes         |
| Partner operations     | Responsible                                       | Registration hygiene, conflict detection, territory data, system of record, portal publication |
| Deal desk              | Responsible for case rulings; Consulted on policy | Neutral adjudication on individual deals; pricing and margin protection                        |
| Sales leadership / CRO | Consulted (critically)                            | Comp design: the root-cause lever; without their sign-off comp neutrality never happens        |
| Legal / finance        | Consulted                                         | Contract rights, territory definitions, pricing-clause compliance                              |

Startup vs enterprise: early-stage, the channel chief is Responsible and Accountable at once: there is no partner ops or deal desk to delegate to, and the trap is over-regulating with process the company can't staff. Enterprise separates the roles fully (chief partner officer above a dedicated partner ops function) and formalizes the written escalation path with timelines, criteria, and authority levels.
