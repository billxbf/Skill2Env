# Selection rubric, intake form and lifecycle messages

Contents: the two-stage gate · scoring rubric · reviewer rules · intake form fields · acceptance, rejection, renewal, non-renewal and removal messages.

## Table of Contents

- [Two-stage gate, not a single score](#two-stage-gate-not-a-single-score)
- [Scoring rubric (stage 2 only)](#scoring-rubric-stage-2-only)
- [Intake form fields](#intake-form-fields)
- [Lifecycle messages](#lifecycle-messages)

## Two-stage gate, not a single score

Stage 1 is a **gate**: does the candidate meet two or more of the published criteria, over the last 12 months, with evidence a reviewer can open? A candidate who fails the gate is not scored - scoring them invites reviewers to argue a favourite past the published rules.

Stage 2 is a **rank**, used only when qualified candidates outnumber the slots. Publish the gate; keep the rank internal. A published score turns every cycle into a leaderboard dispute, while an unpublished gate makes every rejection indefensible.

## Scoring rubric (stage 2 only)

Score each candidate 0-5 per line, multiply by the weight, and sum. **Every weight below is self-set.**

Programs keep their internal scoring private, so these weights encode this skill's argument - support and mentoring above reach - rather than an observed distribution. Recalibrate them to the program's stated purpose, and write the change into the charter rather than applying it silently.

The only comparable published rubric comes from `jonathimer/devmarketing-skills@power-user-cultivation`:

- Content created: +25.
- Top-decile usage: +20.
- Answering others' questions: +20.
- Community activity: +15.
- Social mentions: +10.
- Accepted feature requests: +10.

It ranks content creation highest and has no mentoring, tenure or coverage-gap line at all. Worth knowing when a user arrives quoting it: the disagreement is about whether a champions program is buying reach or buying depth.

| Signal                                                      | Weight | 0                                          | 5                                                              |
| ----------------------------------------------------------- | ------ | ------------------------------------------ | -------------------------------------------------------------- |
| Answers others' questions (community, forum, issue tracker) | ×5     | never                                      | a recognised, reliable answerer in a topic area                |
| Sustained tenure of visible activity                        | ×4     | under 6 months, or a spike at announcement | 2+ years, no gaps                                              |
| Mentoring and newcomer treatment                            | ×4     | absent or dismissive                       | escorts first-time contributors through to a merged PR         |
| Teaching in public (talks, workshops, streams)              | ×3     | none                                       | recurring, to audiences outside the company's reach            |
| Non-paywalled content about the technology                  | ×3     | none, or all gated behind their own funnel | regular, and in a language or region the vendor does not cover |
| Direct contribution to the project or ecosystem             | ×3     | none                                       | sustained, above the published floor                           |
| Coverage gap closed (region, language, vertical, ecosystem) | ×3     | duplicates existing coverage               | only credible candidate in a market with no presence           |
| Product depth in production use                             | ×2     | evaluated it once                          | runs it at scale and reasons about its trade-offs              |
| Reach (followers, audience size)                            | ×1     | small                                      | large                                                          |

Why reach is weighted last: reach can be granted by the platform perks; the willingness to answer a stranger's question at 23:00 cannot. A roster selected on reach fills with names that never show up. When the audit at the end of a cycle shows the accepted cohort was mostly the highest-reach applicants, the rubric was not actually applied.

**Reviewer rules.**

- Use at least two reviewers per candidate, scoring independently before comparing.
- Require a written one-line justification per score above 3.
- Recuse any reviewer who nominated the candidate.
- Record the final score and the decision - a candidate who reapplies deserves a comparison against their own last cycle, not a fresh opinion.

**Anti-signal overrides.** These end the review regardless of score:

- Hostility or condescension toward beginners.
- Activity beginning the week applications open.
- An unresolved code-of-conduct case.
- A request for the title as compensation.

Competitor employment and consultancy conflicts do not auto-disqualify but trigger the written conflict-of-interest rule from the charter.

## Intake form fields

Keep it short enough to complete in 20 minutes. Every extra field costs you the candidates who are busy contributing.

**Identity and eligibility**

- Name, preferred public name, primary community handle, country and time zone, primary languages.
- Confirm 18+ (or the program's stated minimum).
- Employer, and whether that employer competes with the product.
- Does your employer require approval for you to hold this title? Approved / not required / pending.
- Are you subject to gift-value limits (public sector, healthcare, finance)?

**Evidence, one block per criterion claimed**

- Which criteria do you meet? (checkboxes, minimum two)
- For each: 2-3 links, plus one line on what it was and roughly when.
- What have you done in the last 12 months that a reviewer would not find by searching?

**Fit and intent**

- What do you want out of this, in your own words?
- Which perk would matter most to you? (ranked list - the answers are also the program's perk research)
- Where do you want to be more active next year?
- What would make you step back? (surfaces capacity limits before they turn into an inactive roster entry)

**Consent**

- Acknowledge the code of conduct and the obligations, including the may-not list.
- Acknowledge the disclosure expectation for public posts.
- Acknowledge the NDA scope, if pre-release access is a perk.
- Consent to the public roster listing (name, photo, links) and to its retention as an alumni record after the term.

**Nomination variant.** For nomination-only programs, the nominator supplies the evidence block and the nominee confirms eligibility, consent and capacity. Cap nominations per nominator - GitHub Stars uses three - so the roster does not mirror one enthusiastic person's network.

## Lifecycle messages

Adapt the wording; keep the structure. Every one of these is sent by a named human, never from a no-reply address.

**Acceptance**

> You're in the 2026 cohort - congratulations, and thank you for the year of answers in the forum that got you here.
>
> Term: 1 March 2026 to 28 February 2027. What happens next: a 30-minute onboarding call this month, then the six-weekly cohort call and the quarterly roadmap briefing. Your private channel invite is attached.
>
> Two things to read before the first call: the obligations and may-not list (three minutes), and the disclosure wording to use when you post about pre-release features. Both are in the charter.
>
> One ask for the first month: tell us the single thing about the product that most frustrates you. That answer is worth more to us than anything you will post publicly.

**Rejection**

> Thank you for applying, and for the workshops you ran this year - the review team knew your name before the application arrived.
>
> We're not able to include you in this cohort. You met the content-creation criterion clearly, but we need a second criterion and the community-leadership and support signals weren't there yet in the last 12 months.
>
> The most direct path: answering questions in the forum is the criterion we weight highest, and consistency over a year matters more than volume in a month. If that's where you spend the next year, you'd be a strong candidate in the January 2027 window.
>
> This changes nothing about your standing here. Reply if you'd like to talk it through.

Do not send: a template with no named gap, a "we had many strong applicants" line and nothing else, or silence. A rejected candidate is still an active community member, and how the rejection reads decides whether they stay one.

**Renewal invitation** (sent 90 days before the term ends, activity record attached)

> Your term ends on 28 February. We'd like you to continue, and here's the record we're judging: 41 forum answers, two workshops, the Portuguese translation of the getting-started guide, and the six issues that changed the retry defaults.
>
> Say yes by 31 January and nothing changes. Say pause and you keep the title on the roster with no expectations for six months - parental leave, a job change and burnout all count, and we don't need details. Say no and you move to alumni, keep the dated title, and we'll ask you to help review the next cohort.

**Non-renewal** (never a surprise; the notice above is what makes it not one)

> Your term ends on 28 February and we're not renewing it. The renewal test is the same published criteria over the last term, and there's been no visible activity or contact since June.
>
> You move to alumni: the title stays as "Champion, 2025-2026", the roster page keeps your entry with those dates, and you stay on the quarterly digest. If the reason was capacity and next year is different, the January window is open to you and the record from 2025 counts.

**Removal for conduct** (decided by the moderation process, not the program owner alone)

> Following the moderation team's review of the incident on 14 May, your champion status ends today and the roster entry has been removed. The decision and the appeal path are in the message from the moderation team.
>
> We will not publish a reason. If people ask us, we'll say the status ended and nothing more.

Removals are announced as facts without narrative, and never as a public rebuke - the goal is that the conduct standard is visibly enforced, not that the person is made an example of.
