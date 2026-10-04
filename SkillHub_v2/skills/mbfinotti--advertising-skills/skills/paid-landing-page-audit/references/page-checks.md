# Heuristic Page Checks

Run in this order: it is sequenced by revenue impact for paid traffic, not by ease of checking. Message match caps everything downstream of it, so it goes first. Measurement sanity goes last, even though it is the easiest to verify.

Every result here is an **opinion** until this page's own data upgrades it.

Say the ordering out loud rather than leaving it implied by the letters: the section order A > B > C > … > J is a value ordering, revenue at stake for paid traffic.

The effort ordering disagrees, and following it is the classic mistake: J measurement == H policy == A message match cost minutes (one page load carrying the real ad's parameters), while F speed and G accessibility need rendered field data and tooling. Run in value order anyway: what a check costs to run says nothing about what the leak costs.

One exception: anything found in H (cloaking, prohibited claims, an undisclosed endorsement, a missing consent banner) reports at the top of the fix list regardless of its rank here, because disapproval takes the whole campaign rather than one funnel step.

Capability gate for the whole file: if you can fetch and render the page, verify each check against the rendered result at a phone-sized viewport (~390px wide) and a desktop viewport, with the real ad's URL parameters attached. Otherwise work from pasted copy or screenshots, and move every check that needs rendering (load, layout shift, dynamic content, redirects) into "Could not check".

## A. Message match (ad → page)

The single highest-leverage check for paid traffic, partly enforced by the platforms themselves: landing page experience is a Google Quality Score component, and Meta reviews the ad and its destination together. Four match axes - check all four, not just the first:

- **Verbal.** Does the page headline confirm the ad's specific promise, ideally in the ad's own words? A specific keyword or claim landing on a generic homepage-style H1 resets the visitor's information scent to zero. Ad says "download the template", page asks for a demo - that is a broken promise, not a nuance.
- **Visual.** Does the hero echo the ad's creative - its thumbnail, its opening video frame, its colour world, the product or person shown? Clickers recognise pages by sight faster than by reading; a page that looks unrelated to the ad reads as a wrong turn. Nearly every audit checks words only - check the pixels too.
- **Offer.** Same offer, same price, same discount, same CTA verb as the ad. A price or offer that shifts between click and page is both a conversion killer and a platform-policy risk (bait-and-switch).
- **Geo and language.** For every geo the campaign targets: right language, right currency, offer valid in that region, region-appropriate compliance text. One non-localised page behind a multi-geo campaign fails this silently.

**Dynamic personalisation check.** If the page swaps headlines or blocks by UTM, keyword insertion, or ad set: load it with the real parameters from a real ad and confirm the personalised variant actually renders. The common failure is silent - the generic fallback serves and nobody notices, because the page "works". Also confirm click IDs (the ad platform's click identifier parameter) survive the landing and every redirect. If they are stripped, the platform cannot attribute or optimise.

## B. Above the fold, on the device the spend lands on

Check the first screen mobile-first when paid social or mobile-heavy search carries the spend. Attention research says why this screen dominates: visual first impressions form in about 50ms (Lindgaard 2006), and about 57% of viewing time lands above the fold (NN/g 2018) - people do scroll, but only if this screen gives them a reason.

- One clear promise, one primary CTA. Count the competing calls to action; more than one primary action is a leak. A lower-commitment secondary link (e.g. "watch a demo") is fine _below_ the primary, not beside it as an equal.
- The five-second test: can a stranger say what this is, who it is for, and what to do next after five seconds on the first screen alone?
- Primary CTA visible in the first phone viewport - not pushed below a hero image or video.
- Headline states the outcome in plain language at a low reading grade; front-load the information-carrying words (the F-pattern scanning evidence is the reason to front-load, not a layout to imitate).
- Hero paints before the Core Web Vitals LCP "good" threshold (2.5s at the 75th percentile); a heavy hero video is a common silent offender on paid social.
- Mobile-specific stability: heroes sized with viewport units can jump when the mobile browser chrome collapses - check for layout jump on scroll, and check CLS (good ≤ 0.1).

## C. Offer and value-proposition clarity

- Prefix the headline and each benefit line with "Now you can…" - if the sentence is compelling and true, it holds; if it turns vague or obvious, the line is feature-speak and needs rewriting.
- Is the price visible, or deliberately withheld? Hiding price is only defensible for genuinely high-ticket, call-booked offers - and even then the page should say what determines it.
- Risk reversal present and findable: guarantee, free trial, "cancel anytime", returns - whichever fits the offer.
- Does the page answer the visitor's stage? Cold paid-social traffic needs the problem named before the product; high-intent search traffic wants the offer confirmed immediately. Same page rarely serves both well.

## D. Form and checkout friction

- Count the fields. Every field costs conversion and the cost is non-linear - state the direction, never a percentage - published figures disagree. For each field ask: needed _now_, or collectible after the conversion?
- **B2B exception, stated explicitly:** when lead quality, not lead volume, is the bottleneck, adding a qualifying field is a legitimate recommendation - judged against pipeline, not fill rate.
- Inline validation as the user types, not an error dump on submit; error messages name the field and the fix in plain words.
- Labels stay visible (placeholder-only labels vanish on focus); one column; the submit button says what happens next, not "Submit".
- Mobile: correct keyboard type per field (numeric for phone, email keyboard for email), input font size at or above 16px (below that, iOS zooms on focus and breaks the layout), tap targets comfortably sized - WCAG 2.2 AA floor is 24×24 CSS px, practitioner guidance and WCAG AAA sit at 44×44.
- B2C checkout specifically: costs revealed early (extra costs revealed late are the top stated abandonment reason in Baymard's survey data), guest checkout offered, payment methods and wallets visible before commitment, no forced account creation before purchase.

## E. Trust and objection handling

- Place proof at the point of friction, not in a footer or FAQ: the counter to an objection belongs where the objection arises. For each objection family the page provokes, find the counter on the page and note _where_ it sits relative to where the doubt occurs.

  Five recurring objection families:
  - Trust: "who are you?"
  - Price: "worth it?"
  - Fit: "for someone like me?"
  - Timing: "why now?"
  - Effort: "how hard is this?"

- Testimonials must be attributable - real name, role, specific result. Anonymous filler reads as fake and costs more than it earns. Fabricated testimonials and reviews are illegal under the FTC's fake-review rule, not just bad practice.
- Urgency and scarcity only when genuine. A countdown that resets, invented stock limits, or fake "X people viewing" widgets are findings _against_ the page - flag them, never recommend them.
- Security cues near the payment or personal-data moment for B2C; recognisable customer logos and concrete numbers for B2B.

## F. Speed and stability

- Judge against Core Web Vitals "good" thresholds, field data at the 75th percentile: LCP ≤ 2.5s, INP ≤ 200ms, CLS ≤ 0.1. Lab estimates are opinions; field data is observation.
- If the page passes all three, say so in "Not a problem" and move on - speed work on a passing page steals priority from message and offer work.
- Paid framing: a slow page does not just lose the visitor, it wastes the already-paid click and corrupts the conversion data automated bidding learns from.

## G. Accessibility as a conversion check

Accessibility failures are friction for everyone and legal risk besides. Treat them as conversion findings, not a separate compliance annex.

- Contrast: 4.5:1 for normal text, 3:1 for large text (WCAG 2.2 AA) - check the actual CTA button, whose colour is usually chosen for brand, not legibility.
- Every form input has a visible label; keyboard focus is visible; the CTA is reachable and operable by keyboard.
- Paid-specific crossover: a video ad driving to a page whose hero video autoplays without captions loses exactly the audience the ad format attracted; alt text on the proof images that carry the argument.

## H. Ad-platform policy risk

A page that violates the ad platform's destination policies can get ads disapproved or the whole domain flagged - an audit finding category most audits omit entirely.

- Destination basics: page loads, is crawlable, matches the ad's display URL domain, no cloaking or sneaky redirects.
- Claims discipline: no promises the ad platform's policies prohibit (unrealistic results, before/after framings where restricted, implied knowledge of the visitor's personal attributes), no hidden fees or bait-and-switch between ad and page.
- Transparency: identifiable business, reachable contact details, privacy policy present; consent banner implemented where required - and note that consent choices change what the analytics in this audit can even see.
- Restricted verticals (finance, health, employment, housing, credit, and similar) face stricter rules on both the ad and the page - flag elevated risk rather than adjudicating the vertical's law.
- Endorsements and testimonials on the page follow disclosure rules: material connections disclosed where the claim appears, not behind a link.

## I. The path after the conversion

- Does the button lead to a next step - confirmation with expectations set (what arrives, when, from whom), an onboarding action, a relevant offer - or a dead-end "thanks"? A dead end is unfinished revenue and, when expectations go unset, tomorrow's refund.
- B2B: does the thank-you state what happens next and when a human follows up? Speed-to-follow-up is a pipeline lever the page sets expectations for.

## J. Measurement sanity

Last, because it is not a conversion leak itself - but an unmeasured page cannot be optimised, and bad measurement quietly falsified every number used above.

- The conversion event fires once per conversion, on the real completion, not on button click.
- Click IDs persist from landing through to the conversion record.
- Anything deeper - deduplication, server-side setup, consent-mode effects on counts - hands off to `mbfinotti/advertising-skills@ad-conversion-tracking`; discrepancy quantification to `mbfinotti/advertising-skills@ad-attribution-gap`.
