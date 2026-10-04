# SOR/SOT Designation and the Identity Spine

Contents: Definitions; the typical per-object-class pattern; the revenue-recognition pipeline in detail; usage-metering platforms as SOR/SOT; warehouse-as-hub mechanics; the identity spine; worked examples.

## Definitions

- **System of record (SOR):** the operational store that authors and masters a record - the write path. It wants strict transactional behavior.
- **Source of truth (SOT):** the derived, reconciled, authoritative value used for decisions - the read path. It wants broad integration and history.
- **Golden record:** the MDM-specific term for the deduplicated master entity produced by reconciling multiple SORs.

Vendors use all three interchangeably; practitioners do not, and neither should the policy. The design principle (Digna, with Nutrient and Kohezion converging independently): forcing one system to do both jobs is the mistake, because the write path and the read path want opposite properties.

IBM's formulation of the same split: an SOR is authoritative for one business domain; an SOT aggregates and harmonizes across SORs. That is enterprise-data-architecture terminology applied to GTM by analogy rather than a RevOps-native formulation - present it as a lens, not as a RevOps standard.

## The typical per-object-class pattern

**This table is the dominant pattern in practice, not a published canon. Individual orgs vary - adapt it, never copy it unexamined.**

| Object class                           | Typical SOR (authors)                                                          | Typical SOT (decisions read)                        | Note                                                                                                                 |
| -------------------------------------- | ------------------------------------------------------------------------------ | --------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| Account                                | CRM                                                                            | Warehouse account dimension, often MDM-resolved     | Parent/child hierarchy usually reconciled in the warehouse against a firmographic provider                           |
| Contact / Lead / Person                | CRM + marketing automation                                                     | CDP or warehouse identity table                     | The highest duplication surface in the stack                                                                         |
| Deal / Opportunity                     | CRM                                                                            | Warehouse opportunity fact table                    | CRM authors; the warehouse is truth for pipeline metrics                                                             |
| Subscription / Contract                | Billing platform                                                               | Warehouse; billing itself for invoicing             | The CRM opportunity and the billing subscription routinely disagree - that is why both columns exist                 |
| Usage event                            | Metering platform (or product analytics/app database before usage is billable) | Warehouse; the metering platform for billable usage | See "Usage-metering platforms as SOR/SOT" below for named vendor mechanics                                           |
| Revenue metrics (ARR/MRR/NRR/bookings) | None single - derived                                                          | Warehouse + the definitional home                   | ARR/MRR are normalized from active subscriptions, not raw billings                                                   |
| Recognized revenue                     | General ledger (ASC 606)                                                       | GL/ERP                                              | A separate SOR from CRM bookings entirely; owned by Finance - see "The revenue-recognition pipeline in detail" below |

The canonical example worth repeating to the user: the CRM authors the opportunity, but the warehouse is the source of truth for the ARR number - and the GL is a third, separately-authored number for recognized revenue. The CRM figure and the GL figure never match by design.

## The revenue-recognition pipeline in detail

Vendor documentation, not just practitioner convention, supports a four-layer chain for the recognized-revenue object specifically - the closest thing in this skill's sourcing to a published canon, though it covers one object class, not the whole table above. Chargebee's own product docs state the boundary plainly: a RevRec engine (ASC 606 five-step model) absorbs pricing, billing, payment, and revenue complexity and posts one summarized journal entry per period, so "the GL stays exactly what it's meant to be: a system of record" and is explicitly not a data warehouse.

| Layer         | Authoritative for                                  | Typical vendor                                                       |
| ------------- | -------------------------------------------------- | -------------------------------------------------------------------- |
| CRM           | Contract terms, bookings, ARR at signature         | Salesforce, HubSpot                                                  |
| Billing       | Invoices, subscriptions, payments, credits         | Zuora Billing, Chargebee, Stripe Billing                             |
| RevRec engine | ASC 606 five-step allocation, recognition schedule | Zuora Revenue (RevPro), Chargebee RevRec, Stripe Revenue Recognition |
| GL            | Summarized period journal entries                  | NetSuite, QuickBooks, Sage Intacct                                   |

Why the CRM and GL numbers diverge is structural, not a data-quality problem: each layer is authoritative for a different moment in the deal lifecycle. A December annual close can show full contract value in CRM bookings immediately while the GL recognizes only a thin slice that month, the rest sitting in deferred revenue. Named divergence triggers, sourced to a rev-integrity vendor's own documentation (safebooks.ai): timing differences (a Q4 booking that starts recognizing in Q1), allocation differences (bundled elements recognizing at different rates), and modification differences (a post-booking change altering the schedule) - plus, at the billing-to-RevRec seam specifically, invoices generated before service activation, billing credits that never flow through to a RevRec adjustment, usage-based components billed in arrears against fixed fees recognized ratably, and refunds processed outside billing. Ben Murray (The SaaS CFO) argues from the CRM side that ARR/MRR should never be reported straight out of CRM at all, since the CRM is rarely the correct source of truth for recurring revenue - reinforcing that the CRM and GL numbers are two different objects, not one object measured twice.

Vendors formalize the CRM/billing boundary through documented directional sync, not genuine bidirectional truth. Zuora's own connector documentation: the Zuora Billing Connector for Salesforce performs a single directional sync from Zuora to Salesforce, near real-time - Zuora Billing is authoritative, Salesforce is a downstream mirror for billing-owned objects, enforced at the field level by a CRM ID field on the Zuora account that prevents a duplicate account being created on resync. Stripe's own reconciliation documentation names a live discrepancy: an unpaid invoice stays "open" and continues to be recognized as revenue in the Revenue Recognition report, but because it was never collected, the Balance summary report excludes it - a documented mismatch between two reports from the same vendor, not a bug.

A second, competing architecture is emerging that collapses this stack instead of reconciling it: Rillet and LedgerUp both pitch native-GL revenue recognition, arguing the reconciliation layer between a standalone RevRec tool and the books recreates the manual work it was meant to remove. Treat this as vendor positioning documenting a real, growing second school (unify the ledger) against the traditional school (keep CRM/billing/RevRec/GL separate, reconcile explicitly) - state both in the deliverable rather than picking a winner silently, the same posture this skill takes on the data-contract debate.

## Usage-metering platforms as SOR/SOT

For usage-based and consumption billing, the metering/billing platform itself - not product analytics, not the warehouse - is the documented source of truth for the usage events that feed invoices, verified across three named vendors' own API documentation.

| Vendor    | Dedup mechanism                                     | Backfill/correction window                                                               | Documented control                                   |
| --------- | --------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------- |
| Orb       | `idempotency_key`                                   | Raw events retained indefinitely for re-query; grace period governs near-real-time dedup | Ingestion validation + dedup, pre-invoice            |
| Metronome | `transaction_id`                                    | 34-day resubmission window; structured correction files                                  | Void/regenerate finalized invoices, full audit trail |
| Amberflo  | Not separately documented in public materials found | "Auto reconciliations" (vendor claim, unverified)                                        | Event-level audit trail, ingestion to invoice        |

The reason product analytics and the warehouse are excluded is structural, not a vendor gap: billing needs row-level correctness guarantees - no double counting, defined grace periods, auditable corrections tied to one invoice - which idempotency keys and correction workflows exist to provide, while analytics tools and the warehouse are built for aggregate, eventually-consistent analysis. A warehouse can join CRM, billing, product-telemetry, and support data, but has no opinion about what any of it means for a single invoice line.

Treat the metering layer's vendor landscape as unstable, not the designation itself: within roughly six months in 2026, every major independent metering vendor was acquired by a payments or CRM incumbent - Stripe acquired Metronome, Salesforce is acquiring m3ter, and Adyen is acquiring Orb. The designation (metering platform = SOR/SOT for billable usage events) holds regardless of which company ends up operating that layer.

The org-wide split, in one breath (ARISE GTM):

- The CRM owns commercial relationships and engagement, and "should not be your event log or your data warehouse".
- Billing owns contract truth (plans, seats, MRR/ARR inputs, renewal dates, churn events), which the CRM references and never recomputes.
- Product analytics owns behavioral events, usable for revenue decisions only when every event carries consistent user, account, and domain identifiers.
- The warehouse is where the three representations of "the same customer" get reconciled.

## Warehouse-as-hub mechanics

The mature pattern: the warehouse is SOT, operational systems stay SOR for what they author, and reverse-ETL syncs modeled values back into operational tools. Two rules keep it honest:

1. **The warehouse is the sole author of every field it syncs outward.** If anything else also writes that field - a rep, an enrichment provider, another sync - the value re-exports, the lineage turns circular, and the org has two truths again with extra steps.
2. **Adopt it at the right stage.** Practitioner recommendation: warehouse-as-hub above roughly $10M ARR or with usage-based billing; below that, a CRM-centric pattern is adequate and reverse-ETL is overhead. The threshold is a practitioner benchmark, not audited research - tag it as such.

MDM applies to GTM mainly at the account and person entities: the warehouse account dimension becomes the golden record compiled from multiple SORs, while the CRM remains SOR for sales-authored fields (Gartner's "Consolidation MDM" style).

## The identity spine

The verified pattern fix for cross-system join-key mismatch (Supportbench):

- Pick **one canonical account ID and one canonical person ID**.
- Map every system's native keys back to them in an alias table.
- Resolve exact matches automatically.
- Route fuzzy cases to human review.

Domain-based matching and "the CRM ID as universal key" both break on M&A, subsidiaries, and self-serve signups - the alias table is what absorbs those breaks.

The identity problem is two problems, not one (Datawhistl): account/CRM data is a strong-key, near-solved regime; anonymous behavioral data is keyless and mostly unresolvable, and tooling papers over the seam. Two consequences for policy:

- Measure resolution coverage against the **linkable population**, never all traffic - against all traffic, every identity metric is noise.
- Do not fund a large budget pretending anonymous identity is fully resolvable. Accept the boundary and design reporting around it.

Per motion:

- B2B resolves deterministically at the account level (domain matching, firmographic enrichment).
- PLG/B2C stitches anonymous-to-known users deterministically plus probabilistically in the analytics/CDP identity graph.
- Hybrid clusters self-serve signups into workspaces by domain, then reconciles the workspace graph with the account hierarchy in the warehouse - the seam where most identity failures originate.

## Worked example - done right

Illustrative composite for a hybrid-motion SaaS company at roughly the warehouse-as-hub stage; the pattern is sourced, the company is not real.

```
Object class     SOR                SOT                       Owner
Account          CRM                warehouse dim_account     RevOps lead
Person           CRM + marketing    warehouse identity table  RevOps lead
                 automation
Opportunity      CRM                warehouse fct_opportunity RevOps lead
Subscription     billing platform   warehouse                 Finance systems owner
Usage event      product analytics  warehouse                 Analytics eng lead
ARR / MRR        derived            warehouse + signed        Analytics eng lead,
                                    definitions               definitions signed by Finance
Recognized rev   general ledger     general ledger            Controller
Synced-back      warehouse is sole author of every field reverse-ETL'd
fields           into CRM (health tier, computed ARR, usage summary)
```

What makes it right:

- SOR and SOT designated separately per object class.
- Derived metrics have no fake SOR.
- Recognized revenue stays with Finance.
- The sole-author rule for synced fields is written into the table itself.
- Every row has a named owner.

## Negative example - done wrong

> "Salesforce is our single source of truth. All teams should treat Salesforce as authoritative for customer data. The data team syncs warehouse metrics into Salesforce so everything lives in one place."

Three defects, each a documented failure mode:

- Truth is declared per **system** instead of per object class, so the billing-vs-CRM subscription disagreement has no rule to resolve it.
- The CRM is implicitly asked to be the event log and warehouse it cannot be.
- Warehouse values synced into a CRM that other processes also write creates circular lineage - the "single" source of truth now has multiple authors and no arbiter.

The one-sentence policy reads decisive and settles nothing.
