# Portal component checklist and design notes

Vendor names below are citations and integration notes, never requirements - every pattern is achievable on whichever platform the team runs.

## Core component set

The consolidation payoff (DigitalAPI's framing): without a portal, teams stitch together a docs tool, a key-management spreadsheet, a sandbox, a ticket queue, and a finance handoff. The portal connects discovery, testing, access, subscriptions, and analytics in one surface.

- API catalog (with search - for multi-gateway orgs, a gateway-agnostic catalog auto-synced from each gateway's admin API avoids a fragmented per-gateway experience)
- Authentication and self-service key management
- Interactive documentation (reference generated from the spec, try-it console on the endpoint page)
- Sandbox / test-mode entry with a visible test-vs-live toggle
- Usage dashboards, quota visibility, and overage alerts per developer
- Governance controls: RBAC, approval flows, quotas
- Changelog / release notes, status-page link, support escalation path (the maintained-platform trust signals)
- Billing and plan management when the API is monetized

**The dividing line between a docs site and a portal is the self-service credential lifecycle**: sign up, create, rotate, and revoke keys without filing a ticket. Some documentation-focused products deliberately stop short of this - if the product being designed has no credential lifecycle, it is a documentation site, and this skill's portal-level advice applies only partially.

## Self-service credential lifecycle - UX patterns (lifecycle UX only, key mechanics belong to the auth sibling skill)

- **Scoping at creation**: let the creator pick restricted, least-privilege permissions when the key is created, not afterwards (Stripe's restricted keys are the reference implementation).
- **Test and live keys as parallel pairs** on one dashboard with a mode toggle, prefixed so environment is readable from the key itself.
- **Zero-downtime rotation via an overlap window**: old and new keys both work during a bounded transition (Stripe allows up to 7 days, practitioner guidance is a few hours), so migration is gradual. Immediate expiration is reserved for confirmed compromise. Key names persist across rotation.
- **Expiration chosen at creation** with org-level maximum-lifetime policies (GitHub's fine-grained tokens are the reference: expiration is mandatory at creation, admins can cap lifetimes, tokens unused for a year are auto-removed, and "never used" is surfaced as a deletion signal).
- **Audit hygiene**: show last-used timestamps. Flag or limit long-unused keys with a dashboard restore path.
- **Programmatic lifecycle events**: webhooks notifying integrating apps of rotation and expiration, where the platform supports it.

## Try-it console requirements

- Native integration on the endpoint page - never a separate tool the developer must leave the docs to open.
- Auto-populated auth: the signed-in developer's own key injected into the console and into every code snippet.
- Multi-language, copy-paste-and-run code samples generated from the spec.
- Docs kept in sync with the spec via automation. A hand-maintained parallel copy will drift.
- Realistic environment handling: the console targets the sandbox by default, with the mode toggle visible.

Integration note - the console tool landscape, roughly ascending in interactivity and cost:

- Spec-rendered consoles you host yourself: Swagger UI, Scalar (adds polish and multi-language snippet generation), Stoplight Elements (embeds in an existing shell).
- Read-only three-panel references: open-source Redoc, no live runner.
- Hosted developer hubs with credential-injected explorers and per-developer request logs: ReadMe, Mintlify.
- Collection-based interop: Postman collections as a de-facto import/export standard, forkable via public workspaces.

## RBAC and tenancy patterns

- Two-level hierarchy is the prevailing model: Organization → Project/Workspace (OpenAI, Kong Konnect). Keys, files, and usage scope to the project.
- Roles bundle permissions (Owner/Admin/Member/Viewer tiers). Groups of users can be synced from an identity provider via SCIM for enterprise tenants.
- Partner-portal specifics: approval-gated signup (configurable), team-owned and team-shared applications, viewer-vs-consumer role split (may view the catalog vs may register and hold credentials), page-level visibility permissions, one API publishable to several portals under centralized RBAC.
- Environment separation (dev/staging/prod or test/live) as a first-class concept on every credential, log, and usage surface.

## Search and AI assistant pattern

The recurring implementation across vendors:

- An "Ask AI" widget co-located with the search box.
- Natural-language input.
- Answers grounded in the docs with inline citations linking to source pages.
- An explicit "I don't know" fallback instead of guessing.
- Analytics surfacing unanswered and low-confidence questions as a documentation backlog.

A deflection maturity ladder (DevRev's framing - vendor-sourced, use for orientation only):

- Static FAQ and keyword search: roughly 10-20% of tickets.
- Rule-based bots: 30-50%.
- Conversational RAG assistants: higher still.

Third-party and vendor estimates place RAG doc-assistant deflection broadly at 20-40%. All of these are vendor-reported - validate against your own pre-assistant ticket baseline.

Integration note - assistant vendors in current use:

- Docs platforms with built-in assistants and `llms.txt`/MCP generation: Mintlify.
- Search-native generative layers: Algolia AskAI.
- Purpose-built RAG answer engines deployable as widget, in-app chat, community bot, or API: kapa.ai, Inkeep.

## Build-vs-buy platform categories

Integration note only - the decision logic lives in the SKILL.md workflow:

- **Gateway-bundled portals**: developer portals shipped as part of an API management platform. Best when the org already runs, or is choosing, that gateway.
  - Kong Konnect Dev Portal.
  - Google Apigee's integrated portal, with a CMS-based Drupal distribution as its customizable variant.
  - Zuplo, which bundles a portal on every tier including free.
- **Hosted docs/developer-hub platforms**: ReadMe, Mintlify, Fern and peers - strong on docs, try-it, and AI assistance. Credential lifecycle depth varies, sometimes composed with the gateway.
- **CMS-based custom portals**: built on a CMS so business-side authors get real authoring workflows while engineers push specs via CI/CD (the pattern Pronovix builds on Drupal). This is the custom-build path - it requires a funded, permanent owner.
- **Internal-portal frameworks (excluded)**: Backstage-class frameworks are for internal service catalogs. Their threat model assumes no untrusted external access, standing one up takes months of platform-team work, and the community consensus is not to build an external portal on one. If the org uses one internally, pair it with a separate external portal rather than exposing it.

Third-party pricing figures for these platforms circulate widely but mostly originate from competing vendors. Treat any specific contract number as unofficial and re-verify with the vendor at decision time.
