"""Canonical paths and frozen calendar constants."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / "artifacts"
MARKET_DB = Path(r"D:\projectsdata\candles\market_ohlcv.sqlite")
RESEARCH_DB = ARTIFACTS / "sqlite" / "research.sqlite"
LEAKAGE_REGISTRY = ARTIFACTS / "sqlite" / "leakage_registry.json"
FORWARD_LOCKBOX_START = "2026-05-01"
# After D-036 peeks on May→2026-08-04 multitrade lockbox diagnostics: only bars
# on/after this UTC date may host *new* multitrade parameter claims as unsealed forward.
# Copying OHLCV elsewhere does not reset contamination of the prior window.
POST_MULTITRADE_FREEZE_START = "2026-08-05"

BINANCE_PERPS = [
    "BTCUSDT",
    "ETHUSDT",
    "SOLUSDT",
    "BNBUSDT",
    "XRPUSDT",
    "ADAUSDT",
    "DOGEUSDT",
    "AVAXUSDT",
    "LINKUSDT",
    "DOTUSDT",
    "TRXUSDT",
    "XLMUSDT",
    "VETUSDT",
    "HYPEUSDT",
]
PRIMARY_SYMBOLS = ["BTCUSDT", "ETHUSDT", "SOLUSDT"]
DECISION_TIMEFRAMES = ["15m", "1h", "4h"]

TF_MS = {
    "1m": 60_000,
    "5m": 300_000,
    "15m": 900_000,
    "30m": 1_800_000,
    "1h": 3_600_000,
    "2h": 7_200_000,
    "4h": 14_400_000,
    "1d": 86_400_000,
    "1w": 604_800_000,
}

ROUND_TRIP_COST = 0.0016  # frozen screening hurdle


def touch_timeframe(decision_tf: str, symbol: str) -> str:
    """Map decision timeframe to touch resolution.

    Prefer the lowest available touch series that keeps same-bar ordering data-driven.
    For 1h decisions that means 1m (not 5m): several expansion symbols had 5m warehouse
    series stall weeks behind 1h/1m, which forced adverse same-bar fallbacks.
    """
    sym = symbol.upper()
    if decision_tf == "15m":
        return "1m" if sym in ("BTCUSDT", "ETHUSDT") else "5m"
    if decision_tf == "1h":
        return "1m"
    if decision_tf == "4h":
        return "15m"
    return decision_tf


def ensure_artifact_dirs() -> None:
    for path in (
        ARTIFACTS / "sqlite",
        ARTIFACTS / "folds",
        ARTIFACTS / "reports",
        ARTIFACTS / "models",
    ):
        path.mkdir(parents=True, exist_ok=True)
