"""Four-proof causality gate (mandatory before train / pack freeze / live authorize).

A green shared ``leakage`` report alone is **illegal** evidence for warehouse-backed
spaces (D-014, D-016, D-025, D-055). Agents must produce all four proofs:

1. **builder_responsiveness** — tip shape-shock moves features (CAUS-WAREHOUSE-001)
2. **recompute_prefix** — warehouse recomputed from handed candles is prefix-invariant
3. **no_live_feature_fill** — live path refuses NaN features (no zero-fill of retrace)
4. **layer_a_pred_identity** — research warehouse join vs recompute path agree on tip
   predictions (agents cannot audit a shadow builder while training on another)

Artifacts land in ``artifacts/evidence/four_proof/<stamp>/`` and their SHA-256 hashes
must be present on ``pack_meta.json`` before ``register_freeze`` / live certificate.
"""

from __future__ import annotations

import ast
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

from llm2.paths import ARTIFACTS, ROOT
from llm2.research_policy import PolicyError, WAREHOUSE_BACKED_SPACES

EVIDENCE_ROOT = ARTIFACTS / "evidence" / "four_proof"
PROOF_KEYS = (
    "builder_responsiveness",
    "recompute_prefix",
    "no_live_feature_fill",
    "layer_a_pred_identity",
)
MICRO_RUNNER = ROOT / "llm2" / "live" / "micro_runner.py"


def _sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _sha256_file(path: Path) -> str:
    return _sha256_bytes(path.read_bytes())


def _write_json(path: Path, obj: dict[str, Any]) -> str:
    path.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(obj, indent=2, default=str, sort_keys=True) + "\n"
    path.write_text(text, encoding="utf-8")
    return _sha256_bytes(text.encode("utf-8"))


def proof_no_live_feature_fill() -> dict[str, Any]:
    """Static proof: micro_runner must not zero-fill missing structure features."""
    src = MICRO_RUNNER.read_text(encoding="utf-8")
    # Forbidden patterns that silently invent values research never scored.
    forbidden = [
        r"fillna\(0\.0\)",
        r"fillna\(0\)",
        r"last_retrace_pct.*=.*0\.0",
        r"zero-fill retrace",
        r"zero_fill",
    ]
    hits = []
    for pat in forbidden:
        if re.search(pat, src):
            # Allow the explanatory comment that says zero-fill was removed.
            for m in re.finditer(pat, src):
                line_start = src.rfind("\n", 0, m.start()) + 1
                line = src[line_start : src.find("\n", m.start())]
                if line.strip().startswith("#"):
                    continue
                hits.append({"pattern": pat, "line": line.strip()[:160]})
    ok = len(hits) == 0
    # Also require the refuse-on-NaN path exists.
    has_nan_refuse = "nan_cols" in src and ("STRUCTURE" in src or "isna" in src)
    if not has_nan_refuse:
        hits.append({"pattern": "nan_refuse", "line": "missing nan_cols refuse path"})
        ok = False
    return {
        "proof": "no_live_feature_fill",
        "ok": ok,
        "hits": hits,
        "source": str(MICRO_RUNNER.relative_to(ROOT)),
        "source_sha256": _sha256_file(MICRO_RUNNER),
    }


def proof_builder_responsiveness(
    ohlcv: pd.DataFrame,
    *,
    space: str,
    symbol: str,
    timeframe: str,
) -> dict[str, Any]:
    from llm2.features.guard import make_builder, _prefer_leakage

    _prefer_leakage()
    from leakage.checks import check_builder_responsiveness

    builder = make_builder(space, symbol)
    # Keep recompute tractable.
    frame = ohlcv.iloc[-2500:].copy() if len(ohlcv) > 2500 else ohlcv
    findings = check_builder_responsiveness(
        frame, builder, interval=timeframe, compare_rows=40
    )
    return {
        "proof": "builder_responsiveness",
        "ok": len(findings) == 0,
        "space": space,
        "symbol": symbol,
        "timeframe": timeframe,
        "n_findings": len(findings),
        "findings": [
            {
                "check": f.check.value,
                "column": f.column,
                "message": f.message,
                "detail": f.detail,
            }
            for f in findings
        ],
        "conformance": "CAUS-WAREHOUSE-001",
    }


def proof_recompute_prefix(
    ohlcv: pd.DataFrame,
    *,
    space: str,
    symbol: str,
    timeframe: str,
    cuts: int = 2,
) -> dict[str, Any]:
    from llm2.features.guard import make_builder, _prefer_leakage

    _prefer_leakage()
    from leakage import run_leakage_audit

    builder = make_builder(space, symbol)
    frame = ohlcv.iloc[-3000:].copy() if len(ohlcv) > 3000 else ohlcv
    report = run_leakage_audit(
        ohlcv=frame,
        build_features=builder,
        interval=timeframe,
        symbol=symbol,
        timeframe=timeframe,
        cuts=cuts,
        compare_rows=min(200, max(50, len(frame) // 10)),
        run_forward_corr=False,
        require_decisive=True,
    )
    hard = [
        {
            "check": f.check.value,
            "column": f.column,
            "message": f.message,
        }
        for f in report.findings
        if f.severity.value == "HARD"
    ]
    return {
        "proof": "recompute_prefix",
        "ok": bool(report.ok),
        "space": space,
        "symbol": symbol,
        "timeframe": timeframe,
        "summary": report.summary(),
        "hard_findings": hard,
        "n_columns": report.n_columns,
    }


def proof_layer_a_pred_identity(
    ohlcv: pd.DataFrame,
    *,
    space: str,
    symbol: str,
    timeframe: str,
    model: Any | None = None,
    feature_columns: list[str] | None = None,
    tip_bars: int = 24,
) -> dict[str, Any]:
    """Research warehouse join vs leakage-recompute path must agree on tip rows.

    This is the anti-shadow-builder proof: agents cannot audit a recompute builder
    while training on a calendar-keyed warehouse join that still leaks.
    """
    from llm2.data.indicators import clear_indicator_cache
    from llm2.features.guard import _with_recomputed_structure
    from llm2.features.registry import build_space

    # Structure S/R depends on the full swing path. Truncating the recompute
    # window (even to 5k bars) flips tip structure_bias vs the warehouse that
    # was built on the complete series. Hand the full frame; score tip only.
    frame = ohlcv
    clear_indicator_cache()
    warehouse = build_space(frame, space, symbol=symbol, timeframe=timeframe)
    clear_indicator_cache()
    if space in WAREHOUSE_BACKED_SPACES and space != "macro_v1":
        recomputed = _with_recomputed_structure(
            frame, interval=timeframe, symbol=symbol, space=space
        )
    else:
        recomputed = build_space(frame, space, symbol=symbol, timeframe=timeframe)

    cols = list(feature_columns or sorted(set(warehouse.columns) & set(recomputed.columns)))
    tip_idx = warehouse.index[-tip_bars:]
    n_diff = 0
    max_abs = 0.0
    first_bad = None
    for ts in tip_idx:
        if ts not in recomputed.index:
            n_diff += 1
            first_bad = first_bad or str(ts)
            continue
        for c in cols:
            if c not in warehouse.columns or c not in recomputed.columns:
                continue
            a = float(pd.to_numeric(warehouse.loc[ts, c], errors="coerce"))
            b = float(pd.to_numeric(recomputed.loc[ts, c], errors="coerce"))
            if np.isnan(a) and np.isnan(b):
                continue
            d = abs(a - b) if np.isfinite(a) and np.isfinite(b) else 1.0
            if d > 1e-9:
                n_diff += 1
                max_abs = max(max_abs, d if np.isfinite(d) else max_abs)
                first_bad = first_bad or f"{ts}:{c}"
                break

    pred_diff = None
    if model is not None and cols:
        wh = warehouse.reindex(columns=cols).dropna()
        rc = recomputed.reindex(columns=cols).dropna()
        common = wh.index.intersection(rc.index)[-tip_bars:]
        if len(common) > 0:
            p1 = model.predict(wh.loc[common].to_numpy(dtype=float))
            p2 = model.predict(rc.loc[common].to_numpy(dtype=float))
            m1 = np.asarray(p1.mean if hasattr(p1, "mean") else p1, dtype=float).reshape(-1)
            m2 = np.asarray(p2.mean if hasattr(p2, "mean") else p2, dtype=float).reshape(-1)
            pred_diff = float(np.max(np.abs(m1 - m2))) if len(m1) else None

    ok = n_diff == 0 and (pred_diff is None or pred_diff <= 1e-9)
    return {
        "proof": "layer_a_pred_identity",
        "ok": ok,
        "space": space,
        "symbol": symbol,
        "timeframe": timeframe,
        "tip_bars": tip_bars,
        "n_feature_rows_differ": n_diff,
        "max_abs_feature_diff": max_abs,
        "first_bad": first_bad,
        "pred_mean_max_abs_diff": pred_diff,
        "n_columns_compared": len(cols),
    }


def run_four_proof_gate(
    *,
    space: str,
    symbol: str,
    timeframe: str = "1h",
    ohlcv: pd.DataFrame | None = None,
    model: Any | None = None,
    feature_columns: list[str] | None = None,
    out_dir: Path | None = None,
) -> dict[str, Any]:
    """Execute all four proofs and persist hashed artifacts."""
    from llm2.data.loader import load_ohlcv

    if ohlcv is None:
        ohlcv = load_ohlcv(symbol, timeframe)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    dest = out_dir or (EVIDENCE_ROOT / f"{space}_{symbol}_{timeframe}_{stamp}")
    dest.mkdir(parents=True, exist_ok=True)

    proofs: dict[str, Any] = {}
    hashes: dict[str, str] = {}

    p1 = proof_builder_responsiveness(ohlcv, space=space, symbol=symbol, timeframe=timeframe)
    hashes["builder_responsiveness"] = _write_json(dest / "builder_responsiveness.json", p1)
    proofs["builder_responsiveness"] = p1

    p2 = proof_recompute_prefix(ohlcv, space=space, symbol=symbol, timeframe=timeframe)
    hashes["recompute_prefix"] = _write_json(dest / "recompute_prefix.json", p2)
    proofs["recompute_prefix"] = p2

    p3 = proof_no_live_feature_fill()
    hashes["no_live_feature_fill"] = _write_json(dest / "no_live_feature_fill.json", p3)
    proofs["no_live_feature_fill"] = p3

    p4 = proof_layer_a_pred_identity(
        ohlcv,
        space=space,
        symbol=symbol,
        timeframe=timeframe,
        model=model,
        feature_columns=feature_columns,
    )
    hashes["layer_a_pred_identity"] = _write_json(dest / "layer_a_pred_identity.json", p4)
    proofs["layer_a_pred_identity"] = p4

    ok = all(bool(proofs[k]["ok"]) for k in PROOF_KEYS)
    summary = {
        "stamp": stamp,
        "space": space,
        "symbol": symbol,
        "timeframe": timeframe,
        "ok": ok,
        "proofs_ok": {k: bool(proofs[k]["ok"]) for k in PROOF_KEYS},
        "artifact_dir": str(dest),
        "artifact_hashes": hashes,
        "rule": "FOUR_PROOF_GATE_V1",
        "note": (
            "Warehouse-backed spaces may not treat a lone shared leakage PASS as evidence."
        ),
    }
    summary_hash = _write_json(dest / "four_proof_summary.json", summary)
    summary["summary_sha256"] = summary_hash
    _write_json(dest / "four_proof_summary.json", summary)
    latest = EVIDENCE_ROOT / "four_proof_latest.json"
    _write_json(latest, summary)
    return summary


def require_four_proof_ok(summary: dict[str, Any]) -> None:
    if not summary.get("ok"):
        raise PolicyError(
            "FOUR_PROOF_GATE FAILED: "
            + json.dumps(summary.get("proofs_ok"), sort_keys=True)
            + ". A green shared leakage PASS alone is not evidence for warehouse spaces."
        )


def attach_four_proof_to_pack(pack_dir: Path, summary: dict[str, Any]) -> dict[str, Any]:
    """Write four-proof hashes into pack_meta.json (call after a green gate)."""
    require_four_proof_ok(summary)
    pack_dir = Path(pack_dir)
    meta_path = pack_dir / "pack_meta.json"
    meta = json.loads(meta_path.read_text(encoding="utf-8")) if meta_path.is_file() else {}
    evidence = dict(meta.get("evidence") or {})
    evidence["four_proof_hashes"] = dict(summary.get("artifact_hashes") or {})
    evidence["four_proof_ok"] = True
    evidence["four_proof_summary_sha256"] = summary.get("summary_sha256")
    evidence["four_proof_artifact_dir"] = summary.get("artifact_dir")
    evidence["four_proof_stamp"] = summary.get("stamp")
    meta["evidence"] = evidence
    meta["four_proof_ok"] = True
    meta["four_proof_hashes"] = evidence["four_proof_hashes"]
    meta_path.parent.mkdir(parents=True, exist_ok=True)
    meta_path.write_text(json.dumps(meta, indent=2, default=str) + "\n", encoding="utf-8")
    return meta


def require_four_proof_hashes_on_pack(pack_dir: Path) -> dict[str, Any]:
    """Refuse pack freeze / live certificate without four-proof artifact hashes."""
    meta_path = Path(pack_dir) / "pack_meta.json"
    if not meta_path.is_file():
        raise PolicyError(f"pack_meta.json missing at {pack_dir} — cannot freeze")
    meta = json.loads(meta_path.read_text(encoding="utf-8"))
    evidence = meta.get("evidence") or {}
    hashes = evidence.get("four_proof_hashes") or meta.get("four_proof_hashes")
    if not isinstance(hashes, dict) or not hashes:
        raise PolicyError(
            f"pack freeze REFUSED for {pack_dir}: missing evidence.four_proof_hashes. "
            "Run llm2.evidence.four_proof.run_four_proof_gate and attach hashes before freeze."
        )
    missing = [k for k in PROOF_KEYS if not hashes.get(k)]
    if missing:
        raise PolicyError(
            f"pack freeze REFUSED for {pack_dir}: four_proof_hashes missing keys {missing}"
        )
    if not evidence.get("four_proof_ok", meta.get("four_proof_ok")):
        raise PolicyError(
            f"pack freeze REFUSED for {pack_dir}: four_proof_ok is not true"
        )
    return hashes


def refuse_warehouse_leakage_pass_alone(
    *,
    space: str,
    leakage_passed: bool,
    four_proof_ok: bool | None,
) -> None:
    """Hard stop: warehouse space + leakage PASS + no four-proof = illegal."""
    if space not in WAREHOUSE_BACKED_SPACES:
        return
    if leakage_passed and not four_proof_ok:
        raise PolicyError(
            f"feature space {space!r}: shared leakage PASS is not sufficient evidence "
            "(D-014/D-016/D-025/D-055). four_proof_ok must be True before train/freeze."
        )


def refuse_pred_mismatch_hard_stop(
    *,
    n_bars_pred_differ: int,
    context: str = "live_vs_bt",
) -> None:
    """Live↔backtest prediction mismatch is a hard stop, like a failed gate."""
    if int(n_bars_pred_differ) > 0:
        raise PolicyError(
            f"PRED_MISMATCH_HARD_STOP ({context}): n_bars_pred_differ="
            f"{n_bars_pred_differ}. Stop optimization / freeze / deploy. "
            "Treat as leakage or engine parity failure until Layer A is identically zero."
        )


def micro_runner_has_no_fill_ast() -> bool:
    """AST-level guard used by tests (comments cannot satisfy this)."""
    tree = ast.parse(MICRO_RUNNER.read_text(encoding="utf-8"))
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
            if node.func.attr == "fillna" and node.args:
                arg0 = node.args[0]
                if isinstance(arg0, ast.Constant) and arg0.value in (0, 0.0):
                    return False
    return True
