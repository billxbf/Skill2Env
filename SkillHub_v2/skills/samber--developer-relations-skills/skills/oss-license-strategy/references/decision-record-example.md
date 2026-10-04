# Worked decision record, weak version beside strong

Contents: the scenario · the weak record · the strong record · what separates them · artifact checklist.

## Scenario

A four-person company maintains a Go workflow engine. It ships as a library plus a self-hostable server, has 30 outside contributors, MIT today, and is planning a hosted commercial offering next year. Dependencies are all MIT/Apache-2.0 except one BSD-3-Clause parser.

## Weak version - what a rushed session produces

```markdown
# Licensing decision - workflow engine

## Outbound license AGPL-3.0, to protect us from cloud providers reselling our work.

## Contribution policy CLA, for legal safety.

## Notes We'll switch the license before the hosted launch. MIT was too permissive

                         and we want to keep our competitive advantage.
```

Why it fails, line by line:

- No constraint section, so nobody checked whether the dependencies or the contributors' employers allow the change. The 30 existing contributors are not mentioned at all - and every one of them must consent, since MIT plus no CLA means no pre-granted relicensing right.
- "Protect us from cloud providers" is asserted, not argued:
  - No named competitor.
  - No statement of what AGPL obliges them to do.
  - No acknowledgement that some enterprises ban AGPL in writing - Google's published policy is the checkable example - which may include accounts this project sells to.
- "CLA, for legal safety" hides the real reason (future dual licensing) behind a phrase that reads to contributors as a rights grab.
- "Switch the license before launch" ignores that every published release stays MIT forever - the library is already forkable from the last MIT commit.
- No artifacts, no revisit trigger, no eliminated options. Next quarter the same debate restarts from zero.

## Strong version

```markdown
# Licensing decision - workflow engine

## Artifact & trigger

Two artifacts in one repository. The Go library is imported into users' binaries - the
obligation trigger is distribution. The server is self-hosted and reachable over a network -
the trigger for a network-copyleft license would be interaction, not distribution.

## Constraints

- Shipped dependencies: 41 modules, all MIT or Apache-2.0 except one BSD-3-Clause parser.
  No copyleft inbound; no forced outbound license. Verified from go.mod plus the vendor tree.
- Two contributors work for employers with open-source policies restricting copyleft
  contributions; both confirmed they can keep contributing under a permissive library license.
- 30 outside contributors hold copyright on code still present. No CLA was ever in place, so
  any license change on existing code needs their individual consent.
- Eliminated: GPL-3.0 for the library (kills adoption in the closed-source integrations that
  are 60% of current usage). Eliminated: SSPL and BUSL for either artifact (not OSI-approved;
  our top three target accounts filter procurement on OSI approval).

## Posture

Commercial optionality on the server, maximum adoption on the library. Split the repository's
licensing rather than picking one compromise license for both.

## Outbound license

- Library: stays MIT. No change, so no consent problem, and integrations keep working.
- Server: AGPL-3.0 for new releases from v3.0. It beat Elastic License 2.0 because AGPL is
  OSI-approved and survives procurement filters; it beat staying MIT because a hosted
  competitor could otherwise resell the server with no reciprocity.
- Excluded by this choice: enterprises whose policy bans AGPL outright. Accepted, because the
  commercial license is exactly the path we want them on.

## Contribution policy

DCO on the library (provenance, near-zero friction). CLA on the server, introduced with v3.0,
with the reason published: we sell a commercial license of the server, which needs rights AGPL
alone does not grant us. Existing history is grandfathered; the CLA applies to new server
contributions only.

## Business model

B2B. The lever is dual licensing on the server: AGPL for everyone, commercial license for
companies that cannot publish their own service source. The competitor addressed is a managed
"workflow engine as a service" offering - named in the internal version of this record. The
library is deliberately outside the lever; it is the distribution channel.

## Artifacts

- LICENSE (MIT, unchanged) at root; server/LICENSE (AGPL-3.0) plus a root LICENSING.md
  explaining the boundary, since a root LICENSE would otherwise claim the whole tree.
- SPDX-License-Identifier headers per file, matching each directory's license.
- Collective notice "Copyright The Workflow Engine Authors" replacing three stale personal
  notices.
- CONTRIBUTING.md: DCO instructions with the amend/rebase recovery commands, CLA section with
  the stated reason, both enforced by a check on every pull request.
- Registry metadata license field updated for the library; container image label for the server.

## Revisit

Reopen if: we join a foundation (their rules override this), a fork of the server gains real
traction, the commercial license produces no revenue within four quarters, or a dependency
adopts copyleft.
```

## What separates the two

- Constraints first.
- Options eliminated in writing.
- Each choice paired with who it excludes.
- One artifact per licensing boundary.
- A stated reason wherever contributors are asked for something.
- A trigger for revisiting.

The strong record is longer only where the extra lines stop a future argument.

## Artifact checklist for any record

- LICENSE files at every licensing boundary, unmodified text, detectable by an automated detector.
- SPDX headers and a collective copyright notice.
- Registry/package metadata and image labels updated.
- NOTICE file if the license requires attribution propagation; third-party notices preserved.
- Contributing guide updated with the policy and its recovery commands.
- An automated check enforcing the policy on every incoming change.
