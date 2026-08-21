"""Refresh warehouse Last+Mark for live LLM2 pivot pairs (15m decide + 1m touch)."""
from __future__ import annotations

from tradesim.ensure_source import prefer_botsgeneral_tradesim

prefer_botsgeneral_tradesim()

from tradesim.research import ensure_candles

if __name__ == "__main__":
    raise SystemExit(
        ensure_candles(
            ["ETHUSDT", "SOLUSDT"],
            ["15m", "1m"],
            price_types=("last", "mark"),
            incremental=True,
            quiet=False,
        )
    )
