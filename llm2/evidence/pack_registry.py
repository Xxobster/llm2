"""Machine-readable live pack version registry.

Every freeze/deploy writes:
  - pack_meta.json evidence fields on the pack directory
  - a row in research.sqlite live_pack_versions
  - an append-only RESEARCH_LEDGER line

Former models stay usable: open_pack_run(version_id) reopens a stored
tradesim run_id when evidence.tradesim_run_ids is populated — never resim
under the freeze-evidence label.
"""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from llm2.live.certificate import pack_fingerprint
from llm2.paths import ARTIFACTS, RESEARCH_DB, ROOT
from llm2.registry.db import ResearchDB
from llm2.registry.ledger import append_ledger

LIVE_PACKS = ARTIFACTS / "live_packs"
VERSIONS_MD = LIVE_PACKS / "VERSIONS.md"
CERT_DIR = ROOT / "configs" / "live"

# Known live/deployed services (used when backfilling / regenerating VERSIONS.md).
KNOWN_LIVE: dict[str, dict[str, Any]] = {
    "eth_multitrade_v1_2": {
        "account_ref": "Xxobster8",
        "service": "llm2-structure-eth-multitrade-v1_2",
        "deployed": True,
    },
    "eth_multitrade_v1_1": {
        "account_ref": "Xxobster8",
        "service": "llm2-structure-eth-multitrade-v1_1",
        "deployed": False,
    },
    "eth_multitrade_v1": {
        "account_ref": "Xxobster8",
        "service": "llm2-structure-eth-multitrade-v1",
        "deployed": False,
    },
    "btc_fwd_single_v1": {
        "account_ref": "Xxobster7",
        "service": "llm2-structure-micro",
        "deployed": True,
    },
    "eth_direction_single_v1": {
        "account_ref": "Xxobster7",
        "service": "llm2-structure-eth",
        "deployed": True,
    },
    "sol_direction_single_v1": {
        "account_ref": "Xxobster7",
        "service": "llm2-structure-sol",
        "deployed": True,
    },
    "eth_k5_double3h_v1": {
        "account_ref": "Xxobster6",
        "service": "llm2-structure-eth-k5-double3h-v1",
        "deployed": True,
    },
    "btc_k5_double3h_v1": {
        "account_ref": "Xxobster10",
        "service": "llm2-structure-btc-k5-double3h-v1",
        "deployed": True,
    },
    "sol_k5_double3h_v1": {
        "account_ref": "Xxobster10",
        "service": "llm2-structure-sol-k5-double3h-v1",
        "deployed": True,
    },
}


def _utcnow() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def _isoformat() -> str:
    return datetime.now(timezone.utc).isoformat()


def _json_dumps(obj: Any) -> str:
    return json.dumps(obj, indent=2, default=str, sort_keys=False)


def ensure_registry_schema(db: ResearchDB | None = None) -> ResearchDB:
    """Apply schema (idempotent CREATE IF NOT EXISTS)."""
    reg = db or ResearchDB()
    # ResearchDB._init_schema already runs schema.sql
    return reg


def load_pack_meta(pack_dir: Path) -> dict[str, Any]:
    path = pack_dir / "pack_meta.json"
    if path.is_file():
        return json.loads(path.read_text(encoding="utf-8"))
    return {}


def load_strategy(pack_dir: Path) -> dict[str, Any]:
    path = pack_dir / "strategy.json"
    if path.is_file():
        return json.loads(path.read_text(encoding="utf-8"))
    return {}


def infer_version_id(pack_dir: Path, meta: dict[str, Any], strategy: dict[str, Any]) -> str:
    for src in (
        meta.get("version_id"),
        strategy.get("version_id"),
        (strategy.get("multitrade") or {}).get("version_id"),
        (strategy.get("version_lineage") or {}).get("version_id"),
    ):
        if src:
            return str(src)
    # Fall back to directory name
    name = pack_dir.name
    if name.startswith("structure_v1_"):
        # structure_v1_ethusdt_multitrade_v1_2 → eth_multitrade_v1_2-ish
        return name.replace("structure_v1_", "")
    return name


def normalize_pack_meta(
    pack_dir: Path,
    *,
    evidence: dict[str, Any] | None = None,
    live: dict[str, Any] | None = None,
    metrics: dict[str, Any] | None = None,
    status: str | None = None,
    readiness: str | None = None,
) -> dict[str, Any]:
    """Merge existing pack_meta/strategy into the canonical schema."""
    meta = load_pack_meta(pack_dir)
    strategy = load_strategy(pack_dir)
    version_id = infer_version_id(pack_dir, meta, strategy)
    pack_hash = (pack_dir / "pack_hash.txt").read_text(encoding="utf-8").strip() if (
        pack_dir / "pack_hash.txt"
    ).is_file() else (pack_fingerprint(pack_dir) or None)

    lineage = strategy.get("version_lineage") or meta.get("version_lineage") or {}
    parent = (
        meta.get("parent_pack")
        or meta.get("parent")
        or lineage.get("parent_pack")
        or None
    )
    replaces = (
        meta.get("replaces_version")
        or lineage.get("replaces")
        or None
    )
    strategy_id = (
        meta.get("strategy_id")
        or strategy.get("strategy_id")
        or version_id
    )

    ev = dict(meta.get("evidence") or {})
    if evidence:
        for k, v in evidence.items():
            if v is None:
                continue
            if k in ("tradesim_run_ids", "report_paths") and isinstance(v, list):
                prev = list(ev.get(k) or [])
                for item in v:
                    if item not in prev:
                        prev.append(item)
                ev[k] = prev
            else:
                ev[k] = v

    live_doc = dict(meta.get("live") or {})
    known = KNOWN_LIVE.get(version_id) or {}
    for k, v in known.items():
        live_doc.setdefault(k, v)
    # Certificate heuristic
    if live_doc.get("certificate_path") is None:
        cand = CERT_DIR / f"{pack_dir.name}_certificate.yaml"
        if cand.is_file():
            live_doc["certificate_path"] = str(cand.relative_to(ROOT)).replace("\\", "/")
    if live is not None:
        live_doc.update({k: v for k, v in live.items() if v is not None})

    metrics_doc = dict(meta.get("metrics") or meta.get("headline_metrics") or {})
    if metrics:
        metrics_doc.update(metrics)

    try:
        pack_path = str(pack_dir.resolve().relative_to(ROOT.resolve())).replace("\\", "/")
    except ValueError:
        pack_path = str(pack_dir.resolve())

    out = {
        **{k: v for k, v in meta.items() if k not in {
            "evidence", "live", "metrics", "headline_metrics"
        }},
        "version_id": version_id,
        "strategy_id": strategy_id,
        "status": status or meta.get("status") or "FROZEN",
        "readiness": readiness
        or meta.get("readiness")
        or meta.get("settlement_verdict")
        or "RESEARCH_ONLY",
        "frozen_utc": meta.get("frozen_utc") or _utcnow(),
        "pack_hash": pack_hash or meta.get("pack_hash"),
        "pack_path": pack_path,
        "parent_pack": parent,
        "replaces_version": replaces,
        "evidence": ev,
        "live": live_doc,
        "metrics": metrics_doc,
    }
    return out


def write_pack_meta(pack_dir: Path, meta: dict[str, Any]) -> Path:
    path = pack_dir / "pack_meta.json"
    path.write_text(_json_dumps(meta) + "\n", encoding="utf-8")
    return path


def _upsert_sqlite(meta: dict[str, Any], db: ResearchDB | None = None) -> None:
    reg = ensure_registry_schema(db)
    now = _isoformat()
    with reg._connect() as conn:
        conn.execute(
            """
            INSERT INTO live_pack_versions (
                version_id, pack_path, pack_hash, strategy_id, status, readiness,
                replaces_version, parent_pack, frozen_utc, evidence_json, live_json,
                metrics_json, created_at, updated_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(version_id) DO UPDATE SET
                pack_path=excluded.pack_path,
                pack_hash=excluded.pack_hash,
                strategy_id=excluded.strategy_id,
                status=excluded.status,
                readiness=excluded.readiness,
                replaces_version=excluded.replaces_version,
                parent_pack=excluded.parent_pack,
                frozen_utc=excluded.frozen_utc,
                evidence_json=excluded.evidence_json,
                live_json=excluded.live_json,
                metrics_json=excluded.metrics_json,
                updated_at=excluded.updated_at
            """,
            (
                meta["version_id"],
                meta.get("pack_path") or "",
                meta.get("pack_hash"),
                meta.get("strategy_id"),
                meta.get("status"),
                meta.get("readiness"),
                meta.get("replaces_version"),
                meta.get("parent_pack"),
                meta.get("frozen_utc"),
                json.dumps(meta.get("evidence") or {}, default=str),
                json.dumps(meta.get("live") or {}, default=str),
                json.dumps(meta.get("metrics") or {}, default=str),
                now,
                now,
            ),
        )
        conn.commit()


def register_freeze(
    pack_dir: Path | str,
    *,
    evidence: dict[str, Any] | None = None,
    metrics: dict[str, Any] | None = None,
    status: str | None = None,
    readiness: str | None = None,
    require_run_id: bool = False,
    ledger: bool = True,
) -> dict[str, Any]:
    """Register a frozen pack. Fail closed if require_run_id and none present.

    Does not downgrade an existing LIVE_ACTIVE status unless ``status`` is
    passed explicitly (avoids evidence-only attach clobbering live state).
    """
    pack_dir = Path(pack_dir)
    if not pack_dir.is_absolute():
        pack_dir = ROOT / pack_dir
    if not pack_dir.is_dir():
        raise FileNotFoundError(pack_dir)

    existing = load_pack_meta(pack_dir)
    prev_status = str(existing.get("status") or "")
    # Preserve live status when only attaching evidence/metrics.
    eff_status = status
    if eff_status is None:
        if prev_status in {"LIVE_ACTIVE", "FROZEN_ROLLED_BACK"}:
            eff_status = prev_status
        else:
            eff_status = "FROZEN"
    eff_readiness = readiness or existing.get("readiness") or "RESEARCH_ONLY"

    meta = normalize_pack_meta(
        pack_dir,
        evidence=evidence,
        metrics=metrics,
        status=str(eff_status),
        readiness=str(eff_readiness),
    )
    run_ids = list((meta.get("evidence") or {}).get("tradesim_run_ids") or [])
    if require_run_id and not run_ids:
        raise RuntimeError(
            f"register_freeze require_run_id=True but {pack_dir} has no "
            "evidence.tradesim_run_ids — refuse freeze without stored backtest"
        )
    # Four-proof causality gate (D-055 / D-057): refuse freeze without hashed artifacts.
    from llm2.evidence.four_proof import require_four_proof_hashes_on_pack

    require_four_proof_hashes_on_pack(pack_dir)
    write_pack_meta(pack_dir, meta)
    _upsert_sqlite(meta)
    if ledger:
        append_ledger(
            "PACK_FREEZE "
            f"version_id={meta['version_id']} pack_hash={meta.get('pack_hash')} "
            f"run_ids={run_ids} path={meta.get('pack_path')}",
            tier=0,
        )
    return meta


def register_live(
    version_id: str,
    *,
    deployed: bool,
    account_ref: str | None = None,
    service: str | None = None,
    certificate_path: str | None = None,
    deployed_utc: str | None = None,
) -> dict[str, Any]:
    """Update live deployment status for an existing version."""
    rows = list_versions()
    match = next((r for r in rows if r["version_id"] == version_id), None)
    if not match:
        raise KeyError(f"version_id not registered: {version_id}")
    pack_dir = ROOT / match["pack_path"]
    live_update = {
        "deployed": bool(deployed),
        "deployed_utc": deployed_utc or (_utcnow() if deployed else None),
    }
    if account_ref is not None:
        live_update["account_ref"] = account_ref
    if service is not None:
        live_update["service"] = service
    if certificate_path is not None:
        live_update["certificate_path"] = certificate_path
    meta = normalize_pack_meta(pack_dir, live=live_update)
    if deployed:
        meta["status"] = "LIVE_ACTIVE"
    elif meta.get("status") == "LIVE_ACTIVE":
        meta["status"] = "FROZEN_ROLLED_BACK"
    write_pack_meta(pack_dir, meta)
    _upsert_sqlite(meta)
    event = "PACK_LIVE" if deployed else "PACK_ROLLBACK"
    append_ledger(
        f"{event} version_id={version_id} deployed={deployed} "
        f"service={meta.get('live', {}).get('service')} "
        f"account={meta.get('live', {}).get('account_ref')}",
        tier=1 if deployed else 0,
    )
    return meta


def list_versions() -> list[dict[str, Any]]:
    ensure_registry_schema()
    with ResearchDB()._connect() as conn:
        rows = conn.execute(
            "SELECT * FROM live_pack_versions ORDER BY updated_at DESC"
        ).fetchall()
    out: list[dict[str, Any]] = []
    for r in rows:
        d = dict(r)
        for key in ("evidence_json", "live_json", "metrics_json"):
            raw = d.pop(key, None)
            name = key.replace("_json", "")
            try:
                d[name] = json.loads(raw) if raw else {}
            except json.JSONDecodeError:
                d[name] = {}
        out.append(d)
    return out


def get_version(version_id: str) -> dict[str, Any] | None:
    for row in list_versions():
        if row["version_id"] == version_id:
            return row
    return None


def primary_run_id(version_id: str) -> str | None:
    row = get_version(version_id)
    if not row:
        return None
    ids = list((row.get("evidence") or {}).get("tradesim_run_ids") or [])
    return str(ids[0]) if ids else None


def open_pack_run(
    version_id: str | None = None,
    *,
    run_id: str | None = None,
    store_path: str | Path | None = None,
) -> dict[str, Any]:
    """Reopen a stored tradesim run without resimulating.

    Prefer ``tradesim-research open --run-id`` when CLI available; otherwise
    return the path to the report directory under projectsdata backtests.
    """
    rid = run_id or (primary_run_id(version_id) if version_id else None)
    if not rid:
        raise RuntimeError(
            f"no tradesim run_id for version_id={version_id!r}; cannot open without resim"
        )
    report_root = Path(store_path or r"D:\projectsdata\backtests\reports") / str(rid)
    cmd = [
        sys.executable,
        "-m",
        "tradesim.research.cli",
        "open",
        "--run-id",
        str(rid),
    ]
    # Prefer botsgeneral tradesim
    src = Path(r"C:\projects\botsgeneral\packages\tradesim\src")
    env = dict(**{k: v for k, v in __import__("os").environ.items()})
    if src.is_dir():
        env["PYTHONPATH"] = str(src) + (
            (";" + env["PYTHONPATH"]) if env.get("PYTHONPATH") else ""
        )
    # Try CLI first; if missing still return structured location
    cli_ok = False
    cli_err = None
    try:
        which = shutil.which("tradesim-research")
        if which:
            r = subprocess.run(
                [which, "open", "--run-id", str(rid)],
                capture_output=True,
                text=True,
                timeout=120,
                env=env,
            )
            cli_ok = r.returncode == 0
            cli_err = (r.stderr or r.stdout or "")[:500]
        else:
            r = subprocess.run(cmd, capture_output=True, text=True, timeout=120, env=env)
            cli_ok = r.returncode == 0
            cli_err = (r.stderr or r.stdout or "")[:500]
    except Exception as exc:  # noqa: BLE001
        cli_err = f"{type(exc).__name__}: {exc}"

    return {
        "version_id": version_id,
        "run_id": str(rid),
        "report_dir": str(report_root) if report_root.is_dir() else None,
        "cli_invoked": True,
        "cli_ok": cli_ok,
        "cli_detail": cli_err,
        "note": (
            "Reopened stored tradesim run — not a fresh simulation. "
            "Do not label a resim as freeze evidence."
        ),
    }


def backfill_all_packs(*, write_versions_md: bool = True) -> list[dict[str, Any]]:
    """Scan artifacts/live_packs/*/ and register each directory."""
    ensure_registry_schema()
    registered: list[dict[str, Any]] = []
    if not LIVE_PACKS.is_dir():
        return registered
    for pack_dir in sorted(LIVE_PACKS.iterdir()):
        if not pack_dir.is_dir():
            continue
        if not (pack_dir / "strategy.json").is_file():
            continue
        meta = register_freeze(
            pack_dir,
            require_run_id=False,
            ledger=False,
        )
        # Fix status for known live (and packs that already mark live.deployed).
        vid = meta["version_id"]
        known = KNOWN_LIVE.get(vid) or {}
        live_doc = meta.get("live") or {}
        want_live = bool(known.get("deployed") or live_doc.get("deployed"))
        if want_live:
            meta = register_live(
                vid,
                deployed=True,
                account_ref=known.get("account_ref") or live_doc.get("account_ref"),
                service=known.get("service") or live_doc.get("service"),
                certificate_path=live_doc.get("certificate_path"),
            )
        registered.append(meta)
    append_ledger(
        f"PACK_REGISTRY_BACKFILL n={len(registered)} "
        f"versions={[m['version_id'] for m in registered]}",
        tier=0,
    )
    if write_versions_md:
        regenerate_versions_md()
    return registered


def regenerate_versions_md() -> Path:
    """Regenerate VERSIONS.md from the SQLite registry (human rollback map)."""
    rows = list_versions()
    # Prefer deterministic order: deployed first, then alpha
    rows_sorted = sorted(
        rows,
        key=lambda r: (
            0 if (r.get("live") or {}).get("deployed") else 1,
            str(r.get("version_id") or ""),
        ),
    )
    lines = [
        "# Live pack versions (rollback map)",
        "",
        "Immutable rule: never overwrite a frozen pack in place to “upgrade” behavior.",
        "Ship a new directory + certificate + systemd unit; leave prior packs on disk.",
        "",
        "Generated from `live_pack_versions` in research.sqlite via "
        "`llm2.evidence.pack_registry.regenerate_versions_md`. Do not hand-edit "
        "without re-running the generator after pack freezes.",
        "",
        "| version_id | pack path | status | account | VPS service | readiness | notes |",
        "|---|---|---|---|---|---|---|",
    ]
    for r in rows_sorted:
        live = r.get("live") or {}
        metrics = r.get("metrics") or {}
        note_bits = []
        if r.get("replaces_version"):
            note_bits.append(f"replaces {r['replaces_version']}")
        if metrics.get("profit_factor") is not None:
            note_bits.append(f"PF={metrics['profit_factor']}")
        if metrics.get("expectancy_return_units") is not None:
            note_bits.append(f"E[r]={metrics['expectancy_return_units']}")
        if live.get("deployed"):
            note_bits.insert(0, "**active**")
        lines.append(
            f"| `{r.get('version_id')}` | `{r.get('pack_path')}` | "
            f"{r.get('status') or ''} | {live.get('account_ref') or '—'} | "
            f"`{live.get('service') or '—'}` | {r.get('readiness') or '—'} | "
            f"{'; '.join(note_bits) or '—'} |"
        )
    lines.extend(
        [
            "",
            "## Rollback",
            "",
            "1. Stop current active unit for that account.",
            "2. `systemctl enable --now` the previous service (pack retained on disk).",
            "3. Call `register_live(old_version, deployed=True)` and "
            "`register_live(new_version, deployed=False)`.",
            "4. Never overwrite a frozen pack directory in place.",
            "",
            "## Open metrics without resim",
            "",
            "```python",
            "from llm2.evidence.pack_registry import open_pack_run, primary_run_id",
            "print(primary_run_id('eth_multitrade_v1_2'))",
            "open_pack_run('eth_multitrade_v1_2')  # tradesim-research open --run-id …",
            "```",
            "",
            f"_Generated {_utcnow()} UTC._",
            "",
        ]
    )
    VERSIONS_MD.parent.mkdir(parents=True, exist_ok=True)
    VERSIONS_MD.write_text("\n".join(lines), encoding="utf-8")
    return VERSIONS_MD


def register_compare_report(
    generation_id: str,
    *,
    report_path: Path | str,
    control_metrics: dict[str, Any],
    candidate_metrics: dict[str, Any],
    tradesim_run_ids: list[str] | None = None,
    control_version_id: str | None = None,
    candidate_version_id: str | None = None,
) -> None:
    """Stamp an outer-transfer compare into the ledger + evaluation_runs."""
    ensure_registry_schema()
    report_path = Path(report_path)
    rel = str(report_path.relative_to(ROOT)).replace("\\", "/") if report_path.is_absolute() and ROOT in report_path.parents else str(report_path)
    with ResearchDB()._connect() as conn:
        conn.execute(
            "INSERT OR REPLACE INTO evaluation_runs "
            "(run_id, trial_id, run_type, gates_json, readiness, created_at) "
            "VALUES (?, ?, ?, ?, ?, ?)",
            (
                generation_id,
                None,
                "outer_transfer_compare",
                json.dumps(
                    {
                        "control": control_metrics,
                        "candidate": candidate_metrics,
                        "report_path": rel,
                        "tradesim_run_ids": tradesim_run_ids or [],
                        "control_version_id": control_version_id,
                        "candidate_version_id": candidate_version_id,
                    },
                    default=str,
                ),
                "RESEARCH_ONLY",
                _isoformat(),
            ),
        )
        conn.commit()
    append_ledger(
        f"OUTER_TRANSFER_COMPARE generation_id={generation_id} "
        f"control_exp_ru={control_metrics.get('expectancy_return_units')} "
        f"cand_exp_ru={candidate_metrics.get('expectancy_return_units')} "
        f"control_pf={control_metrics.get('profit_factor')} "
        f"cand_pf={candidate_metrics.get('profit_factor')} path={rel}",
        tier=0,
    )
    # Attach report to control pack evidence if known
    if control_version_id:
        row = get_version(control_version_id)
        if row and row.get("pack_path"):
            register_freeze(
                ROOT / row["pack_path"],
                evidence={
                    "report_paths": [rel],
                    "generation_id": generation_id,
                    "tradesim_run_ids": tradesim_run_ids or [],
                },
                require_run_id=False,
                ledger=False,
            )
