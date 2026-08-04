"""Decision-theoretic cost hurdle for probability gating."""

from __future__ import annotations

from dataclasses import dataclass

from llm2.paths import ROUND_TRIP_COST


@dataclass(frozen=True)
class CostHurdle:
    round_trip_cost: float = ROUND_TRIP_COST
    tp_pct: float = 0.01
    sl_pct: float = 0.02
    taker_rate: float = 0.00055
    entry_slippage: float = 0.0005
    risk_margin: float = 0.0

    @property
    def mu_plus(self) -> float:
        """Net win magnitude after per-fill fees (TP limit assumed taker unless proven)."""
        entry_cost = self.taker_rate + self.entry_slippage
        exit_cost = self.taker_rate
        return self.tp_pct - entry_cost - exit_cost

    @property
    def mu_minus(self) -> float:
        entry_cost = self.taker_rate + self.entry_slippage
        exit_cost = self.taker_rate
        return self.sl_pct + entry_cost + exit_cost

    def break_even_probability(self) -> float:
        mp, mm = self.mu_plus, self.mu_minus
        if mp + mm <= 0:
            return 1.0
        return (mm + self.risk_margin) / (mp + mm)

    def expected_value(self, p_hat: float) -> float:
        pi = self.break_even_probability()
        mp, mm = self.mu_plus, self.mu_minus
        return p_hat * mp - (1.0 - p_hat) * mm - self.risk_margin

    def should_trade(self, p_hat: float) -> bool:
        return self.expected_value(p_hat) > 0

    def screening_hurdle_return(self) -> float:
        """Frozen round-trip hurdle for quick screening."""
        return self.round_trip_cost
