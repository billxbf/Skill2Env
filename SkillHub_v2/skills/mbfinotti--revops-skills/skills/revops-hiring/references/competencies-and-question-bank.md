# Competencies and Question Bank

## Competency set

Define 4-6 competencies per role; they become the scorecard's rows and everything else hangs off them. There is no survey-backed RevOps competency standard; the best published starting point is Fullcast's interview guide, which scores five areas:

- Strategic thinking / business acumen.
- Technical and analytical.
- Cross-functional leadership.
- Change management and execution.
- Systems thinking and problem solving.

Adapt the set to the archetype - a systems hire weights technical depth higher, a strategist weights cross-functional leadership - and to the segment (see the B2B and B2C section of SKILL.md).

## Requirements matrix

- Must-haves: 5-7 maximum, weighted to sum to 100%. "Listing 15+ requirements signals either an unrealistic expectation or a lack of role clarity" (SyncGTM).
- Nice-to-haves: additive bonus points on top, never part of the 100%.
- Disqualifiers: a separate checklist, never negative points inside the score.
- Experience scores level-relative: the same years-of-experience number scores differently per target level, and overqualified and underqualified both score low.

## Certifications and tool depth

- **Certs are table stakes, not predictors**: the core CRM administrator certification proves configuration ability and nothing else. Generic RevOps certificates from training companies carry less weight than demonstrable platform expertise, and "a candidate may have deep [CRM] expertise and still lack the commercial judgment to prioritize the right work."
- **Test depth without over-indexing**: probe one tool to bedrock - ask the candidate to explain one data-model or automation decision they made and the trade-offs they accepted - then weight process thinking and business acumen higher. The blunt practitioner version: "I'd rather hire someone who's phenomenal at process design and mediocre at [the CRM] than the inverse."
- **SQL** is the highest-leverage transferable technical skill at every level, because it survives a stack migration.

## Question bank structure

Per competency: 2-3 behavioral questions ("Tell me about a time..."), 1-2 situational ("How would you handle..."), plus follow-up probes.

Reusable probes:

- "What was the outcome?"
- "What would you do differently?"
- "Who else was involved and what was your specific role?"
- "What was the hardest part?"

Never ask leading questions ("We value collaboration - how collaborative are you?") and never bundle two questions into one. On top of the static bank, generate candidate-specific questions from each resume's gaps and concerns.

## Domain probes - hard to fake

The strongest questions come from RevOps's own documented failure modes, not a generic bank: a candidate can rehearse a conflict story, but cannot fake an opinion on why a scoring model decayed. Ask them to defend or attack, in this order - `rehearsability, hardest to fake first: define before automate > single source of truth > measure every handoff > revenue team alignment`. The first forces the candidate to name something they would refuse to automate, which no prepared story covers. The last is the most B2B-marketing-specific and lands flat on a PLG or consumer req - delete it there rather than asking it thin.

- Single source of truth - one canonical system per object; what to do when two systems disagree.
- Define before automate - "automating a broken process just creates broken results faster"; what would they refuse to automate on day one?
- Measure every handoff - every team-to-team handoff needs an SLA, tracking, and a named owner.
- Revenue team alignment - marketing calling something an MQL that sales will not work is a definitional failure, not a data failure.

Known mistakes to probe:

- Over-weighted content downloads in scoring.
- No negative scoring.
- Set-and-forget models.
- Stage-skips and silent close-date pushes.
- Stale-deal alerts reps ignore.

Industry-commonly-cited numbers (pipeline coverage around 3-4x, speed-to-lead decay, stage-conversion bands) are prompts, not facts to recite - the signal is whether the candidate questions a number's provenance.

## Discriminating questions

Ranked by discriminating power per interview minute, best ratio first:

- efficiency: tool-first vs process-first filter > systems and process design > forecast judgment > stakeholder backbone > first principles > CRM data modelling
- interview minutes: CRM data modelling > first principles > forecast judgment == systems and process design > stakeholder backbone > tool-first filter
- reaches a competency no other question does: CRM data modelling > forecast judgment > first principles > systems and process design == stakeholder backbone > tool-first filter

Ties:

- Forecast judgment and systems-and-process design cost the same - one scenario plus two probes, about ten minutes each.
- Systems design and stakeholder backbone tie on reach because both land on change management, so running both buys a second data point rather than a second competency.

- _Tool-first versus process-first_ - the highest-yield filter at every level, and it consumes no dedicated minutes because it rides on every other question. A candidate whose first question about any problem is "what tool do you use for that?" is a red flag.
- _Systems and process design_ - "Your VP of Sales tells you the CRM data is wrong and they don't trust it. What do you do in the first 30 days?" Wrong: "I'd clean up the data." Right: structured audit, stakeholder interviews, prioritization.
- _Forecast judgment_ - "Walk me through how you would assess forecast accuracy and identify where the forecast is failing." Strong answers compare forecast categories and commit values against actuals over time. Fullcast's variant: "Our forecast accuracy is consistently off by 20-30%. How would you diagnose and fix this?"
- _Stakeholder backbone_ - "Tell me about a time you had to push back on a sales leader's request."
- _First principles_ - "How would you build a revenue forecast at a company with no clean pipeline data?" The best answers start from data-quality baselines, not forecasting methodology.
- _CRM data modelling_ - have them design a clean object structure, not populate fields: custom objects, account hierarchy, lead-to-account matching, when declarative automation beats code. Green flag: opinions about record types and the cost of nested formulas.

What this order starves: CRM data modelling - the highest ceiling on a systems req and last on ratio, because it eats a whole session and only an interviewer who has built a data model can grade it. Promote it to first when the archetype is systems and someone on the panel qualifies to score it.

Delete, do not demote: on a strategist req with no systems ownership, drop the data-modelling question outright rather than shortening it. A half-asked data model scores noise, and the shortened question still consumes the slot a better one wanted.

The ordering is a default, not a law. Re-rank it against the archetype, the level, and the panel you actually have - a panel with no forecast owner cannot grade forecast judgment, whatever its ratio says.

## Red/green scoring anchors

Camela Thompson (Head of Marketing, RevOps Co-op) published these pairs for vetting consultants; they transfer directly as anchors because the weak and strong answers are near-identical in confidence and differ only in method:

| Weak answer                                             | Strong answer                                              |
| ------------------------------------------------------- | ---------------------------------------------------------- |
| "We use a standard setup across all clients"            | "Let's meet with every stakeholder before we make changes" |
| "We'll clean up your CRM first"                         | "We'll talk to users before we touch a single record"      |
| "We'll define the scope after a few requirements calls" | "We need access first, then we'll provide thorough scope"  |

Further red flags from the same source:

- Vague timelines.
- "We'll figure that out in discovery."
- No documentation plan.
- No handoff process.

## Anchored scale and scoring rules

- Pick a scale: 1/3/5 and 1-4 are both in common use. No published research compares point counts for discriminative validity in structured-interview scorecards - the field's own comprehensive review (Levashina, Hartwell, Morgeson & Campion, 2014, Personnel Psychology) names this an open question, so ordering the two here would be false precision.
- Anchor every point, not just the endpoints: on a fixed scale length, full-point anchoring measurably resists disability bias better than endpoints-only anchoring (Reilly, Bocketti, Maser & Wennet, 2006). Write a behavioral description of what each anchor looks like _for this role_. A bare number or a generic label like "Strong" collapses into gut-feel scoring.
- Every score cites evidence: a quote or a concrete example. No evidence, no score.
- Interviewers submit scores before the debrief; debrief time goes where scores diverged; disqualifying signals are recorded separately from the score.
- Weight the recommendation by (fit × confidence), not fit alone: strong fit at low confidence means "proceed, verify later", and "insufficient data" is a valid output.
- Bias mitigations, ranked by bias removed per unit of process friction, best first: score before discussion (near-zero - a form and a rule, and it kills the anchoring on the first confident voice) > score each criterion separately (a template change, defeats the halo effect) > judge qualifications only (a redaction step someone runs per resume, for name and gender bias) > diverse panel (a standing constraint on who you have, for affinity bias). The order starves the last one, which is also the only mitigation that changes what the loop can see at all - promote it when the panel is currently homogeneous, because no scoring discipline recovers a signal nobody in the room recognizes.

## Resume flags

**Red** (Pulse, VEN Studio):

- "Strategic thinker" claimed at analyst level.
- "Owned full RevOps function" at a 30-person company.
- "Drove $50M in pipeline" from an analyst.
- Heavy consulting jargon with no named tools.

**Green:**

- Named tools with versions and stack layers.
- Specific numbers tied to specific work ("cut lead-routing SLA from 18 hours to 4").
- Promotion inside the same company.
- Candid mention of a failure and its fix.
