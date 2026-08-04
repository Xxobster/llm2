"""Forward lockbox seal: no silent Finplot / eval peeks."""

from __future__ import annotations

import pytest

from llm2.evidence.lockbox_guard import (
    CLI_ACCEPT_CONTAMINATE,
    CLI_ACCEPT_FINPLOT,
    require_lockbox_access,
    window_includes_forward_lockbox,
)
from llm2.paths import FORWARD_LOCKBOX_START
from llm2.research_policy import PolicyError


def test_window_includes_lockbox():
    assert window_includes_forward_lockbox(FORWARD_LOCKBOX_START)
    assert window_includes_forward_lockbox("2026-06-01")
    assert not window_includes_forward_lockbox("2025-01-01", "2025-12-01")
    assert window_includes_forward_lockbox("2025-01-01", "2026-06-01")
    assert not window_includes_forward_lockbox("2025-01-01", FORWARD_LOCKBOX_START)


def test_silent_lockbox_refused(tmp_path, monkeypatch):
    log = tmp_path / "peek.jsonl"
    monkeypatch.setenv("LLM2_PEEK_LOG", str(log))
    monkeypatch.delenv("LLM2_I_ACCEPT_LOCKBOX_CONTAMINATION", raising=False)
    monkeypatch.delenv("LLM2_I_ACCEPT_FINPLOT_LOCKBOX", raising=False)
    with pytest.raises(PolicyError, match="sealed"):
        require_lockbox_access(
            experiment_id="unit_silent",
            window_start=FORWARD_LOCKBOX_START,
            purpose="finplot_lockbox_open",
            accepted_contamination=False,
            open_finplot=True,
            accepted_finplot=False,
            path=log,
        )
    assert not log.is_file() or log.read_text(encoding="utf-8").strip() == ""


def test_finplot_refused_without_second_flag(tmp_path, monkeypatch):
    log = tmp_path / "peek.jsonl"
    monkeypatch.setenv("LLM2_PEEK_LOG", str(log))
    monkeypatch.delenv("LLM2_I_ACCEPT_FINPLOT_LOCKBOX", raising=False)
    with pytest.raises(PolicyError, match="Finplot"):
        require_lockbox_access(
            experiment_id="unit_finplot",
            window_start=FORWARD_LOCKBOX_START,
            purpose="finplot_lockbox_open",
            symbols=["ETHUSDT"],
            accepted_contamination=True,
            open_finplot=True,
            accepted_finplot=False,
            path=log,
        )


def test_report_only_accept_logs_peek(tmp_path, monkeypatch):
    log = tmp_path / "peek.jsonl"
    monkeypatch.setenv("LLM2_PEEK_LOG", str(log))
    rec = require_lockbox_access(
        experiment_id="unit_report",
        window_start=FORWARD_LOCKBOX_START,
        purpose="lockbox_report_only",
        symbols=["BNBUSDT"],
        accepted_contamination=True,
        open_finplot=False,
        accepted_finplot=False,
        path=log,
        window_end="2026-08-02",
    )
    assert rec is not None
    assert rec["evidence_class"] == "LOCKBOX_OPENED_CONTAMINATED"
    assert "unit_report" in log.read_text(encoding="utf-8")


def test_finplot_with_dual_accept(tmp_path, monkeypatch):
    log = tmp_path / "peek.jsonl"
    monkeypatch.setenv("LLM2_PEEK_LOG", str(log))
    rec = require_lockbox_access(
        experiment_id="unit_dual",
        window_start=FORWARD_LOCKBOX_START,
        purpose="finplot_lockbox_open",
        accepted_contamination=True,
        open_finplot=True,
        accepted_finplot=True,
        path=log,
    )
    assert rec is not None
    assert rec["extra"]["open_finplot"] is True


def test_pre_lockbox_window_no_gate():
    assert (
        require_lockbox_access(
            experiment_id="unit_pre",
            window_start="2024-01-01",
            window_end="2025-10-01",
            purpose="outer_fold",
            accepted_contamination=False,
        )
        is None
    )


def test_cli_flag_names_stable():
    assert CLI_ACCEPT_CONTAMINATE == "--i-accept-lockbox-contamination"
    assert CLI_ACCEPT_FINPLOT == "--i-accept-finplot-lockbox"
