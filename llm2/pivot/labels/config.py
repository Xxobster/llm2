"""Pivot label configuration (per timeframe)."""

from __future__ import annotations

import hashlib
import json
from dataclasses import asdict, dataclass, field
from typing import Any, Sequence


@dataclass(frozen=True)
class PivotLabelConfig:
    """Configuration for a single pivot timeframe label family."""

    timeframe: str
    left_bars: int
    right_bars: int
    confirm_bars: int
    min_left_prominence_atr: float
    min_right_reversal_atr: float
    min_reversal_pct: float
    atr_period: int = 14
    label_family: str = "fractal_prominence_atr"
    # Forecast horizons as bar counts on this timeframe (derived from wall-clock elsewhere).
    forecast_horizon_bars: tuple[int, ...] = (1, 3, 6)
    event_match_price_tol_pct: float = 0.001
    event_match_time_tol_bars: int = 1
    tie_break: str = "leftmost"  # leftmost | rightmost for equal extrema
    suppress_neighbor_bars: int = 1

    def __post_init__(self) -> None:
        if self.left_bars < 1 or self.right_bars < 1:
            raise ValueError("left_bars and right_bars must be >= 1")
        if self.confirm_bars < self.right_bars:
            raise ValueError("confirm_bars must be >= right_bars (knowability)")
        if self.tie_break not in {"leftmost", "rightmost"}:
            raise ValueError(f"unknown tie_break={self.tie_break}")

    @property
    def version(self) -> str:
        payload = json.dumps(asdict(self), sort_keys=True, separators=(",", ":"))
        return hashlib.sha256(payload.encode("utf-8")).hexdigest()[:16]

    def to_dict(self) -> dict[str, Any]:
        d = asdict(self)
        d["config_version"] = self.version
        return d


def default_configs() -> dict[str, PivotLabelConfig]:
    """Research-initial configs (not outer-OOS tuned)."""
    common = dict(
        left_bars=3,
        right_bars=3,
        confirm_bars=3,
        atr_period=14,
        label_family="fractal_prominence_atr",
    )
    return {
        "5m": PivotLabelConfig(
            timeframe="5m",
            min_left_prominence_atr=0.5,
            min_right_reversal_atr=0.5,
            min_reversal_pct=0.001,
            forecast_horizon_bars=(1, 3, 6),
            **common,
        ),
        "15m": PivotLabelConfig(
            timeframe="15m",
            min_left_prominence_atr=0.5,
            min_right_reversal_atr=0.5,
            min_reversal_pct=0.0015,
            forecast_horizon_bars=(1, 2, 4),
            **common,
        ),
        "1h": PivotLabelConfig(
            timeframe="1h",
            min_left_prominence_atr=0.6,
            min_right_reversal_atr=0.6,
            min_reversal_pct=0.002,
            forecast_horizon_bars=(1, 2, 4),
            **common,
        ),
        "4h": PivotLabelConfig(
            timeframe="4h",
            left_bars=2,
            right_bars=2,
            confirm_bars=2,
            min_left_prominence_atr=0.6,
            min_right_reversal_atr=0.6,
            min_reversal_pct=0.003,
            atr_period=14,
            forecast_horizon_bars=(1, 2, 3),
        ),
        "1d": PivotLabelConfig(
            timeframe="1d",
            left_bars=2,
            right_bars=2,
            confirm_bars=2,
            min_left_prominence_atr=0.75,
            min_right_reversal_atr=0.75,
            min_reversal_pct=0.005,
            atr_period=14,
            forecast_horizon_bars=(1, 2, 3),
        ),
    }


def configs_from_mapping(raw: dict[str, Any]) -> dict[str, PivotLabelConfig]:
    """Build configs from ``configs/pivot_forecasting.yaml`` pivot_label section."""
    out: dict[str, PivotLabelConfig] = {}
    for tf, cfg in (raw or {}).items():
        out[str(tf)] = PivotLabelConfig(
            timeframe=str(tf),
            left_bars=int(cfg["left_bars"]),
            right_bars=int(cfg["right_bars"]),
            confirm_bars=int(cfg["confirm_bars"]),
            min_left_prominence_atr=float(cfg["min_left_prominence_atr"]),
            min_right_reversal_atr=float(cfg["min_right_reversal_atr"]),
            min_reversal_pct=float(cfg["min_reversal_pct"]),
            atr_period=int(cfg.get("atr_period", 14)),
        )
    return out
