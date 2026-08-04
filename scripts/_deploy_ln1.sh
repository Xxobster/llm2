#!/usr/bin/env bash
set -euo pipefail
REMOTE=ln1
ROOT=/opt/llm2-structure
LOCAL_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PACK="$LOCAL_ROOT/artifacts/live_packs/structure_v1_lgbm"
CERT="$LOCAL_ROOT/configs/live/structure_v1_lgbm_certificate.yaml"

ssh "$REMOTE" "mkdir -p $ROOT/pack $ROOT/state $ROOT/logs $ROOT/llm2"

# pack (rsync if available, else scp -r)
if command -v rsync >/dev/null 2>&1; then
  rsync -az --delete "$PACK/" "$REMOTE:$ROOT/pack/"
else
  scp -r "$PACK/." "$REMOTE:$ROOT/pack/"
fi
scp -r "$LOCAL_ROOT/llm2/." "$REMOTE:$ROOT/llm2/"
scp "$CERT" "$REMOTE:$ROOT/structure_v1_lgbm_certificate.yaml"

# secrets (Xxobster7) — never echo
if [[ -f "$HOME/.trading/secrets.env" ]]; then
  ssh "$REMOTE" "mkdir -p /root/.trading"
  scp "$HOME/.trading/secrets.env" "$REMOTE:/root/.trading/secrets.env"
  ssh "$REMOTE" "chmod 600 /root/.trading/secrets.env"
fi

ssh "$REMOTE" bash -s <<'REMOTE'
set -euo pipefail
ROOT=/opt/llm2-structure
cd "$ROOT"
python3 -m venv venv
./venv/bin/pip install -q -U pip
./venv/bin/pip install -q lightgbm joblib pandas numpy pyyaml scikit-learn
cat > /etc/systemd/system/llm2-structure-micro.service <<'UNIT'
[Unit]
Description=LLM2 structure_v1 micro-live SHADOW
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
WorkingDirectory=/opt/llm2-structure
Environment=PYTHONPATH=/opt/llm2-structure
Environment=LLM2_INDICATORS_DB=/opt/llm2-structure/pack/indicators_live_slice.sqlite
Environment=TRADING_SECRETS_ENV=/root/.trading/secrets.env
ExecStart=/opt/llm2-structure/venv/bin/python -m llm2.live.micro_runner --pack /opt/llm2-structure/pack --state /opt/llm2-structure/state/micro_live_state.sqlite --mode SHADOW --account Xxobster7 --cert /opt/llm2-structure/structure_v1_lgbm_certificate.yaml
Restart=always
RestartSec=10
StandardOutput=append:/opt/llm2-structure/logs/micro_live.log
StandardError=append:/opt/llm2-structure/logs/micro_live.log

[Install]
WantedBy=multi-user.target
UNIT
systemctl daemon-reload
systemctl enable --now llm2-structure-micro.service
systemctl --no-pager -l status llm2-structure-micro.service | head -25
REMOTE
echo DEPLOY_OK
