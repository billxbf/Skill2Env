<p align="center">
  <img src="assets/s2e_title.png" alt="Skill2Env" width="400">
</p>

<p align="center">
<a href="https://www.apache.org/licenses/LICENSE-2.0"><img src="https://img.shields.io/badge/License-Apache%202.0-green.svg" alt="Apache 2.0 License" /></a>
<a href="paper/Skill2Env_arXiv.pdf"><img src="https://img.shields.io/badge/📄_Paper-red?style=flat-square" alt="Tech Report" /></a>
<a href="SkillHub/"><img src="https://img.shields.io/badge/🤗_SkillHub-pink?style=flat-square" alt="SkillHub" /></a>
<a href="https://hub.harborframework.com/datasets/skill2env/skill2env"><img src="https://img.shields.io/badge/Dataset-HarborHub-orange" alt="Dataset" /></a>

Skill2Env turns any [Agent Skill](https://agentskills.io) into RL-ready terminal tasks in the [Harbor](https://harborframework.com) format.

<p align="center">
  <img src="assets/pipeline.png" alt="Skill2Env pipeline" width="800">
</p>

## Requirements

- Linux host with Docker running (`docker info` works). 
- Python 3.12+ and [`uv`](https://docs.astral.sh/uv/).
- A Codex login at `~/.codex/auth.json` (see below). The Codex agents inside the containers use this file for authentication.
- Internet access while generating: planner and creator containers research and download public assets. 

## Install

```bash
git clone git@github.com:NVlabs/Skill2Env.git
cd Skill2Env
uv sync
```

## Authenticate Codex

Install the Codex CLI and sign in once. This writes `~/.codex/auth.json`, which `skill2env` bind-mounts
into every agent container:

```bash
npm install -g @openai/codex
codex login
```

On a headless server, sign in on a machine with a browser and copy `~/.codex/auth.json` to the server
(or set `CODEX_HOME` to the directory holding it).

Also log in to Docker Hub so base-image resolution uses your authenticated pull quota.

```bash
docker login
```


## How it works

1. **Planner** (one Codex agent per Skill) reads the whole Skill, researches public artifacts
   (repositories pinned to commits, datasets, specs), and writes `N` independent, end-to-end
   problem proposals at Terminal-Bench 3 difficulty that together cover the Skill's breadth. Each
   names the capabilities it tests, the environment with artifact links, the problem, why it is
   hard, its success criteria, the Skill's approach, and good and bad solving behaviors.
   Proposals never involve the physical world, private data, or authentication.
2. **Host** samples only the requester's voice for each instruction: `tone`, `expertise`, and
   `personality`. These never change what is required or verified.
3. **Creator** (one Codex agent per proposal) realizes the whole proposal as a Harbor task: Docker
   environment, `instruction.md` stating every verified requirement, a deterministic
   `tests/test.sh`, `tests/rubric.md` (`## Good Signals` / `## Negative Signals`), and a reference
   `solution/solve.sh`. It also maps every reward metric to the instruction sentence requiring it.
4. **Acceptance**: static checks (including that every mapped quote appears verbatim in
   `instruction.md`), then Harbor Oracle (must score 1) and NOP (must score 0), and every reward
   metric must be mapped. Only accepted tasks are published.

## Quick start

Generate two tasks from one sample Skill:

```bash
uv run skill2env generate SkillHub/test_samples/game-developer -n 2
```

The first run builds the generator image with the latest Codex CLI, which adds a few minutes.
Accepted tasks land under `output/` (`-o` to change it):

```text
output/
├── _corpus_manifest.json
└── task_<skill>_<8-char-id>/
    ├── instruction.md
    ├── task.toml
    ├── environment/
    │   ├── Dockerfile
    │   └── ... fixtures and setup files
    ├── tests/
    │   ├── test.sh
    │   ├── rubric.md
    │   └── ... optional verifier helpers
    └── solution/
        ├── solve.sh
        └── ... optional solution helpers
```

Private run state (planner proposals, creator prompts and transcripts, rejected candidates, and
acceptance logs) is written to `.skill2env/runs/<run-id>/`.

## Generate from [SkillHub](./SkillHub/)

`SkillHub/skills/` contains license-friendly Skill folders (see [`SkillHub/README.md`](SkillHub/README.md)).
The path is scanned recursively, so it can point at one Skill, one family, or the whole hub:

```bash
uv run skill2env generate SkillHub_v2/skills -n 3 -j 8 -o output/skillhub2 --resume
```

Retained tasks keep the source hierarchy under the output root. `--resume` skips every Skill that
a previous run into the same output root already finished.

Start with a small `-j` (about one per two CPU cores) and raise it only after watching CPU, memory,
Docker, and Codex rate-limit behavior.

### Options

| Flag | Default | Meaning |
| --- | --- | --- |
| `-n, --tasks N` | 3 | Problem proposals, and therefore tasks, per Skill (max 16) |
| `-o, --out DIR` | `output` | Output root |
| `-j, --workers N` | 4 | Concurrent Codex agents; also caps concurrent Oracle/NOP runs |
| `--model NAME` | `gpt-6.1-sol` | Codex model for planner and creators |
| `--effort LEVEL` | `high` | `low`, `medium`, `high`, `xhigh`, or `max` |
| `--resume` | off | Skip Skills already finished under the output root |

The Codex CLI version is always the latest one on npm (falling back to the newest local generator
image when offline). The Codex auth file is read from `$CODEX_HOME/auth.json` (default
`~/.codex/auth.json`).

## Submit tasks to the Harbor hub

See Habor's [official guide](https://docs.harborframework.com/core-concepts/harbor-hub/publish) on publishing tasks or dataset.

## Troubleshooting

Codex runs a nested sandbox inside its container. On Ubuntu hosts with AppArmor, allow unprivileged
user namespaces once and make it persistent:

```bash
sudo sysctl -w kernel.apparmor_restrict_unprivileged_userns=0
echo "kernel.apparmor_restrict_unprivileged_userns = 0" | sudo tee /etc/sysctl.d/99-skill2env-userns.conf
```

Without this, every creator shell command fails with
`bwrap: loopback: Failed RTM_NEWADDR: Operation not permitted` and tasks end in
`creator_contract_failed`.



## License

Project-owned source is licensed under [Apache-2.0](LICENSE). See the
[third-party notices](THIRD_PARTY_NOTICES.md) for skill2env's dependencies and container/build tools.

Third-party material in `SkillHub/` retains its respective copyright and license terms.
See the [source and license inventory](SkillHub/skillhub_source_licenses.csv),
[preserved license files](SkillHub/licenses/), and [SkillHub README](SkillHub/README.md).
