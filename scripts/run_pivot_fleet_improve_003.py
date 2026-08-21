"""Fleet improve 003: ETH q50 + SOL atr_clip_w5 + BTC p80 (RESEARCH_ONLY, no Finplot).

Frozen before PF. Rank by intent expectancy.
BTC: mid-density p76..p79 + 1h structure; no ETH/SOL placement copy.
ETH/SOL: deepen fleet siblings (soft VSA, w5, level_strong if ECE holds).
"""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.metrics import average_precision_score

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
from llm2.pivot.strategy.score_oos import (  # noqa: E402
    _atr_frac,
    gate_mask,
    limit_price_side,
    score_symbol_oos,
)
from llm2.pivot.strategy.soft_vsa import absorption_scores, train_threshold  # noqa: E402
from llm2.pivot.strategy.working_limit import LimitIntent, materialize_working_limits  # noqa: E402
from llm2.pivot.train.multihead import expected_calibration_error  # noqa: E402
from llm2.validation.folds import index_to_ms  # noqa: E402

TP = SL = 0.01
MAX_ROWS = 120_000
PACK = "level_vsa"


def _leak(symbol: str, pack: str, tf: str = "15m") -> dict:
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


def _diag(sc) -> dict:
    y = np.asarray(sc.y_any, dtype=float)
    p = np.asarray(sc.p_any, dtype=float)
    m = np.isfinite(y) & np.isfinite(p)
    y, p = y[m], p[m]
    br = float(np.mean(y)) if y.size else float("nan")
    pr = (
        float(average_precision_score(y, p))
        if y.size >= 20 and len(np.unique(y)) >= 2
        else float("nan")
    )
    ece = expected_calibration_error(y, p) if y.size >= 20 else float("nan")
    yl, pl = np.asarray(sc.y_level, dtype=float), np.asarray(sc.level_ret, dtype=float)
    ml = np.isfinite(yl) & np.isfinite(pl)
    ae = np.abs(yl[ml] - pl[ml]) if ml.any() else np.array([])
    return {
        "frac_any": br,
        "pr_auc_lift": float(pr - br) if np.isfinite(pr) else float("nan"),
        "ece": float(ece),
        "level_p90": float(np.percentile(ae, 90)) if ae.size else float("nan"),
    }


def _bt(symbol, tf, ohlcv, signals, *, tag: str, max_hold: int, sl: float = SL):
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


def _atr_clip_level(sc, lo: float = 0.8, hi: float = 1.5) -> np.ndarray:
    lr = np.asarray(sc.level_ret, dtype=float).copy()
    atr = np.asarray(sc.atr_frac, dtype=float)
    out = np.sign(lr) * np.clip(np.abs(lr), lo * atr, hi * atr)
    out[~np.isfinite(lr) | ~np.isfinite(atr)] = np.nan
    return out


def _train_pct_gate(sc, base: np.ndarray, q: float) -> tuple[np.ndarray, float]:
    """P75 base ∩ p_any >= train percentile q of base rows (first 70%).

    Note: q=75 here is *within* the already P75-gated set (stricter than raw P75).
    For a true P75 control, use ``base`` directly without this helper.
    """
    p = np.asarray(sc.p_any, dtype=float)
    idx = np.flatnonzero(base)
    if idx.size < 40:
        return base.copy(), float("nan")
    cut = max(30, int(0.7 * idx.size))
    thr = float(np.nanpercentile(p[idx[:cut]], q))
    return base & np.isfinite(p) & (p >= thr), thr


def _mid_density_gates(sc, base: np.ndarray) -> dict[str, tuple[np.ndarray, float]]:
    """Gates between raw P75 and fleet P80: interpolate thresholds on train slice."""
    p = np.asarray(sc.p_any, dtype=float)
    idx = np.flatnonzero(base)
    out: dict[str, tuple[np.ndarray, float]] = {"p75_raw": (base.copy(), float("nan"))}
    if idx.size < 40:
        return out
    cut = max(30, int(0.7 * idx.size))
    train_p = p[idx[:cut]]
    train_p = train_p[np.isfinite(train_p)]
    if train_p.size < 30:
        return out
    # Floor = median thr_any on train base rows (binding P75); ceiling = p80 of p_any
    thr_floor = float(np.nanmedian(sc.thr_any[idx[:cut]]))
    thr_ceil = float(np.nanpercentile(train_p, 80))
    if not np.isfinite(thr_floor) or not np.isfinite(thr_ceil) or thr_ceil <= thr_floor:
        thr_floor = float(np.nanpercentile(train_p, 0))
        thr_ceil = float(np.nanpercentile(train_p, 80))
    for name, alpha in (("p76", 0.2), ("p77", 0.4), ("p78", 0.6), ("p79", 0.8), ("p80", 1.0)):
        thr = thr_floor + alpha * (thr_ceil - thr_floor)
        out[name] = (base & np.isfinite(p) & (p >= thr), thr)
    return out


def _soft_vsa_mask(sc, base: np.ndarray) -> tuple[np.ndarray, float]:
    is_short = sc.p_high >= 0.5
    scores = absorption_scores(sc.ohlcv, sc.ts_ms, is_short)
    idx = np.flatnonzero(base)
    cut = max(30, int(0.7 * idx.size)) if idx.size else 30
    thr = train_threshold(scores[idx[:cut]] if idx.size else scores, q=0.70)
    return scores >= thr, thr


def _run(
    symbol,
    sc,
    mask,
    *,
    tag: str,
    work: int,
    level_override=None,
    tp: float = TP,
    sl: float = SL,
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
    h = int(getattr(sc, "horizon_bars", 4) or 4)
    max_hold = h + 2
    intents = [
        LimitIntent(
            decision_ts_ms=int(ts[j]),
            side=Side.SHORT if is_short[j] else Side.LONG,
            limit_price=float(lim[j]),
            stop_offset=sl,
            target_offset=tp,
            max_hold_bars=max_hold,
            work_bars=work,
        )
        for j in range(len(ts))
    ]
    sigs, fill = materialize_working_limits(sc.ohlcv, intents, work_bars=work)
    fill_pct = float(fill["fill_rate"])
    print(
        f"  BT {tag} intent={n_intent} fill%={100*fill_pct:.1f} path={fill['n_filled_path']}",
        flush=True,
    )
    res = _bt(symbol, sc.timeframe, sc.ohlcv, sigs, tag=tag, max_hold=max_hold, sl=sl)
    out = {"tag": tag, "n_intent": n_intent, "fill_pct": fill_pct, "fill_stats": fill, **res}
    if res.get("status") == "RAN":
        out["expectancy_intent_all"] = float(res["net_pnl"]) / n_intent
        print(
            f"    n={res['n_trades']} PF={res['profit_factor']:.3f} WR={res['win_rate']:.3f} "
            f"pnl={res['net_pnl']:.2f} exp_i={out['expectancy_intent_all']:.5f} "
            f"ebr={res['entry_bar_exit_rate']}",
            flush=True,
        )
    return out


def _rank(arms: list[dict]) -> list[dict]:
    ran = [a for a in arms if a.get("status") == "RAN"]
    ran = sorted(
        ran,
        key=lambda a: (
            -float(a.get("expectancy_intent_all") or -1e9),
            -float(a.get("net_pnl") or -1e9),
            -float(a.get("n_trades") or 0),
        ),
    )
    return [
        {
            "rank": i + 1,
            "tag": a["tag"],
            "expectancy_intent_all": a.get("expectancy_intent_all"),
            "profit_factor": a.get("profit_factor"),
            "n_trades": a.get("n_trades"),
            "fill_pct": a.get("fill_pct"),
            "win_rate": a.get("win_rate"),
            "net_pnl": a.get("net_pnl"),
            "entry_bar_exit_rate": a.get("entry_bar_exit_rate"),
        }
        for i, a in enumerate(ran)
    ]


def _promote(
    fleet: dict,
    arm: dict,
    *,
    ece_ok: bool = True,
    max_entry_bar: float | None = 0.35,
) -> dict:
    if arm.get("status") != "RAN" or fleet.get("status") != "RAN":
        return {"promote": False, "reason": "not_ran"}
    exp_ok = float(arm.get("expectancy_intent_all") or -1e9) > float(
        fleet.get("expectancy_intent_all") or -1e9
    )
    pf_ok = float(arm.get("profit_factor") or 0) >= 0.85 * float(fleet.get("profit_factor") or 1)
    pnl_ok = float(arm.get("net_pnl") or -1e9) >= float(fleet.get("net_pnl") or 0) * 0.95
    ebr = float(arm.get("entry_bar_exit_rate") or float("nan"))
    ebr_ok = True if max_entry_bar is None or not np.isfinite(ebr) else ebr <= max_entry_bar
    return {
        "intent_exp_improved": bool(exp_ok),
        "pf_not_collapsed": bool(pf_ok),
        "pnl_near_or_better": bool(pnl_ok),
        "ece_ok": bool(ece_ok),
        "entry_bar_ok": bool(ebr_ok),
        "promote": bool(exp_ok and pf_ok and ece_ok and ebr_ok),
        "promote_volume": bool(exp_ok and pf_ok and ece_ok and pnl_ok and ebr_ok),
        "entry_bar_exit_rate": ebr,
    }


def _mid_atr(sc, base: np.ndarray) -> np.ndarray:
    abs_lr = np.abs(sc.level_ret)
    atr = sc.atr_frac
    return (
        base
        & np.isfinite(abs_lr)
        & np.isfinite(atr)
        & (abs_lr >= 0.8 * atr)
        & (abs_lr <= 1.5 * atr)
    )


def main() -> int:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out_dir = ARTIFACTS / "reports" / "pivot_forecast"
    out_dir.mkdir(parents=True, exist_ok=True)
    print(f"fleet improve 003 stamp={stamp}", flush=True)

    leak = []
    for sym in ("BTCUSDT", "ETHUSDT", "SOLUSDT"):
        for pack in (PACK, "level_strong"):
            leak.append(_leak(sym, pack, "15m"))
        leak.append(_leak(sym, PACK, "1h"))
    for x in leak:
        print(f"  leakage {x['symbol']} {x['tf']} {x['pack']}: {x['status']}", flush=True)
    if any(x["status"] != "PASS" for x in leak):
        print("LEAKAGE FAIL", flush=True)
        return 2

    freeze_doc = {
        "stamp": stamp,
        "preregister": "configs/preregister/pivot_fleet_improve_003.yaml",
        "research_fleet": ["ETH_q50_w4", "SOL_atr_clip_w5", "BTC_p80_w4"],
        "not_live": True,
        "no_finplot": True,
        "ranking": "expectancy_intent_all",
    }
    freeze_path = out_dir / f"fleet_improve_003_freeze_{stamp}.json"
    freeze_path.write_text(json.dumps(freeze_doc, indent=2), encoding="utf-8")
    print(f"WROTE {freeze_path}", flush=True)

    report: dict = {
        "generation_id": "pivot_fleet_improve_003",
        "stamp": stamp,
        "readiness_max": "RESEARCH_ONLY",
        "not_live": True,
        "freeze_path": str(freeze_path),
        "leakage": leak,
        "fleet": {},
        "symbols": {},
        "updated_fleet_picks": {},
    }

    # ---------- BTC ----------
    print("SCORE BTC 15m ret …", flush=True)
    btc = score_symbol_oos(
        "BTCUSDT",
        timeframe="15m",
        horizon_bars=4,
        feature_pack=PACK,
        max_rows=MAX_ROWS,
        level_mode="ret",
        atr_min=2.0,
    )
    print("SCORE BTC 15m level_strong …", flush=True)
    btc_s = score_symbol_oos(
        "BTCUSDT",
        timeframe="15m",
        horizon_bars=4,
        feature_pack="level_strong",
        max_rows=MAX_ROWS,
        level_mode="ret",
        atr_min=2.0,
    )
    print("SCORE BTC 1h ret atr_min=1.0 …", flush=True)
    btc_1h = score_symbol_oos(
        "BTCUSDT",
        timeframe="1h",
        horizon_bars=2,
        feature_pack=PACK,
        max_rows=MAX_ROWS,
        level_mode="ret",
        atr_min=1.0,
    )
    d_btc, d_btc_s, d_btc_1h = _diag(btc), _diag(btc_s), _diag(btc_1h)
    base = gate_mask(btc, mode="p75", tp=TP, sl=SL)
    mid_gates = _mid_density_gates(btc, base)
    arms_btc = []
    thr_map = {}
    # raw P75 control + interpolated mid-density + fleet p80
    for key, tag in (
        ("p75_raw", "BTC_p75_raw_w4"),
        ("p76", "BTC_p76_w4"),
        ("p77", "BTC_p77_w4"),
        ("p78", "BTC_p78_w4"),
        ("p79", "BTC_p79_w4"),
        ("p80", "BTC_p80_w4"),
    ):
        m, thr = mid_gates[key]
        thr_map[tag] = thr
        arms_btc.append(_run("BTCUSDT", btc, m, tag=tag, work=4))
    fleet_btc = next(a for a in arms_btc if a["tag"] == "BTC_p80_w4")
    mid_s = _mid_density_gates(btc_s, gate_mask(btc_s, mode="p75", tp=TP, sl=SL))
    arms_btc.append(
        _run("BTCUSDT", btc_s, mid_s["p80"][0], tag="BTC_level_strong_p80_w4", work=4)
    )
    b1 = gate_mask(btc_1h, mode="p75", tp=TP, sl=SL)
    mid_1h = _mid_density_gates(btc_1h, b1)
    arms_btc.append(_run("BTCUSDT", btc_1h, b1, tag="BTC_1h_p75_w2", work=2))
    arms_btc.append(_run("BTCUSDT", btc_1h, mid_1h["p80"][0], tag="BTC_1h_p80_w2", work=2))

    prom_btc = {}
    for a in arms_btc:
        if a["tag"] == "BTC_p80_w4":
            continue
        ece_ok = True
        if "level_strong" in a["tag"]:
            ece_ok = float(d_btc_s["ece"]) <= float(d_btc["ece"]) * 1.02 + 1e-9
        # 1h is structure trial — allow ECE scale diff but enforce entry-bar cap
        prom_btc[a["tag"]] = _promote(fleet_btc, a, ece_ok=ece_ok, max_entry_bar=0.35)

    rank_btc = _rank(arms_btc)
    # pick: promote_volume else promote else fleet
    vol = [a for a in arms_btc if prom_btc.get(a["tag"], {}).get("promote_volume")]
    if vol:
        pick_btc = sorted(vol, key=lambda a: -float(a.get("net_pnl") or -1e9))[0]["tag"]
    else:
        prom = [a for a in arms_btc if prom_btc.get(a["tag"], {}).get("promote")]
        pick_btc = (
            sorted(prom, key=lambda a: -float(a.get("expectancy_intent_all") or -1e9))[0]["tag"]
            if prom
            else "BTC_p80_w4"
        )
    report["symbols"]["BTCUSDT"] = {
        "fleet_tag": "BTC_p80_w4",
        "diagnostics": d_btc,
        "diagnostics_level_strong": d_btc_s,
        "diagnostics_1h": d_btc_1h,
        "thr_map": thr_map,
        "arms": arms_btc,
        "ranking_by_intent_expectancy": rank_btc,
        "promotions_vs_fleet": prom_btc,
        "pick": pick_btc,
    }
    report["fleet"]["BTCUSDT"] = fleet_btc
    print(f"  PICK BTC: {pick_btc}", flush=True)

    # ---------- ETH ----------
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
    print("SCORE ETH q50 level_strong …", flush=True)
    eth_s = score_symbol_oos(
        "ETHUSDT",
        timeframe="15m",
        horizon_bars=4,
        feature_pack="level_strong",
        max_rows=MAX_ROWS,
        level_mode="q50",
        atr_min=2.0,
    )
    d_eth, d_eth_s = _diag(eth), _diag(eth_s)
    ebase = gate_mask(eth, mode="p75", tp=TP, sl=SL)
    vsa_e, thr_vsa_e = _soft_vsa_mask(eth, ebase)
    arms_eth = [
        _run("ETHUSDT", eth, ebase, tag="ETH_q50_w4", work=4),
        _run("ETHUSDT", eth, ebase & vsa_e, tag="ETH_q50_softvsa_w4", work=4),
        _run("ETHUSDT", eth, ebase, tag="ETH_q50_w5", work=5),
        _run(
            "ETHUSDT",
            eth_s,
            gate_mask(eth_s, mode="p75", tp=TP, sl=SL),
            tag="ETH_q50_level_strong_w4",
            work=4,
        ),
        _run("ETHUSDT", eth, _mid_atr(eth, ebase), tag="ETH_q50_mid_atr_w4", work=4),
    ]
    fleet_eth = next(a for a in arms_eth if a["tag"] == "ETH_q50_w4")
    prom_eth = {}
    for a in arms_eth:
        if a["tag"] == "ETH_q50_w4":
            continue
        ece_ok = True
        if "level_strong" in a["tag"]:
            ece_ok = float(d_eth_s["ece"]) <= float(d_eth["ece"]) * 1.02 + 1e-9
        prom_eth[a["tag"]] = _promote(fleet_eth, a, ece_ok=ece_ok)
    rank_eth = _rank(arms_eth)
    vol = [a for a in arms_eth if prom_eth.get(a["tag"], {}).get("promote_volume")]
    if vol:
        pick_eth = sorted(vol, key=lambda a: -float(a.get("net_pnl") or -1e9))[0]["tag"]
    else:
        prom_list = [a for a in arms_eth if prom_eth.get(a["tag"], {}).get("promote")]
        pick_eth = (
            sorted(
                prom_list, key=lambda a: -float(a.get("expectancy_intent_all") or -1e9)
            )[0]["tag"]
            if prom_list
            else "ETH_q50_w4"
        )
    report["symbols"]["ETHUSDT"] = {
        "fleet_tag": "ETH_q50_w4",
        "diagnostics": d_eth,
        "diagnostics_level_strong": d_eth_s,
        "soft_vsa_thr": thr_vsa_e,
        "arms": arms_eth,
        "ranking_by_intent_expectancy": rank_eth,
        "promotions_vs_fleet": prom_eth,
        "pick": pick_eth,
    }
    report["fleet"]["ETHUSDT"] = fleet_eth
    print(f"  PICK ETH: {pick_eth}", flush=True)

    # ---------- SOL ----------
    print("SCORE SOL ret …", flush=True)
    sol = score_symbol_oos(
        "SOLUSDT",
        timeframe="15m",
        horizon_bars=4,
        feature_pack=PACK,
        max_rows=MAX_ROWS,
        level_mode="ret",
        atr_min=2.0,
    )
    print("SCORE SOL level_strong …", flush=True)
    sol_s = score_symbol_oos(
        "SOLUSDT",
        timeframe="15m",
        horizon_bars=4,
        feature_pack="level_strong",
        max_rows=MAX_ROWS,
        level_mode="ret",
        atr_min=2.0,
    )
    print("SCORE SOL 1h …", flush=True)
    sol_1h = score_symbol_oos(
        "SOLUSDT",
        timeframe="1h",
        horizon_bars=2,
        feature_pack=PACK,
        max_rows=MAX_ROWS,
        level_mode="ret",
        atr_min=1.0,
    )
    d_sol, d_sol_s, d_sol_1h = _diag(sol), _diag(sol_s), _diag(sol_1h)
    sbase = gate_mask(sol, mode="p75", tp=TP, sl=SL)
    clip = _atr_clip_level(sol)
    clip_s = _atr_clip_level(sol_s)
    clip_1h = _atr_clip_level(sol_1h)
    vsa_s, thr_vsa_s = _soft_vsa_mask(sol, sbase)
    arms_sol = [
        _run("SOLUSDT", sol, sbase, tag="SOL_atr_clip_w5", work=5, level_override=clip),
        _run("SOLUSDT", sol, sbase, tag="SOL_atr_clip_w4", work=4, level_override=clip),
        _run(
            "SOLUSDT",
            sol,
            sbase & vsa_s,
            tag="SOL_atr_clip_softvsa_w5",
            work=5,
            level_override=clip,
        ),
        _run(
            "SOLUSDT",
            sol_s,
            gate_mask(sol_s, mode="p75", tp=TP, sl=SL),
            tag="SOL_atr_clip_level_strong_w5",
            work=5,
            level_override=clip_s,
        ),
        _run(
            "SOLUSDT",
            sol_1h,
            gate_mask(sol_1h, mode="p75", tp=TP, sl=SL),
            tag="SOL_1h_atr_clip_w2",
            work=2,
            level_override=clip_1h,
        ),
    ]
    fleet_sol = next(a for a in arms_sol if a["tag"] == "SOL_atr_clip_w5")
    prom_sol = {}
    for a in arms_sol:
        if a["tag"] == "SOL_atr_clip_w5":
            continue
        ece_ok = True
        if "level_strong" in a["tag"]:
            ece_ok = float(d_sol_s["ece"]) <= float(d_sol["ece"]) * 1.02 + 1e-9
        prom_sol[a["tag"]] = _promote(fleet_sol, a, ece_ok=ece_ok, max_entry_bar=0.35)
    rank_sol = _rank(arms_sol)
    vol = [a for a in arms_sol if prom_sol.get(a["tag"], {}).get("promote_volume")]
    # for 1h, also require entry_bar not worse than 15m fleet by much if promoting volume
    pick_sol = "SOL_atr_clip_w5"
    if vol:
        pick_sol = sorted(vol, key=lambda a: -float(a.get("net_pnl") or -1e9))[0]["tag"]
    else:
        prom = [a for a in arms_sol if prom_sol.get(a["tag"], {}).get("promote")]
        if prom:
            pick_sol = sorted(
                prom, key=lambda a: -float(a.get("expectancy_intent_all") or -1e9)
            )[0]["tag"]

    report["symbols"]["SOLUSDT"] = {
        "fleet_tag": "SOL_atr_clip_w5",
        "diagnostics": d_sol,
        "diagnostics_level_strong": d_sol_s,
        "diagnostics_1h": d_sol_1h,
        "soft_vsa_thr": thr_vsa_s,
        "arms": arms_sol,
        "ranking_by_intent_expectancy": rank_sol,
        "promotions_vs_fleet": prom_sol,
        "pick": pick_sol,
    }
    report["fleet"]["SOLUSDT"] = fleet_sol
    print(f"  PICK SOL: {pick_sol}", flush=True)

    report["updated_fleet_picks"] = {
        "BTCUSDT": pick_btc,
        "ETHUSDT": pick_eth,
        "SOLUSDT": pick_sol,
    }

    path = out_dir / f"fleet_improve_003_{stamp}.json"
    latest = out_dir / "fleet_improve_003_latest.json"
    path.write_text(json.dumps(report, indent=2, default=str), encoding="utf-8")
    latest.write_text(path.read_text(encoding="utf-8"), encoding="utf-8")
    md = out_dir / f"fleet_improve_003_{stamp}.md"
    md.write_text(_md(report), encoding="utf-8")
    print(f"WROTE {path}", flush=True)
    print(f"UPDATED FLEET: {report['updated_fleet_picks']}", flush=True)
    try:
        print(_md(report), flush=True)
    except UnicodeEncodeError:
        pass
    return 0


def _md(r: dict) -> str:
    lines = [
        f"# Fleet improve 003 (`{r['stamp']}`)",
        "",
        f"**{r['readiness_max']}** — not live; no Finplot",
        "",
        f"**Updated fleet picks:** `{r.get('updated_fleet_picks')}`",
        "",
    ]
    for sym, block in r["symbols"].items():
        d = block["diagnostics"]
        lines.append(f"## {sym} (fleet=`{block['fleet_tag']}` → pick=`{block['pick']}`)")
        lines.append(
            f"lift={d['pr_auc_lift']:.4f} ece={d['ece']:.4f} level_p90={d['level_p90']:.4f}"
        )
        lines.append("")
        lines.append("| rank | tag | intent_exp | PF | WR | n | fill% | pnl | ebr% |")
        lines.append("|---:|---|---:|---:|---:|---:|---:|---:|---:|")
        for row in block["ranking_by_intent_expectancy"]:
            lines.append(
                f"| {row['rank']} | {row['tag']} | {row['expectancy_intent_all']:.5f} | "
                f"{row['profit_factor']:.3f} | {row['win_rate']:.3f} | {row['n_trades']} | "
                f"{100*float(row['fill_pct']):.1f}% | {row['net_pnl']:.2f} | "
                f"{100*float(row.get('entry_bar_exit_rate') or float('nan')):.1f}% |"
            )
        lines.append("")
        for k, v in block["promotions_vs_fleet"].items():
            lines.append(
                f"- `{k}`: promote={v.get('promote')} volume={v.get('promote_volume')}"
            )
        lines.append("")
    return "\n".join(lines)


if __name__ == "__main__":
    raise SystemExit(main())
