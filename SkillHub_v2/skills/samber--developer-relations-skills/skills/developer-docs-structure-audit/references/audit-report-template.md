# Audit report shape

## Table of Contents

- [Template](#template)
- [Verdict](#verdict)
- [Section ratings](#section-ratings)
- [Scorecard](#scorecard)
- [Coverage matrix](#coverage-matrix)
- [Findings](#findings)
- [Remediation queue](#remediation-queue)
- [Not covered by this audit](#not-covered-by-this-audit)
- [Inputs](#inputs)
- [Finding format](#finding-format)
- [Severity tiers](#severity-tiers)
- [Filled excerpt](#filled-excerpt)
- [Verdict](#verdict)
- [Findings](#findings)
- [Remediation queue](#remediation-queue)
- [Negative example - findings that should never ship](#negative-example-findings-that-should-never-ship)
- [Delivery rules](#delivery-rules)

## Template

```markdown
# Docs structure audit - <product>, <date>

## Verdict

<Three sentences: the shape of the problem, the single biggest cost it creates, the size of the fix.>

## Section ratings

| Section                                                                                            | Information architecture | New user content | Content maintainability | Content creation processes |
| -------------------------------------------------------------------------------------------------- | ------------------------ | ---------------- | ----------------------- | -------------------------- |
| Guides                                                                                             | 2                        | 1                | 3                       | 1                          |
| ...                                                                                                |
| <1 = not present, 2 = needs improvement, 3 = meets standards, 4 = meets or exceeds, 5 = exemplary> |

## Scorecard

| Measure     | Now | Target | Threshold source | Status |
| ----------- | --- | ------ | ---------------- | ------ |
| Mode purity | 61% | ≥ 90%  | agreed baseline  | fail   |
| ...         |

## Coverage matrix

<surfaces × four modes, gaps marked>

## Findings

<one block per finding, must-fix first>

## Remediation queue

<ordered by reader need fixed per hour of effort - see SKILL.md Step 8>

| #   | Action | Page(s) | Mode outcome | Reader need fixed | Effort | Evidence |
| --- | ------ | ------- | ------------ | ----------------- | ------ | -------- |

## Not covered by this audit

<accuracy, prose style, SEO, sample runnability - and who owns each>

## Inputs

<what was inventoried, which signals were available, what was inferred>
```

## Finding format

```
[severity] <page path>
- Now: <what the page mixes, misplaces, or lacks  - with the evidence: heading names, step counts, table>
- Reader impact: <who arrives here with which need and leaves without it>
- Next action: <one action, doable in one sitting>
```

One action per finding. A finding whose action is "restructure the docs" is not a finding; split it until each part is a single move.

## Severity tiers

- **Must fix** - a reader with a common need cannot succeed: no entry point for a primary audience, a surface with no reference, a mixed page on the adoption path, orphaned pages that only search can reach.
- **Should fix** - the need is met but expensively: mixed pages off the main path, how-tos filed as concepts, duplicated content diverging between two locations.
- **Worth noting** - hygiene: single-page nav sections, depth beyond three levels, stale pages, titles that do not match their mode.

## Filled excerpt

```markdown
## Verdict

The docs are three how-to collections and an API dump: 47 of 78 pages inform action, and every page
that explains the system is inside a procedure. New users have no supported first path, and evaluators
have nothing to read before committing. Roughly 12 page splits and one new tutorial close the gap;
no re-platforming is needed.

## Findings

[must fix] docs/concepts/authentication.md

- Now: token-lifecycle diagram (explanation), then 8 numbered rotation steps, then a 22-row scope table.
  Three modes on one URL; the page is the #2 landing page from search.
- Reader impact: someone rotating a key mid-incident scrolls past a diagram; someone evaluating the
  security model hits procedure noise and leaves.
- Next action: extract the 8 steps into guides/rotate-an-api-key.md and link it from the concept page.

[must fix] no entry point for the Python SDK

- Now: the Python SDK has 6 how-tos and an API reference, no tutorial or quickstart. Site search shows
  "python getting started" at 214 queries in 90 days with 0 results.
- Reader impact: the largest ecosystem in the product has no supported first hour.
- Next action: write a single-path quickstart to the first successful API call; keep alternatives out.

[should fix] docs/guides/webhooks.md

- Now: starts by installing the CLI and creating an account, then forks four ways on framework.
- Reader impact: competent readers wade through setup; beginners hit branches they cannot judge.
- Next action: replace the setup section with a prerequisites line linking the quickstart.

## Remediation queue

| #   | Action                             | Page(s)                    | Mode outcome         | Reader need fixed                           | Effort | Evidence                         |
| --- | ---------------------------------- | -------------------------- | -------------------- | ------------------------------------------- | ------ | -------------------------------- |
| 1   | Split rotation steps into a how-to | concepts/authentication.md | explanation + how-to | rotating a key stops needing a concept page | 1h     | 214 zero-result searches         |
| 2   | Trim setup from webhooks guide     | guides/webhooks.md         | how-to               | the guide stops re-teaching setup           | 30m    | ticket cluster "webhook 401"     |
| 3   | Write Python quickstart            | new: tutorials/python.md   | tutorial             | Python adopters get a first-run path        | 1d     | 31 tickets - promoted above rank |
```

## Negative example - findings that should never ship

```markdown
[must fix] Site-wide

- Now: the documentation does not follow Diátaxis.
- Reader impact: poor developer experience.
- Next action: restructure the docs site around the four modes in Q3.
```

Three separate defects, each common and each tempting:

- The evidence is a framework name rather than an observation about a page.
- The impact is a slogan nobody can disagree with or act on.
- The action is a quarter-long project that pays off only at the end, and it is the teardown Diátaxis explicitly warns against.

The same underlying problem, written so a maintainer can pick it up before lunch:

```markdown
[must fix] docs/guides/index.md

- Now: the Guides landing page lists 34 links with no grouping; 11 are conceptual, 23 are procedures.
  Site search shows "how to" queries landing here at a 71% exit rate.
- Reader impact: someone arriving with a task scans 34 undifferentiated links and leaves for search.
- Next action: split the list into "Tasks" and "Concepts" groups on this page only; no files move.
```

## Delivery rules

- Order the queue by the Step 8 ranking, say in the report that it is a ratio and not a severity list, and mark any row promoted above its rank with the signal that promoted it.
- Cap the queue at what the team can absorb before the next re-score, then say what was deferred.
- Give credit where a section is already clean; an audit that reports only failures gets read as an attack on whoever wrote the docs.
