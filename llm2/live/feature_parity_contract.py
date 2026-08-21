"""Live vs backtest structure feature contract.

Backtest / hunt (canonical)
---------------------------
``build_space(ohlcv, "structure_v1", symbol=..., timeframe=...)`` with default
``recent_only=False`` reads confirmed-swing rows from the research warehouse
``D:\\projectsdata\\indicators\\indicators.sqlite`` (full history). Swings are
computed once over the full Open-High-Low-Close-Volume (OHLCV) series by
botsgeneral ``indicators.update`` — never from a rolling 800-bar window.

Live (required)
---------------
Must consume the **same full-history structure geometry** as that warehouse.
Allowed implementations:

1. Sync / copy the research warehouse series into the pack slice, then tip-extend
   with a full-history recompute when the tip is missing; or
2. Recompute structure from **full** shared/research candles (``limit=None``)
   into the pack slice via ``refresh_symbol``.

Forbidden
---------
``refresh_symbol(..., limit=800)`` (or any short window) + ``upsert_bundle`` wipe.
That rebuilds swings from a truncated left edge and flips ``pred_mean`` vs
backtest (ETH 2026-08-03 16:00 UTC: live +0.456 vs warehouse −0.310).

``recent_only=True`` is only a *read* window into an already-correct warehouse
and is parity-safe when the underlying series is full-history (Layer A audit:
full vs recent_only match rate 1.0 on the same warehouse).
"""

from __future__ import annotations

# Imported by tests / docs scanners.
BACKTEST_USES_TRUNCATED_STRUCTURE_REFRESH = False
LIVE_MUST_MATCH_FULL_HISTORY_WAREHOUSE = True
FORBIDDEN_LIVE_STRUCTURE_LIMIT = 800
