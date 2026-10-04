# Worked Examples

Two full rule sets, one filled dossier, one negative example. Provenance tags: [ACADEMIC] peer-reviewed result, [VENDOR] vendor or agency rule of thumb, [DERIVE] compute from the program's own data. All [DERIVE] values below are illustrative - recompute from the program's own 90-day baseline.

## Rule set - B2C ecommerce (apparel store, 350 affiliates, ~$60K/month commissions, last-click, 30-day cookie, 60-day hold)

| #   | Signal                                            | Threshold                                                | Band               | Action                                           | Legitimate trip risk                                     |
| --- | ------------------------------------------------- | -------------------------------------------------------- | ------------------ | ------------------------------------------------ | -------------------------------------------------------- |
| C1  | Data-center ASN / declared bot / non-browser UA   | Any (GIVT list filter)                                   | -                  | Filter pre-commission, no case opened            | None - list-based                                        |
| C2  | Time on site after cookie set                     | < 2s [ACADEMIC]                                          | Hold & Investigate | Throttle; run cookie-drop reproduction           | Deep-linked flash-sale traffic - check landing page      |
| C3  | Conversion rate                                   | > 2 SD above program mean, 2 weeks running [VENDOR→tune] | Watch              | Log; weekly triage                               | Genuinely great content partner - check traffic mix      |
| C4  | Chargeback rate                                   | > 3% rolling 30 days [VENDOR]                            | Suspend & Escalate | Suspend; reverse period; dossier to network      | Product-quality issue - check other affiliates' rate     |
| C5  | Clicks high, conversions near zero                | > 5x program click-to-sale ratio [DERIVE]                | Hold & Investigate | Throttle; referrer + redirect-chain audit        | Top-of-funnel content partner - check engagement         |
| C6  | Extension wins last-click seconds before checkout | Attribution flip < 60s pre-purchase, recurring [DERIVE]  | Hold & Investigate | Stand-down audit; contract check                 | Permitted coupon extension - terms decide, not this rule |
| C7  | Branded-SERP ad traced to affiliate               | Any, if terms ban brand bidding                          | Suspend & Escalate | Timestamped screenshots; warn once, then suspend | Whitelisted partner - check the whitelist first          |
| C8  | New affiliate: no traffic 2 weeks, then spike     | > 50 conversions in week 3 from cold start [DERIVE]      | Watch              | Manual review; keep net-90 terms                 | Seasonal creator launch - check content dates            |

## Rule set - B2B SaaS lead-gen (CPL program, $120/qualified lead, 60 partners, server-side postback, 90-day hold)

| #   | Signal                                | Threshold                                              | Band                    | Action                                  | Legitimate trip risk                                           |
| --- | ------------------------------------- | ------------------------------------------------------ | ----------------------- | --------------------------------------- | -------------------------------------------------------------- |
| B1  | Form-fill time                        | < 3s, no pointer movement [VENDOR]                     | Hold & Investigate      | Throttle; sample-call the leads         | Autofill power users - pair with B2 before acting              |
| B2  | Disposable/role-account email domains | > 10% of partner's leads [DERIVE]                      | Hold & Investigate      | Throttle; validate remaining leads      | Privacy-conscious ICP - check qualified rate                   |
| B3  | Lead-to-qualified rate                | < half program norm over 30+ leads [DERIVE]            | Hold & Investigate      | Throttle; CRM outcome export to dossier | Untrained SDR routing - check other partners' rate same period |
| B4  | Lead-to-demo-show rate                | Near zero over 20+ booked [DERIVE]                     | Suspend & Escalate      | Suspend; reverse unlocked leads         | Wrong-timezone booking flow - check booked times               |
| B5  | Duplicate contact data across leads   | Same phone/device fingerprint, 3+ "companies" [DERIVE] | Suspend & Escalate      | Suspend; dossier; clawback              | Agency submitting for clients - verify with the partner        |
| B6  | Conversion velocity                   | 3+ leads/minute or metronomic ~30s spacing [VENDOR]    | Hold & Investigate      | Throttle; server-log review             | Webinar/conference batch upload - check event calendar         |
| B7  | Volume up, zero customers downstream  | 90 days, 50+ leads, no closed-won [DERIVE]             | Watch → Hold at quarter | Quarterly review; reprice-or-exit talk  | Long sales cycle - match window to cycle length                |

Do not swap these sets: B2C click-timing rules on B2B lead-gen produce false positives; B2B downstream rules alone on ecommerce miss attribution theft for months.

## Filled investigation dossier (B2B case)

```
DOSSIER 2026-031  -  partner "LeadSpring Media" (platform ID P-4471)
Rules triggered  : B2 (34% disposable domains, Hold), B3 (lead-to-qualified 4% vs norm 22%,
                   Hold), B5 (41 leads across 3 device fingerprints, Suspend  -  this is the
                   rule the recommendation rests on; B2 and B3 alone would mandate Hold),
                   2026-07-02→08-10. B5 legitimate-trip check run: partner is not an agency
                   submitting for clients, confirmed against the signed profile
Baseline vs seen : qualified 22%±6 → 4%; demo-show 61% → 0% (11 booked)
Evidence         : CRM export (61 leads, outcomes); 9/10 sample calls dead numbers;
                   postback log  -  41 leads from 3 device fingerprints; screenshots archived
Exposure         : $7,320 held (61 × $120); $3,480 paid prior cycle; reserve covers $1,050
Declared vs seen : declared "newsletter + LinkedIn"; observed referrers 88% blank
Prior history    : none; partner active 11 weeks
Recommendation   : Suspend & Escalate  -  reverse held, claw back paid via negative balance.
                   Reviewer: program owner (not detecting analyst)
Appeal           : notified 08-12, neutral wording; 14-day window open until 08-26
```

## Negative example - do not deliver this rule set

> "Flag any affiliate whose session durations average under 5 seconds (industry standard). Terminate immediately - fraud must be stopped fast. Our coupon extension partner converts 4x the program average, which proves poaching: terminate and claw back. Target: catch 100% of fraud. The network's compliance team monitors our program daily, so no separate investigation process is needed. Hold window stays at 14 days to keep affiliates happy."

Why every sentence fails:

- "Industry standard" is a vendor rule of thumb presented as a constant, untuned against any baseline - and session-duration heuristics are exactly what AI-generated synthetic traffic now defeats.
- Instant termination destroys the evidence a network report or legal escalation would need, and skips any appeal - the false positive is unrecoverable.
- High conversion from a coupon extension is a last-click artifact, not proof of anything: that partner needs an incrementality test and possibly a lower tier, not enforcement.
- A 100% catch target with no false-positive ceiling guarantees over-blocking; catch rate and false-positive rate are only meaningful as a pair.
- The network is structurally conflicted (paid on commission volume) and reactive; nobody is monitoring the program daily on the owner's behalf.
- A 14-day hold against 120-180-day chargeback windows means every stolen-card commission is paid and gone; no clawback, reserve, or negative-balance clause is even mentioned.
