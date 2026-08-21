#!/usr/bin/env bash
# Deploy live parity + max-hold fixes to all LLM2 structure roots on a host.
set -euo pipefail
HOST="${1:?host ln1|ln3}"
ROOT_LOCAL="${2:-d:/projects/LLM2}"

FILES=(
  "llm2/live/micro_runner.py"
  "llm2/live/refresh_structure.py"
  "llm2/live/feature_parity_contract.py"
)

# Discover install roots that have micro_runner.py
mapfile -t ROOTS < <(ssh -o BatchMode=yes "$HOST" "find /opt -maxdepth 2 -type f -path '/opt/llm2-structure*/llm2/live/micro_runner.py' 2>/dev/null | sed 's#/llm2/live/micro_runner.py##' | sort -u")

if [[ ${#ROOTS[@]} -eq 0 ]]; then
  echo "No llm2-structure roots on $HOST" >&2
  exit 1
fi

echo "HOST=$HOST roots=${#ROOTS[@]}"
for r in "${ROOTS[@]}"; do
  echo "  $r"
  ssh -o BatchMode=yes "$HOST" "mkdir -p '$r/llm2/live'"
  for f in "${FILES[@]}"; do
    scp -o BatchMode=yes "$ROOT_LOCAL/$f" "$HOST:$r/$f"
  done
  # Drop stale bytecode so imports pick up new modules.
  ssh -o BatchMode=yes "$HOST" "rm -rf '$r/llm2/live/__pycache__'"
done

echo "Import smoke on first root..."
FIRST="${ROOTS[0]}"
ssh -o BatchMode=yes "$HOST" "cd '$FIRST' && ./venv/bin/python -c \"
from llm2.live.refresh_structure import refresh_symbol, ensure_live_structure_parity, MIN_STRUCTURE_HISTORY_BARS
from llm2.live.feature_parity_contract import FORBIDDEN_LIVE_STRUCTURE_LIMIT
from llm2.live import micro_runner
assert MIN_STRUCTURE_HISTORY_BARS['1h'] > FORBIDDEN_LIVE_STRUCTURE_LIMIT
print('OK', FIRST, 'min_1h', MIN_STRUCTURE_HISTORY_BARS['1h'])
\""
echo "DEPLOY_OK $HOST"
