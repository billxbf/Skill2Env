# Press Kit Checklist

Contents: press page · briefing pack · technical proof pack · quote craft · spokesperson prep · maintenance.

Two artefacts with different lifetimes. The press page is public and permanent. The briefing pack is private and per-announcement.

## Press page (`/press` or `/newsroom`)

- [ ] One-sentence, one-paragraph and ~100-word descriptions, copy-paste ready, in the same words the company uses everywhere else.
- [ ] Founding date, headquarters, headcount band, total funding if disclosed.
- [ ] Leadership and principal-engineer bios, third person, with high-resolution headshots downloadable without a form.
- [ ] Logo pack: SVG and PNG, light and dark, with usage rules and the correct capitalisation of the product name.
- [ ] Product screenshots and one short demo recording.
- [ ] Coverage list, most recent first.
- [ ] A named press contact, a real email address, and a stated response time.
- [ ] Pronunciation note if the name is not obvious.

Anti-patterns that cost coverage:

- A contact form instead of an address.
- Assets behind a lead-capture gate.
- A logo pack in a proprietary archive format.
- A page whose latest entry is two years old, which reads as a dead company to anyone checking before they write.

State a response time only if it will be honoured. An unmonitored press address is worse than none.

## Briefing pack (per announcement)

- [ ] The news in one sentence, then in one paragraph.
- [ ] Embargo line - date, clock time, timezone - repeated in the email and in the document.
- [ ] Two or three approved quotes with name, title and pronunciation if needed.
- [ ] Interview availability: who, which windows, which timezone, how to reach them at lift time.
- [ ] Assets: architecture diagram, screenshots, short recording, logo.
- [ ] The technical proof pack below.
- [ ] A named contact reachable during the embargo and at lift.
- [ ] For funding: round size, lead, participating investors, prior total, and what the money changes.
- [ ] For an open-source announcement: repository link, licence, governance state, maintainer count.

Send it as a linked page or plain text. A PDF is the format reporters complain about most, because they cannot copy from it cleanly on a deadline.

## Technical proof pack

The part that decides whether a developer-press story survives its own comment section.

- [ ] A running artefact: repository, sandbox, preview environment, or downloadable build available now - not "on request".
- [ ] Every performance claim with hardware, software versions, dataset, configuration and the harness, ideally public and runnable by a stranger.
- [ ] Architecture explanation separating what is genuinely new from what is assembled from known components.
- [ ] Comparison table against real alternatives with stated criteria - including the rows where you lose.
- [ ] Known limitations and an explicit statement of who this is not for.
- [ ] Licence, pricing and the boundary between open and commercial, stated without ambiguity.
- [ ] Security and compliance posture when the audience is enterprise buyers.
- [ ] Whatever a sceptical commenter would demand within an hour of publication - supply it before they ask.

## Quote craft

Reporters cut quotes that say nothing. A usable quote makes a claim, takes a position, or explains a decision.

- Weak: "We're thrilled to bring this innovative capability to our customers."
- Usable: "We knew the plugin API had to break the day we measured that 80% of our tail latency was other people's code running in our request path."

Write quotes for the person who will be named, in their own register, and get their approval before they ship. Two quotes is usually enough: one from the technical decision-maker, one from a customer or partner if the story needs external validation.

## Spokesperson prep

- Brief the spokesperson on the angle, the three points to land, and the two questions they least want.
- Agree in advance what is off the record and what is embargoed - different things, both stated explicitly.
- Rehearse the honest answer to the hardest question. Conceding a real limitation before bridging is what a technical audience reads as credible; a dodge is what they clip.
- Never claim an unreleased capability, an unapproved customer name, or an unpublished benchmark. Published articles outlive embargoes.
- If the spokesperson is going on a recorded show rather than into a written piece, hand the preparation to samber/developer-relations-skills@tech-podcast-interview-prep.

## Maintenance

Refresh the press page whenever headcount, funding, leadership or the product description changes, and add coverage as it lands. Re-check every asset link before each announcement; a broken logo link in a briefing pack is a request the reporter will not send twice.
