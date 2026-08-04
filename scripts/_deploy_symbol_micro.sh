#!/usr/bin/env bash
# Deploy one structure_v1 symbol pack as its own VPS service.
# Usage: _deploy_symbol_micro.sh <name> <local_pack_dir> <local_cert> <remote_root>
set -euo pipefail
NAME="$1"
LOCAL_PACK="$2"
LOCAL_CERT="$3"
REMOTE_ROOT="$4"
HOST="${HOST:-94.156.189.76}"
ACCOUNT="${ACCOUNT:-Xxobster7}"

ssh "root@${HOST}" "mkdir -p ${REMOTE_ROOT}/{pack,state,logs} && ln -sfn /opt/llm2-structure/venv ${REMOTE_ROOT}/venv && ln -sfn /opt/llm2-structure/llm2 ${REMOTE_ROOT}/llm2"

# Sync pack (exclude wal/shm)
rsync -az --delete \
  --exclude '*.sqlite-wal' --exclude '*.sqlite-shm' \
  "${LOCAL_PACK}/" "root@${HOST}:${REMOTE_ROOT}/pack/"

scp "${LOCAL_CERT}" "root@${HOST}:${REMOTE_ROOT}/certificate.yaml"

UNIT="/etc/systemd/system/llm2-structure-${NAME}.service"
ssh "root@${HOST}" "cat > ${UNIT}" <<EOF
[Unit]
Description=LLM2 structure_v1 ${NAME} micro-live LIVE MIN_EXCHANGE
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
WorkingDirectory=${REMOTE_ROOT}
Environment=PYTHONPATH=${REMOTE_ROOT}
Environment=LLM2_INDICATORS_DB=${REMOTE_ROOT}/pack/indicators_live_slice.sqlite
Environment=LLM2_STRUCTURE_SOURCE=binance
Environment=SHARED_CANDLES_DB=/var/lib/botsgeneral/shared_candles.db
Environment=TRADING_SECRETS_ENV=/root/.trading/secrets.env
Environment=PYTHONPATH=${REMOTE_ROOT}:/opt/botsgeneral/packages/live_candles/src:/opt/botsgeneral/packages/indicators/src
ExecStart=${REMOTE_ROOT}/venv/bin/python -m llm2.live.micro_runner --pack ${REMOTE_ROOT}/pack --state ${REMOTE_ROOT}/state/micro_live_state.sqlite --mode LIVE --live-orders --account ${ACCOUNT} --cert ${REMOTE_ROOT}/certificate.yaml
Restart=always
RestartSec=10
StandardOutput=append:${REMOTE_ROOT}/logs/micro_live.log
StandardError=append:${REMOTE_ROOT}/logs/micro_live.log

[Install]
WantedBy=multi-user.target
EOF

ssh "root@${HOST}" "systemctl daemon-reload && systemctl enable --now llm2-structure-${NAME}.service && sleep 2 && systemctl is-active llm2-structure-${NAME}.service && tail -n 20 ${REMOTE_ROOT}/logs/micro_live.log"
echo "deployed ${NAME} -> ${REMOTE_ROOT}"
