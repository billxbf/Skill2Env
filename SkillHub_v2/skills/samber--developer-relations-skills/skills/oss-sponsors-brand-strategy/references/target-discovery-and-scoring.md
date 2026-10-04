# Target discovery, verification and scoring

How to turn a company's stack into a ranked, verified sponsorship shortlist. Endpoints and manifest paths move, so confirm each one against the registry's current documentation.

## Contents

- Measurement rules
- Step A - resolve the dependency graph
- Step B - map packages to repositories and maintainers
- Step C - pull health and criticality signals
- Step D - find and verify funding destinations
- Step E - collect reach signals (manual)
- Scoring rubric
- Worked shortlist
- The same shortlist done badly
- Disqualifiers

## Measurement rules

Every row of a shortlist is a claim about somebody else's project, published with money attached. Four rules keep it honest, each one a failure that hand-collected dependency lists produce.

- **Measure, do not estimate.** Maintainer counts, download volume and staleness all have APIs. Hand-collected figures have reported five-plus maintainers for a package whose registry publish rights list one, and zero downloads for a package moving 164 million a week.
- **Repository contributors are a different population from publish rights.** Fragility depends on who can ship a release, not on who has ever merged a commit.
- **Unassessable is not clean.** Every candidate resolves to assessed-fine, assessed-flagged, or not-assessable-because-X. Registries differ in what they expose; some ecosystems publish no maintainer list at all.
- **Carry the denominator.** "412 of 470 dependencies resolved; 58 had no source repository" is the honest form of any coverage percentage, and the form that survives an audit.
- **Quote figures verbatim** from whatever produced them. Rounding a scorecard number or a download count breaks reproducibility for no gain.

## Step A - resolve the dependency graph

Prefer the company's own SBOM or lockfiles when they exist; they describe what actually ships. Otherwise resolve from the published package.

A public resolution API returns a full tree - direct and transitive - in one call:

```
https://api.deps.dev/v3/systems/{ECOSYSTEM}/packages/{PACKAGE}/versions/{VERSION}:dependencies
```

`ECOSYSTEM` covers npm, PyPI, Cargo, Go, RubyGems, Maven and NuGet. Each returned node carries `versionKey.name`, `versionKey.version` and `relation` (`SELF`, `DIRECT`, `INDIRECT`). Percent-encode package names: `@scope/pkg` → `%40scope%2Fpkg`.

For an application that publishes no package, read the manifest directly and resolve each declared dependency.

## Step B - map packages to repositories and maintainers

```
https://api.deps.dev/v3/systems/{ECOSYSTEM}/packages/{NAME}/versions/{VERSION}
```

Take `relatedProjects` where `relationType` is `SOURCE_REPO`. Then **deduplicate by owner, not by package** - a single maintainer often stands behind a dozen dependencies, and the sponsorship decision is per maintainer. Deduplication is what produces the actionable minimum: the fewest destinations covering the most dependencies.

Batch requests (about ten at a time) and skip packages with no resolvable repository, counting them as unresolvable rather than dropping them silently.

## Step C - pull health and criticality signals

```
https://api.deps.dev/v3/projects/github.com%2F{owner}%2F{repo}
```

Returns the project's security-scorecard checks plus stars, license and open-issue count. The **Maintained** check (0-10) is the liveness proxy:

| Score | Read as                                   |
| ----- | ----------------------------------------- |
| 7-10  | Actively maintained                       |
| 4-6   | Partially maintained - ask before funding |
| 0-3   | Likely dormant - money changes nothing    |

For ecosystem-level importance, the open criticality-score dataset rates projects from 0 (least critical) to 1 (most critical) using ten weighted signals:

- Project age.
- Update recency.
- Contributor count.
- Organizational diversity of contributors.
- Commit frequency.
- Release cadence.
- Issue-closure and comment activity.
- Dependents count.

It is published as a public dataset and is explicitly designed to prioritize where support goes.

Fragility is the inverse read of the same data: few contributors, one dominant organization, and a high dependents count is exactly the profile where a sponsorship changes an outcome.

## Step D - find and verify funding destinations

Check in this order, once per owner:

1. **Repository funding manifest** - `.github/FUNDING.yml` on the default branch.
2. **Owner-level fallback** - `{owner}/.github` → `FUNDING.yml`, which applies to every repository of that owner that has none of its own. Look each owner up once and reuse the result.
3. **Registry metadata** - the package registry's own funding field, which may be a string, an object with a `url`, or an array.
4. **The project's site or docs**, when the first three come back empty.

Manifest keys map to destinations directly:

- A sponsorship-platform username.
- A collective slug.
- A coffee/tipping handle.
- A dependency-share handle.
- Up to four custom URLs.

**Verify every destination before it enters the list.** Fetch each URL:

- A live page is included.
- A 404 or a "not enrolled" page is excluded.
- A redirect is followed and the final URL recorded.

Never present a funding link from model memory; funding pages change, and paying into a stale destination fails silently.

A project with no verified destination is not a target. It may still deserve support in kind - contribution time, CI credits, hosting, security review - and belongs in a separate list, framed as an opportunity rather than a failing. Many maintainers do not want money.

## Step E - collect reach signals (manual)

No API exposes placement value. Collect per candidate:

- Traffic on the surface the tier grants (README, docs site, project homepage, a curated list). Maintainers who sell placement usually publish or will share these numbers - one well-known maintainer prices tiers against published monthly view counts of 60k, 20k and 6k on specific lists.
- Package download or install volume as an audience-size proxy.
- Owned channels: newsletter, chat community, conference presence.
- **Audience alignment**: do this project's users look like your buyers, or your future hires? A small project whose audience is exactly your ICP beats a large project whose audience is not - the same test creator programs apply to influencers, and it matters more than raw size.

## Scoring rubric

The axes and weights below are defaults written for this skill, not a published rubric - present them as a proposal and let the user change them. What matters is that the primary mandate is the thing that breaks ties, and that the weights are written down before the candidates are scored rather than after.

1. Score each candidate 1-5 on four axes.
2. Weight them against the mandate.
3. Record the number so the shortlist can be re-derived next year.

| Axis               | Question                                                    | Weight if supply chain | Weight if reach |
| ------------------ | ----------------------------------------------------------- | ---------------------- | --------------- |
| Exposure           | How much of our stack depends on it?                        | ×3                     | ×1              |
| Fragility          | How close is this to one person stopping?                   | ×2                     | ×1              |
| Audience fit       | Do its users look like our buyers or hires?                 | ×1                     | ×3              |
| Relationship value | Would we want this maintainer reachable during an incident? | ×2                     | ×1              |

Payability is a filter, not an axis. Health below the dormancy threshold is also a filter - fund a dormant project only as an explicit revival bet, with the maintainer's agreement.

## Worked shortlist

| Project                           | Deps covered                 | Maintained | Fragility                    | Audience fit                    | Destination (verified)                    | Amount/yr     | Mandate                                                    |
| --------------------------------- | ---------------------------- | ---------- | ---------------------------- | ------------------------------- | ----------------------------------------- | ------------- | ---------------------------------------------------------- |
| CLI framework used in our SDK     | 14 (1 direct, 13 transitive) | 9          | 5 - one maintainer           | 4 - our SDK users read its docs | sponsorship platform, personal account ✅ | $6,000        | Reach + supply chain                                       |
| Crypto library in the auth path   | 3 direct                     | 8          | 4 - two maintainers          | 2                               | fiscal-host collective ✅                 | $12,000       | Supply chain                                               |
| Log-parsing utility               | 22 transitive                | 5          | 5 - one maintainer, sporadic | 1                               | sponsorship platform ✅                   | $120 ($10/mo) | Supply chain (breadth)                                     |
| Data-viz library on our docs site | 2 direct                     | 9          | 2 - vendor-backed            | 5                               | none found ❌                             | -             | Disqualified: no destination; propose contribution instead |

Amounts sit on the maintainer's published ladder wherever one exists; the $12,000 line is a custom amount agreed by invoice because the library is load-bearing for the product. Both tables are illustrative: the projects are composites, and the numbers show the shape of a defensible row rather than a benchmark to hit.

## The same shortlist done badly

The common failure is not laziness - it is a list that looks rigorous and measures the wrong things.

| Project               | Stars | Why we picked it                        | Amount/yr |
| --------------------- | ----- | --------------------------------------- | --------- |
| Popular web framework | 78k   | Everyone knows it; great logo placement | $25,000   |
| Language runtime      | 91k   | Critical to us                          | $20,000   |
| Testing library       | 34k   | Our staff engineer likes it             | $5,000    |

Four things are wrong with it, in order of cost:

1. **Stars rank popularity, not exposure or fragility.** None of these rows says how much of the company's stack depends on the project, or how close it is to one person stopping.
2. **The three biggest recipients are already funded.** Two are backed by a corporate parent or a foundation with paid staff; the marginal effect of the money is close to zero, and a pledge-style accounting would question whether the largest line counts at all.
3. **No destination was verified.** "Great logo placement" names no surface, no traffic and no tier that grants it.
4. **The long tail is missing entirely.** The single-maintainer packages carrying 22 transitive dependencies each - where $10/month is genuinely load-bearing - never entered the list, because they have no stars to sort by.

The fix is not more diligence on these three rows. It is starting from the dependency graph instead of from recall.

## Disqualifiers

- **Vendor-owned project.** A sponsorship is a rounding error to a funded company and buys nothing.
- **Employee-maintained project**, when the program has a conflict-of-interest rule.
- **Subscription-only recipient**, when the budget pays one-off amounts.
- **Dormant project** with no revival plan agreed with the maintainer.
- **Live conduct or security controversy.** The brand attaches to the sponsee, and the sponsorship page is public.
- **License or governance conflict** with the company's own policy.
