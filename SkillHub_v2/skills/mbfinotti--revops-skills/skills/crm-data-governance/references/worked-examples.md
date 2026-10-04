# Worked Examples

## Done right: five-field governance spec (mid-market SaaS, B2B with a B2C product line)

| Field                             | Owner                              | System of record                                     | Precedence / sync                               | Refresh SLA                                                     | Enforcement                                         |
| --------------------------------- | ---------------------------------- | ---------------------------------------------------- | ----------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------- |
| Lifecycle stage (contact)         | J. Okafor, Marketing Ops           | Marketing automation until SQL, then CRM             | Real-time push; CRM wins post-SQL               | Event-driven                                                    | Restricted picklist; edit locked to owning function |
| Industry (account)                | J. Okafor, Marketing Ops           | Enrichment provider (designated overwrite exception) | Scheduled pull; enrichment wins over manual     | Semiannual                                                      | Restricted picklist                                 |
| Close date (opportunity)          | M. Reyes, Sales Ops                | CRM (rep-entered)                                    | Single writer                                   | Derived from 45-day cycle: re-verify on every push              | Conditional validation: push requires a reason      |
| Renewal date (account)            | D. Chen, Finance                   | Billing system                                       | Real-time push; CRM copy read-only              | Event-driven (contract events)                                  | Per-role edit permissions: integration-only writer  |
| Consent status (person, B2C line) | A. Laurent, Marketing Ops (policy) | Consent-management system                            | Real-time push; block-and-alert on any conflict | Event-driven + legal-basis changes; retention schedule attached | Integration-only writes; centralized consent logic  |

Sample dictionary row (Close date): `Opportunity | CloseDate | Date | "The date the buyer is expected to sign, per the buyer's stated process" | Owner: M. Reyes (Sales Ops) | Populated by: rep | Consumed by: forecast rollup, comp | SoR: CRM | Enforcement: push-reason validation | Required at: Proposal+ | SLA: re-verify each push | Sensitivity: none | Status: active | Last reviewed: 2026-08`.

Note what makes this pass:

- Every owner is a person.
- The enrichment-overwrite on Industry is a documented exception, not an accident.
- The B2C consent field carries retention and centralized logic.
- The close-date SLA is explicitly derived from the user's own cycle, provenance-tagged.

Three fields carry real-time push against the efficiency order, and each one earns the promotion for the stated reason - a stage change that fires automation, a contract event, a consent withdrawal that may not be a batch behind. This team had an integration platform already running; a team without one deletes that pattern and accepts the staleness in writing.

## Done wrong: the required-fields purge

A mid-market team reacts to "our CRM is dirty" like this:

- Makes 14 fields hard-required at record creation.
- Assigns ownership of all fields to "the RevOps team".
- Switches the enrichment provider to overwrite-everything to "fix stale data".
- Writes a 30-page governance policy.
- Forms a council that meets once at kickoff.

Six months later:

- Required fields hold "n/a", ".", and invented phone numbers.
- Reps route around the CRM entirely for early-stage records.
- Verified direct-dial numbers were clobbered by stale enrichment.
- Employee count flaps weekly between the CRM and the marketing platform because both still write it.
- The custom-field count grew 20% because nobody staffs intake.
- No one can say who approves a picklist change - the policy document says "the council."

Each mistake mapped to the rule it broke:

| Mistake                                 | Broken rule                                                                                      |
| --------------------------------------- | ------------------------------------------------------------------------------------------------ |
| 14 hard-required fields                 | Efficiency order skipped straight to its worst rung; reps are not the enforcement of last resort |
| Owner = "the RevOps team"               | One named person per field; everyone-owns-nothing                                                |
| Enrichment overwrite-everything         | Augment by default; risk-tier writes; identity fields need human review                          |
| Both systems still write employee count | One system of record per field; conflict detection                                               |
| Council met once                        | Governance dies from lack of a meeting, not lack of a document                                   |
| Field count grew unchecked              | Intake with duplicate check is part of the system, not paperwork                                 |

The fix is not a better policy document - it is fewer required fields, named humans, one writer per field, and a weekly meeting that actually happens.
