"""Economic diagnostics for predicted pivot levels (not only correlation)."""

from __future__ import annotations

from typing import Any

import numpy as np
import pandas as pd

from llm2.validation.folds import index_to_ms


def _safe_pct(a: np.ndarray) -> float:
    a = np.asarray(a, dtype=float)
    a = a[np.isfinite(a)]
    return float(np.mean(a)) if a.size else float("nan")


def level_error_stats(
    *,
    y_level_ret: np.ndarray,
    pred_level_ret: np.ndarray,
    atr_frac: np.ndarray | None = None,
) -> dict[str, float]:
    """MAE / P90 of absolute level error in return space and ATR units."""
    y = np.asarray(y_level_ret, dtype=float)
    p = np.asarray(pred_level_ret, dtype=float)
    m = np.isfinite(y) & np.isfinite(p)
    if not m.any():
        return {
            "n": 0,
            "mae_pct": float("nan"),
            "p50_abs_pct": float("nan"),
            "p90_abs_pct": float("nan"),
            "bias_pct": float("nan"),
            "corr": float("nan"),
            "mae_atr": float("nan"),
            "p90_abs_atr": float("nan"),
        }
    err = p[m] - y[m]
    abs_e = np.abs(err)
    out = {
        "n": int(m.sum()),
        "mae_pct": float(abs_e.mean()),
        "p50_abs_pct": float(np.median(abs_e)),
        "p90_abs_pct": float(np.percentile(abs_e, 90)),
        "bias_pct": float(err.mean()),
        "corr": float(np.corrcoef(p[m], y[m])[0, 1]) if m.sum() > 2 else float("nan"),
        "mae_atr": float("nan"),
        "p90_abs_atr": float("nan"),
    }
    if atr_frac is not None:
        a = np.asarray(atr_frac, dtype=float)[m]
        ok = np.isfinite(a) & (a > 1e-12)
        if ok.any():
            e_atr = abs_e[ok] / a[ok]
            out["mae_atr"] = float(e_atr.mean())
            out["p90_abs_atr"] = float(np.percentile(e_atr, 90))
    return out


def touch_diagnostics(
    *,
    ohlcv: pd.DataFrame,
    decision_ts_ms: np.ndarray,
    limit_prices: np.ndarray,
    is_short: np.ndarray,
    work_bars: int,
    true_side_high: np.ndarray | None = None,
) -> dict[str, Any]:
    """Touch rate of predicted limit within ``work_bars`` and wrong-side touches.

    Long limit rests below: touch if low <= limit. Short limit rests above:
    touch if high >= limit.
    Wrong-side: opposite extreme pierces a mirrored distance before (or without)
    preferred touch within the window — crude path diagnostic.
    """
    bar_ts = index_to_ms(ohlcv.index)
    high = ohlcv["high"].to_numpy(dtype=float)
    low = ohlcv["low"].to_numpy(dtype=float)
    close = ohlcv["close"].to_numpy(dtype=float)
    n_bars = len(bar_ts)
    idx = np.searchsorted(bar_ts, decision_ts_ms.astype(np.int64), side="left")
    valid = (idx < n_bars) & (bar_ts[np.clip(idx, 0, n_bars - 1)] == decision_ts_ms.astype(np.int64))
    touch = np.zeros(len(decision_ts_ms), dtype=bool)
    wrong = np.zeros(len(decision_ts_ms), dtype=bool)
    first_touch_bar = np.full(len(decision_ts_ms), -1, dtype=np.int64)

    for j in range(len(decision_ts_ms)):
        if not valid[j]:
            continue
        i0 = int(idx[j]) + 1  # first executable after close decision
        i1 = min(n_bars, i0 + int(work_bars))
        if i0 >= n_bars:
            continue
        lim = float(limit_prices[j])
        c0 = float(close[int(idx[j])])
        if not np.isfinite(lim) or lim <= 0 or not np.isfinite(c0) or c0 <= 0:
            continue
        short = bool(is_short[j])
        # Preferred touch
        for k in range(i0, i1):
            if short and high[k] >= lim:
                touch[j] = True
                first_touch_bar[j] = k - i0
                break
            if (not short) and low[k] <= lim:
                touch[j] = True
                first_touch_bar[j] = k - i0
                break
        # Wrong-side: opposite side moves by the same |limit-close| first
        dist = abs(lim / c0 - 1.0)
        if dist < 1e-9:
            continue
        if short:
            # wrong for short limit (selling high): market dumps and never tags high
            mirror = c0 * (1.0 - dist)
            for k in range(i0, i1):
                hit_pref = high[k] >= lim
                hit_wrong = low[k] <= mirror
                if hit_wrong and not hit_pref:
                    wrong[j] = True
                    break
                if hit_pref:
                    break
        else:
            mirror = c0 * (1.0 + dist)
            for k in range(i0, i1):
                hit_pref = low[k] <= lim
                hit_wrong = high[k] >= mirror
                if hit_wrong and not hit_pref:
                    wrong[j] = True
                    break
                if hit_pref:
                    break

    side_ok = None
    if true_side_high is not None:
        th = np.asarray(true_side_high, dtype=float)
        # is_short predicts high pivot → short; y_high=1 means true high
        pred_high = is_short.astype(float)
        m = np.isfinite(th) & (th >= 0)
        side_ok = float(np.mean((pred_high[m] == th[m]))) if m.any() else float("nan")

    return {
        "n": int(len(decision_ts_ms)),
        "n_valid": int(valid.sum()),
        "touch_rate": _safe_pct(touch.astype(float)),
        "wrong_side_touch_rate": _safe_pct(wrong.astype(float)),
        "mean_bars_to_touch_if": float(
            np.mean(first_touch_bar[first_touch_bar >= 0])
            if (first_touch_bar >= 0).any()
            else float("nan")
        ),
        "side_accuracy_on_events": side_ok,
        "work_bars": int(work_bars),
    }
