"""Leakage-guard adapter for pivot OHLCV feature packs (causal, no warehouse)."""

from __future__ import annotations

import pandas as pd

from llm2.pivot.features.packs import build_feature_frame


def build_features_for_guard(
    ohlcv: pd.DataFrame,
    *,
    interval: str = "15m",
    pack: str = "level_focus",
) -> pd.DataFrame:
    """Same builder research uses — not a simplified clean path.

    ``interval`` is accepted for leakage-CLI compatibility; pack features are
    timeframe-agnostic OHLCV transforms.
    """
    _ = interval
    return build_feature_frame(ohlcv, pack=pack)
