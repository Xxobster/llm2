"""Fleet 004: ETH dual arms + BTC 1h entry-bar attack + SOL hold.

RESEARCH_ONLY. Not live. Rank by intent expectancy.
Hard-block promote if entry-bar exit rate > 35%.
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
from llm2.pivot.strategy.score_oos import gate_mask, limit_price_side, score_symbol_oos  # noqa: E402
from llm2.pivot.strategy.soft_vsa import absorption_scores, train_threshold  # noqa: E402
from llm2.pivot.strategy.working_limit import LimitIntent, materialize_working_limits  # noqa: E402
from llm2.validation.folds import index_to_ms  # noqa: E402

PACK = "level_vsa"
MAX_ROWS = 120_000
EBR_CAP = 0.35


def _leak(symbol: str, tf: str, pack: str = PACK) -> dict:
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
        return {"symbol": symbol, "tf": tf, "pack": pack, "status": "PASS"}
    except Exception as exc:  # noqa: BLE001
        return {"symbol": symbol, "tf": tf, "status": "FAIL", "error": str(exc)[:300]}


def _bt(symbol, tf, ohlcv, signals, *, tag: str, max_hold: int, sl: float):
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
    # leverage from the widest SL used among signals
    sl_use = max(
        float(sl),
        max((float(getattr(s, "stop_offset", sl) or sl) for s in signals), default=sl),
    )
    bundle = run_strategy_backtest(
        window,
        signals,
        symbol=symbol,
        timeframe=tf,
        strategy_id=tag,
        touch_ohlcv=touch_win if len(touch_win) else None,
        touch_timeframe=touch_tf,
        costs=research_costs_baseline(),
        margin=research_margin(leverage=float(leverage_from_stop(sl_use))),
        sizing=research_sizing(),
        sim=research_sim_limit_entry(max_hold_bars=max_hold, decision_timeframe=tf),
        instrument=research_instrument(symbol),
        funding_ts_ms=f_ts[fmask],
        funding_rate=f_rt[fmask],
        plot=False,
        print_headline=False,
        store_path=None,
    )
    m = bundle.metrics
    trades = getattr(getattr(bundle, "result", None), "trades", None) or ()
    holds = [float(getattr(t, "hold_bars", 1)) for t in trades] if trades else []
    ebr = float(np.mean(np.asarray(holds) <= 0)) if holds else float("nan")
    return {
        "status": "RAN",
        "n_trades": int(m.n_trades),
        "profit_factor": float(m.profit_factor),
        "win_rate": float(m.win_rate),
        "net_pnl": float(m.net_pnl),
        "expectancy": float(m.expectancy),
        "entry_bar_exit_rate": ebr,
    }


def _p80_mask(sc) -> tuple[np.ndarray, float]:
    base = gate_mask(sc, mode="p75", tp=0.01, sl=0.01)
    p = np.asarray(sc.p_any, dtype=float)
    idx = np.flatnonzero(base)
    cut = max(30, int(0.7 * idx.size)) if idx.size else 30
    thr_floor = float(np.nanmedian(sc.thr_any[idx[:cut]])) if idx.size else 0.35
    train_p = p[idx[:cut]] if idx.size else p
    train_p = train_p[np.isfinite(train_p)]
    thr_ceil = float(np.nanpercentile(train_p, 80)) if train_p.size else 0.5
    thr = thr_ceil if thr_ceil > thr_floor else thr_floor
    return base & np.isfinite(p) & (p >= thr), thr


def _soft_vsa(sc, base: np.ndarray) -> tuple[np.ndarray, float]:
    scores = absorption_scores(sc.ohlcv, sc.ts_ms, sc.p_high >= 0.5)
    idx = np.flatnonzero(base)
    cut = max(30, int(0.7 * idx.size)) if idx.size else 30
    thr = train_threshold(scores[idx[:cut]] if idx.size else scores, q=0.70)
    return scores >= thr, thr


def _atr_clip(sc, lo=0.8, hi=1.5) -> np.ndarray:
    lr = np.asarray(sc.level_ret, dtype=float)
    atr = np.asarray(sc.atr_frac, dtype=float)
    out = np.sign(lr) * np.clip(np.abs(lr), lo * atr, hi * atr)
    out[~np.isfinite(lr) | ~np.isfinite(atr)] = np.nan
    return out


def _run_mask(
    symbol,
    sc,
    mask,
    *,
    tag: str,
    work: int,
    tp: float,
    sl: float,
    level_override=None,
    sl_per_row: np.ndarray | None = None,
    tp_per_row: np.ndarray | None = None,
):
    n_intent = int(mask.sum())
    if n_intent < 15:
        return {"tag": tag, "status": "TOO_FEW_GATED", "n_intent": n_intent}
    if level_override is not None:
        old = sc.level_ret
        sc.level_ret = level_override
        ts, is_short, lim = limit_price_side(sc, mask)
        sc.level_ret = old
    else:
        ts, is_short, lim = limit_price_side(sc, mask)
    idx = np.flatnonzero(mask)
    h = int(getattr(sc, "horizon_bars", 2) or 2)
    max_hold = h + 2
    intents = []
    for j in range(len(ts)):
        sl_j = float(sl_per_row[idx[j]]) if sl_per_row is not None else float(sl)
        tp_j = float(tp_per_row[idx[j]]) if tp_per_row is not None else float(tp)
        sl_j = float(np.clip(sl_j, 0.005, 0.05))
        tp_j = float(np.clip(tp_j, 0.005, 0.08))
        intents.append(
            LimitIntent(
                decision_ts_ms=int(ts[j]),
                side=Side.SHORT if is_short[j] else Side.LONG,
                limit_price=float(lim[j]),
                stop_offset=sl_j,
                target_offset=tp_j,
                max_hold_bars=max_hold,
                work_bars=work,
            )
        )
    sigs, fill = materialize_working_limits(sc.ohlcv, intents, work_bars=work)
    print(
        f"  BT {tag} intent={n_intent} fill%={100*float(fill['fill_rate']):.1f} "
        f"path={fill['n_filled_path']}",
        flush=True,
    )
    res = _bt(symbol, sc.timeframe, sc.ohlcv, sigs, tag=tag, max_hold=max_hold, sl=sl)
    out = {
        "tag": tag,
        "n_intent": n_intent,
        "fill_pct": float(fill["fill_rate"]),
        "fill_stats": fill,
        "tp": tp,
        "sl": sl,
        **res,
    }
    if res.get("status") == "RAN":
        out["expectancy_intent_all"] = float(res["net_pnl"]) / n_intent
        print(
            f"    n={res['n_trades']} PF={res['profit_factor']:.3f} WR={res['win_rate']:.3f} "
            f"pnl={res['net_pnl']:.2f} exp_i={out['expectancy_intent_all']:.5f} "
            f"ebr={100*float(res['entry_bar_exit_rate']):.1f}%",
            flush=True,
        )
    return out


def _promote(ref: dict, arm: dict) -> dict:
    if arm.get("status") != "RAN" or ref.get("status") != "RAN":
        return {"promote": False, "reason": "not_ran"}
    ebr = float(arm.get("entry_bar_exit_rate") or float("nan"))
    ebr_ok = np.isfinite(ebr) and ebr <= EBR_CAP
    ebr_pref = np.isfinite(ebr) and ebr <= 0.25
    exp_ok = float(arm.get("expectancy_intent_all") or -1e9) > float(
        ref.get("expectancy_intent_all") or -1e9
    )
    pf_ok = float(arm.get("profit_factor") or 0) >= 0.85 * float(ref.get("profit_factor") or 1)
    return {
        "entry_bar_ok": bool(ebr_ok),
        "entry_bar_preferred": bool(ebr_pref),
        "intent_exp_improved": bool(exp_ok),
        "pf_not_collapsed": bool(pf_ok),
        "promote": bool(ebr_ok and exp_ok and pf_ok),
        "entry_bar_exit_rate": ebr,
    }


def main() -> int:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out_dir = ARTIFACTS / "reports" / "pivot_forecast"
    out_dir.mkdir(parents=True, exist_ok=True)
    print(f"fleet 004 stamp={stamp}", flush=True)

    leak = [
        _leak("ETHUSDT", "15m"),
        _leak("SOLUSDT", "15m"),
        _leak("BTCUSDT", "15m"),
        _leak("BTCUSDT", "1h"),
    ]
    for x in leak:
        print(f"  leakage {x['symbol']} {x['tf']}: {x['status']}", flush=True)
    if any(x["status"] != "PASS" for x in leak):
        return 2

    freeze = {
        "stamp": stamp,
        "preregister": "configs/preregister/pivot_fleet_004_eth_dual_btc1h.yaml",
        "eth_dual": ["ETH_q50_w4", "ETH_q50_softvsa_w4"],
        "sol_hold": "SOL_atr_clip_w5",
        "btc_15m_fleet": "BTC_p80_w4",
        "ebr_cap": EBR_CAP,
        "btc_1h_arms_frozen_before_pf": [
            "BTC_1h_p80_tp1_sl1_w2",
            "BTC_1h_p80_tp15_sl15_w2",
            "BTC_1h_p80_tp2_sl2_w2",
            "BTC_1h_p80_tp2_sl15_w2",
            "BTC_1h_p80_sl_atr1p0_tp_eq_w2",
            "BTC_1h_p80_sl_atr1p5_tp_eq_w2",
            "BTC_1h_p80_atr_min2_tp15_sl15_w2",
            "BTC_1h_p80_filter_atr_ge_sl_w2",
        ],
    }
    freeze_path = out_dir / f"fleet_004_freeze_{stamp}.json"
    freeze_path.write_text(json.dumps(freeze, indent=2), encoding="utf-8")
    print(f"WROTE {freeze_path}", flush=True)

    report: dict = {
        "generation_id": "pivot_fleet_004_eth_dual_btc1h",
        "stamp": stamp,
        "readiness_max": "RESEARCH_ONLY",
        "not_live": True,
        "freeze_path": str(freeze_path),
        "leakage": leak,
    }

    # ---- ETH dual ----
    print("SCORE ETH q50 …", flush=True)
    eth = score_symbol_oos(
        "ETHUSDT",
        timeframe="15m",
        horizon_bars=4,
        feature_pack=PACK,
        max_rows=MAX_ROWS,
        level_mode="q50",
        atr_min=2.0,
    )
    ebase = gate_mask(eth, mode="p75", tp=0.01, sl=0.01)
    vsa, vsa_thr = _soft_vsa(eth, ebase)
    eth_vol = _run_mask(
        "ETHUSDT", eth, ebase, tag="ETH_q50_w4", work=4, tp=0.01, sl=0.01
    )
    eth_qual = _run_mask(
        "ETHUSDT", eth, ebase & vsa, tag="ETH_q50_softvsa_w4", work=4, tp=0.01, sl=0.01
    )
    report["eth_dual"] = {
        "soft_vsa_thr": vsa_thr,
        "volume_arm": eth_vol,
        "quality_arm": eth_qual,
        "policy": "volume=q50_w4; quality=q50_softvsa_w4; rank quality by intent_exp",
    }
    print(
        f"  ETH dual: vol n={eth_vol.get('n_trades')} PF={eth_vol.get('profit_factor')} "
        f"qual n={eth_qual.get('n_trades')} PF={eth_qual.get('profit_factor')} "
        f"exp_i {eth_vol.get('expectancy_intent_all')} vs {eth_qual.get('expectancy_intent_all')}",
        flush=True,
    )

    # ---- SOL hold ----
    print("SCORE SOL ret (hold atr_clip_w5) …", flush=True)
    sol = score_symbol_oos(
        "SOLUSDT",
        timeframe="15m",
        horizon_bars=4,
        feature_pack=PACK,
        max_rows=MAX_ROWS,
        level_mode="ret",
        atr_min=2.0,
    )
    sbase = gate_mask(sol, mode="p75", tp=0.01, sl=0.01)
    sol_arm = _run_mask(
        "SOLUSDT",
        sol,
        sbase,
        tag="SOL_atr_clip_w5",
        work=5,
        tp=0.01,
        sl=0.01,
        level_override=_atr_clip(sol),
    )
    report["sol_hold"] = {
        "arm": sol_arm,
        "revisit_1h": False,
        "reason": "entry_bar still >35% on prior 1h trials; hold 15m atr_clip_w5",
    }

    # ---- BTC 15m fleet ref + 1h attack ----
    print("SCORE BTC 15m p80 ref …", flush=True)
    btc15 = score_symbol_oos(
        "BTCUSDT",
        timeframe="15m",
        horizon_bars=4,
        feature_pack=PACK,
        max_rows=MAX_ROWS,
        level_mode="ret",
        atr_min=2.0,
    )
    m80_15, thr15 = _p80_mask(btc15)
    btc15_fleet = _run_mask(
        "BTCUSDT", btc15, m80_15, tag="BTC_p80_w4", work=4, tp=0.01, sl=0.01
    )

    print("SCORE BTC 1h atr_min=1.0 …", flush=True)
    btc1 = score_symbol_oos(
        "BTCUSDT",
        timeframe="1h",
        horizon_bars=2,
        feature_pack=PACK,
        max_rows=MAX_ROWS,
        level_mode="ret",
        atr_min=1.0,
    )
    print("SCORE BTC 1h atr_min=2.0 …", flush=True)
    btc1_s = score_symbol_oos(
        "BTCUSDT",
        timeframe="1h",
        horizon_bars=2,
        feature_pack=PACK,
        max_rows=MAX_ROWS,
        level_mode="ret",
        atr_min=2.0,
    )
    m80, thr1 = _p80_mask(btc1)
    m80s, thr1s = _p80_mask(btc1_s)
    atr = np.asarray(btc1.atr_frac, dtype=float)

    arms = [
        _run_mask(
            "BTCUSDT", btc1, m80, tag="BTC_1h_p80_tp1_sl1_w2", work=2, tp=0.01, sl=0.01
        ),
        _run_mask(
            "BTCUSDT", btc1, m80, tag="BTC_1h_p80_tp15_sl15_w2", work=2, tp=0.015, sl=0.015
        ),
        _run_mask(
            "BTCUSDT", btc1, m80, tag="BTC_1h_p80_tp2_sl2_w2", work=2, tp=0.02, sl=0.02
        ),
        _run_mask(
            "BTCUSDT", btc1, m80, tag="BTC_1h_p80_tp2_sl15_w2", work=2, tp=0.02, sl=0.015
        ),
        _run_mask(
            "BTCUSDT",
            btc1,
            m80,
            tag="BTC_1h_p80_sl_atr1p0_tp_eq_w2",
            work=2,
            tp=0.01,
            sl=0.01,
            sl_per_row=np.clip(1.0 * atr, 0.008, 0.04),
            tp_per_row=np.clip(1.0 * atr, 0.008, 0.04),
        ),
        _run_mask(
            "BTCUSDT",
            btc1,
            m80,
            tag="BTC_1h_p80_sl_atr1p5_tp_eq_w2",
            work=2,
            tp=0.01,
            sl=0.01,
            sl_per_row=np.clip(1.5 * atr, 0.01, 0.05),
            tp_per_row=np.clip(1.5 * atr, 0.01, 0.05),
        ),
        _run_mask(
            "BTCUSDT",
            btc1_s,
            m80s,
            tag="BTC_1h_p80_atr_min2_tp15_sl15_w2",
            work=2,
            tp=0.015,
            sl=0.015,
        ),
        _run_mask(
            "BTCUSDT",
            btc1,
            m80 & np.isfinite(atr) & (atr >= 0.01),
            tag="BTC_1h_p80_filter_atr_ge_sl_w2",
            work=2,
            tp=0.01,
            sl=0.01,
        ),
    ]

    promotions = {a["tag"]: _promote(btc15_fleet, a) for a in arms}
    # best promote with lowest ebr among promoted; else best ebr<=cap by intent_exp
    promoted = [a for a in arms if promotions[a["tag"]].get("promote")]
    if promoted:
        pick = sorted(
            promoted,
            key=lambda a: (
                float(a.get("entry_bar_exit_rate") or 1),
                -float(a.get("expectancy_intent_all") or -1e9),
            ),
        )[0]["tag"]
    else:
        ok_ebr = [
            a
            for a in arms
            if a.get("status") == "RAN"
            and float(a.get("entry_bar_exit_rate") or 1) <= EBR_CAP
        ]
        pick = (
            sorted(
                ok_ebr, key=lambda a: -float(a.get("expectancy_intent_all") or -1e9)
            )[0]["tag"]
            if ok_ebr
            else None
        )

    report["btc"] = {
        "fleet_15m_p80": btc15_fleet,
        "thr_15m_p80": thr15,
        "thr_1h_p80": thr1,
        "thr_1h_atr_min2_p80": thr1s,
        "arms_1h": arms,
        "promotions_vs_15m_p80": promotions,
        "pick_1h_if_any": pick,
        "policy": "keep BTC_p80_w4 until 1h arm promotes with ebr<=35%",
    }

    report["updated_fleet"] = {
        "ETHUSDT_volume": "ETH_q50_w4",
        "ETHUSDT_quality": "ETH_q50_softvsa_w4",
        "SOLUSDT": "SOL_atr_clip_w5",
        "BTCUSDT_15m": "BTC_p80_w4",
        "BTCUSDT_1h": pick,
    }

    path = out_dir / f"fleet_004_{stamp}.json"
    latest = out_dir / "fleet_004_latest.json"
    path.write_text(json.dumps(report, indent=2, default=str), encoding="utf-8")
    latest.write_text(path.read_text(encoding="utf-8"), encoding="utf-8")
    md = out_dir / f"fleet_004_{stamp}.md"
    md.write_text(_md(report), encoding="utf-8")
    print(f"WROTE {path}", flush=True)
    print(f"UPDATED FLEET: {report['updated_fleet']}", flush=True)
    try:
        print(_md(report), flush=True)
    except UnicodeEncodeError:
        pass
    return 0


def _md(r: dict) -> str:
    lines = [
        f"# Fleet 004 (`{r['stamp']}`)",
        "",
        f"**{r['readiness_max']}** — ETH dual + BTC 1h entry-bar attack + SOL hold",
        "",
        f"**Fleet:** `{r.get('updated_fleet')}`",
        "",
        "## ETH dual",
    ]
    for key in ("volume_arm", "quality_arm"):
        a = r["eth_dual"][key]
        if a.get("status") != "RAN":
            lines.append(f"- {key}: {a.get('status')}")
            continue
        lines.append(
            f"- **{a['tag']}**: n={a['n_trades']} PF={a['profit_factor']:.3f} "
            f"WR={a['win_rate']:.3f} pnl={a['net_pnl']:.2f} "
            f"exp_i={a['expectancy_intent_all']:.5f} ebr={100*a['entry_bar_exit_rate']:.1f}%"
        )
    lines.append("")
    lines.append("## SOL hold")
    a = r["sol_hold"]["arm"]
    if a.get("status") == "RAN":
        lines.append(
            f"- **{a['tag']}**: n={a['n_trades']} PF={a['profit_factor']:.3f} "
            f"ebr={100*a['entry_bar_exit_rate']:.1f}% (1h not revisited)"
        )
    lines.append("")
    lines.append("## BTC 1h entry-bar attack")
    ref = r["btc"]["fleet_15m_p80"]
    lines.append(
        f"15m fleet `{ref.get('tag')}`: n={ref.get('n_trades')} PF={ref.get('profit_factor')} "
        f"exp_i={ref.get('expectancy_intent_all')} ebr={ref.get('entry_bar_exit_rate')}"
    )
    lines.append("")
    lines.append("| tag | n | PF | WR | pnl | exp_i | ebr% | promote |")
    lines.append("|---|---:|---:|---:|---:|---:|---:|---|")
    prom = r["btc"]["promotions_vs_15m_p80"]
    for a in r["btc"]["arms_1h"]:
        if a.get("status") != "RAN":
            lines.append(f"| {a.get('tag')} | — | — | — | — | — | — | {a.get('status')} |")
            continue
        p = prom.get(a["tag"], {})
        lines.append(
            f"| {a['tag']} | {a['n_trades']} | {a['profit_factor']:.3f} | {a['win_rate']:.3f} | "
            f"{a['net_pnl']:.2f} | {a['expectancy_intent_all']:.5f} | "
            f"{100*a['entry_bar_exit_rate']:.1f}% | {p.get('promote')} |"
        )
    lines.append("")
    lines.append(f"**BTC 1h pick:** `{r['btc'].get('pick_1h_if_any')}`")
    return "\n".join(lines)


if __name__ == "__main__":
    raise SystemExit(main())
