# Content Review - Structure Over Vocabulary

Run this only after authentication and reputation are cleared. Content is the weakest placement lever; say so in the report.

## The folklore explainer (give this when asked about "spam trigger words")

No independent, controlled, published study ties word choice, word count, or link count to spam **placement** (as opposed to reply rate). Reputation-based filters at the major consumer providers decide on authentication, sender reputation, and engagement first; individual words contribute almost nothing.

A clean-reputation domain inboxes "FREE!!! Act now"; a burned domain does not inbox a haiku. Vendor listicles ("600+ spam trigger words", "urgency phrases trigger immediate quarantine", "subject lines weighted 2-3x") cite no methodology; label them vendor and move on.

One honest nuance: corporate gateway filters (rule-based scorers of the SpamAssassin family, default spam threshold: score ≥5.0) do apply content rules. But those rules are overwhelmingly **structural** (image-only mail, mismatched HTML/plain-text parts, ALL CAPS, excess punctuation, URI reputation), not banned-vocabulary lists. Conflating gateway scoring with Gmail/Outlook consumer filtering is a common error; keep the two separate in the report.

## The ten structural checks

Severity map:

- BLOCKER: deception or a hard requirement missing.
- RISK: a structural signal rule-based filters score or providers document.
- ADVISORY: practitioner/vendor convention, direction sound, magnitude unproven.

The severity map orders the report; this orders the editing work:

- efficiency (fix first): deceptive framing > plain-text part > link-domain quality > image weight > opt-out mechanism > signature > ALL CAPS and punctuation > attachments > tracking pixels
- compliance cost (review triggered, reversibility lost): opt-out mechanism == signature > every other check, none of which carries any

Effort barely separates these: each is one edit to one template, an hour at most, with rebuilding an image-heavy layout sitting at the top of that hour - so value alone sets the order and no separate effort line would say anything. Opt-out and signature tie on compliance cost because they carry the same exposure, the recipient region's identification and opt-out requirements, checked against the same reference. Both jump the queue to first whenever that region requires them, since a legal requirement is a gate and not a rung.

No ranking for check 8 (length), nor for vocabulary. Ranking them would be false precision: no evidence orders them against the other checks or against each other, and a number placed there would be read as a finding.

1. **Deceptive framing** - fake `Re:`/`Fwd:`, forged headers, misleading From name, subject promising what the body doesn't contain. BLOCKER (also an ethics-boundary and legal issue in every region).
2. **Plain-text part** - HTML-only mail with no plain-text MIME part is scored by gateway filters; HTML and text parts that diverge score worse. RISK. For cold 1:1 B2B, the practitioner norm is plain-text-style mail resembling personal correspondence (no independent placement quantification - but it also removes checks 3, 5, 6 by construction). B2C bulk HTML design is normal and fine; this check diverges by regime.
3. **Image weight** - image-only mail and low text-to-image ratio are explicit gateway scoring rules. RISK if image-only; ADVISORY for heavy-but-not-only.
4. **Link count and link-domain quality** - domain reputation of every link matters more than how many; no credible "N links = spam" threshold exists (say so if asked). URL shorteners and redirect chains resemble phishing and are scored. RISK for shorteners/redirects or off-reputation link domains; keep link domains consistent with the sending domain.
5. **Tracking pixels and link rewriting** - contested: vendors claim pixels "trigger filters"; provider documentation supports only image-suppression for suspicious senders. Treat effects as reputation-mediated via the tracking **domain**, not automatic. Shared tracking domains tie your reputation to strangers'; a custom tracking domain is the fix if tracking is kept. "Naked" first sends (no pixel, no rewrites) are a vendor convention, reasonable for cold B2B. ADVISORY.
6. **Attachments** - discouraged in cold outbound (practitioner norm, unquantified); they add gateway suspicion and friction. ADVISORY; RISK for executable or archive types.
7. **ALL CAPS and excess punctuation** in subject or body - real structural scoring rules. RISK in the subject (also flag under the subject check), ADVISORY in the body.
8. **Length** - every "short emails work" number (best under 100 words; 20-39 words; 75-100 words) is a vendor **reply-rate** finding, the datasets contradict each other, and none measures spam placement. Advise brevity for replies if the user wants it, but never present length as a deliverability fix. ADVISORY at most, clearly labeled.
9. **Signature** - real name, real role, real company, working reply path; minimal links and images; physical postal address where the recipient's law requires it (compliance reference). Missing legally-required elements: BLOCKER via the compliance layer; bloated signature: ADVISORY.
10. **Opt-out mechanism** - regime split:
    - B2C / bulk / marketing: one-click `List-Unsubscribe` headers plus a visible link are a provider requirement; missing is a BLOCKER (see authentication reference for the exact headers).
    - B2B genuine 1:1 cold: genuinely contested, and no independent test resolves it. One camp: a plain-text opt-out line reduces complaints (the most damaging signal) and helps compliance. Other camp: an unsubscribe link makes 1:1 mail look bulk and can trigger filtering. Present both positions; default to a plain, honest opt-out sentence where the recipient's region requires an opt-out at all (most do), because the legal requirement outranks the placement speculation. Never hide or obfuscate it; that is a refusal.

## Subject line - boundary with the subject-line tester

Flag only deception (fake `Re:`/`Fwd:` - BLOCKER) and placement-damaging structure (ALL CAPS, excess punctuation - RISK). Do not score open-rate potential, judge angle or curiosity, or produce variants; route all of that to `mbfinotti/sales-skills@cold-email-subject-line-tester`.

## Reporting content findings

- Order findings by severity, then by check number; order the fixes the user has to make by the efficiency line above, never by that same reporting order.
- Attach the provenance label to every claim, especially vendor reply-rate statistics the user may already believe are placement rules.
- Close the content section with one sentence restating the hierarchy: content was reviewed last because it decides least.
