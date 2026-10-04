# Marshroom Skills

Agent skills for [Claude Code](https://claude.com/claude-code) that integrate with the [Marshroom](https://github.com/marshroom/marshroom) macOS app for GitHub Issue-driven development.

## What is Marshroom?

Marshroom is a macOS developer productivity tool that uses GitHub Issues as the Single Source of Truth (SSOT). It manages a cart of issues via `~/.config/marshroom/state.json`, which serves as the bridge between the macOS app, CLI, and Claude Code.

## Skills

| Skill | Command | Description |
|-------|---------|-------------|
| **Start Issue** | `/start-issue` | Creates a feature/hotfix branch, injects project + issue context, updates status to `running` |
| **Create PR** | `/create-pr` | Pushes branch, creates PR with `Closes #N`, includes issue body, updates status to `pending` |
| **Validate PR** | `/validate-pr` | Validates branch name, PR body closing keywords, and status pipeline |

## Installation

### Via Vercel Agent Skills (Recommended)

```bash
npx skills add marshroom/marshroom-skills
```

### Manual Installation

Copy the skill files to your project's `.claude/commands/` directory:

```bash
# Clone or download marshroom-skills
git clone https://github.com/marshroom/marshroom-skills.git /tmp/marshroom-skills

# Copy to your project
mkdir -p .claude/commands
cp /tmp/marshroom-skills/skills/start-issue/SKILL.md .claude/commands/start-issue.md
cp /tmp/marshroom-skills/skills/create-pr/SKILL.md .claude/commands/create-pr.md
cp /tmp/marshroom-skills/skills/validate-pr/SKILL.md .claude/commands/validate-pr.md
```

Or use the installer script included in this package:

```bash
bash /path/to/marshroom/marshroom-skills/scripts/install-skill.sh
```

## Prerequisites

- **`gh` CLI** — GitHub CLI, installed and authenticated (`gh auth login`)
- **`git`** — Available in PATH
- **Marshroom app** — Running with issues in your cart
- **`marsh` CLI** (optional) — For status updates and tmux HUD integration

## The GOAT Workflow

Marshroom follows a five-stage execution pipeline:

```
Draft → Inject → Execute → Review → Ship
```

### 1. Draft (Status: `soon`)

Pick issues in the Marshroom macOS app. Click the cart icon to add them to your cart.

### 2. Inject (Status: `running`)

Run `/start-issue` in Claude Code:

```
/start-issue 42
```

This will:
- Checkout `main` and pull latest
- Create a branch (`Feature/#42` or `HotFix/#42`)
- Inject the project's `CLAUDE.md` context
- Display the full issue body for the agent
- Update status to `running`

### 3. Execute

Work on the issue with full context. Claude Code has access to:
- The project's `CLAUDE.md` guidelines
- The complete issue description
- The correct branch already checked out

### 4. Review (Status: `pending`)

Run `/create-pr` when the work is done:

```
/create-pr
```

This will:
- Push the branch
- Create a PR with the issue title and `Closes #N`
- Include the original issue body in the PR description
- Update status to `pending`

### 5. Ship (Status: `completed`)

Optionally validate before merging:

```
/validate-pr
```

Once the PR is merged, the Marshroom poller detects the closure and marks the issue as `completed`.

## State File

All skills read from `~/.config/marshroom/state.json`. See [references/state-schema.md](references/state-schema.md) for the full v3 schema documentation.

## Multi-Repo Support

Marshroom is designed for developers working across multiple repositories. Each cart entry includes repo URLs, so skills automatically match the current working directory's git remote to find the relevant issue.

## License

MIT
