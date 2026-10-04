# License families, traits and compatibility

Contents: families and trigger events · per-license traits · compatibility directions · published heuristics · what a license cannot do.

## Families and what triggers the obligation

| Family                     | Trigger                           | Obligation                                               | Reference licenses                                        |
| -------------------------- | --------------------------------- | -------------------------------------------------------- | --------------------------------------------------------- |
| Public domain equivalent   | none                              | none                                                     | Unlicense, CC0-1.0, 0BSD                                  |
| Permissive                 | distribution                      | preserve copyright and license notices                   | MIT, ISC, BSD-2-Clause, BSD-3-Clause, Apache-2.0, BSL-1.0 |
| Weak / file-level copyleft | distribution of a modified file   | publish modified files; larger work may stay proprietary | MPL-2.0, EPL-2.0                                          |
| Library copyleft           | distribution of a linked work     | recipients must be able to relink a modified library     | LGPL-2.1, LGPL-3.0                                        |
| Strong copyleft            | distribution of a derivative work | whole derivative work under the same license             | GPL-2.0, GPL-3.0                                          |
| Network copyleft           | network interaction               | remote users count as recipients and can demand source   | AGPL-3.0                                                  |

The trigger, not the family name, is what matters. A company can run modified GPL code as a hosted service and publish nothing, because nothing was distributed - that gap is the entire reason AGPL exists.

## Per-license traits worth knowing

- **MIT** - shortest and most recognized permissive license. Silent on patents and on trademarks. Safe default for a small project; leaves every future option open because a sole author can still relicense.
- **ISC / BSD-2-Clause** - functionally MIT with different wording. Choose one and move on; the difference is not strategy.
- **BSD-3-Clause** - adds a no-endorsement clause. Slightly weaker rating in permissive-license reviews because of the extra condition.
- **Apache-2.0** - express patent grant plus patent retaliation (a contributor's patent suit terminates their grant), explicit trademark carve-out, and a `NOTICE` mechanism for required attributions. The default for anything with corporate contributors, patent exposure, or a foundation on the roadmap. Verbose enough that some tiny projects skip it.
- **MPL-2.0** - copyleft per file. Static linking into a proprietary product is fine; modified MPL files must be published. Section 3.3 allows combining with GPL/LGPL/AGPL code unless the author marked Exhibit B "Incompatible With Secondary Licenses".
- **LGPL-2.1 / 3.0** - proprietary applications may link, but recipients must be able to swap in a modified library. Dynamic linking keeps this simple; static linking pulls relink obligations onto the application, and locked devices raise installation-information duties under v3.
- **GPL-2.0 vs GPL-3.0** - v3 adds a patent grant, anti-tivoization terms and clearer termination-cure rules. v2 remains where an ecosystem is pinned to it (kernel-adjacent code). "or any later version" is a separate decision: it future-proofs but hands the steward a future say.
- **AGPL-3.0** - GPL-3.0 plus the network clause. It is a business lever as much as a philosophy: a company unwilling to publish its own service source buys a commercial license instead.
  - Some enterprises refuse it outright in writing: Google's published policy says "code licensed under the GNU Affero General Public License (AGPL) MUST NOT be used at Google", and forbids installing AGPL programs on company machines without Open Source Programs Office authorization.
  - No credible figure exists for how many companies run that rule, so cite named policies, never a percentage.
- **Unlicense / CC0** - public-domain dedication. Some jurisdictions do not recognize dedication, and some corporate policies reject the ambiguity; BSD-0 or MIT is usually the safer way to say "do anything".

Content that is not code (documentation, specs, media) usually wants a Creative Commons license instead - CC-BY-4.0 is the common choice, and foundations often mandate it for docs. Never apply a code license to prose or a content license to code.

## Compatibility is directional

Ask "can code under A be combined into a work distributed under B", never "are A and B compatible".

- Apache-2.0 → GPLv3 works. GPLv3 → Apache-licensed project does not; the ASF refuses it because GPLv3's authors treat linking as creating a derivative work.
- Apache-2.0 → GPLv2 is **not** accepted by the FSF, which reads Apache's patent-termination and indemnification terms as restrictions GPLv2 does not permit. Mixed dependency graphs hit this in practice.
- MPL-2.0 → GPL/LGPL/AGPL works through MPL §3.3; the combination then ships under both licenses.
- Permissive → anything works, which is precisely why a permissive project can be absorbed into a closed competitor without reciprocity. That is a feature or a defect depending on step 2's posture.
- Copyleft → permissive never works. A single copyleft dependency in the shipped artifact can decide the outbound license before any preference is expressed.

Audit method:

1. Enumerate shipped dependencies, including transitive ones.
2. Separate build-only and test-only dependencies.
3. Check vendored or copy-pasted code.
4. Record each result as an SPDX identifier, so the check is repeatable in CI.

## Published heuristics you can cite

**FSF license recommendations**:

- Programs under about 300 lines → Apache-2.0, because copyleft overhead is not worth it.
- Library against an entrenched non-copyleft competitor → LGPL.
- Library trying to displace a proprietary format → permissive, to buy adoption (the FSF concedes this failed for Ogg Vorbis).
- Library with a specialized capability and no entrenched alternative → GPL.
- Server software → AGPL.

**Blue Oak Council license list** - rates permissive licenses Gold / Silver / Bronze / Lead by drafting quality and patent handling, so a company can write "Bronze or better" into policy instead of maintaining its own allowlist. BSD-2-Clause-Patent is the only Gold; Apache-2.0, MIT and ISC sit in Silver; joke licenses are Lead.

**OSI approval** - the marker most procurement allowlists filter on. If a license is not on that list, expect a bespoke legal review at every adopting company, which is a distribution cost paid on every deal.

## What no license can do

- Stop a competitor willing to comply. Copyleft redirects competition into compliance work; it does not prevent it.
- Protect the project's name. That is trademark, a separate asset needing its own policy; foundations require transferring it as a condition of joining.
- Apply retroactively. Published releases stay under their original terms forever.
- Create adoption. If nothing depends on the project, no clause converts anything.
