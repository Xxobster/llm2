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
    # Causal structure minus last_retrace* (post-CAUS-STRUCT-001 clean alpha).
    "structure_v1_no_retrace": ("llm2.features.structure_v1", "build_structure_v1_no_retrace"),
    # structure without last_retrace* + causal running-retrace depth (not orange).
    "structure_v1_run_retrace": ("llm2.features.run_retrace_v1", "build_structure_v1_run_retrace"),
    "xs_v1": ("llm2.features.xs_v1", "build_xs_v1"),
    "oi_v1": ("llm2.features.oi_v1", "build_oi_v1"),
    "structure_oi_v1": ("llm2.features.oi_v1", "build_structure_oi_v1"),
    "news_v1": ("llm2.features.news_v1", "build_news_v1"),
    "structure_news_v1": ("llm2.features.news_v1", "build_structure_news_v1"),
    "structure_oi_news_v1": ("llm2.features.news_v1", "build_structure_oi_news_v1"),
}

# Spaces that need symbol (and usually timeframe) kwargs.
_STRUCTURE_LIKE = frozenset(
    {
        "structure_v1",
        "structure_v1_no_retrace",
        "structure_v1_run_retrace",
        "oi_v1",
        "structure_oi_v1",
        "news_v1",
        "structure_news_v1",
        "structure_oi_news_v1",
    }
)


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
    if space in _STRUCTURE_LIKE:
        # Warehouse-backed: keyed by symbol/timeframe; fail loud without symbol.
        missing = {"symbol"} - set(kwargs)
        if missing and space != "news_v1":
            raise TypeError(f"{space} requires {sorted(missing)}")
        allowed = (
            "symbol",
            "timeframe",
            "higher_timeframes",
            "include_volatility_normalised",
            "source",
            "recent_only",
            "exchange",
        )
        return builder(ohlcv, **{k: v for k, v in kwargs.items() if k in allowed})
    return builder(ohlcv)


def list_spaces() -> list[str]:
    return sorted(_SPACE_IMPORTS.keys())
