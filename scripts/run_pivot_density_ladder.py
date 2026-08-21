"""Density ladder for sparse pi*+band arms (RESEARCH_ONLY, count-first).

FROZEN before any outer Profit Factor (PF) is viewed:
  1) p75                         — volume control
  2) p75 & pi*                   — usually == p75 when thr_any > pi*
  3) p75 & fixed band (tight)    — sparse chart arm (0.15%..2%)
  4) p75 & wide band             — 0.08%..3%
  5) p75 & ATR band 0.5..2.0x    — DEFAULT denser chart candidate
  6) p75 & soft |level| p20..p80 — train-quantile band
  7) pi*_only (no p75)           — diagnostic counts only

Promotion rule (preregistered): prefer arm (5) if trade N >= ~100/symbol AND
fill PF stays near the sparse tight-band arm (no post-hoc band widening).
Report intent_N / fill_pct / trade_N separately on every arm.
"""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from tradesim.ensure_source import prefer_botsgeneral_tradesim

prefer_botsgeneral_tradesim()

from tradesim import Side, research_instrument, research_margin, research_sizing  # noqa: E402
from tradesim import research_sim_limit_entry  # noqa: E402

from llm2.backtest.run import run_strategy_backtest  # noqa: E402
from llm2.data.loader import load_ohlcv  # noqa: E402
from llm2.data.macro import load_funding  # noqa: E402
from llm2.gates.evidence import leverage_from_stop, research_costs_baseline  # noqa: E402
from llm2.paths import ARTIFACTS, FORWARD_LOCKBOX_START, TF_MS, touch_timeframe  # noqa: E402
from llm2.pivot.strategy.ev import net_bracket_magnitudes  # noqa: E402
from llm2.pivot.strategy.score_oos import gate_mask, limit_price_side, score_symbol_oos  # noqa: E402
from llm2.pivot.strategy.working_limit import LimitIntent, materialize_working_limits  # noqa: E402
from llm2.validation.folds import index_to_ms  # noqa: E402
import pandas as pd  # noqa: E402

SYMBOLS = ("BTCUSDT", "ETHUSDT")
TF, H, TP, SL, WORK = "15m", 4, 0.01, 0.01, 4
PACK = "level_vsa"
MAX_ROWS = 120_000


def _counts(sc, pi: float) -> dict:
    p75 = gate_mask(sc, mode="p75", tp=TP, sl=SL)
    pi_m = gate_mask(sc, mode="pi_star", tp=TP, sl=SL, pi_star=pi)
    band = gate_mask(
        sc, mode="pi_star_level", tp=TP, sl=SL, pi_star=pi, min_abs_level=0.0015, max_abs_level=0.02
    )
    wide = gate_mask(
        sc, mode="pi_star_level", tp=TP, sl=SL, pi_star=pi, min_abs_level=0.0008, max_abs_level=0.03
    )
    abs_lr = np.abs(sc.level_ret)
    atr = sc.atr_frac
    atr_band = p75 & np.isfinite(abs_lr) & np.isfinite(atr) & (abs_lr >= 0.5 * atr) & (abs_lr <= 2.0 * atr)
    # train soft quantile band on first 70% of p75 rows
    idx = np.flatnonzero(p75)
    cut = max(30, int(0.7 * idx.size))
    train_abs = abs_lr[idx[:cut]]
    train_abs = train_abs[np.isfinite(train_abs)]
    lo = float(np.nanpercentile(train_abs, 20)) if train_abs.size else 0.0015
    hi = float(np.nanpercentile(train_abs, 80)) if train_abs.size else 0.02
    qband = p75 & np.isfinite(abs_lr) & (abs_lr >= lo) & (abs_lr <= hi)
    # pi without requiring p75 (diagnostic)
    pi_only = (sc.p_any >= pi) & np.isfinite(sc.p_any)
    thr_med = float(np.nanmedian(sc.thr_any[np.isfinite(sc.thr_any)])) if np.isfinite(sc.thr_any).any() else float("nan")
    return {
        "n_rows": int(sc.n_rows),
        "thr_any_median": thr_med,
        "pi_star": float(pi),
        "n_p75": int(p75.sum()),
        "n_p75_and_pi": int(pi_m.sum()),
        "n_pi_star_level_tight": int(band.sum()),
        "n_pi_star_level_wide": int(wide.sum()),
        "n_p75_atr_band": int(atr_band.sum()),
        "n_p75_qband_p20_p80": int(qband.sum()),
        "n_pi_only_no_p75": int(pi_only.sum()),
        "qband_lo": lo,
        "qband_hi": hi,
        "masks": {
            "p75": p75,
            "atr_band": atr_band,
            "qband": qband,
            "wide": wide,
            "tight": band,
        },
    }


def _bt(symbol, ohlcv, signals, *, tag: str, max_hold: int):
    if len(signals) < 12:
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
    window = ohlcv.iloc[max(0, i0 - 80) : min(len(ohlcv), i1 + 80)]
    w_ts = index_to_ms(window.index)
    fmask = (f_ts >= int(w_ts[0])) & (f_ts <= int(w_ts[-1]))
    end, start = window.index[-1], window.index[0]
    touch_end = end + pd.Timedelta(milliseconds=int(TF_MS[TF])) - pd.Timedelta(milliseconds=1)
    touch_win = touch.loc[(touch.index >= start) & (touch.index <= touch_end)]
    bundle = run_strategy_backtest(
        window,
        signals,
        symbol=symbol,
        timeframe=TF,
        strategy_id=tag,
        touch_ohlcv=touch_win if len(touch_win) else None,
        touch_timeframe=touch_tf,
        costs=research_costs_baseline(),
        margin=research_margin(leverage=float(leverage_from_stop(SL))),
        sizing=research_sizing(),
        sim=research_sim_limit_entry(max_hold_bars=max_hold, decision_timeframe=TF),
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
        "entry_bar_exit_rate": ebr,
    }


def _run_mask(symbol, sc, mask, *, tag: str, work: int = WORK):
    n_intent = int(mask.sum())
    if n_intent < 15:
        return {
            "tag": tag,
            "status": "TOO_FEW_GATED",
            "n_intent": n_intent,
            "fill_pct": float("nan"),
            "n_trades": 0,
        }
    ts, is_short, lim = limit_price_side(sc, mask)
    intents = [
        LimitIntent(
            decision_ts_ms=int(ts[j]),
            side=Side.SHORT if is_short[j] else Side.LONG,
            limit_price=float(lim[j]),
            stop_offset=SL,
            target_offset=TP,
            max_hold_bars=H + 2,
            work_bars=work,
        )
        for j in range(len(ts))
    ]
    sigs, fill = materialize_working_limits(sc.ohlcv, intents, work_bars=work)
    n_path = int(fill.get("n_filled_path", 0))
    fill_pct = float(n_path / n_intent) if n_intent else float("nan")
    print(
        f"  BT {tag} intent_N={n_intent} path_fill={n_path} fill%={100*fill_pct:.1f}",
        flush=True,
    )
    res = _bt(symbol, sc.ohlcv, sigs, tag=tag, max_hold=H + 2)
    out = {
        "tag": tag,
        "n_intent": n_intent,
        "fill_pct": fill_pct,
        "fill_stats": fill,
        **res,
    }
    if res.get("status") == "RAN":
        out["n_trades"] = int(res["n_trades"])
        print(
            f"    trade_N={res['n_trades']} PF={res['profit_factor']:.3f} "
            f"WR={res['win_rate']:.3f} ebr={res['entry_bar_exit_rate']}",
            flush=True,
        )
    return out


def _promotion_note(sym_block: dict) -> dict:
    """Apply frozen promotion rule after arms are scored (no band edits)."""
    arms = {a["tag"]: a for a in sym_block["arms"]}
    sym = next(iter(arms)).split("_")[0]
    sparse = arms.get(f"{sym}_tight_band", {})
    atr = arms.get(f"{sym}_atr_band", {})
    sparse_pf = float(sparse.get("profit_factor", float("nan")))
    atr_n = int(atr.get("n_trades", 0) or 0)
    atr_pf = float(atr.get("profit_factor", float("nan")))
    near = (
        np.isfinite(sparse_pf)
        and np.isfinite(atr_pf)
        and sparse_pf > 0
        and atr_pf >= 0.85 * sparse_pf
    )
    ok_n = atr_n >= 100
    promote = bool(ok_n and near and atr.get("status") == "RAN")
    return {
        "default_candidate": f"{sym}_atr_band",
        "n_trades_atr_band": atr_n,
        "pf_atr_band": atr_pf,
        "pf_sparse_tight": sparse_pf,
        "n_ge_100": ok_n,
        "pf_near_sparse_85pct": near,
        "promote_atr_band": promote,
        "rule": "promote P75+ATR band only if trade_N>=100 and fill PF >= 0.85 * tight-band PF",
    }


def main() -> int:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    pi = net_bracket_magnitudes(TP, SL).pi_star
    print(f"density ladder stamp={stamp} pi*={pi:.4f} (counts frozen before PF)", flush=True)
    report = {
        "stamp": stamp,
        "pi_star": pi,
        "readiness_max": "RESEARCH_ONLY",
        "ladder_frozen": True,
        "default_denser_chart": "p75_atr_band_0.5_2.0x",
        "no_post_hoc_band_widening": True,
        "symbols": {},
        "counts_freeze": {},
    }
    scored = {}
    # Phase 1: score + freeze counts (no PF yet)
    for sym in SYMBOLS:
        level_mode = "atr" if sym == "ETHUSDT" else "ret"
        print(f"SCORE {sym} level={level_mode} …", flush=True)
        sc = score_symbol_oos(
            sym,
            timeframe=TF,
            horizon_bars=H,
            feature_pack=PACK,
            max_rows=MAX_ROWS,
            level_mode=level_mode,
        )
        c = _counts(sc, pi)
        masks = c.pop("masks")
        report["counts_freeze"][sym] = c
        scored[sym] = {"sc": sc, "masks": masks, "level_mode": level_mode}
        print(
            f"  FROZEN counts thr_any_med={c['thr_any_median']:.3f} p75={c['n_p75']} "
            f"tight={c['n_pi_star_level_tight']} wide={c['n_pi_star_level_wide']} "
            f"atr_band={c['n_p75_atr_band']} qband={c['n_p75_qband_p20_p80']}",
            flush=True,
        )

    out_dir = ARTIFACTS / "reports" / "pivot_forecast"
    out_dir.mkdir(parents=True, exist_ok=True)
    freeze_path = out_dir / f"density_ladder_counts_{stamp}.json"
    freeze_path.write_text(
        json.dumps(
            {
                "stamp": stamp,
                "pi_star": pi,
                "counts_freeze": report["counts_freeze"],
                "note": "frozen before any arm Profit Factor",
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    print(f"WROTE counts freeze {freeze_path}", flush=True)

    # Phase 2: backtests (PF viewed only after freeze file exists)
    for sym, pack in scored.items():
        sc, masks = pack["sc"], pack["masks"]
        arms = [
            _run_mask(sym, sc, masks["p75"], tag=f"{sym}_p75_ctrl"),
            _run_mask(sym, sc, masks["tight"], tag=f"{sym}_tight_band"),
            _run_mask(sym, sc, masks["wide"], tag=f"{sym}_wide_band"),
            _run_mask(sym, sc, masks["atr_band"], tag=f"{sym}_atr_band"),
            _run_mask(sym, sc, masks["qband"], tag=f"{sym}_qband_p20p80"),
            _run_mask(sym, sc, masks["atr_band"], tag=f"{sym}_atr_band_work6", work=6),
        ]
        block = {"level_mode": pack["level_mode"], "arms": arms}
        block["promotion"] = _promotion_note(block)
        report["symbols"][sym] = block
        print(f"  promotion {sym}: {block['promotion']}", flush=True)

    path = out_dir / f"density_ladder_{stamp}.json"
    latest = out_dir / "density_ladder_latest.json"
    path.write_text(json.dumps(report, indent=2, default=str), encoding="utf-8")
    latest.write_text(path.read_text(encoding="utf-8"), encoding="utf-8")
    print(f"WROTE {path}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
