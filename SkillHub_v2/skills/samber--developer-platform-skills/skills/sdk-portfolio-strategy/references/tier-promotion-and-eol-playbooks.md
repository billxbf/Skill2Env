# Tier frameworks, promotion gates, and EOL playbooks

Named, citable frameworks for step 3 (tiers and promotion) and step 6 (deprecation and EOL) of the workflow.

## Tier frameworks

**Two-tier (official + community) - the simplest documented norm.**

- Stripe: "Stripe-maintained SDKs are available for Ruby, PHP, Java, Python, Node, .NET and Go. Community libraries are also available for other server languages."
- Twilio, on its community tier: "these libraries are not supported by Twilio, and we can't speak to their accuracy/completeness."
- Plaid: "community libraries are not officially supported by Plaid… Plaid cannot… guarantee that they will be kept up-to-date."

Copy the structure: an official tier with a support commitment, a community tier with an explicit non-guarantee, support routed to the community repo.

**MCP's SDK Tiering System** (modelcontextprotocol.io/community/sdk-tiers) - the cleanest numbered ladder:

- Tier 1: fully supported, with complete protocol implementation and all non-experimental features.
- Tier 2: actively maintained, still working toward full spec support.
- Tier 3: experimental, partial, or specialized.

Tiering is by implementation completeness, never by feature ambition - experimental features are required at no tier.

**Azure - tier 1 names concrete languages.** Azure's SDK policy requires a GA library to "support all four tier-1 languages (.NET, Java, Python, TypeScript) unless there is a good (and documented) reason to not include support for one." Its beta gate is four checkable requirements:

- At least 2 languages (one statically typed, one dynamically typed).
- A beta available for at least one month.
- No known critical bugs.
- Three reference customers external to the Azure organization.

Post-GA states: Active (minimum 12 months) and Deprecated (critical-fixes-only for at least 12 months, or 3 years if the deprecation involves breaking changes).

**Google Cloud - quality level encoded in the version and package metadata**, not a separate policy page.

- GA requires version ≥1.0 plus the `"Development Status :: 5 - Production/Stable"` classifier.
- Beta and Alpha use the corresponding classifiers.
- Alpha/Preview carries an explicit warning that libraries can "get deprecated and deleted before ever being promoted."

Most Google Cloud libraries are auto-generated (GAPIC). The hand-maintained minority is identifiable by an `.OwlBot.yaml` file, a mechanical way to audit generated-vs-handwritten in an existing portfolio.

Google Cloud Looker's support policy gives the checkable community-status criteria: an SDK stays community when it:

- Lacks required features.
- Lacks support/automation infrastructure (automated testing, packaging, docs, examples).
- Is built on deprecated technology.
- Hasn't been tested by enough distinct users.

## The promotion gate - one documented case, the rest inferred

**Anthropic's Ruby SDK (the Alex Rudall case) is the only cleanly documented community-to-official promotion on record.** The canonical `anthropic` RubyGem name belonged to Rudall's community library. When Anthropic shipped its official Ruby SDK (beta ~April 2025, `anthropics/anthropic-sdk-ruby`), Rudall donated the gem name and renamed his project to `ruby-anthropic`.

Anthropic's official README credits him: "Thank you @alexrudall for giving feedback, donating the anthropic Ruby Gem name, and paving the way by building the first Anthropic Ruby SDK." The mechanism promotion actually turned on the maintainer's willingness to transfer the canonical package namespace, plus vendor support commitment - not a vendor decision alone.

Other commonly-cited "promotions" (DigitalOcean's `godo`, Stripe's `stripe-go`) are now official, but no announcement documents a formal promotion event for either. A fuller promotion rubric spans sustained usage/download volume, feature completeness (auth, pagination, retries), maintainer cooperation on namespace, and a vendor support commitment. Write this explicitly into your own policy rather than pointing to any published checklist.

## AWS's five-phase SDK lifecycle

Per docs.aws.amazon.com/sdkref/latest/guide/maint-policy.html, each major SDK version moves through:

- **Phase 0 - Developer Preview**: not supported, not for production, breaking changes expected.
- **Phase 1 - General Availability**: fully supported; AWS commits to "at least 24 months" of GA support - the floor to cite when asked how soon an SDK can be deprecated.
- **Phase 2 - Maintenance Announcement**: public announcement at least 6 months before maintenance mode, typically timed with the next major version's GA so users get a migration target on day one of the notice.
- **Phase 3 - Maintenance**: critical bug fixes and security issues only. No API updates. **Internal inconsistency to cite honestly:** the core SDKs-and-Tools policy defaults this phase to 12 months, while AWS's own Powertools docs state a 6-month default - the two AWS policies genuinely differ by product line, so never quote "AWS's policy" as one number without naming which document.
- **Phase 4 - End-of-Support**: no further releases; published packages remain on registries, the repo may be archived.

Communication mechanism: a pinned GitHub RFC issue plus updates to reference docs, guides, marketing pages, and READMEs. AWS also ties dependency support to a mechanical downstream rule worth copying: support ends 6 months after the community or vendor ends support for that dependency.

Worked timelines:

- AWS SDK for JavaScript v2: maintenance announced Sept 8, 2024, end-of-support Sept 8, 2025 (the 12-month default).
- AWS SDK for Java v1.x: maintenance July 31, 2024, end-of-support Dec 31, 2025.
- AWS SDK for .NET v3: maintenance March 1, 2026, end-of-support June 1, 2026, only a 3-month window, proof the default flexes per product line.

## Sentry's three-phase full-SDK EOL playbook

Sentry's published playbook (develop.sentry.dev, "Deprecating an SDK") is the most rigorous public evidence-gated process, written in RFC-2119 MUST/SHOULD terms:

**Phase 1 - Build the case, before any announcement.**

- Document upstream platform health ("Has the platform reached end of life?").
- Gather usage data (orgs, projects actively using the SDK).
- Pull download trends from the language's own registry analytics (npmtrends, PyPI Stats, NuGet, Maven Central).
- Quantify revenue at risk by isolating "orgs that use the SDK exclusively (no other Sentry SDKs) - this is the true at-risk segment."

Document opportunity cost against higher-growth SDKs, identify migration paths, and record engineering-manager approval in the team tracker. This is the sourced answer to "what data justifies killing a low-usage SDK."

**Phase 2 - Execute, order matters:** "cut the final release before announcing, and announce before archiving." Steps in order:

1. Final release pinned to up-to-date dependencies.
2. Pinned GitHub deprecation issue stating why, alternatives, and remaining timeline.
3. Backlog closed with uniform messaging.
4. A prominent README notice naming successor SDKs.
5. Docs-site warning banners.
6. Registry deprecation marker.
7. Repo archived.
8. Support and GTM teams notified.

High-impact deprecations should also get a blog post.

**Phase 3 - Post-EOL cleanup, 6-12 months after archival:** de-index retired docs but keep them reachable at their direct URLs (don't 404), and redirect to the successor SDK's docs.

Documented executions, each naming a specific successor:

- `sentry-cordova` archived March 2026 (users routed to Capacitor/React Native/Flutter SDKs).
- `sentry-xamarin` archived after Xamarin's own end-of-life (routed to `sentry-dotnet` via .NET MAUI).

## Other citable sunset floors

- **Stripe, language-runtime deprecation** (a separate axis from API deprecation): when a language runtime reaches its own end of life, Stripe marks it deprecated and runs an extended support window of 1 to 2 years depending on the language, pre-announced in docs, READMEs, and changelogs. Documented example: Python 2.7 support dropped at `stripe-python` 6.0.0.
- **Azure:** 12 months of critical fixes minimum after deprecation, 3 years if breaking changes are involved. For a tiny remaining user base, Azure's guidance is white-glove: "consider working with them individually to migrate" instead of a blanket timeline.
- **Google Cloud:** Preview/Alpha libraries carry no promotion guarantee at all and can be deleted before ever reaching GA, the harshest documented policy. Make sure your own alpha tier says which model it follows.

**Six-step sunset sequence** - gathered from AWS, Sentry, Stripe, and Azure practices:

1. Gather usage and revenue-at-risk evidence per Sentry's exclusive-user model.
2. Confirm a migration path exists.
3. Announce with a fixed timeline - 6 to 24 months is the observed range.
4. Cut a clean final release.
5. Mark the package deprecated on its registry.
6. Archive only after the announced window closes.

Write this as your own policy when you adopt it.
