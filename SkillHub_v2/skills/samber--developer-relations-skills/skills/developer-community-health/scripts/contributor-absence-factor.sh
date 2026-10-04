#!/usr/bin/env bash
# Compute the contributor absence factor: the smallest number of people
# producing a given share (default 50%) of commits in a git repository.
# Higher is safer; 1 means a single point of failure.
#
# Requires: bash 3.2+ (macOS default) or bash 4/5 (Linux), plus git, grep,
# sort, uniq, awk.
# Portable across macOS (BSD userland) and Linux (GNU coreutils): uses plain
# POSIX ERE and POSIX awk, no GNU-only flags.
set -euo pipefail

usage() {
  cat <<'EOF'
Usage: contributor-absence-factor.sh [-r REPO] [-s SINCE] [-p PERCENT] [-x EXCLUDE_REGEX]

  -r REPO           path to the git repository (default: current directory)
  -s SINCE          only count commits after this date, e.g. "12 months ago" (default: all history)
  -p PERCENT        share of commits to cover, 1-100 (default: 50)
  -x EXCLUDE_REGEX  case-insensitive regex of author names to drop, e.g. "bot|\[bot\]|dependabot"
                    (default: bot|\[bot\]|dependabot|renovate|github-action)
  -h                show this help

Output: the absence factor, the covering contributors, and the total commit count.
Bots are excluded by default because automated commits inflate the factor and hide real concentration.
EOF
}

repo="."
since=""
percent=50
exclude='bot|\[bot\]|dependabot|renovate|github-action'

while getopts ":r:s:p:x:h-:" opt; do
  case "$opt" in
    r) repo="$OPTARG" ;;
    s) since="$OPTARG" ;;
    p) percent="$OPTARG" ;;
    x) exclude="$OPTARG" ;;
    h) usage; exit 0 ;;
    -) [ "$OPTARG" = "help" ] && { usage; exit 0; }; echo "unknown option --$OPTARG" >&2; exit 2 ;;
    :) echo "option -$OPTARG needs a value" >&2; exit 2 ;;
    *) usage >&2; exit 2 ;;
  esac
done

command -v git >/dev/null || { echo "git not found" >&2; exit 1; }
git -C "$repo" rev-parse --git-dir >/dev/null 2>&1 || { echo "not a git repository: $repo" >&2; exit 1; }
case "$percent" in ''|*[!0-9]*) echo "-p must be an integer" >&2; exit 2 ;; esac
[ "$percent" -ge 1 ] && [ "$percent" -le 100 ] || { echo "-p must be between 1 and 100" >&2; exit 2; }

log_args=(-C "$repo" log --no-merges --pretty=format:%aN)
[ -n "$since" ] && log_args+=(--since="$since")

# Identity note: this counts author names as git records them. Merge aliases of the
# same person before trusting the number, or the factor reads higher than reality.
git "${log_args[@]}" \
  | grep -Eiv "$exclude" \
  | sort | uniq -c | sort -rn \
  | awk -v pct="$percent" '
      { count[NR]=$1; name[NR]=substr($0, index($0,$2)); total+=$1 }
      END {
        if (total == 0) { print "no commits matched"; exit 1 }
        target = total * pct / 100
        running = 0
        for (i = 1; i <= NR; i++) {
          running += count[i]
          printf "  %2d. %-40s %6d commits\n", i, name[i], count[i]
          if (running >= target) { factor = i; break }
        }
        printf "\nTotal commits: %d (from %d contributors)\n", total, NR
        printf "Contributor absence factor at %d%%: %d\n", pct, factor
      }'
