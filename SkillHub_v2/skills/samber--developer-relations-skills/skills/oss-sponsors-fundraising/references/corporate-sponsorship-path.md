# The corporate sponsorship path

Everything in this file exists because individual sponsorship plateaus: a widely depended-on library's typical income through personal sponsorship sits under $1,000/month, "at least 12 times less than the alternative" of a senior engineering salary (Filippo Valsorda). Valsorda cites $355k in New York at the 90th percentile, $232k in London, $163k in Berlin.

The same argument's evidence for the status quo: `ua-parser-js`, at 6.5k stars, held $41.61 on Open Collective, and the Log4j2 maintainer had three GitHub sponsors. Company money is a different motion, not a bigger tier.

Scale check on the individual channel, from GitHub's own reporting: more than $100 million has flowed through GitHub Sponsors since 2019 to over 70,000 maintainers and organizations from more than 280,000 sponsors, and in 2022 nearly 40% of that funding came from organizations. A large channel with a small median.

## Contents

- Why companies pay
- Finding the companies that depend on you
- The two funder motions
- Outreach: weak and strong
- The one-page prospectus
- The payable checklist
- Renewal

## Why companies pay

Companies fund maintainers from budget lines that already exist, and the pitch has to name one:

- **Supply-chain security.** Companies pledging support for maintainers budget upwards of **$2,000 per employed developer per year**; the movement reports **$7.27M** raised in total, $3M+ in the trailing year, with members including Sentry, Sanity, Zerodha, Posit, AG Grid and Mux. One founder states the return directly: sponsorship pays back "in two major ways: brand marketing, and securing our supply chain."
- **Marketing reach.** Placement priced against real traffic is a media buy, and media budgets renew annually.
- **Engineering support.** Named commitments - security-report handling, review and release timelines, upgrade support - are bought as risk reduction, not charity.

What the money buys, in the words of a maintainer who invoices companies directly: "security practices, like two-factor authentication and mandatory code review; updates to keep up with the evolution of the ecosystem; reliable timelines for reviewing and merging or rejecting contributions; support and troubleshooting for filed issues and bug reports; quality standards; careful handling of security reports; adoption of standards; even a succession plan." The realistic price band he names for that package is **0.3x to 1x of a market engineering salary**.

## Finding the companies that depend on you

In rough order of signal strength:

1. **Dependency graphs and reverse-dependency listings** - who ships your package in production code.
2. **Public repositories and lockfiles** on the company's own organization.
3. **Issues and pull requests filed from company email domains or accounts** - they already have an engineer paying attention.
4. **Job posts naming the technology** - a company hiring for your library depends on it structurally.
5. **Conference talks and engineering blog posts** describing an architecture built on it.

Twenty well-qualified companies beats a mailing list. Record for each: the evidence of dependence, the likely budget line, and a named contact.

## The two funder motions

Sophisticated funders allocate in two ways at once, and the maintainer captures them differently:

- **Breadth.** Small automatic sponsorships across the whole dependency tree - one company covered "95% or greater coverage" of its fundable dependencies at $4-$10 each, noting "for many of our dependencies, we are likely their first and sole sponsor". Captured with **zero outreach**: a `FUNDING.yml`, package funding metadata, and a live funding link.
- **Depth.** Judgement-based amounts to projects the company depends on heavily - examples from the same $500,000 programme: $15,000 to the library underpinning one of its products, $10,000 and $6,000 to two language foundations, $1,750 to a framework. Captured by being **visibly load-bearing for that company's product**, which is what the outreach below argues.

Two further mechanisms sit alongside them, and neither is won by pitching a sponsorship page:

- **Employee-nominated funds.** A fixed monthly budget awarded to one project per cycle by internal nomination and vote (Indeed's is $10,000/month). Captured by the engineer inside the company who already uses the project - see [funder-scan-and-eligibility.md](./funder-scan-and-eligibility.md) for the four eligibility rules a candidate must satisfy.
- **Pledge and foundation membership.** Open Source Pledge members commit more than $2,000 per employed developer per year to maintainers and foundations; the movement reports $7.27M raised in total. Captured indirectly, by being a recipient of the foundation or platform that money flows through.

## Outreach: weak and strong

**Weak - do not send:**

> Subject: Sponsorship request
>
> Hi, I maintain libfoo, an open-source project used by thousands of developers. Maintaining it takes a lot of unpaid time and I'm asking companies that use it to support my work on GitHub Sponsors. Any amount helps! Here's the link.

It asks for charity, addresses nobody in particular, names no dependence, and offers nothing a budget owner can justify.

**Strong:**

> Subject: libfoo maintenance - support tier for <Company>
>
> Hi <Name>, I maintain libfoo. Your `api-gateway` and `billing` services depend on it (visible in your public repos), and three of your engineers have filed issues this year, so this is likely load-bearing for you.
>
> I currently maintain it in evenings. I'm setting up a small number of company support tiers so the projects that companies actually run in production get a defined level of service: security reports acknowledged within 48 hours, a published release cadence, and named support for major-version upgrades. $1,000/month, invoiced annually, logo in the README and docs.
>
> If maintenance risk on this dependency is worth removing, I can send a one-page summary and an invoice this week. If sponsorship is the wrong budget for it, is security or platform engineering the better door?

Why it works:

- Names the dependence with evidence.
- Names the risk.
- Names the service.
- Names the price.
- Offers a route when the first budget line is wrong.

## The one-page prospectus

One page, no slide deck:

1. **What the project is** and who depends on it - with two or three named or categorised adopters.
2. **Usage evidence** - downloads, dependent repositories, notable deployments.
3. **Who maintains it** and how much time it currently gets.
4. **What sponsorship funds** - bounded commitments with numbers, not "more development".
5. **Tiers and prices**, with what each placement is worth in traffic.
6. **How to pay** - entity, invoicing, tax form, currency, minimum.
7. **What sponsorship does not buy** - roadmap influence, merged pull requests, exclusivity.

Section 7 raises the price rather than lowering it: a maintainer who will not sell neutrality is a safer dependency.

## The payable checklist

Companies pay recipients that fit their existing process. Before the first outreach, be able to answer yes to all of these:

- A legal entity or an explicit personal-contractor arrangement, in a country the company can pay.
- The tax form the payer's jurisdiction expects.
- The ability to issue a numbered invoice with payment terms.
- Bank details for transfer, not only a card-based donation page.
- A named beneficiary and a stable contact address.
- A fiscal host, where the project is multi-maintainer or the money should not land on one person's tax return.
- Awareness of the platform floor: invoiced sponsorships through the main platform start at **$5,000 per invoice**, so anything smaller must route through a fiscal host.

The maintainers who get paid are not the most deserving; they are the ones a finance department can process without an exception.

## Renewal

Corporate budgets are annual, so the renewal is decided months before it lapses.

- Send a short proof-of-value note each quarter: what shipped, what was triaged, what the sponsorship covered.
- Log the customer's budget month and open the renewal conversation a full cycle ahead.
- Watch concentration: when one sponsor exceeds half the program's income, the project is a contractor with a single client. Grow the next tier down before the exposure matters.
