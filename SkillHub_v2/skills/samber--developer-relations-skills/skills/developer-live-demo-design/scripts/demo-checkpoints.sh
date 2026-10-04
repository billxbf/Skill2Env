#!/usr/bin/env bash
# Manage demo checkpoints as git tags, so any demo segment can be entered
# directly instead of replaying the segments before it.
#
# Usage:
#   demo-checkpoints.sh save <n> <label>   tag the current tree as segment n
#   demo-checkpoints.sh list               list checkpoints in order
#   demo-checkpoints.sh goto <n>           enter segment n
#   demo-checkpoints.sh reset              return to segment 1
#   demo-checkpoints.sh next | prev        move one segment
#
# Checkpoints are local tags named demo/step-<n>-<label>. They are never pushed.
#
# Requires: bash 3.2+ (macOS default) or bash 4/5 (Linux), plus git, sed,
# sort, head.
# Portable across macOS (BSD userland) and Linux (GNU coreutils): uses POSIX
# sed/sort options only, no GNU-only flags.

set -eu

PREFIX="demo/step-"

die() { printf '%s\n' "$1" >&2; exit 1; }

require_repo() {
  git rev-parse --git-dir >/dev/null 2>&1 || die "not inside a git repository"
}

require_clean() {
  # Entering a checkpoint discards local edits, which is the point on stage but
  # a disaster during authoring. Refuse unless the tree is clean.
  if [ -n "$(git status --porcelain)" ]; then
    die "working tree is dirty - commit, stash, or run: git checkout -- ."
  fi
}

tag_for() {
  git tag --list "${PREFIX}$1-*" | head -n 1
}

current_step() {
  git tag --points-at HEAD --list "${PREFIX}*" | head -n 1 |
    sed "s|^${PREFIX}||; s|-.*$||"
}

cmd_save() {
  [ $# -eq 2 ] || die "usage: save <n> <label>"
  git tag -f "${PREFIX}$1-$2" >/dev/null
  printf 'saved %s%s-%s at %s\n' "$PREFIX" "$1" "$2" "$(git rev-parse --short HEAD)"
}

cmd_list() {
  git tag --list "${PREFIX}*" | sort -t- -k2 -n
}

cmd_goto() {
  [ $# -eq 1 ] || die "usage: goto <n>"
  tag=$(tag_for "$1")
  [ -n "$tag" ] || die "no checkpoint for segment $1 (run: list)"
  require_clean
  git checkout --quiet "$tag"
  printf 'at %s\n' "$tag"
}

cmd_move() {
  cur=$(current_step)
  [ -n "$cur" ] || die "HEAD is not on a checkpoint; use: goto <n>"
  if [ "$1" = "next" ]; then cmd_goto "$((cur + 1))"; else cmd_goto "$((cur - 1))"; fi
}

require_repo
[ $# -ge 1 ] || die "usage: save|list|goto|reset|next|prev"
action=$1
shift

case "$action" in
  save)  cmd_save "$@" ;;
  list)  cmd_list ;;
  goto)  cmd_goto "$@" ;;
  reset) cmd_goto 1 ;;
  next)  cmd_move next ;;
  prev)  cmd_move prev ;;
  *)     die "unknown command: $action" ;;
esac
