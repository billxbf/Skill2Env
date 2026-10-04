# Pre-launch timeline

Everything that has to happen before launch day, in the order the lead times force. The stages are sized by how long each one takes to undo, not by how much work it is: a rename is the most expensive mistake on this page, so it goes first.

## 8+ weeks out: Name and license

### Trademark clearance

Search for phonetic, visual and conceptual similarity - not just identical matches - across every jurisdiction the project will be used in. Then secure the domain, the code-host organization and the social handles before the name appears anywhere public. The principle behind that order is "secure first, release later": once a name is visible, changing it costs the URL, the accumulated search history and the announcement itself.

Two facts make this non-optional for open source specifically:

- Free distribution is still use in commerce. Distributing software over the internet at no charge can create or infringe trademark rights (_Planetary Motion v. Techsplosion_, 261 F.3d 1188). "Nobody paid us" is not a defense; that is why projects receive cease-and-desist letters and rename after they are already popular.
- Visibility accelerates the problem rather than protecting you. The OpenClaw/"Clawdbot" episode is the recent cautionary case: rapid repository visibility, then legal pressure, then a forced rename.

Any colorable conflict is a rename before launch. It is never a risk to accept and fix afterwards.

### License, CLA/DCO, foundation path

Settle these in the same pass, because each one is harder to change after adoption than before it:

- The license itself. Relicensing an established project reliably triggers a fork: HashiCorp's move from MPL 2.0 to BSL 1.1 in August 2023 produced the OpenTF manifesto, endorsed by over 140 companies and 700+ individuals, and OpenTofu launched under the Linux Foundation a month later.
- CLA versus DCO. DCO sign-off is the CNCF default; CLAs are project-elected. Decide before the first external pull request arrives, not after.
- Trademark ownership, if a foundation is on the roadmap. CNCF requires that a project's trademark and logo assets transfer to the Linux Foundation - a stronger requirement than the license. The reason, as Linkerd's creator put it during the Synadia/NATS dispute: a permissive license lets anyone ship a relicensed fork, but trademark ownership means the one thing they cannot do is call it by the original name.

Use `samber/developer-relations-skills@oss-license-strategy` for the license decision itself; this page only fixes when it has to be done.

## 3 weeks out: Press

Only relevant if press coverage is part of the goal. Supabase's own figure is the anchor: press "needs to be organized up to 3 weeks before you plan to Launch". General PR guidance is more permissive for smaller launches (24–48 hours for a standard announcement, one to two weeks for a large enterprise one) - treat that split as practitioner convention, not a rule.

Outlets that actually cover open-source launches:

- TechCrunch
- The New Stack
- The Register
- TechTarget
- SDxCentral
- The relevant category trades
- The Linux Foundation/CNCF newsroom, for foundation-backed news

Embargo, exclusive and briefing mechanics (including the fact that a public repository leaks its own news through tags, registry publishes and merged pull requests) belong to `samber/developer-relations-skills@tech-press-relations`. Do not reinvent them here.

## 1–2 weeks out: War room and readiness

### Stand up the war room

Generalized from GitLab's public Developer Advocacy handbook, the only complete launch-day playbook published openly:

| Element               | What it means concretely                                                                                                                                            |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| DRI per channel       | One named person owns each of: the anchor thread, each secondary community, social, chat, and incoming issues. "The team is watching" is not an owner.              |
| Response cadence      | A stated interval, not "as needed". GitLab reviews its mention channel 1–2 times daily in steady state; a launch day needs continuous coverage for the first hours. |
| Escalation path       | When the responder cannot answer, they pull in the engineer who can, by name, in the thread. Agree who those people are and that they are reachable.                |
| Speaking authority    | Who may commit to a roadmap item, a date, or a licensing statement in public. Everyone else defers.                                                                 |
| Shared tracking       | One place where handled items get marked handled, so two people do not answer the same comment differently.                                                         |
| Pre-drafted templates | Answers to the three or four objections you already know are coming, written before launch day rather than under load.                                              |

Note the editing constraint that shapes response discipline on Hacker News: the window to edit a comment closes after two hours. Read before posting.

### Security contact

Publish `SECURITY.md` with a private reporting channel and confirm someone is actually watching it. Coordinated disclosure only works if the path exists before the first report - a vulnerability surfacing in a public launch thread has to move private immediately, and it cannot if there is nowhere to move it to.

The runbook once a report is valid:

1. Open a private advisory.
2. Add the reporter as a collaborator.
3. Develop and test the patch on a private branch.
4. Request a CVE through a numbering authority.
5. Credit the reporter on publication.

### Freeze

Freeze the default branch and production changes for launch day. A mid-launch refactor breaks the thing strangers are cloning right now.

## Launch day and after

The hour-by-hour run of show lives in the launch-day runbook; this page stops at the freeze.

Decide the shape before you get here. A single project with one story wants a Show HN anchor and, optionally, Product Hunt as a secondary. A company-backed project with at least three announceable items and a conference on the calendar can carry a multi-day caravan instead.

Supabase's Launch Week and Cloudflare's Innovation Weeks are the two documented models. Cloudflare's origin explains why the format exists at all: rather than one annual conference, it deconstructed the user conference "down to one of its most critical elements, which is, we'll make a bunch of product announcements around… a particular theme", and found the published schedule itself acted as a forcing function on the teams.

## Common sequencing mistakes

- Running trademark clearance after the repository is public, because the name "felt available".
- Treating the license as a launch-week decision. It is an 8-week decision; the announcement has to explain it, and any company-backed project has to state the commercial boundary in the post itself.
- Booking press before the readiness gate passes, which turns a slipped blocker into a broken embargo.
- Writing `SECURITY.md` in response to the first report rather than before the first reader.
- Assigning channels to a team rather than to named people, then discovering at T+2h that everyone assumed someone else had Reddit.
