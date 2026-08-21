"""ETH multitrade p75 forward-lockbox metrics + optional Finplot.

Uses the **frozen live pack** ``structure_v1_ethusdt_multitrade_p75_v1``
(model.joblib + strategy multitrade knobs with strength_quantile=0.75).

**Sealed by default (D-038 / D-036):** bars on/after FORWARD_LOCKBOX_START require
``--i-accept-lockbox-contamination``. Interactive Finplot also requires
``--i-accept-finplot-lockbox`` and ``--show``. Authorized peeks append peek_log
as ``LOCKBOX_OPENED_CONTAMINATED``. Numbers are **diagnostic only** — not a
promotion / scale gate. Prefer outer-fold settle for quotable evidence.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

# Default sealed: no interactive Finplot until dual accept.
os.environ.setdefault("TRADESIM_NO_PLOT", "1")

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))
_leak = Path(r"C:\projects\botsgeneral\packages\leakage\src")
if _leak.is_dir() and str(_leak) not in sys.path:
    sys.path.insert(0, str(_leak))

import joblib
import numpy as np
import pandas as pd

from tradesim.ensure_source import prefer_botsgeneral_tradesim

prefer_botsgeneral_tradesim()

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
from llm2.evidence.lockbox_guard import (  # noqa: E402
    add_lockbox_guard_args,
    require_lockbox_access,
    seal_finplot_unless_authorized,
)
from llm2.experiments.eth_multitrade_nested import (  # noqa: E402
    MIN_EDGE,
    build_multitrade_signals,
)
from llm2.features.registry import build_space  # noqa: E402
from llm2.gates.evidence import leverage_from_stop, research_costs_baseline  # noqa: E402
from llm2.hunt.targets import proxy_side, target_family  # noqa: E402
from llm2.live.multitrade import MEAN_LOOKBACK, parse_multitrade_config  # noqa: E402
from llm2.paths import ARTIFACTS, FORWARD_LOCKBOX_START, TF_MS, touch_timeframe  # noqa: E402
from llm2.research_policy import PolicyError  # noqa: E402
from llm2.validation.folds import index_to_ms  # noqa: E402

SPACE = "structure_v1"
PACK = ARTIFACTS / "live_packs" / "structure_v1_ethusdt_multitrade_p75_v1"
OUT_DIR = ARTIFACTS / "reports" / "structure_v1_eth_multitrade_p75_lockbox"
STORE = Path(r"D:\projectsdata\backtests\tradesim_runs.sqlite")
DEFAULT_TRADE_CAP = 200
EXPERIMENT_ID = "structure_v1_eth_multitrade_p75_lockbox"
EVIDENCE_CLASS = "LOCKBOX_OPENED_CONTAMINATED"


def _json_default(obj: object) -> object:
    if isinstance(obj, float) and (np.isnan(obj) or np.isinf(obj)):
        return None
    if isinstance(obj, (np.floating,)):
        v = float(obj)
        if np.isnan(v) or np.isinf(v):
            return None
        return v
    if isinstance(obj, (np.integer,)):
        return int(obj)
    raise TypeError(f"Object of type {type(obj)!r} is not JSON serializable")


def _as_float(v: object, default: float = float("nan")) -> float:
    if v is None:
        return default
    if isinstance(v, (int, float, np.floating, np.integer)):
        return float(v)
    # Nested tradesim reports (SharpeReport, etc.)
    for attr in ("annualized", "raw", "value", "ratio", "sharpe", "sortino"):
        if hasattr(v, attr):
            try:
                return float(getattr(v, attr))
            except (TypeError, ValueError):
                continue
    try:
        return float(v)  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return default


def _metrics_blob(m: object, *, n_trades_lockbox: int | None = None) -> dict:
    def g(name: str, default=None):
        return getattr(m, name, default)

    as_dict = {}
    if hasattr(m, "as_dict") and callable(m.as_dict):
        try:
            as_dict = dict(m.as_dict() or {})
        except Exception:  # noqa: BLE001
            as_dict = {}

    out = {
        "n_trades": int(n_trades_lockbox if n_trades_lockbox is not None else g("n_trades", 0) or 0),
        "n_trades_engine": int(g("n_trades", 0) or 0),
        "net_pnl": _as_float(g("net_pnl", as_dict.get("net_pnl"))),
        "profit_factor": _as_float(g("profit_factor", as_dict.get("profit_factor"))),
        "win_rate": _as_float(g("win_rate", as_dict.get("win_rate"))),
        "expectancy": _as_float(g("expectancy", as_dict.get("expectancy"))),
        "expectancy_return_units": _as_float(
            g("expectancy_return_units", as_dict.get("expectancy_return_units"))
        ),
        "sharpe_daily_raw": _as_float(
            as_dict.get("sharpe_daily_raw", as_dict.get("sharpe_raw"))
        ),
        "sharpe_annualized": _as_float(
            as_dict.get("sharpe_annualized", as_dict.get("sharpe_ann"))
        ),
        "sortino_annualized": _as_float(
            as_dict.get("sortino_annualized", as_dict.get("sortino_ann"))
        ),
        "max_drawdown": _as_float(g("max_drawdown", as_dict.get("max_drawdown"))),
        "total_fees": _as_float(g("total_fees", as_dict.get("total_fees"))),
        "total_funding": _as_float(g("total_funding", as_dict.get("total_funding"))),
        "n_longs": int(g("n_longs", as_dict.get("n_longs", 0)) or 0),
        "n_shorts": int(g("n_shorts", as_dict.get("n_shorts", 0)) or 0),
        "avg_trade_pnl": _as_float(g("avg_trade_pnl", as_dict.get("avg_trade_pnl"))),
    }
    return out


def _trade_pnl(t: object) -> float:
    for name in ("realized_pnl", "net_pnl", "pnl"):
        if hasattr(t, name):
            try:
                return float(getattr(t, name) or 0.0)
            except (TypeError, ValueError):
                continue
    return 0.0


def _trade_side(t: object) -> int:
    s = getattr(t, "side", 0)
    return int(getattr(s, "value", s) or 0)


def _pooled_trade_stats(trades: list) -> dict:
    if not trades:
        return {
            "n_trades": 0,
            "net_pnl": 0.0,
            "profit_factor": float("nan"),
            "win_rate": float("nan"),
            "expectancy": float("nan"),
            "expectancy_return_units": float("nan"),
            "n_longs": 0,
            "n_shorts": 0,
        }
    pnls = np.asarray([_trade_pnl(t) for t in trades], dtype=float)
    rus = np.asarray(
        [float(getattr(t, "return_units", float("nan")) or float("nan")) for t in trades],
        dtype=float,
    )
    sides = [_trade_side(t) for t in trades]
    gp = float(pnls[pnls > 0].sum())
    gl = float((-pnls[pnls < 0]).sum())
    if gl <= 0:
        pf = float("inf") if gp > 0 else float("nan")
    else:
        pf = gp / gl
    wins = int((pnls > 0).sum())
    rus_ok = rus[np.isfinite(rus)]
    return {
        "n_trades": int(len(trades)),
        "net_pnl": float(pnls.sum()),
        "profit_factor": pf,
        "win_rate": float(wins / len(trades)) if trades else float("nan"),
        "expectancy": float(pnls.mean()) if trades else float("nan"),
        "expectancy_return_units": float(rus_ok.mean()) if rus_ok.size else float("nan"),
        "n_longs": int(sum(1 for s in sides if s > 0)),
        "n_shorts": int(sum(1 for s in sides if s < 0)),
        "total_fees": float(sum(float(getattr(t, "fees", 0.0) or 0.0) for t in trades)),
        "total_funding": float(
            sum(float(getattr(t, "funding", 0.0) or 0.0) for t in trades)
        ),
    }


def run_lockbox(
    *,
    start: str,
    trade_cap: int,
    store: bool,
    show: bool,
) -> dict:
    if not (PACK / "model.joblib").is_file():
        raise SystemExit(f"missing pack model: {PACK}")
    strategy = json.loads((PACK / "strategy.json").read_text(encoding="utf-8"))
    mt = parse_multitrade_config(strategy)
    if not mt:
        raise SystemExit("pack is not multitrade")
    cfg = dict(mt)
    cfg.setdefault("bar_ms", 3_600_000)

    blob = joblib.load(PACK / "model.joblib")
    model = blob["model"]
    cols = list(blob.get("feature_columns") or strategy.get("feature_columns") or [])
    symbol = str(strategy["symbol"]).upper()
    timeframe = str(strategy["timeframe"])
    target = str(strategy["target"])
    family = target_family(target)
    sl = float(cfg["base_sl"])
    lookback = int(cfg.get("mean_lookback") or MEAN_LOOKBACK)

    ohlcv = load_ohlcv(symbol, timeframe)
    start_ts = pd.Timestamp(start, tz="UTC")
    if ohlcv.index.tz is None:
        ohlcv.index = ohlcv.index.tz_localize("UTC")
    if int((ohlcv.index >= start_ts).sum()) < 50:
        raise RuntimeError(
            f"insufficient lockbox bars after {start} (data end {ohlcv.index.max()})"
        )

    feats = build_space(ohlcv.copy(), SPACE, symbol=symbol, timeframe=timeframe)
    feats = feats.reindex(columns=cols)
    if "last_retrace_pct" in feats.columns:
        feats["last_retrace_pct"] = feats["last_retrace_pct"].fillna(0.0)
    for c in feats.columns:
        if c.startswith("last_retrace_pct_"):
            feats[c] = feats[c].fillna(0.0)
    aligned = feats.dropna()

    # Warm |mean| history so the p75 gate is defined at lockbox open (books empty).
    warm_start = start_ts - pd.Timedelta(hours=int(lookback) + 48)
    warm_mask = (aligned.index >= warm_start) & (aligned.index < start_ts)
    lock_mask = aligned.index >= start_ts
    if int(lock_mask.sum()) < 50:
        raise RuntimeError(f"insufficient aligned lockbox bars after {start}")

    seed_strength: list[float] = []
    if int(warm_mask.sum()) > 0:
        Xw = aligned.loc[warm_mask].to_numpy(dtype=float)
        pred_w = model.predict(Xw)
        mean_w = pred_w.mean if pred_w.mean is not None else np.zeros(len(Xw))
        mean_w = np.asarray(mean_w, dtype=float).reshape(-1)
        side_w = proxy_side(mean_w, family)
        for s, m in zip(side_w, mean_w, strict=True):
            if int(s) == 0 or not np.isfinite(m) or abs(float(m)) < MIN_EDGE:
                continue
            seed_strength.append(abs(float(m)))

    Xl = aligned.loc[lock_mask].to_numpy(dtype=float)
    ts_idx = aligned.index[lock_mask]
    ts_ms = index_to_ms(ts_idx)
    pred = model.predict(Xl)
    mean = pred.mean if pred.mean is not None else np.zeros(len(ts_idx))
    mean = np.asarray(mean, dtype=float).reshape(-1)
    side = proxy_side(mean, family)
    close_oos = ohlcv["close"].reindex(ts_idx).to_numpy(dtype=float)
    signals, sig_stats = build_multitrade_signals(
        ts_ms,
        side,
        mean,
        cfg=cfg,
        close=close_oos,
        seed_strength_hist=seed_strength[-lookback:] if seed_strength else None,
    )

    end_ts = ts_idx[-1]
    pad_start = start_ts - pd.Timedelta(days=14)
    window = ohlcv.loc[(ohlcv.index >= pad_start) & (ohlcv.index <= end_ts)].copy()

    touch_tf = touch_timeframe(timeframe, symbol)
    touch = load_ohlcv(symbol, touch_tf)
    dec_ms = int(TF_MS[timeframe])
    touch_end = end_ts + pd.Timedelta(milliseconds=dec_ms) - pd.Timedelta(milliseconds=1)
    touch_win = touch.loc[(touch.index >= pad_start) & (touch.index <= touch_end)]
    touch_ms = int(TF_MS[touch_tf])
    need = dec_ms // touch_ms
    last_dec = int(window["ts_ms"].iloc[-1]) if "ts_ms" in window.columns else int(
        window.index[-1].value // 1_000_000
    )
    t_ts = (
        touch_win["ts_ms"].to_numpy(dtype=np.int64)
        if "ts_ms" in touch_win.columns
        else (touch_win.index.asi8 // 1_000_000).astype(np.int64)
    )
    lo = int(np.searchsorted(t_ts, last_dec, side="left"))
    hi = int(np.searchsorted(t_ts, last_dec + dec_ms, side="left"))
    if hi - lo < need and len(window) > 1:
        window = window.iloc[:-1]
        end_ts = window.index[-1]
        touch_end = end_ts + pd.Timedelta(milliseconds=dec_ms) - pd.Timedelta(milliseconds=1)
        touch_win = touch.loc[(touch.index >= pad_start) & (touch.index <= touch_end)]

    funding = load_funding(symbol)
    if funding.empty:
        raise RuntimeError("no funding — refusing lockbox without live cost model")
    funding_ts = (funding.index.asi8 // 1_000_000).astype(np.int64)
    funding_rt = funding.to_numpy(dtype=float)
    w_ts = index_to_ms(window.index)
    fmask = (funding_ts >= int(w_ts[0])) & (funding_ts <= int(w_ts[-1]))

    lev = float(leverage_from_stop(sl))
    try:
        instrument = research_instrument(symbol)
    except Exception:  # noqa: BLE001
        instrument = None

    k = int(cfg["max_positions_per_side"])
    version_id = str(strategy.get("version_id") or "eth_multitrade_p75_v1")
    bundle = run_strategy_backtest(
        window,
        signals,
        symbol=symbol,
        timeframe=timeframe,
        strategy_id=f"llm2-{version_id}-lockbox",
        touch_ohlcv=touch_win,
        touch_timeframe=touch_tf,
        costs=research_costs_baseline(),
        margin=research_margin(leverage=lev),
        sizing=research_sizing(),
        sim=research_sim_hedge(
            max_hold_bars=int(cfg["hold_addon"]),
            decision_timeframe=timeframe,
            max_positions_per_side=k,
            max_positions_per_symbol=k * 2,
        ),
        instrument=instrument,
        funding_ts_ms=funding_ts[fmask],
        funding_rate=funding_rt[fmask],
        strategy_meta={
            "name": f"{symbol} multitrade p75 LOCKBOX",
            "version_id": version_id,
            "generation_id": EXPERIMENT_ID,
            "symbol": symbol,
            "timeframe": timeframe,
            "lockbox_start": start,
            "strength_quantile": float(cfg.get("strength_quantile", 0.75)),
            "clarity": cfg.get("clarity"),
            "clarity_scope": cfg.get("clarity_scope"),
            "fib_ext": cfg.get("fib_ext"),
            "hold_addon": cfg.get("hold_addon"),
            "k_per_side": k,
            "leverage": lev,
            "sizing": "MIN_EXCHANGE",
            "evidence_class": EVIDENCE_CLASS,
            "promotion": "FORBIDDEN_from_lockbox",
            "pack": str(PACK.relative_to(_ROOT)).replace("\\", "/"),
            "signal_stats": sig_stats,
            "seed_strength_n": len(seed_strength[-lookback:] if seed_strength else []),
            "note": (
                "Diagnostic lockbox only (D-036/D-038). Do not retune knobs or "
                "promote capital from these numbers."
            ),
        },
        plot=False,
        print_headline=True,
        store_path=str(STORE) if store else None,
    )

    start_ms = int(start_ts.value // 1_000_000)
    trades_all = list(bundle.result.trades)
    trades_lb = [
        t for t in trades_all if int(getattr(t, "entry_ts_ms", 0) or 0) >= start_ms
    ]
    pooled = _pooled_trade_stats(trades_lb)
    engine_m = _metrics_blob(bundle.metrics)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    trades_rows = []
    for t in sorted(trades_lb, key=lambda x: int(getattr(x, "entry_ts_ms", 0) or 0)):
        trades_rows.append(
            {
                "entry_ts_ms": int(getattr(t, "entry_ts_ms", 0) or 0),
                "exit_ts_ms": int(getattr(t, "exit_ts_ms", 0) or 0),
                "side": _trade_side(t),
                "realized_pnl": _trade_pnl(t),
                "return_units": float(getattr(t, "return_units", float("nan"))),
                "tag": str(getattr(t, "tag", "") or ""),
                "exit_reason": str(getattr(t, "exit_reason", "") or ""),
            }
        )
    trades_csv = OUT_DIR / "lockbox_trades.csv"
    pd.DataFrame(trades_rows).to_csv(trades_csv, index=False)

    try:
        trades_rel = str(trades_csv.relative_to(_ROOT)).replace("\\", "/")
    except ValueError:
        trades_rel = str(trades_csv)
    summary = {
        "experiment_id": EXPERIMENT_ID,
        "evidence_class": EVIDENCE_CLASS,
        "version_id": version_id,
        "pack": str(PACK),
        "symbol": symbol,
        "timeframe": timeframe,
        "lockbox_start": start,
        "data_end": str(end_ts),
        "generated_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "n_signals": int(len(signals)),
        "signal_stats": sig_stats,
        "seed_strength_n": int(len(seed_strength[-lookback:] if seed_strength else [])),
        "multitrade": {
            "strength_quantile": float(cfg.get("strength_quantile", 0.75)),
            "clarity": cfg.get("clarity"),
            "clarity_scope": cfg.get("clarity_scope"),
            "fib_ext": cfg.get("fib_ext"),
            "hold_addon": cfg.get("hold_addon"),
            "max_positions_per_side": k,
            "base_tp": cfg.get("base_tp"),
            "base_sl": cfg.get("base_sl"),
            "base_hold": cfg.get("base_hold"),
        },
        "engine_metrics_full_sim": engine_m,
        "lockbox_entry_trades": pooled,
        "finplot": bool(show),
        "trades_csv": trades_rel,
        "note": (
            "LOCKBOX_OPENED_CONTAMINATED diagnostic. Not a promotion or scale gate. "
            "Quote outer-fold structure_v1_eth_multitrade_strength_p75_001 for history; "
            "use live/micro recon for post-deploy truth. Do not retune from this window."
        ),
    }

    # Persist before Finplot so a GUI block still leaves metrics on disk.
    stamp_now = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(summary, indent=2, default=_json_default) + "\n"
    (OUT_DIR / f"metrics_{stamp_now}.json").write_text(payload, encoding="utf-8")
    (OUT_DIR / "metrics_latest.json").write_text(payload, encoding="utf-8")
    (
        ARTIFACTS / "reports" / "structure_v1_eth_multitrade_p75_lockbox_latest.json"
    ).write_text(payload, encoding="utf-8")
    print(payload, flush=True)
    print(f"wrote {OUT_DIR / 'metrics_latest.json'}", flush=True)

    if show:
        plot_ohlcv = window.loc[window.index >= start_ts]
        bars = ohlcv_to_bar_series(plot_ohlcv, symbol=symbol, timeframe=timeframe)
        title = (
            f"{symbol} multitrade p75 LOCKBOX | q={cfg.get('strength_quantile')} "
            f"K={k} scope={cfg.get('clarity_scope')} | "
            f"[{start_ts.date()} -> {end_ts.date()}] "
            f"n={pooled['n_trades']} PF={float(pooled['profit_factor']):.2f} "
            f"PnL={float(pooled['net_pnl']):.2f} | DIAGNOSTIC ONLY"
        )
        plot_backtest(
            bars,
            bundle.result,
            title=title,
            metrics=bundle.metrics,
            trade_style="boxes",
            max_zone_trades=int(trade_cap),
            strategy_meta={
                "name": f"{version_id} lockbox",
                "evidence_class": EVIDENCE_CLASS,
                "version_id": version_id,
                "strength_quantile": float(cfg.get("strength_quantile", 0.75)),
                "k_per_side": k,
                "clarity_scope": cfg.get("clarity_scope"),
                "fib_ext": cfg.get("fib_ext"),
                "hold_addon": cfg.get("hold_addon"),
                "leverage": lev,
                "sizing": "MIN_EXCHANGE",
                "lockbox_start": start,
                "lockbox_n_trades": pooled["n_trades"],
                "lockbox_pf": pooled["profit_factor"],
                "lockbox_net_pnl": pooled["net_pnl"],
                "promotion": "FORBIDDEN_from_lockbox",
                "note": (
                    f"Green/red boxes = hold win/loss (last {trade_cap} zones). "
                    "Contaminated diagnostic — not for promotion."
                ),
            },
            show=True,
            show_metrics_window=True,
        )

    return summary


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description=(
            "ETH multitrade p75 lockbox report. Requires "
            "--i-accept-lockbox-contamination; Finplot needs --show + "
            "--i-accept-finplot-lockbox."
        )
    )
    ap.add_argument("--start", default=FORWARD_LOCKBOX_START)
    ap.add_argument("--trade-cap", type=int, default=DEFAULT_TRADE_CAP)
    ap.add_argument("--store", action="store_true", default=False)
    ap.add_argument("--show", action="store_true", help="Open Finplot (dual accept).")
    ap.add_argument("--no-show", action="store_true", help="Report-only (default).")
    add_lockbox_guard_args(ap)
    args = ap.parse_args(argv)

    open_finplot = bool(args.show) and not bool(args.no_show)
    try:
        require_lockbox_access(
            experiment_id=EXPERIMENT_ID,
            window_start=str(args.start),
            window_end="warehouse_end",
            purpose="finplot_lockbox_open" if open_finplot else "lockbox_report_only",
            symbols=["ETHUSDT"],
            arms="eth_multitrade_p75_v1",
            n_arms=1,
            accepted_contamination=bool(args.i_accept_lockbox_contamination),
            open_finplot=open_finplot,
            accepted_finplot=bool(args.i_accept_finplot_lockbox),
            notes="scripts/plot_eth_multitrade_p75_lockbox.py diagnostic only",
        )
    except PolicyError as exc:
        print(f"REFUSED: {exc}", flush=True)
        return 2

    show = seal_finplot_unless_authorized(
        open_finplot=open_finplot,
        accepted_finplot=bool(args.i_accept_finplot_lockbox),
    )

    stamp = run_conformance_check(quiet=True)
    if not stamp.get("passed"):
        print("tradesim conformance not green; refusing lockbox plot", flush=True)
        return 1

    summary = run_lockbox(
        start=str(args.start),
        trade_cap=int(args.trade_cap),
        store=bool(args.store),
        show=show,
    )
    print(
        f"done finplot={summary.get('finplot')} n={summary.get('lockbox_entry_trades', {}).get('n_trades')}",
        flush=True,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
