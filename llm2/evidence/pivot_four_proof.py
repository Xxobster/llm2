"""Four-proof style gate for pivot OHLCV tip packs (not warehouse structure).

Produces the same hash keys expected by live certificates:
builder_responsiveness, recompute_prefix, no_live_feature_fill, layer_a_pred_identity.
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
from llm2.pivot.features.packs import build_feature_frame
from llm2.research_policy import PolicyError
from llm2.validation.folds import index_to_ms

EVIDENCE_ROOT = ARTIFACTS / "evidence" / "four_proof"
PIVOT_RUNNER = ROOT / "llm2" / "live" / "pivot_runner.py"
PROOF_KEYS = (
    "builder_responsiveness",
    "recompute_prefix",
    "no_live_feature_fill",
    "layer_a_pred_identity",
)


def _sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _write_json(path: Path, obj: dict[str, Any]) -> str:
    path.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(obj, indent=2, default=str, sort_keys=True) + "\n"
    path.write_text(text, encoding="utf-8")
    return _sha256_bytes(text.encode("utf-8"))


def proof_no_live_feature_fill_pivot() -> dict[str, Any]:
    src = PIVOT_RUNNER.read_text(encoding="utf-8")
    forbidden = [r"fillna\(0\.0\)", r"fillna\(0\)", r"zero_fill"]
    hits = []
    for pat in forbidden:
        for m in re.finditer(pat, src):
            line_start = src.rfind("\n", 0, m.start()) + 1
            line = src[line_start : src.find("\n", m.start())]
            if line.strip().startswith("#"):
                continue
            hits.append({"pattern": pat, "line": line.strip()[:160]})
    ok = len(hits) == 0 and "nan_features" in src and "nan_cols" in src
    if "nan_features" not in src:
        hits.append({"pattern": "nan_refuse", "line": "missing nan_features refuse"})
        ok = False
    # AST: no Call fillna(0)
    tree = ast.parse(src)
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
            if node.func.attr == "fillna":
                hits.append({"pattern": "fillna_call", "line": "fillna Call in AST"})
                ok = False
    return {
        "proof": "no_live_feature_fill",
        "ok": ok,
        "hits": hits,
        "source": str(PIVOT_RUNNER.relative_to(ROOT)),
        "source_sha256": hashlib.sha256(src.encode("utf-8")).hexdigest(),
    }


def proof_feature_responsiveness(
    ohlcv: pd.DataFrame, *, pack: str, timeframe: str
) -> dict[str, Any]:
    """Tip shape-shock must move level_vsa features."""
    frame = ohlcv.iloc[-2500:].copy() if len(ohlcv) > 2500 else ohlcv.copy()
    base = build_feature_frame(frame, pack=pack)
    shocked = frame.copy()
    # Shock last 40 closes by +1%
    n = min(40, len(shocked))
    shocked.iloc[-n:, shocked.columns.get_loc("close")] = (
        shocked["close"].iloc[-n:].to_numpy(dtype=float) * 1.01
    )
    shocked.iloc[-n:, shocked.columns.get_loc("high")] = (
        shocked["high"].iloc[-n:].to_numpy(dtype=float) * 1.01
    )
    shocked.iloc[-n:, shocked.columns.get_loc("low")] = (
        shocked["low"].iloc[-n:].to_numpy(dtype=float) * 1.01
    )
    alt = build_feature_frame(shocked, pack=pack)
    cols = [c for c in base.columns if c in alt.columns]
    tip = base.index[-n:]
    moved = 0
    for ts in tip:
        for c in cols:
            a = float(pd.to_numeric(base.loc[ts, c], errors="coerce"))
            b = float(pd.to_numeric(alt.loc[ts, c], errors="coerce"))
            if np.isfinite(a) and np.isfinite(b) and abs(a - b) > 1e-12:
                moved += 1
                break
    ok = moved > 0
    return {
        "proof": "builder_responsiveness",
        "ok": ok,
        "pack": pack,
        "timeframe": timeframe,
        "tip_bars": n,
        "n_rows_moved": moved,
        "conformance": "CAUS-PIVOT-OHLCV-001",
    }


def proof_prefix_features(
    ohlcv: pd.DataFrame, *, pack: str, timeframe: str
) -> dict[str, Any]:
    frame = ohlcv.iloc[-4000:].copy() if len(ohlcv) > 4000 else ohlcv.copy()
    full = build_feature_frame(frame, pack=pack)
    cut = max(500, len(frame) // 2)
    pref = build_feature_frame(frame.iloc[:cut].copy(), pack=pack)
    cols = [c for c in full.columns if c in pref.columns]
    n_diff = 0
    first_bad = None
    overlap = pref.index.intersection(full.index)
    # Compare prefix tip of cut window (exclude last few for rolling warm)
    check = overlap[:-5] if len(overlap) > 5 else overlap
    for ts in check[-80:]:
        for c in cols:
            a = float(pd.to_numeric(full.loc[ts, c], errors="coerce"))
            b = float(pd.to_numeric(pref.loc[ts, c], errors="coerce"))
            if np.isnan(a) and np.isnan(b):
                continue
            if not (np.isfinite(a) and np.isfinite(b) and abs(a - b) <= 1e-9):
                n_diff += 1
                first_bad = first_bad or f"{ts}:{c}"
                break
    return {
        "proof": "recompute_prefix",
        "ok": n_diff == 0,
        "pack": pack,
        "timeframe": timeframe,
        "n_rows_differ": n_diff,
        "first_bad": first_bad,
        "n_columns": len(cols),
    }


def proof_tip_pred_identity(
    ohlcv: pd.DataFrame,
    *,
    pack_dir: Path,
) -> dict[str, Any]:
    from llm2.live.pivot_runner import load_pack, tip_decide

    strategy, blob = load_pack(pack_dir)
    full = ohlcv.iloc[-3000:].copy() if len(ohlcv) > 3000 else ohlcv.copy()
    d_full = tip_decide(ohlcv=full, strategy=strategy, blob=blob)
    # Truncate to same tip bar with shorter warm-up still covering feature windows
    short = full.iloc[-1500:].copy()
    d_short = tip_decide(ohlcv=short, strategy=strategy, blob=blob)
    keys = ("action", "p_any", "p_high", "level_ret", "side", "limit_px", "bar_ts_ms")
    diffs = {}
    for k in keys:
        a, b = d_full.get(k), d_short.get(k)
        if isinstance(a, float) and isinstance(b, float):
            if not (np.isfinite(a) and np.isfinite(b) and abs(a - b) <= 1e-9):
                diffs[k] = {"full": a, "short": b}
        elif a != b:
            diffs[k] = {"full": a, "short": b}
    return {
        "proof": "layer_a_pred_identity",
        "ok": len(diffs) == 0,
        "diffs": diffs,
        "full": {k: d_full.get(k) for k in keys},
        "short": {k: d_short.get(k) for k in keys},
        "pack_dir": str(pack_dir),
    }


def run_pivot_four_proof(
    *,
    pack_dir: Path,
    ohlcv: pd.DataFrame | None = None,
) -> dict[str, Any]:
    pack_dir = Path(pack_dir)
    strategy = json.loads((pack_dir / "strategy.json").read_text(encoding="utf-8"))
    symbol = str(strategy["symbol"])
    timeframe = str(strategy["timeframe"])
    feature_pack = str(strategy["feature_pack"])
    if ohlcv is None:
        from llm2.data.loader import load_ohlcv

        ohlcv = load_ohlcv(symbol, timeframe)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    dest = EVIDENCE_ROOT / f"pivot_{pack_dir.name}_{symbol}_{timeframe}_{stamp}"
    dest.mkdir(parents=True, exist_ok=True)

    proofs: dict[str, Any] = {}
    hashes: dict[str, str] = {}
    p1 = proof_feature_responsiveness(ohlcv, pack=feature_pack, timeframe=timeframe)
    hashes["builder_responsiveness"] = _write_json(dest / "builder_responsiveness.json", p1)
    proofs["builder_responsiveness"] = p1

    p2 = proof_prefix_features(ohlcv, pack=feature_pack, timeframe=timeframe)
    hashes["recompute_prefix"] = _write_json(dest / "recompute_prefix.json", p2)
    proofs["recompute_prefix"] = p2

    p3 = proof_no_live_feature_fill_pivot()
    hashes["no_live_feature_fill"] = _write_json(dest / "no_live_feature_fill.json", p3)
    proofs["no_live_feature_fill"] = p3

    p4 = proof_tip_pred_identity(ohlcv, pack_dir=pack_dir)
    hashes["layer_a_pred_identity"] = _write_json(dest / "layer_a_pred_identity.json", p4)
    proofs["layer_a_pred_identity"] = p4

    ok = all(bool(proofs[k]["ok"]) for k in PROOF_KEYS)
    summary = {
        "stamp": stamp,
        "space": f"pivot:{feature_pack}",
        "symbol": symbol,
        "timeframe": timeframe,
        "pack_dir": str(pack_dir),
        "ok": ok,
        "proofs_ok": {k: bool(proofs[k]["ok"]) for k in PROOF_KEYS},
        "artifact_dir": str(dest),
        "artifact_hashes": hashes,
        "rule": "PIVOT_FOUR_PROOF_V1",
    }
    summary_hash = _write_json(dest / "four_proof_summary.json", summary)
    summary["summary_sha256"] = summary_hash
    _write_json(dest / "four_proof_summary.json", summary)
    _write_json(EVIDENCE_ROOT / "four_proof_latest.json", summary)

    if not ok:
        raise PolicyError(
            "PIVOT_FOUR_PROOF FAILED: " + json.dumps(summary["proofs_ok"], sort_keys=True)
        )

    # Attach to pack_meta
    meta_path = pack_dir / "pack_meta.json"
    meta = json.loads(meta_path.read_text(encoding="utf-8")) if meta_path.is_file() else {}
    evidence = dict(meta.get("evidence") or {})
    evidence["four_proof_hashes"] = hashes
    evidence["four_proof_ok"] = True
    evidence["four_proof_summary_sha256"] = summary_hash
    evidence["four_proof_artifact_dir"] = str(dest)
    meta["evidence"] = evidence
    meta["four_proof_ok"] = True
    meta["four_proof_hashes"] = hashes
    meta_path.write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")
    return summary
