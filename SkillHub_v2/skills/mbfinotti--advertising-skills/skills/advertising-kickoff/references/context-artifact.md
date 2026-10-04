# Context artifact - `advertising-context.md`

One versioned file at the project root, committed with the project when it lives in git. Its existence is the cold/warm signal; its content is what the warm start reads instead of re-interviewing. Keep every field to one line - this file is read at every session start, so bloat taxes every session.

## Template

```markdown
# Advertising context

- **Updated**: <date> (session <n>)
- **Business model**: <B2B sales-led | B2B self-serve | B2C | mixed - one line of nuance>
- **Offer / price point**: <what is sold and at what price; note AOV or contract value>
- **Channels / spend**: <channels currently bought, monthly spend band, committed vs discretionary>
- **Conversion / source of truth**: <the event that counts as success; which system is authoritative for it>
- **CAC-ROAS position**: <current position vs target; whether a written guardrail policy exists>
- **In-flight work**: <what is being built, tested, or fixed right now, one line per item>
- **Decided**: <closed decisions, one line each - off the table>
- **Open**: <live questions, one line each>
- **Constraints**: <budget commitments, the date a result must land by, compliance/regulated vertical, creative capacity>
- **Horizon / effort ceiling**: <one-off win or compounding asset; hours, weekly time, or headcount and sign-off available>
- **Stakeholders**: <name/role → decision role: decides | consulted | informed>

## Session log

- <date> - <session goal> → <skill(s) used> → <outcome in one line>
```

## Worked example

```markdown
# Advertising context

- **Updated**: 2026-04-09 (session 5)
- **Business model**: B2C e-commerce, self-serve; a B2B wholesale line exists but gets no paid spend
- **Offer / price point**: skincare subscription, $42/month; AOV $58 with one-time add-ons
- **Channels / spend**: paid social + paid search, ~$28k/month; $10k committed to a seasonal flight through May
- **Conversion / source of truth**: first paid subscription; order system authoritative, platform pixels indicative only
- **CAC-ROAS position**: blended CAC $61 vs $70 break-even; guardrail policy written, owned by the CFO
- **In-flight work**: retargeting sequence redesign (draft); Q2 creative test batch in briefing
- **Decided**: no new channel until the seasonal flight ends; UGC creators over studio production for Q2
- **Open**: whether to move search to value-based bidding after the flight
- **Constraints**: seasonal peak ends 2026-05-31; one designer, ~2 assets/week; no consent-mode gaps allowed (EU traffic)
- **Horizon / effort ceiling**: compounding asset; ~4 hours/week from the growth lead, no new headcount before Q3
- **Stakeholders**: growth lead → decides; CFO → consulted (guardrails, budget raises); founder → informed

## Session log

- 2026-03-12 - why did ROAS drop → `mbfinotti/advertising-skills@ad-account-diagnostic` → creative decay named as failing layer
- 2026-03-19 - confirm wear-out → `mbfinotti/advertising-skills@ad-creative-fatigue` → verdict: fatigued, brief replacements
- 2026-04-09 - brief Q2 creative batch → `mbfinotti/advertising-skills@ad-creative-brief` → 3 briefs handed to designer and 2 creators
```

Why this works:

- every field answers a question the next session would otherwise ask
- the log line names goal, skill, and outcome so re-routing can build on it
- the source of truth is named so measurement questions never get re-litigated
- constraints carry dates the routines can anchor to

## Negative example - do not produce this

```markdown
# Advertising context

We are an ambitious brand investing in performance marketing across multiple
platforms to drive growth. Our ads could be doing better and there are many
ideas floating around about creative, budgets, and new channels. The team is
aligned on moving fast. Next steps: keep optimizing and test more things.

## Notes

- Spend is significant
- Tracking may or may not be fine
- Lots of ideas: TikTok? influencers? more retargeting? rebrand?
```

Why this fails:

- no field answers a concrete question (which channels? what spend? which event counts? who decides?), so the next session must re-interview anyway; the artifact exists but the start is still cold
- "Spend is significant" gives the budget cluster nothing to route on
- "Tracking may or may not be fine" hides the one fact that gates every launch
- the idea dump routes nowhere

Vague ambition displaces the facts the router actually needs.

## Update rules

- Patch changed fields; never rewrite the whole file each session.
- Refresh **Constraints** and **Horizon / effort ceiling** the moment either changes. The short-list and the routine set are re-ranked from those two fields on every warm start, so a stale value silently mis-orders the whole session's recommendations.
- Append exactly one session-log line per session, before the session ends.
- Move an item from **Open** to **Decided** only when the stakeholder with the _decides_ role has signed off - record who.
- Keep a separate ADR-style decision log only when contested decisions genuinely accumulate (e.g. repeated budget-raise disputes); until then the Decided/Open lists are the record.
- These rules apply unchanged to B2B and B2C projects; only the field values differ.
