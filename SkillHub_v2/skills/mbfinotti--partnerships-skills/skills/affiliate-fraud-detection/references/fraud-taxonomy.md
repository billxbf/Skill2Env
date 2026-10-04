# Affiliate Fraud Taxonomy

Patterns by funnel layer, each with the observable tell it leaves in program data. Defensive depth only: enough to recognize, never to reproduce. Vendor names appear only as sourced illustrations.

## Click layer (predominantly B2C ecommerce and mobile)

- **Cookie stuffing / forced clicks.** Tracking cookies dropped without a genuine click (hidden iframes, invisible pixels, redirects, injected scripts); the affiliate collects commission when the user later buys organically. Server-side signal capture is required: a client-side pixel cannot distinguish a stuffed cookie from an organic one.
  - Tell: commissions on customers with no meaningful referral touchpoint.
  - Tell: near-zero time between "click" and cookie set.
  - Tell: reproduction test - clean browser, visit the suspect page, check whether an affiliate cookie appears without any click.
- **Click spam and click injection (mobile).** Spam floods low-quality clicks hoping to win last-click on organic installs; injection fires a click in the instant before an install completes. Tell: click-to-install time distribution - spam shows a long flat tail, injection an implausible near-zero cluster.
- **Typosquatting / URL hijacking.** Lookalike misspelled domains redirect through affiliate links. Tell: referrers from misspelled brand domains; redirect chains through unknown intermediate domains. Chachra, Savage & Voelker (IMC 2015) found 84% of stuffed cookies in their crawl arrived via typosquatted/intermediate domains and over 91% via redirects.
- **Brand bidding and direct linking.** Ads bought on the merchant's branded search terms (or misspellings), often direct-linking to the merchant, capturing traffic the merchant would have won anyway.
  - Tell: branded-keyword CPC rising.
  - Tell: affiliate "referrals" with branded-search characteristics and abnormally high conversion.
  - Tell: screenshot sweeps of branded SERPs across geos.

## Attribution layer - where legitimate and fraudulent blur

- **Adware and browser-extension attribution hijacking.** An extension overwrites existing attribution at checkout instead of standing down when another affiliate is earlier in the clickstream. Tell: last-click flipping from a content partner to an extension seconds before purchase; extension partners' share of checkouts spiking without upstream traffic. Precedent: the PayPal Honey network removals for affiliate link hijacking and concealed stand-down violations; the parallel litigation shows courts have not settled whether last-click cookie replacement is unlawful.
- **Coupon and toolbar last-click poaching.** Sitting at the checkout moment to win last-click on demand other channels created. Legitimate for some partners, abusive for others - the central false-positive problem. A high last-click share is never itself evidence of fraud: it calls for an incrementality test and possibly a lower commission tier, not enforcement.

## Conversion and account layer

- **Fake leads / form-fill fraud** - the dominant B2B lead-gen pattern. Bots or click farms submit forms with invented, recycled, or stolen contact data on CPL/CPA programs.
  - Tell: downstream collapse weeks later - lead-to-qualified and lead-to-demo-show rates far below program norm.
  - Tell: disposable-email and role-account domains.
  - Tell: duplicate emails/phones/addresses across leads.
  - Tell: form fills under 3 seconds with no mouse movement and identical field-skip patterns.
- **Bot and data-center traffic.** GIVT under IAB/MRC: declared bots and spiders, data-center ASN resolution, non-browser user agents. Caught by routine list filtration; needs no judgment call.
- **Stolen-card transaction fraud.** The fraudster builds a legitimate-looking record, then buys through their own link with stolen cards; conversions look real and commissions fire before the cardholder disputes. Tell: chargebacks landing 60-180 days later, concentrated on one affiliate. This is why a validation window alone never covers it: only clawback, negative-balance carry-forward, and a chargeback reserve recover money already paid out.
- **Self-referral.** The affiliate converts through their own link. Tell: registration IP, device, or billing details shared between the affiliate account and the "customer".
- **Multi-account rings and collusion.** One operator running several accounts, or coordinated rings. Tell: shared device fingerprints, IPs, or payout destinations across supposedly unrelated accounts.
- **Incentivized or misrepresented traffic.** Traffic driven by incentives onto non-incentive offers, or a declared traffic source that disagrees with observed referrers. Tell: referrer audit vs the source declared at application.
- **AI-generated synthetic traffic** - the fastest-growing category. Synthetic sessions engineer realistic scroll depth, dwell time, and session lifecycle, defeating first-generation session-duration filters. Tell: behavioral metrics look normal while downstream outcomes (revenue per visitor, lead quality, retention) stay at zero. Weight server-side and downstream-outcome signals; treat recent vendor detection-efficacy claims as unverified.

## Legal footing, briefly

- Cookie stuffing is prosecutable as US federal wire fraud. The eBay cases are the only adjudicated dollar figures in the field:
  - One affiliate took roughly $28M in commissions: five months federal prison, $25,000 fine.
  - A second was sentenced to fifteen months over a scheme within ~$5.2M paid.
- Aggressive last-click attribution without a clear contract violation and technical evidence is not established fraud. Enforce the contract; do not allege crime.
- Prevalence numbers disagree by methodology: a publisher-side HTTP-log study found over a third of publishers attempted stuffing, while a user-side crawl found end users rarely encounter stuffed cookies. Both are right about different questions - distrust any single "affiliate fraud rate".
