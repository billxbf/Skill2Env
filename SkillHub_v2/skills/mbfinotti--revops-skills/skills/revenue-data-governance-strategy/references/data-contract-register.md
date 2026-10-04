# The Data-Contract Register

## One term, two meanings

"Data contract" names both a technical artifact (a versioned schema spec enforced in CI) and an organizational agreement between a producer team and its consumers. Andrew Jones, who coined the term at GoCardless in 2021, treats it as both at once; Chad Sanderson treats it primarily as an enforced technical boundary. Keep both meanings visible in the register: every entry is an agreement first and an artifact second.

## What a contract bundles

Four elements recur across every source that defines the term: **schema, quality checks, SLA, and ownership** - plus how consumers access the data. The dominant open standard is ODCS (Open Data Contract Standard, Bitol project, Linux Foundation AI & Data - descended from PayPal's internal data-contract template): one versioned YAML file covering fundamentals, schema, quality, SLA, security/stakeholders.

Adjacent mechanisms that express the same bundle: transformation-tool model contracts (enforced column types, versioned models) and schema registries for event streams. Name the bundle in the register; the specific format is the org's choice.

The RevOps ownership split around contracts (Pedowitz Group): **RevOps owns the shared models, the contracts, quality, and canonical IDs; each department owns its own domain data and usage.** Their starting artifact set is worth copying: an object dictionary, a contract library, and lineage diagrams linked directly from dashboards - so a reader traces a number to its source without asking anyone.

## The debate - state both sides in the deliverable

This is unsettled, and the deliverable must say so rather than picking a winner silently:

- **Andrew Jones** reports real success at GoCardless but frames contracts as "a big culture shift that is going to take some time," needing constant communication.
- **Chad Sanderson** - who built a contracts company - is now notably measured: "Contracts are genuinely good at one thing... They take a boundary everyone already agrees is critical and turn it into an agreement that gets enforced automatically on every change. For the handful of fields where everyone knows that if this breaks the business goes down, that is exactly the right control." He also argues producer-defined contracts fail without top-to-bottom buy-in - producers "will change contracts however they need to when shipping new features as they have no accountability for data outages downstream" - and advocates starting **consumer-defined**, as the awareness mechanism. The recurring failure he names: contracts written but not enforced, catching breakage downstream, "definitionally reactive."

The working conclusion for this skill: contracts succeed as narrow, automated circuit breakers on the handful of producer boundaries whose breakage takes down revenue reporting, and fail as a broad governance layer - the emerging consensus among the practice's own inventors. Note the conflict of interest both ways: vendors selling contract tooling have an incentive to claim broader efficacy than the evidence supports.

## Enforcement actions, weakest to strongest

1. **Consumer-defined monitoring check** - a scheduled query on the consumer side that fails loudly on drift. Cheapest; builds the awareness Sanderson says producer-side contracts need first.
2. **Scheduled contract tests** - the contract's quality checks run on a schedule against the produced data; violations page the producer's owner.
3. **CI/pre-merge validation on the producer** - contract tests fail the producer's build, comment on the offending change, and tag subscribed consumers; the strongest tools add circuit breakers. This is "shift-left": enforcement at the point of code change, not detection after breakage.

Every register entry names its rung and who acts when it fires. A contract with no enforcement action is documentation, and documentation is the documented failure mode.

## A real-world instance: usage-metering ingestion as a data contract

Unlike the illustrative composite below, this boundary is real and named. Usage-metering platforms (Orb, Metronome) document the exact contract bundle this section describes, enforced in their own ingestion API rather than proposed as a pattern: an idempotency or transaction identifier on every event (schema), ingestion-time payload and timestamp validation plus deduplication (quality), a bounded grace or resubmission window such as Metronome's 34-day correction path (SLA), and a documented void-and-regenerate procedure for invoices that finalized before a correction landed (ownership of the fix). This is rung-1/2 enforcement (see below) already running in production at the vendor layer - a producer boundary this skill would otherwise have to specify from scratch is already specified, which is worth citing to a user standing up their own usage-based billing contract register rather than reinventing the bundle.

## Worked register entry - done right

Illustrative composite; the boundary pattern is sourced, the company is not real.

```
Boundary     : billing platform -> warehouse subscription model (feeds ARR)
Producer     : billing platform integration, owned by Finance systems owner
Consumer     : analytics engineering (ARR model); downstream: exec reporting
Why critical : a schema or semantics change here silently corrupts the
               company's ARR number - the QBR test fails within one cycle
Bundle       : schema (subscription id, account alias key, plan, seat count,
               MRR amount, start/end/cancel dates); quality (no null account
               keys, amounts reconcile to invoiced totals within the agreed
               tolerance); SLA (loaded by 06:00, gaps flagged within 1h);
               ownership (producer owner named above)
Defined by   : consumer (analytics engineering) - first cycle
Enforcement  : rung 2 now (scheduled contract tests paging the producer owner);
               promote to rung 3 producer CI once the billing integration has
               a deploy pipeline the tests can gate
```

## Negative example - done wrong

> "Q3 initiative: data contracts on all 40 GTM pipelines. Each team documents its schemas in the contract template by end of month. The data team will review quarterly."

Every failure mode, in one register entry:

- Coverage is org-wide instead of critical-boundary-only, so most contracts protect nothing worth the maintenance.
- The contracts are documents with a quarterly review, not enforced checks, written but never enforced.
- Producers document their own boundaries with no consumer pull and no accountability for downstream outages.
- By the quarterly review, half the schemas have drifted, teaching everyone the register is fiction.

Forty stale contracts govern less than three enforced ones.
