"""Compare post-fix live pred_mean to full warehouse recompute (same model)."""
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

BAR = pd.Timestamp("2026-08-05 09:00:00", tz="UTC")
LIVE_PRED = -0.4619535933616573
LIVE_SIDE = -1
PACK = ROOT / "artifacts/live_packs/structure_v1_ethusdt_direction"
WAREHOUSE = Path(r"D:\projectsdata\indicators\indicators.sqlite")
CANDLES = Path(r"D:\projectsdata\candles\market_ohlcv.sqlite")
OUT = ROOT / "artifacts/reports/live_pred_post_fix_ETHUSDT_20260805T0900.json"


def main() -> int:
    from tradesim.ensure_source import prefer_botsgeneral_tradesim

    prefer_botsgeneral_tradesim()
    os.environ["LLM2_INDICATORS_DB"] = str(WAREHOUSE)
    os.environ["LLM2_STRUCTURE_SOURCE"] = "binance"
    from llm2.data.indicators import clear_indicator_cache
    from llm2.features.registry import build_space

    blob = joblib.load(PACK / "model.joblib")
    cols = list(blob["feature_columns"])
    end = int(BAR.value // 10**6)
    import sqlite3

    con = sqlite3.connect(f"file:{CANDLES}?mode=ro", uri=True)
    rows = con.execute(
        """
        SELECT ts_ms, open, high, low, close, volume FROM market_ohlcv
        WHERE symbol='ETHUSDT' AND timeframe='1h' AND source='binance'
          AND price_type='last_price' AND ts_ms<=?
        ORDER BY ts_ms DESC LIMIT 3000
        """,
        (end,),
    ).fetchall()
    con.close()
    rows = list(reversed(rows))
    idx = pd.to_datetime([r[0] for r in rows], unit="ms", utc=True)
    ohlcv = pd.DataFrame(
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
    assert ohlcv.index[-1] == BAR, ohlcv.index[-1]
    clear_indicator_cache()
    feats = build_space(
        ohlcv, "structure_v1", symbol="ETHUSDT", timeframe="1h", recent_only=False
    )
    row = feats.reindex(columns=cols).iloc[[-1]]
    for c in row.columns:
        if c == "last_retrace_pct" or str(c).startswith("last_retrace_pct_"):
            row[c] = row[c].fillna(0.0)
    pred = blob["model"].predict(row.to_numpy(dtype=float))
    mean = float(np.asarray(pred.mean if hasattr(pred, "mean") else pred).reshape(-1)[0])
    side = 1 if mean > 0.1 else (-1 if mean < -0.1 else 0)
    abs_diff = abs(mean - LIVE_PRED)
    report = {
        "evidence_class": "LIVE_PRED_POST_FIX",
        "maximum_earned_readiness": "LIVE_STOP / RESEARCH_ONLY",
        "bar_ts": BAR.isoformat(),
        "live_pred_mean": LIVE_PRED,
        "live_side": LIVE_SIDE,
        "warehouse_pred_mean": mean,
        "warehouse_side": side,
        "abs_diff": abs_diff,
        "side_match": side == LIVE_SIDE,
        "close_match_1e3": abs_diff < 1e-3,
        "note": (
            "Post full-history slice refresh + feature_snapshot. "
            "Pre-fix ledger bars remain non-reproducible."
        ),
        "generated_utc": datetime.now(timezone.utc).isoformat(),
    }
    OUT.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps(report, indent=2))
    return 0 if report["side_match"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
