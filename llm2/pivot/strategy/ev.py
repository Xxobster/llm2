"""Decision-theoretic EV gate for fixed TP/SL brackets (return space).

Uses Bybit-style per-fill fee rates. Default research posture: entry may be maker
for resting LIMIT, exits treated as taker until maker-exit evidence is proven
(consistent with research baseline conservatism for exits).
"""

from __future__ import annotations

from typing import NamedTuple


# Canonical non-VIP Bybit USDT-perp rates (research baseline).
TAKER = 0.00055
MAKER = 0.00020


class BracketMags(NamedTuple):
    mu_plus: float
    mu_minus: float
    pi_star: float
    fee_win: float
    fee_loss: float


def net_bracket_magnitudes(
    tp_pct: float,
    sl_pct: float,
    *,
    entry_fee: float = MAKER,
    exit_fee_tp: float = TAKER,
    exit_fee_sl: float = TAKER,
    entry_slip: float = 0.0,
    exit_slip_tp: float = 0.0,
    exit_slip_sl: float = 0.0,
    risk_lambda: float = 0.0,
) -> BracketMags:
    """Net win/loss magnitudes and break-even hit probability π*.

    ``mu_plus`` / ``mu_minus`` are in fractional return space on the entry notional
    (approx: price move ± fees/slips). Fees charged per fill on that notional.
    """
    tp = float(tp_pct)
    sl = float(sl_pct)
    fee_win = float(entry_fee) + float(exit_fee_tp)
    fee_loss = float(entry_fee) + float(exit_fee_sl)
    mu_plus = tp - fee_win - float(entry_slip) - float(exit_slip_tp)
    mu_minus = sl + fee_loss + float(entry_slip) + float(exit_slip_sl)
    denom = mu_plus + mu_minus
    if denom <= 0:
        pi = 1.0
    else:
        pi = (mu_minus + float(risk_lambda)) / denom
    return BracketMags(
        mu_plus=float(mu_plus),
        mu_minus=float(mu_minus),
        pi_star=float(pi),
        fee_win=float(fee_win),
        fee_loss=float(fee_loss),
    )


def break_even_probability(
    tp_pct: float,
    sl_pct: float,
    **kwargs,
) -> float:
    return net_bracket_magnitudes(tp_pct, sl_pct, **kwargs).pi_star
