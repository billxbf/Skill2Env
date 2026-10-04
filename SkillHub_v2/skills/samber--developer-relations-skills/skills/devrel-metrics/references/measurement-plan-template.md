# Measurement framework template and worked example

## Contents

- [Template](#template)
- [Worked example](#worked-example)
- [Weak versus strong, section by section](#weak-versus-strong-section-by-section)

## Template

```markdown
# DevRel measurement framework - <company>, <horizon>

## Driver and goals

Funded driver: <one of the seven, in the funder's words> - owner: <name, role>
Goals this horizon: <at most three, each traceable to a drop-off or a business need>

## Metric sheet

| #   | Metric | Tier | Definition | Source | Baseline | Threshold | Owner | Action if breached |
| --- | ------ | ---- | ---------- | ------ | -------- | --------- | ----- | ------------------ |

Primary metric per goal is marked **P**. Total rows: 5-8.
Every threshold carries a source tag in its own cell: `(published: <who published it>)`,
`(baseline)` for a line derived from this program's own history, or `(hypothesis)` for a
circulating number being tested. A cell with no tag is not ready to ship.

## Attribution rule

Methods in use and what each may claim. Lookback window. Stage condition.
What a rule change does to the trend. Blind spots this rule cannot see.

## Reporting

Cadence: <monthly operational / quarterly decision / annual reset>
Audience and format per cadence.
The five-sentence summary the funder can repeat without you.

## Known blind spots

<what this framework cannot observe, and what it would take to observe it>

## Review

Next review: <date>. Kill-rule status per metric (cycles since it last changed a decision).
```

## Worked example

Fictional but realistic: a Series A API company, self-serve entry with a sales-assisted enterprise tier, one advocate plus one docs engineer.

```markdown
# DevRel measurement framework - Northwind API, H2

## Driver and goals

Funded driver: developer enablement - "developers sign up and never get their first call working"

- owner: VP Product.
  Goals: (1) raise first-success rate on the self-serve path; (2) cut the support load new
  accounts create; (3) keep an honest read on whether enablement work reaches enterprise deals.

## Metric sheet

| #       | Metric                                              | Tier            | Definition                                                                               | Source                                           | Baseline                         | Threshold                                                                             | Owner         | Action if breached                                                                          |
| ------- | --------------------------------------------------- | --------------- | ---------------------------------------------------------------------------------------- | ------------------------------------------------ | -------------------------------- | ------------------------------------------------------------------------------------- | ------------- | ------------------------------------------------------------------------------------------- |
| 1 **P** | First-success rate, 7 days                          | Enablement      | share of new accounts making a successful authenticated API call within 7 days of signup | product analytics, `first_successful_call` event | 22% (Q1 21%, Q2 23%, Q3 22%)     | below 20% for two consecutive months (baseline)                                       | docs engineer | run a cold-run test of the quickstart and fix the top step failure before new content ships |
| 2       | Median time to first success                        | Enablement      | signup → `first_successful_call`, median                                                 | product analytics                                | 41 min                           | above 60 min (baseline)                                                               | docs engineer | instrument step drop-off and locate the slow step                                           |
| 3       | Step-level drop-off, quickstart                     | Enablement      | share abandoning at each documented step                                                 | docs + product analytics                         | baselining                       | -                                                                                     | docs engineer | set threshold at next review                                                                |
| 4       | Support tickets per 100 new accounts, first 30 days | Enablement      | tickets opened ÷ new accounts × 100                                                      | support system                                   | 14                               | above 18 (baseline)                                                                   | support lead  | mine the top three ticket topics into troubleshooting pages                                 |
| 5 **P** | 30-day retention of first-success cohort            | Product impact  | still making calls 30 days after first success, by monthly cohort                        | product analytics                                | 58%                              | below 50% (baseline)                                                                  | advocate      | interview five lapsed accounts before proposing anything                                    |
| 6       | Self-reported first touch                           | Engagement      | signup question, stable option list                                                      | signup survey                                    | 61% response rate                | response rate below 40% (hypothesis - a circulating figure, not a measured benchmark) | advocate      | shorten or reposition the question                                                          |
| 7 **P** | Influenced pipeline                                 | Business impact | see attribution rule                                                                     | CRM                                              | €0 recorded (rule new this half) | reported, not targeted, for two quarters                                              | VP Product    | none - baselining                                                                           |
| 8       | Verbatim evidence                                   | Qualitative     | quotes and friction findings with source, date and the fix shipped                       | manual log                                       | 4 per quarter                    | fewer than 2 (baseline)                                                               | advocate      | schedule two user conversations                                                             |

## Attribution rule

Self-reported first touch is the standing instrument, reported as "self-reported", never as
attribution. Tagged links are used per campaign for artifact comparison only, never for totals.
An opportunity is DevRel-influenced when, in the 180 days before it reached stage 2, a contact on
the account attended a program event, had a public question answered by the team, or named a
program surface as first touch. Influenced value is never presented as sourced; Marketing may
claim the same opportunities. The rule is fixed for the fiscal year; any change is announced as a
restatement.

Blind spots: word-of-mouth inside a company, docs read without signing up, AI assistants
answering from our docs without a visit, and anything reaching an enterprise buyer through a
partner.

## Reporting

Monthly: metrics 1-4 and 6 to the product team, one page, trend lines against baseline.
Quarterly: full sheet plus the qualitative evidence to the VP Product and the exec team.
Annual: re-derive the sheet from the driver; assume half the metrics change.

Five-sentence summary: "New developers get their first API call working 22% of the time within a
week, and we are moving that to the high twenties this half. The step data will tell us which
part of the quickstart is losing them. Accounts that reach first success stay: 58% are still
calling at 30 days. We report enterprise influence, not sourced revenue, and the rule is written
down. Everything else we publish is an input to those numbers, not a result."

## Known blind spots

No visibility into docs readers who never sign up. No identity link between community members and
accounts, so community-to-expansion cannot be measured this half; it needs an identity mapping in
the CRM, roughly two engineering days.

## Review

Next review: end of Q4. Kill-rule status: metric 6 has not changed a decision in one cycle.
```

## Weak versus strong, section by section

**Driver**

- Weak: "Grow developer adoption and community engagement while supporting sales."
- Strong: "Developer enablement - developers sign up and never get their first call working. Owner: VP Product."

The weak version names three drivers, so every candidate metric scores equally and the sheet fills with everything measurable.

**A metric row**

- Weak: `Docs traffic | up 15% | marketing dashboard`
- Strong: `First-success rate, 7 days | Enablement | share of new accounts making a successful authenticated API call within 7 days | product analytics, first_successful_call event | 22% | below 20% two months running | docs engineer | cold-run the quickstart, fix the top step failure`

The weak row cannot be acted on, cannot be audited, and cannot fall for a reason anyone can name.

**A threshold**

- Weak: `first response within 24 hours - industry standard`
- Strong: `first response within 24 hours (self-set hypothesis - widely repeated, unpublished; our trailing median is 31 hours, revisit after three periods)`. Confirmed via search: CHAOSS's own guidance explicitly avoids hardcoding a universal number, offering "two business days" only as a worked example of a self-selected benchmark - not 24 hours, and not a target CHAOSS itself endorses.

The weak version invites exactly one question - "whose standard?" - and it has no answer. The strong version survives that question, and it also tells the reader what the team is actually doing about the gap. The same applies to any figure lifted from a conference talk. CHAOSS, the only vendor-neutral publisher of repository health definitions, deliberately leaves the target for each of its four starter metrics to the project, so a repository threshold presented as an external standard is almost certainly folklore.

**Attribution**

- Weak: "DevRel drove €400K in pipeline this quarter."
- Strong: "€400K of pipeline is DevRel-influenced under the written rule; Marketing claims the same opportunities. Sourced revenue is not something this team measures."

The weak version wins one meeting and loses the next one, when someone asks Sales for the same number.

**Reporting**

- Weak: a 30-row dashboard, refreshed when someone remembers.
- Strong: eight rows, a named owner each, monthly operational read and quarterly decision read, with a kill rule that removes anything which has not changed a decision in two cycles.

**Blind spots**

- Weak: section omitted.
- Strong: three named gaps with the cost of closing one of them.

Publishing the gaps is what makes the rest of the sheet believable. An exec who finds an unstated gap discounts everything else on the page.
