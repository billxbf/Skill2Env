# Audit report, measurement and maintenance

Contents: report template · worked report excerpt · Search Console segmentation · thresholds · maintenance triggers.

## Table of Contents

- [Report template](#report-template)
- [Verdict](#verdict)
- [Coverage of this audit](#coverage-of-this-audit)
- [Blocking defects](#blocking-defects)
- [Duplication and versioning](#duplication-and-versioning)
- [Page signals](#page-signals)
- [Internal linking](#internal-linking)
- [Fix list](#fix-list)
- [Pass threshold](#pass-threshold)
- [Worked excerpt](#worked-excerpt)
- [Blocking defects](#blocking-defects)
- [Search Console segmentation](#search-console-segmentation)
- [Thresholds](#thresholds)
- [Maintenance triggers](#maintenance-triggers)

## Report template

```markdown
# Docs SEO audit: docs.example.com - 2026-08-28

## Verdict

One paragraph: what is blocking search performance, and the single fix
with the largest effect.

## Coverage of this audit

Pages crawled: N (from sitemap / from URL list).
Not verified: <what could not be checked and why - no Search Console access,
no repository access, platform blocked the crawl>.

## Blocking defects

Anything that makes correct pages invisible. These override any score.
| # | Defect | Pages affected | Fix | Owner | Effort |

## Duplication and versioning

Declared posture, actual posture, and the gap between them.

## Page signals

Template-level fixes first (title template, description defaults,
heading levels), per-page fixes second.

## Internal linking

Orphans, dead ends, and the contextual links to add from the
highest-authority pages.

## Fix list

Ordered by (pages affected x severity) / effort. One line per fix:
what changes, in which file, who owns it.

## Pass threshold

The agreed numbers and where each one stands today.
```

## Worked excerpt

```markdown
## Blocking defects

| #   | Defect                                                                                                   | Pages | Fix                                                             | Owner      | Effort |
| --- | -------------------------------------------------------------------------------------------------------- | ----- | --------------------------------------------------------------- | ---------- | ------ |
| 1   | `/v1/` and `/v2/` disallowed in robots.txt, so their `noindex` is never read - 812 URLs indexed URL-only | 812   | remove the Disallow, serve `X-Robots-Tag: noindex` from the CDN | infra      | 1h     |
| 2   | Sitemap lists every version; 3 of 4 contradict the canonical tag                                         | 1,204 | regenerate from the stable alias only                           | docs build | 2h     |
| 3   | PR preview host returns no `X-Robots-Tag`; 41 preview URLs indexed                                       | 41    | add the header at the CDN, then request removal                 | infra      | 1h     |
```

Note the shape: each row names the file or system that changes and who owns it. A defect list with no owner column comes back unchanged at the next audit.

## Search Console segmentation

Search Console is the only source that sees a docs site's real queries. Treat third-party volume estimates as directional at best - most technical queries report as zero.

Segment before reading anything:

- One filter set per path prefix (`/docs/`, `/reference/`, `/blog/`). A sitewide average hides that reference pages get impressions and no clicks while guides get the reverse.
- Filter to the canonical version path; version noise otherwise dominates every report.
- Read the Pages report against the sitemap in both directions: URLs in the sitemap but not indexed is the indexation gap; URLs indexed but absent from the sitemap is the leak (previews, retired versions, the platform subdomain).
- Watch the "Duplicate, Google chose different canonical" bucket specifically - it is the direct readout of whether the version posture is working.

Where Search Console access is unavailable, the crawl script's summary plus a `site:` query per section is a usable substitute for everything except query data. Say so in the report's coverage section rather than filling the gap with estimates.

### Limits of the query data itself

Documented in Google's Search Analytics API reference:

- `rowLimit` accepts 1-25,000 and defaults to 1,000, so an unmodified export is the head of the list only.
- Groupable and filterable dimensions are `country`, `device`, `page`, `query`, `searchAppearance`, `date`, `hour`. **There is no position filter** - average position comes back as a metric, so a "positions 5-20" shortlist has to be filtered client-side after a large export.
- "The API […] does not guarantee to return all data rows but rather top ones."
- Rare queries are withheld for privacy. On a technical property that suppresses exactly the long tail of error strings and symbol names you care about, so treat the visible tail as a floor and never sum query rows into a site total.
- Search Console's own help notes that chart totals and table totals can differ because of property-versus-page aggregation.

## Thresholds

Two different kinds of number end up in this table, and mixing them is how a threshold conversation goes wrong. The first column of the verdict is which kind you are quoting.

**Sourced requirements** are enforced by the search engine or the spec, so they are defects rather than targets. Put them in the blocking-defects section, not here:

- a page disallowed in `robots.txt` never has its `noindex` or canonical read
- an `hreflang` set with a missing return link may be ignored entirely
- a sitemap file may not exceed 50,000 URLs or 50MB uncompressed
- `lastmod` is only used when it is consistently accurate

**Baselines for this skill** - assembled here, not industry standards. Say so when you present them, then agree adjusted numbers with the user before the fix pass so remediation has a finish line:

| Metric                                         | Baseline      | Measured with                             |
| ---------------------------------------------- | ------------- | ----------------------------------------- |
| Canonical docs URLs indexed                    | ≥ 95%         | Search Console Pages report vs. sitemap   |
| Pages where Google chose a different canonical | 0             | Search Console Pages report               |
| Non-200 URLs in the sitemap                    | 0             | crawl script                              |
| Docs pages with a unique title                 | 100%          | crawl script                              |
| Orphan pages (no inbound internal link)        | 0             | crawl script                              |
| Indexed preview / retired-version URLs         | 0             | `site:` query per host and version prefix |
| Core Web Vitals passing for the docs path      | ≥ 90% of URLs | Search Console Core Web Vitals report     |

Only the Core Web Vitals row has a sourced component: each metric's own pass mark is Google's, while the share of URLs required to reach it is this skill's baseline.

Re-run the crawl after the fix pass and compare the two summaries. That diff is the deliverable's proof, not the original findings list.

Report ranking and indexation outcomes as pending rather than promised. Configuration and consistency are verifiable in the same session. Re-indexing, re-ranking and snippet changes are not, and no ranking-factor weight quoted in an audit is measurable by the person quoting it.

Two numbers not worth targeting: bounce rate (a developer who found the answer and left is a success) and pages per session on reference content.

## Maintenance triggers

Book these now - a docs site regresses through routine releases, not neglect:

- **A new version ships**: the canonical alias moves, the sitemap regenerates, the previous version's banner appears.
- **A version is retired**: per-page redirect targets chosen, sitemap updated in the same deploy.
- **The docs generator or theme is upgraded**: re-check the title template, the sitemap plugin and the anchor-id scheme - theme upgrades silently reset all three.
- **A new locale launches**: `hreflang` set regenerated across every locale, not just the new one.
- **Quarterly**: re-run the crawl, diff against the last summary, check the "different canonical" bucket.

If your environment has persistent memory, store the durable decisions:

- the version posture and its canonical target
- the chosen primary domain
- the title template
- the agreed thresholds
- which surface owns which query family

The next pass is a diff against those, and re-deriving them each cycle is where this work usually dies.
