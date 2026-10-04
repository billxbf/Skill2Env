# Post examples

Weak and strong versions of the four post types the practice produces. The difference is almost always specificity plus something at stake.

## Contents

- [Shipping post](#shipping-post)
- [Decision post](#decision-post)
- [Failure post](#failure-post)
- [Metrics post](#metrics-post)
- [Stopping a disclosure](#stopping-a-disclosure)
- [Charter example](#charter-example)

## Shipping post

**Weak**

> 🚀 Big week for the project! Lots of improvements and bug fixes shipped. Check out the new release, we think you'll love it. Star the repo if you find it useful! #buildinpublic

Nothing verifiable, nothing a reader can act on, and a star solicitation that developer audiences read as marketing.

**Strong**

> v0.9 is out. The parser rewrite lands: config files over ~5 MB now load in 0.4 s instead of 12 s, because we stopped re-reading includes on every reference.
>
> Breaking: `--strict` now rejects duplicate keys instead of warning. Migration note in the release, one line for most people.
>
> Still open: Windows path handling is wrong for UNC shares (#412). Fix targeted for the next release.

Concrete numbers with the mechanism, the breaking change stated before anyone hits it, and a known defect named without being asked.

## Decision post

**Weak**

> We decided to rewrite the storage layer. Excited about where this is going!

**Strong**

> We are replacing the storage layer, and we picked the boring option over the interesting one.
>
> Options we weighed: keep the current embedded engine (simplest, but no concurrent writers), move to a client-server database (solves it, adds an operational dependency for every user), or a hybrid with a write-ahead log (what we chose).
>
> The hybrid wins because our users install this on laptops and CI runners where "just run a database" is not acceptable. It costs us a more complex recovery path, which is why the next release ships a repair command before the new engine becomes the default.

Alternatives named fairly, the constraint doing the work made explicit, and the cost accepted out loud. Readers who disagree can argue with the constraint instead of the conclusion.

## Failure post

**Weak**

> Sorry about the downtime earlier. Everything is back to normal now, thanks for your patience!

**Strong**

> Yesterday's release corrupted the local cache for anyone upgrading from 2.3 with a custom cache path. Roughly a tenth of installs based on download counts by version.
>
> Cause: the migration assumed the default path and deleted the directory it computed, not the one configured.
>
> Fix: 2.4.1 is out; it detects the broken state and rebuilds. If you already lost the cache, nothing else was touched - data lives in the store, not the cache.
>
> What changes: migrations now run against a temporary copy, and the release checklist adds an upgrade test from the two previous minor versions with a non-default config. We had no such test, which is the real defect.

Impact first in terms the reader can check against their own install, then cause, then the systemic change. No blame, no vagueness about scope.

## Metrics post

**Weak**

> We crossed 10k stars! Incredible community, thank you all 🙏

Stars are the loudest and least meaningful signal, and a milestone with nothing attached teaches nobody anything.

**Strong**

> Quarterly numbers: 41k weekly downloads (up from 28k), 19 distinct contributors (up from 12), median first response on issues 31 hours (target 48), and 6 sponsors covering about a fifth of the hosting bill.
>
> The download growth is one downstream project adopting us - the underlying contributor and sponsor curves are much flatter, and that is the number I actually care about.
>
> Stars went from 8.1k to 10.3k. It did not change anything.

Several metrics with direction, an honest attribution of what caused the good number, and an explicit statement of which signal is being ignored.

**Do not do this**

> Just hit $14k MRR 🚀 [screenshot of a revenue chart]
>
> 6 months ago this was $0. Building in public works. Ask me anything.

Two separate problems, and the second is the one people miss. A bare screenshot is now the format most associated with fabricated numbers: tools exist purely to generate convincing fake revenue charts, and a verified-revenue service exists as the market's answer to them. Readers discount an unverifiable chart rather than being impressed by it.

And a milestone with no mechanism attached teaches nobody anything, which is the part that would have earned the credibility the screenshot was reaching for. If the number is published, publish it from something a reader can check, and say what produced it.

## Stopping a disclosure

Every documented case of a founder withdrawing public revenue was framed defensively, and each one became a second public event in its own right. Plan the exit before it is needed.

**Weak**

The dashboard simply stops updating. No post, no note on the page.

Silence after disclosure is read as bad news, and usually as worse news than the truth. This is the single most common way the practice ends.

**Strong**

> I'm retiring the public revenue page at the end of this month.
>
> Why: we hired two people this year, and the number stopped being my personal milestone the moment it became theirs. It also draws a category of attention I'd rather not aim at a three-person team.
>
> What stays public: the changelog, the roadmap, the quarterly write-up including the misses. Everything that was useful to you is still there. The archive of past numbers stays up - I'm not deleting history, just not adding to it.

The reason is specific and structural rather than defensive, the reader learns what they keep, and nothing is quietly deleted. Note the shape: this only reads well because the person had something left to keep publishing. A charter that put everything on rung 5 has no graceful exit available.

## Charter example

The deliverable this skill produces, filled in for a small solo-maintained library.

```markdown
# Build-in-public charter - libfoo

Goal Contributors first, sponsors second. Not adoption-at-any-cost.
Audience Individual backend developers picking libraries themselves; a
secondary company-adoption track needs release-cadence evidence.
Rung Rungs 1-3: shipping log, decisions, failures.
Rung 4 (downloads, contributors, response time) quarterly.
Rung 5 excluded: income is 40 EUR/month of sponsorship and
publishing it would invite support expectations it cannot fund.
Boundaries No unfixed-security detail, ever. No dated roadmap; direction only.
No named users without written consent. Contract work stays private.
Cadence Release spine, roughly every 3 weeks, plus one quarterly report.
Budget 90 min per release post, 2 h per quarterly report.
Anchor CHANGELOG.md plus a post on the project blog.
Amplifiers Two developer communities where the maintainer already participates.
Support plan README states part-time maintenance and a 1-week response target.
Feature requests go to a public discussion, never DMs.
Measurement Quarterly: contributor count, first-response time, sponsor count,
inbound quality. Reviewed at the same time as the report.
Pause rule If two consecutive releases ship with no post, drop to the
quarterly report only, and say so publicly.
```
