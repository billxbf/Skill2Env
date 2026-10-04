# Routing detail - developer-platform-skills collection

Route only from the declared scopes below. Every "do not route here" line comes from the skill's own description, not from inference. The kickoff's own routing table states what each skill covers; this file states where each one _stops_, which is what a two-way keyword collision actually needs.

Nothing here is ranked, and nothing in it should be. Scope is a match test, not a ratio. Ranking lives in the kickoff's short-list and routine set, where several skills compete for one session (see `samber/developer-platform-skills@developer-platform-kickoff` § 4 and § 7).

Seven skills sit at macro altitude:

- `api-integration-surface-strategy`
- `api-versioning-policy`
- `sdk-portfolio-strategy`
- `developer-portal-design`
- `etl-connector-strategy`
- `integration-partnership-strategy`
- `connector-marketplace-strategy`

Each shares subject keywords with a tactical sibling and is separated from it by altitude, not by topic.

Three further pairs split by _side of the table_, where the keywords are identical and the advice inverts:

- Operator vs submitter.
- Issuer vs consumer.
- Provider vs client.

Both kinds are collected under Boundary pairs below.

## Table of Contents

- [Per-skill signals](#per-skill-signals)
- [Boundary pairs](#boundary-pairs)
- [Ordered chains](#ordered-chains)
- [Sibling-repo recommendations](#sibling-repo-recommendations)

## Per-skill signals

### `samber/developer-platform-skills@api-integration-surface-strategy`

- Route here: "which API should we build first", "should we add GraphQL or MCP", "a deal is blocked on a surface we don't have", API-first vs embedded-first sequencing.
- Do not route here: designing any chosen surface - it hands off to the per-surface sibling once the surface is picked.

### `samber/developer-platform-skills@public-api-design-review`

- Route here:
  - Audit a REST surface against design rules, bucketing findings Must-change or Improvement.
  - Stand up the review program (lifecycle triggers, reviewer authority, linting, federation).
  - "Review this API before we publish it."
- Do not route here: generating a spec or server code; error taxonomy, versioning, idempotency, auth, rate limits and docs depth each belong to a named sibling.

### `samber/developer-platform-skills@api-error-design`

- Route here: "our errors just say 400", designing the code taxonomy and the RFC 9457 envelope, making messages actionable, signalling retryability.
- Do not route here: client-side retry mechanics, whole-surface consistency review, incident or status-page communication.

### `samber/developer-platform-skills@api-idempotency-retry`

- Route here: "make POST safe to retry", "customers are double-charged", adding an `Idempotency-Key` header, writing retry guidance, setting SDK backoff defaults.
- Do not route here: what the error response signals (`api-error-design`); webhook delivery retries (`webhook-platform-design`).

### `samber/developer-platform-skills@api-rate-limit-policy`

- Route here: setting and publishing quota and burst numbers, the header family, the 429 and `Retry-After` contract, noisy-neighbour fairness, enterprise limit-increase paths.
- Do not route here: throttling infrastructure or gateway configuration; the 429 envelope shape, client backoff mechanics and deprecation machinery belong to siblings.

### `samber/developer-platform-skills@public-graphql-api-design`

- Route here: "should this be GraphQL", designing or reviewing a public schema, Relay cursor connections, error result types, depth and complexity ceilings, the federation trust boundary, persisted queries.
- Do not route here: published cost/quota policy (`api-rate-limit-policy`), deprecation and versioning policy, push-event architecture.

### `samber/developer-platform-skills@public-grpc-api-design`

- Route here: "should we expose gRPC at all", proto governance and AIP conventions, buf breaking-change gates, the `google.rpc.Status` error model, transcoding and gateway architecture, the pre-exposure audit.
- Do not route here: language-specific server implementation; internal-only gRPC, which this skill's own gate usually sends back to REST.

### `samber/developer-platform-skills@api-auth-key-management`

- Route here: key format and storage, least-privilege scoping, rotation UX, the key dashboard, offboarding, compliance lifecycle governance - and the unresolved "keys or OAuth?" question, which this skill owns.
- Do not route here:
  - Consuming another vendor's API.
  - OAuth flow design.
  - Webhook signing schemes.

### `samber/developer-platform-skills@oauth2-provider-design`

- Route here: "let third-party apps act on our users' behalf", "add Sign in with X plus delegated access", defining scopes, designing consent, setting token lifetimes, gating app publishing behind verification.
- Do not route here: integrating against someone else's OAuth; API-key design.

### `samber/developer-platform-skills@api-versioning-policy`

- Route here: picking a version scheme, writing the breaking-change definition, setting notice windows, sunset signalling and enforcement, breaking-change governance. Asks the API paradigm first - REST's version-and-sunset and GraphQL's continuous evolution are different policies.
- Do not route here: client SDK versioning, which is plain SemVer; auditing whether one surface is well-designed.

### `samber/developer-platform-skills@api-reference-quality`

- Route here: "find our undocumented endpoints", measuring docs completeness against a spec, missing examples or snippet parity, broken try-it, "stop our reference drifting" via CI lint and contract-test gates.
- Do not route here: site-wide docs information architecture, the quickstart page, sample-corpus policy, agent-facing docs - all `samber/developer-relations-skills`.

### `samber/developer-platform-skills@webhook-platform-design`

- Route here: "add webhooks to our API", event taxonomy, payload envelope and schema versioning, HMAC signing, delivery guarantees and dead-letter policy, subscription lifecycle, the consumer debugging surface.
- Do not route here: consumer-side retry mechanics, signing-key storage lifecycle, sandbox mechanics.

### `samber/developer-platform-skills@sdk-portfolio-strategy`

- Route here: "which SDK languages first", generated vs handwritten, tiering and promoting community SDKs, sunsetting a low-usage SDK, release cadence, decoupling SDK SemVer from API versioning.
- Do not route here: single-SDK ergonomics, registry publishing mechanics, whether to offer SDKs as a surface at all.

### `samber/developer-platform-skills@mcp-server-offering`

- Route here: "should we ship an MCP server", choosing which tools to expose, securing write-capable tools, versioning the tool surface, judging MCP ROI.
- Do not route here: code-generation MCP builder skills, which scaffold what this skill specifies; documenting an existing SDK for agent consumption (`samber/developer-relations-skills@coding-agent-docs-optimization`).

### `samber/developer-platform-skills@sql-jdbc-access-design`

- Route here: "offer SQL access to customers", a JDBC/ODBC endpoint, connecting customer BI tools to product data, tenant isolation, the schema-stability contract, pricing a SQL add-on.
- Do not route here: bulk file delivery (`bulk-data-sharing-design`); ETL-platform connectors (`etl-connector-strategy`).

### `samber/developer-platform-skills@bulk-data-sharing-design`

- Route here: "ship customer data as Parquet", offering a warehouse or lake share, setting an export freshness posture, partitioning and schema-evolution contracts, egress cost allocation, cross-border residency.
- Do not route here: live SQL endpoints, ETL-platform connectors, surface selection.

### `samber/developer-platform-skills@etl-connector-strategy`

- Route here: "get us listed in an ETL platform catalog", build vs partner-built for a source connector, adding CDC to a SaaS product (honestly: API sources ship pseudo-CDC, never log-based), justifying connector engineering spend.
- Do not route here: pipeline-building for data teams; the vendor's own inbound connector marketplace.

### `samber/developer-platform-skills@developer-portal-design`

- Route here: designing or restructuring a portal, console or API dashboard, cutting time to first call, deciding where each self-service surface sits, portal search, RBAC and tenancy, build vs buy.
- Do not route here: internal service catalogs; designing any individual surface the portal hosts - each has its own sibling.

### `samber/developer-platform-skills@api-test-mode-design`

- Route here: designing a sandbox or test mode, choosing the isolation model, magic test values and simulated personas, on-demand test events, reset and seeding, graduation to live.
- Do not route here: code-execution sandboxing, unit-test mocking, a marketing try-it playground, partner sandbox _provisioning timing_ (`partner-app-onboarding`).

### `samber/developer-platform-skills@integration-error-observability`

- Route here: "build a developer-facing error dashboard", exposing request logs to integrators, correlation IDs that survive into a support ticket, alerting partners when their integration breaks, "cut integration support tickets".
- Do not route here: platform-wide incident comms (`api-status-communication`), webhook delivery mechanics, the shape of a single error response.

### `samber/developer-platform-skills@api-status-communication`

- Route here: designing or auditing a status page, writing incident updates or a public postmortem, uptime and SLA reporting, announcing planned maintenance.
- Do not route here: deprecation and breaking-change notices (`api-versioning-policy`), per-integration error surfacing, webhook delivery status.

### `samber/developer-platform-skills@integration-partnership-strategy`

- Route here: picking integration partners from demand data rather than relationships, tiering partnership depth on the referral-to-OEM ladder, evaluating a certification-program join, fixing sourced-vs-influenced partner attribution, where the function reports.
- Do not route here: your own marketplace, ETL-platform listings, integration-surface choice.

### `samber/developer-platform-skills@partner-app-onboarding`

- Route here: designing or auditing the partner-developer entry flow, self-service vs application-gated registration, when sandbox tenancy is provisioned, whether certification gates submission, cutting time-to-first-submitted-app.
- Do not route here: review-gate mechanics, sandbox isolation architecture, post-launch partner tier ladders, listing content, reseller sales enablement.

### `samber/developer-platform-skills@integration-listing-optimization`

- Route here: improving your own listing's conversion or search rank on someone else's marketplace, winning installs and compliant reviews, badge pursuit, defending rank against decay.
- Do not route here: anything the marketplace _operator_ decides - standards, review, monetization, promotion.

### `samber/developer-platform-skills@connector-marketplace-strategy`

- Route here: "should we build an app store", "is our ecosystem ready", setting the take-rate _level_ and curation posture, governing third-party apps at the policy level, seeding a two-sided ecosystem from zero, build vs join vs embedded iPaaS.
- Do not route here: partner onboarding, app review, listing standards, monetization _mechanics_ - all execution siblings; being a connector on others' data platforms is `etl-connector-strategy`.

### `samber/developer-platform-skills@app-marketplace-review`

- Route here: designing the review pipeline, setting approval criteria, what re-triggers review after an update, auditing app permissions, hardening the publish channel, appeal paths, delisting and revocation policy.
- Do not route here: submitter onboarding, listing-content standards, marketplace strategy.

### `samber/developer-platform-skills@app-marketplace-listing-standards`

- Route here: defining what every listing must contain, screenshot and media requirements, the description quality bar, category taxonomy design, rejection criteria, when stale listings get downgraded or delisted.
- Do not route here: optimizing your own listing on someone else's marketplace; the security review behind admission.

### `samber/developer-platform-skills@app-marketplace-monetization-model`

- Route here: merchant-of-record posture, billing rails, the fee stack and its anti-circumvention rule, fee waivers, payout cadence and hold windows, the facilitator/VAT tax layer.
- Do not route here: the take-rate _level_ and tier structure (`connector-marketplace-strategy`); this skill designs the collection mechanics under whatever level that skill set.

### `samber/developer-platform-skills@app-marketplace-launch-marketing`

- Route here: launching a marketplace, sizing the founding cohort, coordinating the reveal and partner embargoes, featured-app and spotlight rotations, allocating MDF and per-partner co-marketing budget.
- Do not route here: a vendor optimizing its own listing on someone else's marketplace.

### `samber/developer-platform-skills@developer-platform-career`

- Route here: breaking into an API Product Manager, Platform Engineer/Architect, or Partner/Integration Engineer role, prepping a platform-engineering or API-PM interview, evaluating an offer against this track's own ladder and comp benchmark.
- Do not route here: hiring for these roles (`developer-platform-hiring`), or a developer advocate, community manager, developer educator, or DevRel-flavored DX engineer target - `samber/developer-relations-skills@devrel-career`.

### `samber/developer-platform-skills@developer-platform-hiring`

- Route here: writing a posting, building a scorecard or interview loop, sourcing candidates, or setting a compensation stance for an API Product Manager, Platform Engineer/Architect, or Partner/Integration Engineer role.
- Do not route here: candidate-side prep (`developer-platform-career`), or hiring a developer advocate, community manager, developer educator, or DevRel-flavored DX engineer - `samber/developer-relations-skills@devrel-hiring`.

### `samber/developer-platform-skills@developer-platform-kickoff`

- Route here: project start, periodic check-in, "which skill do I need", re-routing mid-project. This skill routes; it never performs a sibling's job itself.

## Boundary pairs

Where two or more siblings collide on keywords, decide from these declared-scope boundaries.

**Split by altitude.** The kickoff's altitude rule names each macro/tactical pair; these are the questions that decide them at the boundary:

- **api-integration-surface-strategy vs every per-surface skill** - "Should we add GraphQL?" → strategy. "Design our GraphQL schema" → the surface skill. A surface question arriving with no audience attached is always the strategy question in disguise.
- **api-versioning-policy vs public-api-design-review** - "What are we allowed to change?" → policy. "Is this surface well-designed?" → review. A review that finds no agreed breaking-change definition escalates up to the policy.
- **sdk-portfolio-strategy vs api-idempotency-retry** - "Which SDKs first?" → portfolio. "What should the SDK do on a 503?" → idempotency-retry.
- **developer-portal-design vs api-auth-key-management / api-test-mode-design / integration-error-observability / api-reference-quality** - "Where does the key dashboard live and what else belongs on that page?" → portal. "What does a key look like and how does rotation work?" → key management. The portal decides which self-service surfaces exist and where; each sibling designs one of them.
- **connector-marketplace-strategy vs the four app-marketplace skills** - "Should we build one?" and "what take-rate?" → strategy. "How do we collect it?" → monetization-model. "What must a listing contain?" → listing-standards. "What gets rejected?" → review. "How do we launch it?" → launch-marketing.
- **integration-partnership-strategy vs partner-app-onboarding / etl-connector-strategy / integration-listing-optimization** - "Which partners matter?" → strategy. "How does a partner get from signup to first app?" → onboarding. "How do we get listed on their ETL catalog?" → etl-connector-strategy. "Why is our listing not converting?" → listing-optimization.

**Split by side of the table:**

- **integration-listing-optimization vs app-marketplace-listing-standards / app-marketplace-launch-marketing** - same words, opposite chairs. You are the submitter optimizing a listing you own on a marketplace you don't → listing-optimization. You are the operator writing the rules and promoting the catalog → standards and launch-marketing. Ask which side of the review gate the user sits on before routing any "marketplace listing" question.
- **api-auth-key-management vs oauth2-provider-design** - both are credentials you issue, split by whose data the caller acts on. The customer's own backend calling your API on its own behalf → API keys. A third-party app acting on your _users'_ behalf, needing consent → OAuth. Key management owns the decision boundary itself, so an unresolved "keys or OAuth?" starts there.
- **webhook-platform-design vs api-idempotency-retry** - both concern retries, split by direction. You delivering events to a consumer, with your retry schedule and dead-letter policy → webhook-platform-design. A client retrying its call into you, with idempotency keys and backoff → idempotency-retry.

**Split by scope of the audience:**

- **api-error-design vs integration-error-observability vs api-status-communication** - three altitudes of "something failed":
  - One response body an integrator receives → api-error-design. "Our error messages are useless" routes here.
  - One integration's history, aggregated and replayable, visible to the integrator who built it → integration-error-observability. "Partners don't know their integration is broken" routes here.
  - The whole platform's health, visible to everyone at once → api-status-communication. "Customers didn't know we were down" routes here.
- **sql-jdbc-access-design vs bulk-data-sharing-design vs etl-connector-strategy** - three ways to give customers the data, split by who runs the pipe:
  - You expose a live queryable endpoint or share → SQL/JDBC.
  - You deliver files or a lake share on a cadence → bulk sharing.
  - A third-party ETL platform pulls from your API on the customer's behalf → etl-connector-strategy.

  Scan frequency and freshness expectations decide between the first two; who the customer already pays decides the third.

- **api-rate-limit-policy vs public-graphql-api-design** - GraphQL's depth and complexity ceilings are schema design decisions and live with the schema; the published quota, tier numbers, headers and 429 contract are policy and live with rate-limit-policy. A GraphQL cost model needs both, in that order.
- **partner-app-onboarding vs app-marketplace-review vs api-test-mode-design** - three stages of the same partner's path:
  - Getting to a first submission → onboarding.
  - What happens to that submission → review.
  - How the sandbox they build in is actually isolated → test-mode-design.

## Ordered chains

Propose a chain only when the task genuinely decomposes this way; never fabricate a sequence. Each chain is listed in dependency order, not efficiency order - a later link consumes what the earlier one produces, so there is no ratio to rank.

- `api-integration-surface-strategy` → the chosen surface skill → `api-versioning-policy` - decide which surface, design it, then commit to what you will and won't break in it. Publish before the promise exists and every later change is negotiated case by case.
- `public-api-design-review` → `api-error-design` → `api-idempotency-retry` → `api-reference-quality` - audit, fix the error contract the audit exposed, make failing calls safe to retry, then document. Documenting first just freezes the flaws in prose.
- `api-auth-key-management` → `api-rate-limit-policy` → `integration-error-observability` - you cannot meter or attribute what you cannot identify; the identity issued first is what limits key on and what error rates split by.
- `oauth2-provider-design` → `partner-app-onboarding` → `app-marketplace-review` - apps need delegated auth before a partner journey means anything, and a journey before there are submissions to review.
- `connector-marketplace-strategy` → `app-marketplace-listing-standards` → `app-marketplace-review` → `app-marketplace-monetization-model` → `app-marketplace-launch-marketing` - settle whether and at what curation level, write what a listing must contain, define what gets rejected, wire up collection, then launch. Launching first means grandfathering every early listing.
- `developer-portal-design` → `api-test-mode-design` → `api-reference-quality` - the portal decides which self-service surfaces exist and where; the sandbox and the reference each land in a slot it already reserved.
- `integration-partnership-strategy` → `etl-connector-strategy` or `integration-listing-optimization` - the prioritization decides which platform is worth the connector or listing. Building either first pays a maintenance tax for a platform nobody's customers use.
- `webhook-platform-design` → `integration-error-observability` - delivery logs and replay are the debugging surface for the deliveries the first link creates.

## Sibling-repo recommendations

`developer-platform-skills` owns the _platform surface_: the API and its lifecycle, the integration surfaces around it, the portal, and the partner and marketplace ecosystem. Two sibling `samber` collections cover adjacent ground this collection intentionally excludes. Recommend installing the sibling instead of stretching a task onto a skill above that doesn't cover it; never frame it as a dependency - this collection stays fully usable standalone.

### `samber/developer-relations-skills` - DevRel practice

Recommend the sibling repo, not a skill above, when the task is:

- Site-wide docs information architecture, rather than endpoint-level reference completeness → `samber/developer-relations-skills@developer-docs-structure-audit`.
- The quickstart page and its first-run narrative → `samber/developer-relations-skills@developer-quickstart-guide`.
- Making an existing SDK, API or protocol consumable by a coding agent unattended → `samber/developer-relations-skills@coding-agent-docs-optimization`. Distinct from `mcp-server-offering`, which builds a _new_ agent-facing tool surface rather than documenting an existing one.
- Whether to evolve from product to platform at all, and how far up the openness ladder → `samber/developer-relations-skills@developer-ecosystem-strategy`. Upstream of `connector-marketplace-strategy`: the ecosystem question is "should we be a platform", the marketplace question is "should we run a catalog".
- The devtools revenue model, or what to open-source → `samber/developer-relations-skills@devtools-business-model`, `samber/developer-relations-skills@oss-distribution-strategy`.
- Anything else in the DevRel practice - developer content and SEO, community, events, open-source program operations. Start at `samber/developer-relations-skills@developer-relations-kickoff` when the boundary is unclear.

Distinguish from this collection: `developer-platform-skills` owns what the platform _is_ and what integrating with it costs; `developer-relations-skills` owns how developers hear about it, learn it, and stay. "Design our webhook platform" stays here; "write the tutorial that teaches it" goes to the sibling.

**Career and hiring split by what the role is screened on, not by the word "platform" in a title.** `developer-platform-career`/`-hiring` cover API Product Manager, Platform Engineer/Architect, and Partner/Integration Engineer - roles screened on API and system design judgment as a primary skill. `samber/developer-relations-skills@devrel-career`/`devrel-hiring` cover developer advocate, community manager, developer educator, and DevRel's own DX-engineer flavor - roles screened on communication and community craft. A "platform engineer" title is doubly ambiguous on top of this split: it can also mean internal developer platforms (Kubernetes, Backstage, golden paths), a population neither pair of skills covers - see `developer-platform-career`'s own disambiguation step before routing any "platform engineer" hiring or career task.

### `samber/dev-event-organizer-skills` - technical event operations

Recommend the sibling repo when the task is running a conference, hackathon, meetup or developer event as an _event_ - venue, sponsorship, CFP, speakers, budget, logistics - rather than as a DevRel program. A marketplace launch keynote is `app-marketplace-launch-marketing` here; producing the conference the keynote happens at is the sibling repo.

Coverage gaps this collection does not fill at all - per-marketplace submission playbooks, package-registry publishing mechanics, API changelog automation, federated-graph offerings, API monetization, connector certification programs, and deployed-integration health monitoring - are listed with their boundaries in `samber/developer-platform-skills@developer-platform-kickoff` § 8. Name the gap from there; never promise a skill exists.
