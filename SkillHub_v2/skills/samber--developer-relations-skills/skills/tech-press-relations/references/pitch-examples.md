# Pitch Examples

Contents: subject lines · four worked pitches with their weak twins · the embargo email · the source reply · what makes the difference.

Every example below is illustrative and uses invented companies and numbers. Replace them with facts you can source; never ship a placeholder figure.

## Table of Contents

- [Subject lines](#subject-lines)
- [Pitch 1 - data story](#pitch-1-data-story)
- [Pitch 2 - major version with breaking changes](#pitch-2-major-version-with-breaking-changes)
- [Pitch 3 - funding](#pitch-3-funding)
- [Pitch 4 - licence change, hostile territory](#pitch-4-licence-change-hostile-territory)
- [The embargo email](#the-embargo-email)
- [The source reply, when a reporter asks you for a quote](#the-source-reply-when-a-reporter-asks-you-for-a-quote)
- [What separates the good from the weak](#what-separates-the-good-from-the-weak)

## Subject lines

| Weak                              | Stronger                                                           | Why                                        |
| --------------------------------- | ------------------------------------------------------------------ | ------------------------------------------ |
| Introducing Fernbank 2.0          | Fernbank 2.0 drops Postgres support - here's the migration cost    | Names the consequence a reader must act on |
| New data on developer workflows   | 41% of deploys we measured happen after 4pm Friday                 | The number is the story                    |
| Story idea for you!               | Re: your piece on build-cache pricing - we have the meter data     | Anchors to their own work                  |
| Exciting partnership announcement | Embargo Sep 4, 09:00 CET: Fernbank donates its runtime to the CNCF | States what and when in one line           |
| Following up on my last email     | The customer from my last email can talk Thursday                  | Follow-up carries new information          |

## Pitch 1 - data story

**Good.**

> Subject: 41% of production deploys we measured happen after 4pm Friday
>
> Hi Dana,
>
> Your piece on deployment freezes last month argued the Friday taboo is folklore. We have data either way.
>
> We analysed 2.3 million deploys across 4,100 organisations on our platform between January and June. 41% of production deploys land after 16:00 local on Friday, and their rollback rate is 1.4x the weekday average - but the gap disappears entirely for teams with automated rollback.
>
> Methodology and the anonymised dataset are here: <link>. Our infrastructure lead who ran the analysis can talk this week, and two customers in the sample have agreed to be named.
>
> Useful for a follow-up?
>
> - Sam, platform engineering, Fernbank

**Weak twin.** "Fernbank, the leading deployment intelligence platform, today announced groundbreaking new research revealing surprising insights into developer deployment behaviour. Our data shows that developers deploy at all hours! Let me know if you'd like the full report." - no number, no methodology, no relevance to anything she wrote, and the adjectives do the work the evidence should.

## Pitch 2 - major version with breaking changes

**Good.**

> Subject: Embargo Sep 9, 14:00 UTC: Fernbank 3.0 breaks its plugin API - why we did it
>
> Hi Marcus,
>
> You covered the plugin-compatibility mess in this ecosystem in March, so you may want this one early.
>
> Fernbank 3.0 breaks the plugin API. The old interface made every plugin a synchronous blocker in the request path; the new one is async and cuts p99 from 780ms to 120ms on our own workload. It also means all 340 community plugins need changes, and we're shipping a codemod that handles roughly 70% of them.
>
> Embargo to Sep 9, 14:00 UTC. Briefing pack, benchmark harness and the migration guide: <link>. Our maintainer can walk through the decision and the fallout on Thursday or Friday.
>
> - Sam

**Weak twin.** A version that leads with "Fernbank 3.0 is our most powerful release ever" and buries the break in paragraph four. Technical reporters write the break either way; hiding it just means the sender is not the source for it.

## Pitch 3 - funding

**Good.**

> Subject: Exclusive: Fernbank raised $14M to make build caching a shared utility
>
> Hi Priya,
>
> Offering you this one exclusively - you've tracked the build-infrastructure consolidation longer than anyone.
>
> Fernbank raised $14M led by <investor>, announcing Oct 2. The interesting part isn't the round: we're using it to run the cache as a shared multi-tenant utility, which every competitor has said is impossible for confidentiality reasons. We think the confidentiality argument is wrong and we're publishing the isolation model alongside the announcement.
>
> Can give you the founder, the lead investor, and two design partners under embargo. Need an answer by Friday so I can plan the rest.
>
> - Sam

**Weak twin.** "We're thrilled to announce our Series A! We'd love to get your thoughts." The round alone is a form, not a story, and "thoughts" is not an ask.

## Pitch 4 - licence change, hostile territory

**Good.**

> Subject: Fernbank is relicensing to BUSL on Nov 1 - happy to answer the hard questions
>
> Hi Alex,
>
> Heads up before it lands, since you wrote the definitive piece on the last relicensing wave.
>
> Fernbank moves from Apache 2.0 to BUSL 1.1 on Nov 1, with a four-year Apache conversion window. Existing releases stay Apache forever. The trigger was three vendors reselling the hosted product at a combined revenue several times ours; the numbers are in the post.
>
> We expect people to be angry and we're not going to pretend otherwise. Our founder will do an on-record interview including the questions about community trust and the fork risk.
>
> Post and FAQ under embargo here: <link>.
>
> - Sam

**Weak twin.** Framing it as "a clarification of our licensing to better serve the community". Every reader recognises the move, and the euphemism becomes the story.

## The embargo email

Keep it separate from the pitch, and repeat the terms:

> Confirming: everything below is under embargo until **Thursday 9 September, 14:00 UTC**. If that doesn't work for your publishing schedule, tell me now and I'll find a way rather than have you sit on it.
>
> In the pack: the announcement, two approved quotes, the benchmark harness, architecture diagram, and screenshots. <name> is available for interview Tue-Wed, 09:00-17:00 CET.
>
> I'm reachable at <phone> from lift time onwards for corrections.

## The source reply, when a reporter asks you for a quote

Answer in publishable form. Speed beats polish here - a usable answer in twenty minutes gets used; a perfect one tomorrow does not.

> Happy to be quoted:
>
> "Most teams don't have a caching problem, they have a cache-invalidation problem, and buying a bigger cache makes it worse." - Sam Okoye, principal engineer, Fernbank
>
> Two things I'd add off the record if useful: <context>. And I'd push back gently on the framing that this is new - <reason>.
>
> Reachable until 22:00 CET tonight on <phone>.

## What separates the good from the weak

- The good version could be checked by a stranger before publication; the weak one could only be repeated.
- The good version names a consequence for the reader; the weak one names a feeling of the sender.
- The good version concedes something true and unflattering. That concession is what makes the rest believable to a technical audience.
