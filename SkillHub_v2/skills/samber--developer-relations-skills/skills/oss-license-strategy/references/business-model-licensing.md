# Licensing as a business-model lever, and how to change a license

Contents: the three monetizable structures · source-available instruments · Fair Source and DOSP · documented outcomes · relicensing playbook · announcement template.

## The three structures a license can support

**Dual licensing.** The same code under a copyleft license and, for a fee, under a commercial license without those obligations. It only works when the copyleft obligations are genuinely inconvenient - AGPL for server software, LGPL/GPL for a client library where source-disclosure or relink duties collide with the customer's product. The vendor must hold or be granted all the rights, which is why dual-licensing vendors run CLAs (see `contribution-policy.md`).

**Open core.** Permissive or copyleft core plus proprietary add-ons, usually the ones enterprises need: SSO, audit logs, multi-tenancy, support SLAs. The license question becomes where the line sits. Draw it once, publish it, and never move a shipped feature across it toward the proprietary side - that move, not the model, is what burns trust.

**Source-available restriction.** Publish the code, forbid the specific competing use, optionally convert to an open license later. Covered below.

Hosting the software yourself is the fourth model and needs no licensing lever at all: it monetizes operations, not terms. Recommend it before recommending a restriction, because it costs no contributors.

## Source-available instruments

None of these is an OSI-approved open source license: the Open Source Definition forbids restricting a field of endeavour, which is exactly what a non-compete clause does.

- **BUSL 1.1** - three parameters the adopter sets:
  - **Change Date**: at most four years after first publication.
  - **Change License**: must be GPL-2.0-or-later or compatible.
  - **Additional Use Grant** (optional): the production use allowed for free.

  Production use outside the grant needs a commercial license until the Change Date.

- **FSL (Functional Source License)** - BUSL with the parameters frozen: two years, converting to MIT or Apache-2.0, no per-adopter use grant. Created by Sentry, framed as "you can do anything with FSL software except economically undermine its producer". Easier for an adopter's legal team because every FSL project reads the same.
- **Elastic License 2.0** - plain source-available terms: no offering the product as a hosted service, no circumventing license keys, no removing notices. No conversion date.
- **SSPL** - copyleft extended to the whole service stack: offering the software as a service obliges publishing the service's management and orchestration source. The OSI board rejected it publicly in January 2021 as a "fauxpen source" license, one whose adopters "claim that their product continues to remain 'open' under the new license, but the new license actually has taken away user rights". This breaches clause 6 of the Open Source Definition by restricting deployment as a cloud service.
- **PolyForm family** (Noncommercial, Small Business, Shield, Perimeter, Free Trial) - short, plain-language licenses when one targeted restriction is really what is wanted, without the parameter machinery.

**Fair Source** (fair.io, 2024) is a definition rather than a license: code publicly readable, usable and modifiable with minimal restrictions protecting the producer's business model, and subject to **Delayed Open Source Publication** - a planned future release under an OSI-approved license. FSL and BUSL satisfy it.

Vocabulary discipline: "source-available", "fair source", "delayed open source". Never "open source". The claim is checkable in seconds and the correction arrives publicly.

## What the documented changes actually produced

| Project       | Change                                                                            | Outcome                                                                                                                                                                                                                                                   |
| ------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Elasticsearch | Apache-2.0 → SSPL + Elastic License 2.0 (2021)                                    | AWS forked OpenSearch. In 2024 Elastic added AGPL-3.0 as a third option, framed as "adding another option, and not removing anything".                                                                                                                    |
| Redis         | BSD → RSALv2 + SSPLv1 (March 2024)                                                | AWS and Google backed the Valkey fork. Redis added AGPLv3 in Redis 8 (May 2025); its CEO wrote that the change achieved the goal against cloud providers but "hurt our relationship with the Redis community", and acknowledged SSPL is not OSI-approved. |
| HashiCorp     | MPL-2.0 → BUSL-1.1 (August 2023), future releases only, SDKs and APIs left on MPL | The OpenTF manifesto gathered over 140 companies and over 700 individuals within weeks; the Linux Foundation launched the OpenTofu fork on 20 September 2023. A 2024 cease-and-desist alleging copied code was publicly rebutted and went no further.     |

Three transferable lessons:

- The fork is the predictable response rather than the worst case.
- The community cost outlasts the licensing win.
- The escape hatches everyone uses in practice are the old releases and the permissive SDKs left untouched.

## Relicensing playbook

1. **Establish who must consent.** Every copyright holder whose code is still present, unless a contributor agreement already granted the right to relicense. Mozilla's Firefox relicensing ran 2001-2006 - plan in months, not weeks.
2. **Map the unreachable contributions.** For each: rewrite, remove, or accept that the change cannot cover that code.
3. **Fix the version boundary.** The change binds future releases only; published releases stay under their old terms permanently and can always be forked.
4. **Decide what stays.** SDKs, clients, APIs, examples and documentation are usually best left permissive - they are what keeps the ecosystem intact and the announcement survivable.
5. **Prepare for the fork.** Name who would plausibly lead it, what they would need, and what your response is. A vendor surprised by a fork looks unprepared for the consequence it chose.
6. **Write the announcement before finalizing the decision.** If it cannot be written honestly, the decision is not ready.

Direction matters: moving _toward_ restriction (permissive → copyleft, open → source-available) provokes forks; moving _away_ from it (source-available → OSI-approved) is received well, which is why two of the three cases above eventually did it.

## Announcement template

```markdown
# <Project> licensing change

What changes old license → new license, effective from version X / date Y
What does not change releases up to X, SDKs/clients, docs, the trademark policy
Who this affects the specific use now requiring a commercial license, with an example
Who this does not the uses explicitly still allowed, with examples
Why the concrete commercial situation, named - not "sustainability"
Contributors what happens to existing contributions, what is asked going forward
Alternatives the fork is available; here is the last commit under the old license
```

State the competitor situation plainly. Vague community-protection framing is read as evasion and gets picked apart in public within hours.
