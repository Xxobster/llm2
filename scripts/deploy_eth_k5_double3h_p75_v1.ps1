# Deploy ETH K5 p75 to 185.203.119.52 / Xxobster3 (Windows OpenSSH).
$ErrorActionPreference = "Stop"
$ROOT = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$VpsHost = if ($env:VPS_HOST) { $env:VPS_HOST } else { "185.203.119.52" }
$ACCOUNT = if ($env:ACCOUNT) { $env:ACCOUNT } else { "Xxobster3" }
$NAME = "eth-k5-double3h-p75-v1"
$LOCAL_PACK = Join-Path $ROOT "artifacts\live_packs\structure_v1_ethusdt_k5_double3h_p75_v1"
$LOCAL_CERT = Join-Path $ROOT "configs\live\structure_v1_ethusdt_k5_double3h_p75_v1_certificate.yaml"
$REMOTE_ROOT = "/opt/llm2-structure-$NAME"
$LN1 = "94.156.189.76"
$UNIT = "llm2-structure-$NAME"
$GITBASH = "C:\Program Files\Git\bin\bash.exe"

Write-Host "== authorize pack locally =="
Set-Location $ROOT
python scripts\authorize_eth_k5_double3h_p75_v1_live.py

Write-Host "== secrets Xxobster3 =="
ssh "root@$VpsHost" "mkdir -p /root/.trading"
ssh "root@$LN1" "grep -E '^Xxobster3_API_(KEY|SECRET)=' /root/.trading/secrets.env" | ssh "root@$VpsHost" "cat > /tmp/x3.env"
ssh "root@$VpsHost" @'
set -e
touch /root/.trading/secrets.env
grep -vE "^Xxobster3_API_(KEY|SECRET)=" /root/.trading/secrets.env > /tmp/secrets.new || true
cat /tmp/x3.env >> /tmp/secrets.new
mv /tmp/secrets.new /root/.trading/secrets.env
chmod 600 /root/.trading/secrets.env
rm -f /tmp/x3.env
grep -E "^Xxobster3_" /root/.trading/secrets.env | sed "s/=.*/=***/"
'@

Write-Host "== bootstrap llm2 =="
ssh "root@$VpsHost" "mkdir -p /opt/llm2-structure/llm2"
# tar over ssh for llm2 tree (no rsync)
& $GITBASH -lc "cd '$($ROOT -replace '\\','/')' && tar -C llm2 -cf - . | ssh root@$VpsHost 'mkdir -p /opt/llm2-structure/llm2 && tar -C /opt/llm2-structure/llm2 -xf -'"

$hasVenv = ssh "root@$VpsHost" "test -x /opt/llm2-structure/venv/bin/python && echo YES || echo NO"
if ($hasVenv -notmatch "YES") {
  Write-Host "copying venv from ln1 (large)..."
  ssh "root@$LN1" "tar -C /opt/llm2-structure -cf - venv" | ssh "root@$VpsHost" "tar -C /opt/llm2-structure -xf -"
}

Write-Host "== pack dirs =="
ssh "root@$VpsHost" "mkdir -p $REMOTE_ROOT/pack $REMOTE_ROOT/state $REMOTE_ROOT/logs && ln -sfn /opt/llm2-structure/venv $REMOTE_ROOT/venv && ln -sfn /opt/llm2-structure/llm2 $REMOTE_ROOT/llm2"

Write-Host "== sync pack =="
& $GITBASH -lc "cd '$($LOCAL_PACK -replace '\\','/')' && tar --exclude='*.sqlite-wal' --exclude='*.sqlite-shm' -cf - . | ssh root@$VpsHost 'rm -rf $REMOTE_ROOT/pack/*; mkdir -p $REMOTE_ROOT/pack; tar -C $REMOTE_ROOT/pack -xf -'"
scp "$LOCAL_CERT" "root@${VpsHost}:${REMOTE_ROOT}/certificate.yaml"

Write-Host "== systemd unit =="
$pypath = "${REMOTE_ROOT}:/opt/llm2-structure:/opt/botsgeneral/packages/tradesim/src:/opt/botsgeneral/packages/leakage/src:/opt/botsgeneral/packages/live_candles/src:/opt/botsgeneral/packages/indicators/src"
$unitBody = @"
[Unit]
Description=LLM2 structure_v1 $NAME micro-live LIVE MIN_EXCHANGE
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
WorkingDirectory=$REMOTE_ROOT
Environment=PYTHONPATH=$pypath
Environment=LLM2_INDICATORS_DB=${REMOTE_ROOT}/pack/indicators_live_slice.sqlite
Environment=LLM2_STRUCTURE_SOURCE=binance
Environment=SHARED_CANDLES_DB=/var/lib/botsgeneral/shared_candles.db
Environment=TRADING_SECRETS_ENV=/root/.trading/secrets.env
Environment=TRADESIM_REQUIRE_UNDER=/opt/botsgeneral/packages/tradesim
ExecStart=${REMOTE_ROOT}/venv/bin/python -m llm2.live.micro_runner --pack ${REMOTE_ROOT}/pack --state ${REMOTE_ROOT}/state/micro_live_state.sqlite --mode LIVE --live-orders --account $ACCOUNT --cert ${REMOTE_ROOT}/certificate.yaml
Restart=always
RestartSec=10
StandardOutput=append:${REMOTE_ROOT}/logs/micro_live.log
StandardError=append:${REMOTE_ROOT}/logs/micro_live.log

[Install]
WantedBy=multi-user.target
"@
$unitBody | ssh "root@$VpsHost" "cat > /etc/systemd/system/$UNIT.service"
ssh "root@$VpsHost" "systemctl daemon-reload; systemctl enable --now $UNIT.service; sleep 3; systemctl is-active $UNIT.service"

Write-Host "== register bots =="
scp (Join-Path $ROOT "scripts\_vps_register_eth_k5_p75_xxobster3.py") "root@${VpsHost}:/tmp/"
ssh "root@$VpsHost" "sed -i 's/\r$//' /tmp/_vps_register_eth_k5_p75_xxobster3.py; /opt/botsgeneral/venv/bin/python /tmp/_vps_register_eth_k5_p75_xxobster3.py"

Write-Host "== collector =="
ssh "root@$VpsHost" @'
set +e
for u in botsgeneral-collector@185.203.119.52.service botsgeneral-collector.service; do
  systemctl enable --now "$u" 2>/dev/null
done
systemctl list-units --all --no-pager | grep -i botsgeneral-collector | head -10
bots discover 2>&1 | head -50
'@

Write-Host "== status =="
ssh "root@$VpsHost" "systemctl is-active $UNIT.service; tail -n 60 $REMOTE_ROOT/logs/micro_live.log; echo '--- bots sitrep ---'; bots sitrep 2>&1 | head -80; echo '--- bots ---'; bots 2>&1 | head -120"

Write-Host "OK: $NAME on ${ACCOUNT}@$VpsHost"
