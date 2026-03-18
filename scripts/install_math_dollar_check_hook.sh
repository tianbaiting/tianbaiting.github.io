#!/usr/bin/env bash
set -euo pipefail

repo_root="$(git rev-parse --show-toplevel)"
hook_path="$repo_root/.git/hooks/pre-commit"
checker="$repo_root/scripts/check_math_dollar_blocks.py"

if [[ ! -f "$checker" ]]; then
  echo "ERROR: checker not found at $checker" >&2
  exit 1
fi

chmod +x "$checker"

cat > "$hook_path" <<'HOOK'
#!/usr/bin/env bash
set -euo pipefail

repo_root="$(git rev-parse --show-toplevel)"
"$repo_root/scripts/check_math_dollar_blocks.py" --staged
HOOK

chmod +x "$hook_path"
echo "Installed pre-commit hook: $hook_path"
echo "This hook runs: scripts/check_math_dollar_blocks.py --staged"
