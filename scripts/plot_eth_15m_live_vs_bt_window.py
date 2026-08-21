"""Side-by-side Finplot: LIVE 15m ordered trades vs FREE backtest on same window.

LIVE path: reconstruct tradesim Signals from ledger orders (order_retCode=0)
           with live TP/SL/hold, then simulate exits on research candles.
BT path:   frozen pack model + multitrade wall_clock p75 gate free-running
           on the identical OHLCV window (warmed for strength lookback).

Evidence class: LIVE_VS_BT_DISPLAY_ONLY — not a promotion gate.
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

import joblib  # noqa: E402
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

from tradesim import Side, Signal  # noqa: E402
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
from llm2.paths import ARTIFACTS, TF_MS, touch_timeframe  # noqa: E402
from llm2.validation.folds import index_to_ms  # noqa: E402

SYMBOL = "ETHUSDT"
TIMEFRAME = "15m"
PACK = (
    ARTIFACTS
    / "live_packs"
    / "structure_v1_ethusdt_15m_multitrade_wall_clock_p75_v1"
)
LEDGER = ARTIFACTS / "reports" / "_live_15m_ledger_dump.json"
OUT_DIR = ARTIFACTS / "reports" / "structure_v1_eth_15m_live_vs_bt_window"
STORE = Path(r"D:\projectsdata\backtests\tradesim_runs.sqlite")
LOG = OUT_DIR / "_finplot.log"
SL = 0.02
MIN_EDGE = DIRECTION_BAND
HOLD_ADDON = 48
BASE_HOLD = 24
MEAN_LOOKBACK = 672
K = 7
FIB = 1.618
STRENGTH_Q = 0.75


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


def _metrics_blob(bundle, *, label: str, extra: dict) -> dict:
    m = bundle.metrics
    sh = getattr(m, "sharpe", None)
    sharpe_ann = None
    if sh is not None:
        sharpe_ann = float(
            getattr(sh, "annualised", getattr(sh, "annualized", float("nan")))
        )
    return {
        "label": label,
        "n_trades": int(m.n_trades),
        "profit_factor": float(m.profit_factor),
        "win_rate": float(getattr(m, "win_rate", float("nan"))),
        "expectancy_return_units": float(
            getattr(m, "expectancy_return_units", float("nan"))
        ),
        "expectancy": float(getattr(m, "expectancy", float("nan"))),
        "net_pnl": float(m.net_pnl),
        "payoff_ratio": float(getattr(m, "payoff_ratio", float("nan"))),
        "total_fees": float(getattr(m, "total_fees", float("nan"))),
        "n_liquidations": int(getattr(m, "n_liquidations", 0) or 0),
        "entry_bar_exits": int(getattr(m, "entry_bar_exits", 0) or 0),
        "sharpe_annualised": sharpe_ann,
        "run_id": getattr(bundle, "run_id", None),
        **extra,
    }


def _load_live_orders(ledger: dict) -> list[dict]:
    out = []
    for d in ledger.get("decisions") or []:
        det = d.get("detail") or {}
        ret = det.get("order_retCode")
        if ret not in (0, "0") and ret != 0:
            continue
        side = int(d.get("side") or 0)
        if side == 0:
            continue
        out.append(
            {
                "bar_ts_ms": int(d["bar_ts_ms"]),
                "bar_utc": d.get("bar_utc"),
                "side": side,
                "pred_mean": float(d.get("pred_mean") or 0.0),
                "tp_pct": float(det.get("tp_pct") or 0.01),
                "sl_pct": float(det.get("sl_pct") or SL),
                "max_hold_bars": int(
                    det.get("max_hold_bars") or det.get("hold") or BASE_HOLD
                ),
                "qty": float(det.get("order_qty") or 0.01),
                "book_idx": int(det.get("book_idx") or 0),
            }
        )
    return out


def _live_signals(orders: list[dict]) -> list[Signal]:
    sigs: list[Signal] = []
    for o in orders:
        sigs.append(
            Signal(
                ts_ms=int(o["bar_ts_ms"]),
                side=Side.LONG if o["side"] > 0 else Side.SHORT,
                symbol=SYMBOL,
                stop_offset=float(o["sl_pct"]),
                target_offset=float(o["tp_pct"]),
                max_hold_bars=int(o["max_hold_bars"]),
                qty=float(o["qty"]),
                tag=f"live_b{o.get('book_idx') or 0}",
                meta={
                    "source": "live_ledger_order",
                    "pred_mean": float(o["pred_mean"]),
                    "book_idx": o.get("book_idx"),
                },
            )
        )
    return sigs


def _run(
    window: pd.DataFrame,
    sigs: list[Signal],
    *,
    strategy_id: str,
    strategy_meta: dict,
    touch: pd.DataFrame,
    touch_tf: str,
    funding_ts: np.ndarray,
    funding_rt: np.ndarray,
) -> object:
    w_ts = index_to_ms(window.index)
    fmask = (funding_ts >= int(w_ts[0])) & (funding_ts <= int(w_ts[-1]))
    lev = float(leverage_from_stop(SL))
    return run_strategy_backtest(
        window,
        sigs,
        symbol=SYMBOL,
        timeframe=TIMEFRAME,
        strategy_id=strategy_id,
        touch_ohlcv=touch,
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
        strategy_meta=strategy_meta,
        plot=False,
        print_headline=True,
        store_path=str(STORE),
    )


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    LOG.write_text("", encoding="utf-8")
    t0 = time.perf_counter()
    conf = run_conformance_check()
    if conf.get("passed") is False:
        raise RuntimeError("conformance failed")
    if "botsgeneral" not in str(__import__("tradesim").__file__).lower():
        raise RuntimeError("tradesim not botsgeneral")
    if not LEDGER.is_file():
        raise FileNotFoundError(f"missing live ledger dump {LEDGER}")
    if not (PACK / "model.joblib").is_file():
        raise FileNotFoundError(PACK)

    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
    orders = _load_live_orders(ledger)
    if not orders:
        raise RuntimeError("no live orders in ledger dump")
    live_start_ms = min(o["bar_ts_ms"] for o in orders)
    live_end_ms = max(int(d["bar_ts_ms"]) for d in ledger["decisions"])
    # Pad after last decision for max-hold exits.
    pad_end_ms = live_end_ms + HOLD_ADDON * int(TF_MS[TIMEFRAME])
    warm_start_ms = live_start_ms - (MEAN_LOOKBACK + 500) * int(TF_MS[TIMEFRAME])

    _log(
        f"LIVE window orders n={len(orders)} "
        f"[{datetime.fromtimestamp(live_start_ms/1000,tz=timezone.utc)} → "
        f"{datetime.fromtimestamp(live_end_ms/1000,tz=timezone.utc)}] "
        f"sim_end_pad={datetime.fromtimestamp(pad_end_ms/1000,tz=timezone.utc)}"
    )

    strategy = json.loads((PACK / "strategy.json").read_text(encoding="utf-8"))
    blob = joblib.load(PACK / "model.joblib")
    if isinstance(blob, dict) and "model" in blob:
        model = blob["model"]
        cols = list(blob.get("feature_columns") or strategy.get("feature_columns") or [])
    else:
        model = blob
        cols = list(strategy.get("feature_columns") or [])
    if not cols:
        raise RuntimeError("pack missing feature_columns")

    ohlcv = load_ohlcv(SYMBOL, TIMEFRAME)
    ohlcv = ohlcv.loc[
        (index_to_ms(ohlcv.index) >= warm_start_ms)
        & (index_to_ms(ohlcv.index) <= pad_end_ms)
    ].copy()
    if len(ohlcv) < MEAN_LOOKBACK + 50:
        raise RuntimeError(f"insufficient OHLCV after warm load: {len(ohlcv)}")

    feats = build_space(
        ohlcv, "structure_v1", symbol=SYMBOL, timeframe=TIMEFRAME, recent_only=False
    )
    aligned = feats.reindex(columns=cols)
    for c in aligned.columns:
        if c == "last_retrace_pct" or str(c).startswith("last_retrace_pct_"):
            aligned[c] = aligned[c].fillna(0.0)
    # Drop rows with remaining NaN (structure warmup tip)
    valid = aligned.dropna()
    X = valid.to_numpy(dtype=float)
    pred = model.predict(X)
    mean = np.asarray(
        pred.mean if hasattr(pred, "mean") else pred, dtype=float
    ).reshape(-1)
    side = proxy_side(mean, target_family(str(strategy.get("target", "direction"))))
    close_v = ohlcv["close"].reindex(valid.index).to_numpy(dtype=float)
    ts_v = index_to_ms(valid.index)

    # Restrict free-run emission window to live decide range (still warm strength before).
    emit_mask = (ts_v >= live_start_ms) & (ts_v <= live_end_ms)
    pre_mask = ts_v < live_start_ms
    seed_hist = [float(abs(m)) for m in mean[pre_mask] if np.isfinite(m)]
    seed_hist = seed_hist[-MEAN_LOOKBACK:]
    free_sigs, free_stats = build_multitrade_signals(
        ts_v[emit_mask],
        side[emit_mask],
        mean[emit_mask],
        cfg=_cfg(),
        close=close_v[emit_mask],
        seed_strength_hist=seed_hist,
    )
    live_sigs = _live_signals(orders)
    _log(
        f"free_sigs={len(free_sigs)} live_sigs={len(live_sigs)} "
        f"emit_n={int(emit_mask.sum())} seed_strength_n={len(seed_hist)}"
    )

    # Comparison of entry timestamps
    free_ts = {int(s.ts_ms) for s in free_sigs}
    live_ts = {int(s.ts_ms) for s in live_sigs}
    entry_cmp = {
        "n_live_entries": len(live_ts),
        "n_bt_entries": len(free_ts),
        "intersection": len(live_ts & free_ts),
        "live_only": sorted(live_ts - free_ts),
        "bt_only": sorted(free_ts - live_ts),
        "live_only_utc": [
            datetime.fromtimestamp(t / 1000, tz=timezone.utc).isoformat()
            for t in sorted(live_ts - free_ts)
        ],
        "bt_only_utc": [
            datetime.fromtimestamp(t / 1000, tz=timezone.utc).isoformat()
            for t in sorted(free_ts - live_ts)
        ],
    }
    _log(
        f"entry_match live={entry_cmp['n_live_entries']} bt={entry_cmp['n_bt_entries']} "
        f"both={entry_cmp['intersection']} live_only={len(entry_cmp['live_only'])} "
        f"bt_only={len(entry_cmp['bt_only'])}"
    )

    # Sim window: pad after live for exits; slight pre for chart context
    win0 = pd.Timestamp(live_start_ms, unit="ms", tz="UTC") - pd.Timedelta(hours=6)
    win1 = pd.Timestamp(pad_end_ms, unit="ms", tz="UTC")
    window = ohlcv.loc[(ohlcv.index >= win0) & (ohlcv.index <= win1)].copy()
    touch_tf = touch_timeframe(TIMEFRAME, SYMBOL)
    touch_full = load_ohlcv(SYMBOL, touch_tf)
    dec_ms = int(TF_MS[TIMEFRAME])
    touch_end = window.index[-1] + pd.Timedelta(milliseconds=dec_ms) - pd.Timedelta(
        milliseconds=1
    )
    touch = touch_full.loc[
        (touch_full.index >= window.index[0]) & (touch_full.index <= touch_end)
    ]
    funding = load_funding(SYMBOL)
    funding_ts = (funding.index.asi8 // 1_000_000).astype(np.int64)
    funding_rt = funding.to_numpy(dtype=float)

    common_meta = {
        "evidence_class": "LIVE_VS_BT_DISPLAY_ONLY",
        "live_unit": "llm2-structure-eth-15m-multitrade-wall-clock-p75-v1",
        "window_live": [
            datetime.fromtimestamp(live_start_ms / 1000, tz=timezone.utc).isoformat(),
            datetime.fromtimestamp(live_end_ms / 1000, tz=timezone.utc).isoformat(),
        ],
        "promotion_allowed": False,
    }

    _log("running LIVE-order-forced sim …")
    live_bundle = _run(
        window,
        live_sigs,
        strategy_id="eth_15m_live_orders_forced",
        strategy_meta={**common_meta, "arm": "live_orders_forced"},
        touch=touch,
        touch_tf=touch_tf,
        funding_ts=funding_ts,
        funding_rt=funding_rt,
    )
    _log("running FREE BT sim …")
    free_bundle = _run(
        window,
        free_sigs,
        strategy_id="eth_15m_free_bt_live_window",
        strategy_meta={**common_meta, "arm": "free_multitrade_wall_clock_p75"},
        touch=touch,
        touch_tf=touch_tf,
        funding_ts=funding_ts,
        funding_rt=funding_rt,
    )

    live_m = _metrics_blob(
        live_bundle,
        label="LIVE_ORDERS_FORCED_THROUGH_TRADESIM",
        extra={"n_live_ledger_orders": len(orders), "signal_stats": None},
    )
    free_m = _metrics_blob(
        free_bundle,
        label="FREE_BACKTEST_PACK_MODEL",
        extra={"signal_stats": free_stats},
    )
    report = {
        "evidence_class": "LIVE_VS_BT_DISPLAY_ONLY",
        "promotion_allowed": False,
        "created_utc": datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ"),
        "elapsed_sec": round(time.perf_counter() - t0, 1),
        "live_metrics": live_m,
        "backtest_metrics": free_m,
        "entry_comparison": entry_cmp,
        "note": (
            "LIVE chart uses ledger order entries (order_retCode=0) forced into "
            "tradesim with live TP/hold/qty; FREE BT uses frozen pack model + "
            "multitrade gate on the same candle window. Display-only."
        ),
    }
    (OUT_DIR / "metrics_latest.json").write_text(
        json.dumps(report, indent=2, default=str), encoding="utf-8"
    )
    _log(f"wrote {OUT_DIR / 'metrics_latest.json'}")
    _log(
        "METRICS_LIVE "
        f"n={live_m['n_trades']} pf={live_m['profit_factor']:.4f} "
        f"eru={live_m['expectancy_return_units']:.6f} wr={live_m['win_rate']:.4f} "
        f"pnl={live_m['net_pnl']:.4f}"
    )
    _log(
        "METRICS_BT "
        f"n={free_m['n_trades']} pf={free_m['profit_factor']:.4f} "
        f"eru={free_m['expectancy_return_units']:.6f} wr={free_m['win_rate']:.4f} "
        f"pnl={free_m['net_pnl']:.4f}"
    )
    print(json.dumps(report, indent=2, default=str))

    plot_ohlcv = ohlcv.loc[
        (index_to_ms(ohlcv.index) >= live_start_ms)
        & (index_to_ms(ohlcv.index) <= live_end_ms)
    ].copy()
    # include a little exit tail on the chart
    plot_end = min(
        pad_end_ms,
        int(index_to_ms(ohlcv.index)[-1]),
    )
    plot_ohlcv = ohlcv.loc[
        (index_to_ms(ohlcv.index) >= live_start_ms - 6 * 3_600_000)
        & (index_to_ms(ohlcv.index) <= plot_end)
    ].copy()
    bars = ohlcv_to_bar_series(plot_ohlcv, symbol=SYMBOL, timeframe=TIMEFRAME)

    title_live = (
        f"ETH 15m LIVE orders (forced sim) | n={live_m['n_trades']} "
        f"PF={live_m['profit_factor']:.2f} | ledger Xxobster11"
    )
    title_bt = (
        f"ETH 15m FREE backtest (pack model) | n={free_m['n_trades']} "
        f"PF={free_m['profit_factor']:.2f} | same window"
    )
    _log("opening LIVE Finplot …")
    plot_backtest(
        bars,
        live_bundle.result,
        title=title_live,
        metrics=live_bundle.metrics,
        strategy_meta={"name": "eth_15m_live_orders_forced", **common_meta},
        trade_style="lines",
        trade_labels="none",
        max_zone_trades=0,
        show=True,
        show_metrics_window=True,
    )
    _log("opening FREE BT Finplot …")
    plot_backtest(
        bars,
        free_bundle.result,
        title=title_bt,
        metrics=free_bundle.metrics,
        strategy_meta={"name": "eth_15m_free_bt_live_window", **common_meta},
        trade_style="lines",
        trade_labels="none",
        max_zone_trades=0,
        show=True,
        show_metrics_window=True,
    )
    _log("finplots returned")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
