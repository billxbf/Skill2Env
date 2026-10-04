# Sync

Quick git synchronization with remote repository.

## Installation

```bash
# 1. Add marketplace (first time only)
claude plugin marketplace add october-academy/claude-plugins

# 2. Update marketplace
claude plugin marketplace update

# 3. Install plugin
claude plugin install sync@october-plugins

# 4. Restart Claude Code
```

## Usage

```bash
/sync              # Pull from origin main
/sync develop      # Pull from origin develop
/sync upstream     # Pull from upstream main (forks)
```

### Korean Triggers

- "동기화"
- "원격에서 가져와"
- "풀 받아"

## How It Works

```
┌───────────────────────────────────────────┐
│  /sync                                     │
└──────────────────┬────────────────────────┘
                   │
                   ▼
┌───────────────────────────────────────────┐
│  1. Pre-sync Check                         │
│     - Uncommitted changes?                 │
│     - Stash / Commit / Discard?            │
└──────────────────┬────────────────────────┘
                   │
                   ▼
┌───────────────────────────────────────────┐
│  2. Fetch and Pull                         │
│     git pull origin main                   │
│     (or --rebase for cleaner history)      │
└──────────────────┬────────────────────────┘
                   │
                   ▼
┌───────────────────────────────────────────┐
│  3. Report Results                         │
│     - Commits pulled                       │
│     - Files changed                        │
│     - Conflict status                      │
└───────────────────────────────────────────┘
```

## Handling Conflicts

If merge conflicts occur:

1. List conflicting files
2. Offer to help resolve
3. After resolution: `git add <files>` → `git commit`

## Common Scenarios

### Fork Workflow

```bash
# Add upstream if not exists
git remote add upstream <original-repo-url>

# Sync with upstream
git fetch upstream
git merge upstream/main
```

### Diverged Branches

Options:
- **Merge** (default): `git pull origin main`
- **Rebase** (cleaner): `git pull --rebase origin main`
- **Reset** (destructive): `git reset --hard origin/main`

## Error Handling

| Error | Solution |
|-------|----------|
| "Uncommitted changes" | Stash or commit first |
| "Merge conflict" | Help resolve conflicts |
| "Remote not found" | Check `git remote -v` |

## License

MIT
