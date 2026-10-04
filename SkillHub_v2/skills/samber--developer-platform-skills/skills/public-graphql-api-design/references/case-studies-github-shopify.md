# Case studies: GitHub and Shopify

Two large, long-running, publicly documented production GraphQL APIs - cite these by name instead of inventing hypotheticals. Sources: GitHub Docs (global node IDs and migration guides), Shopify's `graphql-design-tutorial` and developer platform docs.

## GitHub: one identity system across REST and GraphQL

GitHub's REST API exposes a `node_id` on most objects; the same identifier is the `id` field on GraphQL's `Node` interface. The documented workflow: fetch an object via REST, take its `node_id`, and hand it straight to a GraphQL `node(id: ...)` lookup - one ID space serving both APIs, so clients mix surfaces freely. GitHub treats `Node` as its foundational abstraction: "a generic term for an object" reachable by direct lookup or via a connection.

Use this as the worked example whenever the interview says a REST surface coexists (clarifying question 3).

## GitHub: shrinking an ID migration's blast radius

GitHub needed a new global-ID encoding for consistent response-time performance. Instead of a deadline-driven forced migration, it shipped an `X-Github-Next-Global-ID` request header: `1` always returns the new format, `0` returns legacy-or-new depending on the object's creation date.

The key design decision: **any consumer who never stored a global ID anywhere needed no changes at all.** The migration's blast radius shrank by construction to only the clients that had persisted IDs.

Cite this when a schema-evolution discussion needs an ID-format-change precedent: the discipline is "minimize what a breaking change actually breaks," applied to identifiers.

## Shopify: mutation design rules from production

From `graphql-design-tutorial`, distilled from years of production schema evolution:

- **Focused business-action mutations** over one monolithic update: `publishPost`, `cancelOrder`, each with a tightly scoped input and payload.
- **Rule #22** - keep the selection argument (which object) separate from the change-data argument (what changes); a merged input with a nullable `id` blurs filter and target.
- **Rule #24** - mutation payload fields are mostly nullable "unless there is really a value to return in every possible error case"; an all-non-null payload can't represent partial failure.
- **Rule #8** - object references, never ID fields: `author: User!`, not `authorId: ID!`.
- **Rule #9** - name fields for the client's mental model, not the legacy API or the data store.
- **Noun-first mutation naming** (`userCreate`) - deliberately inverted from Apollo's verb-first so a type's mutations group together under alphabetical tooling.
- The tutorial's own reasoning for nullable payloads states that GraphQL's built-in query-level errors are a poor fit for business-level mutation failure - independent corroboration of the union-result-type default.

## Shopify: admission control and cost weighting

Shopify's platform statically analyzes each query's cost **before executing it** - an over-budget query is rejected without doing any work. Clients accrue 50 points/second up to a 1,000-point cap, and **mutations are weighted at 10x** a read of equivalent shape. The design lessons that transfer (the scoring mechanics themselves belong to `samber/developer-platform-skills@api-rate-limit-policy`):

- Check ceilings pre-execution - admission control, not post-hoc billing.
- Price mutations far above reads.
- Expose the computed cost back to the caller so integrators self-regulate instead of discovering ceilings through rejections.

## Shopify: the versioned-GraphQL counter-example

GraphQL's philosophy says continuous evolution, no versions - Shopify versions anyway. Its GraphQL Admin API ships quarterly date-based versions (`YYYY-01`, `YYYY-04`, `YYYY-07`, `YYYY-10`), each supported at least 12 months, and as of 2026 new public app-store submissions **must** use the GraphQL Admin API while the REST Admin API is legacy-only.

Cite this whenever someone claims GraphQL means you don't need a version: paradigm does not dictate versioning policy - Shopify chose one unified date-versioning story across both API surfaces. The policy side lives with `samber/developer-platform-skills@api-versioning-policy`.
