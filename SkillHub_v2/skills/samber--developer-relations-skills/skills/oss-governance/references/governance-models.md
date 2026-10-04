# Governance models

Catalogue, fit criteria, real implementations, and how projects move between models.

## The four implementable shapes

Catalogued below by project size, which is not a recommendation order - the efficiency ranking that decides what to adopt lives in step 2 of the skill.

**1. Single-maintainer authority.** One person decides; contributions welcome, direction not negotiated. Only acceptable alongside a written succession plan and a stated response expectation ("I work on this 2-5 hours a week").

**2. Maintainer council.** Everyone with merge rights also decides: lazy consensus by default, simple majority when a vote is called, two-thirds for removals and amendments. Assumes no gap between who writes the code and who decides - the natural first written governance at three to eight maintainers.

**3. Elected steering committee.** A body elected by the contributor base owns direction, policy, budget and final escalation, technical authority delegated to per-area maintainers. Its overhead - election officers, terms, eligibility, vacancies - buys legitimacy a self-selecting group cannot claim once the community outgrows the maintainer set.

**4. Federated subprojects.** A thin council charters subprojects with their own maintainers, cadence and scope. Right when parts of the project have grown separate contributor communities; wrong as a starting point, because it multiplies process before there is anyone to govern.

Translate rather than adopt two older labels:

- **BDFL** is shape 1 with a founder's aura.
- **Meritocracy** is any shape where roles are earned by contribution - a term some communities reject, so prefer "earned roles".

**Liberal contribution** is a policy layered on 2 or 3, not a fifth shape: influence follows current work rather than historic status. It widens the maintainer pool fastest and suits projects needing contributor growth more than stability.

## Fit table

Fit only - the effort, value and reversibility of each model, and the order to consider them in, are in step 2 of the skill.

| Project shape                                 | Model                                  | Main risk it addresses              |
| --------------------------------------------- | -------------------------------------- | ----------------------------------- |
| 1-2 maintainers, any user base                | Single-maintainer authority            | none - it addresses cost, not risk  |
| 3-8 maintainers, one shared area              | Maintainer council                     | ad-hoc decisions, unclear promotion |
| Many contributors, several stakeholder groups | Elected steering committee             | legitimacy, capture by one group    |
| Several components with distinct communities  | Federated subprojects                  | cross-component deadlock            |
| Single vendor, external adopters              | Council + organization-balanced voting | invisible vendor control            |

Two modifiers stack onto any row:

- **Organization-balanced voting** gives each employer one vote (independents count as their own) on listed decision types, while day-to-day merges stay on lazy consensus; it also expresses as a seat cap.
- **Delegation** gives working groups or per-area owners a named scope, which is how a council survives growth without becoming a committee.

## Reference implementations

Read the source documents before copying any of them - each is tuned to a community far larger than most projects.

| Project         | Shape it implements                         | What to take from it                                                                                        |
| --------------- | ------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| Jaeger          | maintainer council                          | a self-selecting maintainer group, lazy consensus, majority vote on demand                                  |
| Node.js         | council plus a technical steering committee | consensus-seeking with concrete fallbacks and a label as the escalation path                                |
| Python          | elected steering council                    | a bounded no-confidence procedure and a supermajority to amend the governance document itself               |
| Kubernetes      | elected committee                           | staggered terms, impartial election officers, contribution-based eligibility, company representation limits |
| Apache projects | committee with binding votes                | justified vetoes on code, majority approval on releases which cannot be vetoed                              |

Ready-to-fill templates for the council, election and federated shapes, plus an organization-balanced voting module, come from the CNCF contributor-strategy group. The smallest legally-reviewed council version is GitHub's Minimum Viable Governance. Both are permissively licensed and meant to be renamed and edited.

## Migration paths

Governance changes are themselves governance decisions - run them through the current rules, announce with a comment window, record who approved.

- **Solo → council**: the hard part is not the document, it is having a second maintainer. Recruit from reviewers, grant staged rights, then write the council rules once two people have actually been deciding together.
- **Council → elected committee**: define the electorate before the seats (contribution-based eligibility over 12 months, counting reviews, issues and docs, not just commits). Run one election before claiming the model.
- **Anything → federated**: charter the first subproject as an experiment with explicit scope and a review date; if the council still makes all its decisions, the split was premature.
- **Vendor-led → neutral**: sequence matters; the order and reasoning are in the neutrality reference.

## The constraint behind every model

Forkability is what limits authority: contributors can copy the code and leave, so deference is voluntary and permanent. Fogel's formulation is that the _possibility_ of forks matters far more than actual forks. A model surviving only because exit is expensive is a lock-in, and the audience most likely to notice is the one whose adoption you want.

## Choosing by project shape, not by ambition

Nadia Eghbal's _Working in Public_ taxonomy sorts projects on two independent axes - users and contributors - and is the fastest sanity check on a proposed model:

|                | Few contributors                                                                                 | Many contributors                                         |
| -------------- | ------------------------------------------------------------------------------------------------ | --------------------------------------------------------- |
| **Many users** | **Stadium** - the dominant modern shape: a large dependent user base served by one or two people | **Federation** - needs delegation, elections, subprojects |
| **Few users**  | **Club** - informal governance is genuinely fine                                                 | **Toy** - many hands, little dependency                   |

The consequence matters for stadiums, which most widely-depended-on libraries are: a stadium adopting an elected committee has solved a problem it does not have and left its real one - maintainer attention - untouched.
