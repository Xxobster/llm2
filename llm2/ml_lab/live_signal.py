"""One shared tip-signal for Post-Only Average-True-Range formula packs.

Research (``run_atr_bracket_arm``) and live must resolve the last closed bar
through this module so the live bit, limit, stop and target cannot drift.

Missing Average True Range or idea bits are refused, never zero-filled.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

import numpy as np
import pandas as pd

from llm2.autonomy.public_formulas import ema, kaufman_efficiency_ratio
from llm2.diagonal_sr.bar_series import make_bar_series
from llm2.edge_lab.sim_atr import atr_brackets, limit_prices
from llm2.ml_lab.idea_catalog import signals_from_ohlcv
from llm2.ml_lab.idea_catalog_f import IDEA_IDS_F, signals_f
from llm2.ml_lab.idea_catalog_i import IDEA_IDS_I, signals_i
from llm2.ml_lab.idea_catalog_j import IDEA_IDS_J, signals_j
from llm2.ml_lab.live_guards import SOL_EMA_SPEC
from llm2.validation.folds import index_to_ms

# ema192 uses min_periods=192; Savitzky–Golay z-score window is 64. Keep a buffer.
MIN_PREFIX_BARS = 250
IDEA = str(SOL_EMA_SPEC["idea"])


@dataclass(frozen=True)
class TipSignal:
    fires: bool
    idea: str
    side: str
    is_short: bool
    bar_ts_ms: int
    close: float
    atr_frac: float
    sl_pct: float
    tp_pct: float
    limit_px: float
    n_prefix_bars: int
    bit: float = 0.0
    nan_cols: tuple[str, ...] = ()
    geometry: dict[str, Any] = field(default_factory=dict)

    @property
    def ok(self) -> bool:
        return len(self.nan_cols) == 0


def _signal_bits(ohlcv: pd.DataFrame, timeframe: str, idea: str) -> np.ndarray:
    """Dispatch to the catalog that owns this idea. Same functions research scores."""
    if idea in IDEA_IDS_F:
        return np.asarray(signals_f(ohlcv, timeframe)[idea], dtype=float)
    if idea in IDEA_IDS_I:
        return np.asarray(signals_i(ohlcv, timeframe)[idea], dtype=float)
    if idea in IDEA_IDS_J:
        return np.asarray(signals_j(ohlcv, timeframe)[idea], dtype=float)
    sigs = signals_from_ohlcv(ohlcv, timeframe)
    if idea not in sigs:
        raise ValueError(f"unknown live idea {idea!r}")
    return np.asarray(sigs[idea], dtype=float)


def build_features_for_guard(ohlcv: pd.DataFrame, **kwargs: Any) -> pd.DataFrame:
    """Causal columns for leakage / four-proof of the Exponential Moving Average pack."""
    tf = str(kwargs.get("timeframe") or SOL_EMA_SPEC["timeframe"])
    symbol = str(kwargs.get("symbol") or SOL_EMA_SPEC["symbol"])
    c = ohlcv["close"].to_numpy(dtype=float)
    sc = make_bar_series(symbol, tf, ohlcv)
    sigs = signals_from_ohlcv(ohlcv, tf)
    return pd.DataFrame(
        {
            "ema12": ema(c, 12),
            "ema48": ema(c, 48),
            "ema192": ema(c, 192),
            "efficiency_ratio": kaufman_efficiency_ratio(c, 10),
            "atr_frac": sc.atr_frac,
            "power_ema_stack_long": sigs[IDEA],
        },
        index=ohlcv.index,
    )


def tip_signal(
    ohlcv: pd.DataFrame,
    *,
    spec: dict[str, Any] | None = None,
) -> TipSignal:
    """Resolve the last closed bar for a frozen Average-True-Range formula pack."""
    cfg = spec or SOL_EMA_SPEC
    idea = str(cfg.get("idea") or IDEA)
    symbol = str(cfg.get("symbol") or "SOLUSDT")
    tf = str(cfg.get("timeframe") or "1h")
    if ohlcv is None or len(ohlcv) < MIN_PREFIX_BARS:
        n = 0 if ohlcv is None else len(ohlcv)
        raise ValueError(f"need >={MIN_PREFIX_BARS} closed bars for {idea}, got {n}")

    bit_arr = _signal_bits(ohlcv, tf, idea)
    bit = float(bit_arr[-1])
    sc = make_bar_series(symbol, tf, ohlcv)
    close = float(sc.close[-1])
    atr_f = float(sc.atr_frac[-1])
    ts = index_to_ms(ohlcv.index)
    bar_ts_ms = int(ts[-1])

    nan_cols: list[str] = []
    if not np.isfinite(close) or close <= 0:
        nan_cols.append("close")
    if not np.isfinite(atr_f):
        nan_cols.append("atr_frac")
    if not np.isfinite(bit):
        nan_cols.append(idea)

    sl_arr, tp_arr = atr_brackets(
        np.asarray([atr_f], dtype=float),
        k_sl=float(cfg["k_sl"]),
        tp_ratio=float(cfg["tp_ratio"]),
        sl_cap=float(cfg["sl_cap"]),
    )
    sl_pct = float(sl_arr[0])
    tp_pct = float(tp_arr[0])
    if not np.isfinite(sl_pct) or sl_pct <= 0:
        nan_cols.append("sl_pct")
    if not np.isfinite(tp_pct) or tp_pct <= 0:
        nan_cols.append("tp_pct")

    is_short = bool(np.isfinite(bit) and bit <= -0.5)
    lim = limit_prices(
        np.asarray([close], dtype=float),
        np.asarray([atr_f], dtype=float),
        np.asarray([is_short], dtype=bool),
    )
    limit_px = float(lim[0])
    if not np.isfinite(limit_px) or limit_px <= 0:
        nan_cols.append("limit_px")

    fires = bool(np.isfinite(bit) and abs(bit) >= 0.5) and not nan_cols
    return TipSignal(
        fires=fires,
        idea=idea,
        side="Sell" if is_short else "Buy",
        is_short=is_short,
        bar_ts_ms=bar_ts_ms,
        close=close,
        atr_frac=atr_f,
        sl_pct=sl_pct,
        tp_pct=tp_pct,
        limit_px=limit_px,
        n_prefix_bars=int(len(ohlcv)),
        bit=bit if np.isfinite(bit) else float("nan"),
        nan_cols=tuple(nan_cols),
        geometry={
            "k_sl": float(cfg["k_sl"]),
            "tp_ratio": float(cfg["tp_ratio"]),
            "sl_cap": float(cfg["sl_cap"]),
            "atr_frac": atr_f,
            "bit": bit if np.isfinite(bit) else None,
        },
    )
