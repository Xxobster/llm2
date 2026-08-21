"""Causal timing / rest gates for pivot LIMIT strategies (RESEARCH_ONLY helpers)."""

from __future__ import annotations

import numpy as np
import pandas as pd

from llm2.validation.folds import index_to_ms


def vsa_absorption_ok(
    ohlcv: pd.DataFrame,
    decision_ts_ms: np.ndarray,
    is_short: np.ndarray,
) -> np.ndarray:
    """Binary rest/no-rest from VSA-like bar shape at the decision close.

    Short (fade high): want wide/high-vol bar that closes off the high (rejection).
    Long (fade low): want wide/high-vol bar that closes off the low (bounce).
    """
    bar_ts = index_to_ms(ohlcv.index)
    pos = {int(t): i for i, t in enumerate(bar_ts.tolist())}
    h = ohlcv["high"].to_numpy(dtype=float)
    l = ohlcv["low"].to_numpy(dtype=float)
    c = ohlcv["close"].to_numpy(dtype=float)
    v = (
        ohlcv["volume"].to_numpy(dtype=float)
        if "volume" in ohlcv.columns
        else np.ones(len(c))
    )
    spread = h - l
    vol_ma = pd.Series(v).rolling(48, min_periods=12).mean().to_numpy()
    sp_ma = pd.Series(spread).rolling(48, min_periods=12).mean().to_numpy()
    with np.errstate(divide="ignore", invalid="ignore"):
        rel_vol = v / np.where(vol_ma > 0, vol_ma, np.nan)
        rel_sp = spread / np.where(sp_ma > 0, sp_ma, np.nan)
        off_hi = (h - c) / np.where(spread > 0, spread, np.nan)
        off_lo = (c - l) / np.where(spread > 0, spread, np.nan)

    out = np.zeros(len(decision_ts_ms), dtype=bool)
    for j, t in enumerate(decision_ts_ms):
        i = pos.get(int(t))
        if i is None:
            continue
        if not (np.isfinite(rel_vol[i]) and np.isfinite(rel_sp[i])):
            continue
        if rel_vol[i] < 1.2 or rel_sp[i] < 1.0:
            continue
        if is_short[j]:
            out[j] = bool(np.isfinite(off_hi[i]) and off_hi[i] >= 0.55)
        else:
            out[j] = bool(np.isfinite(off_lo[i]) and off_lo[i] >= 0.55)
    return out


def medium_atr_mask(
    atr_frac: np.ndarray,
    *,
    lo_q: float = 0.25,
    hi_q: float = 0.75,
) -> np.ndarray:
    """Keep rows whose ATR fraction is inside the sample's [lo_q, hi_q] band."""
    a = np.asarray(atr_frac, dtype=float)
    ok = np.isfinite(a) & (a > 0)
    if ok.sum() < 50:
        return ok
    lo = float(np.nanpercentile(a[ok], 100 * lo_q))
    hi = float(np.nanpercentile(a[ok], 100 * hi_q))
    return ok & (a >= lo) & (a <= hi)


def session_utc_mask(
    decision_ts_ms: np.ndarray,
    *,
    hours_utc: tuple[int, ...] = (7, 8, 9, 10, 11, 12, 13, 14, 15, 16),
) -> np.ndarray:
    """Simple UTC hour filter (European/US overlap-ish). Knowable from timestamp."""
    dt = pd.to_datetime(np.asarray(decision_ts_ms, dtype=np.int64), unit="ms", utc=True)
    hours = set(int(h) for h in hours_utc)
    return np.array([int(x.hour) in hours for x in dt], dtype=bool)


def funding_near_mask(
    decision_ts_ms: np.ndarray,
    *,
    avoid_minutes: int = 30,
) -> np.ndarray:
    """Avoid resting in the ±avoid_minutes window around 00/08/16 UTC funding."""
    dt = pd.to_datetime(np.asarray(decision_ts_ms, dtype=np.int64), unit="ms", utc=True)
    out = np.ones(len(dt), dtype=bool)
    for i, t in enumerate(dt):
        # minutes from nearest funding hour
        mins = t.hour * 60 + t.minute
        for fh in (0, 8, 16):
            d = abs(mins - fh * 60)
            d = min(d, 24 * 60 - d)
            if d <= int(avoid_minutes):
                out[i] = False
                break
    return out


def map_htf_side_agree(
    decision_ts_ms: np.ndarray,
    is_short_ltf: np.ndarray,
    *,
    htf_ts_ms: np.ndarray,
    htf_p_high: np.ndarray,
) -> np.ndarray:
    """True when last completed HTF bar's side agrees with LTF side."""
    htf_ts = np.asarray(htf_ts_ms, dtype=np.int64)
    htf_p = np.asarray(htf_p_high, dtype=float)
    out = np.zeros(len(decision_ts_ms), dtype=bool)
    for j, t in enumerate(decision_ts_ms):
        # last HTF bar with ts < decision (completed)
        k = int(np.searchsorted(htf_ts, int(t), side="left")) - 1
        if k < 0 or not np.isfinite(htf_p[k]):
            continue
        htf_short = htf_p[k] >= 0.5
        out[j] = bool(htf_short == bool(is_short_ltf[j]))
    return out


def time_bucket_work_bars(
    time_pred: np.ndarray,
    *,
    horizon: int,
    default_work: int = 4,
) -> np.ndarray:
    """Per-row work bars; 0 = cancel (model says later than horizon)."""
    tb = np.asarray(time_pred, dtype=float)
    out = np.full(tb.shape, int(default_work), dtype=np.int64)
    finite = np.isfinite(tb)
    late = finite & (tb > float(horizon) + 0.5)
    early = finite & ~late
    out[late] = 0
    # ceil(time) + 1 bar of slack, clipped to [1, horizon]
    wb = np.ceil(tb[early]).astype(np.int64) + 1
    out[early] = np.clip(wb, 1, int(horizon))
    return out
