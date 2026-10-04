# Curation method detail

Contents: the numeric budget-fill arithmetic, the full freshness-check reasoning, and the re-ranking heuristics SKILL.md compresses to a summary.

## Fill the budget, then re-rank

Fill the declared effort ceiling top-down from the efficiency order in SKILL.md, then stop. Only for that arithmetic, turn the magnitudes into numbers:

- Newsletter issue: ~5 minutes.
- Benchmark report: ~20 minutes once a quarter (~2 minutes a week).
- Podcast episode: ~35 minutes.
- Live show: ~50 minutes.
- Capped community habit: ~20 minutes a week.
- Capped feed skim: ~10 minutes a week.

The ranking never depends on those numbers. They exist to check a list against a budget, and a user who reads twice as fast changes every one of them without changing the order.

## Re-rank against what you already know about the user

The default assumes attention is uniform, and it rarely is. Before presenting anything, adjust for:

- A commute or a gym habit makes audio nearly free, so podcasts and live shows jump to the top for that user. Interview question 6 (mediums actually consumed) is what surfaces it.
- A community already joined, or a membership already paid, starts at zero cost and outranks a newsletter that still has to earn a subscription.
- A user who already reads every newsletter in their niche has exhausted that rung; their next marginal minute is worth more in a community or a benchmark report.
- A vertical with little benchmark reporting - most of B2C high-ticket - moves benchmark reports down for lack of supply, not lack of value.

This ordering is a default, not a law. It shifts with context and with who executes it: a rep who retains nothing from audio and a rep who retains nothing from text should not receive the same list.

## Freshness check, full reasoning

The dominant failure mode in this field is silent brand migration, not shutdown - see sources.md's Graveyard table for named cases (Sales Hacker to GTMnow, Blissful Prospecting to Outbound Squad, Outreach.io to Outreach.ai). Old URLs redirect or die quietly, so "the page loads" proves nothing in either direction.

If you can browse or fetch the web, verify each source this way:

1. Fetch the source's URL and inspect where it lands. A redirect to a different brand means migration, not death - record the new identity. A loading page is not proof of life until you see dated recent content.
2. Confirm the fetched page belongs to the entity you meant before recording any verdict. Domain collisions are real: lookalike domains get resold or belong to unrelated companies in other industries (see the Bridge Group caution in sources.md - bridgegroupinc.com is the research firm, bridgegroup.com is an unrelated wealth manager).
3. Check podcasts on the podcast host or RSS feed, never the company homepage. Company-affiliated shows sit on lead-gen landing pages that publish no episode archive.
4. Treat an empty personal newsletter platform as inconclusive about the person. Creators spin up a newsletter, post twice, and move their real cadence elsewhere (Josh Braun and Kyle Coleman's dead Substacks are the named example) - check a second channel before calling them inactive.
5. Treat a failed fetch on YouTube, Reddit, LinkedIn, or X as unknown, not dead. These platforms block plain fetches; a verdict there needs an authenticated browser session or a second source.
6. Record a last-verified date on every entry you touch. A list without per-source dates rots silently.
7. Never invent a subscriber, download, or member count. Report numbers only with their origin ("self-claimed", "third-party tracker"), and write "not stated" when none is published. Self-reported community counts routinely exceed third-party estimates several-fold (RevGenius's own 60k-100k claim against a ~17k third-party tracker figure is the named example in sources.md).

If you cannot browse the web, build the list from the snapshot alone: state the snapshot date prominently, keep each source's recorded status and last-verified date, and tell the user which entries deserve a manual re-check before they invest time.
