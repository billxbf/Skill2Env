# Row-Level-Security Failure-Mode Catalog

The concrete implementation layer under step 3's "enforce isolation in the engine". Postgres-family mechanics first, then the cloud-warehouse equivalents, then the cross-engine anti-pattern checklist. Work through the failure modes _before_ writing policies - each one is cheap to prevent and expensive to discover in production.

## The core principle

RLS is the last line of defense, not the only one. Policies decide which _rows_ a role may see after the engine has already allowed the SQL operation - RLS does not itself grant SELECT/INSERT/UPDATE/DELETE, so matching `GRANT`s are still required. Decide the operation surface and column exposure per table first; RLS answers "which rows", privileges and column grants answer "which operations and fields".

For an _external_ SQL handle specifically, engine-level enforcement is mandatory rather than best-practice: the tenant holds a live query connection, so there is no application layer left to intercept a query that forgot its filter.

## Postgres RLS failure modes, ranked by severity

1. **Infinite policy recursion (critical - crashes the server).** A helper function called from a policy on table A queries table B, whose own policy calls back into a function touching table A; the recursion exhausts memory. Fix: any helper function invoked from inside a policy must be `SECURITY DEFINER` with `SET search_path = pg_catalog, public, pg_temp` pinned, so it bypasses RLS on the tables it reads and breaks the cycle.
2. **Missing `WITH CHECK`.** `USING` filters reads; `WITH CHECK` validates writes. A policy with only `USING` lets a tenant insert or update rows it cannot read back - for example rows attributed to a _different_ tenant. Every write-path policy needs both clauses.
3. **Permissive policies compound with OR.** Multiple policies on one table combine with OR, so a single `USING (true)` policy silently defeats every stricter policy beside it. Audit all of a table's policies together, never one at a time.
4. **View bypass.** Views run with their creator's privileges by default, so an owner-privileged view over an RLS table leaks every row regardless of caller. Fix: `WITH (security_invoker = true)` (PostgreSQL 15+) so the view respects the caller's own RLS.

Two configuration traps that sit beside the four:

- **Enable is not enough - FORCE it.** Without `ALTER TABLE ... FORCE ROW LEVEL SECURITY`, the table's owner role bypasses RLS entirely, defeating isolation for anything that runs elevated (admin tooling, migrations, background jobs) against tenant tables.
- **Inject tenant identity server-side.** Extract the tenant ID from a verified session token and set it in the database session context before any query runs on that connection; the policy reads the session-context value. A policy that reads a client-supplied parameter is tenant-ID tampering waiting to happen.

## Performance rules

A slow policy gets "temporarily" disabled under load pressure - which is how a correctness control becomes an outage story. Keep policies fast by design:

- Index every column a policy predicate references (`tenant_id` first of all).
- Wrap per-row function calls in a subquery: `USING (tenant_id = (SELECT auth_tenant_id()))` evaluates once per query; the bare call form evaluates once per row and is measurably slower at scale.
- Denormalize the tenant identifier onto child tables rather than resolving it through a join at query time.
- Use `SECURITY DEFINER` helper functions for cross-table membership checks, avoiding RLS-on-RLS chains - for speed, not only for recursion safety.

Protected fields (`tenant_id`, `owner_id`, role, billing status) need a `BEFORE UPDATE` trigger comparing `OLD`/`NEW` - RLS predicates cannot see the previous row value, so RLS alone cannot stop a tenant rewriting its own `tenant_id`. And expose narrow views or functions projecting only safe columns instead of widening a base table's grants to serve a "public" read case.

## Cloud-warehouse equivalents

A reader coming from Postgres will assume `USING`/`WITH CHECK` policies are the only primitive. The warehouses solve the same problem with a different one - and it has its own trap:

- **Snowflake**: a secure view joins the private base table to a private entitlement table on `sd.access_id = sa.access_id AND sa.snowflake_account = current_account()`; only the secure view enters the share. **`CURRENT_ROLE()` and `CURRENT_USER()` return `NULL` inside a secure view shared to another account** - `CURRENT_ACCOUNT()` is the only safe identity primitive across a share, and the same NULL trap applies to row-access policies (`IS_DATABASE_ROLE_IN_SESSION()` is the row-access-policy equivalent). Snowflake's `SIMULATED_DATA_SHARING_CONSUMER` session parameter exists precisely to test a share's isolation as if querying from the consumer side before granting access - use it as the probe mechanism for the isolation gate.
- **Databricks Delta Sharing**: a dynamic view filtered on `current_recipient('property')`, with properties set per recipient on the share. Recipient-property _partition filtering_ is documented as a best-effort optimization, not an access-control feature - hard isolation comes only from the view predicate.
- The lesson is identical across engines: Postgres RLS says "never rely on the WHERE clause alone", and the warehouse version is "never rely on partition pruning or session-role functions across a share".

## Multi-tenant anti-pattern checklist

Adapted from OWASP's multi-tenant guidance; each line is an audit finding for a customer-facing surface:

- Sequential or guessable tenant/resource IDs (enables cross-tenant enumeration).
- Any query path that skips the tenant filter - including "internal" or admin callers - without an explicit, audited override path.
- Tenant data stored without a `tenant_id` column, even on tables that feel single-tenant today.
- Credentials shared across tenants.
- "Internal service" treated as exempt from tenant validation.

## Known scaling trap: schema-per-tenant

Schema-per-tenant looks like easy isolation and stands up quickly, but connection pooling and DDL migrations commonly break down past a few hundred tenants, forcing a disruptive mid-flight re-architecture. Treat it as a failure mode to warn about, not a default to recommend at any real scale - the architecture menu in SKILL.md step 2 covers the rungs that do scale.
