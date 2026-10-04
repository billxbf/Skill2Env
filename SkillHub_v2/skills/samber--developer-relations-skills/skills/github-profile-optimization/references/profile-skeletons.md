# Profile skeletons and worked examples

Pick the skeleton matching what the _reader_ is deciding, not what the account happens to contain. Every skeleton is a starting order, not a required section list - delete anything the account cannot fill honestly.

## Contents

- Personal: maintainer of a used project
- Personal: DevRel practitioner or advocate
- Personal: engineer building credibility
- Organization: public profile
- Organization: member-only profile
- Worked examples, positive and negative
- Observed patterns on shipped organization profiles

## Personal: maintainer of a used project

Reader is deciding whether to use, trust, or contribute to your work.

1. One sentence: what you build and for whom.
2. The projects, three to six lines, each `name - what it does - who it is for`. No stars.
3. Project status in plain words: maintained, seeking maintainers, feature-frozen.
4. How to reach you for what: bug reports here, security there, commercial questions elsewhere.
5. Optional: funding route, in one line.

Pins carry the weight here: flagship first, then the repositories a contributor or integrator actually opens next.

## Personal: DevRel practitioner or advocate

Reader is a conference organizer, a hiring manager, a potential collaborator, or a developer who just watched your talk.

1. One sentence: the ecosystem you work in and the audience you serve.
2. Recent public work: talks, posts, videos - three items with links, newest first.
3. What you are working on now, with the month it was last true.
4. Where else you are: the four social links plus a personal site.
5. Speaking or collaboration availability, if you want inbound.

Pins here are portfolio artefacts - demos, workshop material, tools you built for talks - not necessarily your most-starred repositories.

## Personal: engineer building credibility

Reader is evaluating capability from public evidence.

1. One sentence: what you do and the stack you do it in.
2. Two or three projects with an outcome each ("handles N requests/day", "used by X").
3. Contributions to other people's projects, linked to merged pull requests rather than claimed.
4. Contact route.

Skip stats widgets entirely: they measure activity, and the reader is judging judgement. The contribution graph is weak evidence in both directions, so let merged pull requests carry the proof.

## Organization: public profile

Reader is a developer sent here from a search result, a talk, a package page, or a job posting.

1. Positioning line: what the organization builds, in the visitor's vocabulary.
2. The open-source stance: what is open, what is commercial, under which licence. One short paragraph, stated plainly.
3. Entry points: two to five named repositories with a one-line "start here if you want to…".
4. One primary call to action: documentation, community, or careers - pick one, not three.
5. Optional: how to contribute, and where support actually happens.

Pins should not simply repeat the repositories named in the README prose; use them to cover a second layer (runtime components, SDKs, examples) so the two surfaces together give a fuller tour.

## Organization: member-only profile

Only build one if someone owns it. Useful content: paved-road repositories, internal onboarding entry points, who to ask for what. It rots faster than the public one because nobody outside sees it - assign an owner and a review date or skip it.

## Worked examples, positive and negative

**Positioning line - personal**

- Weak: `Full-stack developer passionate about clean code and new technologies.` Unfalsifiable, describes half the platform.
- Strong: `I maintain the Rust client for <protocol> and write about database internals. Most of my public work is storage-layer tooling.`

**Positioning line - organization**

- Weak: `We are building the future of developer productivity.` No product, no audience, no verifiable claim.
- Strong: `The Postgres development platform - hosted Postgres with auth, storage and realtime, most of it open source.` Names the technology, the surface area, and the licensing stance.

**Project list entry**

- Weak: `⭐ awesome-thing - 2.3k stars!` Stars are already displayed by the platform; repeating them adds nothing and dates instantly.
- Strong: `awesome-thing - schema diffing for Postgres migrations. Start here if you review migrations in CI.`

**Status line**

- Weak: `🔭 I'm currently working on something exciting!` Unverifiable, and reads as abandoned six months later.
- Strong: `Maintained. Reviewing pull requests weekly; last release 2026-07. Not accepting new feature requests until the 3.0 branch lands.`

**Decoration**

- Weak: a stats card, a streak card, a trophy row, a visitor counter and a typing animation above the first sentence. Five external dependencies, each of which can freeze in the image proxy, and no information a reader can act on.
- Strong: one project banner with alt text, or nothing at all.

**Call to action**

- Weak: five links of equal weight (docs, blog, Discord, Twitter, newsletter, careers).
- Strong: one bolded primary route plus a short "elsewhere" line.

**Audience mismatch - the most expensive mistake here**

An engineer targeting infrastructure teams ships a streak card, a trophy row and a language-percentage donut above their first sentence. It reads as engaged to an early-career peer group and as noise to the senior reviewer they are actually trying to reach - and none of the three widgets can see the private work that is most of their output. The fix is not fewer widgets; it is three pinned original repositories, each with a description and an outcome line, plus the anonymized private-contribution toggle enabled.

**Employed developer with an empty graph**

- Weak: "commit something small every day to rebuild the streak." That is padding evidence, it is visible as padding, and it fixes nothing about the private work it is meant to represent.
- Strong: enable anonymized private-contribution counts, then link two merged pull requests in other people's repositories. Both are checkable; a streak is not.

**Answering "how do I get more stars"**

- Weak: pointing at trending mechanics or promotion cadence as if the profile drove it.
- Strong: naming what stars measure (attention and promotion reach, not adoption or quality), noting that buying them is a detectable, industrialized practice, and redirecting to adoption evidence the page can honestly carry - named users, download counts, release cadence.

## Observed patterns on shipped organization profiles

Read live on 2026-08-26 - treat as evidence of convention, not as a template to copy:

- **Supabase** - tagline "The Postgres Development Platform", verified on two domains. Pins run flagship first, then the runtime components an integrator opens next (realtime, postgres, postgres-meta, client library, auth). Pin order is an architecture tour, not a star ranking.
- **Grafana Labs** - README opens on a banner, then an open-source stance paragraph, then a named four-project block, then "Work with us" linking careers. Pins deliberately add projects the prose does not name (k6, Pyroscope), so the two surfaces cover different ground.
- **Vercel** - one-line positioning, pins mixing the famous open-source asset, the commercial CLI, and newer strategic bets.

None of the three uses stats widgets, visitor counters or trophy rows. All three have a verified domain badge.
