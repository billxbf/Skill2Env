# Automated migration tooling

Five rungs of automation exist, ranked here by reader hours saved per engineering hour spent building and holding them. Document whichever you have; build down the list only as far as the budget reaches.

| Rung                                             | What it buys the reader                                                 | What it costs you                                                             |
| ------------------------------------------------ | ----------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| Search patterns and literal messages, per change | Every call site located, by a human or an agent, with no tooling at all | Near-zero - it is the affected-if line you already write                      |
| Deprecation warnings in N-1                      | Their own build output becomes their personal inventory                 | One interim release, plus the warning plumbing behind it                      |
| Lint rule                                        | New code stops reintroducing the old API after the migration            | A day, then it lives with the ruleset                                         |
| Codemod                                          | The mechanical majority of edits, across a whole codebase               | A week, corpus validation, and a rewrite every time the API moves again       |
| Compat build                                     | A migration that ships to production half-done                          | A standing job: dual behavior paths and per-feature flags until it is retired |

- value: compat build > codemod > deprecation warnings in N-1 > search patterns and literal messages > lint rule
- engineering plus upkeep effort: compat build > codemod > deprecation warnings in N-1 > lint rule > search patterns and literal messages
- efficiency: search patterns and literal messages > deprecation warnings in N-1 > lint rule > codemod > compat build

The lint rule outranks the codemod on efficiency while losing to it badly on value: it is a day of work against a week, and it defends the migration after the guide stops being read, which is where the second wave of regressions comes from.

**Default: ship the first rung, always**, and buy the second whenever N-1 can still ship a release. That order starves the compat build and, one rung above it, the codemod - the two things readers ask for by name.

Promote them anyway when the blast radius crosses hundreds of call sites per consumer, or when consumers are large applications that cannot hold a long-lived migration branch. When nobody owns the tooling after the release, say so and stay on the first two rungs rather than shipping a codemod that rots into a wrong answer.

This ranking is a default, not a law. An ecosystem where the codemod is nearly free (`cargo fix --edition`, `go fix`, an OpenRewrite recipe close to one you already publish) moves the codemod straight to the top for that project.

## Codemods

Ecosystem tooling, as an integration note rather than a requirement (the guide outlives any of these):

| Ecosystem               | Tooling                                                               |
| ----------------------- | --------------------------------------------------------------------- |
| JavaScript / TypeScript | `jscodeshift`, the `codemod` CLI, `ast-grep`, type-only codemod packs |
| Rust                    | `cargo fix --edition`                                                 |
| Python                  | `libcst` codemods, `pyupgrade`                                        |
| Go                      | `go fix`, `gofmt -r` rewrite rules                                    |
| JVM / polyglot          | OpenRewrite recipes                                                   |

Documentation rules, in order of how often they are broken:

1. **Publish the exact command**, not the tool's homepage. A reader mid-upgrade should never have to navigate.
2. **Publish both granularities** - an all-changes recipe and the per-change commands - because a reader who already fixed half the codebase wants only the rest.
3. **State the coverage boundary in the same breath as the command.** React's v19 guide says outright that its codemods do not cover TypeScript changes. An unstated gap is discovered as a broken build, and it discredits the whole guide, not just that entry.
4. **Name the residue.** Codemods handle literal arguments and static call sites; dynamic dispatch, re-exports, generated code and string-keyed access survive. Say which of those apply and how to find them.
5. **Tell the reader how to verify.** Typecheck, run the test suite, review the diff. A mechanical rewrite is review-required, not fire-and-forget, and saying so preempts the "your codemod broke my build" issue.
6. **Never position the codemod as a replacement for the breaking-change list.** It is the first pass; the list is the contract.

Validate the codemod against a corpus, not one repository: clone every example app, internal consumer and public dependent you can, run it across all of them, and publish what it left behind. One project is not a sample, and the residue list is the paragraph readers cannot reconstruct for themselves.

## Compat / migration builds

A compat build runs old-version behavior by default, warns on each deprecated usage, and lets the project flip behavior per feature and per module. Vue's v3 migration build is the reference implementation, and its documented workflow generalizes:

1. Update tooling and companion libraries.
2. Install the compat build behind an alias so imports stay unchanged.
3. Clear compile-time errors first - they block everything else.
4. Work through runtime warnings in batches, filtering by feature flag.
5. Migrate module by module, flipping each one's flag as it is done.
6. Remove the compat build and the flags.

The property worth stating explicitly in the guide: a compat build makes the migration **shippable mid-way**. The team deploys a half-migrated application instead of maintaining a long-lived branch that rots against main. That single sentence changes how a team plans the work, so it belongs near the top of the guide, not in an appendix.

## The manual path, which every guide ships

The first rung is not a consolation prize for projects without tooling - it is what makes the manual path findable and it ships whatever else exists. Per breaking change, give the search pattern that locates every call site and the literal runtime message. That pair is also exactly what a coding agent needs to do the work unattended, which is why it outranks tooling that only a human can drive.

When there is no codemod, say so plainly. Readers who assume one exists spend their first hour looking for it.
