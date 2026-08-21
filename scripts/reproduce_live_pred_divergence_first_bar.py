"""Reproduce first ETH live pred: truncated 800-bar structure vs full warehouse.

Evidence class: LIVE_FEATURE_PARITY_DIAGNOSTIC (post-lockbox if window includes it).
"""
from __future__ import annotations

import hashlib
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

import joblib
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

BAR_TS = pd.Timestamp("2026-08-03 16:00:00", tz="UTC")
LIVE_PRED = 0.4560721581125096
PACK = ROOT / "artifacts" / "live_packs" / "structure_v1_ethusdt_direction"
WAREHOUSE = Path(r"D:\projectsdata\indicators\indicators.sqlite")
CANDLES = Path(r"D:\projectsdata\candles\market_ohlcv.sqlite")
OUT = ROOT / "artifacts" / "reports" / "live_pred_divergence_first_bar.json"


def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def _load_binance_tf(
    timeframe: str, end_inclusive: pd.Timestamp, *, n_bars: int
) -> pd.DataFrame:
    import sqlite3

    end_ms = int(end_inclusive.value // 1_000_000)
    con = sqlite3.connect(f"file:{CANDLES}?mode=ro", uri=True)
    # Prefer last_price; fall back to densest complete last synonym.
    q = """
    SELECT ts_ms, open, high, low, close, volume
    FROM market_ohlcv
    WHERE symbol='ETHUSDT' AND timeframe=? AND source='binance'
      AND price_type='last_price' AND ts_ms <= ?
    ORDER BY ts_ms DESC
    LIMIT ?
    """
    rows = con.execute(q, (timeframe, end_ms, int(n_bars))).fetchall()
    if len(rows) < max(50, n_bars // 4):
        q2 = """
        SELECT ts_ms, open, high, low, close, volume
        FROM market_ohlcv
        WHERE symbol='ETHUSDT' AND timeframe=? AND source='binance'
          AND price_type IN ('last','last_price') AND ts_ms <= ?
        ORDER BY ts_ms DESC
        LIMIT ?
        """
        rows = con.execute(q2, (timeframe, end_ms, int(n_bars))).fetchall()
    con.close()
    if not rows:
        raise RuntimeError(f"no candles for {timeframe} end={end_inclusive}")
    rows = list(reversed(rows))
    idx = pd.to_datetime([r[0] for r in rows], unit="ms", utc=True)
    return pd.DataFrame(
        {
            "ts_ms": [int(r[0]) for r in rows],
            "open": [float(r[1]) for r in rows],
            "high": [float(r[2]) for r in rows],
            "low": [float(r[3]) for r in rows],
            "close": [float(r[4]) for r in rows],
            "volume": [float(r[5]) for r in rows],
        },
        index=idx,
    )


def _load_binance_1h(end_inclusive: pd.Timestamp, *, n_bars: int) -> pd.DataFrame:
    return _load_binance_tf("1h", end_inclusive, n_bars=n_bars)

def _predict(feats: pd.DataFrame, blob: dict) -> float:
    cols = list(blob["feature_columns"])
    row = feats.reindex(columns=cols).iloc[[-1]]
    for col in row.columns:
        if col == "last_retrace_pct" or str(col).startswith("last_retrace_pct_"):
            row[col] = row[col].fillna(0.0)
    x = row.to_numpy(dtype=float)
    if np.isnan(x).any():
        nan_cols = row.columns[row.iloc[0].isna()].tolist()
        raise RuntimeError(f"NaN features: {nan_cols[:20]}")
    pred = blob["model"].predict(x)
    mean = float(np.asarray(pred.mean if hasattr(pred, "mean") else pred).reshape(-1)[0])
    return mean


def main() -> int:
    from tradesim.ensure_source import prefer_botsgeneral_tradesim

    prefer_botsgeneral_tradesim()

    bg_ind = Path(r"C:\projects\botsgeneral\packages\indicators\src")
    if bg_ind.is_dir() and str(bg_ind) not in sys.path:
        sys.path.insert(0, str(bg_ind))

    blob = joblib.load(PACK / "model.joblib")
    model_sha = _sha256(PACK / "model.joblib")

    # --- Path A: full warehouse structure (today's recompute) ---
    os.environ["LLM2_INDICATORS_DB"] = str(WAREHOUSE)
    os.environ["LLM2_STRUCTURE_SOURCE"] = "binance"
    from llm2.data.indicators import clear_indicator_cache
    from llm2.features.registry import build_space

    clear_indicator_cache()
    ohlcv_fullish = _load_binance_1h(BAR_TS, n_bars=3000)
    assert ohlcv_fullish.index[-1] == BAR_TS, ohlcv_fullish.index[-1]
    feats_wh = build_space(
        ohlcv_fullish,
        "structure_v1",
        symbol="ETHUSDT",
        timeframe="1h",
        recent_only=False,
    )
    pred_wh = _predict(feats_wh, blob)

    # --- Path B: live-like truncated refresh (800 bars) into temp slice ---
    from indicators.compute import compute_structure
    from indicators.store import IndicatorDB

    ohlcv_800 = _load_binance_1h(BAR_TS, n_bars=800)
    assert len(ohlcv_800) == 800
    assert ohlcv_800.index[-1] == BAR_TS

    tmp_db = ROOT / "artifacts" / "reports" / "_tmp_eth_trunc800_slice.sqlite"
    if tmp_db.exists():
        tmp_db.unlink()
    ind = IndicatorDB(tmp_db)
    try:
        for tf, n in (("1h", 800), ("4h", 800), ("1w", 350)):
            df = _load_binance_tf(tf, BAR_TS, n_bars=n)
            bundle = compute_structure(
                df.reset_index(drop=True),
                source="binance",
                symbol="ETHUSDT",
                timeframe=tf,
            )
            ind.upsert_bundle(bundle)
    finally:
        ind.close()
    os.environ["LLM2_INDICATORS_DB"] = str(tmp_db.resolve())
    clear_indicator_cache()
    # Live decide uses ~300 OHLCV bars for vol-normalised cols
    ohlcv_300 = ohlcv_800.iloc[-300:].copy()
    feats_trunc = build_space(
        ohlcv_300,
        "structure_v1",
        symbol="ETHUSDT",
        timeframe="1h",
        recent_only=True,
    )
    pred_trunc = _predict(feats_trunc, blob)

    # Feature diffs at tip
    cols = list(blob["feature_columns"])
    a = feats_wh.reindex(columns=cols).iloc[-1]
    b = feats_trunc.reindex(columns=cols).iloc[-1]
    diffs = []
    for c in cols:
        va, vb = a.get(c), b.get(c)
        if pd.isna(va) and pd.isna(vb):
            continue
        if pd.isna(va) or pd.isna(vb) or float(va) != float(vb):
            diffs.append(
                {
                    "column": c,
                    "warehouse": None if pd.isna(va) else float(va),
                    "trunc800": None if pd.isna(vb) else float(vb),
                    "abs_diff": None
                    if pd.isna(va) or pd.isna(vb)
                    else abs(float(va) - float(vb)),
                }
            )
    diffs.sort(key=lambda d: -(d["abs_diff"] or 1e9))

    report = {
        "evidence_class": "LIVE_PRED_DIVERGENCE_DIAGNOSTIC",
        "maximum_earned_readiness": "LIVE_STOP / RESEARCH_ONLY",
        "bar_ts": BAR_TS.isoformat(),
        "live_ledger_pred_mean": LIVE_PRED,
        "live_ledger_side": 1,
        "model_sha256": model_sha,
        "path_warehouse_pred_mean": pred_wh,
        "path_trunc800_live_like_pred_mean": pred_trunc,
        "abs_live_vs_warehouse": abs(LIVE_PRED - pred_wh),
        "abs_live_vs_trunc800": abs(LIVE_PRED - pred_trunc),
        "trunc800_matches_live": abs(LIVE_PRED - pred_trunc) < 1e-4,
        "warehouse_matches_live": abs(LIVE_PRED - pred_wh) < 1e-4,
        "n_feature_mismatches_wh_vs_trunc": len(diffs),
        "top_feature_diffs": diffs[:15],
        "root_cause_hypothesis": (
            "Live refresh_symbol(limit=800) deletes/rebuilds structure from only "
            "the last 800 OHLCV bars each decision hour. Confirmed-swing geometry "
            "on a truncated window differs from the full-history warehouse; "
            "decisions store no feature snapshot so past decide-time rows are lost."
        ),
        "generated_utc": datetime.now(timezone.utc).isoformat(),
    }
    OUT.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
