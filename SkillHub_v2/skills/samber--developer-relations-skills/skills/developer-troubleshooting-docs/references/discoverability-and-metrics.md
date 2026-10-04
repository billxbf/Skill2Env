# Discoverability, verification and measurement

Contents: how readers arrive · page-level findability · wiring the product back into docs · what no longer works · verification protocol · metrics · sourced benchmarks and numbers to refuse · freshness · pass threshold · maintenance triggers.

## How readers arrive

A developer hitting an error pastes the string somewhere: a search engine, an assistant, the docs search box, or the issue tracker. Nobody browses a troubleshooting section speculatively. Every findability decision follows from that.

Assistants now sit between many readers and the docs - they retrieve and paraphrase whichever page states the error, the cause and the steps most explicitly. The structure that helps a human scanner (labelled fields, one cause per block, fenced error text) is the same structure that survives retrieval, so there is no separate optimization to do.

## Page-level findability

- Put the error string verbatim in the title, the first heading and the body. "Troubleshooting authentication" never matches a search for `invalid_grant`.
- Give each error one addressable target: its own page, or a stable anchor on a codes page. A code buried mid-paragraph cannot be linked from the product.
- Answer in the first screen. Message, cause, first fix - before any preamble about the feature.
- Keep the page indexable: no login wall, no client-side-only rendering, stable URL, redirect if it moves.
- Name the versions the entry applies to on the page, not just in a sidebar; readers land on old copies.
- Cross-link the entry from the page where the error is produced (the auth guide, the deploy step), not only the reverse.

## Wiring the product back into the docs

The strongest referrer is the failure itself.

- Ship a documentation URL in the error payload. Stripe's API errors carry a `doc_url` attribute pointing at that code's entry, so the integration surfaces the link at failure time.
- Give the CLI an explain path: `rustc --explain E0382` prints the same content as the web page, in the terminal where the reader already is.
- Keep identifiers stable across releases. Renaming an error code invalidates every link, bookmark and cached answer pointing at it.
- Make the emitted string and the entry title identical strings; two spellings of one error halve the match rate.

## What no longer works

- **FAQ structured data**: eligibility was cut to well-known government and health sites in 2023, and Google Search Central announced the rich result stopped appearing entirely on 7 May 2026, removing the documentation in June 2026. Marking troubleshooting content as `FAQPage` for search real estate now buys nothing.
- **Question-shaped headings written for search rather than for readers** ("Why does my build fail?") when the reader is searching an exact string.
- **A single mega "Troubleshooting" page** holding thirty issues: only one of them can win the query, anchors get lost in caches, and the page becomes unmaintainable.

## Verification protocol

Publish nothing that has not been run.

1. Reproduce the error on a supported version, and capture the emitted text from that run.
2. Execute the fix exactly as written, from the state the reader is in - not from your already-configured machine.
3. Record the post-fix signal as the "confirm it worked" line.
4. Check applicability at both edges: the oldest supported version and the current one. Note where behaviour differs.
5. Have someone who did not write the entry follow it cold. Their first hesitation marks the step with an unstated assumption.
6. Re-check every command and placeholder for leaked credentials and customer identifiers.

Entries that cannot be reproduced (environment-specific, third-party, intermittent) get published only with an explicit "reported under these conditions, not reproduced here" note - an unverified fix stated confidently costs more trust than an honest gap. Write the Docs' documentation principles state the underlying rule directly: "Consider incorrect documentation to be worse than missing documentation."

The Good Docs Project applies the same bar as a shipping gate: publish a troubleshooting page only if the team can test the fixes on every supported platform and keep them current. An untested page burns the reader's remaining patience at the exact moment they have least of it.

## Metrics

| Metric                                        | How to read it                                                                                                                |
| --------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Cluster coverage                              | Share of the top-N clusters with a published entry. The headline number.                                                      |
| Ticket volume per covered error               | Compare fixed windows before and after publication. Per-error deflection is measurable; a site-wide "deflection rate" is not. |
| Zero-result docs searches for covered strings | Should reach zero; a nonzero value usually means the string is not verbatim on the page.                                      |
| Entry as first search result for its string   | Check per entry on the real search surface, not in an SEO tool.                                                               |
| Time-to-resolve on tickets linking the entry  | Falls when the entry is good; rises when it is stale and readers try it first.                                                |
| Entries touched since the last release        | Staleness proxy - publishing volume without this number is vanity.                                                            |
| Escape-hatch quality                          | Share of escalations that arrive with the attachments the entry asked for.                                                    |

Deep instrumentation across devrel surfaces belongs to the analytics skill; the numbers above only need docs search, ticket counts and page analytics.

## Sourced benchmarks, and the numbers to refuse

Set expectations against published data rather than ambition.

- **The self-service ceiling.** Gartner's December 2023 survey of 5,728 customers found only 14% of customer service and support issues fully resolved in self-service, and only 36% even for issues customers rated "very simple", despite 73% using self-service at some point. Gartner Senior Director Eric Keller: "while 73% of customers use self-service at some point in their customer service journey, it's concerning to see that so few fully resolve there." An earlier Gartner survey (n=8,398) reported 9%. Best-in-class self-service does not fully resolve most contacts; write the objective accordingly.
- **The loyalty case.** CEB/Gartner research published as Dixon, Freeman and Toman, "Stop Trying to Delight Your Customers" (_Harvard Business Review_, 2010) and expanded in _The Effortless Experience_ (2013): 96% of customers who experience a high-effort service interaction become more disloyal, against 9% for a low-effort interaction. This is the argument for the work that survives a stakeholder who does not believe in ticket deflection.
- **Resolution over deflection.** Practitioner analysis argues resolution rate matters more than deflection rate, and that cost per resolution is the true efficiency metric because it accounts for the repeat contacts that cost-per-contact hides.
- **Refuse the folklore.** The widely repeated deflection percentages and the "$15-$50 per support ticket" figure circulate without traceable methodology. Treat any unattributed deflection or per-ticket cost number as marketing; use the team's own finance figures or state that the number is unknown.

## Freshness

No published, docs-specific freshness SLA from a named vendor could be verified for troubleshooting content; the commonly cited cadence guidance is SEO-oriented (a substantive update changing roughly 20-30% of textual content, with date-only changes counting against quality). Two workable rules in its absence:

- Refresh whenever the product changes - the trigger is the release, not the calendar.
- If a competent reader could point at a provably stale sentence, the page is overdue.

## Pass threshold

Every entry ships with all six parts present:

- verbatim message
- applicability
- cause
- executed fix
- confirmation signal
- escape hatch

Five out of six is a draft. That gate is structural and non-negotiable.

The coverage number is not. **80% of the top 20 clusters within the current cycle is this skill's self-set baseline, not a published benchmark** - negotiate it with the user against real capacity, write down the number you agreed, and re-run the clustering pass afterwards to compare. The same top clusters reappearing unchanged is the signal that the entries are not being found, not that more entries are needed.

## Maintenance triggers

- A release changes an error's text, code or cause → update or retire the entry in the same release.
- The underlying bug ships a fix → move the known-issues entry into the changelog and delete it.
- An entry's cluster disappears from the mining pass for two cycles → archive it rather than keeping it in the navigation.
- The escape hatch's channel closes or moves → fix every entry pointing at it; a dead escape hatch converts a helped reader into an angry one.
