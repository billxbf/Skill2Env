# Sources behind this skill's claims

Every named practice, figure and threshold in this skill traces to one of the entries below. Anything not traceable here is labelled in place as a self-set baseline. Cite these when a colleague asks why the guide is shaped this way - an argument from a published policy ends faster than an argument from taste.

## Guide anatomy and per-change entries

- **React 19 upgrade guide** (react.dev, 2024) - section order (installing, codemods, breaking changes, new deprecations, notable changes, TypeScript changes, changelog), the "upgrade to React 18.3 first to help identify any issues" staged-path instruction, the all-changes codemod recipe, and the explicit statement that the recipe "does not include the TypeScript changes".
- **Prisma v7 upgrade material** - priority tags per change group so a reader triages before reading, a version-to-version comparison table as the scanning surface, runtime and language floors stated before any code change, troubleshooting keyed by error text, and routing an unsupported path out (stay on the old major) instead of half-supporting it.
- **Stripe upgrade documentation** - date-based named versions, the published exhaustive list of changes considered backward-compatible, per-request version pinning for testing before the account default moves, and the separate versioning tracks for server SDK, browser bundle, mobile SDK and webhooks.

## Deprecation policy

- **Django deprecation timeline** - deprecated in N, still working in N+1, removed in N+2 (roughly 12-18 months); the timeline document organised by removal version; security items labelled as an accelerated timeframe rather than silently accelerated.
- **Node.js deprecation levels** - the four-rung ladder (documentation-only, application, runtime, end-of-life), the `DEP0XXX` stable identifiers with per-version history, and the rule that deprecations can be revoked without the identifier being reused.
- **Ember deprecation guides** - every deprecation carries an `until` version and a stable ID so lint rules and tooling can reference one deprecation rather than a document URL.
- **PEP 387** (Python backwards-compatibility policy) - a documented deprecation process with warnings and a removal target before a break lands.

## Ownership and internal gates

- **Ember RFC process** - originated the "How we teach this" required RFC section; the Recommended stage requires the feature to be integrated into the guides and the API documentation polished before the RFC completes.
- **Rust RFC 1636** ("document_all_features") - copied that gate explicitly: stabilization must not proceed until the How We Teach This requirements are fulfilled. A later Rust internals thread admits the changelog half "has not ever been done" - evidence that docs gates need enforcement, not just wording.
- **Kubernetes KEP template** - required `Upgrade / Downgrade Strategy` and `Version Skew Strategy` sections plus a Production Readiness Review; the enhancements freeze removes an incomplete KEP from the release.
- **Technical Writer HQ** - migration guides described as content senior writers inherit, because they are high-risk, cross-team, and "can break production if misunderstood".

## Support windows and version skew

- **Kubernetes version-skew policy** - three most recent minor releases maintained; documented skew limits between components force a staged upgrade order and forbid direct multi-minor jumps. AKS documents the fallout for clusters that violate skew.
- **Node.js release policy** - even-numbered majors historically got 18 months Active LTS plus 12 months Maintenance; from v27 every major becomes LTS after a Current phase. Published as a machine-readable schedule file the tooling ecosystem reads.
- **PostgreSQL versioning policy** - each major supported for five years after initial release, with cross-major upgrade tooling that can bridge several majors in one hop.
- **endoflife.date** - community-run aggregator of EOL dates with an API, consumed by CI and compliance checks.

## Validation

- **`cargo test --doc` and `mdbook test`** (Rust) - code blocks in docs and books compiled and run by the build.
- **Software Engineering at Google, chapter 22** - the Rosie platform "takes a large change and shards it based upon project boundaries and ownership rules into changes that can be submitted atomically"; Chromium's own large-scale-change workflow is the comparable public case.

## Named laws and methods

- **The Churn Rule** - Software Engineering at Google, chapter 1: "infrastructure teams must do the work to move their internal users to new versions themselves or do the update in place, in backward-compatible fashion. This policy, which we've called the 'Churn Rule', scales better." Google adopted it in 2012 after finding that announcing a delete date and pushing migration work onto customers fails as the dependency graph grows.
- **Hyrum's Law** (hyrumslaw.com) - "With a sufficient number of users of an API, it does not matter what you promise in the contract: all observable behaviors of your system will be depended on by somebody."
- **Diátaxis** - the four-mode documentation compass; a migration guide is a how-to (goal-oriented, assumes competence, teaches nothing).
- **Expand/contract**, also called parallel change - the additive-then-destructive schema migration pattern implemented by Postgres and MySQL online schema-change tooling.

## Adoption figures

- **Chrome Manifest V3** - Google blog, May 2024: over 85% of actively maintained extensions on V3, after the December 2022 pause and the republished timeline. A 93% figure attributed to a Google spokesperson in 2025 press coverage is a press quote rather than a Google publication - quote the 85% instead.
- **Kubernetes in production** - Datadog Security Labs, data as of October 2025: 78% of hosts on mainstream-supported versions, 19% extended, 3% unsupported.
- **React** - State of React 2024 and 2025 (Devographics): React 18.x around 78% of version-question respondents in 2024; React 19 around 48% versus React 18 around 41% in 2025.
- **Python 2 sunset** - Python Software Foundation: January 1 2020, with 2.7.18 released April 2020, after the original 2015 target was extended once.
