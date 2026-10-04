# Skill routing reference

Read this before routing any task that could plausibly match two skills. Every disambiguation below comes from the siblings' own declared scopes, not from inference.

## Table of Contents

- [Boundary forks](#boundary-forks)
- [Do-not-route signals](#do-not-route-signals)
- [Host auto-selection](#host-auto-selection)
- [Ordered chains](#ordered-chains)
- [Coverage gaps](#coverage-gaps)
- [Sibling-collection recommendations](#sibling-collection-recommendations)

## Boundary forks

### Docs authoring - four skills, four jobs

Ask what the reader is trying to do, not what the page will be called.

| Reader's state                                             | Route to                                                           | Never route to                                                     |
| ---------------------------------------------------------- | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| Has never run the thing; needs one verified success fast   | `samber/developer-relations-skills@developer-quickstart-guide`     | `samber/developer-relations-skills@developer-tutorial`             |
| Wants to learn a concept by building something             | `samber/developer-relations-skills@developer-tutorial`             | `samber/developer-relations-skills@developer-quickstart-guide`     |
| Already competent; needs one specific task done            | no skill - see Coverage gaps                                       | either of the above                                                |
| Landed on the repository and is deciding whether to bother | `samber/developer-relations-skills@readme-optimization`            | `samber/developer-relations-skills@developer-quickstart-guide`     |
| Pasted an error string into a search box                   | `samber/developer-relations-skills@developer-troubleshooting-docs` | `samber/developer-relations-skills@developer-docs-structure-audit` |
| A coding agent, not a human, reading unattended            | `samber/developer-relations-skills@coding-agent-docs-optimization` | `samber/developer-relations-skills@developer-docs-structure-audit` |

Conflating a tutorial with a how-to guide fails both readers: the learner gets an unexplained recipe, the working developer gets a lecture. When the task is a how-to guide, say the collection has no skill for it rather than routing to the nearest neighbour.

`samber/developer-relations-skills@developer-docs-structure-audit` operates on the whole docs set, never on one page. When the user asks "where should this page live", that is a structure question. When they ask "how do I write this page", route by reader state above.

`samber/developer-relations-skills@docs-code-sample-standards` owns the policy every sample obeys and the audit of an existing corpus. A single snippet inside one page being written belongs to whichever authoring skill owns that page.

### Release communication - changelog vs migration guide

- `samber/developer-relations-skills@changelog-writing` - one release, everything that shipped, one line of action per breaking entry.
- `samber/developer-relations-skills@version-migration-guide` - one breaking change set, blast-radius ordering, before/after code, deprecation timeline, verified by upgrading a real project.

A major version usually needs both, in that order. A patch release needs only the first. Neither owns the versioning policy itself - that is a gap (see below).

### Measurement - three skills, three layers

- `samber/developer-relations-skills@devrel-metrics` - which numbers deserve a target, the attribution rule, and what gets cut. The framework layer.
- `samber/developer-relations-skills@devrel-analytics` - how those numbers get collected: event taxonomy, identity spine, link tagging, surface register. The instrumentation layer.
- `samber/developer-relations-skills@developer-community-health` - the community venue only: activity, responsiveness, contributor funnel, sentiment.

- "Our numbers disagree between tools" routes to `samber/developer-relations-skills@devrel-analytics`.
- "Leadership isn't convinced" routes to `samber/developer-relations-skills@devrel-metrics`.
- "Is our Discord dying" routes to `samber/developer-relations-skills@developer-community-health`.
- "How do we compare to a competitor" routes to `samber/developer-relations-skills@devrel-competitor-analysis` - it looks outward; the other three look inward.

### Open source visibility - launch, distribution, transparency

- `samber/developer-relations-skills@oss-launch` - the launch window itself: readiness gate, positioning, channel sequencing, run of show, trending mechanics.
- `samber/developer-relations-skills@oss-distribution-strategy` - everything after that window: registry presence, curated lists, downstream packaging, release cadence as a visibility beat.
- `samber/developer-relations-skills@build-in-public` - the ongoing personal or company transparency practice, independent of any launch.

"Adoption flattened after launch" is distribution, not a second launch. "What should I post every week" is build-in-public. `samber/developer-relations-skills@tech-press-relations` handles journalists and embargoes for any of the three; it never owns the announcement post itself.

### Sponsorship - who is paying whom

- `samber/developer-relations-skills@oss-sponsors-fundraising` - the maintainer wants money in.
- `samber/developer-relations-skills@oss-sponsors-brand-strategy` - the company decides which projects to fund.
- `samber/developer-relations-skills@developer-event-sponsorship` - the company buys conference, meetup or hackathon sponsorship.

Read the question's subject. "Which tier should we pick on this maintainer's page" is the company side, not the maintainer side.

### Community - four skills on one timeline

1. `samber/developer-relations-skills@developer-community-launch` - before anything exists: should it exist, where, seeded how, and when to fold it back.
2. `samber/developer-relations-skills@developer-community-moderation` - the rules and the enforcement machinery, written before the first incident.
3. `samber/developer-relations-skills@developer-community-health` - measurement, once there is enough activity to have a baseline.
4. `samber/developer-relations-skills@developer-champions` - recognition and obligations for the top members, once a reliable top exists.

A community that has not run 90 days has no health baseline; route measurement asks there to "not now" with that unblocking condition. `samber/developer-relations-skills@oss-contributor-onboarding` is the code-contribution equivalent of a community funnel and belongs to the open-source block, not here.

### Strategy - five skills that all sound like "what should we do"

- `samber/developer-relations-skills@devrel-strategy` - the DevRel program's own charter: driver, goals, pillars, staffing sequence, refused list.
- `samber/developer-relations-skills@devrel-team-structure` - where DevRel reports and how the team is shaped. Org design only.
- `samber/developer-relations-skills@devrel-budget-allocation` - the money split across pillars, with thresholds and a cut list.
- `samber/developer-relations-skills@developer-first-gtm` - how developer adoption becomes revenue. A company-level motion, not a DevRel charter.
- `samber/developer-relations-skills@devtools-business-model` - what is sold and how it makes money at all.

Chain them rather than choosing between them when the user is genuinely at zero: model → GTM → strategy → team → budget.

Three related, narrower skills: `samber/developer-relations-skills@devtools-pricing-strategy` sets the value metric and price points inside the business model; `samber/developer-relations-skills@open-source-company-strategy` decides which assets stay open; `samber/developer-relations-skills@oss-license-strategy` picks the license text for one project.

### Speaking and media - sequence, not competition

`samber/developer-relations-skills@conference-cfp-submission` (get accepted) → `samber/developer-relations-skills@tech-talk-outline` (structure the talk) → `samber/developer-relations-skills@developer-live-demo-design` (make the demo survive). None of them writes slides or coaches delivery.

- `samber/developer-relations-skills@tech-podcast-interview-prep` is for being someone else's guest.
- `samber/developer-relations-skills@technical-video-script` is for your own recorded video.
- `samber/developer-relations-skills@engineering-blog-post` is the written form.
- `samber/developer-relations-skills@developer-case-study` is the customer's story rather than yours.
- `samber/developer-relations-skills@devrel-content-calendar` plans the quarter these pieces land in and never writes them.

### Events - speak, sponsor, or run it yourself

- `samber/developer-relations-skills@conference-cfp-submission`, `samber/developer-relations-skills@tech-talk-outline`, `samber/developer-relations-skills@developer-live-demo-design` - you are on someone else's stage.
- `samber/developer-relations-skills@developer-event-sponsorship` - you are paying to appear at someone else's event.
- `samber/developer-relations-skills@developer-meetup-program` - you run a small recurring local group yourself: format, cadence, speaker pipeline, venue sponsor, health.

Ask who owns the event before routing. A conference or hackathon you organize is not `samber/developer-relations-skills@developer-meetup-program` - that is organizer work and belongs to `samber/dev-event-organizer-skills` (see below).

### Employer brand - the strategy, the surfaces, the other side of the table

- `samber/developer-relations-skills@tech-employer-branding` - why engineers should want to work here, and which channels carry that claim: the EVP, the verification-surface audit, the ranked channel bets, the hiring measurement baseline. Strategy altitude; it produces no artefact.
- `samber/developer-relations-skills@engineering-blog-post` - one post the plan commissions.
- `samber/developer-relations-skills@github-profile-optimization` - the code-host profile the plan audits as one verification surface.
- `samber/developer-relations-skills@devrel-career` - the candidate reading those same surfaces from the other side of the table.

Ask who is hiring whom.

- "How do we attract senior engineers" is the strategy skill.
- "Write the post" and "fix the profile" are the execution skills - and a plan that skips straight to them has no EVP behind it.
- Hiring for DevRel roles specifically - role definitions, job postings, interview loops, scorecards - is none of the four; route to `samber/developer-relations-skills@devrel-hiring`.

### Profile surfaces

`samber/developer-relations-skills@readme-optimization` owns one repository's README. `samber/developer-relations-skills@github-profile-optimization` owns the personal or organization profile page and which repositories get pinned. When both are in play, fix the pinned repositories' READMEs first - the profile sends traffic into them.

## Do-not-route signals

- Debugging a live production incident → not `samber/developer-relations-skills@developer-troubleshooting-docs`; that skill writes the page afterwards.
- Reviewing the product's own source code or error strings → outside the collection.
- Triaging one specific issue → not `samber/developer-relations-skills@oss-issue-triage`; that skill designs the system.
- Legal sign-off on a license, CLA, trademark or contract → every relevant skill is a decision framework and says so.
- Recruiting or interviewing DevRel staff → route to `samber/developer-relations-skills@devrel-hiring`, not `samber/developer-relations-skills@devrel-career` (candidate side only) or `samber/developer-relations-skills@tech-employer-branding` (engineering employer brand, not a role's interview loop).
- Writing courses or lesson content → `samber/developer-relations-skills@developer-education-strategy` stops at the operating model.
- Building the slides, editing the video, running the camera → outside the collection.
- Product-user onboarding (in-app) → not `samber/developer-relations-skills@oss-contributor-onboarding`, which is about code contribution.

## Host auto-selection

Some harnesses select a skill by matching the request against every installed skill's `description`, before this kickoff runs - triggering a sibling directly, or the kickoff and a sibling together.

- A sibling triggered directly, without the kickoff, is not a bypass to correct: each sibling's `description` triggers standalone, and the kickoff exists for ambiguous or multi-skill requests only.
- When both fire on the same request, treat the kickoff's decision as confirming what the harness already started, never a second dispatch that re-runs or contradicts a sibling in progress.

Pattern from `penpot/penpot-ai-kit@penpot-router`: a router degrading to a confirmation role once a host has already auto-selected by description.

## Ordered chains

Offer a chain only when the task genuinely decomposes. Every chain below is in dependency order, not efficiency order: a later link consumes what the earlier one produces and cannot run before it, so ranking a chain adds nothing. Common ones:

- **First DevRel hire, nothing exists:** `samber/developer-relations-skills@developer-segmentation` → `samber/developer-relations-skills@devrel-strategy` → `samber/developer-relations-skills@devrel-metrics` → `samber/developer-relations-skills@devrel-content-calendar`.
- **Open-sourcing a project:** `samber/developer-relations-skills@oss-license-strategy` → `samber/developer-relations-skills@readme-optimization` → `samber/developer-relations-skills@oss-contributor-onboarding` → `samber/developer-relations-skills@oss-launch` → `samber/developer-relations-skills@oss-distribution-strategy`.
- **Docs overhaul:** `samber/developer-relations-skills@developer-docs-structure-audit` → `samber/developer-relations-skills@developer-quickstart-guide` → `samber/developer-relations-skills@docs-code-sample-standards` → `samber/developer-relations-skills@docs-seo`.
- **Major version release:** `samber/developer-relations-skills@version-migration-guide` → `samber/developer-relations-skills@changelog-writing` → `samber/developer-relations-skills@engineering-blog-post`.
- **Conference season:** `samber/developer-relations-skills@conference-cfp-submission` → `samber/developer-relations-skills@tech-talk-outline` → `samber/developer-relations-skills@developer-live-demo-design`.
- **Community from zero:** `samber/developer-relations-skills@developer-community-launch` → `samber/developer-relations-skills@developer-community-moderation` → `samber/developer-relations-skills@developer-community-health` → `samber/developer-relations-skills@developer-champions`.
- **Proving the program:** `samber/developer-relations-skills@devrel-metrics` → `samber/developer-relations-skills@devrel-analytics` → `samber/developer-relations-skills@devrel-budget-allocation`.
- **Maintainer sustainability money:** `samber/developer-relations-skills@oss-sponsors-fundraising` → `samber/developer-relations-skills@build-in-public`.

Each link hands the next one a named artifact. If you cannot say what gets handed over, there is no chain - route to one skill instead.

## Coverage gaps

State these plainly as gaps. Do not route to a neighbour.

- Task-oriented how-to guides, and API reference completeness.
- The versioning and deprecation policy itself (as opposed to documenting one migration).
- The exec-facing DevRel report narrative and budget defense.
- Monetizing one open-source project, and maintainer burnout as a subject of its own. Succession and bus-factor planning are _not_ a gap - `samber/developer-relations-skills@oss-governance` owns them (contributor absence factor, trust ladder, inactivity rule, emeritus).
- A trademark _usage and enforcement_ policy aimed at third parties. Who holds the mark, the domains and the registry accounts belongs to `samber/developer-relations-skills@oss-governance`; clearing a name before launch belongs to `samber/developer-relations-skills@oss-launch`.
- Organizing your own conference or hackathon, conference booth operations, post-event follow-up.
- A developer newsletter, an office-hours program, student and campus programs.
- Choosing a docs platform, and monitoring brand mentions across developer channels.
- Producing any final asset: slides, video files, rendered graphics, published pages.
- Legal advice of any kind.

## Sibling-collection recommendations

Same owner, separate collections. Recommend installing one; never depend on it.

| Signal in the task                                                                            | Belongs to                          |
| --------------------------------------------------------------------------------------------- | ----------------------------------- |
| Public API surface design, versioning policy, error shape, rate limits, idempotency           | `samber/developer-platform-skills`  |
| Webhooks, sandbox and test mode, integration observability, API status communication          | `samber/developer-platform-skills`  |
| SDK portfolio decisions, developer portal design, OAuth for third-party apps                  | `samber/developer-platform-skills`  |
| Building your own connector marketplace, app review, listing standards, marketplace economics | `samber/developer-platform-skills`  |
| Organizing your own conference, meetup logistics at production scale, hackathon operations    | `samber/dev-event-organizer-skills` |
| Selling sponsorship as the organizer, prospectus, pricing, fulfillment                        | `samber/dev-event-organizer-skills` |
| Running a CFP as the organizer, talk selection, speaker sourcing and hospitality              | `samber/dev-event-organizer-skills` |
| Venue, ticketing, schedule design, run of show, attendee experience                           | `samber/dev-event-organizer-skills` |

The line for events runs through who is paying: this collection covers the speaker and the sponsor; the event collection covers the organizer. The line for platforms runs through who builds the surface: this collection covers documenting and evangelizing it; the platform collection covers designing it.

Say it as a recommendation: "This is organizer-side work - `samber/dev-event-organizer-skills` covers it; this collection stops at the sponsor and speaker side." Then stop. Do not improvise the sibling's advice.
