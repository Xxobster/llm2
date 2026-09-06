# Start edge lab hunt 003 only after hunt 001's watchdog has finished.
#
# Hunt 003 scores 5-minute arms, whose context (243k 5m bars + 3.4M 1m touch
# rows) needs roughly 2.4 GB. With hunts 001 and 002 already resident there is
# not enough free physical memory to run all three, so this waits instead of
# oversubscribing and thrashing.

[CmdletBinding()]
param(
    [string]$WorkDir = "D:\projects\LLM2",
    [string]$WaitLog = "artifacts\logs\edge_lab_hunt_001_watchdog.log",
    [int]$PollSec = 120,
    [int]$MinFreeGB = 6
)

$ErrorActionPreference = "Stop"
Set-Location $WorkDir

$chainLog = Join-Path $WorkDir "artifacts\logs\edge_lab_hunt_003_chain.log"
function Say([string]$m) {
    $line = "[{0:u}] {1}" -f (Get-Date).ToUniversalTime(), $m
    Add-Content -Path $chainLog -Value $line -Encoding UTF8
    Write-Host $line
}

Say "chain start: waiting for hunt 001 watchdog to end"

$waitPath = Join-Path $WorkDir $WaitLog
while ($true) {
    if (Test-Path -LiteralPath $waitPath) {
        if (Select-String -LiteralPath $waitPath -Pattern "watchdog end" -Quiet) {
            Say "hunt 001 watchdog ended"
            break
        }
    }
    Start-Sleep -Seconds $PollSec
}

# Wait for memory to actually be released before loading a 5m context.
while ($true) {
    $freeGB = [math]::Round((Get-CimInstance Win32_OperatingSystem).FreePhysicalMemory / 1MB, 1)
    if ($freeGB -ge $MinFreeGB) {
        Say "free memory ${freeGB} GB >= ${MinFreeGB} GB, launching hunt 003"
        break
    }
    Say "free memory ${freeGB} GB < ${MinFreeGB} GB, waiting"
    Start-Sleep -Seconds $PollSec
}

& powershell -NoProfile -File (Join-Path $WorkDir "scripts\watchdog_run.ps1") `
    -Command "python -u scripts/run_edge_lab_hunt_003_structure_mtf.py" `
    -WorkDir $WorkDir `
    -LogPath "artifacts/logs/edge_lab_hunt_003_watchdog.log" `
    -PollSec 60 -StallSec 3600 -MaxRestarts 6

Say "chain end exit=$LASTEXITCODE"
exit $LASTEXITCODE
