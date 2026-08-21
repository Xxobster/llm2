"""Causal next-leg retracement labels (hypothesis generator from CAUS-STRUCT-001).

For leg ``i``, ``retrace_pct`` measures how deep leg ``i+1`` retraced leg ``i``.
That number is knowable only when leg ``i+1`` confirms. This module builds:

* ``next_retrace_pct`` — the eventual retrace of the *current* confirmed leg
* ``next_retrace_known_ts_ms`` — when the label becomes knowable
* ``leg_dir`` — +1 up / -1 down of the leg whose retrace we forecast

Features at decision time must not include this label. The published causal
``last_retrace_pct`` feature is the *previous* completed retrace — a different column.
"""

from __future__ import annotations

import sqlite3
from pathlib import Path

import numpy as np
import pandas as pd

from llm2.data.indicators import SWING_LEFT, SWING_RIGHT, indicators_db_path


def _default_source(symbol: str) -> str:
    from llm2.data.indicators import _default_source as _src

    return _src(symbol)


def load_legs_with_confirm(
    symbol: str,
    timeframe: str = "1h",
    *,
    source: str | None = None,
) -> pd.DataFrame:
    """Legs joined to end-swing confirmation timestamps."""
    db = indicators_db_path()
    if not Path(db).is_file():
        raise FileNotFoundError(db)
    src = source or _default_source(symbol)
    con = sqlite3.connect(f"file:{db}?mode=ro", uri=True, timeout=120.0)
    try:
        legs = pd.read_sql(
            "SELECT leg_id, direction, start_swing_id, end_swing_id, "
            "start_ts_ms, end_ts_ms, length_pct, kind, retrace_pct, fib_ratio "
            "FROM legs WHERE symbol=? AND timeframe=? AND source=? "
            "AND swing_left=? AND swing_right=? ORDER BY leg_id",
            con,
            params=(symbol.upper(), timeframe, src, SWING_LEFT, SWING_RIGHT),
        )
        swings = pd.read_sql(
            "SELECT swing_id, confirm_ts_ms FROM swings "
            "WHERE symbol=? AND timeframe=? AND source=? "
            "AND swing_left=? AND swing_right=?",
            con,
            params=(symbol.upper(), timeframe, src, SWING_LEFT, SWING_RIGHT),
        )
    finally:
        con.close()
    if legs.empty:
        raise ValueError(f"no legs for {symbol} {timeframe}")
    conf = swings.set_index("swing_id")["confirm_ts_ms"]
    legs = legs.copy()
    legs["end_confirm_ts_ms"] = legs["end_swing_id"].map(conf)
    legs["start_confirm_ts_ms"] = legs["start_swing_id"].map(conf)
    return legs


def build_next_retrace_leg_table(
    symbol: str,
    timeframe: str = "1h",
    *,
    source: str | None = None,
) -> pd.DataFrame:
    """One row per forecastable leg (needs a confirmed successor).

    Columns:
      decision_ts_ms  — end-swing confirm of leg i (forecast is issued here)
      known_ts_ms     — end-swing confirm of leg i+1 (label becomes knowable)
      next_retrace_pct — retrace_pct of leg i (measured using leg i+1)
      leg_dir         — +1 up / -1 down
    """
    legs = load_legs_with_confirm(symbol, timeframe, source=source)
    rows = []
    for i in range(len(legs) - 1):
        cur = legs.iloc[i]
        nxt = legs.iloc[i + 1]
        y = float(cur["retrace_pct"])
        dec = cur["end_confirm_ts_ms"]
        known = nxt["end_confirm_ts_ms"]
        if not np.isfinite(y) or pd.isna(dec) or pd.isna(known):
            continue
        if int(known) <= int(dec):
            continue
        direction = str(cur["direction"]).lower()
        leg_dir = 1 if direction == "up" else -1 if direction == "down" else 0
        if leg_dir == 0:
            continue
        rows.append(
            {
                "leg_id": int(cur["leg_id"]),
                "decision_ts_ms": int(dec),
                "known_ts_ms": int(known),
                "next_retrace_pct": y,
                "leg_dir": leg_dir,
                "leg_length_pct": float(cur["length_pct"])
                if np.isfinite(float(cur["length_pct"]))
                else np.nan,
                "leg_kind": str(cur["kind"]),
            }
        )
    out = pd.DataFrame(rows)
    if out.empty:
        raise ValueError(f"no forecastable legs for {symbol} {timeframe}")
    return out


def build_next_retrace_sparse_frame(
    symbol: str,
    timeframe: str = "1h",
    *,
    source: str | None = None,
) -> pd.DataFrame:
    """Sparse frame indexed by decision timestamps (leg confirm)."""
    tab = build_next_retrace_leg_table(symbol, timeframe, source=source)
    idx = pd.to_datetime(tab["decision_ts_ms"].to_numpy(), unit="ms", utc=True)
    frame = tab.set_index(idx)
    frame.index.name = "timestamp"
    return frame[~frame.index.duplicated(keep="last")].sort_index()


def build_next_retrace_dense_labels(
    bar_index: pd.DatetimeIndex,
    symbol: str,
    timeframe: str = "1h",
    *,
    source: str | None = None,
) -> pd.DataFrame:
    """Dense labels on the decision bar index.

    Between leg-i confirm and leg-(i+1) confirm, every bar carries the *same*
    eventual ``next_retrace_pct``. This is valid for supervised learning only if
    features exclude the label; purge at fold edges using ``known_ts_ms``.
    """
    tab = build_next_retrace_leg_table(symbol, timeframe, source=source)
    bar_ms = (pd.DatetimeIndex(bar_index).tz_convert("UTC").asi8 // 1_000_000).astype(
        np.int64
    )
    y = np.full(len(bar_ms), np.nan, dtype=float)
    known = np.full(len(bar_ms), -1, dtype=np.int64)
    leg_dir = np.zeros(len(bar_ms), dtype=float)
    # Vectorized assign per leg window [decision, known).
    for row in tab.itertuples(index=False):
        lo = int(row.decision_ts_ms)
        hi = int(row.known_ts_ms)
        mask = (bar_ms >= lo) & (bar_ms < hi)
        y[mask] = float(row.next_retrace_pct)
        known[mask] = hi
        leg_dir[mask] = float(row.leg_dir)
    return pd.DataFrame(
        {
            "next_retrace_pct": y,
            "next_retrace_known_ts_ms": known,
            "leg_dir": leg_dir,
        },
        index=bar_index,
    )
