# Outreach Compliance

Legal constraints on the recruitment outreach itself, by prospect jurisdiction and channel. Segment the list by recipient location before drafting - the regime attaches to where the prospect is, not where the program is. This is operational guidance, not legal advice; route edge cases (mixed-jurisdiction lists, regulated verticals) to counsel.

## By jurisdiction

| Jurisdiction | Regime          | Cold email to prospects                                                                                                                                                                                                                                                                                                                                                                             | Must carry                                                                                                                          | Exposure                                                                    |
| ------------ | --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| US           | CAN-SPAM        | Legal without prior consent - no B2B exemption, all commercial email covered                                                                                                                                                                                                                                                                                                                        | Accurate from/reply-to and routing, non-deceptive subject, physical postal address, working opt-out honored within 10 business days | Up to $53,088 per violating email (FTC 2025 inflation-adjusted figure)      |
| EU           | GDPR + ePrivacy | Generally permissible under legitimate interest for B2B, with a documented balancing test, role relevance, and transparency. **Member states vary: Germany requires prior opt-in (UWG)** - treat German prospects like Canadian ones                                                                                                                                                                | Identity, purpose, easy objection route; honor access/erasure requests                                                              | Up to EUR 20M or 4% global turnover; German UWG penalties cited to EUR 300k |
| UK           | PECR + UK GDPR  | Unsolicited email to **corporate subscribers** (limited companies, LLPs, Scottish partnerships, public bodies) explicitly allowed. **Sole traders and non-Scottish unincorporated partnerships are individual subscribers under reg. 22** - they need prior consent or the soft opt-in, exactly like Canadian prospects. Personal/freemail addresses count as individual regardless of the employer | Clear sender identity, opt-out offered; recorded consent basis for every individual subscriber                                      | ICO enforcement                                                             |
| Canada       | CASL            | **No cold email without express or implied consent** - implied covers an existing business relationship or a conspicuously published address relevant to the recipient's role (a published "partnerships@" or media-kit contact can qualify; document why)                                                                                                                                          | Consent basis recorded per contact, identification, unsubscribe                                                                     | Up to CA$10M per violation                                                  |

Practical segmentation rule, applied per prospect and not per country:

- US and most-EU prospects → cold sequence with the must-carry items.
- UK prospects → check the legal form first. Limited company, LLP, Scottish partnership or public body → cold sequence. Sole trader, non-Scottish unincorporated partnership, or a personal/freemail address → consent basis required, same handling as Canada.
- Canada, Germany, and UK individual subscribers → outreach only where a documented consent basis exists (inbound contact, published role-relevant address, existing relationship); otherwise use passive-recruitment routes (directories, program page) instead.

The UK check is not optional book-keeping: comparison-site editors, newsletter operators, podcasters and solo consultants - this skill's core target list - are overwhelmingly sole traders, so a country-level "UK is allowed" rule misclassifies most of the list. Companies House lookup or an explicit "Ltd"/"Limited"/"LLP" in the trading name is the cheap check; when the form is unknown, treat the prospect as an individual subscriber.

## Platform channels

- **Professional-network DMs**: platform terms prohibit scraping and automation. US case law (the hiQ litigation) settled that public scraping is likely not federal computer fraud but _remains a terms-of-service breach_ - enforceable by contract claims and account bans. Never recommend automated connection/DM tooling; community-circulated "safe" volumes (~20-25 connection requests/day) are anecdote, not policy. Manual, personalized DMs at low volume.
- **Communities (forums, chat servers, subreddit-style)**: anti-solicitation rules are the norm. Participate and be findable; do not cold-pitch members in-thread or via unsolicited DMs where rules forbid it - a public callout damages the program's name among exactly the professional affiliates it wants.
- **Social DMs (other platforms)**: per-platform messaging policies apply; same manual/low-volume rule.

## List hygiene, all jurisdictions

- Filter unsubscribes, prior opt-outs, and hard bounces out _before_ the campaign starts, and propagate new opt-outs into future list-building.
- Stop on reply, opt-out, or bounce - mid-sequence sends after an opt-out are per-message violations.
- Purchased consumer lists and scraped contact dumps of unknown provenance are not a workable basis; decline them and say why.

## Disclosure - the promise never to make

Affiliate promotion legally requires disclosure of the material connection (FTC endorsement rules in the US; equivalents elsewhere). Never let outreach copy promise or imply that a prospect could promote without disclosure - it is both unlawful and, per practitioner consensus, the fastest way to lose professional affiliates' trust. Disclosure obligations _inside_ the program belong to `mbfinotti/partnerships-skills@affiliate-program-terms`; the outreach-side rule is simply: don't sell against compliance.
