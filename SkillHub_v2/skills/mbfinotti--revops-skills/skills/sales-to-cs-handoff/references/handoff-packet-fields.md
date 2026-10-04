# Handoff Packet Fields

The data set that must transfer at handoff merges the three best-known practitioner inventories, organized here into six categories:

- Kristi Faltorusso's "10 Essentials" checklist.
- Lincoln Murphy's Sixteen Ventures list: CRM data, call recordings, notes, contract terms, goals, concerns, timeline expectations, the customer's own definition of success.
- Gainsight's operationalized set: primary business objective, buying-process engagement history, feature interests, contract details, value areas.

Rules that make the list work:

- Split gate handling by field weight. Blocking everything guarantees the gate gets gamed.
  - **Must-block**: gate refuses the handoff without it.
  - **Optional**: valuable, never blocking.
- Every field names a role on each side. Cut any field with no consumer.
  - **Supplier**: the role that fills it, usually during the sales cycle, not in a panic at close.
  - **Consumer**: the role that reads it at internal sync or kickoff.
- Prefer structured fields for anything measured or gated. Attach recordings and documents for anything with nuance. Free text is the fallback, never the plan. Murphy's warning: the discovery intel that never leaves the rep's head is exactly what loses the emotional connection.
- Right-size per segment: the full set below fits enterprise/high-touch; see segment guidance at the end for what SMB and self-serve keep.

## 1. Commercial and contract

| Field                                                           | Why it transfers                                                                                            | Supplier        |
| --------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | --------------- |
| Products/modules purchased, and exclusions                      | The receiver must know what was actually bought - and what the customer may believe they bought but did not | AE (must-block) |
| Contract value, term, start date, renewal date                  | Sets the renewal clock and coverage tier                                                                    | AE (must-block) |
| Special terms: non-standard renewal, pricing, payment, opt-outs | Non-standard terms surprise post-sale teams at the worst moment                                             | AE (must-block) |
| Discount given and rationale                                    | Context for renewal conversations; deep discounts flag expectation risk                                     | AE (optional)   |

## 2. Goals and success definition

| Field                                                                                    | Why it transfers                                                                                                                          | Supplier                       |
| ---------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| Primary business objective(s) for buying                                                 | The single most-cited field across all three practitioner lists; everything post-sale aligns to it                                        | AE from discovery (must-block) |
| Customer's own definition of success, with metrics/KPIs agreed                           | Murphy's Desired Outcome = Goal + Appropriate Experience: carry the goal _and_ the experience-delivery expectation, not just the contract | AE (must-block)                |
| Timeline expectations set during the sale                                                | Missed timeline expectations read as broken promises                                                                                      | AE (must-block)                |
| Conditions and constraints around the goal (budget cycle, exec mandate, deadline driver) | Explains urgency and sequencing to the receiver                                                                                           | AE (optional)                  |

## 3. Stakeholders and org

| Field                                                           | Why it transfers                                                                                                                         | Supplier        |
| --------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| Economic buyer / signer                                         | Renewal authority; may never appear in onboarding otherwise                                                                              | AE (must-block) |
| Champion and day-to-day contact(s)                              | Who the post-sale owner actually works with                                                                                              | AE (must-block) |
| End-user groups and influencers, with sentiment per stakeholder | Faltorusso's list is explicit: stakeholders _with sentiment_ - a skeptical influencer is a different onboarding than an enthusiastic one | AE (optional)   |
| Org chart overview: reporting lines, dotted lines               | Locates the champion's power and the expansion paths                                                                                     | AE (optional)   |

## 4. Sales-cycle context

| Field                                                                                           | Why it transfers                                                                                                  | Supplier        |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | --------------- |
| Use cases and pain points that resonated                                                        | Onboarding should land first value on the pain that sold the deal, not a generic tour                             | AE (must-block) |
| Competitive evaluation: who else was evaluated, why this vendor won                             | The win reason is the retention thesis; the losing vendor will call again                                         | AE (optional)   |
| Concerns and objections raised during the sale                                                  | Unaddressed concerns resurface as churn signals                                                                   | AE (must-block) |
| Commitments and promises made: SLAs, training, custom work, roadmap items, support expectations | Hidden promises discovered post-signature are the classic handoff failure; reviewed line by line at internal sync | AE (must-block) |

## 5. Technical and delivery requirements

| Field                                                 | Why it transfers                              | Supplier                                           |
| ----------------------------------------------------- | --------------------------------------------- | -------------------------------------------------- |
| Integrations, APIs, custom development needed         | Sizing and sequencing the implementation      | AE / sales engineer (must-block when any exist)    |
| SOW ownership and delivery timeline, if services sold | Who delivers what by when                     | AE / services (must-block when SOW exists)         |
| Security, compliance, data-residency requirements     | Late discovery blocks go-live                 | Sales engineer (optional unless regulated segment) |
| Data migration scope                                  | Often the longest pole in time-to-first-value | Sales engineer (optional)                          |

## 6. Engagement history

| Field                                              | Why it transfers                                                                   | Supplier                                                     |
| -------------------------------------------------- | ---------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| Key call recordings and demo recordings, linked    | The highest-fidelity carrier of nuance; cheaper than perfect notes                 | Auto-captured where tooling exists, else AE links (optional) |
| Content/webinar engagement from the buying process | Gainsight's operational set: shows what topics the buying team already cares about | Marketing automation (optional)                              |
| Feature/module interests expressed pre-sale        | Directs which capabilities to activate first                                       | AE (optional)                                                |

## Right-sizing by segment

- **Enterprise/high-touch**: full set; categories 3-5 carry the weight.
- **Mid-market**: full must-block set; optional fields filled when known, never chased.
- **High-volume SMB**: categories 1, 2, and the commitments field only, as structured CRM fields - a packet document per deal does not scale here.
- **PLG/self-serve and B2C**: the "packet" is the account record itself - plan, billing state, signup source, activation signals, marketing consent. Human-context fields are irrelevant; completeness of the record is the gate.
