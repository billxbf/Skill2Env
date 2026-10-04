# Founding-cohort benchmarks

## Cohort sizes across 12 operators

Founding cohorts span roughly 100x depending on curation philosophy and pre-existing assets:

| Marketplace                    | Debut        | Founding cohort                                   |
| ------------------------------ | ------------ | ------------------------------------------------- |
| Notion API/integrations        | May 13, 2021 | 3 launch partners (Zapier, Typeform, Automate.io) |
| Zoom App Marketplace           | 2018/19      | 15 production-ready apps                          |
| Webflow next-gen Apps          | ~Aug 2023    | 20+ apps                                          |
| Zoom "Zapps" (in-client)       | Oct 14, 2020 | 35 launch partners                                |
| Stripe App Marketplace         | May 24, 2022 | 50+ apps                                          |
| HubSpot Connect                | 2017         | 65 integrations (30 beta + 35 certified)          |
| monday.com Apps Marketplace    | Oct 27, 2020 | operator claimed 100+; press counted 78           |
| Slack App Directory            | Dec 15, 2015 | ~150-160 apps                                     |
| Microsoft Teams app publishing | May 10, 2017 | ~150 integrations                                 |
| Salesforce AgentExchange       | Mar 4, 2025  | 200+ partners                                     |
| Salesforce AppExchange         | 2005         | 575 apps / 250 ISVs by FY-end Jan 2006            |
| Atlassian Marketplace          | May 30, 2012 | ~1,000 add-ons (50 paid)                          |

The modal curated shape is 15-65 vetted apps. The 200+ outlier (AgentExchange) reflects Salesforce's 20-year installed base of existing partners, not a template for a new marketplace.

## The vetting gate

Nearly every operator markets its cohort as security/quality vetted, and the gate is what keeps a cohort small even when developer interest is much larger:

- Slack launched with only ~150 of roughly 4,000 apps developers had built - the rest "were not vetted well enough to be counted as official integrations."
- Zoom: marketplace apps are "fully vetted by Zoom for security and user experience."
- Microsoft Teams: "rigorous validation of the functionality, usability, and security of these apps."
- Salesforce AgentExchange: components "that passed rigorous security and customer reviews."

Implication: a cohort claim is only as strong as the gate behind it. Without a live review process, the launch language cannot honestly use "curated" or "vetted"; the review process is the `samber/developer-platform-skills@app-marketplace-review` sibling's territory.

## Tiering inside a cohort

HubSpot's 2017 Connect launch is the clearest documented tiered cohort: 65 launch integrations split into 30 entry-level "beta integrators" and 35 "Connect Certified Partners" who had "gained significant customer adoption and passed a certification process." The pattern scales the headline number without diluting the top tier's trust signal.

## Marquee anchor logos

Operators consistently name big brands in the launch release:

- AgentExchange led with Google Cloud, DocuSign, and Box.
- Stripe named DocuSign, Dropbox, Intercom, Mailchimp, Ramp, and Xero.
- Slack named Twitter, Dropbox, Trello, and Google Drive.

Three to six anchors is the observed norm; the anchors carry the press story, the rest of the cohort carries the breadth claim.

## Micro-cohort selection: the design-partner criteria

For a 3-6-partner micro-cohort, select on the a16z design-partner framework (Seema Amble, Jennifer Li - "A Framework for Finding a Design Partner"):

- **Urgency:** the partner needs the integration now.
- **Capability:** they can actually ship against a young API.
- **Representativeness:** their use case generalizes to the partners you want next.

The framework advises 5-10 high-quality design partners over a large day-one cohort; Notion's 3-partner debut is the marketplace-scale example.

## Waves instead of one moment

Several operators deliberately staggered inclusion:

- monday.com shipped its Apps Framework (Jun 30, 2020) months before the Apps Marketplace itself (Oct 27, 2020).
- Webflow ran a 2022 beta App Store before the 2023 integrated "next-gen Apps" wave (Whalesync was a launch partner in both).
- Zoom sequenced App Marketplace (15 apps) → Zapps (35 partners) → Zoom Apps GA (50+).
- Stripe launched 50 "with more to come," reaching ~125 apps within about two years.

Each wave is a full coordination cycle (cohort, embargo, event anchor), which is why waves lose on efficiency - but they de-risk a review pipeline that can't vet everything by one date, and they buy multiple press moments.

## Caution: day-one numbers are not always cohorts

- Atlassian's "1,000 add-ons" (2012) came from migrating a pre-existing plugin catalog into the new storefront - not a curated launch cohort.
- Salesforce's "575 apps / 250 ISVs" is a fiscal-year-end snapshot months after AppExchange's 2005 launch, not the launch-day figure.
- monday.com claimed "over a hundred" apps at launch; independent press counted 78.

Treat any operator-published day-one number skeptically until confirmed as a genuinely gated, simultaneously revealed cohort - and expect the press to apply the same skepticism to yours. Operator launch numbers run generous, and the divergence gets reported.

## The reveal pattern (observed) and embargo mechanics (inferred)

Observed across every operator studied:

- The operator's release embeds pre-approved partner quotes (AgentExchange published DocuSign's and Box's language verbatim).
- Partners publish same-day releases pegged to the operator's news (multiple Stripe launch apps all published May 24, 2022).
- The lift anchors to a flagship keynote (AppExchange at Dreamforce 2005, Teams at Build 2017, AgentExchange at TrailblazerDX 2025, Webflow at Webflow Conf, Zoom at Zoomtopia, Slack at a dedicated press event).

Inferred from standard PR practice - no operator discloses its embargo terms:

- State the exact date/time and timezone at the top of the embargo notice.
- Coordinate wire and social timing within roughly 15 minutes across both companies.
- Give 1-2 weeks' embargo lead for complex or security-sensitive launches.
- Use only current approved boilerplate for both brands.
