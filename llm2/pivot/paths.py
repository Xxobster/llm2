"""Paths for the additive pivot multi-timeframe research module."""

from __future__ import annotations

from pathlib import Path

from llm2.paths import ARTIFACTS, MARKET_DB, PROJECTSDATA, ROOT

PIVOT_DATA_DIR = PROJECTSDATA / "pivot"
PIVOT_DB_DEFAULT = PIVOT_DATA_DIR / "pivot_research.sqlite"
PIVOT_CONFIG = ROOT / "configs" / "pivot_forecasting.yaml"
PIVOT_PREREG = ROOT / "configs" / "preregister" / "pivot_mtf_forecast_001.yaml"
PIVOT_REPORTS = ARTIFACTS / "reports" / "pivot_forecast"

__all__ = [
    "MARKET_DB",
    "PIVOT_CONFIG",
    "PIVOT_DATA_DIR",
    "PIVOT_DB_DEFAULT",
    "PIVOT_PREREG",
    "PIVOT_REPORTS",
]
