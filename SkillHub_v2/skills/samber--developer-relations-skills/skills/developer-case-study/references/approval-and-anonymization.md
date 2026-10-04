# Approval and anonymization

Approval decides which version of the story is writable, so open it before drafting. A study built on numbers the adopter will not clear has to be rewritten from scratch.

## Read the contract first

Standard SaaS terms often already grant the vendor a licence to use the customer's name and logo and to say publicly that they are a customer. Vercel's terms carry the clause at §16.4 ("Customer Name"), granting a non-exclusive, royalty-free licence to reproduce the customer's trademarks and logos in marketing materials and to indicate that they are a customer, subject to the customer's own trademark-usage guidelines.

That clause settles the logo wall. It settles nothing else.

None of the following is a trademark use:

- A quote.
- A metric.
- An architecture description.
- An account of how the customer's systems failed before.

Publishing any of them on the strength of a logo clause is how a reference relationship ends. Check the clause, then run the chain below for everything it does not cover.

Two practical consequences:

- The logo-wall question is usually already answered before you ask.
- A customer who says "we never approve case studies" may still be contractually fine with the logo, which keeps a lighter artefact available when the full story is refused.

## The consent chain

Four permissions, often four different holders. Ask at first contact who holds each and how long each takes. The delays below are working estimates, not measured norms - the structure itself matches how a real developer-focused company runs this in public: PostHog's own marketing handbook has the customer tagged for a fact check first, with legal and PR "sometimes" looped in after, not before (`posthog.com/handbook/marketing/customer-case-studies`).

| Permission                            | Usual holder                                | Typical delay |
| ------------------------------------- | ------------------------------------------- | ------------- |
| Being quoted and named, with title    | The interviewed engineer                    | Immediate     |
| Spending the team's credibility on it | Their manager                               | Days          |
| Company name, logo, published wording | Communications or marketing                 | Days to weeks |
| Technical detail and metrics          | Security, or legal for regulated industries | Weeks         |

Enterprise adopters run the full chain. A startup collapses it to one or two people. An individual developer or OSS maintainer _is_ the chain - a message is enough, but ask explicitly whether their employer may be mentioned.

Get naming and logo permission in writing from someone who can actually grant it. A chat approval from the engineer does not bind their company.

What stalls a chain, independent of company size, is a vague ask. B2B case-study consultant Joel Klettke describes legal and PR reviewers needing something concrete to say yes or no to - "this is what they want to talk about, are we comfortable with this or with these metrics?" - rather than an open-ended request they have no way to bound. A story with no one accountable for moving it forward gets deprioritized rather than revisited, so naming an owner and a date matters more than the size of the ask (The Campaign podcast, 97th Floor, Feb 21, 2025).

## What review predictably strikes

Pre-redact these so the draft survives the first pass:

- Absolute infrastructure sizes and costs: node counts, cluster sizes, monthly spend, capacity headroom.
- Internal service names, codenames, ticket IDs, repository paths, dashboard URLs.
- Named competitors in the rejected-alternatives section.
- Incident specifics tied to a dated outage the company never publicly disclosed.
- Anything implying a security weakness in the before-state - the single most common deletion.
- Customer-of-the-customer names and any end-user data.

Substitutions that usually survive:

- Ratios instead of absolutes ("cut infrastructure cost by about a third").
- Failure described by mechanism instead of by incident ("retry storms could double-charge").
- Role descriptions instead of team names.

## Anonymization ladder

When naming is refused, descend one rung at a time rather than dropping the story.

1. Named company, named engineer with title. Full credibility.
2. Named company, unnamed engineer ("a staff engineer on the payments team"). Small loss.
3. Unnamed company with an identifying descriptor ("a top-five European mobility platform"), metrics intact. Noticeable loss; the numbers now carry the whole study.
4. Category descriptor only ("a fintech of roughly 200 engineers"), metrics intact. The floor for anything still called a case study.
5. Composite or pattern write-up, no single customer, no attributed quote. Not a case study - publish it as an engineering-pattern post and label it as one.

Never sharpen a descriptor until the company is identifiable while still claiming anonymity. That breaks the agreement in substance even if the name never appears, and it is the kind of failure that ends a reference relationship.

## Review mechanics

Send the full draft, never fragments - reviewers reading isolated quotes strike them for lack of context. Mark exactly what needs a decision:

- Each quote.
- Each metric.
- The architecture description.
- The company name.
- The logo.
- The limitations section.

Give a dated deadline and state the default: "if we do not hear back by the 14th, we publish the anonymised version without the cost figures." A deadline with no default is a deadline that slips.

Let the adopter edit their own quotes freely. Push back once when an edit turns a quote into vendor copy, with the original alongside, then accept their decision.

## Request template

Adapt tone to the relationship; keep the structure.

```
Subject: Case study draft for review  -  decisions needed by <date>

Hi <name>,

Attached is the full draft of the case study from our conversation on <date>.
Nothing is published until you approve it.

Please confirm or correct:
1. Company name and logo usage  -  currently: <named / anonymised as "...">.
2. Quotes  -  three, highlighted in yellow, transcribed verbatim. Edit freely.
3. Metrics  -  four figures, highlighted in blue. Each lists the dashboard and
   window we attributed it to. Strike anything your team cannot vouch for.
4. Architecture section  -  please check technical accuracy; we drew it from
   your diagram plus the call.
5. Limitations section  -  the migration effort and the parts you left on cron.
   We keep this in because engineers trust a story that names its costs, but
   it is yours to cut.

Who else needs to sign off on your side (security, legal, comms)? Happy to
send it to them directly.

If we have not heard back by <date>, we will hold publication and follow up
rather than publish anything unapproved.

<name>
```

## After approval

Keep three artefacts together:

- The written permission.
- The final approved text.
- The metric provenance sheet.

Any later dispute is settled from these.

Republishing in another format commonly needs its own permission, for example:

- Sales one-pager.
- Conference slide.
- Paid ad.
- Homepage logo wall.

Ask for the ones you know you want while the reviewer is already engaged.

Stories go stale. Re-verify anything older than roughly 18 months before reusing it - a self-set convention rather than a measured shelf life, and too long for an adopter in a fast-moving stack. By then:

- The adopter may have migrated away.
- The numbers may have moved.
- The quoted engineer may have left.

Publishing a study for a customer who churned is a reputational cost far larger than the study's value.
