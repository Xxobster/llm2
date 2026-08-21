"""Causal news density features from ``news_events.sqlite``.

Uses ``first_seen_at`` only (ingestion knowledge time), never retroactive
``event_start_at`` revisions. A document contributes to bar ``T`` (open) only if
``first_seen_at <= T + timeframe`` (bar close / completion).

Labels are sparse (document_label ≈ 20 rows); density/count features do not
require sentiment labels. Empty market_reaction is intentional — no reaction
targets here.
"""

from __future__ import annotations

import sqlite3
from functools import lru_cache

import numpy as np
import pandas as pd

from llm2.paths import NEWS_EVENTS_DB, TF_MS


@lru_cache(maxsize=4)
def _load_first_seen_ms() -> np.ndarray:
    if not NEWS_EVENTS_DB.is_file():
        raise FileNotFoundError(f"news warehouse missing: {NEWS_EVENTS_DB}")
    conn = sqlite3.connect(f"file:{NEWS_EVENTS_DB}?mode=ro", uri=True, timeout=60.0)
    try:
        # Prefer source_document (raw knowledge time); fall back canonical_event.
        rows = conn.execute(
            "SELECT first_seen_at FROM source_document "
            "WHERE first_seen_at IS NOT NULL"
        ).fetchall()
        if not rows:
            rows = conn.execute(
                "SELECT first_seen_at FROM canonical_event WHERE first_seen_at IS NOT NULL"
            ).fetchall()
    finally:
        conn.close()
    if not rows:
        return np.asarray([], dtype=np.int64)
    ts = pd.to_datetime([r[0] for r in rows], utc=True, errors="coerce")
    ts = ts[~pd.isna(ts)]
    ms = (ts.asi8 // 1_000_000).astype(np.int64)
    ms.sort()
    return ms


@lru_cache(maxsize=4)
def _load_platform_first_seen() -> dict[str, np.ndarray]:
    """Per-platform first_seen arrays for optional density splits."""
    if not NEWS_EVENTS_DB.is_file():
        return {}
    conn = sqlite3.connect(f"file:{NEWS_EVENTS_DB}?mode=ro", uri=True, timeout=60.0)
    try:
        rows = conn.execute(
            "SELECT source_platform, first_seen_at FROM source_document "
            "WHERE first_seen_at IS NOT NULL"
        ).fetchall()
    finally:
        conn.close()
    if not rows:
        return {}
    plats: dict[str, list[str]] = {}
    for plat, fs in rows:
        p = str(plat or "unknown").lower()
        plats.setdefault(p, []).append(fs)
    out: dict[str, np.ndarray] = {}
    for p, vals in plats.items():
        ts = pd.to_datetime(vals, utc=True, errors="coerce")
        ts = ts[~pd.isna(ts)]
        ms = (ts.asi8 // 1_000_000).astype(np.int64)
        ms.sort()
        out[p] = ms
    return out


def _count_in_window(events_ms: np.ndarray, end_ms: np.ndarray, window_ms: int) -> np.ndarray:
    """Count events with first_seen in (end - window, end] — vectorized via searchsorted."""
    if events_ms.size == 0:
        return np.zeros(len(end_ms), dtype=float)
    right = np.searchsorted(events_ms, end_ms, side="right")
    left = np.searchsorted(events_ms, end_ms - int(window_ms), side="right")
    return (right - left).astype(float)


def build_news_v1(
    ohlcv: pd.DataFrame,
    *,
    symbol: str | None = None,
    timeframe: str = "1h",
) -> pd.DataFrame:
    """News count / surprise density known by each decision-bar close.

    ``symbol`` is accepted for API uniformity with other builders; counts are
    market-wide (asset-linked entities are too sparse to gate today).
    """
    _ = symbol  # reserved for future entity/asset filters
    target_idx = pd.DatetimeIndex(pd.to_datetime(ohlcv.index, utc=True))
    unique_idx = target_idx[~target_idx.duplicated(keep="last")]
    step_ms = int(TF_MS[timeframe])
    # Decision bar open → completion = close knowledge time.
    open_ms = (unique_idx.asi8 // 1_000_000).astype(np.int64)
    close_ms = open_ms + step_ms

    try:
        all_ms = _load_first_seen_ms()
        by_plat = _load_platform_first_seen()
    except FileNotFoundError:
        all_ms = np.asarray([], dtype=np.int64)
        by_plat = {}

    out_u = pd.DataFrame(index=unique_idx)
    # Rolling density windows in hours of decision TF bars.
    for hours, name in ((1, "1h"), (6, "6h"), (24, "24h"), (168, "7d")):
        w_ms = int(hours * 3_600_000)
        out_u[f"news_n_{name}"] = _count_in_window(all_ms, close_ms, w_ms)

    # Surprise: 1h count vs prior 7d mean (shifted so current bar is out of window).
    n1 = out_u["news_n_1h"]
    roll_mean = n1.shift(1).rolling(168, min_periods=24).mean()
    roll_std = n1.shift(1).rolling(168, min_periods=24).std()
    z = (n1 - roll_mean) / roll_std.replace(0, np.nan)
    # Sparse news eras leave undefined z; 0 = "no surprise signal" not a NaN mask
    # that would dropna() the entire row (and destroy structure columns).
    out_u["news_z_1h_vs_7d"] = z.fillna(0.0)
    out_u["news_log1p_1h"] = np.log1p(n1)
    out_u["news_log1p_24h"] = np.log1p(out_u["news_n_24h"])

    # Major platforms only (avoid high-card dummies).
    for plat, key in (
        ("telegram", "tg"),
        ("bluesky", "bsky"),
        ("rss", "rss"),
        ("gdelt", "gdelt"),
    ):
        arr = by_plat.get(plat, np.asarray([], dtype=np.int64))
        out_u[f"news_n_24h_{key}"] = _count_in_window(arr, close_ms, 24 * 3_600_000)

    out = out_u.reindex(target_idx)
    out.index = ohlcv.index
    return out.replace([np.inf, -np.inf], np.nan)


def build_structure_news_v1(
    ohlcv: pd.DataFrame,
    *,
    symbol: str,
    timeframe: str = "1h",
    **kwargs,
) -> pd.DataFrame:
    from llm2.features.structure_v1 import build_structure_v1

    s = build_structure_v1(ohlcv, symbol=symbol, timeframe=timeframe, **kwargs)
    n = build_news_v1(ohlcv, symbol=symbol, timeframe=timeframe)
    return s.join(n, how="left")


def build_structure_oi_news_v1(
    ohlcv: pd.DataFrame,
    *,
    symbol: str,
    timeframe: str = "1h",
    **kwargs,
) -> pd.DataFrame:
    from llm2.features.oi_v1 import build_oi_v1
    from llm2.features.structure_v1 import build_structure_v1

    s = build_structure_v1(ohlcv, symbol=symbol, timeframe=timeframe, **kwargs)
    o = build_oi_v1(ohlcv, symbol=symbol, timeframe=timeframe)
    n = build_news_v1(ohlcv, symbol=symbol, timeframe=timeframe)
    return s.join(o, how="left").join(n, how="left")
