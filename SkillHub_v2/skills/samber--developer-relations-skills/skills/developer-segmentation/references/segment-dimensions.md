# Segmentation dimensions and scoring criteria

Contents: the six dimension families · the test a dimension must pass · seniority · combining dimensions · the seven scoring criteria.

## The six dimension families

| Family                     | Developer-specific values                                                                                                                                                   | Changes                                                                      | Use it when                                                                   |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| Involvement and motivation | paid professional, hobbyist, student or career-changer, researcher, OSS maintainer, non-coder building software with generative tools                                       | credibility codes, price sensitivity, whether a purchase exists at all       | free and paid audiences behave differently, or a large unpaid audience exists |
| Technographic              | primary language and runtime, framework, package manager, cloud or on-prem, adjacent tools already installed, self-hosted vs managed                                        | which SDK, samples and docs track get built; which communities are reachable | the product must be present _in_ an ecosystem to be used                      |
| Sector and workload        | web, mobile, desktop, cloud and platform, embedded and industrial IoT, consumer electronics, AR/VR, games, ML/AI, data science, extensions built on someone else's platform | the reference architecture, the integration list, the event calendar         | the same product solves different problems per workload                       |
| Firmographic               | company size, industry vertical, regulatory regime, region, in-house vs agency vs consultancy                                                                               | whether compliance material blocks adoption, whether sales is involved       | company adoption exists at all                                                |
| Behavioural                | hosting model, scale threshold crossed, build-vs-buy posture, migration in progress, existing incumbent tool                                                                | urgency, switching trigger, the proof that lands                             | usage data or sales notes show consistent behavioural clusters                |
| Role in the decision       | user, technical champion, approving architect, security or legal reviewer, economic buyer                                                                                   | who the evaluation material is written for                                   | anyone other than the user can veto or sign                                   |

## The test a dimension must pass

Ask, for two members on opposite sides of the line: _would we build something different, publish somewhere different, or prove something different?_

- Two yeses make it a dimension worth cutting on.
- One yes makes it a field inside a segment.
- Zero makes it trivia.

Second test - reachability: can you name a venue, list, registry, event or search intent where one side congregates and the other does not? A dimension you cannot address is a research finding, not a segmentation axis.

Both tests are the developer-specific form of the classic segment-validity criteria, which are worth running as a checklist when a cut feels arguable:

| Criterion      | Question for a developer cut                                                                                                                             | Typical failure                                         |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| Measurable     | can you tell which side a given developer is on, and roughly how many sit on the smaller side, from data you already hold or can ask for in one question | "innovative teams" - no observable marker, no headcount |
| Substantial    | is the smaller side big enough to justify its own artefacts                                                                                              | a segment of nine companies                             |
| Accessible     | is there a channel that reaches one side and not the other                                                                                               | a real trait with no venue attached                     |
| Differentiable | would the two sides actually react differently to the same offer                                                                                         | both sides want the same quickstart                     |
| Actionable     | does the cut change a decision you are about to make                                                                                                     | interesting, but nothing downstream consumes it         |

These criteria come from general market-segmentation practice - Kotler and Armstrong's textbook formulation, not from developer research - use them as a checklist, never cite them as a developer-audience standard.

## Seniority

Seniority is the most tempting and least useful cut. A junior and a staff engineer running the same stack on the same workload usually need the same SDK, the same docs and the same samples. It earns a place only when it maps onto something else:

- **Authority** - the person who can standardise a tool across an org is a different segment from the person who can only use it on one service.
- **Learning need** - a product used mainly by newcomers to a domain needs a teaching track a specialist would find insulting.

Otherwise record seniority as a descriptive field.

## Combining dimensions

Use exactly two. One "what we build" dimension and one "how we reach them" dimension produce a grid with three to five populated cells; most grids have empty cells, and empty cells are a useful finding.

A third dimension multiplies the cells past what a team can staff. If a third genuinely matters, it is usually a signal that two products, not one segmentation, are hiding in the audience.

Segments should emerge from observed behaviour and then be named, rather than being named first and populated afterwards. Where a survey or usage dataset exists, clustering on selected attributes produces segments nobody predicted; where it does not, cluster manually on support tickets, sales notes and community threads before writing any label.

## The seven scoring criteria

Score coarsely - 1-3, or high/medium/low. Weight against the funded driver before scoring. Effort is the denominator, never another addend: the skill's step 5 ranks segments by value per unit of effort, so a high effort score pushes a segment down rather than lifting its total.

| Criterion            | Question                                                                                                      | Fails when                                                           |
| -------------------- | ------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| Size                 | how many, with what confidence                                                                                | the only evidence is an unattributed round number                    |
| Reachability         | is there a venue this segment already gathers in, at a cost you can pay                                       | large but with no list, no ecosystem hub, no event, no search intent |
| Fit                  | does the segment already name this problem in its own words                                                   | the pain is assumed rather than quoted                               |
| Value                | what a converted member is worth - revenue, contribution, reference, talent signal                            | the value is stated in a currency the funder does not use            |
| Effort               | what must exist before this segment can succeed: SDK, docs track, compliance pack, integration                | the prerequisite list is longer than the horizon                     |
| Competitive position | does an incumbent own the default choice here, and what would trigger a switch                                | "we are better", with no switching trigger                           |
| Compounding          | does winning this segment make the next one cheaper - references, contributed integrations, ecosystem gravity | winning it leads nowhere                                             |

Weighting examples:

- a program funded for sales enablement weights value and competitive position;
- one funded for contributor community weights reachability and compounding;
- one funded for employer brand weights reachability and fit, and may score revenue value at zero without penalty.
