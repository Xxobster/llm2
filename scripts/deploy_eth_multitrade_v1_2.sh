#!/usr/bin/env bash
# Deploy ETHUSDT multitrade v1.2 (clarity_scope=all) to Xxobster8.
# Stops v1.1; does NOT touch single-book units.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
HOST="${HOST:-94.156.189.76}"
ACCOUNT="${ACCOUNT:-Xxobster8}"
NAME="eth-multitrade-v1_2"
LOCAL_PACK="${ROOT}/artifacts/live_packs/structure_v1_ethusdt_multitrade_v1_2"
LOCAL_CERT="${ROOT}/configs/live/structure_v1_ethusdt_multitrade_v1_2_certificate.yaml"
REMOTE_ROOT="/opt/llm2-structure-${NAME}"

rsync -az --delete \
  --exclude '__pycache__' --exclude '*.pyc' \
  "${ROOT}/llm2/" "root@${HOST}:/opt/llm2-structure/llm2/"

ssh "root@${HOST}" "systemctl stop llm2-structure-eth-multitrade-v1_1.service || true; systemctl disable llm2-structure-eth-multitrade-v1_1.service || true"

HOST="$HOST" ACCOUNT="$ACCOUNT" \
  bash "${ROOT}/scripts/_deploy_symbol_micro.sh" \
    "$NAME" "$LOCAL_PACK" "$LOCAL_CERT" "$REMOTE_ROOT"

echo "OK: ${NAME} on ${ACCOUNT}@${HOST} -> ${REMOTE_ROOT}"
echo "Prior v1.1 left on disk for rollback."
