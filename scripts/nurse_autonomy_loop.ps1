# Outer nurse: if keep-alive dies, start it again. Never starts a second hunt
# while any autonomy python/cmd is already running. Honors artifacts/autonomy/STOP.

[CmdletBinding()]
param(
    [string]$WorkDir = "D:\projects\LLM2",
    [int]$PollSec = 45
)

$ErrorActionPreference = "Stop"
$WorkDir = (Resolve-Path $WorkDir).Path
Set-Location $WorkDir

$logDir = Join-Path $WorkDir "artifacts\logs"
$autoDir = Join-Path $WorkDir "artifacts\autonomy"
New-Item -ItemType Directory -Path $logDir -Force | Out-Null
New-Item -ItemType Directory -Path $autoDir -Force | Out-Null

$nurseLog = Join-Path $logDir "autonomy_nurse.log"
$keepScript = Join-Path $WorkDir "scripts\keep_alive_autonomy_loop.ps1"
$lockPath = Join-Path $logDir "autonomy_research_loop_v1.keepalive.lock"
$stopPath = Join-Path $autoDir "STOP"

function Write-Nurse([string]$msg) {
    $line = "[{0:u}] {1}" -f (Get-Date).ToUniversalTime(), $msg
    try {
        Add-Content -LiteralPath $nurseLog -Value $line -Encoding UTF8 -ErrorAction Stop
    } catch {
        Start-Sleep -Milliseconds 200
        try {
            Add-Content -LiteralPath $nurseLog -Value $line -Encoding UTF8 -ErrorAction Stop
        } catch {
            Write-Host $line
        }
    }
}

function Test-KeepAliveAlive {
    if (-not (Test-Path $lockPath)) { return $false }
    $old = 0
    try { $old = [int](Get-Content -LiteralPath $lockPath -ErrorAction Stop | Select-Object -First 1) } catch { return $false }
    if ($old -le 0) { return $false }
    return [bool](Get-Process -Id $old -ErrorAction SilentlyContinue)
}

function Test-HuntAlive {
    $hits = Get-CimInstance Win32_Process -ErrorAction SilentlyContinue |
        Where-Object {
            $_.CommandLine -and (
                $_.CommandLine -like "*run_autonomous_research_loop.py*" -or
                $_.CommandLine -like "*run_autonomy_public_indicator_hunt.py*"
            ) -and
            $_.CommandLine -notlike "*nurse_autonomy_loop.ps1*" -and
            $_.CommandLine -notlike "*keep_alive_autonomy_loop.ps1*"
        }
    return @($hits).Count -gt 0
}

Write-Nurse "nurse start pid=$PID poll=${PollSec}s"

while ($true) {
    if (Test-Path -LiteralPath $stopPath) {
        Write-Nurse "STOP present -- nurse idle (does not kill hunt; keep-alive will stop it)"
        Start-Sleep -Seconds ([Math]::Max(30, $PollSec))
        continue
    }
    $keep = Test-KeepAliveAlive
    $hunt = Test-HuntAlive
    if ($hunt) {
        $prevErr = $ErrorActionPreference
        $ErrorActionPreference = "Continue"
        $freezeOut = & python -u (Join-Path $WorkDir "scripts\freeze_next_autonomy_public_windows.py") --ensure-remaining 12 --batch 8 2>&1 | Out-String
        $freezeCode = $LASTEXITCODE
        $ErrorActionPreference = $prevErr
        if ($freezeCode -ne 0) {
            Write-Nurse "auto-freeze exited $freezeCode $freezeOut"
        } elseif ($freezeOut -match "auto-froze") {
            Write-Nurse $freezeOut.Trim()
        }
    }
    if (-not $keep) {
        Write-Nurse "keep-alive dead hunt_alive=$hunt -- starting keep-alive"
        Start-Process -FilePath "powershell.exe" `
            -ArgumentList @(
                "-NoProfile", "-ExecutionPolicy", "Bypass",
                "-File", $keepScript,
                "-WorkDir", $WorkDir,
                "-StallSec", "1800",
                "-PollSec", "60",
                "-InnerMaxRestarts", "200"
            ) `
            -WorkingDirectory $WorkDir `
            -WindowStyle Hidden | Out-Null
        Start-Sleep -Seconds 20
    }
    Start-Sleep -Seconds ([Math]::Max(15, $PollSec))
}
