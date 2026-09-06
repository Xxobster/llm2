"""Guards for the frozen Solana 1-hour Exponential Moving Average stack.

Intended product: resting Post-Only entry, cancel if not touched, stay flat.
Gate C all-taker is a Frozen Default Gates V2.1 *stamp* (Shadow-Ready), not a
requirement that live must use market orders or taker fees.
"""

from __future__ import annotations

from typing import Any

from llm2.research_policy import PolicyError

# Shared 1-hour Average-True-Range bracket (same as hunt 009 / 012 inner screen).
_ATR_1H = {
    "k_sl": 1.5,
    "tp_ratio": 1.5,
    "sl_cap": 0.030,
    "work_bars": 3,
    "max_hold_bars": 16,
    "entry": "post_only_limit",
    "expired_entry": "cancel_and_flat",
    "risk_fraction": 0.05,
    "leverage_from_sl_cap": 13.0,
}

SOL_EMA_SPEC = {
    "symbol": "SOLUSDT",
    "timeframe": "1h",
    "idea": "power_ema_stack_long",
    "catalog": "ema",
    **_ATR_1H,
}

BTC_QUAD_SLOPE_SPEC = {
    "symbol": "BTCUSDT",
    "timeframe": "1h",
    "idea": "quad_slope_follow",
    "catalog": "f",
    **_ATR_1H,
}

SOL_FVG_CONFLUENCE_SPEC = {
    "symbol": "SOLUSDT",
    "timeframe": "1h",
    "idea": "fvg_confluence",
    "catalog": "i",
    **_ATR_1H,
}

SOL_HILBERT_AMP_FADE_SPEC = {
    "symbol": "SOLUSDT",
    "timeframe": "1h",
    "idea": "hilbert_amp_fade",
    "catalog": "j",
    **_ATR_1H,
}

AUTHORIZED_LIVE_SPECS: tuple[dict[str, Any], ...] = (
    SOL_EMA_SPEC,
    BTC_QUAD_SLOPE_SPEC,
    SOL_FVG_CONFLUENCE_SPEC,
    SOL_HILBERT_AMP_FADE_SPEC,
)


def live_spec_for(symbol: str, timeframe: str, idea: str) -> dict[str, Any] | None:
    """Return the frozen live spec for this (symbol, timeframe, idea), else None."""
    want = (str(symbol).upper(), str(timeframe), str(idea))
    for spec in AUTHORIZED_LIVE_SPECS:
        got = (str(spec["symbol"]).upper(), str(spec["timeframe"]), str(spec["idea"]))
        if got == want:
            return dict(spec)
    return None


def refuse_shadow_ready_stamp(gates: dict[str, Any], *, spec: dict[str, Any] | None = None) -> None:
    """Cannot label SHADOW_READY when Frozen Default Gates V2.1 overall is not PASS.

    Does **not** forbid a user-authorized minimum-size Post-Only live test.
    """
    name = (spec or SOL_EMA_SPEC).get("idea", "unknown")
    overall = str(gates.get("overall") or "")
    if overall != "PASS":
        raise PolicyError(
            f"SHADOW_READY stamp REFUSED for {name}: V2.1 overall={overall!r}. "
            "That stamp is not the same as a user-authorized min-size limit live test."
        )


def refuse_taker_entry_fallback(*, market_on_unfilled: bool) -> None:
    """This arm's live spec is limit or skip. Unfilled Post-Only must not become a taker."""
    if market_on_unfilled:
        raise PolicyError(
            "expired Post-Only must cancel and stay flat. "
            "Do not send a market order to 'not miss' the signal."
        )


def refuse_venue_min_qty_fallback(
    *,
    qty: float,
    raw_qty: float,
    min_qty: float,
    qty_step: float,
) -> None:
    """Refuse placing the exchange minimum when 5% stop-risk raw qty is larger.

    Floor to the step and skip below min. Never substitute venue-min size for
    the 5% equity-at-stop quantity.
    """
    if float(qty) <= 0:
        return
    min_q = float(min_qty)
    step = float(qty_step)
    raw = float(raw_qty)
    placed = float(qty)
    if raw + 1e-12 >= (min_q + step) and abs(placed - min_q) <= 1e-12:
        raise PolicyError(
            f"refusing venue-min qty={placed} when 5% stop-risk raw_qty={raw} "
            f"(min={min_q} step={step}). Size from 5% of equity at that bar's "
            "stop, not the exchange minimum."
        )
