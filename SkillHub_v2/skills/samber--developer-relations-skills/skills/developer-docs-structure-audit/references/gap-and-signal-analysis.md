# Finding what is missing

## Coverage matrix

Build rows from the product's real surfaces - the things a user adopts one at a time (each SDK or language, each major feature, each deployment target, each integration) - and columns from the four modes.

| Surface      | Tutorial      | How-to   | Reference                | Explanation          |
| ------------ | ------------- | -------- | ------------------------ | -------------------- |
| Python SDK   | quickstart.md | 4 guides | api/python.md            | -                    |
| Webhooks     | -             | 1 guide  | reference/events.md      | concepts/delivery.md |
| Self-hosting | -             | -        | reference/helm-values.md | -                    |

Read it as a heat map:

- Empty **reference** on a surface users configure is the most damaging gap - it sends people to source code or support.
- Empty **how-to** on a surface with real-world variability produces repeat support tickets.
- Empty **tutorial** anywhere in the product means no supported entry point; one good tutorial per audience is usually enough, not one per feature.
- Empty **explanation** shows up later as mistrust: users cannot predict the system, so they do not build on it.
- A row that is empty except for reference describes an undocumented feature with an API dump.

Do not demand a full grid. A minor surface may legitimately need only reference plus one how-to. Justify each proposed page with a signal below, or leave the cell empty and say why.

## Demand signals

Structure cannot tell you what readers wanted and did not find. Gather what the user can actually reach - ask before assuming any of it exists, and mark any conclusion drawn without signals as an inference.

| Signal                                        | Where it lives                          | What it proves                                                                     |
| --------------------------------------------- | --------------------------------------- | ---------------------------------------------------------------------------------- |
| Site-search queries with zero results         | docs search analytics                   | A missing page, named in the user's own words                                      |
| Site-search queries with results but no click | same                                    | A page exists but its title/snippet does not match the need                        |
| Support ticket clusters                       | helpdesk tags, deflection reports       | Repeat cost of a missing or unfindable page                                        |
| Issues labelled question/support/docs         | repository                              | Public, quotable evidence for prioritization                                       |
| Repeated community questions                  | Discord/Slack/forum/public Q&A          | Same question three times = missing page                                           |
| High-exit, high-traffic pages                 | web analytics                           | Page answers the search but not the need                                           |
| Sales and solutions-engineer FAQs             | internal                                | Evaluator questions (limits, security, migration) that never reach public channels |
| Coding-agent failures against your docs       | agent transcripts, integration attempts | Missing machine-readable reference or ambiguous naming                             |

Rank gaps by evidence volume × adoption impact, not by how uncomfortable the hole looks in the matrix.

A high-exit or high-bounce page is not always a failure: it can mean the reader found the answer immediately and left satisfied. One documentation team restructured its docs around clear navigation and FAQ-style entries, then deliberately stopped treating page views and time-on-page as success metrics, tracking bounce rate, self-service rate and case deflection as positive outcomes instead (Stephan Delbos, "Drop the Docs, Get Back to What's Important! How to Create Product Documentation that Encourages User Disengagement", Write the Docs Atlantic 2023, on Mews's documentation restructuring). Pair an exit-rate reading with a support-ticket trend or a satisfaction prompt before logging it as a gap.

## Audience weighting

The same product documented for different buyers needs a different mode mix. Ask who the docs serve before judging balance.

- **Self-serve individual developers** (bottom-up, credit-card or free adoption): weight tutorials and how-tos, keep time-to-first-success short, expect entry from search on an error or a task. Explanation earns its place only where a surprising mental model blocks usage.
- **Team and enterprise adoption** (B2B, an evaluator and a signer behind the user): add explanation early - architecture, security model, limits, cost model, migration path - because someone who will never run the quickstart has to approve the choice. Reference completeness carries procurement weight; missing limits and compliance detail become sales blockers.
- **Both audiences on one site**: keep one entry point per audience rather than one merged tour, and do not let evaluator content colonise the getting-started path.
