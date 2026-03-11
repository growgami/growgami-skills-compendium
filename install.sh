#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SKILLS_DIR="$SCRIPT_DIR/skills"
TARGET="${CLAUDE_SKILLS_DIR:-$HOME/.claude/skills}"

green="\033[32m" dim="\033[2m" yellow="\033[33m" reset="\033[0m"

list_skills() {
  for d in "$SKILLS_DIR"/*/; do
    [ -f "$d/SKILL.md" ] && basename "$d"
  done
}

install_skill() {
  local name="$1"
  local src="$SKILLS_DIR/$name"
  if [ ! -f "$src/SKILL.md" ]; then
    echo -e "  ${yellow}skip${reset} $name (not found)"
    return 1
  fi
  mkdir -p "$TARGET/$name"
  cp -r "$src"/* "$TARGET/$name/"
  echo -e "  ${green}+${reset} $name"
}

if [ "${1:-}" = "--help" ] || [ "${1:-}" = "-h" ]; then
  echo "Usage: ./install.sh [--all | skill1 skill2 ...]"
  echo ""
  echo "  --all         Install all skills"
  echo "  --list        List available skills"
  echo "  skill1 ...    Install specific skills"
  echo "  (no args)     Interactive picker"
  echo ""
  echo "Target: $TARGET (override with CLAUDE_SKILLS_DIR)"
  exit 0
fi

if [ "${1:-}" = "--list" ]; then
  list_skills
  exit 0
fi

mkdir -p "$TARGET"
echo -e "\n  ${dim}Installing to $TARGET${reset}\n"

if [ "${1:-}" = "--all" ]; then
  for name in $(list_skills); do
    install_skill "$name"
  done
  echo ""
  exit 0
fi

if [ $# -gt 0 ]; then
  for name in "$@"; do
    install_skill "$name"
  done
  echo ""
  exit 0
fi

# Interactive picker
skills=($(list_skills))
echo "  Available skills:"
echo ""
for i in "${!skills[@]}"; do
  printf "  %2d) %s\n" $((i+1)) "${skills[$i]}"
done
echo ""
read -rp "  Enter numbers or names (comma-separated), or 'all': " choice

if [ "$choice" = "all" ]; then
  for name in "${skills[@]}"; do
    install_skill "$name"
  done
else
  IFS=',' read -ra picks <<< "$choice"
  for pick in "${picks[@]}"; do
    pick="$(echo "$pick" | xargs)"
    if [[ "$pick" =~ ^[0-9]+$ ]] && [ "$pick" -ge 1 ] && [ "$pick" -le "${#skills[@]}" ]; then
      install_skill "${skills[$((pick-1))]}"
    else
      install_skill "$pick"
    fi
  done
fi
echo ""
