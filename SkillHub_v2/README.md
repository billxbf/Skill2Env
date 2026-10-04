# SkillHub v2

SkillHub v2 is a collection of **6,538** open-source [Agent Skills](https://agentskills.io)
sourced from [skills.sh](https://skills.sh/), in the same folder/manifest format as
[`SkillHub`](../SkillHub). Each skill is a self-contained folder with its `SKILL.md` and bundled
references, scripts, and assets.

## Data Source

Collected on 2026-09-30 from the skills.sh all-time leaderboard, skill sitemaps, source listings,
and owner profiles. Skills with at least **1,000** installs qualified, giving 11,194 candidates
from 1,341 sources. GitHub sources are pinned to commits.

## Filtering & Deduplication

Candidates were dropped if they:

- are not under MIT, Apache 2.0/1.1, CC BY 4.0/3.0, or CC0 1.0
- require an external account, hosted API, login, credential, or hosted MCP service
- have an unavailable source
- are not self-contained within their own folder

Near-duplicates (word 5-gram Jaccard similarity > 0.95) were removed, keeping the
highest-install entry.

## Licensing

[`skillhub_source_licenses.csv`](skillhub_source_licenses.csv) records each retained skill's
path, source, commit, install count, and license, with original license files copied under
[`licenses`](licenses).

## Layout

| Path | Contents |
| --- | --- |
| `skills/` | 6,538 skills, grouped by source repository |
| `test_samples/` | sampled skills for smoke tests and the quick start |
| `skillhub_source_licenses.csv` | One row per `SKILL.md` in `skills/` identifying sources and licenses |
| `statistics.json` | Collection and filtering counts |

Point `skill2env generate --input-root` at any of these directories, or at a single skill folder.
