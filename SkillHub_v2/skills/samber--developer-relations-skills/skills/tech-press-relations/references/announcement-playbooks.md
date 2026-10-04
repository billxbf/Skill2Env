# Announcement Playbooks

Contents: nine announcement classes · the two that need special handling · when there is no news · reactive coverage.

Read the class that matches before drafting. Each entry gives the hook that earns coverage, the trap that kills it, and what the briefing pack needs beyond the standard contents.

## Funding round

- **Hook** - what the money makes possible that was impossible before, and the category thesis the investors are betting on. The round is the occasion, not the story.
- **Trap** - treating the amount as inherently newsworthy. Unless the size or the backer is unusual, "we raised" is a form.
- **Pack** - round size, lead, participants, prior total, what changes operationally, and whether hiring numbers can be quoted.
- **Timing** - investor communications and any disclosure obligation set the date; confirm both before offering an exclusive.

## General availability or exit from beta

- **Hook** - the problem class now solved at production scale, with a named early user and their numbers.
- **Trap** - announcing into a category the reader already knows with no differentiator beyond speed adjectives.
- **Pack** - the named customer, their workload shape, the SLA or scale commitment, and the pricing.

## Major version with breaking changes

- **Hook** - the engineering decision behind the break, its measured payoff, and its honest migration cost.
- **Trap** - framing a break as pure upside. The readers of technical press are the people who must migrate; they will find the cost with or without you.
- **Pack** - migration guide, deprecation timeline, codemod or compatibility layer, and the count of affected downstream projects.
- **Route** - the migration document itself is samber/developer-relations-skills@version-migration-guide.

## Benchmark or research data drop

- **Hook** - an original number nobody else has, framed as an industry benchmark rather than a product claim.
- **Trap** - vendor-run comparisons against competitors. They are challenged within hours unless the harness is public and reproducible.
- **Pack** - methodology, dataset or its anonymised form, the harness, hardware and versions, and a stated limitations section.
- **Bonus** - a benchmark published annually becomes a citable event that earns coverage on a schedule.

## Licence change

- **Hook** - the economics that forced it, stated plainly, and exactly what existing users keep.
- **Trap** - calling it a clarification. Every reader recognises the move and the euphemism becomes the story.
- **Pack** - the old and new licences, the conversion or grant terms, an FAQ answering fork and vendor questions, and the reasoning in numbers.
- **Plan for hostility** - brief the spokesperson to argue the case on record, expect fork announcements, and decide in advance what would make you reverse.
- **The precedent to plan against** - HashiCorp moved Terraform from MPL 2.0 to the Business Source License in August 2023. The OpenTF manifesto appeared within days and was ultimately endorsed by more than 140 companies and over 700 individuals. The Linux Foundation launched the OpenTofu fork on 20 September 2023, and a cease-and-desist HashiCorp sent in April 2024 was publicly rebutted and went no further. Organised opposition on this timescale is the base case for an established project, not the worst case.
- **Route** - the underlying decision is samber/developer-relations-skills@oss-license-strategy.

## Security incident or CVE

- **Hook** - timeline, blast radius, fix, and what changed in the process so it does not recur.
- **Trap** - letting news-cycle convenience influence disclosure timing. The coordinated-disclosure schedule governs; press planning fits around it, never the reverse.
- **Pack** - advisory, affected versions, patched versions, workarounds, detection guidance, credit to the reporter of the vulnerability.
- **Tone** - no minimising language, no passive voice hiding who did what. This class is judged on candour and speed alone.
- **Prerequisite** - coordinated disclosure only works if a monitored private security contact was published before any of this. Google's OSS Vulnerability Guide and GitHub Security Lab both describe the same sequence: private report, private advisory, patch, then public detail with credit to the reporter.

## Acquisition or merger

- **Hook** - what happens to the open-source project, the pricing, the API and the team. That is the entire story for this audience.
- **Trap** - silence on the parts users fear. The unanswered question becomes the headline.
- **Pack** - commitments with dates, who stays, what the licence and roadmap do, and the migration path if anything sunsets.

## Donating a project to a foundation

- **Hook** - the governance change and what vendor neutrality unlocks for adopters and contributors.
- **Trap** - presenting it as generosity. It is a governance decision with consequences, and the interesting question is who now decides what.
- **Pack** - the foundation and stage, the governance model, trademark disposition, maintainer roster, and who funds ongoing work.
- **Route** - the model choice is samber/developer-relations-skills@oss-governance.

## Customer outcome

- **Hook** - architecture before and after, with numbers the customer will stand behind publicly.
- **Trap** - an unnamed "leading enterprise". Anonymity halves the value and invites the reader to assume the worst.
- **Pack** - the customer's approval in writing, their spokesperson's availability, and the metric provenance.
- **Route** - build the story with samber/developer-relations-skills@developer-case-study first, then pitch it.

## When there is no news

Do not manufacture an event. Four alternatives that earn coverage without one:

1. **Proprietary data.** Aggregate what only this company can see, publish the methodology, and package it as a standalone report. It becomes citable long after the news cycle and gets referenced by later articles.
2. **A defensible position.** A technical argument someone is willing to defend publicly, tied to something happening now. Publish it in the open first so there is a public trail.
3. **Being a source.** Offer expertise on stories already running, with no ask attached. This is how the next pitch gets opened.
4. **The primary artefact.** For developer audiences a repository, a post-mortem or a deep write-up frequently outperforms the coverage it would have earned, and reporters find it on their own.

Recommending one of these instead of a pitch is a successful outcome, not a failure.

## Reactive coverage

Injecting a point of view into a running story works when three things hold at once:

- The expertise is genuine.
- The window is still open - roughly the first day.
- There is data or lived experience behind the take.

Send it as a short note to reporters already covering the story, offering a specific data point and one quotable sentence, and publish the same view on an owned surface so the trail exists.

It does not work on tragedies, on stories outside the sender's expertise, or when the angle reduces to "we sell something for this". Speed matters more than polish here: a good contribution in the first hours beats a better one on day three, which will not be read at all.
