# Mining failure signals into a page queue

Contents: signal sources · self-serve vs. contract-bound audiences · running the clustering script · queue cut-off · what to route away from docs · KCS capture loop and role ladder · promote-to-article tooling · feedback signals.

## Table of Contents

- [Signal sources](#signal-sources)
- [Audience differences](#audience-differences)
- [Running the clustering script](#running-the-clustering-script)
- [Ranking rubric](#ranking-rubric)
- [Route away from docs](#route-away-from-docs)
- [Capture loop (KCS)](#capture-loop-kcs)
- [Who writes, who edits](#who-writes-who-edits)
- [Promote-to-article tooling (integration note)](#promote-to-article-tooling-integration-note)
- [Feedback and search signals](#feedback-and-search-signals)

## Signal sources

| Source                            | What to export                                                                             | What it over-represents                            |
| --------------------------------- | ------------------------------------------------------------------------------------------ | -------------------------------------------------- |
| Support tickets                   | Subject, first message, resolution note, tags, dates                                       | Paying customers; failures worth complaining about |
| Issue tracker                     | Titles and bodies of issues labelled question/support, plus issues closed as configuration | Vocal, technical users                             |
| Docs site search                  | Queries, result counts, click-through                                                      | People who already trust the docs                  |
| Community channels and public Q&A | Recurring question threads                                                                 | Beginners and integration-time failures            |
| Error telemetry                   | Counts per error code and per version                                                      | Everything - including failures nobody reports     |
| Sales / solutions engineers       | Their private FAQ list                                                                     | Evaluation-time blockers (limits, proxies, SSO)    |
| Reviews of the last N incidents   | Customer-visible symptoms                                                                  | Rare but expensive failures                        |

Take at least one reported source and one unreported source. Tickets alone show what people complain about; telemetry alone shows what breaks. The gap between them is where silent abandonment lives.

## Audience differences

The page anatomy is identical for every audience - the sourcing is not.

- **Self-serve / individual developers (including OSS)**: no ticket system. Issues, discussions, community channels and search logs carry the whole signal, and the reader has no escalation path, so the escape hatch must be a real, watched channel.
- **Contract-bound / enterprise**: the loudest failures sit in private tickets and never reach the public tracker. Mining only public sources under-serves exactly the accounts that pay. Expect environment-specific causes (proxies, SSO, air-gapped installs, IP allowlists) that need their own conditions block, and check whether a fix may be published at all before writing it.
- **Both**: a support macro and a public entry should never disagree. When one exists, the other is either a link to it or a superset of it.

## Running the clustering script

```bash
python3 scripts/error-cluster.py tickets.csv issues.jsonl --min-count 3 --top 40
python3 scripts/error-cluster.py export.jsonl --format json > clusters.json
python3 scripts/error-cluster.py tickets.csv --key-length 40      # merge over-split clusters
cat support-notes.txt | python3 scripts/error-cluster.py -
```

The script reads three input formats:

- CSV/TSV, where a row is a record.
- JSON/JSONL, where an object is a record.
- Plain text, where a line is a record.

From each record it extracts error-like fragments, replaces the parts that vary (paths, UUIDs, numbers, quoted values, URLs) with placeholders, and ranks clusters by how many records they appear in, with first/last-seen dates when the export carries a date field.

Read the output as a shortlist, not as a verdict:

- Merge clusters that are the same failure under different wording; lower `--key-length` when one failure keeps splitting.
- Split a cluster whose members have different causes - the same string can come from two places.
- A cluster whose `first_seen` sits just after a release is a regression to report, not a page to write.
- Records with no error text at all still matter; skim them for symptom-only failures, which become how-to pages.

Without file access or a scriptable environment, do the same pass by hand on the top 50 tickets: strip the variable parts, tally, and keep one raw example per cluster.

## Ranking rubric

The factors, the ratio they feed and the resulting order are in `SKILL.md` Step 2, where the queue is actually built. One consequence of that ranking belongs here: stop when the marginal cluster is under a handful of occurrences. Ten excellent entries beat sixty stubs, because every stub still costs a maintenance pass on every release.

## Route away from docs

Not every recurring failure is a documentation gap. Say so explicitly and hand it to the right owner:

| Symptom of the cluster                           | Real fix                                                                         |
| ------------------------------------------------ | -------------------------------------------------------------------------------- |
| Error text does not name what to do              | Rewrite the message in the product (a doc page cannot be pasted into a terminal) |
| Fix is "edit three config files in order"        | Product/DX change, or a command that does it                                     |
| Cause is account state (quota, plan, suspension) | Product surface or a support macro, not a public page                            |
| Recent spike, single version                     | Regression - file it; a page would document a bug into permanence                |
| Fix requires credentials the reader lacks        | Escalation path, documented as such                                              |
| Same failure class across several postmortems    | Scheduled product fix; the page is the interim measure only                      |

Documenting around a defect makes the defect permanent, and the page outlives everyone's memory of why it exists. Google's SRE practice states the same rule for incidents: postmortem action items must be _preventative_, not merely _mitigative_, because unaddressed outages "tend to regularly resurface and accumulate over time". Runbooks and workaround pages "can speed up incident response significantly" but are explicitly interim; the PagerDuty case study in the SRE workbook shows the postmortem, not the runbook, driving the permanent fix.

Rust runs the same gate at the other end of the scale: "not all diagnostics have a code", so only errors judged worth a durable, educational explanation get an `--explain` entry. Deciding _not_ to document an error is a legitimate output of this step.

## Capture loop (KCS)

Knowledge-Centered Service, published by the Consortium for Service Innovation, is the operating model behind this: capture knowledge _in_ the resolution workflow (solve loop), then restructure it for reuse (evolve loop). Its article fields - issue, environment, cause, resolution - are the entry block this skill writes. Two consequences for a docs team:

- The resolver writes the raw material at resolution time, while the exact error text and environment are still in front of them. Reconstructed-from-memory entries are the ones that turn out to be wrong.
- Genericize before publishing: strip the customer's identifiers, keep the environment facts that determine whether the entry applies.

Gartner endorsed the same pattern independently in August 2024 guidance: scale self-service content by "expanding content creation responsibilities to reps, enabling them to create knowledge as part of the issue resolution workflow, rather than as a separate process".

Propose the loop to the user as a standing habit, not a one-off: a template field in the ticket tool ("error text, environment, cause, resolution") plus a weekly pass that promotes repeat resolutions into entries keeps the queue from rebuilding.

## Who writes, who edits

The recurring model is distributed authoring with centralized editing, not a single owning role.

| Role                                       | Output                                                              | When                               |
| ------------------------------------------ | ------------------------------------------------------------------- | ---------------------------------- |
| Support/success engineer (KCS Contributor) | First-draft article captured during resolution                      | Solve loop                         |
| Technical writer                           | Editing, standardization, information architecture, UI-text review  | After the draft, then continuously |
| Engineer                                   | The error string itself, and long-form explanations shipped in code | At code-authoring time             |
| KCS Coach / domain expert                  | Dedup, structure, currency of the content base                      | Continuous                         |

GitLab's public handbook is the clearest published example of the engineering half. Engineers "typically write the first draft of documentation for the new features they create", and technical writers review and maintain it. GitLab also names "user interface: any user-facing text, such as UI text and error messages" as its own technical-writing work type, rather than something outside docs.

The KCS licensing model names four author roles - Candidate (work-in-progress only), Contributor (validated articles without coach review), Publisher (externally facing content), Coach (develops others' competency). The KCS v6 Practices Guide (Technique 7.1) gives the one published staffing number in this area: a start-up program runs a coach-to-knowledge-worker ratio of 1:5 to 1:8, evolving toward roughly 1:50 once mature. Use it as a planning input when the user asks what staffing a capture program costs.

## Promote-to-article tooling (integration note)

Every major helpdesk ships a promote-a-ticket-to-an-article path, so check what the user already has before proposing a manual process. None of them clusters by root cause first - that step stays yours, and skipping it produces a page that restates one customer's ticket instead of covering the failure.

- **Zendesk** - Knowledge in the Agent Workspace creates a help-center article directly from the ticket being worked. It does not pre-populate the draft from the ticket, so budget the transcription time.
- **Microsoft Dynamics 365** - "Convert To > To Knowledge Article" auto-populates the draft with the case description, and for a resolved case the case resolution and resolution description too. The cleanest capture path of the group.
- **Freshdesk** - Email-to-KBase converts an agent's ticket reply into a solution article by CC'ing the knowledge base.
- **Salesforce** - Lightning Knowledge attaches articles to cases, including at case close so a reopened case shows what the customer already tried. Only _published_ articles can be attached, so a draft entry cannot be referenced during the resolution it came from.
- **Oracle Fusion Service** - creates draft articles directly from service requests.

## Feedback and search signals

- "Was this helpful?" widgets are cheap but low-resolution: a bare thumbs-down cannot distinguish "the page is wrong" from "my problem was never self-servable". Pair the rating with an optional free-text "why" field, and expect response bias plus widget blindness when the control looks like page furniture.
- Zero-result and no-answer search queries are the strongest low-effort gap signal. In the AI-assistant era the assistant's own unanswered-query log is the same signal on a new surface: a question it could not answer is a page that does not exist yet.
