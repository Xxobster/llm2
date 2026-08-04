#!/usr/bin/env bash
# Deploy ETHUSDT multitrade v1 to 94.x / Xxobster8 (does NOT touch single-book units).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
HOST="${HOST:-94.156.189.76}"
ACCOUNT="${ACCOUNT:-Xxobster8}"
NAME="eth-multitrade-v1"
LOCAL_PACK="${ROOT}/artifacts/live_packs/structure_v1_ethusdt_multitrade_v1"
LOCAL_CERT="${ROOT}/configs/live/structure_v1_ethusdt_multitrade_v1_certificate.yaml"
REMOTE_ROOT="/opt/llm2-structure-${NAME}"

# Sync shared runner code first (symlink target for all llm2-structure* units).
rsync -az --delete \
  --exclude '__pycache__' --exclude '*.pyc' \
  "${ROOT}/llm2/" "root@${HOST}:/opt/llm2-structure/llm2/"

HOST="$HOST" ACCOUNT="$ACCOUNT" \
  bash "${ROOT}/scripts/_deploy_symbol_micro.sh" \
    "$NAME" "$LOCAL_PACK" "$LOCAL_CERT" "$REMOTE_ROOT"

echo "OK: ${NAME} on ${ACCOUNT}@${HOST} -> ${REMOTE_ROOT}"
echo "Single-book llm2-structure-eth (Xxobster7) left untouched."
