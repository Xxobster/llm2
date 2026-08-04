"""First-touch barrier labels."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Literal

import numpy as np
import pandas as pd

from llm2.paths import TF_MS


class FirstTouchLabel(str, Enum):
    UP_FIRST = "UP_FIRST"
    DOWN_FIRST = "DOWN_FIRST"
    NO_TOUCH = "NO_TOUCH"
    AMBIGUOUS = "AMBIGUOUS"


@dataclass(frozen=True)
class FirstTouchConfig:
    barrier_pct: float = 0.01
    horizon_hours: int = 24
    decision_timeframe: str = "1h"
    touch_timeframe: str = "15m"
    entry_reference: Literal["next_open", "close"] = "next_open"


def _touch_scan(
    highs: np.ndarray,
    lows: np.ndarray,
    up_level: float,
    down_level: float,
) -> FirstTouchLabel:
    up_hit = highs >= up_level
    down_hit = lows <= down_level
    if not up_hit.any() and not down_hit.any():
        return FirstTouchLabel.NO_TOUCH
    up_idx = int(np.argmax(up_hit)) if up_hit.any() else highs.size
    down_idx = int(np.argmax(down_hit)) if down_hit.any() else lows.size
    if up_idx == down_idx and up_hit[up_idx] and down_hit[down_idx]:
        return FirstTouchLabel.AMBIGUOUS
    if up_hit.any() and (not down_hit.any() or up_idx < down_idx):
        return FirstTouchLabel.UP_FIRST
    if down_hit.any() and (not up_hit.any() or down_idx < up_idx):
        return FirstTouchLabel.DOWN_FIRST
    return FirstTouchLabel.NO_TOUCH


def build_first_touch_labels(
    decision_df: pd.DataFrame,
    touch_df: pd.DataFrame,
    config: FirstTouchConfig | None = None,
) -> pd.DataFrame:
    config = config or FirstTouchConfig()
    decision = decision_df.sort_index()
    touch = touch_df.sort_index()

    dec_ts = (pd.DatetimeIndex(decision.index).astype("int64") // 1_000_000).astype(np.int64)
    touch_ts = (pd.DatetimeIndex(touch.index).astype("int64") // 1_000_000).astype(np.int64)
    touch_high = touch["high"].to_numpy(dtype=np.float64)
    touch_low = touch["low"].to_numpy(dtype=np.float64)

    if config.entry_reference == "next_open":
        entry_prices = decision["open"].shift(-1).to_numpy(dtype=np.float64)
    else:
        entry_prices = decision["close"].to_numpy(dtype=np.float64)

    horizon_ms = config.horizon_hours * 3_600_000
    decision_ms = TF_MS.get(config.decision_timeframe, TF_MS["1h"])
    n = len(decision)
    labels = np.full(n, FirstTouchLabel.NO_TOUCH.value, dtype=object)
    entry_out = np.full(n, np.nan)
    up_levels = np.full(n, np.nan)
    down_levels = np.full(n, np.nan)

    for i in range(n - 1):
        ref = entry_prices[i]
        if not np.isfinite(ref) or ref <= 0:
            continue
        start_ts = int(dec_ts[i]) + decision_ms
        end_ts = int(dec_ts[i]) + horizon_ms
        left = int(np.searchsorted(touch_ts, start_ts, side="left"))
        right = int(np.searchsorted(touch_ts, end_ts, side="right"))
        up = ref * (1.0 + config.barrier_pct)
        down = ref * (1.0 - config.barrier_pct)
        entry_out[i] = ref
        up_levels[i] = up
        down_levels[i] = down
        if right <= left:
            continue
        labels[i] = _touch_scan(touch_high[left:right], touch_low[left:right], up, down).value

    return pd.DataFrame(
        {
            "entry_ref_price": entry_out,
            "up_barrier": up_levels,
            "down_barrier": down_levels,
            "label": labels,
        },
        index=decision.index,
    )
