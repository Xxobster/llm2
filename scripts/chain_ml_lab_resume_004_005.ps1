# Sequential resume jobs: nested settle 004 (frozen EMA-stack), then hunt 005.
# Do not overlap 1-minute touch loads with other tradesim jobs on a tight RAM box.

[CmdletBinding()]
param(
    [string]$WorkDir = "D:\projects\LLM2",
    [int]$MinFreeGB = 1
)

$ErrorActionPreference = "Stop"
Set-Location $WorkDir

$logDir = Join-Path $WorkDir "artifacts\logs"
New-Item -ItemType Directory -Path $logDir -Force | Out-Null
$chainLog = Join-Path $logDir "ml_lab_resume_004_005_chain.log"
$py = Join-Path $WorkDir ".venv\Scripts\python.exe"
if (-not (Test-Path $py)) { $py = "python" }

function Say([string]$m) {
    $line = "[{0:u}] {1}" -f (Get-Date).ToUniversalTime(), $m
    Add-Content -Path $chainLog -Value $line -Encoding UTF8
    Write-Host $line
}

function Wait-FreeRam {
    while ($true) {
        $freeGB = [math]::Round((Get-CimInstance Win32_OperatingSystem).FreePhysicalMemory / 1MB, 1)
        if ($freeGB -ge $MinFreeGB) {
            Say "free memory ${freeGB} GB >= ${MinFreeGB} GB"
            return
        }
        Say "free memory ${freeGB} GB < ${MinFreeGB} GB, waiting 60s"
        Start-Sleep -Seconds 60
    }
}

$wd = Join-Path $WorkDir "scripts\watchdog_run.ps1"

Say "chain start: settle 004 then hunt 005"
Wait-FreeRam

Say "launch nested settle 004"
& powershell -NoProfile -ExecutionPolicy Bypass -File $wd `
    -Command "$py -u scripts/run_ml_lab_nested_settle_004_ema_stack.py" `
    -WorkDir $WorkDir `
    -LogPath (Join-Path $logDir "ml_lab_nested_settle_004_watchdog.log") `
    -PollSec 60 -StallSec 7200 -MaxRestarts 3 -StartupGraceSec 180 `
    -ChildPriority High -DemoteOllamaAndPoker
Say "settle 004 watchdog exit=$LASTEXITCODE"

Wait-FreeRam
Say "launch hunt 005"
& powershell -NoProfile -ExecutionPolicy Bypass -File $wd `
    -Command "$py -u scripts/run_ml_lab_hunt_005_orb_structure.py" `
    -WorkDir $WorkDir `
    -LogPath (Join-Path $logDir "ml_lab_hunt_005_watchdog.log") `
    -PollSec 60 -StallSec 7200 -MaxRestarts 3 -StartupGraceSec 180 `
    -ChildPriority High -DemoteOllamaAndPoker
Say "hunt 005 watchdog exit=$LASTEXITCODE"
Say "chain end"
exit $LASTEXITCODE
