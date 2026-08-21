"""Leakage guard integration with shared botsgeneral leakage engine."""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any, Callable

import pandas as pd

from llm2.features.registry import build_space, list_spaces
from llm2.paths import LEAKAGE_REGISTRY


def _prefer_leakage() -> None:
    import sys
    from pathlib import Path

    src = Path(r"C:\projects\botsgeneral\packages\leakage\src")
    if src.is_dir() and str(src) not in sys.path:
        sys.path.insert(0, str(src))
    from leakage.ensure_source import prefer_botsgeneral_leakage

    prefer_botsgeneral_leakage()
    import leakage

    if "botsgeneral" not in str(getattr(leakage, "__file__", "")):
        raise RuntimeError(
            f"leakage is not botsgeneral source (got {leakage.__file__}); refusing hunt"
        )


_WAREHOUSE_STRUCTURE_SPACES = frozenset(
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


def _with_recomputed_structure(
    ohlcv: pd.DataFrame,
    *,
    interval: str,
    symbol: str,
    space: str,
    **kwargs: Any,
) -> pd.DataFrame:
    """Point ``LLM2_INDICATORS_DB`` at a temp warehouse built from ``ohlcv``, then build."""
    from llm2.data.indicators import clear_indicator_cache
    from llm2.features.structure_recompute import recompute_structure_warehouse
    from llm2.features.structure_v1 import HIGHER_TIMEFRAMES

    htfs = HIGHER_TIMEFRAMES.get(interval, ())
    db = recompute_structure_warehouse(
        ohlcv,
        symbol=symbol,
        timeframe=interval,
        higher_timeframes=tuple(dict.fromkeys((interval, *htfs))),
        source=str(kwargs.get("source") or "binance"),
    )
    prev = os.environ.get("LLM2_INDICATORS_DB")
    os.environ["LLM2_INDICATORS_DB"] = str(db)
    try:
        clear_indicator_cache()
        return build_space(ohlcv, space, symbol=symbol, timeframe=interval, **kwargs)
    finally:
        clear_indicator_cache()
        if prev is None:
            os.environ.pop("LLM2_INDICATORS_DB", None)
        else:
            os.environ["LLM2_INDICATORS_DB"] = prev


def build_features_for_guard(
    ohlcv: pd.DataFrame,
    *,
    interval: str = "1h",
    space: str = "ohlcv_v1",
    symbol: str = "BTCUSDT",
    **kwargs: Any,
) -> pd.DataFrame:
    """Entry point for the shared leakage audit (must be a pure function of ``ohlcv``).

    Warehouse-backed spaces join a pre-computed indicator database. Truncating the bar
    frame does not truncate that database, so prefix-invariance used to false-PASS and
    missed CAUS-STRUCT-001. The guard recomputes structure into a temporary warehouse from
    the candles it is handed, and the leakage engine's builder-responsiveness probe
    (CAUS-WAREHOUSE-001) hard-fails any builder that still ignores its frame.
    """
    if space in ("crosspair_v1", "xs_v1"):
        return build_space(ohlcv, space, symbol=symbol, **kwargs)
    if space in _WAREHOUSE_STRUCTURE_SPACES:
        return _with_recomputed_structure(
            ohlcv, interval=interval, symbol=symbol, space=space, **kwargs
        )
    _ = interval
    return build_space(ohlcv, space, **{k: v for k, v in kwargs.items() if k != "symbol"})


def make_builder(
    space: str,
    symbol: str = "BTCUSDT",
    *,
    panel: pd.DataFrame | None = None,
) -> Callable[..., pd.DataFrame]:
    """Return a callable matching leakage FeatureBuilder: (ohlcv, *, interval) -> DataFrame.

    Panel-based spaces preload the peer panel once so prefix / future-mutation rebuilds do
    not re-open the market warehouse on every call (and contend with a running hunt).
    """

    def _builder(ohlcv: pd.DataFrame, *, interval: str = "1h") -> pd.DataFrame:
        kwargs: dict[str, Any] = {}
        if panel is not None:
            kwargs["panel"] = panel
        return build_features_for_guard(
            ohlcv, interval=interval, space=space, symbol=symbol, **kwargs
        )

    return _builder


def run_audit_for_space(
    ohlcv: pd.DataFrame,
    *,
    interval: str,
    space: str = "ohlcv_v1",
    symbol: str = "BTCUSDT",
    registry_path: Path | None = None,
    cuts: int = 3,
) -> dict[str, Any]:
    """Run shared leakage audit for one feature space."""
    _prefer_leakage()
    from leakage import format_report, run_leakage_audit, require_clean_audit

    panel = None
    if space in ("xs_v1", "crosspair_v1"):
        from llm2.data.panel import build_close_panel
        from llm2.paths import BINANCE_PERPS, PRIMARY_SYMBOLS

        peers = BINANCE_PERPS[:10] if space == "xs_v1" else PRIMARY_SYMBOLS
        syms = list(dict.fromkeys([symbol.upper(), *[p.upper() for p in peers]]))
        panel = build_close_panel(syms, interval)

    reg = registry_path or LEAKAGE_REGISTRY
    reg.parent.mkdir(parents=True, exist_ok=True)
    report = run_leakage_audit(
        ohlcv=ohlcv,
        build_features=make_builder(space, symbol, panel=panel),
        interval=interval,
        registry_path=str(reg),
        symbol=symbol,
        timeframe=interval,
        cuts=cuts,
    )
    return {
        "space": space,
        "passed": bool(report.ok),
        "ok": bool(report.ok),
        "report_text": format_report(report),
        "report": report,
        "leakage_potential": list(report.leakage_potential),
        "require_clean": lambda: require_clean_audit(report),
    }


def audit_all_spaces(
    ohlcv: pd.DataFrame,
    *,
    interval: str,
    symbol: str = "BTCUSDT",
) -> dict[str, dict[str, Any]]:
    results: dict[str, dict[str, Any]] = {}
    for space in list_spaces():
        try:
            results[space] = run_audit_for_space(
                ohlcv, interval=interval, space=space, symbol=symbol
            )
        except Exception as exc:  # noqa: BLE001
            results[space] = {"space": space, "passed": False, "ok": False, "error": str(exc)}
    return results
