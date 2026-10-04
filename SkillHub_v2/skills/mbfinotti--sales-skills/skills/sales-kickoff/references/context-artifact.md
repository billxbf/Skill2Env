# Context artifact - `sales-context.md`

One versioned file at the project root, committed with the project when it lives in git.

- Existence: the cold/warm signal.
- Content: what the warm start reads instead of re-interviewing.

Keep every field short - this file is read at every session start, so bloat taxes every session.

## Template

```markdown
# Sales context

- **Updated**: <date> (session <n>)
- **Motion**: <B2B outbound-led | B2B inbound/full-cycle AE | B2C high-ticket | mixed - one line of nuance>
- **Seat / team**: <who is selling: SDR, AE, founder…; team size and shape>
- **ICP / offer**: <who is bought by whom, price point, pricing floor - flag what is fixed vs contested>
- **Bottleneck**: <where the funnel hurts most right now, one line>
- **In-flight work**: <what is being built or fixed right now, one line per item>
- **Decided**: <closed decisions, one line each - off the table>
- **Open**: <live questions, one line each>
- **Constraints**: <quota deadlines, quarter close, sender-domain state, outreach regulation, tooling access>
- **Landing date**: <the date the result must land by, or none>
- **Horizon / effort ceiling**: <one-off or compounding asset; hours, a week, a few hours weekly, or headcount and sign-off>
- **Plan state**: <the planning decisions already made and where they live: motion, ICP, segment/tier model, org shape, quota method, comp plan - mark each settled or contested>
- **Stakeholders**: <name/role → decision role: decides | consulted | informed>

## Session log

- <date> - <session goal> → <skill(s) used> → <outcome in one line>
```

## Worked example

```markdown
# Sales context

- **Updated**: 2026-04-02 (session 5)
- **Motion**: B2B outbound-led, mid-market SaaS; ACV ~$18k, 60-day cycle
- **Seat / team**: founder selling + 1 SDR ramping; no dedicated AE yet
- **ICP / offer**: ops leads at 50-200-person logistics companies (fixed); pricing floor $12k - below only with founder sign-off
- **Bottleneck**: meetings book fine; deals stall after the demo
- **In-flight work**: outbound sequence v2 draft; champion maps on 3 stalled deals
- **Decided**: email + phone only, no social automation; one sequencer tool
- **Open**: whether to add an SMS touch for webinar-lead follow-up
- **Constraints**: sender domain warmed only 6 weeks; no call recording allowed on DE prospect calls
- **Landing date**: 2026-06-30 (Q2 close)
- **Horizon / effort ceiling**: compounding; a few hours every week, founder sign-off available, no headcount
- **Plan state**: motion settled (outbound-led); ICP settled; no formal segment/tier model, no quota method, no comp plan yet - all contested
- **Stakeholders**: founder → decides; SDR → consulted (cadence load); fractional CMO → informed

## Session log

- 2026-03-05 - pick a cold-outbound angle → sales-outreach-personalization → 3 ranked angles, hiring-surge angle chosen
- 2026-03-12 - build the cadence → sales-outbound-sequence → 8-touch plan, metric thresholds committed
- 2026-04-02 - unstick 3 stalled deals → deal-champion-mapping → all 3 single-threaded; prove-the-champion actions assigned
```

Why this works:

- Every field answers a question the next session would otherwise ask.
- The log line names goal, skill, and outcome.
- Contested items are flagged rather than smoothed over.

## Negative example - do not produce this

```markdown
# Sales context

We are an ambitious team building a world-class sales motion. We reach out
through various channels and there have been good conversations. Several deals
are in progress. Next steps: keep pushing and improve our sales process.

## Notes

- Great demo on Thursday, they seemed interested
- Lots of ideas about scripts, sequences, negotiation, hiring...
```

Why this fails:

- No field answers a concrete question (what is the motion? who decides? what is the pricing floor?), so the next session re-interviews anyway - the artifact exists but the start is still cold.
- "They seemed interested" is not evidence any deal skill can grade, and the idea dump routes nowhere.

## Update rules

- Patch changed fields; never rewrite the whole file each session.
- Refresh **Landing date** and **Horizon / effort ceiling** whenever either changes - the warm start re-ranks the short-list and the routines off those two fields instead of re-asking, so a stale value silently produces the wrong order.
- Append exactly one session-log line per session, before the session ends.
- Move an item from **Open** to **Decided** only when the stakeholder with the _decides_ role has signed off - record who.
- Keep a separate ADR-style decision log only when contested decisions genuinely accumulate; until then the Decided/Open lists are the record.
- Keep prospect and customer PII out of this file when it is committed to a shared repository - name roles and companies only as far as the team's own privacy rules allow.
