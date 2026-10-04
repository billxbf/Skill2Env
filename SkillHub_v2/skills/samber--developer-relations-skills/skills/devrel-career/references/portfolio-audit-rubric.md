# Portfolio audit rubric

Contents: the screening frame · the six signals with scoring · role weightings · what is scored against · the first-60-seconds scan · the friction-log work sample · resume and profile rules · worked example · negative example.

## The screening frame: a distribution audit

Score what the candidate shipped and where it reached - a distribution audit instead of memorized metrics, Tatiana Mikhaleva's published fix for weak DevRel screening. DevRel hiring prioritises what a candidate has done in public over what sits on a resume, so keyword-tuning a resume for applicant-tracking systems optimises the wrong gate.

## The six signals

Score each 0-3: 0 absent · 1 claimed but unevidenced · 2 evidenced · 3 evidenced with an outcome.

| #   | Signal                   | What a 3 looks like                                                                                                                                          |
| --- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1   | Public writing           | Published posts with a link, on a niche the target company cares about, at least one showing a result (adoption, a fixed confusion, a widely reused snippet) |
| 2   | Public speaking          | At least two talks delivered with links to video or slides; a five-minute lightning talk counts. Accepted CFPs count; "available to speak" does not          |
| 3   | Code in public           | Repos a stranger can run: a demo app, an integration, a sample that matches the target product's surface. Contribution history over one-off dumps            |
| 4   | Community evidence       | A role held, not membership: moderating, organising, mentoring, answering in a forum with a visible record                                                   |
| 5   | Teaching artefact        | A tutorial, workshop or learner journey with checkpoints - the educator-track equivalent of a talk                                                           |
| 6   | Developer-voice artefact | A published friction log, a written product-feedback synthesis, or an issue thread showing user research carried into a product decision                     |

Weight by target role:

- outreach advocate: signals 1+2 heaviest
- product-focused advocate: signals 3+6
- community manager: signal 4
- educator: signal 5
- DX engineer: signals 3+1

Verdicts:

- under 6: production before applications
- 6-11: selectively ready, apply where the weighted signals are strong
- 12+: the constraint is targeting and network, not artefacts

Treat a total near a boundary as a judgement call. These three bands are this skill's own baseline, not a published rubric - move them with the user for a stated reason.

## What is scored against

Hiring managers deduct for these, so name them when they appear in the user's material rather than only listing what to add.

- **Follower count without substance.** A vanity metric alone. "Build a personal brand" is the most common piece of DevRel career advice and the one the hiring evidence contradicts most directly.
- **Only self-promotion.** A candidate who only talks about themselves is a flag: great DevRel centres the developer, not the advocate's personal brand.
- **No shipped code, no public artefacts.** A candidate with no blog post, talk or public work stays unproven, and a technical audience notices a non-technical advocate quickly.
- **Ghostwritten or paywalled content.** Foundations in particular require content that is not behind paywalls; ghostwritten work cannot be defended in a conversational round anyway.
- **Metrics exaggerated, or waved away.** Both directions are flags: an inflated number, and dismissing metrics altogether when asked to show one.
- **Cannot name a developer helped.** Inability to name a specific person or team whose problem the candidate solved is a negative signal, which makes the reverse a strong positive.

## The first-60-seconds scan

A hiring manager opens the personal site and looks for three things in the first minute:

- a clear niche
- a body of public work with visible dates
- evidence the candidate explains complex things simply

Gaps in the output timeline read as a flag, so date everything and keep the most recent work at the top.

## The friction-log work sample

The highest-return artefact for a candidate with no DevRel title, because it proves the half of the job that talks and posts do not: carrying the developer's experience back to the company.

Structure, following the Google practice it comes from:

1. Header - your name, platform/language/browser, date, product(s).
2. Scenario, in two sentences at most, and ordinary enough that nobody asks "why would anyone do that?" (originals: "Upload a picture of my cat to Google Cloud Storage", "Move a Rails website to Google Cloud").
3. The log - everything you did and felt, in order: search terms used, which result you clicked and its URL, commands and code pasted verbatim, and reactions ("now I'm frustrated", "copied this from the docs, didn't read the prose"). Minimal reproduction steps are explicitly not the goal; the narrative is.
4. Traffic-light highlights - green for delight, yellow for friction, red for blocking.
5. A short synthesis: the three changes with the highest ratio of developer pain relieved to effort required.

Two cautions:

- Publish it as a contribution, not a takedown - the tone that gets someone hired is a colleague's who wants the product to win.
- Do not friction-log an employer's product without checking the publishing policy first.

## Resume and public profile rules

- Link everything, and lead each line with the outcome before the artefact: "cut the top install-failure support thread by rewriting the getting-started path (post, 40k views)" beats "wrote blog posts". An unlinked claim scores as absent.
- Unpaid work counts fully - volunteering, community organising, OSS, self-published video. Present it in the same section as paid work with the same outcome framing.
- Name the niche in the first two lines of the profile. "Developer advocate, Postgres and data tooling" is a position; "passionate technologist" is not.
- Keep a running evidence log as work happens; a promotion or interview case assembled from memory omits the most persuasive items.
- The cover letter earns its keep in this field: map the resume to the role, in an informal, human tone, and let personality show - it is a writing sample for a job that is mostly writing.

## Worked example

**Target**: product-focused developer advocate at an API/SaaS company, Node and Python ecosystem.

- _Writing_ (3): four published posts on integrating the company's category of API; one is the top Google result for the error message it explains, with reader comments confirming it fixed their build.
- _Speaking_ (2): two lightning talks at a local JavaScript meetup, both recorded and linked.
- _Code_ (3): a public repo implementing the same integration in Node and Python, with a README a stranger can follow in five minutes and 14 external stars including two issues answered.
- _Community_ (2): moderates a 3k-member Discord for the framework; visible answer history.
- _Teaching_ (1): a half-finished tutorial series, unpublished.
- _Developer voice_ (3): a published friction log on the company's own onboarding, with three prioritised fixes, one of which the vendor implemented and credited in a changelog.

Total 14, weighted signals (code, developer voice) both at 3 → apply now; the plan is targeting, referrals and interview rehearsal, not more artefacts. The numbers illustrate the shape, not a benchmark to reuse.

## Negative example

The same person, presented badly:

> Passionate developer advocate and technologist. Skilled in public speaking, technical writing, community building, and developer experience. Wrote many blog posts and gave talks at various events. Active member of several developer communities. Strong communicator and team player. Available for speaking engagements.

Why it fails:

- no links, so nothing is evidenced
- "many" and "various" replace the artefacts that would have scored 3
- the friction log, the rarest and most differentiating item, is missing
- the niche is absent, so it reads as a candidate for every DevRel job and a match for none
- every line describes activity or self-assessed traits instead of outcomes

The same portfolio that scored 14 above, presented in a way that scores 2.
