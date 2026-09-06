# Watchdog for long research / backtest jobs (Windows PowerShell).
#
# Runs a command, polls liveness + child-log growth, restarts on crash or stall.
# Does NOT restart a clean exit (exit code 0).
#
# Example:
#   powershell -NoProfile -File scripts/watchdog_run.ps1 `
#     -Command 'python -u scripts/run_pivot_confirm_fromto_005.py' `
#     -WorkDir 'D:\projects\LLM2' `
#     -LogPath 'artifacts/logs/fleet_005_watchdog.log' `
#     -PollSec 60 -StallSec 1800 -MaxRestarts 3

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string]$Command,

    [string]$WorkDir = "",

    [string]$LogPath = "",

    [int]$PollSec = 60,

    [int]$StallSec = 1800,

    [int]$MaxRestarts = 3,

    [int]$StartupGraceSec = 120,

    [ValidateSet("Normal", "AboveNormal", "High")]
    [string]$ChildPriority = "High",

    [switch]$DemoteOllamaAndPoker
)

$ErrorActionPreference = "Stop"

if (-not $WorkDir) {
    $WorkDir = (Get-Location).Path
}
$WorkDir = (Resolve-Path $WorkDir).Path

if (-not $LogPath) {
    $stamp = Get-Date -Format "yyyyMMddTHHmmss"
    $LogPath = Join-Path $WorkDir "artifacts\logs\watchdog_$stamp.log"
}
if (-not [System.IO.Path]::IsPathRooted($LogPath)) {
    $LogPath = Join-Path $WorkDir $LogPath
}
$logDir = Split-Path -Parent $LogPath
if ($logDir -and -not (Test-Path $logDir)) {
    New-Item -ItemType Directory -Path $logDir -Force | Out-Null
}

function Set-ProcessTreePriority {
    param([int]$RootPid, [string]$Class)
    $q = New-Object System.Collections.Queue
    $q.Enqueue([int]$RootPid)
    while ($q.Count -gt 0) {
        $id = [int]$q.Dequeue()
        try {
            $p = Get-Process -Id $id -ErrorAction SilentlyContinue
            if ($p) { $p.PriorityClass = $Class }
        } catch { }
        Get-CimInstance Win32_Process -Filter "ParentProcessId=$id" -ErrorAction SilentlyContinue |
            ForEach-Object { $q.Enqueue([int]$_.ProcessId) }
    }
}

function Demote-OllamaAndPoker {
    Get-CimInstance Win32_Process -ErrorAction SilentlyContinue | ForEach-Object {
        $blob = ("{0} {1}" -f $_.Name, $_.CommandLine).ToLowerInvariant()
        if ($blob -match "ollama\.exe|llama-server|deskframe\.solver\.train|arena_eval_sim_loop|arena_free_watch|deskframe\.platforms") {
            try {
                $p = Get-Process -Id $_.ProcessId -ErrorAction Stop
                $p.PriorityClass = "BelowNormal"
            } catch { }
        }
    }
}

function Write-Watch([string]$msg) {
    $line = "[{0:u}] {1}" -f (Get-Date).ToUniversalTime(), $msg
    Add-Content -Path $LogPath -Value $line -Encoding UTF8
    Write-Host $line
}

function Get-LogSize([string]$path) {
    if (Test-Path $path) {
        return [int64](Get-Item -LiteralPath $path).Length
    }
    return [int64]0
}

Write-Watch "watchdog start workdir=$WorkDir poll=${PollSec}s stall=${StallSec}s max_restarts=$MaxRestarts"
Write-Watch "command=$Command"

$attempt = 0
$finalExit = 1
$maxAttempts = $MaxRestarts + 1

while ($attempt -lt $maxAttempts) {
    $attempt++
    $childLog = "$LogPath.child$attempt.log"
    if (Test-Path -LiteralPath $childLog) {
        Remove-Item -LiteralPath $childLog -Force
    }
    New-Item -ItemType File -Path $childLog -Force | Out-Null
    Write-Watch "attempt=$attempt/$maxAttempts child_log=$childLog"

    # Run via cmd so PATH / .py association work; redirect all output to child log.
    $arg = "/c $Command > `"$childLog`" 2>&1"
    $proc = Start-Process -FilePath "cmd.exe" `
        -ArgumentList $arg `
        -WorkingDirectory $WorkDir `
        -PassThru `
        -WindowStyle Hidden

    $pidChild = $proc.Id
    Write-Watch "started pid=$pidChild"
    try {
        Set-ProcessTreePriority -RootPid $pidChild -Class $ChildPriority
        Start-Sleep -Seconds 2
        Set-ProcessTreePriority -RootPid $pidChild -Class $ChildPriority
        Write-Watch "child_priority=$ChildPriority"
    } catch {
        Write-Watch "child_priority_failed: $_"
    }
    if ($DemoteOllamaAndPoker) {
        try { Demote-OllamaAndPoker; Write-Watch "demoted ollama/poker to BelowNormal" } catch { }
    }

    $lastBytes = Get-LogSize $childLog
    $lastGrowUtc = [DateTime]::UtcNow
    $startedUtc = [DateTime]::UtcNow
    $reason = ""

    while (-not $proc.HasExited) {
        Start-Sleep -Seconds ([Math]::Max(5, $PollSec))
        if ($proc.HasExited) { break }

        $bytes = Get-LogSize $childLog
        if ($bytes -gt $lastBytes) {
            $lastBytes = $bytes
            $lastGrowUtc = [DateTime]::UtcNow
        }

        $ageSec = ([DateTime]::UtcNow - $startedUtc).TotalSeconds
        $stallSecNow = ([DateTime]::UtcNow - $lastGrowUtc).TotalSeconds
        if ($ageSec -ge $StartupGraceSec -and $stallSecNow -ge $StallSec) {
            $reason = "STALL no log growth for ${StallSec}s (bytes=$bytes)"
            Write-Watch "killing pid=$pidChild reason=$reason"
            try {
                Stop-Process -Id $pidChild -Force -ErrorAction SilentlyContinue
                Get-CimInstance Win32_Process -Filter "ParentProcessId=$pidChild" -ErrorAction SilentlyContinue |
                    ForEach-Object { Stop-Process -Id $_.ProcessId -Force -ErrorAction SilentlyContinue }
            } catch {
                Write-Watch "kill failed: $_"
            }
            Start-Sleep -Seconds 2
            break
        }
    }

    if (-not $proc.HasExited) {
        try { $null = $proc.WaitForExit(15000) } catch { }
    }
    # Refresh exit code
    try { $proc.Refresh() } catch { }
    $code = if ($proc.HasExited) { [int]$proc.ExitCode } else { -1 }
    Write-Watch "pid=$pidChild exited code=$code reason=$(if ($reason) { $reason } else { 'process_exit' })"

    if ($code -eq 0 -and -not $reason) {
        Write-Watch "SUCCESS clean exit"
        $finalExit = 0
        break
    }

    if ($attempt -ge $maxAttempts) {
        Write-Watch "GIVING UP after $attempt attempts last_code=$code"
        $finalExit = if ($code -ne 0) { $code } else { 2 }
        break
    }

    $backoff = [Math]::Min(120, 15 * $attempt)
    Write-Watch "restarting in ${backoff}s"
    Start-Sleep -Seconds $backoff
}

Write-Watch "watchdog end exit=$finalExit"
exit $finalExit
