"""Cross-sectional rank of forward returns."""

from __future__ import annotations

import pandas as pd

from llm2.data.panel import build_close_panel
from llm2.paths import BINANCE_PERPS


def build_xs_rank_labels(
    ohlcv: pd.DataFrame,
    *,
    symbol: str,
    horizon: int = 1,
    symbols: list[str] | None = None,
) -> pd.DataFrame:
    sym = symbol.upper()
    syms = symbols or BINANCE_PERPS[:10]
    tf = _infer_tf(ohlcv)
    panel = build_close_panel(syms, tf)
    fwd = panel.pct_change(horizon).shift(-horizon)
    ranks = fwd.rank(axis=1, pct=True)
    if sym not in ranks.columns:
        raise ValueError(f"{sym} not in cross-section panel")
    aligned = ranks[sym].reindex(ohlcv.index)
    return pd.DataFrame({"xs_rank": aligned, "horizon": horizon}, index=ohlcv.index)


def _infer_tf(ohlcv: pd.DataFrame) -> str:
    if len(ohlcv) < 3:
        return "1h"
    delta = int((ohlcv.index[1] - ohlcv.index[0]).total_seconds())
    return {900: "15m", 3600: "1h", 14400: "4h", 300: "5m"}.get(delta, "1h")
