"""Causal access to the Fibonacci market-structure warehouse.

``D:\\projectsdata\\indicators\\indicators.sqlite`` holds confirmed swing points, structure
labels (higher high, higher low, lower high, lower low), impulse and correction legs,
Fibonacci retracement and extension grids, and distances to prior confirmed support and
resistance, for 179 series at 15m/1h/4h/1w.

**Swing structure is the most leakage-prone indicator family that exists**, because a pivot
at bar ``i`` is only a pivot once ``swing_right`` further bars have printed. A warehouse
that stamps the pivot at ``i`` rather than at ``i + swing_right`` hands the model a free
look into the future at every swing. This one does not: it stores ``pivot_i``/``pivot_ts_ms``
separately from ``confirm_i``/``confirm_ts_ms``, and ``bar_features`` cites only swings and
levels already confirmed. That was verified rather than assumed, over 60,466 BTCUSDT 1h bars:

- swing highs cited before confirmation: 0
- swing lows cited before confirmation: 0
- nearest support / resistance cited before confirmation: 0
- support above the close, or resistance below it: 0
- Fibonacci anchors that are not actual confirmed swing prices: 0
- structure labels disagreeing with the last event at or before the bar: 0

``ts_ms`` follows the same convention as ``market_ohlcv``: it is the bar's **open** instant,
and the row describes the state once that bar has closed. It is therefore knowable at
``ts_ms + timeframe``, exactly like the bar's own close, which is why same-timeframe use
needs no shift while cross-timeframe use must align on completion.
"""

from __future__ import annotations

import os
import sqlite3
from functools import lru_cache
from pathlib import Path

import numpy as np
import pandas as pd

from llm2.data.macro import align_causal
from llm2.paths import TF_MS

_DEFAULT_INDICATORS_DB = Path(r"D:\projectsdata\indicators\indicators.sqlite")


def indicators_db_path() -> Path:
    """Resolve the indicators warehouse, honouring live ``LLM2_INDICATORS_DB`` overrides.

    Must be read at call time — not import time — so VPS micro-live can point at the pack
    slice after the module has already been imported.
    """
    return Path(os.environ.get("LLM2_INDICATORS_DB") or _DEFAULT_INDICATORS_DB)


# Back-compat name: some call sites still import INDICATORS_DB. Prefer indicators_db_path().
INDICATORS_DB = _DEFAULT_INDICATORS_DB

# The only parameterisation present in the warehouse. Recorded explicitly so that a future
# reparameterisation is a visible change rather than a silent one.
SWING_LEFT = 2
SWING_RIGHT = 2

# Price-valued columns are deliberately excluded from every feature path. A raw level such
# as ``fib_0618`` or ``nearest_support`` is non-stationary and its magnitude carries the
# calendar: a model trained on 2019 prices and tested on 2025 prices will read the level as
# a date. Only the scale-free ``dist_*_pct`` forms and ratios are used.
PRICE_COLUMNS = (
    "close",
    "last_sh_price",
    "last_sl_price",
    "nearest_support",
    "nearest_resistance",
    "fib_0000",
    "fib_0236",
    "fib_0382",
    "fib_0500",
    "fib_0618",
    "fib_0786",
    "fib_1000",
    "fib_1272",
    "fib_1618",
    "fib_2000",
    "fib_2618",
)

SCALE_FREE_COLUMNS = (
    "dist_last_sh_pct",
    "dist_last_sl_pct",
    "dist_fib_0236_pct",
    "dist_fib_0382_pct",
    "dist_fib_0500_pct",
    "dist_fib_0618_pct",
    "dist_fib_0786_pct",
    "dist_support_pct",
    "dist_resistance_pct",
    "last_leg_len_pct",
    "last_retrace_pct",
)

CATEGORICAL_COLUMNS = (
    "structure_bias",
    "last_structure_label",
    "last_leg_dir",
    "last_leg_kind",
)

STRUCTURE_LABELS = ("HH", "HL", "LH", "LL")

# ``last_retrace_pct`` reaches 963 in the BTCUSDT 1h series: a "retracement" beyond the
# prior leg is a breakout, and its magnitude past that point is not meaningful. Clipping
# keeps the informative range without letting a handful of bars dominate any fit.
RETRACE_CLIP = (-1.0, 2.0)


def timeframe_ms(timeframe: str) -> int:
    """Bar length in milliseconds, refusing to guess.

    A default here is dangerous rather than convenient. ``TF_MS`` did not originally carry
    a ``1w`` entry, and a fallback of one hour would have declared a weekly bar complete
    one hour after it opened, leaking six days and twenty-three hours into every weekly
    context column while every test still passed.
    """
    step = TF_MS.get(timeframe)
    if step is None:
        raise KeyError(
            f"unknown timeframe {timeframe!r}; add it to llm2.paths.TF_MS rather than "
            "letting completion-time alignment assume a length"
        )
    return step


def _default_source(symbol: str) -> str:
    """Vendor that produced the structure for a symbol, matching the macro registry.

    Live packs set ``LLM2_STRUCTURE_SOURCE=binance`` (research parity). Execution remains
    on Bybit; only signal candles / structure rows use this source.
    """
    override = (os.environ.get("LLM2_STRUCTURE_SOURCE") or "").strip()
    if override:
        return override
    from llm2.data.macro import _BY_SYMBOL

    spec = _BY_SYMBOL.get(symbol.upper())
    if spec is not None:
        return spec.source
    return "binance"


@lru_cache(maxsize=64)
def load_bar_features(
    symbol: str,
    timeframe: str,
    *,
    source: str | None = None,
    min_ts_ms: int | None = None,
) -> pd.DataFrame:
    """Structure features for one series, indexed by bar open instant.

    The index matches ``market_ohlcv`` exactly, so joining to a decision frame on the same
    symbol and timeframe requires no shift. Cross-timeframe use must go through
    :func:`align_multi_timeframe`, which respects completion.

    ``min_ts_ms`` (when set) reads only bars at/after that open instant — required on the
    VPS live slice so a decision does not scan the full multi-year warehouse copy.
    """
    db = indicators_db_path()
    if not db.is_file():
        raise FileNotFoundError(f"Indicator warehouse missing: {db}")

    src = source or _default_source(symbol)
    conn = sqlite3.connect(f"file:{db}?mode=ro", uri=True, timeout=120.0)
    try:
        conn.execute("PRAGMA busy_timeout=120000")
        if min_ts_ms is None:
            df = pd.read_sql(
                "SELECT * FROM bar_features WHERE symbol = ? AND timeframe = ? AND source = ? "
                "AND swing_left = ? AND swing_right = ? ORDER BY ts_ms",
                conn,
                params=(symbol.upper(), timeframe, src, SWING_LEFT, SWING_RIGHT),
            )
        else:
            df = pd.read_sql(
                "SELECT * FROM bar_features WHERE symbol = ? AND timeframe = ? AND source = ? "
                "AND swing_left = ? AND swing_right = ? AND ts_ms >= ? ORDER BY ts_ms",
                conn,
                params=(
                    symbol.upper(),
                    timeframe,
                    src,
                    SWING_LEFT,
                    SWING_RIGHT,
                    int(min_ts_ms),
                ),
            )
    finally:
        conn.close()

    if df.empty:
        raise ValueError(f"No structure for {symbol} {timeframe} source={src}")

    df.index = pd.to_datetime(df["ts_ms"].to_numpy(), unit="ms", utc=True)
    df.index.name = "timestamp"
    return df[~df.index.duplicated(keep="last")].sort_index()


def available_structure(timeframe: str) -> list[str]:
    """Symbols with structure at ``timeframe``."""
    db = indicators_db_path()
    if not db.is_file():
        return []
    conn = sqlite3.connect(f"file:{db}?mode=ro", uri=True, timeout=60.0)
    try:
        rows = conn.execute(
            "SELECT DISTINCT symbol FROM series WHERE timeframe = ? ORDER BY symbol", (timeframe,)
        ).fetchall()
    finally:
        conn.close()
    return [r[0] for r in rows]


def structure_frame(
    symbol: str,
    timeframe: str,
    *,
    source: str | None = None,
    min_ts_ms: int | None = None,
) -> pd.DataFrame:
    """Scale-free structure features for one series.

    Raw price levels are dropped; distances, ratios, ages and encoded categoricals remain.
    """
    raw = load_bar_features(
        symbol, timeframe, source=source, min_ts_ms=min_ts_ms
    )
    step_ms = timeframe_ms(timeframe)
    out = pd.DataFrame(index=raw.index)

    for col in SCALE_FREE_COLUMNS:
        if col in raw.columns:
            out[col] = pd.to_numeric(raw[col], errors="coerce")
    if "last_retrace_pct" in out.columns:
        out["last_retrace_pct"] = out["last_retrace_pct"].clip(*RETRACE_CLIP)

    # Age of the structure. A swing high three bars old and one three hundred bars old are
    # very different situations that the distance column alone cannot distinguish.
    for prefix, ts_col in (("sh", "last_sh_ts_ms"), ("sl", "last_sl_ts_ms")):
        if ts_col in raw.columns:
            age = (raw["ts_ms"] - pd.to_numeric(raw[ts_col], errors="coerce")) / step_ms
            out[f"bars_since_{prefix}"] = age.where(age >= 0)

    # Where the close sits inside the current Fibonacci grid, as a fraction of the leg.
    if {"fib_0000", "fib_1000", "close"} <= set(raw.columns):
        span = raw["fib_1000"] - raw["fib_0000"]
        out["fib_position"] = ((raw["close"] - raw["fib_0000"]) / span.replace(0, np.nan)).clip(-2, 3)

    # Is the nearer barrier above or below? 0.5 is symmetric, above 0.5 means resistance is
    # further away than support, i.e. more room to run up than down.
    if {"dist_support_pct", "dist_resistance_pct"} <= set(raw.columns):
        total = raw["dist_support_pct"].abs() + raw["dist_resistance_pct"].abs()
        out["sr_asymmetry"] = (raw["dist_resistance_pct"].abs() / total.replace(0, np.nan)).clip(0, 1)

    if "structure_bias" in raw.columns:
        out["structure_bias"] = pd.to_numeric(raw["structure_bias"], errors="coerce")
    if "last_structure_label" in raw.columns:
        # ``structure_bias`` is near-constant and therefore close to useless as a trend
        # state: it reads +1 on 93.7% of BTCUSDT 1h bars, 98.1% of ETHUSDT and 99.2% of
        # XAUUSD. Conditioning on it produces one bucket holding almost everything.
        # The Dow reading of the same structure — higher high or higher low is an uptrend,
        # lower high or lower low a downtrend — splits within a point of 50/50 on every
        # series checked, and is the state actually worth conditioning on.
        lab = raw["last_structure_label"].astype(str)
        out["struct_dir"] = np.where(
            lab.isin(("HH", "HL")), 1.0, np.where(lab.isin(("LH", "LL")), -1.0, np.nan)
        )
    if "last_leg_dir" in raw.columns:
        out["leg_dir_up"] = (raw["last_leg_dir"] == "up").astype(float)
    if "last_leg_kind" in raw.columns:
        out["leg_impulse"] = (raw["last_leg_kind"] == "impulse").astype(float)
    if "last_structure_label" in raw.columns:
        for label in STRUCTURE_LABELS:
            out[f"struct_{label}"] = (raw["last_structure_label"] == label).astype(float)

    return out.replace([np.inf, -np.inf], np.nan)


def structure_labels(symbol: str, timeframe: str, *, source: str | None = None) -> pd.Series:
    """The raw higher-high / higher-low / lower-high / lower-low label per bar."""
    raw = load_bar_features(symbol, timeframe, source=source)
    series = raw["last_structure_label"].astype(str)
    return series.where(series.isin(STRUCTURE_LABELS))


def align_multi_timeframe(
    frame: pd.DataFrame,
    target_index: pd.DatetimeIndex,
    source_timeframe: str,
) -> pd.DataFrame:
    """As-of join a higher-timeframe structure frame onto a lower-timeframe decision index.

    A 4-hour row stamped ``T`` describes the state once that 4-hour bar has closed, so it is
    knowable at ``T + 4h`` and must not be visible to the 1-hour bars inside it. Forward
    filling from ``T`` would leak up to four hours; this shifts to the completion instant
    first and then joins as-of.
    """
    step = pd.Timedelta(milliseconds=timeframe_ms(source_timeframe))
    target_index = pd.DatetimeIndex(target_index)
    out = pd.DataFrame(index=target_index)
    for col in frame.columns:
        series = frame[col].dropna()
        if series.empty:
            continue
        series.index = series.index + step
        out[col] = align_causal(series, target_index)["value"]
    return out


def clear_indicator_cache() -> None:
    load_bar_features.cache_clear()
