# Vendor Case Studies and Pricing Precedents

Named implementations, one candid post-mortem, and the shipped pricing shapes. Figures may be dated; verify current pricing and product status before quoting any of them to a customer. Vendor-vs-vendor comparison claims are marketing, not neutral fact - weight the mechanics, not the adjectives.

## Architecture trade-off summary

| Dimension           | Zero-copy sharing                      | Replicated copy / read endpoint | Per-tenant compute isolation       |
| ------------------- | -------------------------------------- | ------------------------------- | ---------------------------------- |
| Storage cost        | Lowest (no copies)                     | Highest (N copies)              | Shared storage, dedicated compute  |
| Query cost          | Per-query scan (+ cross-region egress) | Prepaid at refresh              | Per-tenant metered compute         |
| Freshness           | Live                                   | Stale to last refresh           | Live                               |
| Noisy-neighbor risk | Depends on consumer compute            | Isolated by copy                | Eliminated by design               |
| Governance          | Centralized at source                  | Duplicated PII surface          | Centralized data, isolated compute |

The tipping rule between the first two columns is scan frequency (Alex Merced's heuristic, one practitioner's rule of thumb: ~20 scans/day on a ~200 GB table makes live re-scanning cost more per month than a replica costs per year). Even Databricks' own docs concede replication is sometimes the cost-efficient choice.

## Platform mechanics

- **Snowflake Secure Data Sharing**: shares are named objects wrapping tables, secure views, and secure UDFs; sharing happens through the metadata layer, so no data is copied and shared data occupies no consumer storage.
  - Full-account consumers pay their own compute.
  - Non-Snowflake consumers get a **reader account** - and reader-account warehouses can consume unlimited credits billed to the _provider_ unless a resource monitor caps them. That default is the sharpest cost exposure of the whole pattern.
- **Databricks Delta Sharing**: an open REST protocol, not proprietary - Databricks-to-Databricks mode plus open sharing for non-Databricks clients (Power BI, Tableau, Spark, pandas) via pre-signed URLs. Governance centralizes in Unity Catalog; auth supports bearer tokens or OIDC federation (no shared secret at all). Provider pays cross-region egress on consumer reads, which scales with consumer query volume; backing the share with an egress-free object store eliminates that line item.
- **BigQuery sharing (Analytics Hub)**: publishers create exchanges holding listings; subscribers get an opaque, read-only linked dataset inside their own project and VPC perimeter. A restricted-egress mode blocks subscribers from exporting shared data out of that dataset entirely. Providers meter usage through the `SCHEMATA_LINK` `INFORMATION_SCHEMA` view - a concrete usage-metering hook.
- **MotherDuck Hypertenancy** (the hosted per-tenant-compute reference): every user, service account, or agent gets a dedicated single-node engine instance with its own CPU/memory/spill that spins up on first query and scales to zero - per-tenant isolation and per-user billing by construction, with read-scaling replica pools for read-heavy tenants. Named production adopter: Together AI chose it as an analytics serving layer explicitly because agent-driven queries on a compute-heavy shared warehouse "would create a serious cost problem" (their Director of Data Engineering, quoted by MotherDuck - vendor-published, weight accordingly).
- **Iceberg REST Catalog** (the vendor-neutral layer under several of the above): an OpenAPI-specified metadata API any compliant client can read; supports credential vending and OAuth2. Caveat: the spec is intentionally silent on performance, so two compliant catalogs can differ by orders of magnitude in response time.

Named adopter of consumer-pays sharing: **HubSpot** ships a native Snowflake Data Share gated to its top data tier, read-only, with the customer explicitly responsible for all Snowflake compute costs incurred reading it.

## PostHog - the strongest documented failure case

PostHog's 2026 engineering post-mortem on rebuilding its data warehouse is first-party, dated, and unusually candid; treat it as the primary failure-mode citation.

- On exposing the shared multi-tenant ClickHouse cluster via SQL: "The prospect of an unbounded number of queries hitting our very not elastic CH cluster is basically untenable and would eventually cause problems across our entire application."
- On isolation: "We simply could not expose direct connections to the Clickhouse cluster without deepening the challenges of multitenancy. On top of that, our query language HogQL is not a language that's already widely supported." Two distinct lessons in one quote: shared-cluster blast radius, and the custom-dialect connectivity tax.
- A third, subtler failure mode - engine drift breaking untested customer query shapes: "We've seen ClickHouse change query results between releases, or based on which settings were enabled. Our test suite catches this for our own queries, but we can't test every shape of customer data and query a warehouse needs to handle." A vendor's regression suite covers its own known queries, never the combinatorial space of arbitrary customer SQL.
- Their fix targets all three at once: single-tenant embedded engine instances per organization, fronted by a Postgres wire-protocol endpoint so standard BI tools and `psql` connect with no custom driver.
- A mundane ongoing cost from their handbook, independent of architecture: external SQL connections fail without specific client drivers installed - recurring first-line support, forever.

## Amplitude - a full product lifecycle as a maintenance-cost signal

Amplitude shipped direct customer SQL access as per-customer dedicated Redshift clusters ("Amplitude Query"), then rebuilt as "Warehouse-native Amplitude" translating chart analyses into SQL running inside the _customer's own_ warehouse - with query optimization at scale as the stated engineering challenge. Warehouse-native is now marked a legacy feature not offered to new customers in Amplitude's own docs.

Read the arc as evidence that a warehouse-native SQL surface costs more to _maintain_ than to build - but don't overstate a specific cause: the deprecation reason isn't independently documented beyond the legacy marking. Separately, Amplitude's additive-only event schema (tables and columns only ever added as new event types arrive) is the shipped existence proof for step 4's contract.

## Pricing precedents

| Vendor / product                        | Shape                             | Mechanics (point-in-time)                                                                                                                                                                                                                                                                                                                                                                                                            |
| --------------------------------------- | --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Stripe Sigma                            | Consumption / volume-tiered       | Read-only SQL environment inside the Stripe Dashboard, tiered on monthly charge volume (roughly $10-15/mo up to 250 charges, ~$450/mo up to 25,000, per-charge overage above); queries themselves unlimited and unmetered; 30-day trial; annual-only above the entry tier. Repriced 2025-09-30 from a per-charge + flat infrastructure fee model - a live example of a vendor changing its SQL-access pricing metric after shipping. |
| Heap Connect                            | Flat tier gate                    | Direct SQL warehouse access gated behind higher plan tiers; free once the tier is bought - the lever is the gate, not usage.                                                                                                                                                                                                                                                                                                         |
| Mixpanel Data Pipelines                 | Flat add-on                       | Sold as an add-on package on top of Growth/Enterprise plans.                                                                                                                                                                                                                                                                                                                                                                         |
| Amplitude Query                         | Flat add-on (dedicated infra)     | Historically bundled SQL access via a dedicated per-customer Redshift cluster - the true "external driver handle" precedent, later superseded (see lifecycle above).                                                                                                                                                                                                                                                                 |
| Snowflake reader accounts / Marketplace | Provider-pays-compute passthrough | Provider pays reader-account compute and invoices separately; paid marketplace listings support per-query pricing and per-active-month pricing, with the payout rail handled by the marketplace.                                                                                                                                                                                                                                     |
| HubSpot Data Share                      | Consumer-pays, tier-gated         | Snowflake share at the top data tier; customer pays all Snowflake compute for reads.                                                                                                                                                                                                                                                                                                                                                 |

How to weight them: Stripe Sigma is a query-inside-the-vendor's-UI feature, not an external driver handle - the strongest evidence that customers _pay_ for SQL access, not of what external JDBC access looks like. Heap Connect and Amplitude Query hand out real connection strings - the strongest evidence for the external-driver shape. All figures came from vendor pricing pages and docs.

## Why this is a category - analyst framing

a16z's data-infrastructure architecture work describes application developers building on the clean, joined data already in the warehouse/lakehouse, with traditional enterprise systems being rebuilt "warehouse-native" and OLAP integration becoming a critical component of application development. Use it as the "why now" narrative; it is analyst framing, not evidence for any implementation detail. Snowflake's own marketing pitches the same monetization angle from the vendor side - embedded live analytics as a new value stream - which is a vendor's sales claim, cited here only to show the platform vendors are actively courting this pattern.
