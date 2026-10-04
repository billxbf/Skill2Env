# Validating a proposed structure, and keeping it

## Who owns a structure audit

The deliverable set for a structure engagement belongs to an information architect and a content strategist:

- Content inventory spreadsheet.
- IA/sitemap diagram.
- Taxonomy.
- Content model spec.
- Metadata schema.
- Migration plan.
- Governance doc.

NN/g's framing is worth repeating to anyone who thinks this is a one-afternoon job: "The IA is much more than just a sitemap. It's a very involved process of constantly making decisions about how your content is organized and maintained."

Three failure modes follow predictably when a generalist runs the audit alone:

- Treating it as a one-off friction log instead of a repeatable inventory-plus-rubric pass.
- Optimising the hero getting-started path while reference and explanation stay unstructured.
- Skipping user validation entirely.

When no writer exists - the normal case in open source - ownership of the structure sits with maintainers through CODEOWNERS and PR review, on top of the external-program routing in SKILL.md.

Sources: NN/g "Information Architecture vs. Sitemaps"; Bynder; Tahzoo; State of Developer Relations Report 2023.

## Card sorting and tree testing

Classification and demand signals say what is wrong today. Only user testing says whether the _proposed_ structure is better.

- **Card sorting** (open, closed or hybrid) surfaces users' mental models and generates candidate categories.
- **Tree testing** validates a proposed hierarchy by measuring task success and first-click accuracy against a text-only tree, isolating structure from visual design.
- **Sequence**: card sort to design, tree test to validate. OptimalSort and Treejack are the industry-standard pair; UXtweak, Maze, UserZoom and Miro cover the same ground.

**Sample sizes that real projects used.** A published GovWebworks engagement ran an open card sort with 69 participants sorting 30 labelled cards, then "asked 222 remote participants to complete four tasks to evaluate the performance of the proposed information architecture." Treat ~60-70 for the sort and 4-6 tasks for the tree test as the working target; the 222-participant tree test is an upper bound, not a requirement.

**A docs-team validation without commercial tooling.** A newly formed technical-writing team inheriting an engineer-written docs set combined three checks instead of one: a content audit, a structural comparison against competitor documentation, and an in-house usability study of real users (Jeffrey Boruszak and Adam Trujillo, "Bootstrap IA Development with In-house Usability Testing", Write the Docs Atlantic 2023). The usability study exposed where actual navigation behaviour diverged from the team's assumptions; the findings split into quick wins shipped immediately and a longer IA roadmap, both delivered ahead of a major launch with no added headcount.

**Interpreting results** (practitioner heuristics, not an authoritative standard):

| Reading                                               | Diagnosis                                                                                          | Action                                                                    |
| ----------------------------------------------------- | -------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| Task success ~45%                                     | "A clear sign that the current categorization is confusing"                                        | Restructure before shipping                                               |
| Task success < ~60%                                   | Structure fails on that task                                                                       | Restructure that branch                                                   |
| Direct-path rate < ~40%                               | Users get there by wandering                                                                       | Relabel, then re-test                                                     |
| 90% success with 30% direct path                      | "Users find the content eventually but get lost along the way - the category labels are ambiguous" | Fix labels, keep the tree                                                 |
| > 80% success and > 60% direct path across core tasks | Structure is not the bottleneck                                                                    | **Cancel the restructure**; spend the budget on gap-filling and freshness |

That last row is the most valuable one in this file. A restructure that a tree test says is unnecessary costs a quarter of writing time and breaks every inbound link for nothing.

**When user testing is not available**, say so in the report and downgrade every structural recommendation from "validated" to "proposed". Analytics substitute partially:

- Top 404s (the CNCF assessment template explicitly asks reviewers to "include a list of the top 404s, as reported through analytics or a search console").
- Zero-result site searches.
- High-exit landing pages.

Sources: NN/g "Card Sorting vs. Tree Testing"; Optimal Workshop; CorsoUX practical guide; GovWebworks UX Playbook Part 2 (2018-10-23); CNCF Falco assessment template; Jeffrey Boruszak and Adam Trujillo, "Bootstrap IA Development with In-house Usability Testing", Write the Docs Atlantic 2023.

## Governance: keeping the structure after the audit

An audit's fixes decay without an enforcement layer. Recommend these as part of the queue, not as a follow-up project.

**Declare the content type in front matter and validate it in CI.** Microsoft Learn requires `title`, `description`, `author`, `ms.author`, `ms.date` and `ms.topic`, and omitting a required attribute "will likely get a validation error during build". The docs-as-code equivalent is a JSON Schema for front matter enforced in CI. A page whose declared type and actual content disagree is then a build failure, not an audit finding two years later.

**Ship page templates so contributors fill blanks instead of inventing structure.** The Good Docs Project templates (explanation, how-to, README, reference, release notes, troubleshooting, tutorial, quickstart, API overview) follow the Diátaxis types directly, so they combine with a Diátaxis audit rather than competing with it. Microsoft Learn and Kubernetes publish equivalent template sets.

**Lint prose and structure in CI.** Vale is the de facto docs-as-code prose linter: a Go CLI that runs locally, in editors and in CI, and ships the Microsoft and Google style guides as packages.

It is fast enough not to be an excuse - vale.sh reports that "GitLab runs 82 rules across all 2,827 pages of its documentation in under twenty seconds."

Pair it with markdownlint, and with the generator's own strict mode (MkDocs strict, Sphinx nitpick, Docusaurus broken-link check).

**Check links on a schedule, not at review time.** lychee is the current standard, an async Rust checker for Markdown/HTML/rST:

- Validates anchor fragments (`--include-fragments`).
- Caches results.
- Ships a GitHub Action.
- Is commonly run on a daily cron that opens an issue on failure.

htmltest is the Hugo-native alternative.

**Assign owners.** CODEOWNERS auto-requests review from the maintainers of a subtree; CNCF recommends it for large codebases and a single-reviewer minimum for small teams. Add a PR template that makes the author declare the content type and confirm it matches the template.

**Keep URLs stable.** Maintain a redirect for every page move and prefer relative internal links. A structure audit that breaks inbound links trades one findability problem for another.

**Re-audit quarterly.** Run this cadence quarterly, using 90-day versus prior-90-day analytics windows, so the audit does not depend on one person remembering to export data:

1. Inventory.
2. Score.
3. Prioritise.
4. Refresh.
5. Measure.

Sources: learn.microsoft.com/contribute/content/metadata; thegooddocsproject.dev/template; vale.sh; github.com/lycheeverse/lychee; CNCF "Security Hygiene Guide for Project Maintainers"; Click Laboratory.
