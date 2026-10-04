# Team shapes and interlocks

## Contents

- Per-shape worked examples and guards
- Interlock modes and how to write them down
- Per-team interlock defaults

## Per-shape worked examples and guards

The shapes, their staffing floors and the order they are chosen in are in step 3 of `SKILL.md`. What follows is only the material that does not fit beside the choice.

**Split by focus.** Documented example at Couchbase (Hoopy/Common Room, _A review of DevRel job titles and career progression_, May 2023):

- Developer advocacy team: sits in the product organisation, producing integrations and educational material.
- Developer relations team: sits in marketing, driving awareness and adoption.

Guard: name one person accountable for the shared voice, and one shared planning ritual, before approving the split.

**Hub-and-spoke.** The published scale-stage spokes are either functional teams (developer experience, education, community, integrations) or multi-functional regional teams - in both cases with specialization made explicit and decision authority pushed down to the spoke. Guard: the hub enables; it does not approve. A hub with an approval queue is a bottleneck wearing a standards label.

**Embedded.** Guard: the craft owner outside the host teams needs real time for the role, not a line in someone's job description, and the promotion criteria each advocate will be levelled against have to be written down before the first advocate moves.

Two checks apply to whichever shape is chosen:

- **Staffing.** Every proposed unit must be able to staff its own floor, including a backup for each surface it owns, or the shape is aspirational.
- **Conway's Law**, the sanity check the same job-titles report puts at the front of the question: the structure of a team imprints on the work it does.
  - A team split by product line produces per-product content and no cross-product story.
  - A team split by channel produces channel metrics and no journey.

Decide which imprint you want.

## Interlock modes

Borrowed from Team Topologies (Matthew Skelton and Manuel Pais). Each adjacent team gets exactly one mode, because the mode is a statement about how much of the other team's attention this consumes.

| Mode           | Definition                                                   | Bandwidth        | Fits                                                             |
| -------------- | ------------------------------------------------------------ | ---------------- | ---------------------------------------------------------------- |
| Collaboration  | working together for a defined period to discover new things | high, time-boxed | launches, a new SDK, a first community venue                     |
| X-as-a-service | one team provides, one consumes, through a clear interface   | low, ongoing     | docs requests, review queues, event support, sample-app requests |
| Facilitation   | one team helps and mentors another                           | medium, decaying | teaching engineers to write, spinning up a champions program     |

Two rules make the modes useful rather than decorative:

- Collaboration must have an end date, or it silently becomes the operating model and the team turns interrupt-driven.
- Team Topologies' cognitive-load principle applies directly: adding an interlock without removing one is the standard way a small team stops being good at anything.

Write each interlock as one line:

`<team> - <mode> - <what crosses the boundary> - <who arbitrates when it stalls>`

The arbitration column is the one people skip and the one that gets used.

## Per-team interlock defaults

Defaults, not rules - override them when the inventory says otherwise.

| Adjacent team            | Usual mode                                                 | What crosses                                              | Common failure                                                        |
| ------------------------ | ---------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------------------- |
| Product                  | collaboration during launches, X-as-a-service otherwise    | developer feedback in, roadmap and launch dates out       | permanent collaboration; DevRel becomes unpaid product management     |
| Engineering              | facilitation                                               | technical review in, writing and demo coaching out        | DevRel absorbed as overflow engineering capacity                      |
| Docs / technical writing | X-as-a-service, either direction                           | drafts, reviews, structure decisions                      | ownership left implicit, so gaps appear exactly between the two teams |
| Support                  | X-as-a-service                                             | recurring failure signals in, troubleshooting content out | DevRel used as an escalation tier                                     |
| Developer marketing      | collaboration on campaigns, X-as-a-service on distribution | content in, channels and audience data out                | the credibility surfaces get campaign-ified                           |
| Sales                    | X-as-a-service, strictly                                   | evaluation material out, field objections in              | advocates booked as pre-sales engineers                               |
| Customer success         | X-as-a-service                                             | adoption blockers in, enablement material out             | one-off customer requests crowding out reusable work                  |

Technical writing deserves the most attention: it is present on 42.7% of DevRel teams and sits under another manager in most of the rest, which makes it the single most common place for work to fall between two orgs.
