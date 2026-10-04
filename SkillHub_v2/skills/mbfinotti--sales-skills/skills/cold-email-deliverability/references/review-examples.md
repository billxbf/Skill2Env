# Review Report Template and Worked Examples

## Table of Contents

- [Template](#template)
- [Findings](#findings)
- [Fix list (in this order)](#fix-list-in-this-order)
- [Measurement plan](#measurement-plan)
- [Worked example - failing review](#worked-example-failing-review)
- [Findings](#findings)
- [Fix list (in this order)](#fix-list-in-this-order)
- [Measurement plan](#measurement-plan)
- [Worked example - passing review](#worked-example-passing-review)
- [Findings](#findings)

## Template

```
# Deliverability Review - <sender> → <audience>

Verdict: BLOCKED | AT RISK | CLEARED
Regime: B2B cold | B2C bulk · Volume: <n>/day (bulk sender: yes/no) · Regions: <list>

## Findings
### 1. Authentication and setup
- [SEVERITY] finding (provenance)
### 2. Reputation and measurement
- ...
### 3. Content structure
- ...
### 4. Compliance
- ...

## Fix list (in this order)
1. ...

## Measurement plan
- Dashboards to enroll · metrics to watch · action thresholds

Gate: <n> BLOCKER, <n> RISK, <n> ADVISORY → verdict. (Not legal advice.)
```

## Worked example - failing review

Submitted setup: SaaS SDR team, 6 mailboxes on the primary corporate domain, ~900 templated sends/day, recipients across the US and Germany. Draft: HTML email built from a marketing template - header banner image, two product screenshots, a shortened tracking link, subject `Re: quick question about your Q3 roadmap` (no prior thread), no opt-out line. DMARC lookup returns nothing.

```
# Deliverability Review - acme sales team → US + DE prospects

Verdict: BLOCKED
Regime: B2B cold, templated at volume · 900/day (bulk: no) · Regions: US, DE

## Findings
### 1. Authentication and setup
- [BLOCKER] No DMARC record on the sending domain (provider-verified requirement
  trajectory; also blocks postmaster compliance status). Publish p=none with rua=
  reporting today; SPF/DKIM alignment unverified until reports arrive.
- [BLOCKER] Cold outbound runs on the primary corporate domain - one complaint
  wave degrades transactional and corporate mail (practitioner consensus).
  Move to a dedicated, honestly-identified sending domain and warm it gradually.
### 2. Reputation and measurement
- [RISK] No postmaster dashboard enrollment: the team is flying blind on the only
  visible Gmail complaint signal. Enroll before resuming volume.
### 3. Content structure
- [BLOCKER] Fake "Re:" subject with no prior thread - deceptive framing (ethics
  boundary; illegal under CAN-SPAM's deceptive-subject rule; M3AAWG-abusive).
- [RISK] Image-heavy HTML with no plain-text part; shortened redirect link
  (structural gateway scoring rules, provider-verified rule categories).
- [ADVISORY] Marketing-template design reads as bulk for 1:1 outreach;
  plain-text-style is the practitioner norm for cold B2B (unquantified).
### 4. Compliance
- [BLOCKER] German recipients: UWG §7 requires prior express consent even B2B -
  this list cannot be cold-emailed lawfully. Remove DE rows or obtain consent.
- [BLOCKER] US recipients: no opt-out and no physical postal address - both
  CAN-SPAM requirements.

## Fix list (in this order)
1. Publish DMARC (p=none + rua), verify SPF/DKIM alignment from reports.
2. Provision a dedicated sending domain identifying the real sender; ramp slowly.
3. Enroll Google Postmaster Tools, Microsoft SNDS/JMRP, Yahoo CFL.
4. Remove German recipients (or collect consent). Add opt-out line + postal
   address for US mail.
5. Rebuild the draft: plain-text part, real subject, full-URL links on your own
   domain, drop the banner/screenshots.
6. Only then: content polish. Note - no word-list edit would have changed any
   finding above.

## Measurement plan
- Gmail spam rate daily (<0.10% target, never ≥0.30%, provider-verified);
  bounce trend; reply rate. Ignore open rate (Apple MPP proxy opens ~55-60%
  per Litmus 2026, vendor; Google states it does not track opens).

Gate: 6 BLOCKER, 2 RISK, 1 ADVISORY → BLOCKED. (Not legal advice.)
```

## Worked example - passing review

Submitted setup: same team, three weeks later. Dedicated sending domain with aligned SPF/DKIM and DMARC `p=quarantine`; PTR and TLS confirmed; Postmaster Tools shows spam rate 0.05%; 240 sends/day across 6 warmed mailboxes; US-only list; plain-text draft, one full-URL link on the sending domain, no pixel on first send, real subject, signature with name, role, postal address, and the line "If this isn't relevant, reply 'no thanks' and I won't write again."

```
# Deliverability Review - acme outbound v2 → US prospects

Verdict: CLEARED
Regime: B2B cold, templated at volume · 240/day (bulk: no) · Regions: US

## Findings
- [PASS] Auth: SPF+DKIM aligned, DMARC p=quarantine, PTR/TLS valid.
- [PASS] Reputation: spam rate 0.05% (below 0.10% target, provider-verified);
  dashboards enrolled; ramp within provider "increase slowly" guidance.
- [PASS] Content: plain-text part present, own-domain link, no deception.
- [PASS] Compliance (US): opt-out line, postal address, honest subject.
- [ADVISORY] Opt-out line in 1:1 cold mail is contested (complaint reduction
  vs bulk appearance - no independent test resolves it). Kept: the legal
  requirement outranks placement speculation. Acknowledged by user.
- [ADVISORY] 40/mailbox/day is a vendor convention, not a provider rule;
  adjust against your own postmaster data, not the folk number.

Gate: 0 BLOCKER, 0 RISK, 2 ADVISORY (acknowledged) → CLEARED.
Next review trigger: volume change, new region, or spam rate crossing 0.10%.
(Not legal advice.)
```
