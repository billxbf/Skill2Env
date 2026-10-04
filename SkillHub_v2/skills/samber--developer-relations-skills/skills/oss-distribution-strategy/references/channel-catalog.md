# Channel catalog

Eleven families of ongoing distribution channel. Widen the outer ring with this, then rank candidates with the adoption test (recurring cost, decay behaviour, observable signal, kill date).

Registry policies, marketplace terms and list rules change without notice - verify on the surface's own documentation before planning around any detail here.

The numbering is a table of contents, not a ranking. The efficiency order, the per-axis breakdown, the ties, what that order starves and the conditions that reorder it all live in SKILL.md step 2; do not re-derive an order from these section numbers.

---

## 1. Registry presence and metadata

**What it is** - the project's page on each registry it publishes to, and the fields that page renders. It rewards findability inside the registry's own search and legibility for the evaluator landing there; the registry page, not the repository, is where most library evaluations start.

**Mechanics worth knowing**

- npm ranks search on title, description, readme and `keywords` only - no popularity/quality signal, just spam and new-package deprioritization; downloads and dependents are user-chosen sort options. New packages take up to two weeks to appear. Wording is the whole lever.
- crates.io caps `keywords` at 5 (20 ASCII chars each) and `categories` at 5, from the fixed slug list at `crates.io/category_slugs`; `description` is required plain text, `documentation` falls back to docs.rs.
- pkg.go.dev surfaces best-practice signals - `go.mod`, a detected redistributable license, a tagged version, a stable v1+ - and generates docs from exported-symbol comments, so those comments are the marketing copy.
- Other registries (PyPI classifiers, container verified-publisher tiers, chart and module registries) expose their own subset - confirm before planning.

- **Cost** - an hour to fix, minutes per release to keep.
- **Decay** - silent but harmful: a description written before the rewrite misleads every visitor.
- **Signal** - registry downloads, registry-referred sessions.
- **Traps**:
  - Empty keyword slots.
  - A description in the project's invented vocabulary instead of the problem's.
  - Missing link fields (docs, repository, funding).
  - Placeholder packages claimed in registries the project doesn't ship to, which read as abandonware.

## 2. Code-host discovery surfaces

**What it is** - the forge's own discovery mechanics, tended on a recurring cadence rather than spiked at launch: topic and collection pages, trending, repository search metadata, the social preview image, Discussions, the releases feed, sponsor and org profiles.

**Mechanics worth knowing**

- GitHub topics and collections are community-curated through pull requests to `github/explore`: a folder named for the URL slug, an `index.md`, and where applicable a 288×288px PNG under 75KB. **Self-promotion is explicitly disallowed** - the PR template requires attesting the submitter is neither sole author of the entry nor an employee of the company behind it. Merges go live on a delay, and tagging a repository with a topic does not surface it until the topic itself is curated.
- Trending has no published specification; the star-velocity explanation is folklore. GitHub's public events firehose stopped emitting most star, PR and issue events, which broke third-party star-based rankings; OSSInsight withdrew its trending feature rather than publish numbers it could no longer trust. Treat external trending tools as unreliable.

- **Cost** - low per surface, but the curation route requires finding an advocate.
- **Decay** - slow and mostly silent; a stale social preview or an abandoned Discussions tab is a mild negative.
- **Signal** - referrals from topic pages, repository visitor sources.
- **Traps** - self-submitting a topic entry and getting the PR closed; treating a trending appearance as a channel rather than a byproduct.

## 3. Curated lists and directories

**What it is** - awesome-lists, ecosystem showcases, category directories, comparison sites. It rewards inclusion in lists a real audience browses, with durable long-tail arrivals rather than a spike.

**Mechanics worth knowing**

- The `sindresorhus/awesome` rules sub-lists inherit in spirit: 30+ days old before submitting upward, passes `awesome-lint`, not AI-generated, carries a Contents table, `contributing.md`, the awesome badge and a Creative Commons license (CC0 recommended). Entries take one fixed shape, `- [Name](URL#readme) - Description.` The bar is explicitly "the best, not everything", excluding unmaintained, archived or thinly documented projects by policy.
- For any target list, read its `contributing.md` and last merged PRs, match the entry format exactly, place it in the right section. Format failures are rejected before the project is judged.
- Contributing first - dead-link fixes, other projects, section improvements - improves the reception of a later self-submission and costs less than it.
- Wait for independent usage before submitting - real stars, issues opened by strangers, an outside contributor - not the week it ships. "The best, not everything" is judged against comparable already-listed projects, and a zero-traction repo reads as unproven no matter how well the entry is formatted.

**Selection test** - do target developers browse it; is the link dofollow on a domain with real authority; was the list touched recently; are comparable projects listed; can arrivals be measured.

- **Cost** - 30-60 minutes per submission, plus a sweep every quarter.
- **Decay** - actively harmful: dead links, old screenshots, superseded names.
- **Signal** - referral arrivals per listing.
- **Traps**:
  - Generic directories that accept anything.
  - Abandoned lists.
  - Paid placement with no visible audience.
  - One description reused verbatim everywhere.
  - Submitting a brand-new, zero-traction project - rejected on the "best, not everything" policy even when the PR itself is well-formed.

## 4. Downstream packaging and mirrors

**What it is** - system package managers, distribution repositories, container and chart registries, corporate artifact proxies, regional mirrors, community forks. It rewards being installable with the command the user already types, inside networks the maintainer cannot reach directly.

**Mechanics worth knowing**

- Homebrew's `homebrew-core`, at last check, requires an upstream-declared stable version with an immutable tag or release verified by SHA-256, forbids downstream-only patches, and pushes binary-only proprietary software to a cask. Historic numeric notability thresholds are no longer stated - read the current policy rather than repeating folklore.
- The fallback below that bar is a self-owned tap/PPA/COPR/overlay: instant and fully controlled, but a far weaker discovery surface - nobody browses a private tap.
- Packagers adopt what is cheap to package: immutable release tarballs with checksums, semantic versions, no build-time network fetches, a documented build, a clear license, a predictable cadence.
- Repology tracks 300+ repository families (325k+ projects, 4.9M+ package entries) and shows which carry a current or outdated version - including copies the maintainer never knew existed.

- **Cost** - high to enter (policy, review, packaging), low to hold if upstream release hygiene is good.
- **Decay** - harmful and partly outside the maintainer's control: users judge the project on a version shipped a year ago.
- **Signal** - repositories carrying a current version; support questions naming a distro package.
- **Traps** - treating someone else's package as owned; letting a fork or regional mirror become the de-facto install and quietly capture the project's users and bug reports.

## 5. Extension and plugin marketplaces

**What it is** - editor, IDE, browser and app-host stores: browsed inside a tool's UI, gated by a review the maintainer does not control, ranked by mostly undocumented mechanics.

**Mechanics worth knowing**

- **VS Code Marketplace** - ranks on installs, ratings, categories (criticized as not install-weighted); verified-publisher setup, no heavy manual gate; largest reach but **no first-party install-stats dashboard**.
- **Open VSX** (Eclipse Foundation) - ranks on downloads, same extension format; 256 MB binary limit, CI-publishable; the default store for Cursor, Windsurf, VSCodium, Gitpod.
- **JetBrains Marketplace** - ratings, reviews, downloads; manual review normally 2 business days with **no guaranteed SLA**; `since-build`/`until-build` ranges are the recurring tax.
- **Chrome Web Store** - engagement and ratings, Manifest V3 required, variable review latency, strictest rules: build for Chrome first and port down. **Firefox AMO / Edge Add-ons** use similar signals and are author-managed; Firefox's different MV3 stance makes porting a real decision.
- **PR-gated app stores** - Obsidian community plugins (PR to `obsidian-releases`, automated scan then manual review, auto-updates from releases) and the Raycast Store (community-manager approval; PRs go stale after 14 days, closed after 21).

**The Open VSX decision.** Microsoft's marketplace terms restrict use to Microsoft in-scope products, so every VS Code fork is contractually barred from it. Cursor migrated to Open VSX in mid-2025 and proxies search itself. A Microsoft-only extension is invisible to the AI-first editor segment - dual-publish from day one.

- **Cost** - listing metadata plus per-store review latency and version-compatibility maintenance.
- **Decay** - harmful: an extension incompatible with the host's current version reads as broken.
- **Signal** - installs per store, ratings, compatibility coverage.
- **Traps** - assuming one store covers the audience; ignoring compatibility ranges until users file the issue.

## 6. The release stream

**What it is** - tags, releases and changelogs as a recurring broadcast to people who already know the project. Recipients and cadence rules: SKILL.md step 6.

**Branch mechanics** - long-term-support or maintenance branches are what conservative company adopters need before committing; pre-release channels serve early adopters without destabilizing the default install.

- **Cost** - release hygiene the project should have anyway, plus writing notes.
- **Decay** - a silence is read as abandonment even by a finished, stable project; the cheap correction is an explicit "stable, maintained, low change rate" statement.
- **Signal** - downstream bot PRs merged, release-page views, version adoption spread.
- **Traps** - cadence theater (dependency bumps announced as features, version inflation); releases with unreadable or absent notes, which waste the broadcast.

## 7. Integration and dependency-graph surface

**What it is** - being reachable from software the user already runs: adapters for adjacent frameworks, first-class support inside a popular host, official examples in someone else's docs, a direct or transitive dependency of a widely used project. It rewards inherited distribution - one adapter inside a popular framework can outperform every listing combined, because it puts the project on the default path instead of a page someone must find.

**Mechanics worth knowing**

- deps.dev (Google Open Source Insights) computes transitive graphs and inverse dependent sets across Go, Maven, PyPI, npm, Cargo and NuGet, with full dependent sets queryable via BigQuery. Complementary: the code host's dependency graph and "used by" badge, Libraries.io, Ecosyste.ms. Closed-source usage is invisible to all of them by deps.dev's own caveat, so a low public dependents count is not evidence of low adoption.
- Only 27.5% of npm packages are depended on by any other package (Wittern et al., MSR 2016). Entering that depended-upon core is a structural advantage, and it is the only family that keeps generating discovery with zero recurring maintenance once earned - it decays only if the hub project is replaced.

**How it is pursued** - find the highest fan-in hub projects in the niche, target adoption or a first-class adapter with each, contribute upstream where the host accepts it, and ask satisfied users who already wrote glue code to upstream it.

**The attribution trade-off** - transitive dependents deliver usage without mindshare; a developer three layers downstream may never learn the name. Counter with a "used by" wall, restrained runtime or console attribution, case studies naming downstream adopters. High fan-in with low visibility also produces outsized issue load.

- **Cost** - high and recurring per integration; near zero to hold a dependency position once earned.
- **Decay** - harmful for adapters, negligible for dependency position.
- **Signal** - dependents count, arrivals referred by the host project's docs.
- **Traps** - building integrations for hosts with no shared audience; unbounded adapter sprawl a solo maintainer cannot keep green.

## 8. Recurring creator and newsletter seeding

**What it is** - the ongoing relationship with 3-5 newsletter curators and podcast hosts, distinct from the launch pitch: embargoed news, major-version demos and case studies on a calendar, keeping the project in front of the audience between launches.

**Mechanics worth knowing**

- The channel is concentrated. Newsletters: Cooperpress (JavaScript Weekly - 179,077 subscribers per its Q3 2024 media kit - Golang Weekly, Node Weekly, Ruby Weekly, Frontend Focus, React Status), plus TLDR, Bytes, Python Weekly, Console.dev, Changelog News, This Week in Rust. Podcasts: Changelog, Software Engineering Daily, Syntax, JS Party, Go Time, Rustacean Station, Talk Python.
- Curators hand-write descriptions and state "signal over noise" as the editorial bar. Editorial picks and paid sponsorship slots are structurally different purchases and must be labelled differently.
- What gets sent matters: an embargo, a live demo, a sandbox or a sample repo - never an announcement with no way to try the thing.

- **Cost** - the highest recurring cost of any family here, and relationship work that cannot be handed to whoever is free.
- **Decay** - the relationship decays, not the artifact.
- **Signal** - newsletter signups and monthly active developers as leading indicators, paired with an activation metric such as time to first successful use.
- **Traps** - conflating sponsored placement with earned coverage, burning a relationship that took years to build; pitching per release instead of on a quarterly calendar.

## 9. Trust and procurement signals

**What it is** - signed releases, build provenance, published SBOMs, a documented disclosure path, an automated supply-chain score. Levers: Sigstore/cosign keyless signing, SLSA provenance, npm provenance attestations, SPDX or CycloneDX SBOMs, the OpenSSF Scorecard's 18+ checks producing a 0-10 score. It rewards clearing procurement, not getting discovered: artifact proxies and allowlists gate what developers can pull at all, review boards validate an SBOM against a baseline, and Scorecard data surfaces inside dependency-review tooling and deps.dev.

**The honest framing** - the link from these signals to downloads or adoption is unestablished; independent sampling found low provenance uptake, Sigstore's totals have no control group, and download counts are gamed. Present this as risk mitigation and procurement enablement, never a download lift.

**Regulatory context** - EU CRA reporting obligations begin September 2026, SBOM technical documentation is enforceable from December 2027, both binding manufacturers rather than upstream maintainers. Expect pressure as fix requests from downstream companies, not direct liability.

- **Cost** - a concentrated one-time setup, then a monthly score check and a per-release SBOM.
- **Decay** - a lapsed signing pipeline fails builds downstream, so it is harmful.
- **Signal** - score above 7 with green attestations; enterprise evaluations that stop stalling.
- **Traps** - treating it as a growth channel; taking on certification-shaped obligations a volunteer project cannot sustain. Funding predicts posture more than intent: paid maintainers publish signed releases with provenance at 50% vs 28% for unpaid ones (Tidelift 2024).

## 10. Machine and agent-readable surfaces

**What it is** - the project as consumed by search engines, answer engines and coding agents rather than a browsing human: structured docs, machine-readable indexes and specs, canonical error strings, accurate metadata everywhere the ecosystem is scraped. It rewards recommendation by the tools developers now ask first - a project whose docs an agent can parse, with an unambiguous install path, gets suggested with correct code; one understandable only by reading a blog post does not.

- **Cost** - mostly documentation work already justified on its own.
- **Decay** - slow.
- **Signal** - arrivals from answer engines where distinguishable; correctness of the code snippets tools produce when asked about the project.
- **Traps** - treating this as a keyword game. The underlying work is unambiguous naming, complete runnable examples and versioned docs, covered by this collection's documentation skills - decide here that the family is in scope, execute it there.

## 11. Artifact and connector hubs

**What it is** - hubs where the unit of distribution is an artifact or connector inside someone else's product: model and dataset hubs, data-connector marketplaces, infrastructure module registries, observability plugin catalogs, automation-node directories, rule and policy registries.

**Why it is not family 5** - the host is a data or infrastructure platform, the reviewer is the platform vendor, and inclusion is usually a PR against the vendor's index repository or a naming convention its crawler matches, not a store upload. The evaluator also sees a support tier next to the entry, which no editor store shows.

**Mechanics worth knowing** (verified against vendor documentation on 2026-08-28; all change without notice)

- **Index-repo hub** (dbt Package Hub) - `dbt-labs/hubcap` runs hourly over the repos in `hub.json`; listing means a PR adding the repo, reviewed by a dbt Labs maintainer. Requires GitHub hosting, `dbt_project.yml` with a `name`, semver release tags (`0.1.0` or `v0.1.0`).
- **Naming-convention hub** (Terraform Registry) - public GitHub repo named `terraform-<PROVIDER>-<NAME>`, standard module structure, semver tags with optional `v` prefix (non-version tags ignored). The **repo description becomes the module's short description**; new versions appear about a minute after a tag push.
- **Tiered-support hub** (Airbyte) - four levels: Airbyte-maintained, Enterprise, Marketplace, Custom. A community connector lands in Marketplace, listed and installable but labelled "not maintained by Airbyte" with no support SLA - and that label is part of what the evaluator reads.
- **License-gated catalog** (Grafana plugins) - public Git repo, mandatory cryptographic signing, license from AGPL-3.0, Apache-2.0, BSD, GPL-3.0, LGPL-3.0 or MIT. Grafana Labs declines forks or duplicates of existing plugins, several plugins bundled as one, environment-specific designs and niche use cases.

**Downloads do not mean here what they mean on a language registry.** Hugging Face counts every `GET`/`HEAD` on a per-library set of query files - `config.json` by default, overridden per library in the open-source `model-libraries.ts` list, plus every `.gguf` file - so a clone inflates the number and a cached pipeline run does not appear. Deduplicated request-level data is a paid publisher-analytics feature. Read each hub's counting documentation before comparing its number to anything.

- **Cost** - a concentrated entry cost (naming, structure, signing, review), then a per-release compatibility tax against the host's version.
- **Decay** - harmful: a connector broken on the host's current version reads as abandoned inside a product the user is paying for.
- **Signal** - installs or pulls per hub, support-tier label, issues from users who name the host product rather than the project.
- **Traps**:
  - Entering a hub whose support tier advertises the project as unsupported when the goal was company adoption.
  - Renaming a repository after listing, which silently breaks a naming-convention hub.
  - Assuming the hub's download number is comparable to a registry's.
