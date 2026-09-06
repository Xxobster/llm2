"""Canonical paths and frozen calendar constants."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / "artifacts"
PROJECTSDATA = Path(r"D:\projectsdata")
MARKET_DB = PROJECTSDATA / "candles" / "market_ohlcv.sqlite"
MARKET_OI_DB = PROJECTSDATA / "candles" / "market_oi.sqlite"
NEWS_EVENTS_DB = PROJECTSDATA / "news" / "news_events.sqlite"
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

    Prefer 1-minute touch so same-bar Take-Profit / Stop-Loss order is
    data-driven, not an Open-High-Low-Close guess. Solana 15m used to map to 5m;
    the warehouse now has full 1m history, so 15m always uses 1m.

    5m also maps to 1m: with 5m touch equal to the decision bar, a bracket hit
    inside the entry bar would be unresolved and would fall back to the adverse
    feasible sequence. 1m history starts 2020-01-01 (2020-09-14 for Solana), so
    5m arms are scored from there; ``cached_touch`` fails closed rather than
    silently degrading when the touch window is thin.
    """
    if decision_tf in ("5m", "15m", "1h", "4h"):
        return "1m"
    return decision_tf


def ensure_artifact_dirs() -> None:
    for path in (
        ARTIFACTS / "sqlite",
        ARTIFACTS / "folds",
        ARTIFACTS / "reports",
        ARTIFACTS / "models",
    ):
        path.mkdir(parents=True, exist_ok=True)
