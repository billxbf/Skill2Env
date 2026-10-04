# Reputation, Measurement, and Remediation

## How placement is actually decided

- Gmail filters at the **mailstream** level, not per message (practitioner-verified, deliverability-expert lineage): reputation of the whole stream accumulates; unengaged deliveries "ding" it until a tipping point, then placement collapses suddenly even though the cause built up slowly.
- The spam-button complaint is the single largest negative signal. Even delete-without-reading counts negatively - an expert estimate puts it around 10% of a spam click's weight (practitioner estimate, not a provider figure).
- Placement is personalized per recipient: the same message can inbox for one user and junk for another. No single test message "proves" placement.
- These mechanics are identical for B2B and B2C; only the levers to influence them differ (see feedback loops and warmup below).

## Thresholds

- Provider-verified, Gmail only: spam rate below 0.10% target; never at or above 0.30%. Measured daily, based on inbox-delivered mail. Since June 2024, senders at ≥0.30% lose mitigation eligibility until 7 consecutive days below it. Negative impact starts above 0.10%, graduated.
- "Keep complaints under 0.1%" as a universal cross-provider law is a vendor extrapolation - Yahoo and Microsoft publish no equivalent number.
- Bounce-rate action points (2%, 3-5%) and "healthy inbox placement ≥90%" tiers are vendor conventions. Direction is sound; magnitudes are not authoritative.

## Instrumentation - enroll before reviewing anything else

Ranked on setup time and standing monitoring; every option here is reversible, so reversibility does not separate them.

- value (visibility bought): Google Postmaster Tools > DMARC aggregate reports > Microsoft SNDS/JMRP > Yahoo CFL
- effort: Microsoft SNDS/JMRP > Yahoo CFL > Google Postmaster Tools == DMARC aggregate reports
- efficiency (enroll first): Google Postmaster Tools == DMARC aggregate reports > Microsoft SNDS/JMRP > Yahoo CFL

Postmaster Tools and DMARC reporting tie on both axes for a real reason: each costs one DNS record, and neither substitutes for the other - one exposes a complaint rate no other source publishes, the other exposes which mail flows are misaligned. Enroll both in one sitting.

What this order starves is the per-complainer feedback loops (SNDS/JMRP, CFL), which cost an hour each and pay only in proportion to that provider's share of the list. Re-rank on the recipient provider mix: a Microsoft-heavy list promotes SNDS/JMRP to first, and Postmaster Tools says nothing about mail it never sees.

- Google Postmaster Tools: the only visible Gmail complaint signal (aggregate spam rate, domain/IP reputation, authentication dashboard, compliance status).
- Microsoft SNDS + JMRP: IP-level data plus per-complaint junk reports.
- Yahoo Complaint Feedback Loop (CFL): per-message complaint reports (ARF, keyed to the DKIM domain); requires DKIM.
- DMARC aggregate-report analysis: the cheapest way to find misaligned or unknown mail flows.
- Feedback-loop asymmetry (provider-verified): Yahoo and Microsoft let you suppress individual complainers after the fact; **Gmail has no per-message feedback loop** - only the aggregate rate. For Gmail, prevention (targeting, relevance, easy opt-out) is structurally the only option.
- Google states verbatim that it does not track open rates and cannot verify third-party open figures. Combined with Apple Mail Privacy Protection pre-fetching pixels (~55-60% of opens per Litmus 2026, vendor measurement; other vendor estimates differ widely), opens are unusable as a placement or engagement KPI. Use replies, non-Apple clicks, bounces, complaints.

## Seed-list / inbox-placement tests

- Mechanics: send to a panel of seed inboxes, read folder placement per provider.
- Validity problems (practitioner-verified, acknowledged by the panel vendors themselves): seed inboxes have no engagement history, and modern placement is personalized by per-recipient engagement - a seed "inbox" result does not prove real recipients will inbox. A large seed set relative to a small real list is itself a negative signal.
- Use them as directional input beside postmaster data and real engagement, never as proof. Vendor "global inbox placement ~83-84%" benchmarks measure the vendor's own panel.

## Warmup and volume - conventions, honestly labeled

- Provider-verified principle only, no numbers: start with low volume, increase slowly, avoid bursts, never immediately double previous volume (Gmail guidance).
- Everything numeric is vendor convention: 2-8 week ramps, "let a new domain sit 2-4 weeks", 30-50 emails/mailbox/day (vendor ranges span 10-65 - a ~3x disagreement with no shared methodology). Treat all of it as starting hypotheses to tune against the sender's own postmaster data. Scale by adding honestly-identified mailboxes/domains, not by pushing one mailbox harder.
- Automated warmup networks (tools that auto-send and auto-reply between member mailboxes) manufacture artificial engagement - the practice M3AAWG names as egregious. Providers increasingly detect it; no independent evidence shows it improves real-recipient placement; it papers over list and authentication problems. Do not recommend them; flag them when found in a setup.
- B2C divergence: bulk ESP senders warm **dedicated IPs** on published day-by-day ramps (dedicated IPs generally recommended above roughly 100k/month - vendor guidance); cold B2B is mailbox-based and warms domains/mailboxes. B2C bulk hygiene additionally includes double opt-in, sunset policies for chronically unengaged addresses, re-engagement before suppression, and rate-limited signup forms (list-bombing defense) - none of which exist in cold B2B.
- Vendor figures to never repeat as fact: "150+/day = 43% higher spam rates", "missing auth = 52% lower placement", "compliant senders average 89% inbox placement". No published methodology behind any of them.

## Remediation - burned domains and blocklists

Triage order (practitioner consensus):

1. Confirm the listing and identify **which asset** is listed: sending IP, sending domain, or a link/URI domain in the body.
2. Stop sending on the affected stream.
3. Fix the root cause (list quality, authentication, complaint driver). Delisting before fixing gets you re-listed, and repeat offenders wait longer.
4. File one documented removal request. Major-blocklist removal is free - anyone charging for delisting is selling a scam tax.
5. Choose the recovery route - rebuild volume slowly on the same domain, or park it and replace it. Ranked below.

Notes:

- Only a handful of blocklists meaningfully affect major-provider delivery (the large reputation lists: Spamhaus SBL/DBL-class, SURBL, SpamCop, Barracuda). "Listed on 200 blacklists" checker results are mostly irrelevant regional noise.
- A domain-level listing needs different remediation than an IP listing - changing IPs won't help a listed domain.
- **Gmail has no delisting process.** Its mitigation form is available only to bulk senders already meeting all guidelines. Recovery = fix spam rate and authentication, then wait (7 clean days restores mitigation eligibility).

### Retire vs rehabilitate

Effort is warming time, monitoring, and reversibility, never a price:

- value (a sending domain that inboxes again): park and replace == rehabilitate
- effort: rehabilitate (a week of clean sending at best, a quarter for a repeat offender, no Gmail delisting path) > park and replace (an hour to provision, a week or more to warm)
- efficiency: park and replace > rehabilitate

The value tie is genuine, not an evasion: neither route buys better placement than the other, only a different wait, which is why effort decides. Rehabilitation wins on exactly one condition - the burned asset is the domain carrying corporate and transactional mail, or one holding years of accumulated positive reputation. Neither can be replaced at all, so the effort axis stops applying and the wait is the only option.

The replacement must honestly identify the same sender: replacing a domain to escape identity, rather than to reset an accidental burn's cost, is the abuse side of the line and never a ranked option. No independent data on recovery rates exists; "85%+ delisting success" claims are vendor and unverified.
