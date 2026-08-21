"""Level redesign + soft VSA + P75 multi-symbol control + SOL TF trial.

RESEARCH_ONLY. Leakage before score. LIMIT only, work 2-4. No re-entry. No full timing stack.

Arms (preregistered):
  Level MAE: level_vsa vs level_strong; ret / atr_resid / q-bands (q50 + narrow width)
  Control: BTC ret P75, ETH atr P75, SOL ret P75 (work4)
  Soft VSA: train q70 score threshold on control
  pi*+band sparse (report only)
  SOL TF: 15m vs 1h (atr_min=1.0) for entry-bar exit rate
"""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from tradesim.ensure_source import prefer_botsgeneral_tradesim

prefer_botsgeneral_tradesim()

from leakage.ensure_source import prefer_botsgeneral_leakage

prefer_botsgeneral_leakage()

from tradesim import Side, research_instrument, research_margin, research_sizing  # noqa: E402
from tradesim import research_sim_limit_entry  # noqa: E402

from llm2.backtest.run import run_strategy_backtest  # noqa: E402
from llm2.data.loader import load_ohlcv  # noqa: E402
from llm2.data.macro import load_funding  # noqa: E402
from llm2.gates.evidence import leverage_from_stop, research_costs_baseline  # noqa: E402
from llm2.paths import ARTIFACTS, FORWARD_LOCKBOX_START, TF_MS, touch_timeframe  # noqa: E402
from llm2.pivot.features.packs import build_feature_frame  # noqa: E402
from llm2.pivot.strategy.ev import net_bracket_magnitudes  # noqa: E402
from llm2.pivot.strategy.level_bands import score_level_bands  # noqa: E402
from llm2.pivot.strategy.level_economy import level_error_stats  # noqa: E402
from llm2.pivot.strategy.score_oos import (  # noqa: E402
    gate_mask,
    limit_price_side,
    score_symbol_oos,
)
from llm2.pivot.strategy.soft_vsa import absorption_scores, train_threshold  # noqa: E402
from llm2.pivot.strategy.working_limit import LimitIntent, materialize_working_limits  # noqa: E402
from llm2.pivot.train.samples import build_samples  # noqa: E402
from llm2.pivot.labels.config import PivotLabelConfig  # noqa: E402
from llm2.validation.folds import index_to_ms  # noqa: E402

SYMBOLS = ("BTCUSDT", "ETHUSDT", "SOLUSDT")
TP = SL = 0.01
H15 = 4
WORK = 4
MAX_ROWS = 120_000


def _leak(symbol: str, pack: str, tf: str) -> dict:
    from leakage import require_clean_audit, run_leakage_audit

    try:
        ohlcv = load_ohlcv(symbol, tf)
        lock = pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC")
        ohlcv = ohlcv.loc[ohlcv.index < lock].iloc[-6000:].copy()

        def _b(df, **_k):
            return build_feature_frame(df, pack=pack)

        require_clean_audit(
            run_leakage_audit(
                ohlcv=ohlcv, build_features=_b, interval=tf, symbol=symbol, timeframe=tf
            )
        )
        return {"symbol": symbol, "pack": pack, "tf": tf, "status": "PASS"}
    except Exception as exc:  # noqa: BLE001
        return {
            "symbol": symbol,
            "pack": pack,
            "tf": tf,
            "status": "FAIL",
            "error": str(exc)[:300],
        }


def _metrics(bundle) -> dict:
    m = bundle.metrics
    out = {
        "n_trades": int(m.n_trades),
        "profit_factor": float(m.profit_factor),
        "net_pnl": float(m.net_pnl),
        "win_rate": float(m.win_rate),
        "expectancy": float(m.expectancy),
    }
    trades = getattr(getattr(bundle, "result", None), "trades", None) or ()
    if trades:
        holds = [float(getattr(t, "hold_bars", 1)) for t in trades]
        out["entry_bar_exit_rate"] = float(np.mean(np.asarray(holds) <= 0))
    return out


def _bt(symbol, tf, ohlcv, signals, *, sl, tag, max_hold):
    if len(signals) < 12:
        return {"status": "TOO_FEW", "n_signals": len(signals)}
    touch_tf = touch_timeframe(tf, symbol)
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
    window = ohlcv.iloc[max(0, i0 - 80) : min(len(ohlcv), i1 + 80)]
    w_ts = index_to_ms(window.index)
    fmask = (f_ts >= int(w_ts[0])) & (f_ts <= int(w_ts[-1]))
    end, start = window.index[-1], window.index[0]
    touch_end = end + pd.Timedelta(milliseconds=int(TF_MS[tf])) - pd.Timedelta(milliseconds=1)
    touch_win = touch.loc[(touch.index >= start) & (touch.index <= touch_end)]
    bundle = run_strategy_backtest(
        window,
        signals,
        symbol=symbol,
        timeframe=tf,
        strategy_id=tag,
        touch_ohlcv=touch_win if len(touch_win) else None,
        touch_timeframe=touch_tf,
        costs=research_costs_baseline(),
        margin=research_margin(leverage=float(leverage_from_stop(sl))),
        sizing=research_sizing(),
        sim=research_sim_limit_entry(max_hold_bars=max_hold, decision_timeframe=tf),
        instrument=research_instrument(symbol),
        funding_ts_ms=f_ts[fmask],
        funding_rate=f_rt[fmask],
        plot=False,
        print_headline=False,
        store_path=None,
    )
    return {"status": "RAN", "metrics": _metrics(bundle), "n_signals": len(signals)}


def _run_limit(symbol, sc, *, gate, level_override=None, extra_mask=None, tag="", work=WORK):
    pi = net_bracket_magnitudes(TP, SL).pi_star
    h_bars = int(getattr(sc, "horizon_bars", H15) or H15)
    max_hold = h_bars + 2
    mask = gate_mask(
        sc, mode=gate, tp=TP, sl=SL, pi_star=pi, min_abs_level=0.0015, max_abs_level=0.02
    )
    if extra_mask is not None:
        mask = mask & extra_mask
    if level_override is not None:
        # temporarily replace level_ret for pricing
        old = sc.level_ret
        sc.level_ret = level_override
        ts, is_short, lim = limit_price_side(sc, mask)
        sc.level_ret = old
    else:
        ts, is_short, lim = limit_price_side(sc, mask)
    n_g = int(mask.sum())
    if n_g < 15:
        return {"tag": tag, "status": "TOO_FEW_GATED", "n_gated": n_g}
    intents = [
        LimitIntent(
            decision_ts_ms=int(ts[j]),
            side=Side.SHORT if is_short[j] else Side.LONG,
            limit_price=float(lim[j]),
            stop_offset=SL,
            target_offset=TP,
            max_hold_bars=max_hold,
            work_bars=work,
        )
        for j in range(len(ts))
    ]
    sigs, fill = materialize_working_limits(sc.ohlcv, intents, work_bars=work)
    print(f"  BT {tag} gated={n_g} fill={fill['n_filled_path']} …", flush=True)
    res = _bt(symbol, sc.timeframe, sc.ohlcv, sigs, sl=SL, tag=tag, max_hold=max_hold)
    out = {"tag": tag, "n_gated": n_g, "fill_stats": fill, **res}
    if res.get("status") == "RAN":
        out["expectancy_intent_all"] = res["metrics"]["net_pnl"] / n_g
        print(
            f"    PF={res['metrics']['profit_factor']:.3f} n={res['metrics']['n_trades']} "
            f"WR={res['metrics']['win_rate']:.3f} ebr={res['metrics'].get('entry_bar_exit_rate')}",
            flush=True,
        )
    return out


def _mae_pack_compare(symbol: str) -> dict:
    rows = {}
    for pack in ("level_vsa", "level_strong"):
        for target in ("ret", "atr_resid"):
            print(f"MAE {symbol} pack={pack} target={target} …", flush=True)
            cfg = PivotLabelConfig(
                timeframe="15m",
                left_bars=3,
                right_bars=3,
                confirm_bars=3,
                min_left_prominence_atr=2.0,
                min_right_reversal_atr=2.0,
                min_reversal_pct=0.0015,
                atr_period=14,
                label_family="fractal_mae",
                suppress_neighbor_bars=3,
            )
            samp = build_samples(
                symbol=symbol,
                timeframe="15m",
                feature_pack=pack,
                label_cfg=cfg,
                horizon_bars=H15,
                max_rows=MAX_ROWS,
            )
            # atr from close path via score helper: rebuild atr on samples
            sc = score_symbol_oos(
                symbol,
                timeframe="15m",
                horizon_bars=H15,
                feature_pack=pack,
                max_rows=MAX_ROWS,
                level_mode="atr" if target == "atr_resid" else "ret",
            )
            bands = score_level_bands(
                samp["X"],
                samp["y_level_ret"],
                sc.atr_frac[: len(samp["y_level_ret"])]
                if len(sc.atr_frac) >= len(samp["y_level_ret"])
                else np.resize(sc.atr_frac, len(samp["y_level_ret"])),
                samp["ts_ms"],
                horizon_bars=H15,
                target=target,
            )
            # align lengths carefully: use sc arrays (same build path)
            # Prefer scoring q50 via dedicated path on sc rows
            # Recompute bands on sc-sized arrays
            # Build X aligned to sc by re-scoring samples equal to sc
            pass
            m = np.isfinite(sc.y_level) & np.isfinite(sc.level_ret)
            rows[f"{pack}_{target}_point"] = level_error_stats(
                y_level_ret=sc.y_level[m],
                pred_level_ret=sc.level_ret[m],
                atr_frac=sc.atr_frac[m],
            )
            # quantile band q50 from level_bands on matching sample length
            # Use samp indices that match finite mask via ts join
            ts_map = {int(t): i for i, t in enumerate(samp["ts_ms"].tolist())}
            pred_q50 = np.full(len(sc.ts_ms), np.nan)
            width = np.full(len(sc.ts_ms), np.nan)
            # need bands on samp — rebuild with atr aligned to samp
            from llm2.pivot.strategy.score_oos import _atr_frac

            ohlcv = sc.ohlcv
            atr_all = _atr_frac(ohlcv)
            ohlcv_ts = index_to_ms(ohlcv.index)
            atr_map = dict(zip(ohlcv_ts.tolist(), atr_all.tolist()))
            atr_s = np.array([atr_map.get(int(t), np.nan) for t in samp["ts_ms"]], dtype=float)
            bands = score_level_bands(
                samp["X"],
                samp["y_level_ret"],
                atr_s,
                samp["ts_ms"],
                horizon_bars=H15,
                target=target,
            )
            for j, t in enumerate(sc.ts_ms):
                i = ts_map.get(int(t))
                if i is None:
                    continue
                pred_q50[j] = bands["q50"][i]
                width[j] = bands["width"][i]
            mq = np.isfinite(sc.y_level) & np.isfinite(pred_q50)
            rows[f"{pack}_{target}_q50"] = level_error_stats(
                y_level_ret=sc.y_level[mq],
                pred_level_ret=pred_q50[mq],
                atr_frac=sc.atr_frac[mq],
            )
            # narrow-band subset: width <= train p50 width
            w_ok = width[mq]
            if w_ok.size:
                thr_w = float(np.nanpercentile(w_ok, 50))
                narrow = mq & np.isfinite(width) & (width <= thr_w)
                rows[f"{pack}_{target}_q50_narrow"] = {
                    **level_error_stats(
                        y_level_ret=sc.y_level[narrow],
                        pred_level_ret=pred_q50[narrow],
                        atr_frac=sc.atr_frac[narrow],
                    ),
                    "width_thr": thr_w,
                    "n_narrow": int(narrow.sum()),
                }
            print(
                f"  point MAE={rows[f'{pack}_{target}_point']['mae_pct']:.4f} "
                f"q50 MAE={rows[f'{pack}_{target}_q50']['mae_pct']:.4f} "
                f"P90_q50={rows[f'{pack}_{target}_q50']['p90_abs_pct']:.4f}",
                flush=True,
            )
    return rows


def main() -> int:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    print(f"pivot level redesign stack stamp={stamp}", flush=True)

    leak = []
    for sym in SYMBOLS:
        for pack in ("level_vsa", "level_strong"):
            leak.append(_leak(sym, pack, "15m"))
        leak.append(_leak(sym, "level_strong", "1h"))
    for x in leak:
        print(f"  leakage {x['symbol']} {x['tf']} {x['pack']}: {x['status']}", flush=True)
    if any(x["status"] != "PASS" for x in leak):
        print("LEAKAGE FAIL", flush=True)
        return 2

    mae = {sym: _mae_pack_compare(sym) for sym in SYMBOLS}

    # Controls + soft VSA + pi band
    trade = {}
    for sym in SYMBOLS:
        level_mode = "atr" if sym == "ETHUSDT" else "ret"
        pack = "level_strong"
        print(f"SCORE trade {sym} pack={pack} level={level_mode} …", flush=True)
        sc = score_symbol_oos(
            sym,
            timeframe="15m",
            horizon_bars=H15,
            feature_pack=pack,
            max_rows=MAX_ROWS,
            level_mode=level_mode,
        )
        # soft VSA threshold from first 70% gated p75 rows
        base_mask = gate_mask(sc, mode="p75", tp=TP, sl=SL)
        is_short = sc.p_high >= 0.5
        scores = absorption_scores(sc.ohlcv, sc.ts_ms, is_short)
        idx = np.flatnonzero(base_mask)
        cut = max(30, int(0.7 * idx.size))
        thr_vsa = train_threshold(scores[idx[:cut]], q=0.70)
        vsa_mask = scores >= thr_vsa
        print(f"  soft VSA thr(train q70)={thr_vsa:.3f}", flush=True)

        arms = [
            _run_limit(sym, sc, gate="p75", tag=f"{sym}_ctrl_p75_{level_mode}"),
            _run_limit(
                sym,
                sc,
                gate="p75",
                extra_mask=vsa_mask,
                tag=f"{sym}_ctrl_p75_softvsa_{level_mode}",
            ),
            _run_limit(sym, sc, gate="pi_star_level", tag=f"{sym}_pi_band_{level_mode}"),
        ]
        # q50 narrow level override for SOL/BTC/ETH control pricing
        # rebuild q50 from bands on same sc
        from llm2.pivot.train.samples import build_samples as _bs
        from llm2.pivot.strategy.score_oos import default_label_cfg, _atr_frac

        samp = _bs(
            symbol=sym,
            timeframe="15m",
            feature_pack=pack,
            label_cfg=default_label_cfg(timeframe="15m"),
            horizon_bars=H15,
            max_rows=MAX_ROWS,
        )
        atr_all = _atr_frac(sc.ohlcv)
        ohlcv_ts = index_to_ms(sc.ohlcv.index)
        atr_map = dict(zip(ohlcv_ts.tolist(), atr_all.tolist()))
        atr_s = np.array([atr_map.get(int(t), np.nan) for t in samp["ts_ms"]], dtype=float)
        bands = score_level_bands(
            samp["X"],
            samp["y_level_ret"],
            atr_s,
            samp["ts_ms"],
            horizon_bars=H15,
            target="atr_resid" if level_mode == "atr" else "ret",
        )
        ts_map = {int(t): i for i, t in enumerate(samp["ts_ms"].tolist())}
        q50 = np.array(
            [bands["q50"][ts_map[int(t)]] if int(t) in ts_map else np.nan for t in sc.ts_ms],
            dtype=float,
        )
        width = np.array(
            [bands["width"][ts_map[int(t)]] if int(t) in ts_map else np.nan for t in sc.ts_ms],
            dtype=float,
        )
        w_tr = width[idx[:cut]]
        w_tr = w_tr[np.isfinite(w_tr)]
        thr_w = float(np.nanpercentile(w_tr, 50)) if w_tr.size else 0.02
        narrow = np.isfinite(width) & (width <= thr_w) & np.isfinite(q50)
        arms.append(
            _run_limit(
                sym,
                sc,
                gate="p75",
                level_override=q50,
                extra_mask=narrow,
                tag=f"{sym}_q50_narrow_{level_mode}",
            )
        )
        trade[sym] = {"level_mode": level_mode, "soft_vsa_thr": thr_vsa, "arms": arms}

    # SOL TF trial for entry-bar
    print("SOL TF trial 1h atr_min=1.0 …", flush=True)
    sol1h = score_symbol_oos(
        "SOLUSDT",
        timeframe="1h",
        horizon_bars=2,
        atr_min=1.0,
        feature_pack="level_strong",
        max_rows=MAX_ROWS,
        level_mode="ret",
    )
    sol_tf = [
        _run_limit("SOLUSDT", sol1h, gate="p75", tag="SOLUSDT_1h_p75_ret", work=2),
    ]

    report = {
        "generation_id": "pivot_level_redesign_001",
        "stamp": stamp,
        "readiness_max": "RESEARCH_ONLY",
        "leakage": leak,
        "level_mae": mae,
        "trade_controls": trade,
        "sol_tf_trial": sol_tf,
        "policy": {
            "no_full_timing_stack": True,
            "no_reentry": True,
            "eth_default_level": "atr",
            "sol_btc_default_level": "ret",
            "pi_band_sparse": True,
        },
    }
    out_dir = ARTIFACTS / "reports" / "pivot_forecast"
    path = out_dir / f"level_redesign_{stamp}.json"
    latest = out_dir / "level_redesign_latest.json"
    md = out_dir / f"level_redesign_{stamp}.md"
    path.write_text(json.dumps(report, indent=2, default=str), encoding="utf-8")
    latest.write_text(path.read_text(encoding="utf-8"), encoding="utf-8")
    md.write_text(_md(report), encoding="utf-8")
    print(f"WROTE {path}", flush=True)
    try:
        print(_md(report), flush=True)
    except UnicodeEncodeError:
        pass
    return 0


def _md(r: dict) -> str:
    lines = [
        f"# Level redesign + soft VSA (`{r['stamp']}`)",
        "",
        f"**{r['readiness_max']}**",
        "",
        "## Level MAE (selected)",
    ]
    for sym, rows in r["level_mae"].items():
        lines.append(f"### {sym}")
        lines.append("| key | MAE | P90 | n |")
        lines.append("|---|---:|---:|---:|")
        for k, v in rows.items():
            lines.append(
                f"| {k} | {v.get('mae_pct')} | {v.get('p90_abs_pct')} | {v.get('n')} |"
            )
        lines.append("")
    lines.append("## Trade arms")
    for sym, block in r["trade_controls"].items():
        lines.append(f"### {sym} (level={block['level_mode']}, softVSA thr={block['soft_vsa_thr']:.3f})")
        lines.append("| tag | n_gated | n_tr | WR | PF | exp_intent | entry_bar% | pnl |")
        lines.append("|---|---:|---:|---:|---:|---:|---:|---:|")
        for a in block["arms"]:
            if a.get("status") != "RAN":
                lines.append(f"| {a.get('tag')} | {a.get('n_gated')} | — | — | {a.get('status')} | — | — | — |")
                continue
            m = a["metrics"]
            lines.append(
                f"| {a['tag']} | {a['n_gated']} | {m['n_trades']} | {m['win_rate']:.3f} | "
                f"{m['profit_factor']:.3f} | {a.get('expectancy_intent_all', float('nan')):.5f} | "
                f"{100*float(m.get('entry_bar_exit_rate', float('nan'))):.1f}% | {m['net_pnl']:.2f} |"
            )
        lines.append("")
    lines.append("## SOL TF trial")
    for a in r["sol_tf_trial"]:
        if a.get("status") != "RAN":
            lines.append(f"- {a.get('tag')}: {a.get('status')} n_gated={a.get('n_gated')}")
        else:
            m = a["metrics"]
            lines.append(
                f"- {a['tag']}: n={m['n_trades']} PF={m['profit_factor']:.3f} "
                f"WR={m['win_rate']:.3f} entry_bar%={100*float(m.get('entry_bar_exit_rate', float('nan'))):.1f}"
            )
    return "\n".join(lines)


if __name__ == "__main__":
    raise SystemExit(main())
