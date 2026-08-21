"""Live fill vs tradesim price percent-deviation helpers (Layer C).

Pure matching / stats — no network, no lockbox side effects.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Sequence

import numpy as np


@dataclass(frozen=True)
class NormalizedFill:
    """One closed live or backtest round-trip for matching."""

    symbol: str
    side: int  # +1 long / -1 short
    entry_price: float
    exit_price: float
    entry_ts_ms: int
    exit_ts_ms: int
    qty: float
    source_id: str = ""
    raw: dict[str, Any] | None = None


def side_from_bybit(side: str | int | None) -> int:
    """Bybit closed-pnl ``side`` is the position side: Buy=long, Sell=short."""
    if side is None:
        return 0
    if isinstance(side, (int, np.integer)):
        s = int(side)
        return 1 if s > 0 else (-1 if s < 0 else 0)
    s = str(side).strip().lower()
    if s in {"buy", "long", "1"}:
        return 1
    if s in {"sell", "short", "-1"}:
        return -1
    return 0


def pct_deviation(live: float, bt: float) -> float:
    """Percent deviation of live vs backtest: 100 * (live - bt) / bt."""
    b = float(bt)
    if not np.isfinite(b) or abs(b) < 1e-12:
        return float("nan")
    return 100.0 * (float(live) - b) / b


def normalize_bybit_closed_row(row: dict[str, Any]) -> NormalizedFill | None:
    """Map one Bybit closed-pnl row to NormalizedFill."""
    try:
        entry = float(row.get("avgEntryPrice") or row.get("entry_price") or 0.0)
        exit_ = float(row.get("avgExitPrice") or row.get("exit_price") or 0.0)
        entry_ts = int(row.get("createdTime") or row.get("entry_ts_ms") or 0)
        exit_ts = int(row.get("updatedTime") or row.get("exit_ts_ms") or 0)
        qty = float(row.get("qty") or 0.0)
    except (TypeError, ValueError):
        return None
    side = side_from_bybit(row.get("side"))
    sym = str(row.get("symbol") or "").upper()
    if side == 0 or entry <= 0 or exit_ <= 0 or exit_ts <= 0 or not sym:
        return None
    if entry_ts <= 0:
        entry_ts = exit_ts
    return NormalizedFill(
        symbol=sym,
        side=side,
        entry_price=entry,
        exit_price=exit_,
        entry_ts_ms=entry_ts,
        exit_ts_ms=exit_ts,
        qty=qty,
        source_id=str(row.get("orderId") or f"{sym}:{exit_ts}"),
        raw=dict(row),
    )


def normalize_tradesim_trade(t: Any, *, symbol: str | None = None) -> NormalizedFill | None:
    """Map a tradesim Trade to NormalizedFill."""
    try:
        entry = float(getattr(t, "entry_price"))
        exit_ = float(getattr(t, "exit_price"))
        entry_ts = int(getattr(t, "entry_ts_ms"))
        exit_ts = int(getattr(t, "exit_ts_ms"))
        qty = float(getattr(t, "qty", 0.0) or 0.0)
        side = int(getattr(t, "side"))
        sym = str(getattr(t, "symbol", symbol or "") or symbol or "").upper()
        tid = str(getattr(t, "trade_id", ""))
    except (TypeError, ValueError, AttributeError):
        return None
    if side == 0 or entry <= 0 or exit_ <= 0 or exit_ts <= 0:
        return None
    return NormalizedFill(
        symbol=sym,
        side=1 if side > 0 else -1,
        entry_price=entry,
        exit_price=exit_,
        entry_ts_ms=entry_ts,
        exit_ts_ms=exit_ts,
        qty=qty,
        source_id=tid or f"bt:{entry_ts}",
        raw=None,
    )


def match_fills(
    live: Sequence[NormalizedFill],
    backtest: Sequence[NormalizedFill],
    *,
    match_tol_ms: int = 3 * 3_600_000,
) -> list[dict[str, Any]]:
    """Greedy one-to-one match by side + closest exit timestamp within tolerance.

    Returns list of match dicts with entry/exit percent deviations.
    """
    used_bt: set[int] = set()
    matches: list[dict[str, Any]] = []
    # Prefer matching most recent live closes first (stable for tiny samples)
    live_sorted = sorted(live, key=lambda x: x.exit_ts_ms)
    for lv in live_sorted:
        best_j = -1
        best_score = None
        for j, bt in enumerate(backtest):
            if j in used_bt:
                continue
            if lv.side != bt.side:
                continue
            if lv.symbol and bt.symbol and lv.symbol != bt.symbol:
                continue
            d_exit = abs(int(lv.exit_ts_ms) - int(bt.exit_ts_ms))
            d_entry = abs(int(lv.entry_ts_ms) - int(bt.entry_ts_ms))
            # Prefer entry alignment (Bybit createdTime ≈ open); exit can drift on holds.
            if d_entry > int(match_tol_ms) and d_exit > int(match_tol_ms):
                continue
            score = (d_entry, d_exit)
            if best_score is None or score < best_score:
                best_score = score
                best_j = j
        if best_j < 0 or best_score is None:
            matches.append(
                {
                    "matched": False,
                    "live": _fill_public(lv),
                    "backtest": None,
                    "entry_pct_dev": None,
                    "exit_pct_dev": None,
                    "exit_ts_delta_ms": None,
                    "entry_ts_delta_ms": None,
                }
            )
            continue
        bt = backtest[best_j]
        used_bt.add(best_j)
        matches.append(
            {
                "matched": True,
                "live": _fill_public(lv),
                "backtest": _fill_public(bt),
                "entry_pct_dev": pct_deviation(lv.entry_price, bt.entry_price),
                "exit_pct_dev": pct_deviation(lv.exit_price, bt.exit_price),
                "exit_ts_delta_ms": int(lv.exit_ts_ms) - int(bt.exit_ts_ms),
                "entry_ts_delta_ms": int(lv.entry_ts_ms) - int(bt.entry_ts_ms),
            }
        )
    return matches


def summarize_pct_devs(matches: Sequence[dict[str, Any]]) -> dict[str, Any]:
    """Distribution of entry/exit percent deviations over matched rows."""
    entry = np.asarray(
        [m["entry_pct_dev"] for m in matches if m.get("matched") and m.get("entry_pct_dev") is not None],
        dtype=float,
    )
    exit_ = np.asarray(
        [m["exit_pct_dev"] for m in matches if m.get("matched") and m.get("exit_pct_dev") is not None],
        dtype=float,
    )
    n_live = len(matches)
    n_matched = int(sum(1 for m in matches if m.get("matched")))
    return {
        "n_live": n_live,
        "n_matched": n_matched,
        "match_rate": (n_matched / n_live) if n_live else float("nan"),
        "entry_pct_dev": _dist(entry),
        "exit_pct_dev": _dist(exit_),
        "abs_entry_pct_dev": _dist(np.abs(entry)) if entry.size else _dist(entry),
        "abs_exit_pct_dev": _dist(np.abs(exit_)) if exit_.size else _dist(exit_),
    }


def _dist(a: np.ndarray) -> dict[str, float | None]:
    a = np.asarray(a, dtype=float)
    a = a[np.isfinite(a)]
    if a.size == 0:
        return {
            "n": 0,
            "mean": None,
            "median": None,
            "p90": None,
            "max": None,
            "min": None,
        }
    return {
        "n": int(a.size),
        "mean": float(np.mean(a)),
        "median": float(np.median(a)),
        "p90": float(np.percentile(a, 90)),
        "max": float(np.max(a)),
        "min": float(np.min(a)),
    }


def _fill_public(f: NormalizedFill) -> dict[str, Any]:
    return {
        "symbol": f.symbol,
        "side": f.side,
        "entry_price": f.entry_price,
        "exit_price": f.exit_price,
        "entry_ts_ms": f.entry_ts_ms,
        "exit_ts_ms": f.exit_ts_ms,
        "qty": f.qty,
        "source_id": f.source_id,
    }
