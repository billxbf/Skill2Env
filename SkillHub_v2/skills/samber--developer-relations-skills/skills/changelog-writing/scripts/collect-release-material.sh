#!/usr/bin/env bash
# Dump the raw material for one release range: commits, merge subjects, changed
# files, diffstat, and the tags bounding the range.
#
# Usage:
#   collect-release-material.sh [--repo <path>] [--from <ref>] [--to <ref>]
#
#   --repo  repository path (default: current directory)
#   --from  range start (default: most recent tag reachable from --to)
#   --to    range end (default: HEAD)
#
# Exit codes: 0 ok, 2 not a git repository, 64 invalid input.
#
# Requires: bash 3.2+ (macOS default) or bash 4/5 (Linux), plus git 2.21+
# (uses `git log --format=%cs`, the short committer-date specifier), grep, sed.
# Portable across macOS (BSD userland) and Linux (GNU coreutils): the grep
# pattern below is plain POSIX ERE, no GNU-only \b/\d/\s/\w escapes or flags.

set -euo pipefail

repo="."
from=""
to="HEAD"

while [ $# -gt 0 ]; do
  case "$1" in
    --repo) repo="${2:?--repo needs a value}"; shift 2 ;;
    --from) from="${2:?--from needs a value}"; shift 2 ;;
    --to)   to="${2:?--to needs a value}"; shift 2 ;;
    -h|--help) sed -n '2,12p' "$0"; exit 0 ;;
    *) echo "unknown argument: $1" >&2; exit 64 ;;
  esac
done

command -v git >/dev/null 2>&1 || { echo "git not found" >&2; exit 2; }
cd "$repo" || exit 64
git rev-parse --git-dir >/dev/null 2>&1 || { echo "not a git repository: $repo" >&2; exit 2; }

if [ -z "$from" ]; then
  # No explicit start: use the last tag, or the root commit for a first release.
  from="$(git describe --tags --abbrev=0 "$to" 2>/dev/null || true)"
  [ -n "$from" ] || from="$(git rev-list --max-parents=0 "$to" | tail -1)"
fi

range="$from..$to"

echo "=== RANGE ==="
echo "$range"
echo "from: $from ($(git log -1 --format=%cs "$from" 2>/dev/null || echo unknown))"
echo "to:   $to ($(git log -1 --format=%cs "$to"))"
echo "commits: $(git rev-list --count "$range")"

echo
echo "=== COMMITS (oldest first) ==="
git log --reverse --no-merges --format='%h %s' "$range"

echo
echo "=== MERGE SUBJECTS (pull requests) ==="
git log --merges --format='%h %s' "$range" || true

echo
echo "=== COMMIT BODIES MENTIONING BREAKING CHANGES ==="
git log --format='%h %s%n%b' "$range" | grep -iE 'breaking|deprecat|remove[d]? support|no longer' || echo "(none found - still verify against the diff)"

echo
echo "=== CHANGED FILES ==="
git diff --name-status "$range"

echo
echo "=== DIFFSTAT ==="
git diff --stat "$range"

echo
echo "=== CONTRIBUTORS ==="
git shortlog -sne "$range"

echo
echo "NOTE: this is raw material, not a changelog. Reduce to the net diff, drop"
echo "changes with no consumer surface, and verify every entry against the diff."
