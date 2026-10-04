# Published findings

Every figure, threshold and named practitioner quoted by this skill, with its source and its confidence. Check this file before repeating any number to a user - several widely repeated changelog claims are unverifiable.

## Contents

- [Peer-reviewed findings](#peer-reviewed-findings)
- [Named practitioners](#named-practitioners)
- [Frameworks with a real lineage](#frameworks-with-a-real-lineage)
- [Platform rules](#platform-rules)
- [Self-set thresholds](#self-set-thresholds)
- [Claims to never make](#claims-to-never-make)

## Peer-reviewed findings

| Finding                                                                                                                           | Source                                                                     | Use it for                                                        |
| --------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| Up to 8 hours for an experienced developer to draft a release-note document                                                       | Moreno et al., cited in Daneshyan et al., FSE 2025                         | Why the task gets skipped or rushed                               |
| Well-formed release notes list only 6-26% of the issues a release addressed                                                       | Abebe, Ali and Hassan                                                      | Coverage expectations; human notes are selective by design        |
| 32,425 release notes across 1,000 GitHub projects yield 8 recurring information categories                                        | Bi, Xia, Lo, Grundy and Zimmermann, IEEE TSE 48:1834-1852, 2022            | Category sets are empirically convergent, not arbitrary           |
| 64.54% of 612 release notes organise changes hierarchically; three writing styles recur                                           | Wu et al., 233 GitHub projects                                             | Grouping by category is the norm readers expect                   |
| Content sources: pull requests 32%, issues 29%, commits 19%, CVE issues 6%                                                        | Nath and Roy                                                               | Commits alone are a minority input - read PRs and issues too      |
| 54% of 900 open-source projects generate release notes from pull requests                                                         | Jiang et al.                                                               | Why PR-only tooling excludes nearly half of projects              |
| ~90% of sampled projects enforce no standard commit specification                                                                 | Daneshyan et al., FSE 2025                                                 | Messy history is the default case, not the exception              |
| SmartNote generated notes for 100% of 23 projects; DeepRelease ~90%; Conventional Changelog ~46%                                  | Daneshyan et al., FSE 2025 (DOI 10.1145/3729345)                           | Git-based generators fail often; applicability beats polish       |
| SmartNote reached 81% commit coverage vs 31% for the projects' own human-written notes                                            | same                                                                       | Human writers trade coverage for concision deliberately           |
| Significance threshold of 0.10-0.15 balanced verbosity against omission                                                           | same                                                                       | Precedent for setting an explicit cut line on large ranges        |
| Over 80% of 17 evaluators preferred SmartNote on completeness, clarity, organisation; only 55% on conciseness                     | same                                                                       | LLM drafts run long; concision is the weak axis                   |
| A raw LLM with no prompt engineering scored worse on all four criteria and produced a 36-line note for one simple change          | same                                                                       | Structure matters more than model choice                          |
| Longer release notes and more frequent updates correlate with higher average ratings - 69,851 releases, 67.7M reviews, 2,232 apps | Yang, Hassan, Zou and Hassan, _Empirical Software Engineering_ 27:55, 2022 | The only outcome evidence in the field; correlational, confounded |

## Named practitioners

| Person            | Then                          | Position                                                                                                                                                                                                                                           | Where                                            |
| ----------------- | ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------ |
| Anna Pickard      | Editorial director, Slack     | The store text box is "just a little space in which we can be human"; voice distilled as _clear, concise, human_, clarity first                                                                                                                    | Building Slack, 2024-02-26; Contagious, 2015     |
| Sarah Maddox      | Technical writer, Google      | The function is to let customers know something changed, especially when it changes how they use the product                                                                                                                                       | quoted in UX Collective, 2020                    |
| Anne Edwards      | Technical writer              | Funny and friendly notes run long, obscure the message, and cost non-native readers extra work                                                                                                                                                     | Write the Docs, quoted in UX Collective, 2020    |
| Karri Saarinen    | Co-founder, Linear            | Returns from changelog discipline are mostly non-user: recruiting, investor confidence, early-adopter trust. Usually the person who built the feature writes the entry                                                                             | Medium, 2020                                     |
| Brandur Leach     | API Experience, Stripe        | Make versioning first-class and the changelog generates itself                                                                                                                                                                                     | Stripe engineering blog, 2017                    |
| Doug Hellmann     | Release management, OpenStack | Move the note into the patch and peer-review it like code (the `reno` design)                                                                                                                                                                      | OpenStack docs                                   |
| Tom Johnson       | API technical writer, Google  | Diffs beat engineers' self-reports as a source: "engineers aren't telling technical writers half of the changes they're making." Running an agent on the task, review comments fell from 15-20 per release to 3-5 after roughly a dozen iterations | idratherbewriting.com, 2025-02-17 and 2026-05-04 |
| Jasmine Greenaway | Developer advocate, Microsoft | "We hate creating release notes when it's our turn to ship software updates"                                                                                                                                                                       | opensource.microsoft.com, 2018-09-06             |

The Pickard-versus-Maddox/Edwards disagreement is genuinely unresolved in the field, not settled by evidence. The Google Play correlation is compatible with both readings.

## Frameworks with a real lineage

- **Announcement tiering** (4 tiers, investment set by expected reader impact). Public version: the PostHog handbook. Older lineage: Pragmatic Institute launch tiering, where tier 3 is reserved for incremental releases with minimal market impact. The Product Marketing Alliance distributes a matrix on the same premise.
- **The note fragment** (`reno`, `towncrier`). Each note is a separate file added in the same patch as the code, so hundreds of contributors avoid merge conflicts on one `CHANGELOG.md` and notes back-port with the code. Rejected alternatives on record: prose files (conflicts), commit messages (wrong audience, immutable), git notes (setup cost).
- **Release versus launch.** PostHog's handbook separates a release (feature available to existing users, product team's call) from a launch (put in front of new people, marketing-led), and adds an anti-veto rule: do not block decisions outside your lane. Most review friction in release communication is disagreement about authority, not wording.

## Platform rules

Verified against first-party documentation: Google Play's 500-character-per-language cap and its carry-forward of translations; Microsoft Store's 1,500-character field; Apple guideline 2.3.12 on describing changes; Firefox AMO's per-version release-notes field pinned to the `en-US` default locale; GitHub's `.github/release.yml` label-to-category mapping with `exclude.labels` and `exclude.authors`; GitHub's instruction to confirm generated notes contain all and only the intended information.

Reported but not verified against a first-party page - flag before quoting: Apple's 4,000-character limit and Promotional Text's 170-character editable field; the ~170-character visible fold; the claim that store what's-new text is not indexed for app-store search; Play's prohibition on promotional content in the field; the 30-40% expansion figure for translation into some languages.

## Self-set thresholds

Neither of these comes from a published standard. Say so if a user asks where they come from.

- **100% traceability.** Grounded in GitHub's "all and only" instruction and in every practitioner account of LLM-assisted drafting; the numeric bar itself is self-set.
- **100% coverage of consumer-observable changes.** Deliberately stricter than observed practice (31% commit coverage, 6-26% of issues). Justified because the failure is silent - a behaviour change with no entry is discovered in production.

## Claims to never make

- That a changelog drove adoption, retention, expansion or revenue. The link is unmeasured; Linear's returns are first-party and unquantified.
- That longer notes cause higher ratings. The study is correlational.
- Any dedicated changelog-tool price from memory. Reported entry prices for the same vendor contradict each other across sources by 20-30%; check the vendor's pricing page on the day.
- A performance number that has no measurement in the source material.
