# The decision unit inside a developer segment

Contents: the four roles · individual vs company adoption · segments with no purchase · splitting on the decision unit · questions that reveal the unit.

## The four roles

| Role                                                 | Cares about                                                                             | Convinced by                                                                                                     | Says no because                                                   |
| ---------------------------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| User / evaluator (usually the developer)             | time to first success, ergonomics, escape hatches, whether it fights the existing stack | working code, honest docs, a benchmark they can re-run, peer proof                                               | it did not work in twenty minutes, or the docs lied once          |
| Technical champion                                   | making the internal case without spending credibility                                   | migration path, reference architecture, a comparison they can paste into an internal doc, named production users | they cannot answer their architect's questions from your material |
| Approver (architect, platform lead, security, legal) | risk, stack fit, licensing, support, exit path                                          | compliance answers, SLA and support terms, licence clarity, data-handling detail, self-host or portability story | one unanswered risk question, which is enough                     |
| Economic buyer                                       | total cost, alternatives, contract terms, timing                                        | a business case in their vocabulary, procurement-ready paperwork, a trigger that makes this quarter the quarter  | no budget line, or no urgency                                     |

The champion's material is the highest-leverage artefact in company adoption: they argue when nobody from your side is in the room, and they lose on questions you could have answered in a document.

## Individual vs company adoption

|                        | Individual adoption                                                     | Company adoption                                                                                       |
| ---------------------- | ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| Who decides            | the developer, or nobody (no purchase)                                  | a developer evaluates; an architect, platform lead, security reviewer or budget owner decides          |
| Segment on             | motivation, ecosystem, workload                                         | firmographics plus which decision roles exist                                                          |
| Artefacts that move it | quickstart, samples, free tier, peer proof, ecosystem presence          | reference architectures, security and licensing clarity, migration and support paths, named references |
| Success looks like     | usage before revenue                                                    | evaluations that survive review                                                                        |
| Common trap            | assuming a purchase exists and writing enterprise material nobody reads | writing developer-delight material and losing at the security review                                   |

Most products carry both paths. Rank them for the horizon; splitting effort evenly serves neither. State which artefacts serve both so they get built once - a clear licence page, honest limits documentation and a credible production-readiness story serve every role in both paths.

## Segments with no purchase

Students, hobbyists, OSS maintainers and internal-tool builders may never generate revenue. That is a legitimate segment only when it is justified against a named non-revenue driver:

- **talent brand** - the segment contains people you want to hire, or who influence hires;
- **contributor supply** - they fix, extend and maintain what you ship;
- **future buyers** - today's hobbyist is the person who picks the stack at their next job, on a horizon measured in years, not quarters;
- **ecosystem gravity** - their integrations and content make the product the default for someone else.

Without one of these written down, the segment belongs in the anti-segment. Unjustified free audiences absorb content and support capacity precisely because they are the easiest to reach.

## Splitting on the decision unit

Two nominal members of one segment with different decision units are two segments. Common triggers:

- a regulated vertical adds a compliance approver that an unregulated one does not have;
- above a company-size threshold, procurement and vendor review appear;
- self-hosted deployments add an infrastructure owner who never touches the API;
- in an agency or consultancy, the person adopting is not the person who lives with the consequences.

## Questions that reveal the unit

Ask these of recent wins and recent losses, not in the abstract:

1. Who first tried it, and how did they hear about it?
2. Who else had to say yes, and what did they ask for?
3. Which question stalled the deal or the rollout longest?
4. Who signed, and what did they need to see?
5. In the losses, which role blocked it, and what would have unblocked them?

Five recent deals answered this way beat any assumed org chart.
