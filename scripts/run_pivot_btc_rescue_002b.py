"""BTC-only rescue pass after 002 (ctrl barely PF~1.02; placement hurt).

Frozen before PF: soft VSA, p80, tp2/sl1, mid-band quality, pi* diagnostic.
RESEARCH_ONLY. Rank by intent expectancy.
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

# reuse helpers from 002
sys.path.insert(0, str(_ROOT / "scripts"))
from run_pivot_exec_improve_002 import (  # noqa: E402
    H,
    MAX_ROWS,
    PACK,
    SL,
    TF,
    TP,
    _atr_clip_level,
    _bt,
    _diag,
    _rank,
    _run,
)
from llm2.paths import ARTIFACTS  # noqa: E402
from llm2.pivot.strategy.ev import net_bracket_magnitudes  # noqa: E402
from llm2.pivot.strategy.score_oos import gate_mask, score_symbol_oos  # noqa: E402
from llm2.pivot.strategy.soft_vsa import absorption_scores, train_threshold  # noqa: E402


def main() -> int:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out_dir = ARTIFACTS / "reports" / "pivot_forecast"
    print(f"BTC rescue 002b stamp={stamp}", flush=True)
    frozen = [
        "BTC_ctrl_ret_w4",
        "BTC_softvsa_w4",
        "BTC_p80_w4",
        "BTC_tp2_sl1_w4",
        "BTC_mid_atr_band_w4",
        "BTC_pi_band_w4",
    ]
    freeze = out_dir / f"btc_rescue_002b_freeze_{stamp}.json"
    freeze.write_text(
        json.dumps({"stamp": stamp, "frozen_arms_before_pf": frozen}, indent=2),
        encoding="utf-8",
    )
    print(f"WROTE {freeze}", flush=True)

    sym = "BTCUSDT"
    sc = score_symbol_oos(
        sym,
        timeframe=TF,
        horizon_bars=H,
        feature_pack=PACK,
        max_rows=MAX_ROWS,
        level_mode="ret",
        atr_min=2.0,
    )
    diag = _diag(sc)
    print(
        f"  diag lift={diag['pr_auc_lift']:.4f} ece={diag['ece']:.4f} p90={diag['level_p90']:.4f}",
        flush=True,
    )
    base = gate_mask(sc, mode="p75", tp=TP, sl=SL)
    # soft VSA train threshold
    is_short = sc.p_high >= 0.5
    scores = absorption_scores(sc.ohlcv, sc.ts_ms, is_short)
    idx = np.flatnonzero(base)
    cut = max(30, int(0.7 * idx.size))
    thr = train_threshold(scores[idx[:cut]], q=0.70)
    vsa = scores >= thr
    # p80 gate: raise thr to p80 of cal thr proxy — use percentile of p_any on train-like first 70%
    p = sc.p_any
    thr80 = float(np.nanpercentile(p[idx[:cut]], 80))
    p80 = base & (p >= thr80)
    abs_lr = np.abs(sc.level_ret)
    atr = sc.atr_frac
    mid = (
        base
        & np.isfinite(abs_lr)
        & np.isfinite(atr)
        & (abs_lr >= 0.8 * atr)
        & (abs_lr <= 1.5 * atr)
    )
    pi = net_bracket_magnitudes(TP, SL).pi_star
    pi_band = gate_mask(
        sc, mode="pi_star_level", tp=TP, sl=SL, pi_star=pi, min_abs_level=0.0015, max_abs_level=0.02
    )

    arms = [
        _run(sym, sc, base, tag="BTC_ctrl_ret_w4", work=4),
        _run(sym, sc, base & vsa, tag="BTC_softvsa_w4", work=4),
        _run(sym, sc, p80, tag="BTC_p80_w4", work=4),
        _run(sym, sc, mid, tag="BTC_mid_atr_band_w4", work=4),
        _run(sym, sc, pi_band, tag="BTC_pi_band_w4", work=4),
    ]
    # tp2/sl1: temporarily use different offsets via custom run
    from tradesim import Side
    from llm2.pivot.strategy.score_oos import limit_price_side
    from llm2.pivot.strategy.working_limit import LimitIntent, materialize_working_limits

    ts, is_short_a, lim = limit_price_side(sc, base)
    intents = [
        LimitIntent(
            decision_ts_ms=int(ts[j]),
            side=Side.SHORT if is_short_a[j] else Side.LONG,
            limit_price=float(lim[j]),
            stop_offset=0.01,
            target_offset=0.02,
            max_hold_bars=H + 2,
            work_bars=4,
        )
        for j in range(len(ts))
    ]
    sigs, fill = materialize_working_limits(sc.ohlcv, intents, work_bars=4)
    print(
        f"  BT BTC_tp2_sl1_w4 intent={int(base.sum())} fill%={100*fill['fill_rate']:.1f}",
        flush=True,
    )
    res = _bt(sym, sc.ohlcv, sigs, tag="BTC_tp2_sl1_w4", max_hold=H + 2)
    arm_tp = {
        "tag": "BTC_tp2_sl1_w4",
        "n_intent": int(base.sum()),
        "fill_pct": float(fill["fill_rate"]),
        "fill_stats": fill,
        **res,
    }
    if res.get("status") == "RAN":
        arm_tp["expectancy_intent_all"] = float(res["net_pnl"]) / max(int(base.sum()), 1)
        print(
            f"    n={res['n_trades']} PF={res['profit_factor']:.3f} WR={res['win_rate']:.3f} "
            f"pnl={res['net_pnl']:.2f} exp_i={arm_tp['expectancy_intent_all']:.5f}",
            flush=True,
        )
    arms.append(arm_tp)

    ranking = _rank(arms)
    ctrl = arms[0]
    promotions = {}
    for a in arms[1:]:
        if a.get("status") != "RAN" or ctrl.get("status") != "RAN":
            promotions[a["tag"]] = {"promote": False}
            continue
        exp_ok = float(a.get("expectancy_intent_all") or -1e9) > float(
            ctrl.get("expectancy_intent_all") or -1e9
        )
        pf_ok = float(a.get("profit_factor") or 0) >= 0.85 * float(ctrl.get("profit_factor") or 1)
        promotions[a["tag"]] = {
            "intent_exp_improved": exp_ok,
            "pf_not_collapsed": pf_ok,
            "promote": bool(exp_ok and pf_ok),
            "n_trades": a.get("n_trades"),
            "profit_factor": a.get("profit_factor"),
            "expectancy_intent_all": a.get("expectancy_intent_all"),
            "net_pnl": a.get("net_pnl"),
        }

    report = {
        "generation_id": "pivot_btc_rescue_002b",
        "stamp": stamp,
        "readiness_max": "RESEARCH_ONLY",
        "diagnostics": diag,
        "soft_vsa_thr": thr,
        "p80_thr": thr80,
        "arms": arms,
        "ranking_by_intent_expectancy": ranking,
        "promotions_vs_ctrl": promotions,
        "pick": ranking[0]["tag"] if ranking else None,
    }
    path = out_dir / f"btc_rescue_002b_{stamp}.json"
    latest = out_dir / "btc_rescue_002b_latest.json"
    path.write_text(json.dumps(report, indent=2, default=str), encoding="utf-8")
    latest.write_text(path.read_text(encoding="utf-8"), encoding="utf-8")
    print(f"WROTE {path}", flush=True)
    print(f"RANK {ranking}", flush=True)
    print(f"PROMOTE {promotions}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
