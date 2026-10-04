# Routing detail - revops-skills collection

Route only from the declared scopes below. Every "do not route here" line comes from the skill's own description, not from inference.

Nothing in this file is ranked, and nothing in it should be. Scope is a match test, not a ratio. Ranking lives in the kickoff's short-list and routine set, where several skills compete for one session (see `mbfinotti/revops-skills@revops-kickoff` § 4 and § 7).

Four skills sit at macro altitude:

- `revenue-funnel`
- `revenue-data-governance-strategy`
- `revenue-kpi-framework`
- `revops-stack-rationalization`

Each shares subject keywords with a tactical sibling and is separated from it by altitude, not by topic. Their boundary pairs below are the ones most often misrouted.

## Table of Contents

- [Per-skill signals](#per-skill-signals)
- [Boundary pairs](#boundary-pairs)
- [Ordered chains](#ordered-chains)
- [Sibling-repo recommendations](#sibling-repo-recommendations)
- [Coverage gaps (v1)](#coverage-gaps-v1)

## Per-skill signals

### `mbfinotti/revops-skills@revenue-funnel`

- Route here: design the revenue funnel model from scratch - settle what the model is for (process vs planning vs forecast) and what unit moves through it (lead, buying group, account), then the stage set, the cohort-based conversion assumptions behind the plan, and the marketing/sales/CS ownership handoffs; "design our funnel", "bowtie model", "demand waterfall", "set our conversion assumptions", no agreed stage set exists yet.
- Do not route here: auditing or rewording an existing stage set's exit criteria (`mbfinotti/revops-skills@pipeline-stage-definition-audit`), the routing or scoring logic inside a stage, or executing the handoff it designs.

### `mbfinotti/revops-skills@lead-scoring`

- Route here: design, validate, or recalibrate a lead scoring model; fit/engagement weighting, negative scoring, decay; set MQL/PQL thresholds and tiers; backtest against closed-won/lost; "our lead scores are wrong", "too many junk MQLs".
- Do not route here: lead routing or assignment - the finished score is an input to `mbfinotti/revops-skills@lead-routing`.

### `mbfinotti/revops-skills@lead-routing`

- Route here: assignment logic for inbound leads - rule precedence, lead-to-account matching, territory assignment rules, round-robin variants, fallback queues, SLA escalation, safe rollout of routing changes; "who gets this lead", leads sitting unworked in a queue.
- Do not route here: designing the lead score itself - it treats the score as an existing input.

### `mbfinotti/revops-skills@pipeline-stage-definition-audit`

- Route here: audit stage definitions against buyer-verifiable milestones; write stage exit criteria; stages named after rep activity ("demo scheduled", "proposal sent"); stage aging, conversion decay, stage-skip diagnostics; "our stages don't mean anything".
- Do not route here: redesigning the funnel from scratch; auditing individual deals within stages (that is `mbfinotti/revops-skills@sales-pipeline-hygiene`).

### `mbfinotti/revops-skills@sales-pipeline-hygiene`

- Route here: periodic, checklist-based audit of an active pipeline snapshot - stale deals against segment stage medians, close-date push anomalies, missing forecast-critical fields; exception list with per-deal dispositions; "clean up our pipeline", cleanup before a QBR.
- Do not route here: rewriting stage definitions or designing standing reminder automation - both out of its scope.

### `mbfinotti/revops-skills@sales-forecast-diagnostic`

- Route here: diagnose why an existing forecast is unreliable - stage inflation, sandbagging, deals without buyer evidence, mass-pushed close dates, wrong forecast categories, manager overrides, comp incentives rewarding bias; "why did we miss the forecast".
- Do not route here: designing the forecasting methodology itself - it only tests whether the number produced is real.

### `mbfinotti/revops-skills@revenue-leakage`

- Route here: trace where deals and revenue silently exit one specific funnel and size the loss in recoverable dollars - untracked steps, unworked leads, handoff gaps, mid-funnel stalls, billing and renewal misses; "where are we losing deals", "leaky funnel".
- Do not route here: auditing stage definitions (it takes them as given) or program-level patterns across funnels - it works one funnel instance.

### `mbfinotti/revops-skills@revenue-data-governance-strategy`

- Route here: org-wide revenue data authority - which system of record authors each object class and which source of truth is read for it, the identity-resolution spine, cross-team data contracts binding producers to consumers, where revenue metric definitions live and who signs them, federated ownership with a council and an escalation path; "finance and sales report different numbers", "we have two ARR numbers", "which system owns revenue data".
- Do not route here: field-level rules inside one CRM (`mbfinotti/revops-skills@crm-data-governance`), deciding which tools stay in the stack, or designing the metric set itself.

### `mbfinotti/revops-skills@crm-data-governance`

- Route here: field ownership, system of record per field, write precedence and conflict rules, freshness SLAs, field request-approval-deprecation lifecycle, governance cadence; "who owns this CRM field", "which system wins", field sprawl, picklist governance.
- Do not route here: deduping records, sweeping stale deals, or designing stages - it writes the rules those enforce.

### `mbfinotti/revops-skills@deal-desk-approval`

- Route here: deal desk design - tiered discount approval matrix, delegation of authority across concession levers, margin floors, exception intake, SLA clocks, precedent control; discount creep; the PLG/B2C promo-policy equivalent.
- Do not route here: business-process approvals outside the deal desk (e.g. CRM field approvals belong to `mbfinotti/revops-skills@crm-data-governance`).

### `mbfinotti/revops-skills@customer-churn-signals`

- Route here: assemble, operationally define, validate, and rank leading churn indicators into a ranked signal register - event, threshold, window, lift, lead time, coverage; "which signals actually predict churn", "our health score misses churn" (the discovery half).
- Do not route here: combining signals into one composite score, tiers, or CS playbooks - that is `mbfinotti/revops-skills@customer-health-score`.

### `mbfinotti/revops-skills@customer-health-score`

- Route here: design, validate, govern a composite health score - weighting, normalization, decay, bands, churn-risk and expansion flags, backtesting, recalibration; "green accounts keep churning".
- Do not route here: discovering which indicators predict churn - `mbfinotti/revops-skills@customer-churn-signals` owns discovery; this skill owns how signals combine.

### `mbfinotti/revops-skills@sales-to-cs-handoff`

- Route here: design and enforce the sales-to-CS handoff - gated closed-won trigger, required handoff packet, timing SLAs, kickoff meeting pattern, CS acceptance/rejection; "the CSM starts from zero", "customers repeat themselves after signing".
- Do not route here: a CSM running one individual handoff; onboarding curriculum; health scoring - it ends when the customer is received and the first-value clock runs.

### `mbfinotti/revops-skills@revenue-kpi-framework`

- Route here: design the org-wide revenue KPI framework - pick the top-of-tree outcome, decompose it into a reconciling metric tree with explicit math, name one owner per branch, pair each owned number with a guardrail counter-metric, and gate the set by company stage and business model; "which metrics should each level track", "revenue KPI tree", "pick our North Star and driver metrics".
- Do not route here: writing the board or exec report against the framework (`mbfinotti/revops-skills@revenue-reporting`), governing where metric definitions live and who signs them, or building dashboards.

### `mbfinotti/revops-skills@revenue-reporting`

- Route here: metric set and narrative for an exec/board revenue report - stable metric spine, locked definitions, plan vs actual vs forecast, presenting a miss, reconciliation and sign-off, reporting cadences; QBR revenue section, investor update.
- Do not route here: building a dashboard in a BI tool or designing the org-level KPI hierarchy - both out of its scope.

### `mbfinotti/revops-skills@revops-stack-rationalization`

- Route here: periodic portfolio review of the whole GTM/RevOps tool stack - four-channel inventory (finance, procurement, SSO, expense), function-level overlap map, TIME scoring, a keep/consolidate/replace/cut verdict per tool timed to its renewal window, and the governance that stops re-sprawl; "too many sales and marketing tools", "SaaS sprawl", "cut tooling spend", "platform vs point solutions".
- Do not route here: evaluating one candidate tool before purchase - a narrower pre-purchase job this skill excludes and no v1 skill covers; contract or legal negotiation; executing the migrations it recommends.

### `mbfinotti/revops-skills@revops-hiring`

- Route here: the hiring-manager side - archetype and level decision, outcome scorecard, interview stage map with question bank, work-sample exercise with rubric, 30-60-90 ramp plan.
- Do not route here: sourcing candidates, posting jobs, applicant tracking, or the candidate side - interview prep for someone seeking a role is `mbfinotti/revops-skills@revops-career`.

### `mbfinotti/revops-skills@revops-career`

- Route here: the candidate side - ladder placement by scope, competency gaps, evidence of structurally invisible work, the four RevOps interview exercises, compensation ask; "how do I break into RevOps".
- Do not route here: anything on the hiring side of the table - that is `mbfinotti/revops-skills@revops-hiring`.

### `mbfinotti/revops-skills@revops-radar`

- Route here: staying current - a time-budgeted watch list of RevOps podcasts, newsletters, communities, events, and people, with freshness verification and a refresh routine.
- Do not route here: any operational RevOps task. A user who asks how to _do_ something routes elsewhere; a user who asks what to _read or follow_ routes here.

### `mbfinotti/revops-skills@revops-kickoff`

- Route here: project start, periodic check-in, "which skill do I need", re-routing mid-project. This skill routes; it never performs a sibling's job itself.

## Boundary pairs

Where two or more siblings collide on keywords, decide from these declared-scope boundaries:

- **lead-scoring vs lead-routing** - scoring designs the number; routing consumes it to assign leads to reps. "Is the score right?" → scoring. "Who gets the lead?" → routing.
- **customer-churn-signals vs customer-health-score** - signals discovers and ranks individual indicators, ending at a validated register; health-score combines signals into one composite. "Which signals predict churn?" → signals. "How should signals roll up into one score?" → health-score. "Our health score misses churn" starts at signals (the inputs are wrong before the combination is).
- **revenue-funnel vs pipeline-stage-definition-audit vs sales-pipeline-hygiene vs revenue-leakage** - four different objects, at two altitudes. Revenue-funnel designs the _model_: which stages exist at all, what unit moves through them, and what conversion rates the plan assumes. Stage-definition-audit audits the _definitions_ inside an agreed model (exit criteria, buyer-verifiability). Pipeline-hygiene audits the _deals_ inside the existing stage set (staleness, pushes, missing fields). Revenue-leakage audits the _flow_ - where records exit one funnel and what the loss is worth - taking stage definitions as given. "We have no agreed funnel", "several motions share one stage list" → revenue-funnel. "Stages are meaningless" → pipeline-stage-definition-audit. "Pipeline is full of junk" → sales-pipeline-hygiene. "Deals disappear between stages" → revenue-leakage. An audit that leaves fewer than two stages usable as anchors escalates up to revenue-funnel.
- **revenue-data-governance-strategy vs crm-data-governance** - same word, two altitudes. Strategy designates which _system_ is authoritative per object class and binds producer teams to consumer teams by contract; crm-data-governance governs the _fields_ inside whichever system won. "Which system owns subscriptions?", "finance and sales quote different ARR" → strategy. "Who owns this field, how fresh must it be, who approves a new one" → crm-data-governance. A validation rule can force an opportunity to carry an ARR value but cannot make it match billing - which is why the field skill never scales up into the system one.
- **revenue-kpi-framework vs revenue-reporting vs revenue-data-governance-strategy** - three jobs over the same metrics. "What should each level track, and how does it reconcile up?" → kpi-framework. "Write the board section" → revenue-reporting. "Whose definition of ARR wins and who may change it?" → strategy.
- **revops-stack-rationalization vs the two governance skills** - rationalization rules on which _tools_ exist; the governance skills rule on which _data_ is authoritative and which fields are governed. "Do we still need this tool?" → rationalization. "Which of these two tools is authoritative for accounts?" → revenue-data-governance-strategy, and answer it first, since a consolidation must respect the designation table.
- **sales-forecast-diagnostic vs sales-pipeline-hygiene** - hygiene is the recurring data-cleanup sweep; sales-forecast-diagnostic asks whether the forecast number is real, separating data-quality from behavioral (sandbagging, overrides, comp bias) from genuine demand problems. A forecast miss caused purely by dirty data still starts at sales-forecast-diagnostic - it performs that separation, then hygiene remediates.
- **crm-data-governance vs sales-pipeline-hygiene** - governance writes the standing rules (ownership, system of record, freshness SLAs); hygiene runs the periodic sweep that catches violations. "Who owns this field / which system wins?" → governance. "Sweep the stale deals" → hygiene.
- **deal-desk-approval vs crm-data-governance** - both contain an approval workflow, over different objects. Approving a discount or non-standard deal term → deal-desk-approval. Approving a field request or schema change → crm-data-governance.
- **sales-to-cs-handoff vs customer-health-score** - handoff is the one-time post-close transfer process, ending when the customer is received; health-score is the ongoing scoring of the live account. Handoff's own scope states health scoring belongs to a sibling.
- **revops-hiring vs revops-career** - same interview loop, opposite sides of the table. Hiring manager building the packet → hiring. Candidate preparing for it → career.
- **revops-radar vs everything else** - radar curates information sources; every operational task belongs to another sibling. A question containing "newsletter", "podcast", "community", "who to follow", or "stay current" → radar; otherwise never.

## Ordered chains

Propose a chain only when the task genuinely decomposes this way; never fabricate a sequence. Each chain is listed in dependency order, not efficiency order - a later link consumes what the earlier one produces, so there is no ratio to rank.

- `revenue-funnel` → `pipeline-stage-definition-audit` → `sales-pipeline-hygiene` → `sales-forecast-diagnostic` - settle which stages exist and what unit moves through them, then fix what each one means, then clean the deals inside them, then test whether the forecast built on them is real. Start at the second link when an agreed stage model already exists: auditing exit criteria for a stage set nobody agreed writes good wording onto the wrong stages, hygiene against broken definitions flags the wrong deals, and a forecast diagnostic on a dirty pipeline can't separate data problems from behavior.
- `lead-scoring` → `lead-routing` - routing consumes the score as an input; a routing design around a broken score routes the wrong leads correctly.
- `customer-churn-signals` → `customer-health-score` → `sales-to-cs-handoff` - validated indicators feed the composite score; the score then informs what the handoff packet must carry about account risk.
- `revenue-data-governance-strategy` → `crm-data-governance` → `sales-pipeline-hygiene` - designate which system is authoritative per object class, then write the field rules inside the winning system, then sweep against them. Field rules written before the system question is settled encode the wrong system's values; sweeping without agreed rules re-litigates every exception.
- `revenue-data-governance-strategy` → `revops-stack-rationalization` - the designation table says which system must survive any consolidation. Cutting tools first can strand the authoritative store for an object class nobody re-designated.
- `revenue-kpi-framework` → `revenue-reporting` - the tree supplies the metric spine and the reconciling math; the report selects from it for one audience. A report assembled before the tree exists picks metrics that do not add up.

## Sibling-repo recommendations

`revops-skills` owns CRM/pipeline _system design_ - process, ownership, data governance. Two sibling `mbfinotti` collections cover adjacent ground this collection intentionally excludes. Recommend installing the sibling instead of stretching a task onto a skill above that doesn't cover it; never frame it as a dependency - this collection stays fully usable standalone.

### `mbfinotti/sales-skills` - sales-execution-tactical (deal-specific, in-the-moment)

Recommend the sibling repo, not a skill above, when the task is:

- Cold call scripting or opener design → `cold-call-opener`
- Discovery-call question sets → `sales-discovery-questions`
- Objection rebuttals for a live deal → `sales-objection-handling`
- Reviewing a call transcript or coaching one call → `sales-call-review`
- Mapping a specific deal's champion, economic buyer, or blockers → `deal-champion-mapping`
- Deal-level qualification red flags or MEDDPICC scoring → `deal-red-flags`, `meddpicc-scorecard`
- Negotiation concession planning or an ROI narrative for one deal → `negotiation-concession-planner`, `deal-value-calc`
- Outbound cadence, subject lines, deliverability, or personalization angles → `sales-outbound-sequence`, `cold-email-subject-line-tester`, `cold-email-deliverability`, `sales-outreach-personalization`
- Meeting recap emails → `sales-meeting-recap`
- SDR/AE hiring, career, or field radar → `sales-hiring`, `sales-career`, `sales-radar`

Recommend it for sales-leadership planning too - the macro decisions a CRO or VP Sales owns, which this collection excludes:

- Quota setting and compensation plan design → `sales-quota-setting`, `sales-comp-design`.
- Org structure and motion → `sales-org-structure`, `sales-motion`.
- ICP, market sizing, account tiering → `sales-icp-definition`, `sales-market-sizing`, `sales-account-tiering`.
- Coverage targets and capacity math → `sales-pipeline-coverage-modeling`.

Distinguish from this collection: `revops-skills` owns the _revenue system_ - funnel model, stage definitions, pipeline hygiene, forecast integrity, data authority, metric tree, and the tool stack under all of it. `sales-skills` owns the sales org's own plan and what a rep says inside one call or deal. "Design our funnel model" stays here; "set next year's quotas" and "help me open this cold call" go to the sibling.

Closest pair: `revenue-kpi-framework` (org-wide tree, every revenue function) against `sales-pipeline-coverage-modeling` (the coverage ratio behind the sales number) - the tree may carry that ratio, but it is derived on the sibling repo.

### `mbfinotti/partnerships-skills` - macro channel/partner strategy, plus affiliate/influencer/referral ops

Recommend the sibling repo, not a skill above, when the task is:

- Partner/channel ecosystem mapping, program design, or tiering → `partner-ecosystem`, `partner-channel-program`, `partner-tiering`
- Co-selling rules between direct and partner sales, or channel-conflict resolution → `co-selling-strategy`, `partner-channel-conflict`
- Partner enablement, alliance prioritization, partner economics, ecosystem expansion, marketplace strategy, joint GTM planning, or partner performance reviews → the sibling's macro skill set
- Affiliate program terms, commission structure, recruitment, onboarding, fraud detection, or payout audit → the sibling's affiliate-ops skills
- Influencer/creator sourcing, outreach, negotiation, campaign briefs, or measurement → the sibling's influencer-ops skills
- Referral incentive design or referral-abuse guardrails → `referral-incentive-design`, `referral-abuse-guardrails`

Distinguish from this collection: `mbfinotti/revops-skills@deal-desk-approval` governs _discount_ approval on a direct deal; a channel-partner deal-registration or conflict question is `co-selling-strategy`/`partner-channel-conflict` on the sibling repo, not this collection.

## Coverage gaps (v1)

No skill in the collection covers these. Name the gap; never promise or invent a skill:

- Record deduplication (merge rules, survivorship)
- Attribution modeling (multi-touch, channel credit)
- Territory design (lead-routing applies territory _assignment rules_ to leads; it does not design the territories)
- Single-tool pre-purchase evaluation (revops-stack-rationalization reviews the whole portfolio periodically; it is not a fit/cost checklist for one candidate tool)
- BI dashboard building (revenue-reporting defines metrics and narrative, revenue-kpi-framework defines the tree; neither builds dashboards)

Quota setting and compensation plan design are not gaps - they belong to `mbfinotti/sales-skills`; see below.
