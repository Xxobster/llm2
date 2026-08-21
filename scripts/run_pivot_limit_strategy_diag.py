"""Diagnostic: calibrated pivot model → limit orders at predicted levels.

Economics (preregistered for this diagnostic only — not optimized on OOS):
- Decision: 15m, rare labels (H=4 bars, ATR min 2.0)
- Act when calibrated P(any) >= train-fold 75th percentile of calibrated scores
- Side: P(high|event) >= 0.5 → short (fade high); else long (buy low)
- Limit entry at close * (1 + predicted level return), clamped to [±0.15%, ±3%]
- TP × SL grid: {1,2,3,5}% × {1,2,3,5}% (diagnostic matrix — not fold-selected OOS)
- max_hold = horizon_bars + 2
- Binance research candles; tradesim research costs; pre-lockbox only
- RESEARCH_ONLY — not a live authorization
"""

from __future__ import annotations

import json
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from tradesim.ensure_source import prefer_botsgeneral_tradesim

prefer_botsgeneral_tradesim()

from tradesim import (  # noqa: E402
    Side,
    Signal,
    research_instrument,
    research_margin,
    research_sizing,
    research_sim_limit_entry,
)
from tradesim.contracts import EntryOrder  # noqa: E402

from llm2.backtest.run import run_strategy_backtest  # noqa: E402
from llm2.data.loader import load_ohlcv  # noqa: E402
from llm2.data.macro import load_funding  # noqa: E402
from llm2.gates.evidence import leverage_from_stop, research_costs_baseline  # noqa: E402
from llm2.paths import ARTIFACTS, FORWARD_LOCKBOX_START, TF_MS, touch_timeframe  # noqa: E402
from llm2.pivot.labels.config import PivotLabelConfig  # noqa: E402
from llm2.pivot.train.calibration import apply_calibrator, fit_binary_calibrator  # noqa: E402
from llm2.pivot.train.multihead import _fit_predict_binary, _fit_predict_reg  # noqa: E402
from llm2.pivot.train.multihead import expected_calibration_error  # noqa: E402
from llm2.pivot.train.samples import build_samples  # noqa: E402
from llm2.pivot.train.walk_forward import ModelSpec  # noqa: E402
from llm2.registry.ledger import append_ledger  # noqa: E402
from llm2.validation.folds import build_outer_folds, index_to_ms  # noqa: E402

SYMBOLS = ("BTCUSDT", "ETHUSDT", "SOLUSDT")
TF = "15m"
H_BARS = 4
ATR_MIN = 2.0
PACK = "price_vol_mom"
TP_ARMS = (0.01, 0.02, 0.03, 0.05)
SL_ARMS = (0.01, 0.02, 0.03, 0.05)
MAX_ROWS = 120_000


def _pct_tag(x: float) -> str:
    return f"{int(round(x * 100)):02d}"


def _arm_key(tp: float, sl: float) -> str:
    return f"tp{_pct_tag(tp)}_sl{_pct_tag(sl)}"


def _lgbm_cls() -> ModelSpec:
    import lightgbm as lgb

    return ModelSpec(
        "lgbm_m",
        lambda: lgb.LGBMClassifier(
            n_estimators=200,
            num_leaves=31,
            learning_rate=0.05,
            class_weight="balanced",
            verbosity=-1,
            random_state=20260810,
        ),
    )


def _label_cfg() -> PivotLabelConfig:
    return PivotLabelConfig(
        timeframe=TF,
        left_bars=3,
        right_bars=3,
        confirm_bars=3,
        min_left_prominence_atr=ATR_MIN,
        min_right_reversal_atr=ATR_MIN,
        min_reversal_pct=0.0015,
        atr_period=14,
        label_family="fractal_strat_diag",
        suppress_neighbor_bars=3,
    )


def _metrics(bundle) -> dict:
    m = bundle.metrics
    return {
        "n_trades": int(m.n_trades),
        "profit_factor": float(m.profit_factor),
        "net_pnl": float(m.net_pnl),
        "win_rate": float(getattr(m, "win_rate", float("nan"))),
        "expectancy": float(getattr(m, "expectancy", float("nan"))),
        "n_liquidations": int(getattr(m, "n_liquidations", 0) or 0),
    }


def _bt(symbol: str, ohlcv: pd.DataFrame, signals: list[Signal], *, sl: float, tag: str):
    if len(signals) < 20:
        return {"status": "TOO_FEW", "n_signals": len(signals)}
    touch_tf = touch_timeframe(TF, symbol)
    lock = pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC")
    touch = load_ohlcv(symbol, touch_tf)
    touch = touch.loc[touch.index < lock]
    funding = load_funding(symbol)
    funding = funding[funding.index < lock]
    f_ts = (funding.index.asi8 // 1_000_000).astype(np.int64)
    f_rt = funding.to_numpy(dtype=float)
    bar_ms = index_to_ms(ohlcv.index)
    sig_ts = np.array([s.ts_ms for s in signals], dtype=np.int64)
    i0 = int(np.searchsorted(bar_ms, int(sig_ts.min()), side="left"))
    i1 = int(np.searchsorted(bar_ms, int(sig_ts.max()), side="right"))
    pad = 80
    window = ohlcv.iloc[max(0, i0 - pad) : min(len(ohlcv), i1 + pad)]
    w_ts = index_to_ms(window.index)
    fmask = (f_ts >= int(w_ts[0])) & (f_ts <= int(w_ts[-1]))
    end, start = window.index[-1], window.index[0]
    dec_ms = int(TF_MS[TF])
    touch_end = end + pd.Timedelta(milliseconds=dec_ms) - pd.Timedelta(milliseconds=1)
    touch_win = touch.loc[(touch.index >= start) & (touch.index <= touch_end)]
    lev = float(leverage_from_stop(sl))
    try:
        bundle = run_strategy_backtest(
            window,
            signals,
            symbol=symbol,
            timeframe=TF,
            strategy_id=f"pivot_lim_{symbol.lower()}_{tag}",
            touch_ohlcv=touch_win if len(touch_win) else None,
            touch_timeframe=touch_tf,
            costs=research_costs_baseline(),
            margin=research_margin(leverage=lev),
            sizing=research_sizing(),
            sim=research_sim_limit_entry(
                max_hold_bars=H_BARS + 2, decision_timeframe=TF
            ),
            instrument=research_instrument(symbol),
            funding_ts_ms=f_ts[fmask],
            funding_rate=f_rt[fmask],
            plot=False,
            print_headline=False,
            store_path=None,
        )
    except Exception as exc:  # noqa: BLE001
        return {"status": "BT_ERROR", "error": str(exc)[:400], "n_signals": len(signals)}
    return {"status": "RAN", "metrics": _metrics(bundle), "n_signals": len(signals)}


@dataclass(frozen=True)
class _Decision:
    ts_ms: int
    side: Side
    limit_price: float
    p_any: float
    p_high: float
    level_ret: float
    thr: float


def _collect_decisions(symbol: str) -> tuple[pd.DataFrame, list[_Decision], dict]:
    cfg = _label_cfg()
    ms = _lgbm_cls()
    print(f"SAMPLES {symbol} …", flush=True)
    samp = build_samples(
        symbol=symbol,
        timeframe=TF,
        feature_pack=PACK,
        label_cfg=cfg,
        horizon_bars=H_BARS,
        max_rows=MAX_ROWS,
    )
    X, ts = samp["X"], samp["ts_ms"]
    y_any, y_high = samp["y_any"], samp["y_high_given"]
    y_level = samp["y_level_ret"]
    ohlcv = load_ohlcv(symbol, TF)
    lock_ms = int(pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC").value // 1_000_000)
    ohlcv = ohlcv.loc[index_to_ms(ohlcv.index) < lock_ms].copy()
    if MAX_ROWS and len(ohlcv) > MAX_ROWS:
        ohlcv = ohlcv.iloc[-MAX_ROWS:].copy()
    ohlcv_ts = index_to_ms(ohlcv.index)
    close_map = dict(zip(ohlcv_ts.tolist(), ohlcv["close"].to_numpy(dtype=float).tolist()))
    closes = np.array([close_map.get(int(t), np.nan) for t in ts], dtype=float)

    purge = max(H_BARS + 6, 24)
    folds = build_outer_folds(ts, purge_bars=purge, embargo_bars=purge)

    decisions: list[_Decision] = []
    cal_diag = []
    for fold in folds:
        tr, te = fold.train_indices, fold.oos_indices
        if tr.size < 800 or te.size < 100:
            continue
        cut = int(tr.size * 0.8)
        tr_fit, tr_cal = tr[:cut], tr[cut:]
        if tr_cal.size < 100:
            tr_fit, tr_cal = tr, tr[-max(100, tr.size // 10) :]

        p_cal_raw = _fit_predict_binary(
            X[tr_fit], y_any[tr_fit], X[tr_cal], model_spec=ms, is_baserate=False
        )
        cal_any = fit_binary_calibrator(y_any[tr_cal], p_cal_raw, method="isotonic")
        p_te_raw = _fit_predict_binary(
            X[tr], y_any[tr], X[te], model_spec=ms, is_baserate=False
        )
        p_te = apply_calibrator(cal_any, p_te_raw)
        p_cal_cal = apply_calibrator(cal_any, p_cal_raw)
        cal_diag.append(
            {
                "fold": fold.fold_index,
                "ece_inner_raw": expected_calibration_error(y_any[tr_cal], p_cal_raw),
                "ece_inner_cal": expected_calibration_error(y_any[tr_cal], p_cal_cal),
                "ece_outer_cal": expected_calibration_error(y_any[te], p_te),
                "pr_note": "outer scores after inner-only calibrator",
            }
        )

        tr_ev = tr[y_high[tr] >= 0]
        p_high_te = np.full(te.size, 0.5)
        if tr_ev.size >= 80:
            p_high_all = _fit_predict_binary(
                X[tr_ev],
                y_high[tr_ev],
                X[te],
                model_spec=ms,
                is_baserate=False,
            )
            p_high_te = p_high_all
            tr_cal_ev = tr_cal[y_high[tr_cal] >= 0]
            if tr_cal_ev.size >= 40:
                p_hg_cal_raw = _fit_predict_binary(
                    X[tr_ev],
                    y_high[tr_ev],
                    X[tr_cal_ev],
                    model_spec=ms,
                    is_baserate=False,
                )
                cal_hg = fit_binary_calibrator(
                    y_high[tr_cal_ev], p_hg_cal_raw, method="isotonic"
                )
                p_high_te = apply_calibrator(cal_hg, p_high_all)

        tr_lv = tr[np.isfinite(y_level[tr])]
        level_te = np.zeros(te.size)
        if tr_lv.size >= 50:
            level_te = _fit_predict_reg(
                X[tr_lv],
                y_level[tr_lv],
                X[te],
                model_name="lgbm",
                is_baserate=False,
            )

        thr = float(np.nanpercentile(p_cal_cal, 75))
        thr = max(thr, 0.35)

        for j, i in enumerate(te):
            if p_te[j] < thr:
                continue
            c = float(closes[i])
            if not np.isfinite(c) or c <= 0:
                continue
            is_high = p_high_te[j] >= 0.5
            lr = float(level_te[j]) if np.isfinite(level_te[j]) else (
                0.005 if is_high else -0.005
            )
            if is_high:
                lr = float(np.clip(lr, 0.0015, 0.03))
                limit_px = c * (1.0 + lr)
                side = Side.SHORT
            else:
                lr = float(np.clip(lr, -0.03, -0.0015))
                limit_px = c * (1.0 + lr)
                side = Side.LONG
            decisions.append(
                _Decision(
                    ts_ms=int(ts[i]),
                    side=side,
                    limit_price=float(limit_px),
                    p_any=float(p_te[j]),
                    p_high=float(p_high_te[j]),
                    level_ret=lr,
                    thr=thr,
                )
            )

    meta = {
        "frac_any_label": samp["frac_any"],
        "n_rows": samp["n_rows"],
        "calibration_folds": cal_diag,
        "n_decisions": len(decisions),
    }
    return ohlcv, decisions, meta


def _signals_for_arm(
    decisions: list[_Decision], *, tp: float, sl: float, limit_entry: bool
) -> list[Signal]:
    out: list[Signal] = []
    for d in decisions:
        if limit_entry:
            out.append(
                Signal(
                    ts_ms=d.ts_ms,
                    side=d.side,
                    stop_offset=float(sl),
                    target_offset=float(tp),
                    max_hold_bars=H_BARS + 2,
                    entry_order=EntryOrder.LIMIT,
                    limit_price=float(d.limit_price),
                    tag="pivot_limit",
                    meta={
                        "p_any": d.p_any,
                        "p_high": d.p_high,
                        "level_ret": d.level_ret,
                        "thr": d.thr,
                    },
                )
            )
        else:
            out.append(
                Signal(
                    ts_ms=d.ts_ms,
                    side=d.side,
                    stop_offset=float(sl),
                    target_offset=float(tp),
                    max_hold_bars=H_BARS + 2,
                    tag="pivot_market",
                    meta={"p_any": d.p_any, "p_high": d.p_high},
                )
            )
    return out


def run_symbol(symbol: str) -> dict:
    ohlcv, decisions, meta = _collect_decisions(symbol)
    out = {
        "symbol": symbol,
        "frac_any_label": meta["frac_any_label"],
        "n_rows": meta["n_rows"],
        "n_decisions": meta["n_decisions"],
        "calibration_folds": meta["calibration_folds"],
        "limit_entry": {},
        "market_entry_control": {},
        "grid_summary": {"limit": [], "market": []},
    }
    n_dec = len(decisions)
    for tp in TP_ARMS:
        for sl in SL_ARMS:
            key = _arm_key(tp, sl)
            lim_sigs = _signals_for_arm(decisions, tp=tp, sl=sl, limit_entry=True)
            mkt_sigs = _signals_for_arm(decisions, tp=tp, sl=sl, limit_entry=False)
            print(
                f"  BT limit {key} n_sig={len(lim_sigs)} …",
                flush=True,
            )
            lim_res = _bt(symbol, ohlcv, lim_sigs, sl=sl, tag=f"lim_{key}")
            print(f"    {lim_res.get('status')} {_short_m(lim_res)}", flush=True)
            out["limit_entry"][key] = {
                **lim_res,
                "tp_pct": tp,
                "sl_pct": sl,
            }
            print(f"  BT market {key} n_sig={len(mkt_sigs)} …", flush=True)
            mkt_res = _bt(symbol, ohlcv, mkt_sigs, sl=sl, tag=f"mkt_{key}")
            print(f"    {mkt_res.get('status')} {_short_m(mkt_res)}", flush=True)
            out["market_entry_control"][key] = {
                **mkt_res,
                "tp_pct": tp,
                "sl_pct": sl,
            }
            out["grid_summary"]["limit"].append(
                _row_summary(key, tp, sl, n_dec, lim_res)
            )
            out["grid_summary"]["market"].append(
                _row_summary(key, tp, sl, n_dec, mkt_res)
            )
    return out


def _short_m(res: dict) -> str:
    if res.get("status") != "RAN":
        return str(res.get("error") or res.get("status"))
    m = res["metrics"]
    return (
        f"n={m['n_trades']} PF={m['profit_factor']:.3f} "
        f"WR={m['win_rate']:.3f} pnl={m['net_pnl']:.2f}"
    )


def _row_summary(key: str, tp: float, sl: float, n_dec: int, res: dict) -> dict:
    row = {
        "arm": key,
        "tp_pct": tp,
        "sl_pct": sl,
        "n_decisions": n_dec,
        "status": res.get("status"),
        "n_signals": res.get("n_signals", n_dec),
    }
    if res.get("status") == "RAN":
        row.update(res["metrics"])
    elif res.get("error"):
        row["error"] = res["error"]
    return row


def main() -> int:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    append_ledger(f"PIVOT_LIMIT_STRAT_DIAG_GRID start {stamp}", tier=0)
    print(
        f"pivot limit strategy diagnostic stamp={stamp} "
        f"tp={TP_ARMS} sl={SL_ARMS} rare H={H_BARS} atr>={ATR_MIN}",
        flush=True,
    )
    rows = []
    for sym in SYMBOLS:
        rows.append(run_symbol(sym))
    report = {
        "generation_id": "pivot_limit_strategy_diag_002_tp_sl_grid",
        "stamp": stamp,
        "source": "binance",
        "lockbox_start": FORWARD_LOCKBOX_START,
        "setup": {
            "timeframe": TF,
            "horizon_bars": H_BARS,
            "atr_min": ATR_MIN,
            "tp_pct_arms": list(TP_ARMS),
            "sl_pct_arms": list(SL_ARMS),
            "entry": "LIMIT at predicted pivot level (clamped) or market control",
            "gate": "calibrated p_any >= max(0.35, train_cal p75)",
            "note": (
                "Full TP×SL diagnostic matrix. Arms are pre-declared; do not promote "
                "by picking the single best cell on this outer path without a further "
                "pre-registered selection protocol. RESEARCH_ONLY."
            ),
        },
        "symbols": rows,
        "readiness_max": "RESEARCH_ONLY",
        "metric_explain_base_rate": (
            "High base rate means the LABEL 'pivot within horizon' was true on most bars "
            "(dense events), NOT that forecast precision was good."
        ),
    }
    out_dir = ARTIFACTS / "reports" / "pivot_forecast"
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / f"limit_strategy_diag_{stamp}.json"
    latest = out_dir / "limit_strategy_diag_latest.json"
    grid_md = out_dir / f"limit_strategy_grid_{stamp}.md"
    text = json.dumps(report, indent=2, default=str)
    out.write_text(text, encoding="utf-8")
    latest.write_text(text, encoding="utf-8")
    grid_md.write_text(_markdown_tables(report), encoding="utf-8")
    print(f"WROTE {out}", flush=True)
    print(f"WROTE {grid_md}", flush=True)
    # Console may be cp1252; files already hold the full UTF-8 tables.
    try:
        print(_markdown_tables(report), flush=True)
    except UnicodeEncodeError:
        print("(grid tables written to markdown file; console encoding cannot render them)", flush=True)
    return 0


def _markdown_tables(report: dict) -> str:
    lines = [
        f"# Pivot limit strategy TP×SL grid (`{report['stamp']}`)",
        "",
        f"Status: **{report['readiness_max']}** — not live authorization.",
        "",
        f"Setup: TF={report['setup']['timeframe']}, H={report['setup']['horizon_bars']}, "
        f"ATR>={report['setup']['atr_min']}, TP x SL full matrix.",
        "",
    ]
    for sym_row in report["symbols"]:
        sym = sym_row["symbol"]
        n_dec = sym_row.get("n_decisions", "?")
        lines.append(f"## {sym} (n_decisions={n_dec})")
        lines.append("")
        for mode, title in (
            ("limit", "LIMIT entry"),
            ("market", "MARKET entry control"),
        ):
            lines.append(f"### {title}")
            lines.append("")
            lines.append(
                "| TP% | SL% | n_trades | WR | PF | expectancy | net_pnl | liq |"
            )
            lines.append(
                "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |"
            )
            for r in sorted(
                sym_row["grid_summary"][mode],
                key=lambda x: (x["tp_pct"], x["sl_pct"]),
            ):
                if r.get("status") != "RAN":
                    lines.append(
                        f"| {100*r['tp_pct']:.0f} | {100*r['sl_pct']:.0f} | "
                        f"— | — | — | — | {r.get('status')} | — |"
                    )
                    continue
                lines.append(
                    f"| {100*r['tp_pct']:.0f} | {100*r['sl_pct']:.0f} | "
                    f"{r['n_trades']} | {r['win_rate']:.3f} | "
                    f"{r['profit_factor']:.3f} | {r['expectancy']:.4f} | "
                    f"{r['net_pnl']:.2f} | {r['n_liquidations']} |"
                )
            lines.append("")
    return "\n".join(lines)


if __name__ == "__main__":
    raise SystemExit(main())
