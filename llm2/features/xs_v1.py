"""Cross-sectional feature space for relative-value targets.

``xs_rank`` is a relative-value label; predicting it from single-symbol open-high-low-
close-volume (OHLCV) features is a mismatch. This space builds only panel-relative
inputs so the model sees the same geometry the label is defined on.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from llm2.data.panel import build_close_panel
from llm2.paths import BINANCE_PERPS


_RET_WINDOWS = (1, 6, 24, 48)
_VOL_WINDOW = 24


def build_xs_v1(
    ohlcv: pd.DataFrame,
    *,
    symbol: str,
    panel: pd.DataFrame | None = None,
    symbols: list[str] | None = None,
) -> pd.DataFrame:
    """Cross-sectional ranks, z-scores and relative momentum vs the peer panel."""
    sym = symbol.upper()
    syms = list(dict.fromkeys(symbols or BINANCE_PERPS[:10]))
    if sym not in syms:
        syms = [sym, *syms]

    tf = _infer_tf(ohlcv)
    if panel is None:
        panel = build_close_panel(syms, tf)
    # Causal panel: completed bars only; drop any columns the warehouse lacked.
    panel = panel.reindex(columns=[c for c in syms if c in panel.columns]).ffill()
    if sym not in panel.columns:
        raise ValueError(f"{sym} missing from cross-sectional panel")

    closes = panel.reindex(ohlcv.index).ffill()
    out = pd.DataFrame(index=ohlcv.index)

    for w in _RET_WINDOWS:
        ret = closes.pct_change(w)
        ranks = ret.rank(axis=1, pct=True)
        z = (ret.sub(ret.mean(axis=1), axis=0)).div(ret.std(axis=1).replace(0, np.nan), axis=0)
        out[f"xs_rank_ret_{w}"] = ranks[sym]
        out[f"xs_z_ret_{w}"] = z[sym]
        # Own return vs equal-weight peer mean (excludes self from the mean).
        peer_mean = ret.drop(columns=[sym], errors="ignore").mean(axis=1)
        out[f"xs_rel_ret_{w}"] = ret[sym] - peer_mean

    # Cross-sectional volatility rank: realised range proxy from absolute returns.
    abs_ret = closes.pct_change().abs()
    vol = abs_ret.rolling(_VOL_WINDOW, min_periods=max(4, _VOL_WINDOW // 4)).mean()
    out[f"xs_rank_vol_{_VOL_WINDOW}"] = vol.rank(axis=1, pct=True)[sym]
    vol_z = (vol.sub(vol.mean(axis=1), axis=0)).div(vol.std(axis=1).replace(0, np.nan), axis=0)
    out[f"xs_z_vol_{_VOL_WINDOW}"] = vol_z[sym]

    # Breadth: fraction of peers with positive 1-bar return (excludes self).
    one = closes.pct_change()
    peers = one.drop(columns=[sym], errors="ignore")
    out["xs_breadth_up"] = (peers > 0).mean(axis=1)
    out["xs_n_peers"] = float(peers.shape[1])

    return out.replace([np.inf, -np.inf], np.nan)


def _infer_tf(ohlcv: pd.DataFrame) -> str:
    if len(ohlcv) < 3:
        return "1h"
    delta = int((ohlcv.index[1] - ohlcv.index[0]).total_seconds())
    return {60: "1m", 300: "5m", 900: "15m", 3600: "1h", 14400: "4h"}.get(delta, "1h")
