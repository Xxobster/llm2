"""Target families, horizons and proxy-side routing (shared, import-safe)."""

from __future__ import annotations

import numpy as np

from llm2.paths import ROUND_TRIP_COST

# How a target becomes a trade, and how it may be scored. Routing is explicit because
# feeding a magnitude target through the directional path scored a constant predictor at
# PF 2.0 and ridge at PF 2988.
TARGET_FAMILY = {
    "fwd_return": "return",
    "quantile": "return",
    "direction": "directional",
    "xs_rank": "rank",
    "volatility": "magnitude",
    "vol_ratio": "magnitude",
}

DEFAULT_HORIZON = {
    "fwd_return": 6,
    "quantile": 6,
    "direction": 6,
    "xs_rank": 6,
    "volatility": 24,
    "vol_ratio": 24,
}

RANK_BAND = 0.05
DIRECTION_BAND = 0.10
# Back-compat private aliases
_RANK_BAND = RANK_BAND
_DIRECTION_BAND = DIRECTION_BAND


def target_family(target: str) -> str:
    try:
        return TARGET_FAMILY[target]
    except KeyError:
        raise ValueError(f"unknown target: {target}") from None


def proxy_side(mean: np.ndarray, family: str) -> np.ndarray:
    """Side from a prediction, in the units the target is actually expressed in."""
    if family == "return":
        return np.where(mean > ROUND_TRIP_COST, 1, np.where(mean < -ROUND_TRIP_COST, -1, 0))
    if family == "directional":
        return np.where(mean > DIRECTION_BAND, 1, np.where(mean < -DIRECTION_BAND, -1, 0))
    if family == "rank":
        return np.where(
            mean > 0.5 + RANK_BAND, 1, np.where(mean < 0.5 - RANK_BAND, -1, 0)
        )
    return np.zeros(len(mean), dtype=int)


# Back-compat alias used by older call sites / tests.
_proxy_side = proxy_side
