"""Wallet-linked sizing: notional = equity × N × leverage.

Frozen live/research policy for structure packs that opt into equity sizing.
MIN_EXCHANGE remains available for dust diagnostics; never treat min-size wallet %
as deployable edge (see research_policy.MIN_SIZE_EQUITY_CAVEAT).
"""

from __future__ import annotations

import math
from typing import Any, Mapping, Sequence

from tradesim.ensure_source import prefer_botsgeneral_tradesim

prefer_botsgeneral_tradesim()

from tradesim import SizingConfig, SizingMode  # noqa: E402
from tradesim.contracts import InstrumentSpec, round_to_step  # noqa: E402
from tradesim.research.defaults import research_sizing_equity_leverage  # noqa: E402
from tradesim.sizing import desired_qty, minimum_executable_qty, normalise_order  # noqa: E402

# Margin fraction of equity per base book (1%). Notional = this × leverage.
DEFAULT_EQUITY_FRACTION = 0.01
DEFAULT_STOP_RISK_FRACTION = 0.05
SIZING_MODE_EQUITY_LEVERAGE = "EQUITY_LEVERAGE_NOTIONAL"
SIZING_MODE_MIN_EXCHANGE = "MIN_EXCHANGE"
SIZING_MODE_RISK_FRACTION = "RISK_FRACTION"


def equity_leverage_notional(
    *,
    equity: float,
    equity_fraction: float,
    leverage: float,
    size_mult: float = 1.0,
) -> float:
    """Gross position notional in quote currency (USDT)."""
    if equity <= 0 or equity_fraction <= 0 or leverage <= 0:
        return 0.0
    return float(equity) * float(equity_fraction) * float(leverage) * max(float(size_mult), 0.0)


def equity_leverage_qty(
    *,
    equity: float,
    equity_fraction: float,
    leverage: float,
    price: float,
    size_mult: float = 1.0,
    instrument: InstrumentSpec | None = None,
) -> float:
    """Quantity = notional / price, floored to venue step when instrument given."""
    if price <= 0:
        return 0.0
    notional = equity_leverage_notional(
        equity=equity,
        equity_fraction=equity_fraction,
        leverage=leverage,
        size_mult=size_mult,
    )
    raw = notional / float(price)
    if instrument is None:
        return float(raw)
    cfg = SizingConfig(
        mode=SizingMode.EQUITY_LEVERAGE_NOTIONAL,
        equity_fraction=float(equity_fraction),
    )
    # stop only for optional risk cap; pass stop=None so cap is skipped
    outcome = normalise_order(
        raw_qty=float(raw),
        price=float(price),
        stop_price=None,
        equity=float(equity),
        spec=instrument,
        cfg=cfg,
    )
    return float(outcome.qty) if outcome.ok else 0.0


def research_equity_sizing(
    *,
    equity_fraction: float = DEFAULT_EQUITY_FRACTION,
    compound: bool = True,
) -> SizingConfig:
    return research_sizing_equity_leverage(
        equity_fraction=float(equity_fraction),
        compound=bool(compound),
    )


def parse_pack_sizing(strategy: Mapping[str, Any] | None) -> dict[str, Any]:
    """Resolve sizing block from pack strategy.json."""
    raw = (strategy or {}).get("sizing")
    equity_fraction = float(
        (strategy or {}).get("equity_fraction")
        if (strategy or {}).get("equity_fraction") is not None
        else DEFAULT_EQUITY_FRACTION
    )
    if isinstance(raw, dict):
        mode = str(raw.get("mode") or SIZING_MODE_MIN_EXCHANGE).upper()
        if raw.get("equity_fraction") is not None:
            equity_fraction = float(raw["equity_fraction"])
        if raw.get("risk_fraction") is not None:
            risk_fraction = float(raw["risk_fraction"])
        else:
            risk_fraction = DEFAULT_STOP_RISK_FRACTION
        compound = bool(raw.get("compound", True))
    elif isinstance(raw, str):
        mode = raw.strip().upper()
        compound = True
        risk_fraction = DEFAULT_STOP_RISK_FRACTION
    else:
        mode = SIZING_MODE_MIN_EXCHANGE
        compound = True
        risk_fraction = DEFAULT_STOP_RISK_FRACTION
    if mode in ("EQUITY_LEVERAGE", "EQUITY_LEVERAGE_NOTIONAL", "N_EQ_X_LEV"):
        mode = SIZING_MODE_EQUITY_LEVERAGE
    if mode in ("RISK_FRACTION", "STOP_RISK_FRACTION", "PCT_EQUITY_AT_SL"):
        mode = SIZING_MODE_RISK_FRACTION
    return {
        "mode": mode,
        "equity_fraction": equity_fraction,
        "risk_fraction": float(risk_fraction),
        "compound": compound,
    }


def labelled_money_metrics(metrics: Any, *, starting_equity: float | None = None) -> dict[str, Any]:
    """Explicit wallet_return vs return_on_invested_notional (never confuse the two)."""
    start = starting_equity
    if start is None:
        start = float(getattr(metrics, "starting_equity", float("nan")))
    end = float(getattr(metrics, "ending_equity", float("nan")))
    net = float(getattr(metrics, "net_pnl", float("nan")))
    invested = float(getattr(metrics, "invested_notional", float("nan")))
    roi = float(getattr(metrics, "return_on_invested", float("nan")))
    wallet_return = (
        (end - float(start)) / float(start)
        if start is not None and float(start) > 0 and math.isfinite(end)
        else float("nan")
    )
    if not math.isfinite(roi) and invested > 0 and math.isfinite(net):
        roi = net / invested
    return {
        "net_pnl_usdt": net if math.isfinite(net) else None,
        "wallet_start_usdt": float(start) if start is not None and math.isfinite(float(start)) else None,
        "wallet_end_usdt": end if math.isfinite(end) else None,
        "wallet_return": wallet_return if math.isfinite(wallet_return) else None,
        "wallet_return_note": (
            "Valid headline only when size is wallet-linked "
            "(EQUITY_LEVERAGE_NOTIONAL / compound). "
            "Not edge under MIN_EXCHANGE fixed qty."
        ),
        "invested_notional_usdt": invested if math.isfinite(invested) else None,
        "roi_on_invested_notional": roi if math.isfinite(roi) else None,
        "roi_on_invested_notional_note": (
            "net_pnl / sum(entry qty × entry price); edge per dollar of position size."
        ),
    }


def peak_concurrent_margin_util(
    trades: Sequence[Any],
    *,
    starting_equity: float,
    leverage: float,
    compound: bool = True,
) -> dict[str, Any]:
    """Sweep open trades for peak concurrent books and margin utilisation.

    Initial margin per open book ≈ entry_notional / leverage. Equity path starts at
    starting_equity and adds closed-trade realized_pnl at exit (order-independent
    approximation when several exit same bar).
    """
    if not trades or starting_equity <= 0 or leverage <= 0:
        return {
            "peak_concurrent_books": 0,
            "peak_margin_usdt": 0.0,
            "peak_margin_utilisation": 0.0,
            "peak_notional_usdt": 0.0,
            "n_trades": 0,
        }

    events: list[tuple[int, int, float, float, float]] = []
    # (ts, kind, margin, notional, realized_on_close) kind: +1 open, -1 close
    for t in trades:
        ent = int(getattr(t, "entry_ts_ms", 0) or 0)
        ext = int(getattr(t, "exit_ts_ms", 0) or 0)
        qty = float(getattr(t, "qty", 0.0) or 0.0)
        ep = float(getattr(t, "entry_price", 0.0) or 0.0)
        notional = abs(qty * ep)
        margin = notional / float(leverage) if leverage > 0 else notional
        pnl = float(getattr(t, "realized_pnl", 0.0) or 0.0)
        events.append((ent, 1, margin, notional, 0.0))
        events.append((ext, -1, margin, notional, pnl))
    # open before close at same ts
    events.sort(key=lambda e: (e[0], -e[1]))

    equity = float(starting_equity)
    used = 0.0
    notional_open = 0.0
    books = 0
    peak_books = 0
    peak_used = 0.0
    peak_util = 0.0
    peak_notional = 0.0

    for _ts, kind, margin, notional, pnl in events:
        if kind > 0:
            used += margin
            notional_open += notional
            books += 1
            peak_books = max(peak_books, books)
            peak_used = max(peak_used, used)
            peak_notional = max(peak_notional, notional_open)
            eq_ref = equity if compound else float(starting_equity)
            if eq_ref > 0:
                peak_util = max(peak_util, used / eq_ref)
        else:
            used = max(0.0, used - margin)
            notional_open = max(0.0, notional_open - notional)
            books = max(0, books - 1)
            if compound:
                equity += pnl

    return {
        "peak_concurrent_books": int(peak_books),
        "peak_margin_usdt": float(peak_used),
        "peak_margin_utilisation": float(peak_util),
        "peak_notional_usdt": float(peak_notional),
        "n_trades": int(len(trades)),
        "leverage_assumed": float(leverage),
        "compound_equity": bool(compound),
        "gate_note": (
            "Compare peak_margin_utilisation to margin max_margin_utilisation (default 60%). "
            "K-book double size is the ruin-relevant stress, not a quiet-month min-size wallet %."
        ),
    }


def min_equity_for_n_fraction(
    *,
    price: float,
    instrument: InstrumentSpec,
    equity_fraction: float,
    leverage: float,
    size_mult: float = 1.0,
    utilisation_headroom: float = 1.0,
) -> float:
    """Smallest equity so venue-min order is still reachable under equity_leverage."""
    min_q = minimum_executable_qty(instrument, price)
    min_notional = max(float(instrument.min_notional), min_q * price) * float(size_mult)
    # notional = equity * N * lev  =>  equity = notional / (N * lev)
    denom = float(equity_fraction) * float(leverage) * float(utilisation_headroom)
    if denom <= 0:
        return math.inf
    return float(min_notional / denom)


def min_equity_for_stop_risk(
    *,
    price: float,
    sl_pct: float,
    instrument: InstrumentSpec,
    risk_fraction: float = DEFAULT_STOP_RISK_FRACTION,
) -> float:
    """Smallest wallet where one venue-minimum lot risks exactly ``risk_fraction``.

    Below this, the exchange minimum already loses more than ``risk_fraction`` if
    the stop is hit. Do not round the lot up. Skip, or add equity.
    """
    if price <= 0 or sl_pct <= 0 or risk_fraction <= 0:
        return math.inf
    min_q = minimum_executable_qty(instrument, price)
    return float(min_q * float(price) * float(sl_pct)) / float(risk_fraction)


def size_by_stop_risk(
    *,
    equity: float,
    price: float,
    sl_pct: float,
    instrument: InstrumentSpec,
    risk_fraction: float = DEFAULT_STOP_RISK_FRACTION,
    size_mult: float = 1.0,
    leverage: float | None = None,
    qty_round: str = "floor",
) -> dict[str, Any]:
    """Quantity from stop-loss cash risk, rounded to the venue step.

    Default ``qty_round='floor'``: never exceed the risk cap; skip if that
    floors below the venue minimum.

    ``qty_round='nearest'``: pick the lot closest to ``equity * risk_fraction``
    at the bar stop (may sit slightly above 5% because of the discrete step).
    Skip when the nearest lot is below the venue minimum — do not bump a dust
    wallet up to min-lot.
    """
    px = float(price)
    sl = float(sl_pct)
    eq = float(equity)
    round_mode = str(qty_round or "floor").lower()
    if round_mode not in {"floor", "nearest"}:
        raise ValueError(f"qty_round must be floor or nearest, got {qty_round!r}")
    stop_price = px * (1.0 - sl)
    cfg = SizingConfig(
        mode=SizingMode.RISK_FRACTION,
        risk_fraction=float(risk_fraction),
        max_risk_fraction=None if round_mode == "nearest" else float(risk_fraction),
    )
    raw, _unit = desired_qty(
        cfg=cfg,
        price=px,
        stop_price=stop_price,
        equity=eq,
        spec=instrument,
        leverage=leverage,
        size_mult=size_mult,
    )
    skip = None
    detail = ""
    if round_mode == "nearest":
        qty = float(round_to_step(float(raw), instrument.qty_step, "nearest"))
        min_q = float(minimum_executable_qty(instrument, px))
        ok = True
        if qty <= 0:
            ok = False
            skip = "QTY_ROUNDS_TO_ZERO"
            detail = f"{raw:g} rounds to zero on a step of {instrument.qty_step:g}"
            qty = 0.0
        elif qty + 1e-12 < min_q:
            ok = False
            skip = "BELOW_MIN_QTY"
            detail = f"{qty:g} is below the venue minimum quantity {min_q:g}"
            qty = 0.0
        elif instrument.min_notional > 0 and qty * px + 1e-12 < float(instrument.min_notional):
            ok = False
            skip = "BELOW_MIN_NOTIONAL"
            detail = f"{qty:g} * {px:g} is below min notional {instrument.min_notional:g}"
            qty = 0.0
        else:
            detail = f"nearest step {instrument.qty_step:g}"
    else:
        outcome = normalise_order(
            raw_qty=float(raw),
            price=px,
            stop_price=stop_price,
            equity=eq,
            spec=instrument,
            cfg=cfg,
        )
        qty = float(outcome.qty) if outcome.ok else 0.0
        ok = bool(outcome.ok and qty > 0)
        if not outcome.ok and outcome.skip_reason is not None:
            skip = str(outcome.skip_reason.value)
        detail = str(outcome.detail or "")
        if not ok and skip is None and qty <= 0:
            skip = "QTY_ROUNDS_TO_ZERO"
    notional = qty * px
    risk_cash = qty * px * sl
    margin = (notional / float(leverage)) if leverage and float(leverage) > 0 else None
    return {
        "ok": bool(ok and qty > 0),
        "qty": qty,
        "raw_qty": float(raw),
        "skip_reason": skip,
        "detail": detail,
        "qty_round": round_mode,
        "notional_usdt": float(notional),
        "risk_usdt": float(risk_cash),
        "actual_risk_fraction": (risk_cash / eq) if eq > 0 else float("nan"),
        "margin_usdt": None if margin is None else float(margin),
        "margin_utilisation": (
            None if margin is None or eq <= 0 else float(margin) / eq
        ),
    }
