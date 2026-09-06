# Keep-alive for the multi-day autonomy research loop.
# Stops only when artifacts/autonomy/STOP exists (or -ForceStop).
# Restarts watchdog_run.ps1 if the loop dies or the child log stalls.

[CmdletBinding()]
param(
    [string]$JobName = "autonomy_research_loop_v1",
    [string]$WorkDir = "",
    [int]$PollSec = 60,
    [int]$StallSec = 3600,
    [int]$StartupGraceSec = 180,
    [int]$InnerMaxRestarts = 200
)

$ErrorActionPreference = "Stop"
if (-not $WorkDir) { $WorkDir = (Get-Location).Path }
$WorkDir = (Resolve-Path $WorkDir).Path
Set-Location $WorkDir

$logDir = Join-Path $WorkDir "artifacts\logs"
$autoDir = Join-Path $WorkDir "artifacts\autonomy"
New-Item -ItemType Directory -Path $logDir -Force | Out-Null
New-Item -ItemType Directory -Path $autoDir -Force | Out-Null

$keepLog = Join-Path $logDir "$JobName.keepalive.log"
$lockPath = Join-Path $logDir "$JobName.keepalive.lock"
$watchLog = Join-Path $logDir "${JobName}_watchdog.log"
$stopPath = Join-Path $autoDir "STOP"
$HuntCommand = "python -u scripts/run_autonomous_research_loop.py"
$Needles = @(
    "run_autonomous_research_loop.py",
    "run_autonomy_public_indicator_hunt.py"
)

function Write-Keep([string]$msg) {
    $line = "[{0:u}] {1}" -f (Get-Date).ToUniversalTime(), $msg
    try {
        Add-Content -LiteralPath $keepLog -Value $line -Encoding UTF8 -ErrorAction Stop
    } catch {
        Start-Sleep -Milliseconds 200
        try {
            Add-Content -LiteralPath $keepLog -Value $line -Encoding UTF8 -ErrorAction Stop
        } catch {
            Write-Host $line
        }
    }
}

function Get-MatchingProcesses([string]$needle) {
    Get-CimInstance Win32_Process -ErrorAction SilentlyContinue |
        Where-Object { $_.CommandLine -and ($_.CommandLine -like "*$needle*") }
}

function Get-HuntPython {
    $out = @()
    foreach ($n in $Needles) {
        $out += @(
            Get-MatchingProcesses $n |
                Where-Object {
                    $_.CommandLine -notlike "*keep_alive_autonomy_loop.ps1*" -and
                    $_.CommandLine -notlike "*nurse_autonomy_loop.ps1*" -and
                    $_.CommandLine -notlike "*watchdog_run.ps1*"
                }
        )
    }
    $out | Sort-Object ProcessId -Unique
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
    Write-Keep "starting inner watchdog"
    # Quote -Command: Start-Process otherwise splits on spaces and powershell.exe
    # eats -Command as its own switch (watchdog never stays up).
    $arg = @(
        "-NoProfile",
        "-ExecutionPolicy", "Bypass",
        "-File", $wd,
        "-Command", "`"$HuntCommand`"",
        "-WorkDir", $WorkDir,
        "-LogPath", $watchLog,
        "-PollSec", "$PollSec",
        "-StallSec", "$StallSec",
        "-MaxRestarts", "$InnerMaxRestarts",
        "-StartupGraceSec", "$StartupGraceSec"
    )
    Start-Process -FilePath "powershell.exe" `
        -ArgumentList $arg `
        -WorkingDirectory $WorkDir `
        -WindowStyle Hidden | Out-Null
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
Write-Keep "keep-alive start pid=$myPid job=$JobName stall=${StallSec}s"

$lastBytes = [int64]0
$lastGrowUtc = [DateTime]::UtcNow
$startedUtc = [DateTime]::UtcNow

try {
    while ($true) {
        try {
            if (Test-Path -LiteralPath $stopPath) {
                Write-Keep "STOP file present -- shutting down hunt tree"
                Stop-HuntTree
                exit 0
            }

            $py = @(Get-HuntPython)
            $childLog = Get-LatestChildLog
            $bytes = Get-LogBytes $childLog
            $statusPath = Join-Path $autoDir "STATUS.md"
            $statusMtime = 0
            if (Test-Path -LiteralPath $statusPath) {
                $statusMtime = [int64]((Get-Item -LiteralPath $statusPath).LastWriteTimeUtc - [DateTime]'1970-01-01Z').TotalSeconds
            }
            $activity = $bytes + $statusMtime
            if ($activity -ne $lastBytes) {
                $lastBytes = $activity
                $lastGrowUtc = [DateTime]::UtcNow
            }
            $stallSecNow = ([DateTime]::UtcNow - $lastGrowUtc).TotalSeconds
            $ageSec = ([DateTime]::UtcNow - $startedUtc).TotalSeconds

            if ($py.Count -gt 0) {
                Write-Keep "heartbeat python=$($py.Count) log_bytes=$bytes stall_s=$([int]$stallSecNow)"
                if ($ageSec -ge $StartupGraceSec -and $stallSecNow -ge $StallSec) {
                    Write-Keep "STALL no hunt-log growth for $([int]$stallSecNow)s -- kill and restart"
                    Stop-HuntTree
                    $lastGrowUtc = [DateTime]::UtcNow
                    $startedUtc = [DateTime]::UtcNow
                    Start-InnerWatchdog
                }
            } else {
                $wd = @(Get-InnerWatchdog)
                if ($wd.Count -gt 0) {
                    Write-Keep "python absent but inner watchdog still up pids=$(($wd | ForEach-Object { $_.ProcessId }) -join ',') -- wait"
                } else {
                    Write-Keep "python absent -- start inner watchdog"
                    Start-InnerWatchdog
                    $startedUtc = [DateTime]::UtcNow
                    $lastGrowUtc = [DateTime]::UtcNow
                    Start-Sleep -Seconds 15
                }
            }
        } catch {
            Write-Keep "loop error $($_.Exception.Message) -- continue"
        }
        Start-Sleep -Seconds ([Math]::Max(15, $PollSec))
    }
} finally {
    if ((Test-Path $lockPath) -and ((Get-Content -LiteralPath $lockPath -ErrorAction SilentlyContinue | Select-Object -First 1) -eq "$myPid")) {
        Remove-Item -LiteralPath $lockPath -Force -ErrorAction SilentlyContinue
    }
    Write-Keep "keep-alive end pid=$myPid"
}
