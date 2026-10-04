# Company type hiring bar

Contents: the three company archetypes and how the hiring bar differs, the dominant small-team condition, and the structural precondition behind the scope-collapse red flag.

## The three archetypes

- **Infrastructure/API-first companies** (Stripe, Twilio-style) - the API _is_ the product. Bar: highest technical depth, dedicated platform teams, staff-level roles carrying 12+ years experience and 5+ years of strategic technical leadership as a stated minimum. Stripe's own posting explicitly invites candidates "whether they've spent their entire career in infrastructure or are looking to apply their skills... for the first time."
- **Companies bolting a public API onto an existing product** - no single sourced example was directly confirmed, but the shape is implied by the prevalence of small API teams (below) and by postings that ask for "API design and development" as one line item inside an otherwise general backend-engineering role rather than as a dedicated platform team's sole mandate.
- **Enterprise platforms with large partner/ISV ecosystems** - evidenced by GitLab's dedicated, three-level Partner Integration Engineering job family reporting through a Director, Partner Solutions Architecture, with tracked KPIs (partners supported, integrations launched, integration usage, year-over-year growth) - a structurally different hiring pattern because the deliverable is partner-relationship-mediated, not a solo technical build.

## The dominant real-world condition: most API teams are small

Postman's State of the API Report found **84% of API teams operate in groups of 1-9 people**, with API-related work spread across testing (81%), development/implementation (73%), and documentation (58%) inside that small group - and no distinct, centralized "platform product manager" or "platform engineering" function called out separately from general engineering roles at most companies. Ownership of API strategy is described as distributed rather than centralized even in "API-first" organizations (82% report an API-first approach, but only 25% describe themselves as fully API-first).

**This is the single most important company-type finding for hiring**: a dedicated, specialized developer-platform hire (API PM, platform architect, and partner engineer as three separate people) is the exception, not the norm. At the modal company, one or two people on a small team absorb API design, partner integration, and often some developer-facing communication simultaneously. This is the structural precondition behind the scope-collapse hiring red flag in the skill body: it is not a hiring-process mistake so much as a real resourcing constraint a hiring manager needs to name explicitly rather than paper over with an inflated single job title.

## What differs across the three archetypes

| Dimension                      | Infra/API-first                                                                              | Bolt-on public API                                                       | Enterprise partner ecosystem                                                                       |
| ------------------------------ | -------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------- |
| Team dedicated to the platform | Yes, often multiple specialized teams                                                        | Rarely a dedicated team; folded into general backend engineering         | Yes, a named partner-engineering function with its own manager and director                        |
| What a hire is measured on     | API design quality, infra reliability, developer-facing contract stability                   | General engineering delivery, API design as one competency among several | Named partner-facing KPIs: partners supported, integrations shipped, usage growth                  |
| Portfolio bar for a candidate  | Highest - staff-level postings can expect 12+ years and prior leadership of API-design teams | Lower, folded into a general "API design and development" line item      | Relationship plus technical hybrid: open-source contribution history, partner-facing communication |

## What this means for the hiring skill

Ask which archetype the hiring company is - dedicated platform org, general engineering team adding an API line item, or a named partner-ecosystem function - before recommending a role split. Asking a bolt-on company to hire three specialized roles (API PM, platform architect, partner engineer) when their real API surface is maintained by 1-9 people is likely to overshoot both budget and real need.
