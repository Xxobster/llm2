"""Macro context features from warehouse cross-asset series.

Rebuilt on ``llm2.data.macro`` after a confirmed look-ahead. The previous version did
``series.reindex(decision_index, method="ffill").shift(1)`` on a daily series whose index
is bar OPEN time, so at 01:00 on 2024-06-05 it handed the model DXY = 104.241, the close of
the whole of 2024-06-05. Alignment is now as-of against each bar's completion instant plus
its publication lag.

Excludes BTC_MCAP / ETH_MCAP: those series are near-linear transforms of the crypto prices
themselves (market cap is approximately price times supply) and produce hard
forward-correlation leakage findings against BTC/ETH returns.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from llm2.data.macro import build_external_panel

# External, non-price-identical macro only.
MACRO_SYMBOLS = [
    "DXY",
    "US10Y",
    "US02Y",
    "VIX",
    "SPX",
    "FNG",
]

_Z_WINDOWS = (5, 20)


def build_macro_v1(
    ohlcv: pd.DataFrame,
    *,
    timeframe: str = "1d",
    symbols: list[str] | None = None,
) -> pd.DataFrame:
    """Causally aligned macro returns, momentum and z-scores on the decision index.

    An ``age_sec`` column accompanies each series. Foreign exchange, indices and rates stop
    updating overnight and at weekends while crypto does not, so a constant run in a macro
    feature means "closed", not "unchanged", and the model needs to be able to tell.
    """
    syms = list(symbols or MACRO_SYMBOLS)
    target_idx = pd.DatetimeIndex(pd.to_datetime(ohlcv.index, utc=True))
    unique_idx = target_idx[~target_idx.duplicated(keep="last")]

    panel = build_external_panel(unique_idx, syms, timeframe, include_age=True)
    out_u = pd.DataFrame(index=unique_idx)

    for sym in syms:
        if sym not in panel.columns:
            continue
        level = panel[sym]
        # Levels themselves are non-stationary and near-duplicated across the panel; only
        # transforms of them go into the feature matrix. Non-positive observations (an
        # inverted term spread, negative oil) have no log return and become NaN.
        out_u[f"macro_logret_1_{sym}"] = np.log(level.where(level > 0)).diff()
        for w in _Z_WINDOWS:
            out_u[f"macro_mom_{w}_{sym}"] = level.pct_change(w)
            roll_mean = level.rolling(w, min_periods=max(2, w // 2)).mean()
            roll_std = level.rolling(w, min_periods=max(2, w // 2)).std()
            out_u[f"macro_z_{w}_{sym}"] = (level - roll_mean) / roll_std.replace(0, np.nan)
        age_col = f"{sym}__age_sec"
        if age_col in panel.columns:
            out_u[f"macro_age_h_{sym}"] = panel[age_col] / 3600.0

    out = out_u.reindex(target_idx)
    out.index = ohlcv.index
    return out.replace([np.inf, -np.inf], np.nan)
