#!/usr/bin/env bash
# Deploy ETH 15m multitrade wall-clock p75 to 185.203.119.52 / Xxobster11.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
HOST="${HOST:-185.203.119.52}"
ACCOUNT="${ACCOUNT:-Xxobster11}"
NAME="eth-15m-multitrade-wall-clock-p75-v1"
LOCAL_PACK="${ROOT}/artifacts/live_packs/structure_v1_ethusdt_15m_multitrade_wall_clock_p75_v1"
LOCAL_CERT="${ROOT}/configs/live/structure_v1_ethusdt_15m_multitrade_wall_clock_p75_v1_certificate.yaml"
REMOTE_ROOT="/opt/llm2-structure-${NAME}"
LN1="${LN1:-94.156.189.76}"
UNIT="llm2-structure-${NAME}"

echo "== authorize pack locally =="
python "${ROOT}/scripts/authorize_eth_15m_multitrade_wall_clock_p75_v1_live.py"

echo "== ensure secrets Xxobster11 on ${HOST} =="
ssh "root@${HOST}" "mkdir -p /root/.trading"
ssh "root@${LN1}" "grep -E '^Xxobster11_API_(KEY|SECRET)=' /root/.trading/secrets.env" \
  | ssh "root@${HOST}" "cat > /tmp/x11.env"
ssh "root@${HOST}" 'set -e
  touch /root/.trading/secrets.env
  grep -vE "^Xxobster11_API_(KEY|SECRET)=" /root/.trading/secrets.env > /tmp/secrets.new || true
  cat /tmp/x11.env >> /tmp/secrets.new
  mv /tmp/secrets.new /root/.trading/secrets.env
  chmod 600 /root/.trading/secrets.env
  rm -f /tmp/x11.env
  grep -E "^Xxobster(3|9|11)_" /root/.trading/secrets.env | sed "s/=.*/=***/"
'

echo "== bootstrap llm2 code (HTF fix for 15m) =="
ssh "root@${HOST}" "mkdir -p /opt/llm2-structure"
rsync -az --delete \
  --exclude '__pycache__' --exclude '*.pyc' --exclude '.git' \
  "${ROOT}/llm2/" "root@${HOST}:/opt/llm2-structure/llm2/"

if ! ssh "root@${HOST}" "test -x /opt/llm2-structure/venv/bin/python"; then
  echo "copying venv from ln1..."
  ssh "root@${LN1}" "tar -C /opt/llm2-structure -cf - venv" \
    | ssh "root@${HOST}" "tar -C /opt/llm2-structure -xf -"
fi

echo "== deploy pack + unit =="
HOST="$HOST" ACCOUNT="$ACCOUNT" \
  bash "${ROOT}/scripts/_deploy_symbol_micro.sh" \
    "$NAME" "$LOCAL_PACK" "$LOCAL_CERT" "$REMOTE_ROOT"

echo "== patch unit PYTHONPATH + tradesim =="
scp "${ROOT}/scripts/_vps185_patch_15m_mt_p75_unit.py" "root@${HOST}:/tmp/"
ssh "root@${HOST}" "sed -i 's/\r$//' /tmp/_vps185_patch_15m_mt_p75_unit.py; python3 /tmp/_vps185_patch_15m_mt_p75_unit.py; systemctl daemon-reload; systemctl restart ${UNIT}.service; sleep 4; systemctl is-active ${UNIT}.service"

echo "== restart sibling llm2 units to pick up code HTF fix =="
ssh "root@${HOST}" "
  systemctl restart llm2-structure-eth-k5-double3h-p75-v1.service || true
  systemctl restart llm2-structure-eth-multitrade-p75-v1.service || true
  sleep 2
  systemctl is-active llm2-structure-eth-k5-double3h-p75-v1.service
  systemctl is-active llm2-structure-eth-multitrade-p75-v1.service
  systemctl is-active ${UNIT}.service
"

echo "== register all llm2 units in bots_registry + report accounts =="
scp "${ROOT}/scripts/_vps_register_llm2_units_185.py" "root@${HOST}:/tmp/"
ssh "root@${HOST}" "sed -i 's/\r$//' /tmp/_vps_register_llm2_units_185.py; /opt/botsgeneral/venv/bin/python /tmp/_vps_register_llm2_units_185.py"
ssh "root@${HOST}" 'cat > /etc/botsgeneral/report.yaml' <<'EOF'
# Phone-friendly report settings — 185.203.119.52
since_date: "2026-07-09"

# Empty allowlist = show every account that has a running bot on this VPS.
# Explicit list kept as documentation of intended live accounts.
accounts:
  - Xxobster3
  - Xxobster9
  - Xxobster11

since_by_bot: {}
EOF

echo "== collector discover (need ETH 15m + 1m) =="
ssh "root@${HOST}" 'bash -s' <<'EOS'
set +e
systemctl enable --now botsgeneral-collector@185.203.119.52.service 2>/dev/null
systemctl is-active botsgeneral-collector@185.203.119.52.service
bots discover 2>&1 | head -60
EOS

echo "== status =="
ssh "root@${HOST}" "
  systemctl is-active ${UNIT}.service
  tail -n 80 ${REMOTE_ROOT}/logs/micro_live.log || true
  echo '--- bots sitrep ---'
  bots sitrep 2>&1 | head -120
  echo '--- bots ---'
  bots 2>&1 | head -160
"

echo "OK: ${NAME} on ${ACCOUNT}@${HOST}"
