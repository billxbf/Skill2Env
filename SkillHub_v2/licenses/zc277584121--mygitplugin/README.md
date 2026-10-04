# mygitplugin

A collection of Git workflow skills for AI coding agents — fork, clone, commit, PR, sync, notifications, and weekly summaries.

## Available Skills

| Skill | Description |
|-------|-------------|
| [`git-fork-clone`](./skills/git-fork-clone/) | Fork a GitHub repo and clone it locally with proper remote setup. |
| [`git-commit-pr`](./skills/git-commit-pr/) | Commit changes and create a PR to the upstream official repo. |
| [`git-create-repo`](./skills/git-create-repo/) | Create a new GitHub repo and clone it locally. |
| [`git-commit-push`](./skills/git-commit-push/) | Commit changes and push to origin without creating a PR. |
| [`git-summarize-weekly`](./skills/git-summarize-weekly/) | Summarize weekly GitHub contributions for weekly reports. |
| [`git-get-notification`](./skills/git-get-notification/) | Check GitHub notifications and recent Issues/PRs for monitored repos. |
| [`git-sync-main`](./skills/git-sync-main/) | Sync the local main branch with the latest code from official upstream or origin. |

## Quick Start

Install all skills globally to **all supported AI coding agents** with one command:

```bash
npx skills add zc277584121/mygitplugin --all -g
```

Update to the latest version:

```bash
npx skills update
```

## Installation

Install using [npx skills](https://skills.sh):

### Install to all agents at once

```bash
# Global — available in all projects, all agents
npx skills add zc277584121/mygitplugin --all -g

# Project-level — current project only, all agents
npx skills add zc277584121/mygitplugin --all
```

### Install to a specific agent

```bash
npx skills add zc277584121/mygitplugin -a claude-code -g
npx skills add zc277584121/mygitplugin -a cursor -g
npx skills add zc277584121/mygitplugin -a codex -g
```

Other supported agents: `windsurf`, `github-copilot`, `cline`, `roo`, `gemini-cli`, `goose`, `kilo`, `augment`, `opencode`, and [40+ more](https://skills.sh).

> **Project vs Global**: Without `-g`, skills are installed into the current project directory. With `-g`, they go to your home directory and are available across projects.

## Updating

```bash
# Check for updates
npx skills check

# Update all globally installed skills to latest
npx skills update
```

To update project-level installs, re-run the `npx skills add` command.

## Claude Code Plugin

This repository can also be installed through the Claude Code plugin system:

```bash
/plugin marketplace add zc277584121/mygitplugin
/plugin install mygitplugin
```

For local plugin development/testing:

```bash
claude --plugin-dir /path/to/mygitplugin
```

## Configuration

- GitHub account: `zc277584121`
- All commits are signed off by: `Cheney Zhang <chen.zhang@zilliz.com>`
- Requires `gh` CLI to be authenticated

## License

MIT
