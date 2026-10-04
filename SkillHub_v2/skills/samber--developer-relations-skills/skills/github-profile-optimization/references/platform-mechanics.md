# Platform mechanics

Hard rules for the profile surfaces on the dominant code host. Re-check anything that looks surprising: hosts change these without notice, and other forges (GitLab, Codeberg, self-hosted) expose different surfaces entirely.

## Contents

- Personal profile README prerequisites
- Organization profile README prerequisites
- Field and display limits
- Contribution graph counting rules
- Achievements
- Image proxying, caching and dynamic content

## Personal profile README prerequisites

All four must hold at once, or nothing renders and no warning is shown:

1. Repository name matches the username exactly.
2. Repository is public.
3. `README.md` sits at the repository root.
4. The file is not empty.

Deleting the file, emptying it, flipping the repository to private, or renaming the repository removes the README from the profile silently. Repositories created before July 2020 with a matching name are not promoted automatically and must be shared to the profile by hand.

The README renders at the top of the Overview tab, above the pinned items.

## Organization profile README prerequisites

| Variant     | Repository                  | Path                | Seen by           |
| ----------- | --------------------------- | ------------------- | ----------------- |
| Public      | `.github` (public)          | `profile/README.md` | Everyone          |
| Member-only | `.github-private` (private) | `profile/README.md` | Signed-in members |

Signed-in members get a member/public toggle and land on the member view by default when member-only content exists. Public organization profiles are unavailable under Enterprise Managed Users.

Domain verification (a DNS TXT record, up to 72 hours to propagate) adds a "Verified" badge. Every domain used in the organization's website and email fields needs verifying separately, including `www.` variants.

## Field and display limits

| Surface                    | Limit                                                                      |
| -------------------------- | -------------------------------------------------------------------------- |
| Bio                        | 160 characters, supports `@mentions` of organizations you belong to        |
| Social account links       | 4                                                                          |
| Pinned items, personal     | 6 total, repositories and gists combined, drag-reorderable                 |
| Pinned items, organization | 6 public + 6 member-visible                                                |
| Status                     | message + emoji, optional busy flag and expiry, scopeable to organizations |
| Repository topics          | 20, lowercase, ≤50 characters each                                         |

With no pins set, the profile falls back to auto-selected "Popular repositories" - an ordering you do not control and that frequently surfaces an abandoned repository.

## Contribution graph counting rules

- Only commits on the **default branch** or `gh-pages` count.
- The authoring email must be connected to the account, or be the host-provided `noreply` address. A machine-local address (`jane@computer.local`) never counts.
- Commits made **inside a fork never count** - the work appears only once merged upstream through a pull request.
- Allow up to **24 hours** for a qualifying contribution to appear.
- Private-repository activity can be surfaced as anonymous counts through a profile setting; visitors see the activity without repository names. The host's own position is that including private work is the more accurate representation of a person's contributions, which makes this toggle the first fix for an employed developer whose graph looks dead - not new public work.

Practical consequence: a heavy contributor working on feature branches, in forks, or behind a work email can show an empty graph, and a light contributor can fill one with trivial commits. Read the graph as evidence of _nothing_ on its own, and never advise gaming it.

## Achievements

| Achievement         | Earned by                                         | Tiers              |
| ------------------- | ------------------------------------------------- | ------------------ |
| Pull Shark          | Merged pull requests                              | 2, 16, 128, 1024   |
| Pair Extraordinaire | Co-authored a merged pull request                 | 10, 24, 48         |
| Starstruck          | Own repository reaching star counts               | 16, 128, 512, 4096 |
| Galaxy Brain        | Accepted discussion answers                       | 2, 8, 16, 32       |
| Quickdraw           | Closed an issue or PR within 5 minutes            | (no tiers)         |
| YOLO                | Merged own PR without review                      | (no tiers)         |
| Public Sponsor      | Sponsoring through the host's sponsorship program | (no tiers)         |

Retired or unobtainable: Arctic Code Vault Contributor, Mars 2020 Contributor, Heart On Your Sleeve, Open Sourcerer. Quickdraw and YOLO are earnable in under a minute and carry no signal; the first four track sustained work and are the only ones worth mentioning to a reader.

## Image proxying, caching and dynamic content

- Every image URL in rendered markdown is rewritten through an anonymizing proxy, so third-party widget services never see the visitor.
- The proxy honours upstream cache headers. A generated image served without `Cache-Control: no-cache` can be served **stale indefinitely** - the standard failure mode of stats and streak cards.
- Images behind authentication or on a private network cannot render at all.
- `curl -X PURGE` against the proxied URL forces a refetch and is the documented escape hatch for a frozen image.
- Embedded HTML is sanitized: no scripts, no forms, no interactive embeds. Anything "live" on a profile is a generated image, a scheduled job rewriting the markdown, or an animation baked into an SVG or GIF.
