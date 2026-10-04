# Extraction-readiness checklist and the honest-CDC ladder

## The extraction-friendly API checklist

Audit every resource in connector scope against these properties. Each one holds on every build path - platform-managed, vendor-SDK, or custom - and for every customer pipeline hand-rolled against the raw API, which is why fixing the API precedes building any connector.

1. **Cursor-based pagination over offset-based.** An opaque, stable cursor eliminates duplicate/missed records under concurrent writes; offsets shift under insert/delete mid-scan. Time-window pagination (start/end timestamp) is the fallback, with the caveat that records sharing a timestamp can duplicate.
2. **A cursor or timestamp guaranteed stable across syncs**, so a connector checkpoints it and resumes exactly where it stopped instead of re-scanning from zero. This single property is what makes incremental sync possible at all - and it is what platform certification bars like "supports incremental sync wherever possible" implicitly grade.
3. **An explicit overlap/reconciliation story for soft-incremental sources.** Where no hard guarantee exists:
   - Persist the last cursor.
   - Re-query a small overlap window.
   - Upsert by stable key so the overlap can't duplicate.
   - Pair with periodic full reconciliation to catch what incremental structurally misses.
4. **Purpose-built bulk/incremental export endpoints, separate from real-time CRUD.** A dedicated "records changed since <cursor>" endpoint - instead of the same paginated endpoint the human UI uses - is the unlock vendors point to for reliable sync. It matters most at first sync: paginated-REST-only backfill is slow and rate-limit-prone; a bulk/async export job backfills once, then hands off to incremental.
5. **Webhooks as a freshness supplement, never a backfill substitute.** Push events cut polling lag for event-shaped data, but the platform-side limitation is stated plainly: webhooks cannot sync historical data - nothing before the connection date is captured. The working pattern is both: webhooks for freshness, a polling/bulk path for backfill and reconciliation.
6. **Rate-limit signaling a connector acts on programmatically:**
   - Standard 429 with `Retry-After`.
   - Where feasible, a 304/not-modified path for polled endpoints that doesn't spend rate-limit budget - connectors poll far more predictably and frequently than interactive clients.
7. **An explicit delete/change signal** - the single most common gap. The platform-side default is blunt: most application APIs don't return deletes as changes, so deletes go undetected and uncaptured. Even sources that expose one have limits - a soft-delete endpoint that stops answering after a hard-delete window loses records permanently. A durable "changes/deletes since <cursor>" feed is the concrete, buildable upgrade over a bare soft-delete flag.
8. **A documented per-resource extraction contract**, instead of leaving connector authors to guess:
   - Which strategy each endpoint actually supports (incremental vs full snapshot).
   - Expected volumes.
   - Whether hard deletes matter.
   - Freshness expectations.
9. **Versioning discipline that assumes connectors aren't watching the changelog.** 87.3% of breaking-change API versions industry-wide ship with no deprecation notice (ICSME 2020, n=1,068 specs). Version the API, publish deprecation/sunset dates, add fields additively, never silently rename or remove. A citable policy shape: date-based versioning where the previous version stays supported for at least 24 more months after a new one ships.

Grade each resource pass/fail per item; a resource that can't pass gets an explicit exclusion note in the strategy document, never a silent skip.

## Why a SaaS source never gets true CDC

"CDC support" as an ETL-platform feature means **log-based CDC**: reading the database's own transaction log (Postgres WAL, MySQL binlog, Oracle redo, SQL Server CDC tables) to reconstruct every insert/update/delete with minimal overhead and near-real-time latency - Debezium being the reference implementation.

A SaaS vendor offering itself as a source connector **cannot use this mechanism**: log-based CDC requires access to the internal transaction log of the system being read, which an external ETL platform - or the vendor's own public API surface - by definition does not have for a multi-tenant SaaS backing database. This is a structural boundary, not a maturity gap. The platforms' own CDC tooling applies log-based CDC only to databases customers point them at directly; every SaaS application source in their catalogs runs API polling.

The platforms say so themselves, under the CDC label: "for most application connectors, Fivetran performs a change data capture (CDC) strategy… based on a last modified date column. Because Fivetran does not receive every change to a row, but only the deltas… Fivetran supports a model of **Eventual Consistency**" (default 6-hour sync). A practitioner essay names the industry-wide pattern: connector platforms are, at bottom, "**pseudo-CDC**: change data capture reconstructed from webhooks and polled list APIs, one bespoke connector at a time."

## The honest substitute ladder, in order of completeness

1. **Timestamp/cursor incremental polling** via the API's own fields (`updated_at`, a stable cursor) - the practical default the checklist above exists to support. Structural weaknesses: changes made and overwritten within one poll interval are invisible; hard deletes are undetectable without a deletion feed.
2. **Webhooks as a push supplement** - genuinely closer to CDC's latency profile, but only as complete as the event catalog, and never a backfill.
3. **A vendor-side change/deletion feed endpoint** - the closest a SaaS gets to log-based completeness: implement internal CDC yourself and republish it as a stable, versioned API contract. Build it when customers report missed deletes or missed rapid updates, and treat it as the upgrade path from bare polling.
4. **Periodic full re-import reconciliation** - a backstop, not a strategy: platforms re-import certain tables specifically because deletes can't be captured from them, accepting a full re-scan to catch what incremental misses.

## Wording for customer-facing material

- Say "incremental sync" or "eventual-consistency extraction"; never an unqualified "CDC support" checkbox next to database sources whose CDC is log-based.
- State the sync/poll interval and name what the model misses: intra-interval overwrites, and hard deletes wherever no deletion feed exists.
- If the deletion feed ships later, announce it as the completeness upgrade it is - that framing is credible precisely because the earlier language didn't overclaim.
