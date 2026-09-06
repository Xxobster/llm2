"""Windows process priority: LLM2 research above Ollama and poker trainers."""

from __future__ import annotations

import ctypes
import sys
from typing import Iterable

HIGH_PRIORITY_CLASS = 0x00000080
ABOVE_NORMAL_PRIORITY_CLASS = 0x00008000
BELOW_NORMAL_PRIORITY_CLASS = 0x00004000
IDLE_PRIORITY_CLASS = 0x00000040

_COMPETITOR_NEEDLES = (
    "ollama.exe",
    "llama-server",
    "deskframe.solver.train",
    "arena_eval_sim_loop",
    "arena_free_watch",
    "deskframe.platforms",
)


def raise_current_process(*, high: bool = True) -> str:
    """Raise this Python process so research wins CPU against Ollama / poker."""
    if sys.platform != "win32":
        return "skip_non_windows"
    kernel32 = ctypes.windll.kernel32
    flag = HIGH_PRIORITY_CLASS if high else ABOVE_NORMAL_PRIORITY_CLASS
    ok = bool(kernel32.SetPriorityClass(kernel32.GetCurrentProcess(), flag))
    return "HIGH" if ok and high else ("ABOVE_NORMAL" if ok else "FAILED")


def _set_pid_class(pid: int, flag: int) -> bool:
    if sys.platform != "win32" or pid <= 0:
        return False
    kernel32 = ctypes.windll.kernel32
    PROCESS_SET_INFORMATION = 0x0200
    handle = kernel32.OpenProcess(PROCESS_SET_INFORMATION, False, int(pid))
    if not handle:
        return False
    try:
        return bool(kernel32.SetPriorityClass(handle, int(flag)))
    finally:
        kernel32.CloseHandle(handle)


def demote_competitors(pids: Iterable[int] | None = None) -> list[int]:
    """Best-effort: set Ollama / poker trainer processes to Below Normal."""
    if sys.platform != "win32":
        return []
    changed: list[int] = []
    if pids is None:
        pids = _competitor_pids()
    for pid in pids:
        if _set_pid_class(int(pid), BELOW_NORMAL_PRIORITY_CLASS):
            changed.append(int(pid))
    return changed


def _competitor_pids() -> list[int]:
    try:
        import subprocess

        raw = subprocess.check_output(
            [
                "powershell",
                "-NoProfile",
                "-Command",
                "Get-CimInstance Win32_Process | "
                "Select-Object ProcessId,Name,CommandLine | ConvertTo-Json -Compress",
            ],
            text=True,
            timeout=20,
        )
    except Exception:  # noqa: BLE001
        return []
    import json

    rows = json.loads(raw or "[]")
    if isinstance(rows, dict):
        rows = [rows]
    out: list[int] = []
    for row in rows:
        blob = f"{row.get('Name') or ''} {row.get('CommandLine') or ''}".lower()
        if any(n in blob for n in _COMPETITOR_NEEDLES):
            out.append(int(row["ProcessId"]))
    return out
