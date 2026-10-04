# Scoring a docs set

## Layer 1 - CNCF TechDocs rubric (sourced)

The CNCF TechDocs team runs a published documentation assessment program for CNCF projects. It is the most concrete public instrument for scoring an existing docs set, and it is free to reuse on any project.

Score each top-level docs section, then the set as a whole, on the 2024 named scale:

| Score | Meaning                    |
| ----- | -------------------------- |
| 1     | Not present                |
| 2     | Needs improvement          |
| 3     | Meets standards            |
| 4     | Meets or exceeds standards |
| 5     | Exemplary                  |

An older CNCF template names only the odd anchors (1 = not present or requires significant work, 3 = present but needs work, 5 = executed extremely well). Use the named 1-5 scale; it forces a decision at 2 and 4.

Rubric categories:

- **Project documentation** (end users): Information architecture, New user content, Content maintainability, Content creation processes, Inclusive language.
- **Contributor documentation**: Communication methods documented, Beginner-friendly issue backlog, "New contributor" getting-started content, Project governance documentation.
- **Website** (infrastructure): twelve criteria covering single-sourcing, branding, accessibility, mobile, HTTPS, production-only analytics and indexing, intra-site search, and documented account custodians.

A structure audit owns the Project documentation category in full and touches Website only through intra-site search. Score contributor documentation only when the user asks for it.

**Published calibration.** The 2024 CNCF analysis of TUF scored these ratings:

- Project documentation: Information architecture 2, New user content 1, Content maintainability 3, Content creation processes 1, Inclusive language 3.
- Contributor documentation: Communication methods 3, Beginner-friendly backlog 1, "New contributor" getting-started 1, Project governance 3.

Read that as the realistic baseline for a serious open-source project with no dedicated writer: mostly 1s and 2s on entry-point and process criteria, 3s where a maintainer culture already exists. A first audit returning straight 4s usually means the rubric was applied too generously, not that the docs are exemplary.

**Deliverable shape.** CNCF splits the output into three documents:

- An analysis (ratings plus comments).
- An implementation plan that breaks recommendations into "achievable work that can be completed in constrained blocks of time".
- An issues document contributors can pick from.

Mirror that split - the report, the queue, and the tickets are three different artefacts with three different readers.

Source: github.com/cncf/techdocs; contribute.cncf.io/techdocs/analyses/2024/TUF/analysis.

## Layer 2 - structural scorecard (this skill's baseline)

The targets below are this skill's own baseline, chosen to be achievable on a mid-sized docs set. State them as such in the report and agree them with the user before scoring - a 30-page project and a 900-page platform do not pass on the same numbers.

| Measure               | How to compute                                              | Baseline target      | Source                                                                            |
| --------------------- | ----------------------------------------------------------- | -------------------- | --------------------------------------------------------------------------------- |
| Mode purity           | single-mode pages ÷ total pages                             | ≥ 90%                | self-set                                                                          |
| Surface coverage      | surfaces carrying the modes their usage requires ÷ surfaces | 100% of top surfaces | self-set                                                                          |
| Entry points          | one tutorial or quickstart per primary audience             | present              | Diátaxis (a missing quadrant strands a class of visitor)                          |
| Orphans               | pages absent from navigation                                | 0                    | self-set                                                                          |
| Dead nav entries      | nav entries with no page                                    | 0                    | self-set                                                                          |
| Broken internal links | link checker over the built site                            | 0                    | self-set                                                                          |
| Nav depth             | deepest navigation level                                    | ≤ 3                  | self-set                                                                          |
| Thin sections         | nav sections holding a single page                          | 0                    | self-set                                                                          |
| Demand coverage       | top 20 recurring questions with a findable answer           | ≥ 90%                | self-set                                                                          |
| Staleness             | pages untouched since the last major release                | ≤ 10%                | self-set                                                                          |
| ROT rate              | pages flagged Redundant, Outdated or Trivial ÷ total        | report, no target    | ROT is a standard content-audit heuristic; report the rate rather than grading it |

An audit that never gets re-scored becomes a document nobody trusts.

## ROT and inventory columns (sourced method)

The standard qualitative heuristic is **ROT** - Redundant, Outdated/Obsolete, Trivial. For many teams ROT _is_ the audit.

Kristina Halvorson's _Content Strategy for the Web_ chunks the qualitative pass into six groups:

- Usability.
- Knowledge level.
- Findability.
- Actionability.
- Audience.
- Accuracy.

Decay analysis adds a 90-day versus prior-90-day comparison from Search Console and analytics, and prioritises URLs that trip several decay signals _and_ carry an O or R flag.

Sources: NN/g "Content Inventory and Auditing 101"; Optimal Workshop; UXmatters; Click Laboratory.

## Why a fixed docs set drifts back (maturity read)

If the team has fixed its structure before and it decayed, the problem is organisational, not structural. JoAnn Hackos's Information Process Maturity Model, from _Managing Your Documentation Projects_ (1994), patterned on the software CMM, places a documentation organisation on five levels:

- Ad hoc.
- Rudimentary.
- Organized and repeatable.
- Managed and sustainable.
- Optimizing.

It assesses ten characteristics, including organizational structure, quality assurance, planning, information design, change management and collaboration.

A team at "ad hoc" or "rudimentary" has no repeatable process, so any structural fix decays. Say so in the report and put the governance layer ahead of further page surgery.

The ISO/IEC/IEEE 265xx family covers the same ground as formal standards. 26514:2022 (design and development of information for users) is the current revised base standard, and its three pillars map onto this audit's inventory, classification and validation steps:

- Audience analysis.
- Derivation of information concepts.
- Usability validation.

Sources: TCBOK; IEEE/ACM 10.1109/IPCC.2017.8013946; iso.org/standard/43073.html.
