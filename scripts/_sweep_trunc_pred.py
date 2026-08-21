"""Sweep truncate window lengths to match live pred 0.456."""
from __future__ import annotations

import os
import sys
from pathlib import Path

import joblib
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, r"C:\projects\botsgeneral\packages\indicators\src")

from tradesim.ensure_source import prefer_botsgeneral_tradesim

prefer_botsgeneral_tradesim()

from indicators.compute import compute_structure
from indicators.store import IndicatorDB
from llm2.data.indicators import clear_indicator_cache
from llm2.features.registry import build_space

BAR = pd.Timestamp("2026-08-03 16:00:00", tz="UTC")
LIVE = 0.4560721581125096
CANDLES = Path(r"D:\projectsdata\candles\market_ohlcv.sqlite")
PACK = ROOT / "artifacts/live_packs/structure_v1_ethusdt_direction"
blob = joblib.load(PACK / "model.joblib")
cols = list(blob["feature_columns"])


def load_tf(tf: str, n: int) -> pd.DataFrame:
    import sqlite3

    end = int(BAR.value // 10**6)
    con = sqlite3.connect(f"file:{CANDLES}?mode=ro", uri=True)
    rows = con.execute(
        """
        SELECT ts_ms, open, high, low, close, volume FROM market_ohlcv
        WHERE symbol='ETHUSDT' AND timeframe=? AND source='binance'
          AND price_type='last_price' AND ts_ms<=?
        ORDER BY ts_ms DESC LIMIT ?
        """,
        (tf, end, n),
    ).fetchall()
    con.close()
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


def pred_for(n1h: int, ohlcv_tail: int = 300):
    tmp = ROOT / f"artifacts/reports/_tmp_sweep_{n1h}.sqlite"
    if tmp.exists():
        tmp.unlink()
    ind = IndicatorDB(tmp)
    try:
        for tf, n in (("1h", n1h), ("4h", n1h), ("1w", min(350, n1h))):
            df = load_tf(tf, n)
            ind.upsert_bundle(
                compute_structure(
                    df.reset_index(drop=True),
                    source="binance",
                    symbol="ETHUSDT",
                    timeframe=tf,
                )
            )
    finally:
        ind.close()
    os.environ["LLM2_INDICATORS_DB"] = str(tmp.resolve())
    os.environ["LLM2_STRUCTURE_SOURCE"] = "binance"
    clear_indicator_cache()
    ohlcv = load_tf("1h", max(n1h, ohlcv_tail)).iloc[-ohlcv_tail:]
    feats = build_space(
        ohlcv, "structure_v1", symbol="ETHUSDT", timeframe="1h", recent_only=True
    )
    row = feats.reindex(columns=cols).iloc[[-1]]
    for c in row.columns:
        if c == "last_retrace_pct" or str(c).startswith("last_retrace_pct_"):
            row[c] = row[c].fillna(0.0)
    if row.isna().any(axis=None):
        return None, row.columns[row.iloc[0].isna()].tolist()
    p = blob["model"].predict(row.to_numpy(dtype=float))
    return float(np.asarray(p.mean if hasattr(p, "mean") else p).reshape(-1)[0]), None


def main() -> None:
    best = None
    for n in (200, 300, 400, 500, 600, 700, 800, 900, 1000, 1200, 1500, 2000):
        p, err = pred_for(n)
        d = None if p is None else abs(p - LIVE)
        print(n, p, d, err)
        if p is not None and (best is None or d < best[0]):
            best = (d, n, p)
    print("BEST", best)


if __name__ == "__main__":
    main()
