# Sourced numbers, chosen baselines, and refusals

Every number this skill uses is quotable, a chosen baseline, or refused. Say which, every time you put one in a brief. A chosen baseline presented as an industry standard is the fastest way to lose an org-design argument with a finance partner.

## Quotable, with attribution

All survey figures below come from _State of Developer Relations 2024_ (11th annual edition), administered by DevRel.Agency, 310 valid respondents, 242 completions, 33 countries, 58 questions, published at `stateofdeveloperrelations.com/2024devrelreport`. It is still the latest edition, so these figures are two budget cycles old - quote them with the year attached.

| Figure                               | Value                                                                                                                                | Use it to                                                       |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------- |
| Reporting line spread                | marketing 33.1%, product 21.7%, CEO 20.3%, engineering 19.9%, sales 3.2%                                                             | prove no line holds a majority, so placement is a trade-off     |
| CEO line movement                    | 20.3%, up from 14.1%                                                                                                                 | show the founder-led line is growing, not a curiosity           |
| More than one team doing DevRel work | 43.6%, up from 33%                                                                                                                   | name fragmentation as the default starting condition            |
| Team size                            | 2-5 people 35.2% (most common), solo 18.2%, under ten 69%                                                                            | reality-check a shape copied from a large company               |
| Functions staffed                    | advocacy 82.2%, community 52.7%, technical writing 42.7%, developer marketing 37.7%, developer education 35.6%, DX engineering 27.4% | show coverage is normally partial and hats are shared           |
| Program budgets excluding salaries   | 60% (26% include salaries for all roles)                                                                                             | force the "does this number include people?" question           |
| Weekly collaboration                 | product 39%, engineering 39%, marketing 35%, support 27%, customer success 25%, sales 23%, C-level 20%                               | budget the real interrupt load before declaring interlock modes |

Non-survey sources this skill quotes:

- Conway's Law framing and the Couchbase split example - Hoopy / Common Room, _A review of DevRel job titles and career progression_, Matthew Revell and Suze Shardlow, May 2023.
- Collaboration / X-as-a-Service / Facilitation definitions and the cognitive-load principle - Team Topologies, Matthew Skelton and Manuel Pais, `teamtopologies.com/key-concepts`.
- Awareness → enablement → engagement responsibility split - Mary Thengvall, "The DevRel Path to Success", marythengvall.com, 9 March 2021.
- The scaling test - Phil Leggetter, "How to seed, grow and scale developer relations", leggetter.co.uk, 2021: "You're only really scaling a team if further investment increases output more than the increase in input."
- Levelling and the "head of" ambiguity - Kim Maida, "Forging your career in DevRel: Advocate to Exec", DevRelCon 2021.

## This skill's chosen baselines

Defensible starting points, consistent with the rest of this collection, and **chosen rather than measured**. Present each as a number the reader may move, never as a standard.

| Baseline                           | Value                                                             | Why this number                                                                                                                      |
| ---------------------------------- | ----------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| Capacity committed to planned work | at most 70% of declared capacity                                  | leaves room for support load, launches and travel, which the survey's weekly-collaboration figures show is a real and recurring draw |
| Shape threshold                    | under roughly ten full-time people, centralized only              | every other shape spends headcount on coordination; 69% of teams are under ten, so this is the common case, not the exception        |
| Surface staffing floor             | one accountable owner plus one named backup per surface           | a bus factor of one is an outage waiting for a resignation                                                                           |
| Reporting-line review              | a dated review, plus an automatic re-run when the sponsor changes | the survey shows placement moves; the interval is yours to set                                                                       |
| Interlock cap                      | one interaction mode per adjacent team                            | more than one mode per team means nobody can say what the boundary is                                                                |

## Numbers to refuse, and what to do instead

Refusing a number is a finding, not an oversight. Fill each with a derivation you show, never with a figure you invent.

- **Headcount ratios.** Every circulating ratio of advocates to developers, product lines, regions or engineers is a single-company anecdote rather than a measured standard. Derive staffing from the surface inventory, and say in the brief that that is what you did.
- **Levelled maturity models.** The Developer Relations Foundation (hosted by the Linux Foundation) states the intent to provide canonical definitions of DevRel structure and organization, and its published material is definitional rather than levelled. Cite it as the field's vendor-neutral body, never as a levelled model, and never invent levels for it.
- **Compensation bands.** DevRel roles are thin in salary-banding datasets, so a band quoted into a brief is guesswork wearing a decimal point. Send the user to live market data instead, and keep compensation out of the org design brief entirely.

## General management numbers - sanity checks only

Generic org-planning and capacity-planning tooling circulates figures like:

- Span of control: 5-8 direct reports.
- IC-to-manager ratio: between 6:1 and 10:1.
- Utilization targets: 75-80% for ICs, 60-70% for managers, 50-60% for interrupt-driven roles.

None is specific to DevRel, and each circulates as convention rather than measurement.

Use them one way only: as a sanity check when a proposed shape adds a management layer. A hub-and-spoke design that gives a hub lead two reports, or a centralized team that gives one manager fourteen, is worth questioning - but say in the brief that the check comes from general management practice, not from DevRel data. The interrupt-driven utilization row is also the closest external echo of the 70% baseline above - an echo, not a source, since it is convention in exactly the same way.
