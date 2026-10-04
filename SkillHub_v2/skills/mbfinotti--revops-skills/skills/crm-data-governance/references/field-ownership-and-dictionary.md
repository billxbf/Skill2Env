# Field Ownership and the Data Dictionary

## Ownership model

- DAMA-DMBOK splits the role three ways: **owner** (senior, accountable for classification, protection, use, and quality), **steward** (business-facing, day-to-day definitions, quality, issue triage), **custodian** (technical/IT, storage and access implementation). Clinton Munkres: "The owner sets the destination. The steward navigates the route. The custodian operates the vehicle." And: "Stewardship is a business role; the moment it lives in IT, business consumers stop trusting that the data definitions reflect business reality."
- RevOps practice collapses this into a RACI split by function - the default assignment map:
  - **Marketing Ops**: lead source, UTMs, lifecycle-stage entry criteria, engagement scoring.
  - **Sales Ops**: opportunity stages, pipeline fields, account hierarchy, deal exit criteria.
  - **CS Ops**: health scores, onboarding milestones, renewal risk.
  - **Finance**: contract terms, billing fields, closed-won revenue records.
- **Consumer ownership** (ORM Tech): assign every field to the function that consumes it, not the one that populates it. Reps populate lead source; marketing consumes it in attribution; marketing owns its definition and picklist values.
- **One named human per field** - "Not a team. A person." (RevBlack). Diffuse ownership is the root anti-pattern: "when everyone owns the data, no one owns the data" (RevOps Co-op). The owner's name goes in the dictionary and stays visible - "a steward whose name doesn't appear in the catalog... isn't really stewarding" (Munkres).
- Every governed field must answer four questions (RevBlack):
  - Who owns this?
  - What's the agreed definition?
  - How does it get created, updated, and retired?
  - Who's allowed to change it?

## Govern revenue-critical fields first

Practitioner-published starting set (EverReady) - calibrate to the user's reporting:

- **Opportunity**: close date, stage, amount, owner, next step, last activity date, decision-maker, forecast category.
- **Account**: active owner, industry, size, status, renewal date.
- **Contact**: buying-process role, primary email, last interaction date.
- **B2C additions**: consent/preference fields, retention-schedule fields, and primary identity keys (email, customer ID, device/channel identifiers) enter the governed set as first-class members.

Anything feeding forecasting, routing, compensation, or executive reporting joins the set. Everything else waits for intake to justify it.

## Dictionary column set (working default)

Use this column set as a starting point; calibrate and extend it against the CRM schema in scope. The columns cover names, types, definitions, relationships, constraints, integration mapping, and sensitivity classifications.

| Column                 | Content                                                       |
| ---------------------- | ------------------------------------------------------------- |
| Field label / API name | Human label plus the machine identifier                       |
| Object                 | Which record type carries it                                  |
| Type + accepted values | Data type; picklist values or format rules                    |
| Definition             | Business meaning - why the field exists, not what it's called |
| Owner                  | Named person + owning function                                |
| Populated by           | Rep entry, automation, integration, enrichment                |
| Consumed by            | Reports, automations, teams that read it                      |
| System of record       | The one authoritative writer                                  |
| Enforcement            | Mechanism from the enforcement menu                           |
| Required-at-stage      | Stage/condition where it becomes mandatory, if any            |
| Refresh SLA            | Cadence or event-driven designation                           |
| Sensitivity            | PII/consent/financial classification                          |
| Status                 | Active / deprecated / pending removal                         |
| Last reviewed          | Date + reviewer                                               |

## Keeping the dictionary honest

- Standalone spreadsheets go stale fast and are invisible to tooling and agents - documentation living "in spreadsheets, confluence pages, or external catalogs" instead of in-system is a named failure mode. Prefer generating rows from live CRM metadata (where it is queryable) and storing ownership/sensitivity in the CRM's own field descriptions where the platform allows.
- Make description and inline help text mandatory at field-build time, stating the business reason - even when the platform doesn't enforce it.
- Reconcile quarterly: diff dictionary against live schema. New fields absent from the dictionary are intake-bypass findings, not clerical gaps.
