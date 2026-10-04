# Generated error catalogs and AI-assistant surfaces

Contents: why generate the catalog · published implementations · how to propose it · retrieval-friendly page shape · re-indexing triggers · machine-readable surfaces · the unanswered-query loop.

## Why generate rather than hand-maintain

A catalog written twice - once as a constant in code, once as a row in the docs - drifts by default. Nobody plans the drift; it arrives with the release that adds a code and forgets the docs. Generation removes the failure mode instead of policing it: one file feeds both artefacts, so the constant and the entry cannot disagree.

Raise this before writing a page per code. It is a small engineering task with a permanent payoff, and it changes the maintenance cost of everything downstream in this skill.

## Published implementations

| Project    | Source of truth                  | What it generates                                                                                                                           |
| ---------- | -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| PostgreSQL | `src/backend/utils/errcodes.txt` | The C header `errcodes.h` and `doc/src/sgml/errcodes-list.sgml`, the documentation's error-code table                                       |
| Rust       | `compiler/rustc_error_codes`     | The online error index and the `rustc --explain <code>` terminal output, from Markdown explanations linked in the `rustc_error_codes` crate |
| Twilio     | One error dictionary             | The web reference page plus a downloadable JSON list of all REST API error codes                                                            |
| Stripe     | One error-code catalog           | The reference table, plus the `doc_url` attribute carried inside every API error object, deep-linking to that code's entry                  |

Rust's RFC 1567 also standardizes what each generated entry must contain:

- error description
- erroneous code example
- explanation
- how to fix

Adopt that as the schema of the source file, not just of the rendered page.

Analogous published accounts outside error catalogs: Sidero Labs' Talos describes wanting "a single source of truth both for markdown and for YAML comments", and Istio moved its reference docs onto a proto/Go-struct source of truth. A specific "we generated our error site from protobuf enums" case study could not be located - treat the protobuf-enum route as a general technique rather than a citable playbook.

## How to propose it

1. Ask where error identifiers are declared today (question 3 of the interview). Several declaration sites means the drift already exists; find it before proposing anything.
2. Diff the documented catalog against the codes the product can actually emit. The size of that diff is the business case.
3. Propose the smallest version: one file, one generator, both outputs checked in. Do not bundle it with a docs-site migration.
4. Name the owning team. This lands in the product repository, not the docs repository, and a docs-owned proposal to change compiler source goes nowhere.

## Serving these pages to assistants

Increasingly the reader is a retrieval system paraphrasing the page rather than a human scanning it. The good news is that there is no separate optimization: the structure that helps a scanner is the structure that survives retrieval.

- **Write blocks that stand alone.** Chunking is one of the most critical steps in a retrieval pipeline, and naive fixed-token splitting damages retrieval when it cuts a sentence, paragraph or logical idea in half. A cause-remedy pair that depends on the paragraph above it retrieves as a fragment.
- **Label the fields.** Symptom, conditions, cause, fix, verification as explicit headings gives the retriever anchors and gives the answer somewhere to point.
- **Document the negative cases.** If information is not explicitly written down it does not exist in the assistant's knowledge base; an undocumented workaround cannot be answered, only guessed at.
- **Prefer an honest refusal to a guess.** Where the assistant is configurable, an explicit "I don't know" guardrail is worth more than coverage: a bot that invents a fix for an undocumented error costs more trust than one that says no documented fix exists yet.

## Re-indexing is part of publishing

Embedding rot is a maintenance hazard distinct from ordinary staleness: the published page is current and the retrieval index still serves the old text. Practitioner guidance from vendors building docs-grounded assistants is to re-embed the corpus when the embedding model meaningfully improves, when roughly 10-15% of the content has changed, or when the domain itself shifts.

Add the trigger to the maintenance plan, with the same owner as the docs release. A troubleshooting workflow that edits pages without ever re-triggering an index rebuild silently serves stale answers to the readers most likely to be mid-incident.

## Machine-readable surfaces

`llms.txt` - an H1 project name, a blockquote summary and H2-organized links, with an optional `llms-full.txt` inlining the full text - is a proposal published by Jeremy Howard of Answer.AI in September 2024. It is explicitly a proposal, not a ratified standard, with no W3C or IETF working group behind it. Treat it as cheap and optional: worth adding if the docs generator supports it, never worth a project.

The more durable version of the same idea is serving clean Markdown for any page on request, as GitHub does through its Markdown API.

Designing these machine-facing entry points across a whole SDK or API surface is a different job from making troubleshooting entries retrievable, and it belongs to samber/developer-relations-skills@coding-agent-docs-optimization. Stop here at the page level.

## The unanswered-query loop

An assistant's failure log is the newest form of the zero-result-search signal, and the strongest one, because it captures the question in the reader's own words rather than as keywords. Feed it back into step 1: unanswered or badly-answered queries become clusters, clusters become entries, and the entries reduce the next cycle's failures. Ask in the interview whether that log is accessible - many teams have it and never look at it.
