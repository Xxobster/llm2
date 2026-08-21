"""Finplot last 1 month of CLEAN outer-OOS for ETH 15m wall_clock_q75.

Window: [2026-04-01, 2026-05-01) UTC — last month before FORWARD_LOCKBOX_START.
Same geometry as D-047 / live pack llm2_structure_eth_15m_multitrade_wall_clock_p75.
Evidence class: DISPLAY_ONLY_CLEAN_OOS_SLICE (not a promotion gate).
"""

from __future__ import annotations

import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

os.environ.pop("TRADESIM_NO_PLOT", None)

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from tradesim.ensure_source import prefer_botsgeneral_tradesim

prefer_botsgeneral_tradesim()

import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

from tradesim import (  # noqa: E402
    research_instrument,
    research_margin,
    research_sizing,
    research_sim_hedge,
)
from tradesim.research.plot import plot_backtest  # noqa: E402

from llm2.backtest.conformance import run_conformance_check  # noqa: E402
from llm2.backtest.run import ohlcv_to_bar_series, run_strategy_backtest  # noqa: E402
from llm2.data.loader import load_ohlcv  # noqa: E402
from llm2.data.macro import load_funding  # noqa: E402
from llm2.experiments.eth_multitrade_nested import build_multitrade_signals  # noqa: E402
from llm2.features.registry import build_space  # noqa: E402
from llm2.gates.evidence import leverage_from_stop, research_costs_baseline  # noqa: E402
from llm2.hunt.targets import DIRECTION_BAND, proxy_side, target_family  # noqa: E402
from llm2.labels.direction import build_direction_labels  # noqa: E402
from llm2.models.boosting import LGBMRegressorPredictor  # noqa: E402
from llm2.paths import ARTIFACTS, FORWARD_LOCKBOX_START, TF_MS, touch_timeframe  # noqa: E402
from llm2.validation.folds import index_to_ms  # noqa: E402

SYMBOL = "ETHUSDT"
TIMEFRAME = "15m"
SPACE = "structure_v1"
TARGET = "direction"
SL = 0.02
BASE_HOLD = 24
HOLD_ADDON = 48
MEAN_LOOKBACK = 672
LABEL_HORIZON = 24
STRENGTH_Q = 0.75
K = 7
FIB = 1.618
MIN_EDGE = DIRECTION_BAND

# Last month of clean pre-lockbox OOS.
DISPLAY_START = "2026-04-01"
DISPLAY_END = FORWARD_LOCKBOX_START  # 2026-05-01 exclusive

OUT_DIR = ARTIFACTS / "reports" / "structure_v1_eth_15m_wall_clock_q75_last1m_clean"
STORE = Path(r"D:\projectsdata\backtests\tradesim_runs.sqlite")
LOG = OUT_DIR / "_finplot.log"


def _log(msg: str) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    print(msg, flush=True)
    with LOG.open("a", encoding="utf-8") as fh:
        fh.write(msg + "\n")


def _cfg() -> dict:
    return {
        "max_positions_per_side": K,
        "clarity": "mean_strength",
        "clarity_scope": "all",
        "fib_ext": FIB,
        "hold_addon": HOLD_ADDON,
        "base_hold": BASE_HOLD,
        "base_tp": 0.01,
        "base_sl": SL,
        "mean_lookback": MEAN_LOOKBACK,
        "uniform_books": False,
        "bar_ms": int(TF_MS[TIMEFRAME]),
        "strength_quantile": STRENGTH_Q,
        "geometry": "wall_clock",
    }


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    LOG.write_text("", encoding="utf-8")
    t0 = time.perf_counter()
    _log(
        f"DISPLAY_ONLY_CLEAN_OOS_SLICE window=[{DISPLAY_START},{DISPLAY_END}) "
        f"lockbox={FORWARD_LOCKBOX_START} arm=wall_clock_q75 "
        f"bot=llm2_structure_eth_15m_multitrade_wall_clock_p75"
    )
    conf = run_conformance_check()
    if conf.get("passed") is False:
        raise RuntimeError("conformance failed")
    if "botsgeneral" not in str(__import__("tradesim").__file__).lower():
        raise RuntimeError("tradesim not botsgeneral")

    disp0 = pd.Timestamp(DISPLAY_START, tz="UTC")
    disp1 = pd.Timestamp(DISPLAY_END, tz="UTC")
    lock = pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC")
    assert disp1 <= lock, "display end must not enter lockbox"

    ohlcv = load_ohlcv(SYMBOL, TIMEFRAME)
    ohlcv = ohlcv.loc[index_to_ms(ohlcv.index) < int(lock.value // 1_000_000)].copy()
    feats = build_space(ohlcv, SPACE, symbol=SYMBOL, timeframe=TIMEFRAME)
    y = build_direction_labels(ohlcv, horizon=LABEL_HORIZON)["direction"]
    aligned = feats.join(y.rename("y"), how="inner").dropna()
    ts_ms = index_to_ms(aligned.index)
    disp0_ms = int(disp0.value // 1_000_000)
    disp1_ms = int(disp1.value // 1_000_000)
    purge_ms = LABEL_HORIZON * int(TF_MS[TIMEFRAME])
    train_end_ms = disp0_ms - purge_ms
    tr = np.where(ts_ms < train_end_ms)[0]
    oos = np.where((ts_ms >= disp0_ms) & (ts_ms < disp1_ms))[0]
    if tr.size < 500 or oos.size < 50:
        raise RuntimeError(f"insufficient bars train={tr.size} oos={oos.size}")

    cols = [c for c in aligned.columns if c != "y"]
    X = aligned[cols].to_numpy(dtype=float)
    yv = aligned["y"].to_numpy(dtype=float)
    _log(f"train_n={tr.size} display_n={oos.size} features={len(cols)}")

    model = LGBMRegressorPredictor(n_estimators=80, learning_rate=0.05)
    model.fit(X[tr], yv[tr])
    pred = model.predict(X[oos])
    mean = np.asarray(pred.mean, dtype=float).reshape(-1)
    side = proxy_side(mean, target_family(TARGET))
    close_oos = ohlcv["close"].reindex(aligned.index).to_numpy(dtype=float)[oos]
    sigs, stats = build_multitrade_signals(
        ts_ms[oos], side, mean, cfg=_cfg(), close=close_oos
    )
    _log(
        f"signals emitted={stats.get('n_emitted')} "
        f"skipped_clarity={stats.get('n_skipped_clarity')}"
    )

    oos0, oos1 = aligned.index[oos[0]], aligned.index[oos[-1]]
    pad = max(50, HOLD_ADDON * 4)
    pos = int(ohlcv.index.searchsorted(oos0))
    window = ohlcv.loc[ohlcv.index[max(0, pos - pad)] : oos1]
    touch_tf = touch_timeframe(TIMEFRAME, SYMBOL)
    touch = load_ohlcv(SYMBOL, touch_tf)
    end, start = window.index[-1], window.index[0]
    dec_ms = int(TF_MS[TIMEFRAME])
    touch_end = end + pd.Timedelta(milliseconds=dec_ms) - pd.Timedelta(milliseconds=1)
    touch_win = touch.loc[(touch.index >= start) & (touch.index <= touch_end)]
    funding = load_funding(SYMBOL)
    funding = funding[funding.index < lock]
    funding_ts = (funding.index.asi8 // 1_000_000).astype(np.int64)
    funding_rt = funding.to_numpy(dtype=float)
    w_ts = index_to_ms(window.index)
    fmask = (funding_ts >= int(w_ts[0])) & (funding_ts <= int(w_ts[-1]))
    lev = float(leverage_from_stop(SL))

    bundle = run_strategy_backtest(
        window,
        sigs,
        symbol=SYMBOL,
        timeframe=TIMEFRAME,
        strategy_id="eth_15m_wall_clock_q75_last1m_clean",
        touch_ohlcv=touch_win,
        touch_timeframe=touch_tf,
        costs=research_costs_baseline(),
        margin=research_margin(leverage=lev),
        sizing=research_sizing(),
        sim=research_sim_hedge(
            max_hold_bars=HOLD_ADDON,
            decision_timeframe=TIMEFRAME,
            max_positions_per_side=K,
            max_positions_per_symbol=K * 2,
        ),
        instrument=research_instrument(SYMBOL),
        funding_ts_ms=funding_ts[fmask],
        funding_rate=funding_rt[fmask],
        strategy_meta={
            "name": "eth_15m_wall_clock_q75_last1m_clean",
            "evidence_class": "DISPLAY_ONLY_CLEAN_OOS_SLICE",
            "window": [DISPLAY_START, DISPLAY_END],
            "lockbox_used": False,
            "selection_on_slice": False,
            "geometry": "wall_clock",
            "strength_quantile": STRENGTH_Q,
            "live_bot": "llm2_structure_eth_15m_multitrade_wall_clock_p75",
        },
        plot=False,
        print_headline=True,
        store_path=str(STORE),
    )
    m = bundle.metrics
    n_tr = int(m.n_trades)
    sh = getattr(m, "sharpe", None)
    sharpe_ann = None
    if sh is not None:
        sharpe_ann = float(
            getattr(sh, "annualised", getattr(sh, "annualized", float("nan")))
        )
    blob = {
        "evidence_class": "DISPLAY_ONLY_CLEAN_OOS_SLICE",
        "promotion_allowed": False,
        "lockbox_used": False,
        "selection_on_slice": False,
        "window": [DISPLAY_START, DISPLAY_END],
        "arm": "wall_clock_q75",
        "live_bot": "llm2_structure_eth_15m_multitrade_wall_clock_p75",
        "timeframe": TIMEFRAME,
        "touch_timeframe": touch_tf,
        "n_trades": n_tr,
        "profit_factor": float(m.profit_factor),
        "win_rate": float(getattr(m, "win_rate", float("nan"))),
        "expectancy_return_units": float(
            getattr(m, "expectancy_return_units", float("nan"))
        ),
        "expectancy": float(getattr(m, "expectancy", float("nan"))),
        "net_pnl": float(m.net_pnl),
        "payoff_ratio": float(getattr(m, "payoff_ratio", float("nan"))),
        "avg_win": float(getattr(m, "avg_win", float("nan"))),
        "avg_loss": float(getattr(m, "avg_loss", float("nan"))),
        "total_fees": float(getattr(m, "total_fees", float("nan"))),
        "n_liquidations": int(getattr(m, "n_liquidations", 0) or 0),
        "entry_bar_exits": int(getattr(m, "entry_bar_exits", 0) or 0),
        "sharpe_annualised": sharpe_ann,
        "signal_stats": stats,
        "run_id": getattr(bundle, "run_id", None),
        "created_utc": datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ"),
        "elapsed_sec": round(time.perf_counter() - t0, 1),
        "note": (
            "Last month of pre-lockbox outer OOS only [2026-04-01,2026-05-01). "
            "Calendar May–Aug 2026 is lockbox/live and was NOT used. Not a promotion gate."
        ),
    }
    latest = OUT_DIR / "metrics_latest.json"
    latest.write_text(json.dumps(blob, indent=2, default=str), encoding="utf-8")
    _log(f"wrote {latest}")
    _log(
        f"METRICS n={n_tr} pf={blob['profit_factor']:.4f} "
        f"eru={blob['expectancy_return_units']:.6f} wr={blob['win_rate']:.4f} "
        f"pnl={blob['net_pnl']:.4f} liq={blob['n_liquidations']}"
    )

    plot_ohlcv = ohlcv.loc[(ohlcv.index >= disp0) & (ohlcv.index < disp1)].copy()
    bars = ohlcv_to_bar_series(plot_ohlcv, symbol=SYMBOL, timeframe=TIMEFRAME)
    title = (
        f"ETH 15m wall_clock_q75 | CLEAN OOS [{DISPLAY_START},{DISPLAY_END}) "
        f"| n={n_tr} | DISPLAY_ONLY (no lockbox)"
    )
    _log(f"opening Finplot bars={len(plot_ohlcv)} trades={n_tr} …")
    plot_backtest(
        bars,
        bundle.result,
        title=title,
        metrics=m,
        strategy_meta={
            "name": "eth_15m_wall_clock_q75_last1m_clean",
            "evidence_class": "DISPLAY_ONLY_CLEAN_OOS_SLICE",
        },
        trade_style="lines",
        trade_labels="none",
        max_zone_trades=0,
        show=True,
        show_metrics_window=True,
    )
    _log("finplot returned")
    print(json.dumps(blob, indent=2, default=str))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
