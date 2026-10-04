# Contribution policy: nothing, DCO, CLA, assignment

Contents: the four rungs · what each buys · enforcement · wording for the contributing guide · institutional positions · failure patterns.

## The four rungs

Numbered by contributor burden, which is a catalogue order and not the order to adopt them in - step 4 of the skill ranks them by what each buys per unit of friction, and starts at the DCO rather than at rung 1.

**1. Inbound = outbound (nothing formal).** Contributions arrive under the project's own license, by the act of contributing - most forges' default terms encode this. Zero friction. It forecloses relicensing without per-contributor consent later.

**2. DCO - Developer Certificate of Origin 1.1.** A short public statement (Linux Foundation, 2004/2006) that the contributor certifies by adding a `Signed-off-by: Name <email>` trailer, produced by `git commit -s`. The contributor asserts they wrote the change or have the right to submit it under the project's license, and that the contribution and the record are public and kept indefinitely. No account, no form, no counterparty to negotiate with.

**3. CLA - individual (ICLA) plus corporate (CCLA).** The contributor grants the project a perpetual, worldwide, non-exclusive, royalty-free, irrevocable copyright license to their contribution - a _license_, not a transfer of ownership. A CCLA covers work an employer owns; mature programs still require an ICLA from each individual on top, and existing bodies of code arrive through a separate software grant.

**4. Copyright assignment.** Ownership transfers to the project or its steward. Maximum flexibility for the steward, maximum burden on the contributor, and the rung practitioners now advise against for new projects. Some contributors simply refuse.

## What each rung actually buys

| Need                                                           | Nothing                        | DCO                            | CLA                                | Assignment          |
| -------------------------------------------------------------- | ------------------------------ | ------------------------------ | ---------------------------------- | ------------------- |
| Right to distribute the contribution under the project license | yes                            | yes                            | yes                                | yes                 |
| Auditable provenance claim per commit                          | no                             | yes                            | yes                                | yes                 |
| Explicit patent license from contributors                      | depends on the project license | depends on the project license | yes                                | yes                 |
| Right to relicense or dual-license later                       | no                             | no                             | yes, if drafted for it             | yes                 |
| Contributor friction                                           | none                           | one commit flag                | a signature step, minutes to weeks | high, often refused |

The decision reduces to one question: **does the project need rights its own license does not already give it?** Relicensing, dual licensing and selling commercial licenses of contributed code are the real answers. If none applies, a DCO is the ceiling.

## Enforcement

- Automate the check on every incoming change. A sign-off requirement enforced by human memory is not a policy, it is folklore.
- Standard tooling exists on both sides: a bot that fails the check when a `Signed-off-by` trailer is missing, and hosted CLA managers that block the merge until an individual signs or appears on a corporate manager's approved-contributor list.
- Publish the fix, not just the failure. A first-time contributor whose PR is red for a missing trailer needs the exact recovery command in the check output: `git commit --amend -s` then a force-push, or `git rebase --signoff` for a multi-commit branch.
- Grandfather existing history when introducing a policy; never demand retroactive sign-off on merged work.

## Wording to put in the contributing guide

DCO variant:

> This project uses the Developer Certificate of Origin. Add a sign-off line to every commit with `git commit -s`, which appends `Signed-off-by: Your Name <your@email>`. By signing off you certify the statement at developercertificate.org: that you wrote the change, or that you have the right to submit it under this project's license. A missing sign-off fails CI; fix it with `git commit --amend -s` (single commit) or `git rebase --signoff <base>` (several).

CLA variant - the part most projects omit, and the one that decides whether people sign:

> Why we ask: <the specific right the project needs, e.g. "we offer a commercial license of this code to customers who cannot accept AGPL, which requires rights the AGPL alone does not give us">. Signing grants us a license to your contribution; you keep your copyright and may use your own work anywhere else. Contributing on behalf of an employer? Your employer signs a corporate agreement once and maintains the list of approved contributors.

An unexplained CLA reads as a rights grab. A CLA with a stated, checkable reason reads as a business arrangement, and most contributors accept it.

## Institutional positions to cite

- **CNCF charter**: every inbound contribution requires a DCO sign-off and arrives under Apache-2.0; a CLA is optional per project and, when adopted, follows the Apache text. Outbound code is Apache-2.0, documentation is CC-BY-4.0, and project trademarks transfer to the foundation.
- **Apache Software Foundation**: ICLA for every committer, CCLA where an employer's IP is involved, software grants for donated codebases - the reference implementation of a full CLA program.
- **Linux Foundation**: ships EasyCLA precisely because CLA administration is the part that fails; it enforces at merge time with individual, corporate and approved-list workflows.
- **Practitioner consensus** (Karl Fogel, _Producing Open Source Software_):
  - A DCO is "probably the minimum amount of CLA a free software project should adopt".
  - CLAs "probably offer the best tradeoff between safety and convenience" when the project needs those rights.
  - Assignment is not recommended for new projects.

## Failure patterns

- **CLA on a hobby project.** Drive-by contributors abandon the PR at the signature wall, and the maintainer inherits an administrative job with no benefit.
- **Corporate contributors stuck in their own legal queue.** A CCLA needs a signatory who can bind the company; budget weeks, and tell contributors up front so they start early.
- **A policy nobody can find.** It belongs in the contributing guide and in the pull-request template, not in a wiki page from three years ago.
- **Mixing rungs by accident.** Requiring a CLA _and_ a DCO doubles friction for one marginal gain; pick the rung the project's needs justify.
- **Assuming a CLA solves patents.** Check whether the project's own license already carries a patent grant (Apache-2.0, GPL-3.0, MPL-2.0 do; MIT and BSD do not) before adding an agreement for that reason alone.
