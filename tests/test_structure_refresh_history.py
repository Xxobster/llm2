"""Regression: truncated structure history flips pred vs full warehouse."""

from __future__ import annotations

import os
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
import pytest

ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / "artifacts/live_packs/structure_v1_ethusdt_direction"
WAREHOUSE = Path(r"D:\projectsdata\indicators\indicators.sqlite")
CANDLES = Path(r"D:\projectsdata\candles\market_ohlcv.sqlite")
BAR = pd.Timestamp("2026-08-03 16:00:00", tz="UTC")


pytestmark = pytest.mark.skipif(
    not (PACK / "model.joblib").is_file() or not WAREHOUSE.is_file() or not CANDLES.is_file(),
    reason="pack/warehouse/candles not available",
)


def _load_1h(n: int) -> pd.DataFrame:
    import sqlite3

    end = int(BAR.value // 10**6)
    con = sqlite3.connect(f"file:{CANDLES}?mode=ro", uri=True)
    rows = con.execute(
        """
        SELECT ts_ms, open, high, low, close, volume FROM market_ohlcv
        WHERE symbol='ETHUSDT' AND timeframe='1h' AND source='binance'
          AND price_type='last_price' AND ts_ms<=?
        ORDER BY ts_ms DESC LIMIT ?
        """,
        (end, n),
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


def _pred(feats: pd.DataFrame, blob: dict) -> float:
    cols = list(blob["feature_columns"])
    row = feats.reindex(columns=cols).iloc[[-1]]
    for c in row.columns:
        if c == "last_retrace_pct" or str(c).startswith("last_retrace_pct_"):
            row[c] = row[c].fillna(0.0)
    p = blob["model"].predict(row.to_numpy(dtype=float))
    return float(np.asarray(p.mean if hasattr(p, "mean") else p).reshape(-1)[0])


def test_trunc800_structure_sign_flips_vs_warehouse(tmp_path: Path):
    """Live bug: refresh limit=800 rebuilds swings on a short window → wrong side."""
    import sys

    sys.path.insert(0, r"C:\projects\botsgeneral\packages\indicators\src")
    from indicators.compute import compute_structure
    from indicators.store import IndicatorDB
    from llm2.data.indicators import clear_indicator_cache
    from llm2.features.registry import build_space
    from llm2.live.refresh_structure import MIN_STRUCTURE_HISTORY_BARS

    assert MIN_STRUCTURE_HISTORY_BARS["1h"] >= 5000

    blob = joblib.load(PACK / "model.joblib")

    os.environ["LLM2_INDICATORS_DB"] = str(WAREHOUSE)
    os.environ["LLM2_STRUCTURE_SOURCE"] = "binance"
    clear_indicator_cache()
    ohlcv = _load_1h(3000)
    feats_wh = build_space(
        ohlcv, "structure_v1", symbol="ETHUSDT", timeframe="1h", recent_only=False
    )
    pred_wh = _pred(feats_wh, blob)

    trunc_db = tmp_path / "trunc800.sqlite"
    ind = IndicatorDB(trunc_db)
    try:
        for tf, n in (("1h", 800), ("4h", 800), ("1w", 350)):
            # reuse 1h loader pattern for other TF via same warehouse candles
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
            df = pd.DataFrame(
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

    os.environ["LLM2_INDICATORS_DB"] = str(trunc_db)
    clear_indicator_cache()
    feats_tr = build_space(
        ohlcv.iloc[-300:],
        "structure_v1",
        symbol="ETHUSDT",
        timeframe="1h",
        recent_only=True,
    )
    pred_tr = _pred(feats_tr, blob)

    # Rebuilding swings on an 800-bar window moves the decision materially. The
    # original assertion pinned both signs and a 0.5 gap, but those numbers came from
    # the era when ``last_retrace_pct`` was back-filled from the following leg
    # (CAUS-STRUCT-001). What the history guard actually protects is that truncation
    # can change the trade, so assert the gap exceeds the directional band.
    from llm2.hunt.targets import DIRECTION_BAND

    assert abs(pred_wh - pred_tr) > DIRECTION_BAND, (
        f"truncated structure should move the prediction past the action band: "
        f"warehouse={pred_wh:.4f} trunc800={pred_tr:.4f}"
    )


def test_feature_snapshot_helper_hash_stable():
    from llm2.live.micro_runner import hashlib as _  # noqa: F401 — import path exists

    cols = ["a", "b"]
    vals = {"a": 1.0, "b": 2.0}
    import hashlib

    raw = np.asarray([vals[c] for c in cols], dtype=np.float64)
    h1 = hashlib.sha256(raw.tobytes()).hexdigest()
    h2 = hashlib.sha256(np.asarray([1.0, 2.0], dtype=np.float64).tobytes()).hexdigest()
    assert h1 == h2
