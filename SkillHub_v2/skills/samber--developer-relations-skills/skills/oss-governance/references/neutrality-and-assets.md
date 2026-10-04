# Neutrality, trademarks and project assets

How a project earns or loses the claim that no single company controls it, and what happens when it loses it.

## Neutrality is transferred, not announced

The consistent finding across every documented case: a press release claiming open governance is worth nothing next to an irreversible transfer of control. **Code-license openness and governance openness are orthogonal** - two separate audits.

Sequence matters when moving from vendor-led to neutral: maintainers from a second organization first, then vote or seat caps, then the trademark and asset transfer. Announcing neutrality before the maintainer pool changes reads as marketing and is checked as marketing.

## The four checkable signals

Evaluated in roughly this order of weight:

1. **Who holds the trademark, domains and registry accounts.** Transfer to a neutral foundation is the strongest lever a vendor can give up - CNCF membership requires organizations to give up control of the project's trademarks. A company-held mark is the cheapest way to lose a neutrality claim.
2. **Maintainer-affiliation ratio** - how many maintainers are employed by more than one company. The metric researchers and foundations use to classify a project as single-vendor, computable from public data.
3. **Contribution agreement shape.** A CLA assigning broad rights to one company is what makes a unilateral relicense possible later; a DCO model (inbound equals outbound) does not concentrate that power. Re-opening a licence while keeping the company CLA does not restore trust - the lever is still in place.
4. **Published, versioned meeting minutes** with a real cadence, not a static page.

## Case: a trademark parked outside a neutral foundation

In 2020 Google placed Istio's trademark in its own Open Usage Commons rather than a neutral foundation, drawing public protest from IBM and Oracle and from the CNCF. The CNCF's CTO said Google had "set up an organization with no details claiming to be solving a 'trademark issue' in open source that doesn't exist given the 100+ open source foundations". IBM said it had taken Google "at good faith that our agreement to take the project to the CNCF would be honored," which "turned out to not be the case".

The dispute closed only when Google donated Istio to the CNCF in 2022 and moved the trademark to the Linux Foundation. **Read**: partners judge the destination of the asset, not the sincerity of the arrangement.

## Case: a vendor-founded foundation keeps latent control

The .NET Foundation is a trade association founded by Microsoft in 2014. In October 2021 its executive director resigned after merging a pull request to a member project using foundation permissions without consulting its active maintainers, triggering a maintainer revolt.

One maintainer's framing: "the real issue is fundamentally who owns the projects in the Foundation?" Maintainers had been assured they would be left to run themselves, and what that meant had drifted. Bylaw changes toward independence would still have needed the founding vendor's agreement.

**Read**: creating a foundation does not by itself remove the founder's authority. Only the asset transfer and the bylaw amendment rule do.

## Case: the maintainer ratio that predicted a fork

Before its 2024 licence change, only two of Redis's five maintainers worked outside the controlling company - the ratio that classified it as single-vendor. When the licence moved to non-OSI-approved terms, the Linux Foundation announced a neutral BSD-3 fork built in about eight days by engineers from six companies, with a neutral technical steering committee from day one.

When the original later re-added a copyleft option, fork contributors noted it "still lacks open governance and includes a CLA allowing future license changes". **Read**: the affiliation ratio is a leading indicator, measurable years before the event it predicted.

## What forks teach about prevention

Nearly every high-profile 2021-2024 fork followed a governance-or-licence lever pulled unilaterally by one controlling entity - a relicense, a trademark transfer to a for-profit, a redirection of purpose. Four patterns worth carrying into a design:

- **Gitea → Forgejo (2022).** The domain and trademark were transferred to a new for-profit without community consultation; contributors forked under a German registered association that structurally _cannot sell_ the mark. An entity that cannot alienate the asset is the direct antidote to name capture.
- **Nix/NixOS (2023-24).** A moderation-team resignation and a sponsorship controversy produced a constitutional assembly, an elected steering committee - and two forks anyway. **Structure without repaired trust just relocates the fight**; never sell a governance rewrite as the remedy for a live trust conflict.
- **Terraform → OpenTofu (2023-24) and Elasticsearch → OpenSearch (2021).** Both followed a relicense, both ended up foundation-hosted. Two transferable details: accused of copying code, OpenTofu answered within days with a public line-by-line provenance analysis rather than a statement, and Elastic eventually re-added an OSI-approved licence under sustained pressure, so a fork can win the argument without winning the market.

Later reporting on the Nix situation indicates continuing instability; treat post-2024 specifics here as evolving and re-verify before quoting a current state.

## Worked audit

The four signals applied as an adopter would, using the pre-fork Redis position:

| Signal                 | Finding                         | Verdict                                     |
| ---------------------- | ------------------------------- | ------------------------------------------- |
| Trademark and domains  | held by the controlling company | fails                                       |
| Maintainer affiliation | 2 of 5 outside the company      | fails - majority single-employer            |
| Contribution agreement | company CLA with broad grant    | fails - relicensing lever intact            |
| Minutes                | no public governance minutes    | fails                                       |
| Licence at the time    | OSI-approved                    | passes, and is irrelevant to the other four |

Four negative signals against one positive licence is exactly the configuration that makes a fork survivable for the forkers and expensive for the vendor. Run this table before claiming neutrality: every row is a specific, cheap fix, and the licence row fixes nothing on its own.
