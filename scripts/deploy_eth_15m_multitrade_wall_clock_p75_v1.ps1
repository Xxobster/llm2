# Deploy ETH 15m multitrade wall-clock p75 to 185.203.119.52 / Xxobster11 (Windows).
$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
if (-not (Test-Path (Join-Path $Root "llm2"))) { $Root = (Get-Location).Path }
$HostName = if ($env:HOST) { $env:HOST } else { "185.203.119.52" }
$Account = if ($env:ACCOUNT) { $env:ACCOUNT } else { "Xxobster11" }
$Name = "eth-15m-multitrade-wall-clock-p75-v1"
$LocalPack = Join-Path $Root "artifacts\live_packs\structure_v1_ethusdt_15m_multitrade_wall_clock_p75_v1"
$LocalCert = Join-Path $Root "configs\live\structure_v1_ethusdt_15m_multitrade_wall_clock_p75_v1_certificate.yaml"
$RemoteRoot = "/opt/llm2-structure-$Name"
$Ln1 = if ($env:LN1) { $env:LN1 } else { "94.156.189.76" }
$Unit = "llm2-structure-$Name"

Write-Host "== authorize pack locally =="
python (Join-Path $Root "scripts\authorize_eth_15m_multitrade_wall_clock_p75_v1_live.py")
if ($LASTEXITCODE -ne 0) { throw "authorize failed" }

Write-Host "== ensure secrets Xxobster11 on $HostName =="
ssh "root@$HostName" "mkdir -p /root/.trading"
ssh "root@$Ln1" "grep -E '^Xxobster11_API_(KEY|SECRET)=' /root/.trading/secrets.env" |
  ssh "root@$HostName" "cat > /tmp/x11.env"
ssh "root@$HostName" @'
set -e
touch /root/.trading/secrets.env
grep -vE "^Xxobster11_API_(KEY|SECRET)=" /root/.trading/secrets.env > /tmp/secrets.new || true
cat /tmp/x11.env >> /tmp/secrets.new
mv /tmp/secrets.new /root/.trading/secrets.env
chmod 600 /root/.trading/secrets.env
rm -f /tmp/x11.env
grep -E "^Xxobster(3|9|11)_" /root/.trading/secrets.env | sed "s/=.*/=***/"
'@

Write-Host "== bootstrap llm2 code =="
ssh "root@$HostName" "mkdir -p /opt/llm2-structure/llm2"
$tmpTar = Join-Path $env:TEMP "llm2_code_deploy.tgz"
if (Test-Path $tmpTar) { Remove-Item $tmpTar -Force }
Push-Location (Join-Path $Root "llm2")
try {
  tar -czf $tmpTar --exclude=__pycache__ --exclude=*.pyc .
} finally { Pop-Location }
scp $tmpTar "root@${HostName}:/tmp/llm2_code.tgz"
ssh "root@$HostName" "rm -rf /opt/llm2-structure/llm2/*; tar -C /opt/llm2-structure/llm2 -xzf /tmp/llm2_code.tgz; rm -f /tmp/llm2_code.tgz"

$venvOk = ssh "root@$HostName" "test -x /opt/llm2-structure/venv/bin/python && echo YES || echo NO"
if ($venvOk.Trim() -ne "YES") {
  Write-Host "copying venv from ln1..."
  ssh "root@$Ln1" "tar -C /opt/llm2-structure -cf - venv" | ssh "root@$HostName" "tar -C /opt/llm2-structure -xf -"
}

Write-Host "== deploy pack + unit =="
ssh "root@$HostName" "mkdir -p $RemoteRoot/{pack,state,logs} && ln -sfn /opt/llm2-structure/venv $RemoteRoot/venv && ln -sfn /opt/llm2-structure/llm2 $RemoteRoot/llm2"
$packTar = Join-Path $env:TEMP "llm2_15m_pack.tgz"
if (Test-Path $packTar) { Remove-Item $packTar -Force }
Push-Location $LocalPack
try {
  tar -czf $packTar --exclude=*.sqlite-wal --exclude=*.sqlite-shm .
} finally { Pop-Location }
scp $packTar "root@${HostName}:/tmp/pack15m.tgz"
scp $LocalCert "root@${HostName}:${RemoteRoot}/certificate.yaml"
ssh "root@$HostName" "rm -rf $RemoteRoot/pack/*; tar -C $RemoteRoot/pack -xzf /tmp/pack15m.tgz; rm -f /tmp/pack15m.tgz"

$pyPath = "${RemoteRoot}:/opt/llm2-structure:/opt/botsgeneral/packages/tradesim/src:/opt/botsgeneral/packages/leakage/src:/opt/botsgeneral/packages/live_candles/src:/opt/botsgeneral/packages/indicators/src"
$unitFile = @"
[Unit]
Description=LLM2 structure_v1 $Name micro-live LIVE MIN_EXCHANGE
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
WorkingDirectory=$RemoteRoot
Environment=PYTHONPATH=$pyPath
Environment=LLM2_INDICATORS_DB=${RemoteRoot}/pack/indicators_live_slice.sqlite
Environment=LLM2_STRUCTURE_SOURCE=binance
Environment=SHARED_CANDLES_DB=/var/lib/botsgeneral/shared_candles.db
Environment=TRADING_SECRETS_ENV=/root/.trading/secrets.env
Environment=TRADESIM_REQUIRE_UNDER=/opt/botsgeneral/packages/tradesim
ExecStart=${RemoteRoot}/venv/bin/python -m llm2.live.micro_runner --pack ${RemoteRoot}/pack --state ${RemoteRoot}/state/micro_live_state.sqlite --mode LIVE --live-orders --account $Account --cert ${RemoteRoot}/certificate.yaml
Restart=always
RestartSec=10
StandardOutput=append:${RemoteRoot}/logs/micro_live.log
StandardError=append:${RemoteRoot}/logs/micro_live.log

[Install]
WantedBy=multi-user.target
"@
$unitFile = $unitFile -replace "`r`n", "`n"
$unitB64 = [Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes($unitFile))
ssh "root@$HostName" "echo $unitB64 | base64 -d > /etc/systemd/system/$Unit.service && systemctl daemon-reload && systemctl enable --now $Unit.service && sleep 4 && systemctl is-active $Unit.service"

Write-Host "== restart sibling llm2 units (code HTF fix) =="
ssh "root@$HostName" @"
systemctl restart llm2-structure-eth-k5-double3h-p75-v1.service || true
systemctl restart llm2-structure-eth-multitrade-p75-v1.service || true
sleep 2
systemctl is-active llm2-structure-eth-k5-double3h-p75-v1.service
systemctl is-active llm2-structure-eth-multitrade-p75-v1.service
systemctl is-active $Unit.service
"@

Write-Host "== register bots + report.yaml =="
scp (Join-Path $Root "scripts\_vps_register_llm2_units_185.py") "root@${HostName}:/tmp/_vps_register_llm2_units_185.py"
ssh "root@$HostName" "sed -i 's/\r`$//' /tmp/_vps_register_llm2_units_185.py; /opt/botsgeneral/venv/bin/python /tmp/_vps_register_llm2_units_185.py"
$reportYaml = @"
# Phone-friendly report settings — 185.203.119.52
since_date: `"2026-07-09`"

# Show every account that has a running bot on this VPS.
accounts:
  - Xxobster3
  - Xxobster9
  - Xxobster11

since_by_bot: {}
"@
$reportYaml = $reportYaml -replace "`r`n", "`n"
$repB64 = [Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes($reportYaml))
ssh "root@$HostName" "echo $repB64 | base64 -d > /etc/botsgeneral/report.yaml; cat /etc/botsgeneral/report.yaml"

Write-Host "== collector / discover =="
ssh "root@$HostName" @"
systemctl enable --now botsgeneral-collector@185.203.119.52.service 2>/dev/null || true
systemctl is-active botsgeneral-collector@185.203.119.52.service
bots discover 2>&1 | head -80
"@

Write-Host "== status =="
ssh "root@$HostName" @"
systemctl is-active $Unit.service
tail -n 100 $RemoteRoot/logs/micro_live.log || true
echo '--- bots sitrep ---'
bots sitrep 2>&1 | head -140
echo '--- bots ---'
bots 2>&1 | head -180
"@

Write-Host "OK: $Name on ${Account}@${HostName}"
