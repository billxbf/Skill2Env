# Worked segment map

Contents: the worked map · weak vs strong versions of each section · a rejected map · a second cut of the same audience.

The product below is illustrative: an open-source tracing library with a paid hosted backend, self-serve pricing, and a small enterprise motion. Figures are placeholders in the correct shape - replace them with your own sourced numbers.

## Table of Contents

- [The map](#the-map)
- [Cut](#cut)
- [Segments](#segments)
- [Primary](#primary)
- [Secondary](#secondary)
- [Anti-segment](#anti-segment)
- [Hypotheses](#hypotheses)
- [Implications](#implications)
- [Review](#review)
- [Weak vs strong](#weak-vs-strong)
- [A rejected map](#a-rejected-map)
- [Segments](#segments)
- [Primary](#primary)
- [Next steps](#next-steps)
- [The same audience, cut differently](#the-same-audience-cut-differently)

## The map

```
# Developer segment map  - <product>, H2 <year>

## Cut
Dimensions: workload (what they instrument) × deployment mode (self-hosted vs hosted).
Rejected: seniority  - a junior and a staff engineer instrumenting the same service need
the same SDK and the same docs. Rejected: region  - support and pricing are identical
everywhere we sell, and no artefact would change.

## Segments

| Segment | Definition | Size + confidence | Decision unit | Needs | Where they gather | Evidence |
|---|---|---|---|---|---|---|
| Solo service owners | 1-3 engineers running a handful of services, hosted everything | ~150k–300k, estimated (language-community sizing filtered to companies <20 engineers, cross-checked against 61% of signups) | user = buyer, card payment | 10-minute quickstart, free tier that survives a real service, one-file config | language-ecosystem forums, package registry, two framework Discords | 340 signups, 22 support threads, 6 interviews  - measured |
| Platform teams | 4-15 engineers owning shared infrastructure for 50+ developers | ~40k–80k, estimated (job-posting counts for platform/SRE roles at 200+ engineer companies) | user evaluates, platform lead approves, VP Eng signs | multi-tenant story, cost-control docs, migration from incumbent, self-host option | infra-focused conferences, CNCF-adjacent Slack, incident-management communities | 14 sales-call notes, 9 tickets  - measured |
| Regulated platform teams | platform teams under data-residency or audit obligations | ~8k–15k, inferred (share of the above in finance/health verticals) | adds security reviewer and legal | data-residency answers, audit log export, signed DPA, self-host parity | vertical conferences, compliance-focused peer groups | 3 lost deals, all on residency  - hypothesis |
| OSS instrumentation authors | maintainers writing exporters and integrations for other libraries | ~2k–5k, inferred | no purchase | stable plugin API, contribution guide, release predictability | the project's own issue tracker, ecosystem working groups | 31 external contributors  - measured |

## Primary
Platform teams. Score (driver = revenue): size 2, reachability 3, fit 3, value 3,
effort 2, competitive position 2, compounding 3. Beat solo service owners, which is
larger and cheaper to reach but converts at a twentieth of the value and already
succeeds without help.

## Secondary
Solo service owners  - served by artefacts platform teams already fund (quickstart,
SDK quality, free tier). No dedicated content, no dedicated events this horizon.

## Anti-segment
Regulated platform teams. Reachable and valuable, but the artefact list  - residency,
audit export, self-host parity  - is three quarters of engineering work we have not
funded. Revisit when the self-host build lands. Saying this in writing stops each
lost deal reopening the debate.

## Hypotheses
Regulated platform teams: 3 data points, below the floor. Test: read the three lost
deals end to end and interview two of the blocking reviewers. Drop the segment if
residency turns out to be a proxy for price.

## Implications
Build: multi-tenant reference architecture, cost-control guide, migration guide from
the incumbent. Publish: infra conferences and one incident-management community.
Prove: two named platform-team references with numbers.
Stop: beginner tutorial series (serves the secondary segment we already win).

## Review
Re-read <date, one quarter out>. Early re-read if: self-host ships, pricing changes,
the incumbent adds a free tier, or platform-team share of new signups passes 35%.
```

## Weak vs strong

**Segment definition**

- Weak: "Enterprise developers." Who? Doing what? Nothing follows from it.
- Strong: "4-15 engineers owning shared infrastructure for 50+ developers." A support engineer can classify a ticket into it in five seconds.

**Size**

- Weak: "About 2 million developers."
- Strong: "~40k–80k, estimated - job-posting counts for platform/SRE roles at companies above 200 engineers, as of <date>."

**Decision unit**

- Weak: "Decision authority: high."
- Strong: "User evaluates, platform lead approves, VP Eng signs; last three deals stalled on the platform lead's multi-tenancy question."

**Anti-segment**

- Weak: "We're not focused on enterprise right now."
- Strong: "Regulated platform teams - needs residency, audit export and self-host parity; three quarters of unfunded engineering. Revisit when self-host ships."

**Implications**

- Weak: "Create more content for platform teams."
- Strong: a named artefact list, a named channel, a named proof point, and one thing that stops.

## A rejected map

This one gets written constantly. It looks finished, and it fails the gate on six counts.

```
# Developer audience  - <product>

## Segments
| Segment | Description | Size |
|---|---|---|
| Beginners | Developers new to the space, learning the basics | Large |
| Professional developers | Developers using this at work | ~4 million |
| Enterprise | Big companies | Growing fast |

## Primary
Professional developers  - the biggest opportunity.

## Next steps
More content for professional developers, plus a beginner tutorial series.
```

What a reviewer should reject, in order:

1. **Seniority is the whole cut.** Beginner, professional and enterprise mix an involvement axis with a firmographic one, and neither changes the artefact: the same SDK and the same docs serve all three.
2. **No decision unit.** "Enterprise" hides an architect, a security reviewer and a budget owner behind one word, so nothing says who the material is written for.
3. **Sizes with no method.** "Large", "~4 million" and "growing fast" carry no attribution, no date, no filter and no confidence tier - and the four-million figure is almost certainly a language-ranking or account count read as a population.
4. **No anti-segment.** Every audience stays in scope, so nothing stops.
5. **Segments overlap.** A professional developer at a large company is in two rows at once; a support engineer could not classify a ticket into exactly one.
6. **The next steps contradict the ranking.** A tutorial series serves the segment the map just deprioritised, which is how the primary segment quietly loses its budget.

Rewritten, the same audience becomes the map at the top of this file:

- a workload × deployment-mode cut
- four rows a support engineer can classify into
- a decision unit per row
- ranges with methods
- one named exclusion
- a stop

## The same audience, cut differently

Under an **ecosystem** cut (language runtime × managed-vs-self-hosted), the same population produces "Go infrastructure teams", "JVM enterprise services", "Node product teams" - and the obvious action becomes SDK parity rather than multi-tenancy documentation.

Neither cut is wrong. Presenting both, then choosing, is what step 2 of the skill is for: the cut decides what the team will notice for the next quarter, and a cut chosen by default is a set of blind spots chosen by default.
