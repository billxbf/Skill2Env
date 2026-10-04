# Education charter template

Contents: the charter structure · a worked positive example · the same charter written badly · weak vs. strong per section.

Present the charter section by section and get explicit approval on each before writing the next.

## Table of Contents

- [Structure](#structure)
- [Gate verdict](#gate-verdict)
- [Audience and motion](#audience-and-motion)
- [Chosen tier](#chosen-tier)
- [Competency map](#competency-map)
- [Credential decision](#credential-decision)
- [Operating model](#operating-model)
- [Budget shape](#budget-shape)
- [Measurement plan](#measurement-plan)
- [Kill rule](#kill-rule)
- [First 90 days](#first-90-days)
- [Where each number comes from](#where-each-number-comes-from)
- [Worked example (positive)](#worked-example-positive)
- [Gate verdict](#gate-verdict)
- [Audience and motion](#audience-and-motion)
- [Chosen tier](#chosen-tier)
- [Competency map](#competency-map)
- [Credential decision](#credential-decision)
- [Operating model](#operating-model)
- [Budget shape](#budget-shape)
- [Measurement plan](#measurement-plan)
- [Kill rule](#kill-rule)
- [First 90 days](#first-90-days)
- [The same charter written badly](#the-same-charter-written-badly)
- [Weak vs. strong, per section](#weak-vs-strong-per-section)

## Structure

```
# Developer education charter - <product>, <period>

## Gate verdict
One sentence: education is / is not the right fix, the evidence behind it, and the
cheaper alternative that was rejected and why.

## Audience and motion
Who the learner is, which motion they belong to (enterprise, partner/SI, bottom-up
individual, student), and who consumes the outcome.

## Chosen tier
The rung, the rejected rungs with reasons, and the observable condition that would
trigger the next rung.

## Competency map
Job tasks → competencies → evidence per competency → modules. Every module traces
to a task.

## Credential decision
Rung, the named external consumer who will act on it, validity and renewal, or an
explicit "no credential" with the reason.

## Operating model
Named owner with weekly hours. Authoring, technical review, lab maintenance and
learner support, each in hours per week. Platform class and where the source lives.
Refresh trigger bound to the product's release cadence. Pricing. Localization stance.
Partner delivery.

## Budget shape
Year-one build and year-two recurring, separately. Recurring is the number that
decides the program.

## Measurement plan
One primary metric per Kirkpatrick level, first-cohort target, the identity join
that makes levels 3-4 possible, and the levels deliberately not measured this year.

## Kill rule
Metric, threshold, review date, action.

## First 90 days
Sequenced, with the first learner-visible artefact dated.

## Where each number comes from
Every figure above in one list, each marked sourced (with vendor and read date) or
own baseline (with how it was derived). Anything neither goes back out of the charter.
```

## Worked example (positive)

Illustrative product: a hosted data-pipeline platform with a self-serve tier and an enterprise motion. **Every figure below is invented** - partner counts, hours, pass rates and targets alike - and shows only the shape and level of specificity to aim for. Replace each number with one you measured, and mark it as yours.

```
# Developer education charter - <product>, <year> H2

## Gate verdict
Education is justified for the partner motion only: three of five implementation
partners shipped pipelines that failed our own review, and two enterprise deals
stalled on "who on your side is trained". Rejected cheaper alternative: better docs
IA - partners find the docs, follow them, and still design the wrong topology, which
is a competence gap, not a findability gap.

## Audience and motion
Primary: implementation engineers at the five contracted SI partners (~40 people).
Secondary: platform engineers at enterprise customers (~15 accounts).
Not in scope: self-serve individual users - they succeed on quickstarts today.

## Chosen tier
Structured curriculum with labs (rung 3), plus a skill badge (rung 4) for the two
partner-critical tasks. Rejected: curated path - partners already read everything
and still fail. Rejected: proctored certification - no standard-setting budget and
no third-party consumer beyond our own partner contracts. Escalation trigger to
certification: a partner contract or a customer RFP requires an independently
verifiable credential, twice, in one quarter.

## Competency map
Job analysis from 9 partner-engineer interviews, 6 months of escalations, and the
review notes on the three failed implementations. Four competencies: topology design,
backfill and replay, failure handling and alerting, cost control. Evidence: one graded
lab each. 11 modules, all tracing to a competency; 3 existing tutorials re-used, 8
authored.

## Credential decision
Skill badges for topology design and failure handling. External consumer: our own
partner tier requirements - a Gold partner needs two badged engineers, effective next
contract cycle. Open Badges format so partner engineers keep it on their own profiles.
No expiry in year one; revisit when the topology model changes.

## Operating model
Owner: <named person>, 12h/week, accountable for curriculum truth.
Authoring 16h/week (2 people), technical review 4h/week from the platform team,
lab maintenance 6h/week, learner support 3h/week.
Platform: hands-on lab platform embedded in the docs site; every lesson and lab source
in our own repository, in Markdown plus Terraform.
Refresh trigger: re-align within 4 weeks of any minor release that changes the pipeline
API; full review each quarter.
Pricing: free to contracted partners. Localization: none until a non-English partner
region proves demand. Partner delivery: train-the-trainer for the two largest partners
in year two, not year one.

## Budget shape
Year one: build 240 person-hours plus lab platform subscription.
Year two recurring: ~30h/week steady state, dominated by lab maintenance and
per-release re-alignment. If year two cannot be staffed, do not start year one.

## Measurement plan
Reaction: per-module drop-off, target <25% at any single module.
Learning: lab pass rate, target 70% within two attempts for cohort one.
Behavior: partner implementations passing our architecture review first time,
baseline 2/5, target 4/5 within two quarters.
Results: enterprise deals stalled on trained-staff objections, baseline 2 per quarter,
target 0.
Identity join: partner engineer email → lab platform account → implementation review
record, agreed with the partner ops team before launch.
Not measured this year: revenue attribution - no clean counterfactual with five partners.

## Kill rule
If partner implementations passing first-time review is still below 3/5 at the review
date <date, two quarters out>, stop authoring, keep the two badge labs on maintenance,
and reopen the gate with the new evidence.

## First 90 days
Weeks 1-3 job task analysis write-up and competency sign-off with partner ops.
Weeks 4-7 topology-design module and its lab, piloted with one partner.
Weeks 8-10 failure-handling module and lab.
Weeks 11-13 badge issuance path, first cohort of 8 engineers, baseline metrics captured.
```

## The same charter written badly

```
# Developer Academy

We are launching <product> Academy to educate our developer community and become the
go-to learning destination for our ecosystem.

Audience: all developers.
Program: a full curriculum with courses, videos and a certification, so our users can
prove their expertise.
Platform: we will evaluate LMS vendors.
Team: the DevRel team will own it.
Success: 1,000 course enrolments and high satisfaction scores in year one.
```

Everything wrong with it, in order:

1. No evidence.
2. No rejected alternative.
3. An audience that cannot be excluded from.
4. A top-rung credential chosen by ambition.
5. A platform decision deferred past the point where it changes the cost.
6. A team label instead of a named owner with hours.
7. No refresh trigger.
8. No year-two budget.
9. Level-1-and-2-only metrics.
10. No kill rule.
11. A target of 1,000 enrolments with no stated origin - invented, borrowed from a competitor's press release, nobody can tell.

It will be stale within two releases and nobody will be accountable for that.

## Weak vs. strong, per section

**Gate verdict**

- Weak: "Our users need more education."
- Strong: "Three of five partners shipped failing implementations after reading correct docs - a competence gap, not a findability gap."

**Tier choice**

- Weak: "A full academy with certification."
- Strong: "Rung 3 plus two skill badges; certification rejected for lack of standard-setting budget; escalation trigger written as an observable condition."

**Owner**

- Weak: "Owned by DevRel."
- Strong: "<named person>, 12h/week, accountable for curriculum truth."

**Refresh trigger**

- Weak: "Content will be reviewed regularly."
- Strong: "Re-aligned within 4 weeks of any minor release changing the pipeline API."

**Measurement**

- Weak: "1,000 enrolments and a 4.5/5 rating."
- Strong: "Partner implementations passing architecture review first time: 2/5 today, 4/5 in two quarters, joined via partner engineer email to the review record."

**Kill rule**

- Weak: "We will review the program annually."
- Strong: "Below 3/5 at <date> → stop authoring, keep two labs on maintenance, reopen the gate."
