# Launch hunt 003 nested settle once there is enough free memory.
# 5-minute contexts plus 1-minute touch windows are the heavy part.

[CmdletBinding()]
param(
    [string]$WorkDir = "D:\projects\LLM2",
    [int]$PollSec = 60,
    [int]$MinFreeGB = 10
)

$ErrorActionPreference = "Stop"
Set-Location $WorkDir
$chainLog = Join-Path $WorkDir "artifacts\logs\edge_lab_settle_003_chain.log"
function Say([string]$m) {
    $line = "[{0:u}] {1}" -f (Get-Date).ToUniversalTime(), $m
    Add-Content -Path $chainLog -Value $line -Encoding UTF8
    Write-Host $line
}

Say "chain start: waiting for ${MinFreeGB} GB free"
while ($true) {
    $freeGB = [math]::Round((Get-CimInstance Win32_OperatingSystem).FreePhysicalMemory / 1MB, 1)
    if ($freeGB -ge $MinFreeGB) {
        Say "free memory ${freeGB} GB >= ${MinFreeGB} GB, launching settle 003"
        break
    }
    Say "free memory ${freeGB} GB < ${MinFreeGB} GB, waiting"
    Start-Sleep -Seconds $PollSec
}

& powershell -NoProfile -File (Join-Path $WorkDir "scripts\watchdog_run.ps1") `
    -Command "python -u scripts/run_edge_lab_nested_settle_003_structure_mtf.py" `
    -WorkDir $WorkDir `
    -LogPath "artifacts/logs/edge_lab_settle_003_watchdog.log" `
    -PollSec 60 -StallSec 3600 -MaxRestarts 4

Say "chain end exit=$LASTEXITCODE"
exit $LASTEXITCODE
