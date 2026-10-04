# Context artifact - `partnerships-context.md`

One versioned file at the project root, committed with the project when it lives in git. Its existence is the cold/warm signal; its content is what the warm start reads instead of re-interviewing. Keep every field to one line - bloat taxes every session start.

## Template

```markdown
# Partnerships context

- **Updated**: <date> (session <n>)
- **Partner motion(s)**: <channel / alliance / co-sell / marketplace / affiliate / influencer / referral - which are in play>
- **B2B / B2C**: <who the program sells to; note when motions differ>
- **Program maturity**: <nothing yet | designing | live and small | live and scaled - per motion when they differ>
- **Partners / creators**: <counts per motion; concentration - e.g. top 3 partners' share of program revenue>
- **Commission / margin model**: <model in force per motion - rev share %, flat CPA, reseller margin, creator flat fee>
- **Attribution / source of truth**: <how conversions are attributed; which system is authoritative for payouts>
- **Legal / compliance posture**: <signed terms version, disclosure regime in scope, legal review capacity>
- **In-flight work**: <what is being built, negotiated or fixed right now, one line per item>
- **Decided**: <closed decisions, one line each - off the table>
- **Open**: <live questions, one line each>
- **Constraints**: <committed contracts, payout/finance approval gates, renewal dates, headcount limits>
- **Horizon / effort ceiling**: <landing date; one-off win vs compounding asset; hours, headcount, sign-off available>
- **Stakeholders**: <name/role → decides | consulted | informed>

## Session log

- <date> - <session goal> → <skill(s) used> → <outcome in one line>
```

## Worked example

```markdown
# Partnerships context

- **Updated**: 2026-05-14 (session 4)
- **Partner motion(s)**: affiliate program (primary); one reseller pilot in discussion, no co-sell or influencer motion yet
- **B2B / B2C**: B2B SaaS, self-serve entry tier; affiliates pitch to SMB ops managers
- **Program maturity**: affiliate live and small (7 months); reseller motion designing
- **Partners / creators**: 64 approved affiliates, 22 active; top 3 affiliates drive 71% of program revenue
- **Commission / margin model**: 25% recurring rev share for 12 months, 60-day validation window; reseller margin undecided
- **Attribution / source of truth**: last-click via tracking links, 90-day cookie; billing system authoritative for payouts, tracking platform indicative only
- **Legal / compliance posture**: terms v2 signed by all actives; FTC + UK CAP in scope; legal review is one external counsel, ~2-week turnaround
- **In-flight work**: payout-run audit process being set up; recruitment sequence for newsletter operators drafted
- **Decided**: no influencer motion before Q4; recurring commission stays capped at 12 months
- **Open**: whether the reseller pilot gets its own margin model or reuses the affiliate rate card
- **Constraints**: payouts run on the 15th monthly, finance sign-off required; renewal of the top affiliate's custom terms on 2026-08-01
- **Horizon / effort ceiling**: reseller margin decision due before the 2026-08-01 renewal; compounding - a few hours weekly, no new headcount, counsel only for terms changes
- **Stakeholders**: partnerships lead → decides; CFO → consulted (rates, payouts); founder → informed

## Session log

- 2026-04-02 - set the commission rate → affiliate-commission-structure → 25% / 12-month recurring adopted
- 2026-04-16 - draft the agreement → affiliate-program-terms → v2 drafted, sent to counsel
- 2026-05-14 - recruit newsletter operators → affiliate-recruitment-outreach → 3-touch sequence drafted for a 40-name list
```

Why this works: every field answers a question the next session would otherwise ask.

- The concentration note flags the risk `affiliate-performance-dashboard` and `partner-performance` need first.
- The named source of truth stops payout questions being re-litigated.
- The constraints carry the dates routines anchor to.
- The horizon and effort ceiling let the next session re-rank without re-asking.
- Each log line names goal, skill and outcome, so re-routing builds on it.

## Negative example - do not produce this

```markdown
# Partnerships context

We believe partnerships are a huge growth lever and are building a world-class
ecosystem across affiliates, resellers, influencers and more. Momentum is
strong and several exciting conversations are ongoing. The commission structure
is competitive. Next steps: keep recruiting great partners and explore new
channels.

## Notes

- Lots of affiliates signed up
- Payouts happen regularly
- Ideas: influencers? marketplaces? a big-brand alliance?
```

Why this fails: no field answers a concrete question, such as which motions are live, what rate applies, which system pays out, or who decides. The artifact exists, but the start is still cold.

- "Competitive" gives the economics cluster nothing to route on.
- "Payouts happen regularly" hides the run date the payout-audit routine anchors to.
- The idea dump routes nowhere.

## Update rules

- Patch changed fields; never rewrite the whole file each session.
- Append exactly one session-log line per session, before the session ends.
- Move an item from **Open** to **Decided** only when the stakeholder with the _decides_ role has signed off - record who.
- Keep a separate ADR-style decision log only when contested decisions accumulate (e.g. repeated commission-rate disputes); until then Decided/Open is the record.
- These rules apply unchanged to B2B and B2C programs; only the field values differ.
