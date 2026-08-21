"""Live-order forced vs free pack backtest Finplots for Xxobster7/8/10 llm2 units.

For each configured bot:
  - LIVE: ledger order_retCode=0 entries forced into tradesim (live TP/SL/hold/qty)
  - FREE BT: frozen pack model + single-book or multitrade gate on same candle window
  - metrics JSON + two Finplots

Evidence class: LIVE_VS_BT_DISPLAY_ONLY (not a promotion gate).
"""

from __future__ import annotations

import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

# Headless batch: set TRADESIM_NO_PLOT=1 to skip charts; default shows Finplots.
# os.environ.setdefault("TRADESIM_NO_PLOT", "0")

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
from llm2.paths import ARTIFACTS, ROUND_TRIP_COST, TF_MS, touch_timeframe  # noqa: E402
from llm2.validation.folds import index_to_ms  # noqa: E402

LEDGERS = ARTIFACTS / "reports" / "_llm2_ln1_all_unit_ledgers.json"
OUT_ROOT = ARTIFACTS / "reports" / "llm2_accounts_live_vs_bt"
STORE = Path(r"D:\projectsdata\backtests\tradesim_runs.sqlite")
PACKS = ARTIFACTS / "live_packs"

# Account → active bots (host ln1 94.x)
BOTS: list[dict[str, Any]] = [
    # Xxobster8
    {
        "account": "Xxobster8",
        "ledger_key": "llm2-structure-eth-multitrade-v1_2",
        "pack": "structure_v1_ethusdt_multitrade_v1_2",
        "label": "ETH_multitrade_v1_2",
    },
    # Xxobster7 single-book fleet
    {
        "account": "Xxobster7",
        "ledger_key": "llm2-structure",
        "pack": "structure_v1_lgbm",
        "label": "BTC_single",
    },
    {
        "account": "Xxobster7",
        "ledger_key": "llm2-structure-eth",
        "pack": "structure_v1_ethusdt_direction",
        "label": "ETH_single",
    },
    {
        "account": "Xxobster7",
        "ledger_key": "llm2-structure-sol",
        "pack": "structure_v1_solusdt_direction",
        "label": "SOL_single",
    },
    # Xxobster10 K5 double
    {
        "account": "Xxobster10",
        "ledger_key": "llm2-structure-btc-k5-double3h-v1",
        "pack": "structure_v1_btcusdt_k5_double3h_v1",
        "label": "BTC_k5_double3h",
    },
    {
        "account": "Xxobster10",
        "ledger_key": "llm2-structure-sol-k5-double3h-v1",
        "pack": "structure_v1_solusdt_k5_double3h_v1",
        "label": "SOL_k5_double3h",
    },
]


def _log(path: Path, msg: str) -> None:
    print(msg, flush=True)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as fh:
        fh.write(msg + "\n")


def _metrics_blob(bundle) -> dict:
    m = bundle.metrics
    sh = getattr(m, "sharpe", None)
    sharpe_ann = None
    if sh is not None:
        sharpe_ann = float(
            getattr(sh, "annualised", getattr(sh, "annualized", float("nan")))
        )
    return {
        "n_trades": int(m.n_trades),
        "profit_factor": float(m.profit_factor) if np.isfinite(float(m.profit_factor)) else None,
        "profit_factor_raw": float(m.profit_factor),
        "win_rate": float(getattr(m, "win_rate", float("nan"))),
        "expectancy_return_units": float(
            getattr(m, "expectancy_return_units", float("nan"))
        ),
        "expectancy": float(getattr(m, "expectancy", float("nan"))),
        "net_pnl": float(m.net_pnl),
        "total_fees": float(getattr(m, "total_fees", float("nan"))),
        "n_liquidations": int(getattr(m, "n_liquidations", 0) or 0),
        "entry_bar_exits": int(getattr(m, "entry_bar_exits", 0) or 0),
        "sharpe_annualised": sharpe_ann,
        "run_id": getattr(bundle, "run_id", None),
    }


def _orders_from_ledger(unit: dict) -> list[dict]:
    out = []
    for d in unit.get("decisions") or []:
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
                "tp_pct": float(det.get("tp_pct") or unit.get("tp_pct") or 0.01),
                "sl_pct": float(det.get("sl_pct") or unit.get("sl_pct") or 0.02),
                "max_hold_bars": int(
                    det.get("max_hold_bars")
                    or det.get("hold")
                    or unit.get("horizon_bars")
                    or 6
                ),
                "qty": float(det.get("order_qty") or 0.0) or None,
                "book_idx": int(det.get("book_idx") or 0),
            }
        )
    return out


def _live_sigs(orders: list[dict], *, symbol: str, default_sl: float) -> list[Signal]:
    sigs = []
    for o in orders:
        kw: dict[str, Any] = {
            "ts_ms": int(o["bar_ts_ms"]),
            "side": Side.LONG if o["side"] > 0 else Side.SHORT,
            "symbol": symbol,
            "stop_offset": float(o.get("sl_pct") or default_sl),
            "target_offset": float(o["tp_pct"]),
            "max_hold_bars": int(o["max_hold_bars"]),
            "tag": f"live_b{o.get('book_idx') or 0}",
            "meta": {
                "source": "live_ledger_order",
                "pred_mean": float(o["pred_mean"]),
                "book_idx": o.get("book_idx"),
            },
        }
        if o.get("qty"):
            kw["qty"] = float(o["qty"])
        sigs.append(Signal(**kw))
    return sigs


def _mt_cfg_from_strategy(strategy: dict) -> dict:
    mt = dict(strategy.get("multitrade") or {})
    tf = str(strategy.get("timeframe") or "1h")
    fam = target_family(str(strategy.get("target") or "direction"))
    default_edge = (
        DIRECTION_BAND if fam == "directional" else ROUND_TRIP_COST
    )
    base = {
        "max_positions_per_side": int(
            mt.get("max_positions_per_side")
            or strategy.get("max_positions_per_side")
            or 1
        ),
        "clarity": str(mt.get("clarity") or "none"),
        "clarity_scope": str(mt.get("clarity_scope") or "addon"),
        "fib_ext": float(mt.get("fib_ext") or 0.0),
        "hold_addon": int(mt.get("hold_addon") or strategy.get("horizon_bars") or 6),
        "base_hold": int(mt.get("base_hold") or strategy.get("horizon_bars") or 6),
        "base_tp": float(mt.get("base_tp") or strategy.get("tp_pct") or 0.01),
        "base_sl": float(mt.get("base_sl") or strategy.get("sl_pct") or 0.02),
        "mean_lookback": int(mt.get("mean_lookback") or 168),
        "uniform_books": bool(mt.get("uniform_books", False)),
        "bar_ms": int(mt.get("bar_ms") or TF_MS.get(tf, 3_600_000)),
        "strength_quantile": float(mt.get("strength_quantile") or 0.5),
        "geometry": str(mt.get("geometry") or "bar_count"),
        "size_double_within_bars": int(mt.get("size_double_within_bars") or 0),
        "size_double_mult": float(mt.get("size_double_mult") or 2.0),
        # BTC/SOL k5 packs use fwd_return (edge ~ ROUND_TRIP_COST), not direction 0.10.
        "min_edge": float(strategy.get("min_edge") or default_edge),
    }
    return base


def _singlebook_signals(
    ts_ms: np.ndarray,
    side: np.ndarray,
    mean: np.ndarray,
    *,
    symbol: str,
    tp: float,
    sl: float,
    hold: int,
    min_edge: float,
) -> tuple[list[Signal], dict]:
    out: list[Signal] = []
    n_emit = 0
    for i in range(len(ts_ms)):
        s = int(side[i])
        m = float(mean[i])
        if s == 0 or not np.isfinite(m) or abs(m) < min_edge:
            continue
        out.append(
            Signal(
                ts_ms=int(ts_ms[i]),
                side=Side.LONG if s > 0 else Side.SHORT,
                symbol=symbol,
                stop_offset=float(sl),
                target_offset=float(tp),
                max_hold_bars=int(hold),
                tag="single",
                meta={"pred_mean": float(m)},
            )
        )
        n_emit += 1
    return out, {"n_emitted": n_emit}


def _run_bt(
    window: pd.DataFrame,
    sigs: list[Signal],
    *,
    symbol: str,
    timeframe: str,
    strategy_id: str,
    strategy_meta: dict,
    sl: float,
    k_side: int,
    touch: pd.DataFrame,
    touch_tf: str,
    funding_ts: np.ndarray,
    funding_rt: np.ndarray,
    max_hold_cap: int,
) -> object:
    w_ts = index_to_ms(window.index)
    fmask = (funding_ts >= int(w_ts[0])) & (funding_ts <= int(w_ts[-1]))
    lev = float(leverage_from_stop(sl))
    return run_strategy_backtest(
        window,
        sigs,
        symbol=symbol,
        timeframe=timeframe,
        strategy_id=strategy_id,
        touch_ohlcv=touch,
        touch_timeframe=touch_tf,
        costs=research_costs_baseline(),
        margin=research_margin(leverage=lev),
        sizing=research_sizing(),
        sim=research_sim_hedge(
            max_hold_bars=max_hold_cap,
            decision_timeframe=timeframe,
            max_positions_per_side=max(1, k_side),
            max_positions_per_symbol=max(1, k_side * 2),
        ),
        instrument=research_instrument(symbol),
        funding_ts_ms=funding_ts[fmask],
        funding_rate=funding_rt[fmask],
        strategy_meta=strategy_meta,
        plot=False,
        print_headline=True,
        store_path=str(STORE),
    )


def process_bot(bot: dict, all_ledgers: dict, *, plot: bool) -> dict:
    key = bot["ledger_key"]
    pack_name = bot["pack"]
    account = bot["account"]
    label = bot["label"]
    out_dir = OUT_ROOT / f"{account}_{label}"
    log = out_dir / "_run.log"
    out_dir.mkdir(parents=True, exist_ok=True)
    log.write_text("", encoding="utf-8")
    t0 = time.perf_counter()

    unit = all_ledgers.get(key) or {}
    if unit.get("error") or not unit.get("decisions"):
        rep = {"error": "no_ledger", "account": account, "label": label, "key": key}
        (out_dir / "metrics_latest.json").write_text(json.dumps(rep, indent=2), encoding="utf-8")
        return rep

    pack = PACKS / pack_name
    strategy = json.loads((pack / "strategy.json").read_text(encoding="utf-8"))
    symbol = str(strategy.get("symbol") or unit.get("strategy_symbol") or "ETHUSDT")
    timeframe = str(strategy.get("timeframe") or unit.get("strategy_timeframe") or "1h")
    sl = float(strategy.get("sl_pct") or 0.02)
    tp = float(strategy.get("tp_pct") or 0.01)
    hold = int(strategy.get("horizon_bars") or 6)
    target = str(strategy.get("target") or "direction")
    family = target_family(target)
    min_edge = float(
        strategy.get("min_edge")
        or (DIRECTION_BAND if family == "directional" else ROUND_TRIP_COST)
    )
    is_mt = str(strategy.get("execution_mode") or "").lower() == "multitrade" or bool(
        strategy.get("multitrade")
    )
    mt_cfg = _mt_cfg_from_strategy(strategy) if is_mt else {}
    k_side = int(mt_cfg.get("max_positions_per_side") or 1)
    max_hold_cap = int(mt_cfg.get("hold_addon") or hold)

    blob = joblib.load(pack / "model.joblib")
    if isinstance(blob, dict) and "model" in blob:
        model = blob["model"]
        cols = list(blob.get("feature_columns") or strategy.get("feature_columns") or [])
    else:
        model = blob
        cols = list(strategy.get("feature_columns") or [])

    orders = _orders_from_ledger({**unit, "tp_pct": tp, "sl_pct": sl, "horizon_bars": hold})
    if not orders:
        rep = {
            "error": "no_live_orders",
            "account": account,
            "label": label,
            "n_decisions": unit.get("n_decisions"),
        }
        (out_dir / "metrics_latest.json").write_text(json.dumps(rep, indent=2), encoding="utf-8")
        _log(log, f"SKIP {account}/{label}: no orders")
        return rep

    live_start_ms = min(o["bar_ts_ms"] for o in orders)
    live_end_ms = max(int(d["bar_ts_ms"]) for d in unit["decisions"])
    lookback = int(mt_cfg.get("mean_lookback") or 168)
    warm_start_ms = live_start_ms - (lookback + 400) * int(TF_MS[timeframe])
    pad_end_ms = live_end_ms + max_hold_cap * int(TF_MS[timeframe])

    _log(
        log,
        f"=== {account}/{label} {symbol} {timeframe} orders={len(orders)} "
        f"mt={is_mt} K={k_side} window="
        f"{datetime.fromtimestamp(live_start_ms/1000,tz=timezone.utc)}→"
        f"{datetime.fromtimestamp(live_end_ms/1000,tz=timezone.utc)}",
    )

    ohlcv = load_ohlcv(symbol, timeframe)
    ohlcv = ohlcv.loc[
        (index_to_ms(ohlcv.index) >= warm_start_ms)
        & (index_to_ms(ohlcv.index) <= pad_end_ms)
    ].copy()
    feats = build_space(
        ohlcv, "structure_v1", symbol=symbol, timeframe=timeframe, recent_only=False
    )
    aligned = feats.reindex(columns=cols)
    for c in aligned.columns:
        if c == "last_retrace_pct" or str(c).startswith("last_retrace_pct_"):
            aligned[c] = aligned[c].fillna(0.0)
    valid = aligned.dropna()
    X = valid.to_numpy(dtype=float)
    pred = model.predict(X)
    mean = np.asarray(pred.mean if hasattr(pred, "mean") else pred, dtype=float).reshape(
        -1
    )
    side = proxy_side(mean, family)
    close_v = ohlcv["close"].reindex(valid.index).to_numpy(dtype=float)
    ts_v = index_to_ms(valid.index)
    emit_mask = (ts_v >= live_start_ms) & (ts_v <= live_end_ms)
    pre_mask = ts_v < live_start_ms
    seed_hist = [float(abs(m)) for m in mean[pre_mask] if np.isfinite(m)][-lookback:]

    if is_mt:
        occ_ts = index_to_ms(ohlcv.index)
        free_sigs, free_stats = build_multitrade_signals(
            ts_v[emit_mask],
            side[emit_mask],
            mean[emit_mask],
            cfg=mt_cfg,
            close=close_v[emit_mask],
            seed_strength_hist=seed_hist,
            occupancy_bars={
                "ts_ms": occ_ts,
                "open": ohlcv["open"].to_numpy(dtype=float),
                "high": ohlcv["high"].to_numpy(dtype=float),
                "low": ohlcv["low"].to_numpy(dtype=float),
            },
        )
    else:
        free_sigs, free_stats = _singlebook_signals(
            ts_v[emit_mask],
            side[emit_mask],
            mean[emit_mask],
            symbol=symbol,
            tp=tp,
            sl=sl,
            hold=hold,
            min_edge=min_edge,
        )

    live_sigs = _live_sigs(orders, symbol=symbol, default_sl=sl)
    # Bar-timestamp set (multi-book same bar counts once for identity of “decision bars”).
    free_ts = {int(s.ts_ms) for s in free_sigs}
    live_ts = {int(s.ts_ms) for s in live_sigs}
    # Full entry count including concurrent books.
    free_keys = {
        (int(s.ts_ms), int((s.meta or {}).get("book_idx") or 0), int(s.side))
        for s in free_sigs
    }
    live_keys = {
        (
            int(s.ts_ms),
            int((s.meta or {}).get("book_idx") or 0),
            1 if s.side == Side.LONG else -1,
        )
        for s in live_sigs
    }
    entry_cmp = {
        "n_live_orders": len(live_sigs),
        "n_bt_signals": len(free_sigs),
        "n_live_entry_bars": len(live_ts),
        "n_bt_entry_bars": len(free_ts),
        "n_live_entries": len(live_ts),  # backward compat → unique bars
        "n_bt_entries": len(free_ts),
        "intersection": len(live_ts & free_ts),
        "live_only_n": len(live_ts - free_ts),
        "bt_only_n": len(free_ts - live_ts),
        "order_intersection": len(live_keys & free_keys),
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
        log,
        f"entries live={entry_cmp['n_live_entries']} bt={entry_cmp['n_bt_entries']} "
        f"both={entry_cmp['intersection']} live_only={entry_cmp['live_only_n']} "
        f"bt_only={entry_cmp['bt_only_n']}",
    )

    win0 = pd.Timestamp(live_start_ms, unit="ms", tz="UTC") - pd.Timedelta(hours=12)
    win1 = pd.Timestamp(pad_end_ms, unit="ms", tz="UTC")
    window = ohlcv.loc[(ohlcv.index >= win0) & (ohlcv.index <= win1)].copy()
    touch_tf = touch_timeframe(timeframe, symbol)
    touch_full = load_ohlcv(symbol, touch_tf)
    dec_ms = int(TF_MS[timeframe])
    touch_end = window.index[-1] + pd.Timedelta(milliseconds=dec_ms) - pd.Timedelta(
        milliseconds=1
    )
    touch = touch_full.loc[
        (touch_full.index >= window.index[0]) & (touch_full.index <= touch_end)
    ]
    funding = load_funding(symbol)
    funding_ts = (funding.index.asi8 // 1_000_000).astype(np.int64)
    funding_rt = funding.to_numpy(dtype=float)

    meta_base = {
        "evidence_class": "LIVE_VS_BT_DISPLAY_ONLY",
        "account": account,
        "label": label,
        "ledger_key": key,
        "pack": pack_name,
        "promotion_allowed": False,
    }

    live_bundle = _run_bt(
        window,
        live_sigs,
        symbol=symbol,
        timeframe=timeframe,
        strategy_id=f"{account}_{label}_live_forced",
        strategy_meta={**meta_base, "arm": "live_orders_forced"},
        sl=sl,
        k_side=k_side,
        touch=touch,
        touch_tf=touch_tf,
        funding_ts=funding_ts,
        funding_rt=funding_rt,
        max_hold_cap=max_hold_cap,
    )
    free_bundle = _run_bt(
        window,
        free_sigs,
        symbol=symbol,
        timeframe=timeframe,
        strategy_id=f"{account}_{label}_free_bt",
        strategy_meta={**meta_base, "arm": "free_pack_model"},
        sl=sl,
        k_side=k_side,
        touch=touch,
        touch_tf=touch_tf,
        funding_ts=funding_ts,
        funding_rt=funding_rt,
        max_hold_cap=max_hold_cap,
    )

    live_m = _metrics_blob(live_bundle)
    free_m = _metrics_blob(free_bundle)
    report = {
        "evidence_class": "LIVE_VS_BT_DISPLAY_ONLY",
        "promotion_allowed": False,
        "account": account,
        "label": label,
        "symbol": symbol,
        "timeframe": timeframe,
        "live_orders": len(orders),
        "window": [
            datetime.fromtimestamp(live_start_ms / 1000, tz=timezone.utc).isoformat(),
            datetime.fromtimestamp(live_end_ms / 1000, tz=timezone.utc).isoformat(),
        ],
        "live_metrics": live_m,
        "backtest_metrics": free_m,
        "entry_comparison": entry_cmp,
        "signal_stats_free": free_stats,
        "elapsed_sec": round(time.perf_counter() - t0, 1),
        "created_utc": datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ"),
    }
    (out_dir / "metrics_latest.json").write_text(
        json.dumps(report, indent=2, default=str), encoding="utf-8"
    )
    _log(
        log,
        f"LIVE n={live_m['n_trades']} pf={live_m['profit_factor_raw']:.4f} "
        f"wr={live_m['win_rate']:.3f} pnl={live_m['net_pnl']:.4f}",
    )
    _log(
        log,
        f"BT   n={free_m['n_trades']} pf={free_m['profit_factor_raw']:.4f} "
        f"wr={free_m['win_rate']:.3f} pnl={free_m['net_pnl']:.4f}",
    )

    if plot and os.environ.get("TRADESIM_NO_PLOT", "").strip() not in ("1", "true", "TRUE"):
        plot_ohlcv = ohlcv.loc[
            (index_to_ms(ohlcv.index) >= live_start_ms - 12 * 3_600_000)
            & (index_to_ms(ohlcv.index) <= min(pad_end_ms, int(index_to_ms(ohlcv.index)[-1])))
        ].copy()
        bars = ohlcv_to_bar_series(plot_ohlcv, symbol=symbol, timeframe=timeframe)
        title_l = (
            f"{account} {label} LIVE forced | {symbol} {timeframe} | "
            f"n={live_m['n_trades']} PF={live_m['profit_factor_raw']:.2f}"
        )
        title_b = (
            f"{account} {label} FREE BT | {symbol} {timeframe} | "
            f"n={free_m['n_trades']} PF={free_m['profit_factor_raw']:.2f}"
        )
        _log(log, "finplot LIVE …")
        plot_backtest(
            bars,
            live_bundle.result,
            title=title_l,
            metrics=live_bundle.metrics,
            strategy_meta={"name": f"{account}_{label}_live", **meta_base},
            trade_style="lines",
            trade_labels="none",
            max_zone_trades=0,
            show=True,
            show_metrics_window=True,
        )
        _log(log, "finplot FREE BT …")
        plot_backtest(
            bars,
            free_bundle.result,
            title=title_b,
            metrics=free_bundle.metrics,
            strategy_meta={"name": f"{account}_{label}_bt", **meta_base},
            trade_style="lines",
            trade_labels="none",
            max_zone_trades=0,
            show=True,
            show_metrics_window=True,
        )
    return report


def main() -> int:
    conf = run_conformance_check()
    if conf.get("passed") is False:
        raise RuntimeError("conformance failed")
    if "botsgeneral" not in str(__import__("tradesim").__file__).lower():
        raise RuntimeError("tradesim not botsgeneral")
    if not LEDGERS.is_file():
        raise FileNotFoundError(LEDGERS)
    all_ledgers = json.loads(LEDGERS.read_text(encoding="utf-8"))
    plot = "--no-plot" not in sys.argv
    only = [a for a in sys.argv[1:] if not a.startswith("-")]
    bots = BOTS
    if only:
        bots = [b for b in BOTS if b["account"] in only or b["label"] in only]
    summary = []
    for bot in bots:
        try:
            rep = process_bot(bot, all_ledgers, plot=plot)
            summary.append(rep)
        except Exception as exc:  # noqa: BLE001
            err = {
                "account": bot["account"],
                "label": bot["label"],
                "error": f"{type(exc).__name__}: {exc}",
            }
            summary.append(err)
            print("FAIL", err, flush=True)
    out = OUT_ROOT / "summary_latest.json"
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(summary, indent=2, default=str), encoding="utf-8")
    print("WROTE", out)
    # compact table
    print("\n=== SUMMARY ===")
    for r in summary:
        if r.get("error"):
            print(r.get("account"), r.get("label"), "ERR", r["error"])
            continue
        lm, bm = r["live_metrics"], r["backtest_metrics"]
        print(
            f"{r['account']:12s} {r['label']:22s} {r['symbol']:8s} "
            f"LIVE n={lm['n_trades']:3d} PF={lm['profit_factor_raw']:>7.3f} "
            f"WR={lm['win_rate']*100:5.1f}% pnl={lm['net_pnl']:>8.3f} | "
            f"BT n={bm['n_trades']:3d} PF={bm['profit_factor_raw']:>7.3f} "
            f"WR={bm['win_rate']*100:5.1f}% pnl={bm['net_pnl']:>8.3f} | "
            f"entries both={r['entry_comparison']['intersection']}/"
            f"{r['entry_comparison']['n_live_entries']}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
