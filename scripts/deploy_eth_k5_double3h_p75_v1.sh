#!/usr/bin/env bash
# Deploy ETH K5 p75 to 185.203.119.52 / Xxobster3.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
HOST="${HOST:-185.203.119.52}"
ACCOUNT="${ACCOUNT:-Xxobster3}"
NAME="eth-k5-double3h-p75-v1"
LOCAL_PACK="${ROOT}/artifacts/live_packs/structure_v1_ethusdt_k5_double3h_p75_v1"
LOCAL_CERT="${ROOT}/configs/live/structure_v1_ethusdt_k5_double3h_p75_v1_certificate.yaml"
REMOTE_ROOT="/opt/llm2-structure-${NAME}"
LN1="${LN1:-94.156.189.76}"
UNIT="llm2-structure-${NAME}"

echo "== authorize pack locally =="
python "${ROOT}/scripts/authorize_eth_k5_double3h_p75_v1_live.py"

echo "== ensure secrets Xxobster3 on ${HOST} =="
ssh "root@${HOST}" "mkdir -p /root/.trading"
ssh "root@${LN1}" "grep -E '^Xxobster3_API_(KEY|SECRET)=' /root/.trading/secrets.env" \
  | ssh "root@${HOST}" "cat > /tmp/x3.env"
ssh "root@${HOST}" 'set -e
  touch /root/.trading/secrets.env
  grep -vE "^Xxobster3_API_(KEY|SECRET)=" /root/.trading/secrets.env > /tmp/secrets.new || true
  cat /tmp/x3.env >> /tmp/secrets.new
  mv /tmp/secrets.new /root/.trading/secrets.env
  chmod 600 /root/.trading/secrets.env
  rm -f /tmp/x3.env
  grep -E "^Xxobster3_" /root/.trading/secrets.env | sed "s/=.*/=***/"
'

echo "== bootstrap llm2 code =="
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

echo "== patch unit PYTHONPATH =="
scp "${ROOT}/scripts/_vps185_patch_p75_unit.py" "root@${HOST}:/tmp/"
ssh "root@${HOST}" "sed -i 's/\r$//' /tmp/_vps185_patch_p75_unit.py; python3 /tmp/_vps185_patch_p75_unit.py; systemctl daemon-reload; systemctl restart ${UNIT}.service; sleep 3; systemctl is-active ${UNIT}.service"

echo "== register bots =="
scp "${ROOT}/scripts/_vps_register_eth_k5_p75_xxobster3.py" "root@${HOST}:/tmp/"
ssh "root@${HOST}" "sed -i 's/\r$//' /tmp/_vps_register_eth_k5_p75_xxobster3.py; /opt/botsgeneral/venv/bin/python /tmp/_vps_register_eth_k5_p75_xxobster3.py"

echo "== collector / discover =="
ssh "root@${HOST}" 'bash -s' <<'EOS'
set +e
for u in botsgeneral-collector@185.203.119.52.service botsgeneral-collector.service; do
  systemctl enable --now "$u" 2>/dev/null
done
systemctl list-units --all --no-pager | grep -i botsgeneral-collector | head -10
bots discover 2>&1 | head -40
EOS

echo "== status =="
ssh "root@${HOST}" "
  systemctl is-active ${UNIT}.service
  tail -n 50 ${REMOTE_ROOT}/logs/micro_live.log || true
  echo '--- bots sitrep ---'
  bots sitrep 2>&1 | head -80
  echo '--- bots ---'
  bots 2>&1 | head -100
"

echo "OK: ${NAME} on ${ACCOUNT}@${HOST}"
