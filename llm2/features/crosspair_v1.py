"""Cross-pair relative features (v1)."""

from __future__ import annotations

import numpy as np
import pandas as pd

from llm2.data.panel import build_close_panel
from llm2.paths import PRIMARY_SYMBOLS


def build_crosspair_v1(
    ohlcv: pd.DataFrame,
    *,
    symbol: str,
    panel: pd.DataFrame | None = None,
    peers: list[str] | None = None,
) -> pd.DataFrame:
    """Relative strength vs BTC/ETH and cross-sectional z-scores."""
    sym = symbol.upper()
    peers = peers or [s for s in PRIMARY_SYMBOLS if s != sym]
    if panel is None:
        all_syms = list(dict.fromkeys([sym, *peers]))
        panel = build_close_panel(all_syms, _infer_tf(ohlcv))

    c = ohlcv["close"].astype(float)
    out = pd.DataFrame(index=ohlcv.index)
    log_ret = np.log(c.replace(0, np.nan)).diff()

    for peer in peers:
        if peer not in panel.columns:
            continue
        peer_close = panel[peer].reindex(ohlcv.index).ffill()
        peer_ret = np.log(peer_close.replace(0, np.nan)).diff()
        out[f"rel_ret_1_{peer}"] = log_ret - peer_ret
        for w in (6, 24, 48):
            out[f"rel_mom_{w}_{peer}"] = c.pct_change(w) - peer_close.pct_change(w)

    # Cross-sectional z of 1-bar return across available panel columns at each timestamp
    rets = panel.pct_change()
    aligned = rets.reindex(ohlcv.index)
    xs_mean = aligned.mean(axis=1)
    xs_std = aligned.std(axis=1).replace(0, np.nan)
    if sym in aligned.columns:
        out["xs_z_ret_1"] = (aligned[sym] - xs_mean) / xs_std

    return out.replace([np.inf, -np.inf], np.nan)


def _infer_tf(ohlcv: pd.DataFrame) -> str:
    if len(ohlcv) < 3:
        return "1h"
    delta = (ohlcv.index[1] - ohlcv.index[0]).total_seconds()
    mapping = {900: "15m", 3600: "1h", 14400: "4h", 300: "5m", 60: "1m"}
    return mapping.get(int(delta), "1h")
