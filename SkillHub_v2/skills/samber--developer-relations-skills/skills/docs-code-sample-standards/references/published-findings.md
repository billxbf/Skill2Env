# Published findings and baselines

Published figures on code-sample quality, the baselines this skill sets for itself, and the circulating claims it refuses to repeat. Cite from this file rather than from memory - a fabricated benchmark in a sample-quality audit destroys the credibility of the whole report.

## Contents

- Compilability and executability
- Staleness and deprecation
- Why sample quality matters
- Corpus scale
- Rubric anchors
- Self-set baselines
- Claims to never repeat

## Compilability and executability

**Yang, Hussain & Lopes, "From Query to Usable Code" (MSR 2016).** Roughly 3 million snippets from accepted Stack Overflow answers, four languages:

| Language                | Parsable | Compilable / runnable |
| ----------------------- | -------- | --------------------- |
| Java (914,974 snippets) | 3.89%    | 1.00% compilable      |
| C#                      | -        | 0.12% compilable      |
| Python                  | 76.22%   | 25.61% runnable       |
| JavaScript              | 65.88%   | 20.00% runnable       |

Dynamic languages were measured as runnable rather than compilable, so the two halves of the table are not directly comparable. Use this to answer "surely our samples are mostly fine" - in a mature, heavily upvoted corpus, statically typed snippet compilability is near zero.

**Horton & Parnin, "Gistable" (ICSME 2018).** 10,259 Python code snippets, ~5,000 with a Dockerfile: 75.6% "require non-trivial configuration to overcome missing dependencies, configuration files, reliance on a specific operating system, or some other environment configuration." Only 24.4% ran without error out of the box. This is the basis for testing from a clean environment rather than a developer laptop.

## Staleness and deprecation

**Zhou & Walker (FSE 2016).** 43% of the Stack Overflow posts investigated contained deprecated APIs. Their Deprecation Watcher reached 100% precision and 86% recall on a 200-question sample - automated deprecation detection is tractable, not aspirational. The skill uses 43% as the baseline above which a deprecation gate outranks other remediation work.

## Why sample quality matters

**Uddin & Robillard, "How API Documentation Fails" (IEEE Software, 2015, DOI 10.1109/MS.2014.80).** Survey of 323 professional developers plus analysis of 179 API documentation units. Three severest problems: ambiguity, incompleteness, incorrectness. Six of ten documented problems were rated outright "blockers" by respondents.

**Stack Overflow 2024 Developer Survey.** 84% of developers who do not use Stack Overflow itself rely on technical documentation to learn; 90% of those use documentation found specifically in API and SDK packages.

**Postman State of the API (2019 wave).** The most-requested enhancement from API producers was "better examples in the documentation" at 63.5%, ahead of standardization (59.4%) and sample code generally (57.8%). Postman has characterised documentation debt as a persistent top-four industry problem across subsequent reports.

## Corpus scale

Useful for calibrating what "large" means before proposing a process:

- **Twilio**: docs "house more than 5,000 pages and nearly 20,000 code samples across nine coding languages."
- **AWS**: the SDK Code Examples library spans 14 SDKs/languages. The public examples repository shows roughly 10,500 stars and 5,800 forks - an adoption proxy, not a quality metric.

## Rubric anchors

Two real, published docs rubrics transfer to samples:

- Tom Johnson's API-documentation rubric: 80 criteria across Findability, Accuracy, Relevance, Clarity, Completeness and Readability.
- A widely circulated docs rubric scoring 0–2 per dimension on a 20-point scale, with "publishable = ≥16/20" and "world-class = ≥18/20".

Use the 20-point form for the stratified human pass; it is fast enough to apply to 50–100 samples in a sitting and its two thresholds are defensible because they are somebody else's, not yours.

## Self-set baselines

State these as baselines whenever you report against them. Each is a self-set default rather than a published coverage standard, chosen to be demanding but reachable:

- **≥80% of the corpus tested** (tier Run or Compile-only, executed by CI).
- **≥90% parity coverage** across tier-1 languages.
- **100% of primary-adoption-path samples at tier Run** - the strictest of the three, and the easiest to defend, since the quickstart and auth path is where a broken sample costs a prospective user entirely.
- **Freshness window** - deliberately left for the team to set; it depends on release cadence, and any fixed number here would be arbitrary.
- **Severity model (P0/P1/P2)** - adapted from general QA practice and applied to samples here.
- **The under-90% compile/run remediation trigger** - a self-set gate rather than a vendor-published one, well supported by the MSR 2016 numbers above.

Google Cloud requires integration tests for critical paths, which is the nearest thing to a public vendor requirement on sample verification.

## Claims to never repeat

- **"94% of developers consider API documentation quality a key factor."** Widely attributed to SlashData and repeated across blogs, yet not confirmed in any SlashData report. Do not cite it.
- **"Single Origin Snippets"** as an expansion of AWS's "SoS" metadata. Only "SoS metadata" appears in the source repository; the expansion is unverified.
- **Any per-vendor claim about snippet-tool feature support** without checking that vendor's current docs. Tooling lists in this space go stale within months.
