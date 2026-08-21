"""Service stop must flatten LIVE exposure (max-hold is in-process only)."""

from __future__ import annotations

import ast
from pathlib import Path


def test_micro_runner_registers_shutdown_flatten():
    src = Path("llm2/live/micro_runner.py").read_text(encoding="utf-8")
    assert "flatten_symbol_on_shutdown" in src
    assert "SHUTDOWN_FLATTEN" in src
    assert "signal.SIGTERM" in src
    tree = ast.parse(src)
    names = {n.name for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)}
    assert "flatten_symbol_on_shutdown" in names
    assert "sleep_until_next_close" in names
