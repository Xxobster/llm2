"""Tests for live pack version registry."""

from __future__ import annotations

import json
from pathlib import Path

from llm2.evidence.pack_registry import (
    ensure_registry_schema,
    open_pack_run,
    register_freeze,
    regenerate_versions_md,
)
from llm2.registry.db import ResearchDB


def test_schema_creates_live_pack_versions(tmp_path: Path):
    db_path = tmp_path / "research.sqlite"
    ResearchDB(path=db_path)
    with ResearchDB(path=db_path)._connect() as conn:
        names = {
            r[0]
            for r in conn.execute(
                "SELECT name FROM sqlite_master WHERE type='table'"
            ).fetchall()
        }
    assert "live_pack_versions" in names


def test_register_freeze_fail_closed_without_run_id(tmp_path: Path, monkeypatch):
    pack = tmp_path / "structure_v1_testpack_v1"
    pack.mkdir()
    (pack / "strategy.json").write_text(
        json.dumps({"version_id": "testpack_v1", "strategy_id": "test"}),
        encoding="utf-8",
    )
    from llm2.evidence.four_proof import PROOF_KEYS

    (pack / "pack_meta.json").write_text(
        json.dumps(
            {
                "version_id": "testpack_v1",
                "status": "FROZEN",
                "four_proof_ok": True,
                "evidence": {
                    "four_proof_ok": True,
                    "four_proof_hashes": {k: "a" * 64 for k in PROOF_KEYS},
                },
            }
        ),
        encoding="utf-8",
    )
    db_path = tmp_path / "research.sqlite"

    def _db(path=None):
        return ResearchDB(path=path or db_path)

    monkeypatch.setattr("llm2.evidence.pack_registry.ResearchDB", _db)
    monkeypatch.setattr(
        "llm2.evidence.pack_registry.ensure_registry_schema",
        lambda db=None: db or _db(),
    )
    meta = register_freeze(
        pack,
        evidence={"report_paths": ["artifacts/reports/dummy.json"]},
        require_run_id=False,
        ledger=False,
    )
    assert meta["version_id"] == "testpack_v1"
    try:
        register_freeze(pack, evidence={"tradesim_run_ids": []}, require_run_id=True)
        raised = False
    except RuntimeError:
        raised = True
    assert raised is True


def test_open_pack_run_requires_run_id():
    try:
        open_pack_run("nonexistent_version_zz")
        assert False, "should raise"
    except RuntimeError as exc:
        assert "run_id" in str(exc).lower() or "version" in str(exc).lower()


def test_regenerate_versions_md_writes():
    ensure_registry_schema()
    path = regenerate_versions_md()
    assert path.is_file()
    text = path.read_text(encoding="utf-8")
    assert "Live pack versions" in text
