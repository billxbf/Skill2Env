# Corpus audit method

How to audit hundreds or thousands of samples without spot-checking. The method is borrowed wholesale from content strategy, because a sample corpus is a content corpus that happens to compile.

## Contents

- Inventory before audit
- ROT triage
- Census plus stratified sample
- Rubric scoring
- Four-stage remediation
- Negative example: the spot-check that isn't an audit

## Inventory before audit

Nielsen Norman Group draws the line precisely: a content **inventory** is "a list of every piece of digital content you currently have"; a content **audit** "examines, assesses, and evaluates the quality of the content". Two artefacts, two passes, in that order.

Build the inventory mechanically before anyone forms an opinion. One row per sample:

`language | product or service area | file path | region-tag or identifier | last-commit date | line count | inline-fenced or extracted-from-source`

The census is what stops an audit from becoming a tour of the pages someone already suspected. Regions of the corpus nobody remembers are exactly where the worst samples live.

## ROT triage

Content strategy's ROT lens transfers directly, and it is the cheapest first cut on a large corpus.

- **Redundant** - the same snippet duplicated across pages. Reconcile to one source; every copy is a future divergence.
- **Outdated** - references a deprecated API, a removed symbol, or a retired auth flow. This is the class with a measured baseline (see `published-findings.md`).
- **Trivial** - a single-API-call snippet with no scenario around it. AWS's own contribution guidance explicitly prefers "code examples that cover broader scenarios and use cases, versus simple code snippets that cover only individual API calls".

Trivial is the category teams resist cutting, because the snippet is not _wrong_. It is still maintenance debt with no reader payoff.

## Census plus stratified sample

Two tiers, chosen by what each check costs.

**Census - everything mechanical, on 100% of the corpus.** Compilation, execution, secret scanning, fence-language checks, prompt-character checks. Marginal cost per sample is near zero, so sampling here saves nothing and misses real defects. Every failure is an automatic finding, no judgement required.

**Stratified sample - everything that needs a reader.** Idiomaticity, whether the scenario is worth documenting, whether the comments add anything, whether the sample teaches a pattern you want copied. Stratify by three axes, because these are where quality drift concentrates:

- **Language** - the language added last is usually the weakest.
- **Product or service area** - coverage follows organisational attention, not reader need.
- **Age** - old samples fail differently from new ones.

Sample size is a judgement call rather than a settled standard. Pick a number you can actually score, state it in the report, and treat any figure you quote from the sample as an estimate with a stated base - never as a corpus-wide count.

## Rubric scoring

Score the stratified sample against a fixed rubric so two reviewers reach comparable numbers. Two published rubrics are worth adapting rather than inventing one: Tom Johnson's 80-criterion API-documentation rubric (Findability, Accuracy, Relevance, Clarity, Completeness, Readability), and the 0–2-per-dimension / 20-point docs rubric with its ≥16 publishable and ≥18 world-class marks (both cited in `published-findings.md`).

The code-sample-specific dimensions, each supported by vendor guidance:

| Dimension           | 0                                                    | 1                                      | 2                                                           |
| ------------------- | ---------------------------------------------------- | -------------------------------------- | ----------------------------------------------------------- |
| Correctness         | does not compile or run                              | compiles, output undocumented or wrong | compiles, runs, output asserted                             |
| Runnability         | fragment; imports elided                             | runs after obvious edits               | runs as copied, given the stated prerequisites              |
| Idiomaticity        | transliterated from another language                 | passes the formatter                   | reads as a native of the language                           |
| Error handling      | blanket catch, or a process-killing helper           | present but generic                    | specific, and only where intrinsic to the example           |
| Credential handling | real-format secret or plausible fake                 | placeholder with no explanation        | explained placeholder, reserved-range host, no secret shape |
| Copy-paste safety   | prompt characters, ellipses, output glued to command | one defect                             | clean, tagged, output in its own block                      |

Record the score per dimension, not a single total - the totals hide which axis the corpus is failing on, which is the only thing that tells you what to fix.

## Four-stage remediation

1. **Inventory (census).** The scanner walks the corpus and emits the row format above.
2. **Automated gates (census-level audit).** Compile, run, secret-scan, lint. Every failure is a finding, filed with severity, before a human reads anything.
3. **Rubric scoring (sample-level audit).** Score the stratified sample; record severity per finding.
4. **Governance for the steady state.** This is the stage that stops the audit recurring - everything before it is a one-off cleanup:
   - Migrate samples into tagged, compilable source with validated metadata.
   - Enforce ownership with code-owner rules.
   - Inject into docs by transclusion rather than by hand-pasting.

Stage 4 is the investment. Stages 1–3 tell you how bad it is; only stage 4 changes the rate at which it gets bad again.

## Negative example: the spot-check that isn't an audit

**What teams do, and why it is tempting:**

> Opened the twelve most-visited docs pages, read every code block, fixed four broken ones. Reported: "sample quality is good, minor issues on the storage pages."

Three things are wrong with it:

- The twelve most-visited pages are the twelve most-maintained pages, so the sample is biased toward the healthiest region of the corpus.
- Nothing was compiled, so "read every code block" caught only defects visible to the eye.
- The conclusion is a corpus-wide claim drawn from a convenience sample, which is the specific error the census/stratified split exists to prevent.

**What the same effort produces done properly:**

> Census: 412 samples inventoried, 380 compiled, 32 failed (92.2% pass → above the 90% gate, no remediation sprint required). Secret scan: 2 findings, both P0, reported immediately.
> Stratified sample: 40 samples scored (stratified by language × age), mean 13.4/20; error handling is the weakest dimension at 0.9/2, concentrated in the Ruby and Java sets.
> Conclusion: the corpus compiles; it does not teach error handling. Fix queue targets that, not the four broken pages.

Same afternoon, a finding the team can act on, and a number that can be recomputed next quarter.
