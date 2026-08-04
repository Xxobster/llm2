"""Fibonacci market-structure features (v1).

Sourced from the confirmed-swing warehouse rather than recomputed, and audited causal
before use (see :mod:`llm2.data.indicators`). Every column is scale-free: raw price levels
are excluded because their magnitude encodes the calendar on a series that went from four
figures to six.

Percent distances are additionally offered in volatility-normalised form. One percent from
resistance is a different situation in a quiet market than in a violent one, and the raw
percent cannot tell those apart; dividing by trailing realised volatility can. The
normaliser is a trailing window, so it stays knowable at the decision bar.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from llm2.data.indicators import align_multi_timeframe, structure_frame

VOL_WINDOW = 168  # one week of hourly bars
NORMALISE = (
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
)

# Higher-timeframe context carried onto the decision index. Structure on a slower clock is
# the classic "which way is the tide running" input, and it is cheap because the warehouse
# already holds it. Alignment is on completion, never on the higher bar's open.
HIGHER_TIMEFRAMES: dict[str, tuple[str, ...]] = {
    "15m": ("1h", "4h"),
    "1h": ("4h", "1w"),
    "4h": ("1w",),
    "1w": (),
}

# Only the summary columns are pulled from a higher timeframe. Carrying all thirty would
# triple the feature count for heavily redundant information.
HIGHER_COLUMNS = (
    "struct_dir",
    "leg_dir_up",
    "leg_impulse",
    "fib_position",
    "sr_asymmetry",
    "dist_last_sh_pct",
    "dist_last_sl_pct",
    "last_retrace_pct",
)


def build_structure_v1(
    ohlcv: pd.DataFrame,
    *,
    symbol: str,
    timeframe: str = "1h",
    higher_timeframes: tuple[str, ...] | None = None,
    include_volatility_normalised: bool = True,
    source: str | None = None,
    recent_only: bool = False,
) -> pd.DataFrame:
    """Confirmed-swing structure on the decision index.

    The warehouse indexes by bar open and describes the state at that bar's close, which is
    the same convention the decision frame uses, so the same-timeframe join is a plain
    reindex with no shift. Higher timeframes go through completion-aware alignment.

    ``recent_only`` (live path) loads warehouse rows from a little before the decision
    window only, so the Virtual Private Server (VPS) bot does not scan multi-year history.
    """
    target_idx = pd.DatetimeIndex(pd.to_datetime(ohlcv.index, utc=True))
    unique_idx = target_idx[~target_idx.duplicated(keep="last")]

    min_ts_ms: int | None = None
    if recent_only and len(unique_idx) > 0:
        # Pad for vol window + swing confirmation lookback + HTF as-of join.
        pad_bars = max(VOL_WINDOW * 2, 400)
        from llm2.paths import TF_MS

        step = int(TF_MS.get(timeframe, 3_600_000))
        min_ts_ms = int(unique_idx[0].value // 1_000_000) - pad_bars * step

    native = structure_frame(symbol, timeframe, source=source, min_ts_ms=min_ts_ms)
    out = native.reindex(unique_idx)

    if include_volatility_normalised:
        close = pd.Series(
            pd.to_numeric(ohlcv["close"], errors="coerce").to_numpy(dtype=float), index=target_idx
        )
        close = close[~close.index.duplicated(keep="last")].reindex(unique_idx)
        vol = np.log(close.where(close > 0)).diff().rolling(VOL_WINDOW, min_periods=VOL_WINDOW // 4).std()
        vol = vol.replace(0, np.nan)
        for col in NORMALISE:
            if col in out.columns:
                out[f"{col}_vol"] = out[col] / vol

    for htf in higher_timeframes if higher_timeframes is not None else HIGHER_TIMEFRAMES.get(timeframe, ()):
        try:
            higher = structure_frame(symbol, htf, source=source, min_ts_ms=min_ts_ms)
        except (ValueError, FileNotFoundError):
            continue
        keep = [c for c in HIGHER_COLUMNS if c in higher.columns]
        if not keep:
            continue
        aligned = align_multi_timeframe(higher[keep], unique_idx, htf)
        out = out.join(aligned.add_suffix(f"_{htf}"))

    out = out.reindex(target_idx)
    out.index = ohlcv.index
    return out.replace([np.inf, -np.inf], np.nan)
