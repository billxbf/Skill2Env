# Coverage audit and measurement

Run this before proposing any new channel. It produces the plan's "Position today" section and the baseline every later comparison reads against.

## 1. Inventory: where the project already is

Answer these before judging anything:

- Which registries carry the project, under which names, and who controls those accounts?
- Which repositories package it downstream, at which version? A cross-repository tracker (Repology and equivalents) answers this across hundreds of distribution families, including copies nobody upstream created.
- Which lists, directories and showcases link to it? Search the project name plus the category term, and check competitors' listings - curated lists tend to carry a whole category.
- Which projects depend on it? Registry "dependents" views and ecosystem index services give an order of magnitude.
- Which mirrors, forks or vendored copies exist, and do any have their own audience?

Gather this directly where you can browse or run commands; otherwise ask the maintainer and mark unknowns as unknown rather than assuming zero - an unknown is a finding, meaning the surface is unmonitored.

## 2. Metadata completeness check

For every registry the project publishes to, check field by field and score it as a percentage of fields filled:

- Description - standalone, plain, in the problem's vocabulary, current with the latest positioning.
- Keyword/tag slots - all used, within the registry's limits, matching terms an evaluator would type.
- Categories/classifiers - from the registry's own taxonomy, not invented.
- License - declared and detectable, matching the repository.
- Links - repository, documentation, homepage, issue tracker, funding, changelog.
- Rendered README - first screen readable in the registry's own rendering, no broken images or forge-only markup.
- Version state - latest release visible, no accidental pre-release as the default install.

Anything below 100% here is the cheapest work available and outranks every new channel.

## 3. Stale-listing sweep

For each listing and package, check:

- Does the link resolve?
- Is the description current?
- Is the screenshot recognizable?
- Does the version match?
- Does the name match after any rename?

Fix or request removal, and record the sweep date - that is what makes the next sweep cheap.

A listing that can be neither corrected nor removed is an argument against the channel family, not a sunk cost to defend.

## 4. Arrival sources

Establish where people currently arrive from with whatever the maintainer already has: repository traffic panels (referrers, unique visitors, cloners), registry download series, documentation analytics, tracking parameters on links they control, and "how did you hear about us" answers in issues and discussions.

Two constraints shape this. Repository traffic panels keep only a short rolling window, so an uncaptured baseline is unrecoverable - snapshot before changing anything. And most OSS distribution is unattributable by design: installs come from mirrors, CI caches and proxies. Read direction and magnitude, never precise attribution.

## 5. Metrics that mean something

**Coverage metrics** (facts, auditable today):

- Metadata completeness per registry.
- Repositories on a current vs. outdated version.
- Live vs. stale listings and days since last sweep.
- Days since last release and the longest gap in the last year.

**Arrival metrics** (behaviour, read as quarterly trends):

- Registry downloads by version where available.
- Unique cloners and visitors.
- Dependents count.
- Referral arrivals per channel.
- Inbound issues and discussions from people who clearly are not existing users.

Stars are the loudest and least informative number here. Track them only paired with downloads or cloners: stars moving alone means an announcement travelled, not that distribution improved.

## 6. Baseline snapshot

Write the numbers down with their date and source, in the plan itself, and re-measure on the review cadence rather than continuously - these series are too noisy week over week.

Expect changes on a quarter's horizon: metadata fixes act within weeks, a curated listing accrues slowly, and a downstream package can take a full release cycle to reach anyone's install path.
