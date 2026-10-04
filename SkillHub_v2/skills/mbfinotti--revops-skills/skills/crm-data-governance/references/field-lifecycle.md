# Field Lifecycle and Governance Cadence

## Intake question set

Every field request answers these before anyone builds (assembled from sourced admin checklists and intake-ticket specs):

- Requester and team.
- Problem statement: what's broken.
- Desired outcome: what improves.
- Users impacted.
- Deadline and why.
- What business requirement does this field address? Who consumes it, and in which reports or workflows?
- What data does it capture - type, format, accepted values? Which systems must it integrate with, and does existing data need migration or cleansing?
- Any privacy/security/sensitivity considerations? Any performance or scale concern? Is it intuitive enough to be adopted?
- Acceptance criteria: how will we know it worked?

First step on receipt: duplicate check against the dictionary. Most requests are an existing field wearing a new label.

## Approval and rejection criteria

Reject or send back for modification when the request:

- Shows no demonstrable business value.
- Won't see real adoption.
- Breaks naming or governance standards.
- Creates a silo instead of integrating.
- Fails privacy/security review.
- Carries real performance cost.
- Duplicates an existing field.

Approval means the field gets, before build, a named owner, a system-of-record designation, a refresh SLA, an enforcement choice, and a dictionary row. Practitioner target for the whole loop, request to published: under one week.

## Periodic review

Fields below a defined population/utilization threshold for **two consecutive quarters** enter a removal review (practitioner rule). Quarterly, the council also reconciles dictionary vs live schema and walks the deprecation queue.

## Deprecation

- Lead with **dependency and impact analysis**, always: formulas, automations, validation rules, layouts, record types, reports, and external integration mappings that reference the field. Get consuming-stakeholder sign-off before touching anything.
- **An empty field is not automatically a deletable field.** An empty field still matters when it's:
  - An integration write target.
  - Seasonal or quarterly-use.
  - Under a compliance/audit hold.
  - Referenced by inactive-but-not-deleted automation.
- Staged retirement is sound practice, but **the phase durations are self-set** - no vendor or governance framework prescribes durations for a four-stage model. Two single-leg vendor precedents anchor the final leg only: Salesforce automatically hard-deletes a custom field **15 days** after it's soft-deleted, unless purged sooner (Salesforce Help, "Purge Deleted Custom Fields"); HubSpot permanently deletes a property **90 days** after it's archived (HubSpot Knowledge Base, "Organize, delete, and export properties"). Neither vendor names a separate deprecated or read-only stage with its own duration, and DAMA-DMBOK and the EDM Council's DCAM both name retirement/decommissioning as a lifecycle stage without prescribing timing. Treat any proposed timeline (e.g. 30 days read-only, 90 days archived) as a default to calibrate with the user, not a standard - the Salesforce and HubSpot windows are reasonable anchors for the archived-to-deleted leg specifically, not for the whole four-stage model. Stage the retirement as:
  1. Label as deprecated.
  2. Read-only.
  3. Archive/export data.
  4. Delete.
- After removal: update related descriptions/help text and clean up orphaned picklist values.

## Governance cadence

"Governance dies from lack of a meeting, not lack of a document" (ORM Tech). The document without the rhythm is shelfware.

- **Council**: small orgs consolidate roles, the seats matter, not the headcount.
  - RevOps chairs.
  - One field-owner per function (Marketing Ops, Sales Ops, CS Ops, Finance).
  - CRM admin/architect for feasibility.
  - An executive sponsor for escalations only.
- **Rhythm** (practitioner-published):
  - Weekly triage, 30-45 min: approve/reject field requests, rule on active sync conflicts.
  - Monthly roadmap, 60 min: priorities, cross-functional changes.
  - Quarterly field-owner review: utilization thresholds, system-of-record map re-validation, dictionary reconciliation, deprecation queue.
- **Decision rights**: documented per change class (new field, picklist change, automation affecting multiple teams, integration mapping); unresolved conflicts escalate to the sponsor. Governance sits with RevOps, not IT.
