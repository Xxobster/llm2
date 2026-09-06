"""FOUR_PROOF_GATE_V1 for the Solana 1-hour Exponential Moving Average stack.

No warehouse join and no model: the live bit is ``signals_from_ohlcv`` plus the
Average-True-Range bracket from ``sim_atr``. The four proofs still apply:

1. **builder_responsiveness** — shocking the tip candles must move features
2. **recompute_prefix** — shared leakage battery on the guard builder
3. **no_live_feature_fill** — live refuses NaN; never invents a stop or bit
4. **layer_a_pred_identity** — live ``tip_signal`` equals research bit / limit / stop
"""

from __future__ import annotations

import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

from llm2.diagonal_sr.bar_series import make_bar_series
from llm2.edge_lab.sim_atr import atr_brackets, limit_prices
from llm2.evidence.four_proof import EVIDENCE_ROOT, PROOF_KEYS, _write_json
from llm2.ml_lab.idea_catalog import signals_from_ohlcv
from llm2.ml_lab.live_guards import SOL_EMA_SPEC
from llm2.ml_lab.live_signal import IDEA, build_features_for_guard, tip_signal
from llm2.paths import ROOT
from llm2.research_policy import PolicyError
from llm2.validation.folds import index_to_ms

SPACE = "ml_lab_ema_stack_v1"
LIVE_SOURCES = (
    ROOT / "llm2" / "live" / "ema_stack_runner.py",
    ROOT / "llm2" / "ml_lab" / "live_signal.py",
)


def _prefer_leakage() -> None:
    from leakage.ensure_source import prefer_botsgeneral_leakage

    prefer_botsgeneral_leakage()
    import leakage

    if "botsgeneral" not in str(leakage.__file__):
        raise PolicyError(f"leakage not from botsgeneral: {leakage.__file__}")


def proof_builder_responsiveness(
    ohlcv: pd.DataFrame, *, symbol: str, timeframe: str
) -> dict[str, Any]:
    _prefer_leakage()
    from leakage.checks import check_builder_responsiveness

    frame = ohlcv.iloc[-2500:].copy() if len(ohlcv) > 2500 else ohlcv.copy()
    findings = check_builder_responsiveness(
        frame, build_features_for_guard, interval=timeframe, compare_rows=40
    )
    return {
        "proof": "builder_responsiveness",
        "ok": len(findings) == 0,
        "space": SPACE,
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
    ohlcv: pd.DataFrame, *, symbol: str, timeframe: str, cuts: int = 2
) -> dict[str, Any]:
    _prefer_leakage()
    from leakage import run_leakage_audit

    frame = ohlcv.iloc[-3000:].copy() if len(ohlcv) > 3000 else ohlcv.copy()
    report = run_leakage_audit(
        ohlcv=frame,
        build_features=build_features_for_guard,
        interval=timeframe,
        symbol=symbol,
        timeframe=timeframe,
        cuts=cuts,
        compare_rows=min(200, max(50, len(frame) // 10)),
        run_forward_corr=False,
        require_decisive=True,
    )
    hard = [
        {"check": f.check.value, "column": f.column, "message": f.message}
        for f in report.findings
        if f.severity.value == "HARD"
    ]
    return {
        "proof": "recompute_prefix",
        "ok": bool(report.ok),
        "space": SPACE,
        "symbol": symbol,
        "timeframe": timeframe,
        "summary": report.summary(),
        "hard_findings": hard,
        "n_columns": report.n_columns,
    }


def proof_no_live_feature_fill() -> dict[str, Any]:
    forbidden = (
        r"fillna\(0\.0\)",
        r"fillna\(0\)",
        r"nan_to_num",
        r"zero_fill",
    )
    hits: list[dict[str, str]] = []
    sources: dict[str, str] = {}
    for path in LIVE_SOURCES:
        src = path.read_text(encoding="utf-8")
        sources[str(path.relative_to(ROOT))] = hashlib.sha256(src.encode("utf-8")).hexdigest()
        for pat in forbidden:
            for m in re.finditer(pat, src):
                line_start = src.rfind("\n", 0, m.start()) + 1
                line = src[line_start : src.find("\n", m.start())]
                if line.strip().startswith("#"):
                    continue
                hits.append(
                    {
                        "file": str(path.relative_to(ROOT)),
                        "pattern": pat,
                        "line": line.strip()[:160],
                    }
                )
    runner = LIVE_SOURCES[0].read_text(encoding="utf-8")
    signal = LIVE_SOURCES[1].read_text(encoding="utf-8")
    required = {
        "runner_nan_refuse": ("nan_features" in runner) and ("nan_cols" in runner),
        "signal_nan_cols": "nan_cols" in signal,
        "signal_isfinite_check": "np.isfinite" in signal,
        "pack_fail_loud": "REQUIRED_PACK_KEYS" in runner,
        "no_taker_fallback": "refuse_taker_entry_fallback" in runner,
        "risk_fraction_sizing": "RISK_FRACTION" in runner,
    }
    for name, present in required.items():
        if not present:
            hits.append({"file": "-", "pattern": name, "line": "missing required guard"})
    return {
        "proof": "no_live_feature_fill",
        "ok": len(hits) == 0,
        "space": SPACE,
        "hits": hits,
        "required_guards": required,
        "sources_sha256": sources,
    }


def proof_layer_a_pred_identity(
    ohlcv: pd.DataFrame,
    *,
    symbol: str,
    timeframe: str,
    tip_bars: int = 24,
) -> dict[str, Any]:
    from llm2.live.pivot_runner import LIVE_OHLCV_BARS

    spec = dict(SOL_EMA_SPEC)
    spec["symbol"] = symbol
    spec["timeframe"] = timeframe
    occ = signals_from_ohlcv(ohlcv, timeframe)[IDEA]
    sc = make_bar_series(symbol, timeframe, ohlcv)
    ts = index_to_ms(ohlcv.index)
    n = len(ohlcv)
    rows: list[dict[str, Any]] = []
    n_diff = 0
    max_px_diff = 0.0
    max_sl_diff = 0.0
    for k in range(n - int(tip_bars), n):
        lo = max(0, k + 1 - int(LIVE_OHLCV_BARS))
        prefix = ohlcv.iloc[lo : k + 1]
        sig = tip_signal(prefix, spec=spec)
        research_fires = bool(float(occ[k]) >= 0.5)
        sl_arr, tp_arr = atr_brackets(
            np.asarray([sc.atr_frac[k]], dtype=float),
            k_sl=float(spec["k_sl"]),
            tp_ratio=float(spec["tp_ratio"]),
            sl_cap=float(spec["sl_cap"]),
        )
        lim = limit_prices(
            np.asarray([sc.close[k]], dtype=float),
            np.asarray([sc.atr_frac[k]], dtype=float),
            np.asarray([False], dtype=bool),
        )
        px_diff = abs(float(sig.limit_px) - float(lim[0]))
        sl_diff = abs(float(sig.sl_pct) - float(sl_arr[0]))
        tp_diff = abs(float(sig.tp_pct) - float(tp_arr[0]))
        max_px_diff = max(max_px_diff, px_diff)
        max_sl_diff = max(max_sl_diff, sl_diff)
        bad = (
            (bool(sig.fires) != research_fires)
            or (int(sig.bar_ts_ms) != int(ts[k]))
            or px_diff > 1e-9
            or sl_diff > 1e-12
            or tp_diff > 1e-12
        )
        if bad:
            n_diff += 1
            rows.append(
                {
                    "bar_ts_ms": int(ts[k]),
                    "live_fires": bool(sig.fires),
                    "research_fires": research_fires,
                    "limit_px_diff": px_diff,
                    "sl_diff": sl_diff,
                    "tp_diff": tp_diff,
                    "nan_cols": list(sig.nan_cols),
                }
            )
    return {
        "proof": "layer_a_pred_identity",
        "ok": n_diff == 0,
        "space": SPACE,
        "symbol": symbol,
        "timeframe": timeframe,
        "idea": IDEA,
        "tip_bars": int(tip_bars),
        "live_prefix_bars": int(LIVE_OHLCV_BARS),
        "n_decisions_differ": n_diff,
        "max_abs_limit_px_diff": max_px_diff,
        "max_abs_sl_diff": max_sl_diff,
        "mismatches": rows[:20],
        "n_research_fires_in_window": int(np.nansum(np.asarray(occ[-int(tip_bars) :], dtype=float) >= 0.5)),
    }


def run_four_proof_gate_ema_stack(
    *,
    symbol: str,
    timeframe: str,
    ohlcv: pd.DataFrame | None = None,
    tip_bars: int = 24,
    out_dir: Path | None = None,
) -> dict[str, Any]:
    from llm2.data.loader import load_ohlcv

    if ohlcv is None:
        ohlcv = load_ohlcv(symbol, timeframe)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    arm = f"{SPACE}_{IDEA}_{symbol}_{timeframe}"
    dest = out_dir or (EVIDENCE_ROOT / f"{arm}_{stamp}")
    dest.mkdir(parents=True, exist_ok=True)

    proofs: dict[str, Any] = {}
    hashes: dict[str, str] = {}

    p1 = proof_builder_responsiveness(ohlcv, symbol=symbol, timeframe=timeframe)
    hashes["builder_responsiveness"] = _write_json(dest / "builder_responsiveness.json", p1)
    proofs["builder_responsiveness"] = p1
    print(f"  builder_responsiveness ok={p1['ok']} findings={p1['n_findings']}", flush=True)

    p2 = proof_recompute_prefix(ohlcv, symbol=symbol, timeframe=timeframe)
    hashes["recompute_prefix"] = _write_json(dest / "recompute_prefix.json", p2)
    proofs["recompute_prefix"] = p2
    print(f"  recompute_prefix ok={p2['ok']} hard={len(p2['hard_findings'])}", flush=True)

    p3 = proof_no_live_feature_fill()
    hashes["no_live_feature_fill"] = _write_json(dest / "no_live_feature_fill.json", p3)
    proofs["no_live_feature_fill"] = p3
    print(f"  no_live_feature_fill ok={p3['ok']} hits={len(p3['hits'])}", flush=True)

    p4 = proof_layer_a_pred_identity(
        ohlcv, symbol=symbol, timeframe=timeframe, tip_bars=tip_bars
    )
    hashes["layer_a_pred_identity"] = _write_json(dest / "layer_a_pred_identity.json", p4)
    proofs["layer_a_pred_identity"] = p4
    print(
        f"  layer_a_pred_identity ok={p4['ok']} differ={p4['n_decisions_differ']}",
        flush=True,
    )

    ok = all(bool(proofs[k]["ok"]) for k in PROOF_KEYS)
    summary = {
        "stamp": stamp,
        "space": SPACE,
        "symbol": symbol,
        "timeframe": timeframe,
        "idea": IDEA,
        "ok": ok,
        "proofs_ok": {k: bool(proofs[k]["ok"]) for k in PROOF_KEYS},
        "artifact_dir": str(dest),
        "artifact_hashes": hashes,
        "rule": "FOUR_PROOF_GATE_V1",
        "readiness": "RESEARCH_ONLY (gate is causality, not performance)",
    }
    text = json.dumps(summary, indent=2, default=str, sort_keys=True) + "\n"
    (dest / "four_proof_summary.json").write_text(text, encoding="utf-8")
    summary["summary_sha256"] = hashlib.sha256(text.encode("utf-8")).hexdigest()
    return summary
