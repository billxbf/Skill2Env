# Curation method detail

Contents: the full attention-costing and budget-fill arithmetic, the ranking-axis reasoning, and the full freshness-check decay-mode taxonomy that SKILL.md compresses to a summary.

## Costing and ranking, in full

Cost each candidate as an order of magnitude of attention, never a precise figure:

- a text issue or post skimmed: minutes
- a video: tens of minutes
- a podcast episode: most of an hour
- a community: tens of minutes to skim, hours if the user posts rather than reads
- an annual event: days in one block

Halve any audio that rides on time already spent - commute, exercise - because that is not attention the user has to find.

Rank by efficiency: value returned per attention-minute, never by cheapness and never by audience size. The three axes disagree, so read all three before picking an order:

- effort (attention per week): `podcasts > community participation > video > newsletter == blog skim`
- value (what it buys): `community == events > podcasts > newsletters == blogs > video`
- efficiency (the default order): `newsletters == blogs > community skim > podcasts > video`

`newsletters == blogs` is a real tie on both axes - same skim cost, same good: what happened, in text quotable in a planning doc. Break it by fit to the user's day job, never by which is better known.

`community == events` ties because they buy the identical good - a question answered against the user's own situation, plus the discovery that renews the list - one continuous, one concentrated once a year. Events sit outside the efficiency line deliberately: amortising a two-day conference across 52 weeks makes it look nearly free and ranks it first, which is arithmetic lying about a cost the user pays as cleared days.

Within a medium, rank by role fit first, then durability: a named individual behind the content, institutional backing, and cross-surface recurrence (same person as podcast guest, speaker, and community lead) all outrank audience size. Never rank by subscriber count.

## Fill the budget, then re-rank

Convert each kept candidate's magnitude to a minutes-per-week number only for this arithmetic, and spend down to ~90% of the stated budget. Reserve the last ~10% for one community - communities surface new sources, which is how the list renews itself. Stop when the budget is spent, even if strong sources remain: name 2-3 as "bench" substitutes instead. The ordering above never depends on those minute figures; they exist only to stop the list overflowing, so a user who disputes a number should change it and keep the order.

Re-rank against what you already know about this user, and say which fact moved which source:

- a source they or their employer already pay for costs nothing extra to add, so its price stops being a reason to skip it
- an employer conference budget turns an event from a personal expense into a free slot
- a colleague already inside a community can be asked instead of joined
- speaking at or organising an event changes what it returns

The order is a default, not a law: it is calibrated for a time-poor practitioner who reads, and it shifts with the interview answers and with who executes it. An IC anchored on one CRM platform gets more per minute from ecosystem release notes than from GTM strategy newsletters, and a leader gets the reverse.

## Freshness check, full decay-mode taxonomy

Verify before recommending - a homepage's own cadence claim ("weekly show") is aspirational until a dated item confirms it. Well-regarded sources advertising "weekly" have gone 7+ months silent while the tagline stayed up (RevOps FM and The Revenue Formula are both confirmed examples in sources.md).

If you can browse or fetch the web, for each source: fetch the canonical URL, find the most recent dated item, and classify by that observed date, never by the site's own claim. Distinguish three decay modes rather than collapsing them into one "dead" verdict:

- **Renamed but alive** - a redirect to a differently-named but clearly related, actively updated property (UNBOUND replacing INBOUND is the named example in sources.md). Record as renamed, update the URL, keep it.
- **Domain resold or squatted** - the remembered URL now serves an unrelated business while the real source lives elsewhere. The link resolves, so this fails silently - confirm the page content actually matches the source's subject, not just that it loads.
- **Genuinely dead** - a parked or for-sale page (OpsStars is the named example in sources.md). Remove; a parked domain is the one unambiguous death signal.

Also catch **not-yet-alive**: a live "coming soon" page with zero published items is not a source yet (Sean Lane's "Higher Olive" is the named example). Note it for the next refresh; do not list it.

Some platform categories systematically resist automated checking: video platforms (consent walls, script-only pages), discussion forums (fetch-blocked), and short-post social networks (login walls, bot blocks). For sources on these, mark them unverified with the reason and fall back to manual: ask the user to open the page and report the newest item's date. For people whose main surface is a blocked social network, verify them via a fetchable surface instead - a podcast guest list, speaker roster, or community team page - and label any handle as stated-there, not independently verified.

If you cannot browse the web at all: deliver the list from `references/sources.md` with each entry's recorded verification date and status, state clearly that you could not re-verify, and give the user the manual check - open each URL, find the newest dated item, apply the classifications above.
