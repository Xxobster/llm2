# Outer keep-alive for a finite long research job.
#
# Inner scripts/watchdog_run.ps1 restarts the child on crash / log stall, then
# can give up (MaxRestarts). This script:
#   - stays detached from Cursor (launch with Start-Process -WindowStyle Hidden)
#   - never starts a second Python if one matching the hunt script is running
#   - if the child dies, starts watchdog_run.ps1 again (SQLite resume)
#   - if the log freezes with Python still alive, kills that tree then restarts
#   - stops only when hunt.sqlite has PlannedArms rows and Python has exited
#
# Example:
#   powershell -NoProfile -File scripts/keep_alive_long_job.ps1 `
#     -JobName diagonal_sr_hunt_001 `
#     -Command "python -u scripts/run_diagonal_sr_autonomous_hunt_001.py --skip-leakage" `
#     -HuntSqlite artifacts/sqlite/diagonal_sr_autonomous_hunt_001/hunt.sqlite `
#     -PlannedArms 1080

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string]$JobName,

    [Parameter(Mandatory = $false)]
    [string]$HuntCommand = "",

    [string]$HuntCommandFile = "",

    [string]$WorkDir = "",

    [string]$HuntSqlite = "",

    [int]$PlannedArms = 0,

    [int]$PollSec = 60,

    [int]$StallSec = 3600,

    [int]$StartupGraceSec = 180,

    [int]$InnerMaxRestarts = 8,

    [string]$PythonNeedle = "run_diagonal_sr_autonomous_hunt_001.py"
)

$ErrorActionPreference = "Stop"

if ($HuntCommandFile -and (Test-Path -LiteralPath $HuntCommandFile)) {
    $HuntCommand = (Get-Content -LiteralPath $HuntCommandFile -Raw).Trim()
}
if (-not $HuntCommand) {
    throw "HuntCommand is empty (pass -HuntCommandFile to avoid powershell -u parsing)"
}

if (-not $WorkDir) {
    $WorkDir = (Get-Location).Path
}

if (-not $WorkDir) {
    $WorkDir = (Get-Location).Path
}
$WorkDir = (Resolve-Path $WorkDir).Path
Set-Location $WorkDir

$logDir = Join-Path $WorkDir "artifacts\logs"
if (-not (Test-Path $logDir)) {
    New-Item -ItemType Directory -Path $logDir -Force | Out-Null
}

$keepLog = Join-Path $logDir "$JobName.keepalive.log"
$lockPath = Join-Path $logDir "$JobName.keepalive.lock"
$watchLog = Join-Path $logDir "${JobName}_watchdog.log"

function Write-Keep([string]$msg) {
    $line = "[{0:u}] {1}" -f (Get-Date).ToUniversalTime(), $msg
    Add-Content -Path $keepLog -Value $line -Encoding UTF8
}

function Get-MatchingProcesses([string]$needle) {
    Get-CimInstance Win32_Process -ErrorAction SilentlyContinue |
        Where-Object { $_.CommandLine -and ($_.CommandLine -like "*$needle*") }
}

function Get-HuntPython {
    Get-MatchingProcesses $PythonNeedle |
        Where-Object { $_.Name -match "python" }
}

function Get-InnerWatchdog {
    Get-MatchingProcesses "${JobName}_watchdog.log" |
        Where-Object { $_.Name -match "powershell" -and $_.CommandLine -like "*watchdog_run.ps1*" }
}

function Get-LatestChildLog {
    $files = Get-ChildItem -LiteralPath $logDir -Filter "${JobName}_watchdog.log.child*.log" -ErrorAction SilentlyContinue |
        Sort-Object LastWriteTime -Descending
    if ($files) { return $files[0].FullName }
    return $null
}

function Get-LogBytes([string]$path) {
    if ($path -and (Test-Path -LiteralPath $path)) {
        return [int64](Get-Item -LiteralPath $path).Length
    }
    return [int64]0
}

function Get-ArmCount {
    if (-not $HuntSqlite) { return -1 }
    $full = if ([System.IO.Path]::IsPathRooted($HuntSqlite)) { $HuntSqlite } else { Join-Path $WorkDir $HuntSqlite }
    if (-not (Test-Path -LiteralPath $full)) { return 0 }
    $code = "import sqlite3,sys; c=sqlite3.connect(sys.argv[1]); print(c.execute('select count(*) from arms').fetchone()[0])"
    try {
        $out = & python -c $code $full 2>$null
        return [int]($out | Select-Object -Last 1)
    } catch {
        return -1
    }
}

function Get-Planned {
    if ($PlannedArms -gt 0) { return $PlannedArms }
    return 1080
}

function Stop-Tree([int]$TargetPid) {
    if ($TargetPid -le 0) { return }
    Get-CimInstance Win32_Process -Filter "ParentProcessId=$TargetPid" -ErrorAction SilentlyContinue |
        ForEach-Object { Stop-Tree -TargetPid ([int]$_.ProcessId) }
    Stop-Process -Id $TargetPid -Force -ErrorAction SilentlyContinue
}

function Stop-HuntTree {
    Get-HuntPython | ForEach-Object {
        Write-Keep "killing hunt python pid=$($_.ProcessId)"
        Stop-Tree -TargetPid ([int]$_.ProcessId)
    }
    Get-InnerWatchdog | ForEach-Object {
        Write-Keep "killing inner watchdog pid=$($_.ProcessId)"
        Stop-Tree -TargetPid ([int]$_.ProcessId)
    }
    Start-Sleep -Seconds 3
}

function Start-InnerWatchdog {
    $wd = Join-Path $WorkDir "scripts\watchdog_run.ps1"
    Write-Keep "starting inner watchdog HuntCommand=$HuntCommand"
    # Quote so powershell.exe does not steal -u / --flags from the hunt command.
    $quotedCmd = '"{0}"' -f ($HuntCommand.Replace('"', '`"'))
    Start-Process -FilePath "powershell.exe" `
        -ArgumentList @(
            "-NoProfile",
            "-ExecutionPolicy", "Bypass",
            "-File", $wd,
            "-Command", $quotedCmd,
            "-WorkDir", $WorkDir,
            "-LogPath", $watchLog,
            "-PollSec", "$PollSec",
            "-StallSec", "$StallSec",
            "-MaxRestarts", "$InnerMaxRestarts",
            "-StartupGraceSec", "$StartupGraceSec"
        ) `
        -WorkingDirectory $WorkDir `
        -WindowStyle Hidden |
        Out-Null
}

$myPid = $PID
if (Test-Path $lockPath) {
    $old = 0
    try { $old = [int](Get-Content -LiteralPath $lockPath -ErrorAction Stop | Select-Object -First 1) } catch { $old = 0 }
    if ($old -gt 0) {
        $alive = Get-Process -Id $old -ErrorAction SilentlyContinue
        if ($alive) {
            Write-Keep "another keep-alive already running pid=$old -- exit"
            exit 0
        }
    }
}
Set-Content -LiteralPath $lockPath -Value "$myPid" -Encoding ASCII
Write-Keep "keep-alive start pid=$myPid job=$JobName stall=${StallSec}s poll=${PollSec}s"

$planned = Get-Planned
$lastBytes = [int64]0
$lastGrowUtc = [DateTime]::UtcNow
$startedUtc = [DateTime]::UtcNow

try {
    while ($true) {
        $n = Get-ArmCount
        if ($n -ge $planned -and $planned -gt 0) {
            $pyDone = @(Get-HuntPython)
            if ($pyDone.Count -eq 0) {
                Write-Keep "COMPLETE arms=$n planned=$planned python_gone -- stop"
                exit 0
            }
            Write-Keep "arms=$n planned=$planned but python still running -- wait for clean exit"
        }

        $py = @(Get-HuntPython)
        $childLog = Get-LatestChildLog
        $bytes = Get-LogBytes $childLog

        if ($bytes -gt $lastBytes) {
            $lastBytes = $bytes
            $lastGrowUtc = [DateTime]::UtcNow
        }

        $stallSecNow = ([DateTime]::UtcNow - $lastGrowUtc).TotalSeconds
        $ageSec = ([DateTime]::UtcNow - $startedUtc).TotalSeconds

        if ($py.Count -gt 0) {
            if ($ageSec -ge $StartupGraceSec -and $stallSecNow -ge $StallSec) {
                Write-Keep "STALL no log growth for $([int]$stallSecNow)s bytes=$bytes log=$childLog -- kill and restart"
                Stop-HuntTree
                $lastGrowUtc = [DateTime]::UtcNow
                $startedUtc = [DateTime]::UtcNow
                Start-InnerWatchdog
            }
        } else {
            Write-Keep "python absent arms=$n/$planned -- start inner watchdog"
            Start-InnerWatchdog
            $startedUtc = [DateTime]::UtcNow
            $lastGrowUtc = [DateTime]::UtcNow
            Start-Sleep -Seconds 15
        }

        Start-Sleep -Seconds ([Math]::Max(15, $PollSec))
    }
} finally {
    if ((Test-Path $lockPath) -and ((Get-Content $lockPath | Select-Object -First 1) -eq "$myPid")) {
        Remove-Item -LiteralPath $lockPath -Force -ErrorAction SilentlyContinue
    }
    Write-Keep "keep-alive end pid=$myPid"
}
