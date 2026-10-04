# Worked ecosystem memos

Two illustrative memos for fictional products. Every number here is invented for the example and none of it is a benchmark - the shape of the argument is what to copy.

Case A ends in yes. Each of its sections shows the **weak** version teams actually write - the negative example - followed by the **strong** version. Read the weak lines as the failure to avoid, not as an acceptable first draft.

Case B ends in no, because most honest runs of this skill do, and a decision to stay a product is a deliverable rather than a non-event.

## Contents

- Case A - an ecosystem approved
  - Hypothesis
  - Evidence
  - Gates
  - Rung
  - Complementor case
  - Flywheel
  - Obligations
  - Measurement
  - Kill criteria
- Case B - an ecosystem declined

# Case A - an ecosystem approved

A hosted feature-flag and experimentation service selling to engineering organizations.

## Hypothesis

**Weak** - "Becoming a platform will make us the system of record for experimentation and drive stickiness across the developer ecosystem."

**Strong** - "Because our customers need **experiment result sinks into their own warehouses and BI tools** that we will not build, **data-tooling vendors and their implementation partners** will build them on **our event export and webhook surfaces**, earning **implementation revenue and pull-through of their own product**, which makes our product more valuable to **the analytics-owning buyer** by **removing the last reason experiments get analysed outside our tool**."

Commoditized complement: warehouse delivery. It is the piece every buyer needs, nobody wants to own, and we do not want to maintain across a dozen destinations.

## Evidence

**Weak** - "Integrations are one of the top themes in customer feedback."

**Strong** - Seven named complements requested in two quarters, with customers attached: warehouse export (4 customers, 2 of them blocking renewals), a BI template pack (3), a mobile SDK for a framework we do not support (2), and four single-customer requests. Three customers already run unsupported export scripts against our API; one shared theirs publicly.

## Gates

**Weak** - "We have an API, so we are ready."

**Strong**

- G1 counted demand: **pass**.
- G2 externalizable interfaces: **pass** for export, **fail** for evaluation hooks (still an internal library call).
- G3 identified builders: **pass**, three vendors contacted, two interested.
- G4 commoditized complement: **pass**.
- G5 staffing: **unknown** - resolver: platform team headcount decision at the next planning round, 6 weeks.
- G6 envelopment: **fail-with-cap** - the observability vendor most customers already run could bundle flag delivery; we cap investment at rung 3 until we see them move.
- G7 complement readiness: **pass**.

## Rung

**Weak** - "We will launch an app marketplace in Q3."

**Strong** - Chosen: **rung 3, partner-built integrations that we list**.

Rejected:

- Rung 4: evaluation hooks fail G2, so the surface does not exist yet.
- Rung 5: G5 unknown and G6 capped; an app model would oblige us to run security review with no team.
- Rung 6: no complement needs our execution context.

Reopen rung 5 when the platform team exists and five listed integrations are live.

## Complementor case

**Weak** - "Partners will benefit from access to our customer base."

**Strong**

- Data-tooling vendor: ~40 of our 300 accounts overlap their ICP, expected attach 25%, ~$8k ARR pull-through each, ~6 person-weeks to build, ~2 weeks a year to maintain - clearly positive against their alternative of a generic webhook recipe.
- Agency: monetizes 3-5 implementation days per deployment, needs referral flow, not revenue share.
- Internal teams: no business case needed, and they will build the first three exports if we document the surface.
- Value share: no take-rate at this rung; the offer is referral flow, a listed slot and a named contact.

## Flywheel

**Weak** - "More integrations attract more customers, which attracts more integrations."

**Strong**

- Loop: listed exports remove the analytics objection → analytics-owning buyers sign → account overlap grows → the next vendor's arithmetic improves.
- Subsidized side: complementors (free sandbox tenancy, free listing, engineering support during the first build).
- Founding cohort: two warehouse vendors and one BI vendor, hand-recruited to cover the top demand line. We build the first export ourselves as the reference implementation, then hand the pattern over.
- Minimum credible pool: five live integrations covering warehouse, BI and alerting before we promote the directory publicly.
- Honest read: for the first two quarters we are pushing this wheel, not riding it.

## Obligations

**Weak** - "We will support our partners."

**Strong**

- Export surface stability: 12 months minimum, 90 days' notice on breaking changes. Owner: platform lead.
- Roadmap boundary: we will not build warehouse connectors ourselves; if that changes, 90 days' notice to listed partners before announcement. Owner: head of product.
- Partner escalation path with a 1-business-day acknowledgement. Owner: support lead.
- Listing review pass before any integration is published. Owner: platform lead.
- Wind-down: 6 months' notice, documented export of configuration. Owner: head of product.
- Liability register: two published surfaces at launch, reviewed each planning round.

## Measurement

**Weak** - "Track integrations and partner satisfaction."

**Strong**

Baseline today:

- 0 partner-built integrations.
- 0% of accounts with an active complement.
- 4 unsupported customer scripts known.

Targets:

- 5 live integrations by end of Q3.
- 20% of accounts with at least one active complement by end of Q4.
- Time from partner signup to first working integration under 3 weeks.
- Top-five concentration reported each quarter with no target (a diagnostic, not a goal).
- Retention delta between accounts with and without an active complement, reported from Q4 once the sample is large enough to mean anything.

## Kill criteria

**Weak** - "We will review the program annually."

**Strong**

- Stop recruiting if fewer than three integrations are live by 31 December.
- De-escalate to rung 2 (we build the connectors ourselves) if, by 31 March, fewer than 10% of accounts have an active complement or the two founding vendors have not shipped an update in six months.
- Wind down with the 6-month notice above if the observability vendor bundles flag delivery and our overlap accounts start churning.

Any of these triggers a written re-decision, not a quiet continuation.

# Case B - an ecosystem declined

A CI runtime-security scanner selling to platform-engineering teams. The exec team asked for an app marketplace. The memo says no, and says it in a form the next person can reopen.

**Hypothesis** - Could not be completed. The complement blank filled as "policy packs", the builder blank as "the security community", the return blank as "reputation". Two of three blanks are vague, so the hypothesis was sent back once and still could not name a builder with a reason of their own.

**Evidence** - Three complements requested in two quarters, all three by the same customer, none tied to a stalled deal. No customer has built unsupported glue against the API. The most-requested item - a policy pack for one compliance regime - was requested by four customers and is a content problem, not an extension-surface problem.

**Gates**

- G1 counted demand: **fail** (three complements, one customer).
- G3 identified builders: **fail** (no organization contacted has a revenue reason).
- G4 commoditized complement: **fail**, and in the worst direction - policy packs _are_ the differentiated part of what we sell, so an abundant free supply of them commoditizes us, not our complements.

G2, G5, G6, G7 not evaluated; G1, G3 and G4 already decide it.

**Decision** - No ecosystem. Stay at rung 2: we write the policy packs ourselves and ship the top-requested regime as a roadmap item. The marketplace question is closed for two quarters, not forever.

**Reopen conditions** - Re-run this skill when any one of these holds:

- Eight or more distinct complements requested by five or more customers.
- A named security vendor asks in writing to publish against us.
- A competitor ships a pack ecosystem and we start losing deals to breadth of coverage.

Owner: head of product. Review date: 31 March.

**Why this is a real deliverable** - The failing gates are written down with the evidence that failed them, so the next exec who asks for a marketplace gets a dated answer instead of a fresh six-week study. Recording G4's failure matters most: it is the one failure that no amount of demand would fix.
