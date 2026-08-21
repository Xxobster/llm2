"""Lightweight Finplot for dense ETH K5 p75 outer fold 5 (all trades as markers).

Default tradesim per-trade line/zone overlays choke Finplot at ~800 trades
(thousands of add_line/add_text objects). This path keeps:
  - full fold candlesticks + realized equity
  - every trade as entry/exit markers (long/short, win/loss colors)
  - metrics window
and does **not** resimulate.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

os.environ.pop("TRADESIM_NO_PLOT", None)

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from tradesim.ensure_source import prefer_botsgeneral_tradesim

prefer_botsgeneral_tradesim()

import finplot as fplt  # noqa: E402
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402
from tradesim.metrics import compute_metrics  # noqa: E402
from tradesim.research.plot import (  # noqa: E402
    TV_BG,
    TV_BEAR,
    TV_BULL,
    TV_FG,
    _apply_dark_theme,
    _bars_frame,
    _ensure_qt_app,
    _force_axes_dark,
    _metrics_text,
    _open_metrics_window,
    _realized_equity_frame,
)
from tradesim.research.store import BacktestStore  # noqa: E402

RUN_ID = "structure_v1_eth_k5_expectancy_strength_p75_001_candidate-f5-bc45ca42d8"
STORE = Path(
    r"D:\projectsdata\backtests\runs"
    r"\structure_v1_eth_k5_expectancy_strength_p75_001_candidate-f5"
    rf"\{RUN_ID}.sqlite"
)
LOG = _ROOT / "artifacts" / "reports" / "_open_p75_f5_finplot_light.log"


def _log(msg: str) -> None:
    LOG.parent.mkdir(parents=True, exist_ok=True)
    line = msg + "\n"
    print(msg, flush=True)
    with LOG.open("a", encoding="utf-8") as fh:
        fh.write(line)


def _marker_frame(index: pd.DatetimeIndex, trades) -> pd.DataFrame:
    """One row per fill marker (entry + exit)."""
    rows: list[dict] = []
    for t in trades:
        entry_ts = pd.to_datetime(int(t.entry_ts_ms), unit="ms", utc=True)
        exit_ts = pd.to_datetime(int(t.exit_ts_ms), unit="ms", utc=True)
        won = float(getattr(t, "realized_pnl", 0.0) or 0.0) >= 0.0
        side = int(t.side)
        color = "#26a69a" if won else "#ef5350"
        # triangle up = long entry / long exit; down = short
        rows.append(
            {
                "ts": entry_ts,
                "price": float(t.entry_price),
                "kind": "entry",
                "side": side,
                "color": color,
                "symbol": "t1" if side > 0 else "t",
            }
        )
        rows.append(
            {
                "ts": exit_ts,
                "price": float(t.exit_price),
                "kind": "exit",
                "side": side,
                "color": color,
                "symbol": "o",
            }
        )
    return pd.DataFrame(rows)


def main() -> int:
    LOG.write_text("", encoding="utf-8")
    _log(f"start RUN_ID={RUN_ID}")
    if not STORE.is_file():
        _log(f"MISSING store {STORE}")
        return 2

    saved = BacktestStore(STORE).load_run(RUN_ID)
    if saved.bars is None:
        _log("no embedded bars")
        return 3
    n_tr = len(saved.result.trades)
    n_bars = len(saved.bars)
    _log(f"loaded bars={n_bars} trades={n_tr}")

    metrics = compute_metrics(saved.result, bars=saved.bars)
    title = (
        f"ETH K5 double p75 | outer fold 5 OOS | {n_tr} trades (markers) "
        f"[{RUN_ID}]"
    )

    _apply_dark_theme(fplt)
    df = _bars_frame(saved.bars)
    eq = _realized_equity_frame(saved.result, df.index)
    _log(f"frames ohlc={len(df)} equity={len(eq)}")

    fplt.axis_height_factor = {0: 0.30, 1: 0.70}
    axes = fplt.create_plot(title, rows=2)
    if not isinstance(axes, (list, tuple)):
        axes = [axes]
    axes = list(axes)
    ax_eq, ax_px = axes[0], axes[1]
    _force_axes_dark(axes)

    fplt.plot(eq.index, eq["equity"].to_numpy(dtype=float), ax=ax_eq, legend="realized equity")
    fplt.candlestick_ochl(
        df[["Open", "Close", "High", "Low"]],
        ax=ax_px,
        candle_width=0.7,
    )
    _force_axes_dark(axes)

    # Efficient bulk markers (no per-trade lines/text).
    markers = _marker_frame(df.index, saved.result.trades)
    _log(f"markers={len(markers)}")
    # Snap to bar times so Finplot x-alignment is correct
    if not markers.empty:
        # Group by visual style for fewer plot calls
        for (side, kind, color), g in markers.groupby(
            ["side", "kind", "color"], sort=False
        ):
            style = "t1" if (int(side) > 0 and kind == "entry") else (
                "t" if (int(side) < 0 and kind == "entry") else "o"
            )
            size = 3 if kind == "entry" else 2
            # finplot wants a Series/DataFrame indexed by time
            s = pd.Series(g["price"].to_numpy(dtype=float), index=pd.DatetimeIndex(g["ts"]))
            # drop duplicate timestamps keep last
            s = s[~s.index.duplicated(keep="last")].sort_index()
            fplt.plot(
                s.index,
                s.values,
                ax=ax_px,
                color=color,
                style=style,
                width=size,
                legend=f"{'L' if int(side) > 0 else 'S'} {kind}",
            )

    meta = saved.strategy_meta or {
        "name": "eth_k5_double3h_p75_v1",
        "strength_quantile": 0.75,
        "fold": 5,
        "note": "lightweight markers — full OOS fold",
    }
    metrics_text = _metrics_text(saved.result, metrics, strategy_meta=meta)
    _ensure_qt_app()
    _open_metrics_window(metrics_text, title=f"Metrics — {title}")
    _log("calling fplt.show() — window should appear now")
    fplt.show()
    _log("fplt.show() returned (window closed)")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:  # noqa: BLE001
        LOG.parent.mkdir(parents=True, exist_ok=True)
        msg = f"FATAL {type(exc).__name__}: {exc}"
        print(msg, flush=True)
        with LOG.open("a", encoding="utf-8") as fh:
            fh.write(msg + "\n")
            import traceback

            fh.write(traceback.format_exc())
        raise
