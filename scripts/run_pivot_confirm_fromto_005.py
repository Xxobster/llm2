"""Fleet 005: pivot confirmation, confidence sizing, from→to next pivot.

RESEARCH_ONLY. Not live. Rank by intent expectancy. Cap entry-bar exit rate at 35%.
Oracle next-pivot take-profit is diagnostic only and cannot promote.
"""

from __future__ import annotations

import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

os.environ.setdefault("TRADESIM_NO_PLOT", "1")

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
from llm2.pivot.strategy.confidence_size import size_mult_linear, size_mult_tertile  # noqa: E402
from llm2.pivot.strategy.confirm_addon import (  # noqa: E402
    addon_signals_after_fill,
    delay_intents_until_confirm,
)
from llm2.pivot.strategy.score_oos import gate_mask, limit_price_side, score_symbol_oos  # noqa: E402
from llm2.pivot.strategy.working_limit import LimitIntent, materialize_working_limits  # noqa: E402
from llm2.validation.folds import index_to_ms  # noqa: E402

PACK = "level_vsa"
MAX_ROWS = 120_000
EBR_CAP = 0.35
PREREG = "configs/preregister/pivot_confirm_fromto_005.yaml"


def _leak(symbol: str, tf: str) -> dict:
    from leakage import require_clean_audit, run_leakage_audit

    try:
        ohlcv = load_ohlcv(symbol, tf)
        lock = pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC")
        ohlcv = ohlcv.loc[ohlcv.index < lock].iloc[-6000:].copy()

        def _b(df, **_k):
            return build_feature_frame(df, pack=PACK)

        require_clean_audit(
            run_leakage_audit(
                ohlcv=ohlcv, build_features=_b, interval=tf, symbol=symbol, timeframe=tf
            )
        )
        return {"symbol": symbol, "tf": tf, "pack": PACK, "status": "PASS"}
    except Exception as exc:  # noqa: BLE001
        return {"symbol": symbol, "tf": tf, "status": "FAIL", "error": str(exc)[:300]}


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


def _atr_clip(sc, lo=0.8, hi=1.5) -> np.ndarray:
    lr = np.asarray(sc.level_ret, dtype=float)
    atr = np.asarray(sc.atr_frac, dtype=float)
    out = np.sign(lr) * np.clip(np.abs(lr), lo * atr, hi * atr)
    out[~np.isfinite(lr) | ~np.isfinite(atr)] = np.nan
    return out


def _span_months(ohlcv: pd.DataFrame) -> float:
    if ohlcv is None or len(ohlcv) < 2:
        return float("nan")
    days = float((ohlcv.index[-1] - ohlcv.index[0]).total_seconds() / 86400.0)
    return days / 30.44 if days > 0 else float("nan")


def _bt(symbol, tf, ohlcv, signals, *, tag: str, max_hold: int, sl: float, concurrent: bool):
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
    sl_use = max(
        float(sl),
        max((float(getattr(s, "stop_offset", sl) or sl) for s in signals), default=sl),
    )
    sim_kw = dict(max_hold_bars=max_hold, decision_timeframe=tf)
    if concurrent:
        sim_kw["allow_concurrent_positions"] = True
        sim_kw["max_positions_per_symbol"] = 2
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
        sim=research_sim_limit_entry(**sim_kw),
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
    skip_counts = dict(getattr(m, "skip_counts", {}) or {})
    size_sum = 0.0
    n_sz = 0
    for t in trades:
        meta = getattr(t, "meta", None) or {}
        if isinstance(meta, dict) and "size_mult" in meta:
            size_sum += float(meta["size_mult"] or 1.0)
            n_sz += 1
    months = _span_months(ohlcv)
    n_tr = int(m.n_trades)
    return {
        "status": "RAN",
        "n_trades": n_tr,
        "profit_factor": float(m.profit_factor),
        "win_rate": float(m.win_rate),
        "net_pnl": float(m.net_pnl),
        "expectancy": float(m.expectancy),
        "entry_bar_exit_rate": ebr,
        "skip_counts": {str(k): int(v) for k, v in skip_counts.items()},
        "n_skip_position_limit": int(skip_counts.get("SKIP_POSITION_LIMIT", 0)),
        "size_mult_sum_filled": float(size_sum) if n_sz else float(n_tr),
        "trades_per_month": float(n_tr / months) if months and np.isfinite(months) else float("nan"),
    }


def _from_to_tp(is_short: bool, close: float, lim: float, to_ret: float) -> float | None:
    to_px = float(close) * (1.0 + float(to_ret))
    if not np.isfinite(to_px) or lim <= 0:
        return None
    if is_short:
        if to_px >= lim * 0.997:
            return None
        tp = (lim - to_px) / lim
    else:
        if to_px <= lim * 1.003:
            return None
        tp = (to_px - lim) / lim
    if not np.isfinite(tp) or tp < 0.003:
        return None
    return float(np.clip(tp, 0.003, 0.08))


def _make_intents(
    sc,
    mask: np.ndarray,
    *,
    work: int,
    tp: float,
    sl: float,
    level_override=None,
    tp_mode: str = "fixed",
    size_mult: np.ndarray | None = None,
    size_meta_key: str = "size_mult",
):
    n_gated = int(mask.sum())
    if n_gated < 15:
        return None, {"status": "TOO_FEW_GATED", "n_intent": n_gated}
    if level_override is not None:
        old = sc.level_ret
        sc.level_ret = level_override
        ts, is_short, lim = limit_price_side(sc, mask)
        sc.level_ret = old
    else:
        ts, is_short, lim = limit_price_side(sc, mask)
    idx = np.flatnonzero(mask)
    h = int(getattr(sc, "horizon_bars", 4) or 4)
    max_hold_def = h + 2
    nxt = sc.next_level_ret
    nxt_t = sc.next_time_bars
    y_nxt = sc.y_next_level
    y_nxt_t = sc.y_next_time
    lr = np.asarray(sc.level_ret, dtype=float)
    intents: list[LimitIntent] = []
    n_skip_geom = 0
    for j, i in enumerate(idx):
        sl_j = float(sl)
        tp_j = float(tp)
        mh = max_hold_def
        if tp_mode == "abs_level":
            tp_j = float(np.clip(abs(float(lr[i])), 0.005, 0.03))
        elif tp_mode == "2x_level":
            abs_lr = float(np.clip(abs(float(lr[i])), 0.005, 0.03))
            tp_j = float(np.clip(2.0 * abs_lr, 0.005, 0.08))
            sl_j = abs_lr
        elif tp_mode in {"pred_next", "oracle_next"}:
            src = y_nxt if tp_mode == "oracle_next" else nxt
            if src is None:
                n_skip_geom += 1
                continue
            to_ret = float(src[i]) if np.isfinite(src[i]) else float("nan")
            tp_use = _from_to_tp(bool(is_short[j]), float(sc.close[i]), float(lim[j]), to_ret)
            if tp_use is None:
                n_skip_geom += 1
                continue
            tp_j = tp_use
            tsrc = y_nxt_t if tp_mode == "oracle_next" else nxt_t
            if tsrc is not None and np.isfinite(tsrc[i]):
                mh = int(np.clip(int(round(float(tsrc[i]))) + 2, 4, 16))
        sl_j = float(np.clip(sl_j, 0.005, 0.05))
        tp_j = float(np.clip(tp_j, 0.005, 0.08))
        meta = {}
        if size_mult is not None:
            meta[str(size_meta_key)] = float(np.clip(size_mult[i], 0.5, 2.0))
        intents.append(
            LimitIntent(
                decision_ts_ms=int(ts[j]),
                side=Side.SHORT if is_short[j] else Side.LONG,
                limit_price=float(lim[j]),
                stop_offset=sl_j,
                target_offset=tp_j,
                max_hold_bars=mh,
                work_bars=work,
                meta=meta or None,
            )
        )
    extra = {"n_skip_geom": n_skip_geom, "n_gated": n_gated}
    return intents, extra


def _run_intents(
    symbol,
    sc,
    intents,
    *,
    tag: str,
    work: int,
    sl: float,
    n_intent: int,
    concurrent: bool = False,
    addon_k: int | None = None,
    extra: dict | None = None,
):
    if intents is None or len(intents) < 12:
        return {
            "tag": tag,
            "status": "TOO_FEW_GATED",
            "n_intent": n_intent,
            **(extra or {}),
        }
    sigs, fill = materialize_working_limits(sc.ohlcv, intents, work_bars=work)
    addon_stats = None
    if addon_k is not None:
        add, addon_stats = addon_signals_after_fill(sc.ohlcv, sigs, confirm_k=int(addon_k))
        sigs = list(sigs) + list(add)
        concurrent = True
    max_hold = max((int(it.max_hold_bars) for it in intents), default=6)
    print(
        f"  BT {tag} intent={n_intent} path_fill={fill['n_filled_path']} "
        f"fill%={100 * float(fill['fill_rate']):.1f}"
        + (f" addon={addon_stats['n_addon']}" if addon_stats else ""),
        flush=True,
    )
    res = _bt(
        symbol,
        sc.timeframe,
        sc.ohlcv,
        sigs,
        tag=tag,
        max_hold=max_hold,
        sl=sl,
        concurrent=concurrent,
    )
    out = {
        "tag": tag,
        "n_intent": n_intent,
        "fill_pct": float(fill["fill_rate"]),
        "fill_stats": fill,
        "addon_stats": addon_stats,
        **(extra or {}),
        **res,
    }
    if res.get("status") == "RAN":
        out["expectancy_intent_all"] = float(res["net_pnl"]) / max(n_intent, 1)
        sz = float(res.get("size_mult_sum_filled") or res["n_trades"] or 1)
        out["expectancy_per_size"] = float(res["net_pnl"]) / max(sz, 1e-9)
        print(
            f"    n={res['n_trades']} PF={res['profit_factor']:.3f} WR={res['win_rate']:.3f} "
            f"pnl={res['net_pnl']:.2f} exp_i={out['expectancy_intent_all']:.5f} "
            f"ebr={100 * float(res['entry_bar_exit_rate']):.1f}% "
            f"pos_skip={res.get('n_skip_position_limit', 0)}",
            flush=True,
        )
    return out


def _run_family(symbol: str, sc, mask: np.ndarray, *, prefix: str, work: int, level_override=None):
    """Control + frozen 005 arms on one scored book."""
    rows = []
    base_intents, extra0 = _make_intents(
        sc, mask, work=work, tp=0.01, sl=0.01, level_override=level_override
    )
    n_intent = int(mask.sum())
    ctrl = _run_intents(
        symbol,
        sc,
        base_intents,
        tag=f"{prefix}_ctrl",
        work=work,
        sl=0.01,
        n_intent=n_intent,
        extra=extra0 if isinstance(extra0, dict) else None,
    )
    rows.append(ctrl)

    sm_lin = size_mult_linear(sc.p_any, sc.thr_any)
    lin_intents, ex = _make_intents(
        sc,
        mask,
        work=work,
        tp=0.01,
        sl=0.01,
        level_override=level_override,
        size_mult=sm_lin,
    )
    rows.append(
        _run_intents(
            symbol,
            sc,
            lin_intents,
            tag=f"{prefix}_size_linear",
            work=work,
            sl=0.01,
            n_intent=n_intent,
            extra=ex if isinstance(ex, dict) else None,
        )
    )
    sm_ter, ter_info = size_mult_tertile(sc.p_any, mask)
    ter_intents, ex = _make_intents(
        sc,
        mask,
        work=work,
        tp=0.01,
        sl=0.01,
        level_override=level_override,
        size_mult=sm_ter,
    )
    rows.append(
        _run_intents(
            symbol,
            sc,
            ter_intents,
            tag=f"{prefix}_size_tertile",
            work=work,
            sl=0.01,
            n_intent=n_intent,
            extra={"tertile": ter_info, **(ex if isinstance(ex, dict) else {})},
        )
    )

    for k in (1, 2, 3):
        delayed, dst = delay_intents_until_confirm(sc.ohlcv, base_intents or [], confirm_k=k)
        rows.append(
            _run_intents(
                symbol,
                sc,
                delayed,
                tag=f"{prefix}_confirm_enter_k{k}",
                work=work,
                sl=0.01,
                n_intent=n_intent,
                extra={"confirm_stats": dst, "n_confirmed": len(delayed)},
            )
        )
        addon_intents, _ex_a = _make_intents(
            sc,
            mask,
            work=work,
            tp=0.01,
            sl=0.01,
            level_override=level_override,
            size_mult=sm_lin,
            size_meta_key="addon_size_mult",
        )
        rows.append(
            _run_intents(
                symbol,
                sc,
                addon_intents,
                tag=f"{prefix}_confirm_addon_k{k}",
                work=work,
                sl=0.01,
                n_intent=n_intent,
                addon_k=k,
            )
        )

    for mode, tag_s in (
        ("abs_level", "fromto_abs_level"),
        ("2x_level", "fromto_2x_level"),
        ("pred_next", "fromto_pred_next"),
        ("oracle_next", "fromto_oracle_next"),
    ):
        intents, ex = _make_intents(
            sc,
            mask,
            work=work,
            tp=0.01,
            sl=0.01,
            level_override=level_override,
            tp_mode=mode,
        )
        n_use = len(intents) if intents is not None else 0
        rows.append(
            _run_intents(
                symbol,
                sc,
                intents,
                tag=f"{prefix}_{tag_s}",
                work=work,
                sl=0.01,
                n_intent=n_use,
                extra={**(ex if isinstance(ex, dict) else {}), "tp_mode": mode, "promote_blocked": mode == "oracle_next"},
            )
        )
    return rows


def _promote(ref: dict, arm: dict) -> dict:
    if arm.get("promote_blocked"):
        return {"promote": False, "reason": "oracle_or_blocked"}
    if arm.get("status") != "RAN" or ref.get("status") != "RAN":
        return {"promote": False, "reason": "not_ran"}
    ebr = float(arm.get("entry_bar_exit_rate") or float("nan"))
    ebr_ok = np.isfinite(ebr) and ebr <= EBR_CAP
    exp_ok = float(arm.get("expectancy_intent_all") or -1e9) > float(
        ref.get("expectancy_intent_all") or -1e9
    )
    pf_ok = float(arm.get("profit_factor") or 0) >= 0.85 * float(ref.get("profit_factor") or 1)
    size_ok = True
    if "size_" in str(arm.get("tag", "")):
        size_ok = float(arm.get("expectancy_per_size") or -1e9) >= 0.95 * float(
            ref.get("expectancy_per_size") or ref.get("expectancy") or -1e9
        )
    return {
        "entry_bar_ok": bool(ebr_ok),
        "intent_exp_improved": bool(exp_ok),
        "pf_not_collapsed": bool(pf_ok),
        "size_not_fake": bool(size_ok),
        "promote": bool(ebr_ok and exp_ok and pf_ok and size_ok),
        "entry_bar_exit_rate": ebr,
    }


def _level_diag(sc) -> dict:
    p90 = np.asarray(sc.level_p90_train, dtype=float)
    nxt_p90 = sc.next_level_p90_train
    return {
        "confirm_bars": int(getattr(sc, "confirm_bars", 3)),
        "frac_any": float(sc.frac_any),
        "frac_next": float(getattr(sc, "frac_next", float("nan"))),
        "level_p90_mean": float(np.nanmean(p90)) if p90.size else float("nan"),
        "next_level_p90_mean": float(np.nanmean(nxt_p90))
        if nxt_p90 is not None and np.size(nxt_p90)
        else float("nan"),
        "n_rows": int(sc.n_rows),
    }


def main() -> int:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out_dir = ARTIFACTS / "reports" / "pivot_forecast"
    out_dir.mkdir(parents=True, exist_ok=True)
    print(f"fleet 005 stamp={stamp}", flush=True)

    leak = [_leak("ETHUSDT", "15m"), _leak("SOLUSDT", "15m"), _leak("BTCUSDT", "15m")]
    for x in leak:
        print(f"  leakage {x['symbol']} {x['tf']}: {x['status']}", flush=True)
    if any(x["status"] != "PASS" for x in leak):
        return 2

    freeze = {
        "stamp": stamp,
        "preregister": PREREG,
        "ebr_cap": EBR_CAP,
        "arms_frozen_before_pf": [
            "ctrl",
            "size_linear",
            "size_tertile",
            "confirm_enter_k1",
            "confirm_enter_k2",
            "confirm_enter_k3",
            "confirm_addon_k1",
            "confirm_addon_k2",
            "confirm_addon_k3",
            "fromto_abs_level",
            "fromto_2x_level",
            "fromto_pred_next",
            "fromto_oracle_next",
            "ETH_label_confirm_4",
            "ETH_label_confirm_5",
        ],
    }
    freeze_path = out_dir / f"fleet_005_freeze_{stamp}.json"
    freeze_path.write_text(json.dumps(freeze, indent=2), encoding="utf-8")
    print(f"WROTE {freeze_path}", flush=True)

    print("SCORE ETH q50 confirm=3 (next head on) …", flush=True)
    eth3 = score_symbol_oos(
        "ETHUSDT",
        timeframe="15m",
        horizon_bars=4,
        feature_pack=PACK,
        max_rows=MAX_ROWS,
        level_mode="q50",
        confirm_bars=3,
        predict_next=True,
    )
    print("SCORE ETH q50 confirm=4 …", flush=True)
    eth4 = score_symbol_oos(
        "ETHUSDT",
        timeframe="15m",
        horizon_bars=4,
        feature_pack=PACK,
        max_rows=MAX_ROWS,
        level_mode="q50",
        confirm_bars=4,
        predict_next=False,
    )
    print("SCORE ETH q50 confirm=5 …", flush=True)
    eth5 = score_symbol_oos(
        "ETHUSDT",
        timeframe="15m",
        horizon_bars=4,
        feature_pack=PACK,
        max_rows=MAX_ROWS,
        level_mode="q50",
        confirm_bars=5,
        predict_next=False,
    )
    print("SCORE SOL ret confirm=3 …", flush=True)
    sol = score_symbol_oos(
        "SOLUSDT",
        timeframe="15m",
        horizon_bars=4,
        feature_pack=PACK,
        max_rows=MAX_ROWS,
        level_mode="ret",
        confirm_bars=3,
        predict_next=True,
    )
    print("SCORE BTC ret confirm=3 …", flush=True)
    btc = score_symbol_oos(
        "BTCUSDT",
        timeframe="15m",
        horizon_bars=4,
        feature_pack=PACK,
        max_rows=MAX_ROWS,
        level_mode="ret",
        confirm_bars=3,
        predict_next=True,
    )

    ebase = gate_mask(eth3, mode="p75", tp=0.01, sl=0.01)
    sbase = gate_mask(sol, mode="p75", tp=0.01, sl=0.01)
    bmask, bthr = _p80_mask(btc)

    print("FAMILY ETH …", flush=True)
    eth_arms = _run_family("ETHUSDT", eth3, ebase, prefix="ETH_q50", work=4)
    print("FAMILY SOL …", flush=True)
    sol_arms = _run_family(
        "SOLUSDT", sol, sbase, prefix="SOL_atrclip", work=5, level_override=_atr_clip(sol)
    )
    print("FAMILY BTC …", flush=True)
    btc_arms = _run_family("BTCUSDT", btc, bmask, prefix="BTC_p80", work=4)

    print("ETH label-confirm 4/5 controls …", flush=True)
    e4 = gate_mask(eth4, mode="p75", tp=0.01, sl=0.01)
    e5 = gate_mask(eth5, mode="p75", tp=0.01, sl=0.01)
    eth4_ctrl_i, ex4 = _make_intents(eth4, e4, work=4, tp=0.01, sl=0.01)
    eth5_ctrl_i, ex5 = _make_intents(eth5, e5, work=4, tp=0.01, sl=0.01)
    eth4_arm = _run_intents(
        "ETHUSDT", eth4, eth4_ctrl_i, tag="ETH_q50_label_confirm_4", work=4, sl=0.01, n_intent=int(e4.sum()), extra=ex4
    )
    eth5_arm = _run_intents(
        "ETHUSDT", eth5, eth5_ctrl_i, tag="ETH_q50_label_confirm_5", work=4, sl=0.01, n_intent=int(e5.sum()), extra=ex5
    )

    def _pack(arms, ref_tag_suffix="_ctrl"):
        ref = next((a for a in arms if str(a.get("tag", "")).endswith(ref_tag_suffix)), arms[0])
        return {
            "control": ref,
            "arms": arms,
            "promotions": {a["tag"]: _promote(ref, a) for a in arms if a is not ref},
        }

    report = {
        "generation_id": "pivot_confirm_fromto_005",
        "stamp": stamp,
        "readiness_max": "RESEARCH_ONLY",
        "not_live": True,
        "freeze_path": str(freeze_path),
        "preregister": PREREG,
        "leakage": leak,
        "btc_p80_thr": bthr,
        "eth": _pack(eth_arms),
        "sol": _pack(sol_arms),
        "btc": _pack(btc_arms),
        "eth_label_confirm": {
            "confirm_3": {"diag": _level_diag(eth3), "arm": eth_arms[0]},
            "confirm_4": {"diag": _level_diag(eth4), "arm": eth4_arm},
            "confirm_5": {"diag": _level_diag(eth5), "arm": eth5_arm},
        },
    }
    promoted = []
    for book in ("eth", "sol", "btc"):
        for tag, p in report[book]["promotions"].items():
            if p.get("promote"):
                promoted.append(tag)
    report["promoted"] = promoted

    path = out_dir / f"fleet_005_{stamp}.json"
    latest = out_dir / "fleet_005_latest.json"
    path.write_text(json.dumps(report, indent=2, default=str), encoding="utf-8")
    latest.write_text(path.read_text(encoding="utf-8"), encoding="utf-8")
    md = out_dir / f"fleet_005_{stamp}.md"
    md.write_text(_md(report), encoding="utf-8")
    (out_dir / "fleet_005_latest.md").write_text(md.read_text(encoding="utf-8"), encoding="utf-8")
    print(f"WROTE {path}", flush=True)
    try:
        print(_md(report), flush=True)
    except UnicodeEncodeError:
        pass
    return 0


def _row(a: dict) -> str:
    if a.get("status") != "RAN":
        return f"| {a.get('tag')} | {a.get('status')} | — | — | — | — | — | — |"
    return (
        f"| {a['tag']} | {a.get('n_intent')} | {a['n_trades']} | {a['profit_factor']:.3f} | "
        f"{a['win_rate']:.3f} | {a['net_pnl']:.2f} | {a.get('expectancy_intent_all', float('nan')):.5f} | "
        f"{100 * float(a['entry_bar_exit_rate']):.1f}% |"
    )


def _md(r: dict) -> str:
    lines = [
        f"# Fleet 005 confirm / from-to (`{r['stamp']}`)",
        "",
        f"**{r['readiness_max']}** — not live. Rank by intent expectancy. Entry-bar cap 35%.",
        "",
        f"**Promoted:** `{r.get('promoted')}`",
        "",
        "## ETH 15m q50 (volume control)",
        "",
        "| tag | n_intent | n | PF | WR | pnl | exp_i | ebr% |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for a in r["eth"]["arms"]:
        lines.append(_row(a))
    lines += [
        "",
        "## SOL 15m atr-clip w5",
        "",
        "| tag | n_intent | n | PF | WR | pnl | exp_i | ebr% |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for a in r["sol"]["arms"]:
        lines.append(_row(a))
    lines += [
        "",
        "## BTC 15m p80",
        "",
        "| tag | n_intent | n | PF | WR | pnl | exp_i | ebr% |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for a in r["btc"]["arms"]:
        lines.append(_row(a))
    lines += ["", "## ETH label confirm_bars sweep (right_bars=3)", ""]
    for key in ("confirm_3", "confirm_4", "confirm_5"):
        d = r["eth_label_confirm"][key]["diag"]
        a = r["eth_label_confirm"][key]["arm"]
        lines.append(
            f"- **{key}**: frac_any={d['frac_any']:.3f} level_P90={d['level_p90_mean']:.4f} "
            f"n={a.get('n_trades')} PF={a.get('profit_factor')} exp_i={a.get('expectancy_intent_all')} "
            f"ebr={a.get('entry_bar_exit_rate')}"
        )
    return "\n".join(lines)


if __name__ == "__main__":
    raise SystemExit(main())
