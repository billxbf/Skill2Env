# Channel playbook

## Table of Contents

- [Choosing the anchor](#choosing-the-anchor)
- [Firing order](#firing-order)
- [Per-channel norms](#per-channel-norms)
- [Individual vs company adoption](#individual-vs-company-adoption)
- [Where deeper platform detail lives](#where-deeper-platform-detail-lives)

## Choosing the anchor

One channel carries the launch; the rest point back at it. Choose by where the target adopter already evaluates projects, not by raw reach.

| Project shape                                            | Anchor candidate                                                                                      |
| -------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| Infrastructure, developer tooling, cross-language appeal | General tech aggregator (Hacker News, Lobsters)                                                       |
| UI, design or broad-appeal tooling with a visual demo    | Product Hunt as anchor, aggregator as amplifier - the one case where that inversion is right          |
| Library or framework bound to one ecosystem              | That ecosystem's community: subreddit, forum, mailing list, Discord showcase                          |
| Plugin, integration, extension                           | The host platform's showcase, marketplace or newsletter - but its review clock sets the date, not you |
| Model, dataset or other consumable ML artifact           | The artifact hub itself: the model or dataset page is the anchor, not a post pointing at it           |
| Research-adjacent tooling                                | The field's community forum, plus a paper page cross-linked to the released artifacts                 |
| Company-backed infrastructure aimed at teams             | The engineering blog post, syndicated to an aggregator and to practitioner newsletters                |

## Firing order

This is the clock, not the priority. It is fixed by mechanics - links must resolve before anyone clicks them, and a thread needs its first comment before strangers arrive - so it does not reorder with the project. Which rows run at all is decided by the efficiency ranking in Step 5: the first three never drop, the last four drop under the conditions stated there, and a dropped row simply never fires.

1. **T-0h** - repository public, tag pushed, registry package live. Every link in every draft must already resolve.
2. **T+0** - anchor post, early in the anchor audience's working day, mid-week. Derive the hour from where that audience actually is; a European ecosystem does not follow US aggregator hours.
3. **T+0 immediately** - the maintainer's first comment on the anchor thread (see the runbook).
4. **T+30-90min** - maintainer's own accounts, linking to the _discussion_, not duplicating it.
5. **T+2-6h** - secondary communities, staggered, each with context rewritten for that community. Never paste the same blurb twice; it reads as a bot and gets removed.
6. **Same week** - newsletters and curated lists. Most publish weekly and pick up what ranked earlier in the week, so submit before or on launch day.
7. **T+3-10 days** - long-form write-up (architecture, war story, benchmark method) as the second wave.

## Per-channel norms

### Tech aggregators (Hacker News and similar)

- Show HN is for something people can actually try - a repository, binary or live demo. Blog posts, sign-up pages, newsletters and lists are off-topic for it, and so are minor version bumps. A signup wall weakens a submission badly: readers must be able to try it directly.
- Title format: `Show HN: <Name> – <plain description of what it does>`. No superlatives, no marketing adjectives; moderators rewrite sensational titles anyway.
- Ranking divides points by a power of elapsed time, so the first hours decide everything. Other inputs: user flags, anti-abuse systems, a penalty for overheated threads, per-account and per-site weighting, moderator action. **High karma buys no ranking advantage** - the widely repeated "500+ karma gets more initial trust" claim is wrong. (500 karma is the _downvote_ threshold, which is a different thing.)
- Asking anyone to upvote or comment is against the rules and gets the submission, the account and sometimes the whole domain penalized. Voting rings are detected.
- `[flagged]` means users flagged it; `[dead]` means software, flags or moderators killed it - enough vouches can restore it.
- Reposts are buried as duplicates, except when the story has had no significant attention for roughly a year. Deleting and resubmitting is not a workaround, and "wait 24 hours and repost" is not a recovery window - it is a duplicate.
- **The second-chance pool is the real recovery path.** Moderators re-inject good submissions that got no traction, giving them a fresh random front-page placement, and they explicitly invite the request: mail them about a submission you think is particularly good for the site, and it is fine if it is your own. Once, politely, then let it go.
- **Launch HN is not available to most projects.** It is YC-only and editorially curated: read the guidance, fill a form, staff decide within two weeks, one per startup. Any advice that says "use Launch HN for a major company launch or funding announcement" is wrong - non-YC companies cannot elect into it.
- There is a human in the loop. The site runs with essentially one full-time moderator plus automated spam/duplicate detection, domain weighting and flamewar cool-offs, and applies stricter standards to new accounts. Post from an account with genuine history.
- The window to edit a comment closes after two hours; threads close to new comments after two weeks.
- Posting hours: no first-party guidance exists. Derive the hour from where the anchor audience actually is. Hardcoded US-morning windows circulating in launch guides are invented.

### Product Hunt

A worthwhile **secondary** channel for open source, never the primary one for a developer-first project - its audience skews product and founder rather than deeply technical, so a dev tool gets more useful feedback on an engineering aggregator. Its durable value is SEO: a product page ranks for branded and category terms for years, which matters more to a slow-monetizing project than launch-day spike traffic. Open-source projects do win top badges there, so the channel is real, just secondary.

Separate what the platform documents from what launch consultancies assert:

| Verified (Product Hunt's own docs)                                                                   | Practitioner folklore                                                                      |
| ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| Ranking runs on "points": upvotes plus weighted engagement such as comments and shares               | "First four hours are shown in random order, then ranked"                                  |
| "Not all upvotes carry the same weight" - the system discounts inauthentic engagement                | Specific vote thresholds for Product of the Day (the least reliable number in circulation) |
| Product of the Day/Week/Month go to the highest points over that period; "there's no secret formula" | Aged accounts (>30 days) weighting more than new ones                                      |
| Soliciting upvotes violates the terms                                                                | 12:01 AM PT launch time and Tue–Thu being best                                             |

The 12:01 AM PT and Tue–Thu conventions are worth following anyway - they are consistent across every guide and cost nothing - but present them to the user as convention, not as platform rule.

What matters at launch-planning level: post the maker comment within a few minutes, in the same shape as an aggregator first comment. For a library rather than a SaaS dashboard, the gallery problem is showing a terminal session, a diff or a benchmark - generic product mockups undersell it.

Listing specifics (character limits, image dimensions, topic counts) change with the platform's form and belong to a platform playbook, not here. Check them against the live submission form before writing copy.

### Subreddits and forums

- Rules differ per community and are enforced by humans who check post history. Read the sidebar and the last month of posts before drafting.
- Post where the maintainer already participates. A first-ever post that is a self-link reads as spam whatever its quality.
- Many communities have a weekly showcase or self-promotion thread - that thread is the sanctioned path, and it works.
- Lead with the problem and the technical decision, not the announcement. Link at the end.

### Chat communities (Discord, Slack, Matrix)

- Use the dedicated showcase channel; posting in general channels burns goodwill fast.
- Ask a moderator first in communities where the rules are unclear. A "yes" also often buys a pin.
- Expect no lasting traffic - chat is where early adopters and first contributors come from, not where volume comes from.

### Social platforms

- Demo first: a GIF or short video of real output outperforms any thread opener.
- Structure: problem → what you tried → what you built → link. One thread, not a drip campaign.
- Tag maintainers of adjacent projects only when the project genuinely builds on or complements theirs, and say how.
- Personal accounts outperform brand accounts for OSS launches; if a company account posts, have the maintainer post too and let the company amplify.

### Artifact and connector hubs

Two hub shapes behave nothing alike at launch. A **presence hub** (a model, dataset or demo directory) can be the anchor itself. A **connector hub** (a marketplace or integration directory) cannot be in a launch plan at all unless it was submitted months earlier - see the clock below.

**When the artifact page is the anchor.** The page carries the launch; every other channel points at it rather than restating it.

- Ship the card complete at T-0. Metadata is what search, filters and the code-snippet tab read - task, library, license, training datasets, base model. A card published bare and fixed a week later has already missed the window.
- Split variants into one repository each and group them in a collection. Each repository then has its own URL, its own search presence and its own download count; a directory listing inside a single repository has none of those.
- Link a runnable demo from the card, and have the demo pull weights from the hub repository rather than external storage - that is what cross-links the artifacts to each other.
- Link the paper. A recognised paper URL in the card is extracted into a tag that cross-links the paper page and filters to every other artifact citing it.
- Treat the hub's community or discussion tab exactly as the aggregator first comment: staffed for the first hours, answering the questions the card failed to answer.

**Ranking runs on recent attention, not on cumulative downloads.** Hugging Face's own release checklist states it plainly: "The more visits and likes your model receives, the higher it appears on the Hugging Face Trending section, bringing even more visibility." No formula is published - `trendingScore` is exposed as an API sort key and nothing else - so treat the mechanism as opaque and drive traffic to the artifact page during the window rather than reverse-engineering a score.

**Likes and downloads are inverse signals, and swapping them is the field's standard error.** Hugging Face's own analysis of the Hub is explicit: "A like says a release matters, and goes to frontier models in the weeks after they ship", while "A download says something is wired into a pipeline that runs on a schedule, and accrues to small, stable models over years" - and "Treating either as a proxy for the other is the most common mistake we see in coverage of the Hub."

Over the period they measured, exactly one repository appeared in both the top 25 by downloads and the top 25 by likes. A launch moves likes; it does not move downloads, and reporting the absence of downloads as failure is a misreading of the surface.

**The connector-hub clock sets the date, not your readiness.** Review windows on the major directories run from days to a full quarter - one workspace marketplace quotes up to 10 business days for a preliminary pass and up to 10 weeks for the functional one, and one automation directory holds new integrations in a 90-day beta before public status.

Some also gate on traction you must already have, which makes them structurally unavailable to a first launch. Submit early and treat the listing as a later wave, or launch without it and announce it when it lands.

### Newsletters and curated lists

- Submit before launch day: weekly issues are assembled days in advance.
- Give the curator a ready-to-paste 2-3 sentence description and a link to a page that explains the project without a login.
- Listing sites and awesome-lists are long-tail distribution, not a launch spike - handle them after the window, once the project has independent usage to show a curator, and let the ongoing distribution work own them.

## Individual vs company adoption

|                      | Individual adoption                        | Company adoption                                                                           |
| -------------------- | ------------------------------------------ | ------------------------------------------------------------------------------------------ |
| Who reads            | The developer who will use it              | The evaluator, who must convince an approver                                               |
| Decides on           | Time-to-first-success, ergonomics, demo    | License compatibility, maintenance, security, support path                                 |
| Assets needed        | Quickstart, demo, zero-config defaults     | Comparison page, security policy, release cadence, roadmap, maintainer/funding model       |
| Channels             | Aggregators, social, ecosystem communities | Engineering blog, practitioner newsletters, ecosystem communities, conference talks        |
| Early signal         | Stars, shares, playground sessions         | Clones from corporate networks, private forks, carefully written issues, license questions |
| Timeline to adoption | Days                                       | Weeks to quarters                                                                          |

A launch aimed at teams that lands only on individual-developer channels produces applause and no deployments. The reverse produces approval questions nobody is staffed to answer.

## Where deeper platform detail lives

This page covers what a launch turns on: choosing the anchor, the firing order, and the mechanics that decide whether a post survives its first hours. Per-platform culture, unwritten codes, algorithm behaviour and listing process have a different shelf life and live in the sibling collection named at the end of the skill - recommend it when the user's question is really about one platform rather than about their launch.
