# Start the hunt 002 nested outer out-of-sample settle after hunt 003 finishes.
#
# The settle builds 15-minute contexts (150k bars plus their 1-minute touch
# windows), which is the heaviest context in the lab. Hunt 003 is resident and
# free physical memory is around 7 GB, so this waits rather than oversubscribing.

[CmdletBinding()]
param(
    [string]$WorkDir = "D:\projects\LLM2",
    [string]$WaitLog = "artifacts\logs\edge_lab_hunt_003_watchdog.log",
    [int]$PollSec = 120,
    [int]$MinFreeGB = 10
)

$ErrorActionPreference = "Stop"
Set-Location $WorkDir

$chainLog = Join-Path $WorkDir "artifacts\logs\edge_lab_settle_002_chain.log"
function Say([string]$m) {
    $line = "[{0:u}] {1}" -f (Get-Date).ToUniversalTime(), $m
    Add-Content -Path $chainLog -Value $line -Encoding UTF8
    Write-Host $line
}

Say "chain start: waiting for hunt 003 watchdog to end"

$waitPath = Join-Path $WorkDir $WaitLog
while ($true) {
    if (Test-Path -LiteralPath $waitPath) {
        if (Select-String -LiteralPath $waitPath -Pattern "watchdog end" -Quiet) {
            Say "hunt 003 watchdog ended"
            break
        }
    }
    Start-Sleep -Seconds $PollSec
}

while ($true) {
    $freeGB = [math]::Round((Get-CimInstance Win32_OperatingSystem).FreePhysicalMemory / 1MB, 1)
    if ($freeGB -ge $MinFreeGB) {
        Say "free memory ${freeGB} GB >= ${MinFreeGB} GB, launching settle 002"
        break
    }
    Say "free memory ${freeGB} GB < ${MinFreeGB} GB, waiting"
    Start-Sleep -Seconds $PollSec
}

& powershell -NoProfile -File (Join-Path $WorkDir "scripts\watchdog_run.ps1") `
    -Command "python -u scripts/run_edge_lab_nested_settle_002_atr.py" `
    -WorkDir $WorkDir `
    -LogPath "artifacts/logs/edge_lab_settle_002_watchdog.log" `
    -PollSec 60 -StallSec 3600 -MaxRestarts 4

Say "chain end exit=$LASTEXITCODE"
exit $LASTEXITCODE
