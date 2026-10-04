# Platform programs for source-connector vendors

Snapshot dated 2026-08-30. Programs, gates, and tier names change; re-verify against each platform's current partner documentation before committing to a path.

## Fivetran (curated archetype - gatekeeps entry)

| Path                  | Status                                 | Who builds/maintains                                                                                                             | Gate                                                                                                                                                                                                             | Notes                                                                                                                                                                                                             |
| --------------------- | -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Partner-Built program | **Closed to new source partners**      | Vendor builds on Fivetran's partner SDK; support triaged by root cause                                                           | Manual code review (repo access, "allow up to a week")                                                                                                                                                           | Remains documented for destination connectors only. Live Partner-Built sources are few and database-leaning (Convex, Datastreamer, PlanetScale, SingleStore, Tracksuit) - it was a narrow track before it closed. |
| Connector SDK         | **Active - the live self-build path**  | Vendor writes a Python connector (`fivetran-connector-sdk`, gRPC-based); listed as a "community connector" alongside native ones | Standard listing, no badge                                                                                                                                                                                       | Ships templates and a mock/local test environment - build and validate without a live Fivetran account. Actively maintained; 100+ community connectors already listed.                                            |
| By Request (Lite)     | **Active - the platform-managed path** | Fivetran builds and maintains                                                                                                    | Six phases (submission, validation, consultation, development, rollout); "two to eight weeks" of initial API-documentation analysis; **can reject**: "if the source is not a great candidate… the process stops" | Advertised turnaround as fast as 30 days once accepted. Fits "SaaS APIs that produce a non-dynamic schema"; dynamic/custom schemas get steered to the SDK.                                                        |

Release-phase clock, all paths: in-dev (hidden) → Private Preview → Beta → GA, with a hard rule that source connectors "must be promoted to Beta within six months of entering Private Preview." Support splits by root cause, not badge: Fivetran fixes Fivetran-side issues; partner-side issues go to the partner, at the partner's own SLA.

## Airbyte (open-contribution archetype - gatekeeps labels)

Three build tiers, least to most code - reach is roughly flat across them (listing never requires certification); the real limit is how much of the API's quirks the declarative layer can express before forcing a move up:

1. **No-code Connector Builder**: UI-driven; one-click "Contribute to Marketplace" opens the submission PR directly.
2. **Low-code declarative manifest**: YAML-like spec on the Python CDK for streams/pagination/auth; no Python for most sources. Centralizes shared logic (cursor handling, resumable refresh) so fixes ship once for every connector built on it.
3. **Full CDK** (Python; community-maintained Java/TypeScript): for sources too custom for the manifest. Starts as a GitHub discussion so design conflicts surface before code.

Quality tiers:

- **Marketplace inclusion**: pass the standard test suite, get merged. Deliberately a low bar: certification would add "a barrier to entry" the platform doesn't want on every contribution.
- **Airbyte Certified**: optional, earned. Principles:
  - Reliability and usability beat feature count - "one solid connector is better than two finicky ones."
  - Fail fast and actionably - never accept a configuration guaranteed to break.
  - Every supported sync mode integration-tested.
  - Incremental sync wherever the source allows.
- **Partner Certified**: _destination connectors only_, the closest analog to Fivetran's closed badge. Quantitative bars:
  - ≥95% first-sync success.
  - ≥95% overall sync success.
  - ≤3-business-day first response.
  - Connector updated at least every 6 months.

Support taxonomy, four levels:

- **Airbyte (Certified)**: platform-built, covered by Airbyte's support SLAs.
- **Enterprise**: Airbyte-built premium connectors (SAP/Oracle/Workday/NetSuite-class).
- **Marketplace**: community-maintained, "not covered by Airbyte support SLAs… may experience backward-incompatible, breaking changes with no notice."
- **Custom**: build-your-own, workspace-exclusive.

The trade this buys: a much larger catalog (600+ advertised) than a curated one, at variable maturity.

## Singer / Stitch / Meltano (open-spec ecosystem - no gate, no floor)

- **Singer** (2017, StitchData): open tap/target spec over stdin/stdout newline-JSON - minimal by design, which enabled a large uncoordinated ecosystem. Stitch open-sourced the _spec_ to crowdsource coverage but withheld the _operational_ tooling (orchestration, state, monitoring), so community taps still needed a paid Stitch subscription to run reliably.
- **Meltano** (GitLab-born) filled the withheld layer as open source, plus a Singer SDK scaffolding spec-compliant taps and MeltanoHub as the catalog (200+ taps/targets).
- **Decay record**: the cautionary case for any custom-path plan, after Stitch's acquisition:
  - Community investment dropped.
  - Each tap is an independent project with no enforced quality bar - "you never know the quality of a tap until you've used it."
  - Most see multiple breaking upstream changes a year, and many go unmaintained.

  Even Meltano's docs warn the "benevolent community member" model "is great in the short-term, but… individuals may not always be able to maintain a connector."

- Stitch itself layers the same certified-vs-community split all three ecosystems converged on:
  - **Certified** taps are commercially supported - "a guarantee that the Stitch team will fix bugs and adapt to new versions of third-party APIs."
  - **Community** taps get commercial support only under an Enterprise contract.

When this path is worth it anyway: a strategic customer segment already composes open-spec stacks the commercial platforms don't reach, and the vendor commits a named owner - the decay record is what happens without one.

## Choosing between them

Match the platform to interview answer 2 (where customers' stacks run), not to a platform-quality league table. Where evidence is split, the archetype difference decides:

- The curated platform's gate buys a stronger quality signal at the risk of rejection and no control.
- The open platform guarantees presence but makes the certified tier the actual differentiator.
- The open-spec ecosystem is presence-of-last-resort with the maintenance obligation fully internalized.
