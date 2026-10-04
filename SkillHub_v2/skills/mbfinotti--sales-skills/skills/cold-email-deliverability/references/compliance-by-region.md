# Legal Compliance by Recipient Region

Regulator-verified syntheses, not legal advice - say so in every report. The recipient's region controls, not the sender's. When a list spans regions, apply each region's rule to its recipients or the strictest rule to all.

National rules and penalty figures change; if you can browse the web, re-verify before asserting a current figure.

## Summary table

| Jurisdiction                   | B2B cold email                                                                                                                                        | B2C                                                | Max penalty                                                          |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------------------------- |
| US (CAN-SPAM)                  | Allowed without prior consent - opt-out regime; no B2B exception, same rules                                                                          | Same                                               | Up to $53,088 per email (FTC inflation-adjusted, effective Jan 2025) |
| EU (GDPR + ePrivacy Directive) | Lawful basis required; legitimate interest possible for B2B in many member states, with documented assessment; member states vary                     | Prior consent required                             | €20M or 4% global turnover                                           |
| France                         | Allowed to a professional address when the message relates to the person's profession; opt-out sufficient                                             | Prior consent                                      | GDPR ceilings                                                        |
| Germany (UWG §7)               | **Prior express consent generally required even B2B** - no exemption, including generic addresses (info@)                                             | Prior consent                                      | Up to €300,000 per case                                              |
| UK (PECR + UK GDPR)            | Corporate subscribers (companies, LLPs) exempt from the consent rule - legitimate interest works; sole traders/partnerships get individual protection | Prior consent (soft opt-in for existing customers) | Up to £500,000 (ICO)                                                 |
| Netherlands                    | B2B-friendly; legitimate interest + opt-out                                                                                                           | Consent                                            | GDPR ceilings                                                        |
| Canada (CASL)                  | **Express or implied consent required even B2B**                                                                                                      | Same                                               | Up to CAD $10M (organization)                                        |
| Australia (Spam Act 2003)      | Consent required (express or inferred)                                                                                                                | Same                                               | Substantial daily penalties                                          |

## US - CAN-SPAM specifics

Opt-out regime, explicitly covering B2B. Requirements:

- No false or misleading headers.
- No deceptive subject lines.
- Identify the message as an ad.
- Valid physical postal address in every email.
- Clear opt-out.
- Honor opt-outs within 10 business days.
- Opt-out mechanism functional for at least 30 days after sending.
- Sender remains liable for third parties sending on their behalf.

## EU - the GDPR / ePrivacy split

Two layers apply at once, and a sender can satisfy one while violating the other.

**GDPR (lawful basis):** legitimate interest can lawfully cover B2B outreach **if** a documented three-part assessment (purpose, necessity, balancing) exists, plus opt-out, sender identity, postal address, and a privacy-policy link. Legitimate interest does not cover B2C or personal addresses.

**ePrivacy Directive (unsolicited marketing):** the unsolicited-marketing article is transposed differently per member state - Germany is the clearest opt-in-only case even for B2B; treat Austria and Poland similarly conservatively. Segment EU lists by member state or apply the German standard to all.

## Canada - CASL specifics

Consent required even B2B, via one of three routes:

- Express consent.
- Implied consent via an existing business relationship - time windows apply, roughly 2 years from a transaction, 6 months from an inquiry.
- **Conspicuous publication**, which requires all three: the recipient conspicuously published the address, no accompanying statement refuses unsolicited messages, and the message is relevant to the recipient's business role.

Mere public availability is insufficient - regulators have rejected that defense in enforcement.

Process requirements:

- Honor opt-outs within 10 business days.
- Keep the unsubscribe functional 60 days after send.
- Keep consent records.

## B2B vs B2C, restated

- B2C bulk mail is opt-in everywhere that matters; the compliance question is consent quality (documented, specific, not pre-checked) plus working one-click unsubscribe.
- B2B cold is legal opt-out-style in the US, UK (corporates), France, Netherlands; effectively opt-in in Germany, Canada, Australia; assessment-gated elsewhere in the EU.
- Identical for both: no deceptive headers or subjects anywhere, an honest working opt-out, honoring it promptly, and sender identification.

## Review checklist

1. Map every recipient to a jurisdiction; flag unknown-region rows.
2. Verify the consent or lawful basis matches that jurisdiction (and is documented where documentation is required).
3. Check the draft for: sender identity, physical address where required, honest subject, visible opt-out.
4. Check the process: opt-out honored within the deadline, suppression list applied before every send, records kept.
5. Any miss on 2-4 = BLOCKER for the affected region's recipients.
