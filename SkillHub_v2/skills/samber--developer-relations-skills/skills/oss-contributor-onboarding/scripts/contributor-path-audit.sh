#!/usr/bin/env bash
# Reports the mechanical facts about a repository's first-contribution path.
# Usage: contributor-path-audit.sh [repo-root]
# Reports facts only, never judgements. Requires git and standard POSIX tools.

# Requires: bash 3.2+ (macOS default) or bash 4/5 (Linux), plus git 2.6+ (for
# `git log --date=format:`), grep, find, wc, tr, awk, sort, uniq, sed, ls.
# Portable across macOS (BSD userland) and Linux (GNU coreutils): uses POSIX
# regex classes and no GNU-only flags.

set -uo pipefail
ROOT="${1:-.}"
cd "$ROOT" 2>/dev/null || { echo "cannot enter $ROOT" >&2; exit 1; }

hr() { printf '\n== %s ==\n' "$1"; }
found() { printf '  %-28s %s\n' "$1" "$2"; }

hr "COMMUNITY HEALTH FILES"
# GitHub display precedence when duplicated: .github/ then root then docs/.
for base in CONTRIBUTING CODE_OF_CONDUCT SECURITY SUPPORT GOVERNANCE; do
  hits=""
  for dir in .github . docs; do
    for ext in "" .md .rst .txt; do
      f="$dir/$base$ext"
      [ -f "$f" ] && hits="$hits ${f#./}"
    done
  done
  if [ -z "$hits" ]; then
    found "$base" "MISSING"
  else
    set -- $hits
    found "$base" "$hits${2:+   <- precedence: $1}"
  fi
done
if [ -f CODEOWNERS ] || [ -f .github/CODEOWNERS ] || [ -f docs/CODEOWNERS ]; then
  found "CODEOWNERS" "present"
else
  found "CODEOWNERS" "MISSING"
fi
if [ -d .github/ISSUE_TEMPLATE ]; then
  found "issue templates" "$(find .github/ISSUE_TEMPLATE -type f | wc -l | tr -d ' ') file(s)"
else
  found "issue templates" "MISSING"
fi
ls .github/PULL_REQUEST_TEMPLATE* .github/pull_request_template* >/dev/null 2>&1 \
  && found "PR template" "present" || found "PR template" "MISSING"

hr "CONTRIBUTING CONTENT PROBE"
CFILE=""
for dir in .github . docs; do
  for ext in .md .rst .txt ""; do
    [ -z "$CFILE" ] && [ -f "$dir/CONTRIBUTING$ext" ] && CFILE="$dir/CONTRIBUTING$ext"
  done
done
if [ -z "$CFILE" ]; then
  echo "  no CONTRIBUTING file to probe"
else
  echo "  file: ${CFILE#./}  ($(wc -w < "$CFILE" | tr -d ' ') words, $(wc -l < "$CFILE" | tr -d ' ') lines)"
  probe() { grep -qiE "$2" "$CFILE" && found "$1" "mentioned" || found "$1" "NOT FOUND"; }
  probe "types of contribution"  "documentation|translat|triage|non-code|design"
  probe "out of scope / vision"  "out of scope|not accept|scope|roadmap|vision"
  probe "environment setup"      "install|setup|bootstrap|dependenc|make |npm |pip |cargo |go mod"
  probe "run the tests"          "test|spec|pytest|jest|go test|cargo test"
  probe "finding work"           "good first issue|help wanted|first-timers|pick an issue|claim"
  probe "branch / commit rules"  "branch|commit message|conventional|squash|rebase"
  probe "legal gate (DCO/CLA)"   "sign-off|signed-off|dco|cla|contributor license"
  probe "review expectations"    "review|maintainer will|respond|business day|within [0-9]"
  probe "where to ask"           "discord|slack|matrix|discussion|mailing list|forum|irc"
  probe "code of conduct link"   "code of conduct|conduct.md"
fi

hr "SETUP SURFACE"
for f in Makefile Taskfile.yml justfile script/bootstrap scripts/setup.sh \
         .devcontainer/devcontainer.json .devcontainer.json \
         docker-compose.yml compose.yaml \
         .nvmrc .python-version .tool-versions rust-toolchain.toml .ruby-version; do
  [ -e "$f" ] && found "$f" "present"
done
[ -f Makefile ] && grep -oE '^[a-zA-Z0-9_.-]+:' Makefile | tr -d ':' | tr '\n' ' ' \
  | sed 's/^/  make targets: /;s/$/\n/'
lock=$(ls package-lock.json yarn.lock pnpm-lock.yaml poetry.lock uv.lock Cargo.lock go.sum \
       Gemfile.lock composer.lock 2>/dev/null | tr '\n' ' ')
found "lockfiles" "${lock:-NONE}"

hr "CI EXPOSURE ON FORK PULL REQUESTS"
wf=$(find .github/workflows .gitlab-ci.yml .circleci -type f 2>/dev/null | wc -l | tr -d ' ')
found "CI config files" "$wf"
if [ "$wf" != "0" ]; then
  sec=$(grep -rlE 'secrets\.[A-Z_]|\$\{\{ *secrets' .github/workflows 2>/dev/null | wc -l | tr -d ' ')
  found "workflows using secrets" "$sec (these cannot run on fork PRs)"
  pt=$(grep -rl 'pull_request_target' .github/workflows 2>/dev/null | wc -l | tr -d ' ')
  found "pull_request_target uses" "$pt (audit each: runs with write scope)"
fi

hr "CONTRIBUTOR HISTORY (git log, all time)"
if [ -d .git ]; then
  [ -f .git/shallow ] && echo "  WARNING: shallow clone, history numbers below are truncated"
  git log --format='%aE' | tr 'A-Z' 'a-z' | sort | uniq -c | sort -rn > /tmp/.cpa_authors.$$
  total_c=$(awk '{s+=$1} END {print s+0}' /tmp/.cpa_authors.$$)
  total_a=$(wc -l < /tmp/.cpa_authors.$$ | tr -d ' ')
  once=$(awk '$1==1' /tmp/.cpa_authors.$$ | wc -l | tr -d ' ')
  found "commits" "$total_c"
  found "distinct authors" "$total_a"
  [ "$total_a" -gt 0 ] && found "one-commit-only authors" "$once ($((once * 100 / total_a))%)"
  # Contributor absence factor: smallest author count covering 50% of commits (CHAOSS).
  awk -v t="$total_c" '{c+=$1; n++} c*2>=t {print "  absence factor (50% of commits): " n; exit}' /tmp/.cpa_authors.$$
  echo "  new authors per year (first commit):"
  git log --reverse --format='%aE|%ad' --date=format:'%Y' \
    | awk -F'|' '!seen[tolower($1)]++ {y[$2]++} END {for (k in y) print "    " k ": " y[k]}' | sort
  rm -f /tmp/.cpa_authors.$$
else
  echo "  not a git repository"
fi

hr "NOT COVERED HERE"
cat <<'EOF'
  Time to first response, first-PR merge rate, and open good-first-issue stock
  need the forge API. Collect them from the host's UI or API and record the date.
EOF
