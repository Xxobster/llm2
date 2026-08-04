"""Feature space registry and builders."""

from __future__ import annotations

from typing import Callable

import pandas as pd

Builder = Callable[..., pd.DataFrame]

# Spaces that need the traded symbol (panel / relative geometry).
_SYMBOL_SPACES = frozenset({"crosspair_v1", "xs_v1"})

_SPACE_IMPORTS: dict[str, tuple[str, str]] = {
    "ohlcv_v1": ("llm2.features.ohlcv_v1", "build_ohlcv_v1"),
    "indicators_v1": ("llm2.features.indicators_v1", "build_indicators_v1"),
    "pivot_v1": ("llm2.features.pivot_v1", "build_pivot_v1"),
    "macro_v1": ("llm2.features.macro_v1", "build_macro_v1"),
    "crosspair_v1": ("llm2.features.crosspair_v1", "build_crosspair_v1"),
    "structure_v1": ("llm2.features.structure_v1", "build_structure_v1"),
    "xs_v1": ("llm2.features.xs_v1", "build_xs_v1"),
}


def get_builder(space: str) -> Builder:
    if space not in _SPACE_IMPORTS:
        raise KeyError(f"Unknown feature space: {space}. Known: {sorted(_SPACE_IMPORTS)}")
    mod_name, attr = _SPACE_IMPORTS[space]
    import importlib

    mod = importlib.import_module(mod_name)
    return getattr(mod, attr)


def build_space(ohlcv: pd.DataFrame, space: str, **kwargs) -> pd.DataFrame:
    from llm2.research_policy import require_warehouse_audit_bound

    # Warehouse-backed spaces without a confirmation-time audit must fail here, not later
    # with a flattering number built on look-ahead the leakage gate cannot see.
    require_warehouse_audit_bound(space)

    builder = get_builder(space)
    if space in _SYMBOL_SPACES:
        return builder(
            ohlcv,
            **{k: v for k, v in kwargs.items() if k in ("symbol", "panel", "peers", "symbols")},
        )
    if space == "macro_v1":
        return builder(ohlcv, **{k: v for k, v in kwargs.items() if k in ("timeframe",)})
    if space == "structure_v1":
        # The warehouse is keyed by symbol and timeframe, so this space cannot be built
        # from bars alone; failing loudly beats silently returning an empty frame.
        missing = {"symbol"} - set(kwargs)
        if missing:
            raise TypeError(f"structure_v1 requires {sorted(missing)}")
        return builder(
            ohlcv,
            **{
                k: v
                for k, v in kwargs.items()
                if k
                in (
                    "symbol",
                    "timeframe",
                    "higher_timeframes",
                    "include_volatility_normalised",
                    "source",
                    "recent_only",
                )
            },
        )
    return builder(ohlcv)


def list_spaces() -> list[str]:
    return sorted(_SPACE_IMPORTS.keys())
