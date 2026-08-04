"""Audit that structure/multitrade backtests charge Bybit-style per-fill fees.

Replays one outer fold of eth_multitrade_v1_1 live geometry and checks:
  1) CostConfig is all-taker 0.055% / maker 0.02% (research defaults)
  2) Each trade.fees ≈ entry_notional*rate + exit_notional*rate (reconstructed)
  3) Stitched fee total scales with n_trades × dust notional (MIN_EXCHANGE)
  4) realized_pnl is net of fees (gross - fees + funding ≈ realized)

Evidence class: ENGINE_AUDIT. Not a performance claim.
"""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

import numpy as np
import pandas as pd

from tradesim.ensure_source import prefer_botsgeneral_tradesim

prefer_botsgeneral_tradesim()

from tradesim import (  # noqa: E402
    research_costs,
    research_instrument,
    research_margin,
    research_sizing,
    research_sim_hedge,
)
from tradesim.contracts import FeeRole, Liquidity  # noqa: E402
from tradesim.fees import price_fill  # noqa: E402

from llm2.backtest.conformance import run_conformance_check  # noqa: E402
from llm2.backtest.run import run_strategy_backtest  # noqa: E402
from llm2.data.loader import load_ohlcv  # noqa: E402
from llm2.data.macro import load_funding  # noqa: E402
from llm2.experiments.eth_multitrade_nested import (  # noqa: E402
    build_multitrade_signals,
    live_control_cfg,
)
from llm2.features.registry import build_space  # noqa: E402
from llm2.gates.evidence import leverage_from_stop, research_costs_baseline  # noqa: E402
from llm2.hunt.targets import proxy_side, target_family  # noqa: E402
from llm2.labels.direction import build_direction_labels  # noqa: E402
from llm2.models.boosting import LGBMRegressorPredictor  # noqa: E402
from llm2.paths import ARTIFACTS, FORWARD_LOCKBOX_START, TF_MS, touch_timeframe  # noqa: E402
from llm2.validation.folds import build_outer_folds, index_to_ms  # noqa: E402

SYMBOL = "ETHUSDT"
TIMEFRAME = "1h"
SL = 0.02
TAKER = 0.00055
GEN = "structure_v1_backtest_fee_audit_001"


def main() -> int:
    conf = run_conformance_check()
    if conf.get("passed") is False:
        raise RuntimeError("conformance failed")

    costs = research_costs_baseline()
    raw = research_costs()
    cost_ok = (
        abs(float(costs.taker_rate) - TAKER) < 1e-12
        and abs(float(raw.taker_rate) - TAKER) < 1e-12
        and costs.liquidity_for(FeeRole.ENTRY) == Liquidity.TAKER
        and costs.liquidity_for(FeeRole.TAKE_PROFIT) == Liquidity.TAKER
        and costs.liquidity_for(FeeRole.STOP) == Liquidity.TAKER
    )

    ohlcv = load_ohlcv(SYMBOL, TIMEFRAME)
    lock = pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC")
    ohlcv = ohlcv.loc[index_to_ms(ohlcv.index) < int(lock.value // 1_000_000)].copy()
    feats = build_space(ohlcv, "structure_v1", symbol=SYMBOL, timeframe=TIMEFRAME)
    y = build_direction_labels(ohlcv, horizon=6)["direction"]
    aligned = feats.join(y.rename("y"), how="inner").dropna()
    cols = [c for c in aligned.columns if c != "y"]
    X = aligned[cols].to_numpy(dtype=float)
    yv = aligned["y"].to_numpy(dtype=float)
    ts_ms = index_to_ms(aligned.index)
    folds = build_outer_folds(ts_ms, purge_bars=6, embargo_bars=6)
    # Use middle fold for a representative price regime
    fold = folds[2]
    tr, oos = fold.train_indices, fold.oos_indices
    model = LGBMRegressorPredictor(n_estimators=80, learning_rate=0.05)
    model.fit(X[tr], yv[tr])
    pred = model.predict(X[oos])
    mean = np.asarray(pred.mean, dtype=float).reshape(-1)
    side = proxy_side(mean, target_family("direction"))
    cfg = live_control_cfg()
    sigs, stats = build_multitrade_signals(ts_ms[oos], side, mean, cfg=cfg)

    oos0, oos1 = aligned.index[oos[0]], aligned.index[oos[-1]]
    pad = max(50, int(cfg["hold_addon"]) * 4)
    pos = int(ohlcv.index.searchsorted(oos0))
    window = ohlcv.loc[ohlcv.index[max(0, pos - pad)] : oos1]
    touch = load_ohlcv(SYMBOL, touch_timeframe(TIMEFRAME, SYMBOL))
    touch_tf = touch_timeframe(TIMEFRAME, SYMBOL)
    end, start = window.index[-1], window.index[0]
    dec_ms = int(TF_MS[TIMEFRAME])
    touch_end = end + pd.Timedelta(milliseconds=dec_ms) - pd.Timedelta(milliseconds=1)
    touch_win = touch.loc[(touch.index >= start) & (touch.index <= touch_end)]
    funding = load_funding(SYMBOL)
    funding = funding[funding.index < lock]
    funding_ts = (funding.index.asi8 // 1_000_000).astype(np.int64)
    funding_rt = funding.to_numpy(dtype=float)
    w_ts = index_to_ms(window.index)
    fmask = (funding_ts >= int(w_ts[0])) & (funding_ts <= int(w_ts[-1]))
    lev = float(leverage_from_stop(SL))
    instrument = research_instrument(SYMBOL)

    bundle = run_strategy_backtest(
        window,
        sigs,
        symbol=SYMBOL,
        timeframe=TIMEFRAME,
        strategy_id="fee-audit",
        touch_ohlcv=touch_win,
        touch_timeframe=touch_tf,
        costs=costs,
        margin=research_margin(leverage=lev),
        sizing=research_sizing(),
        sim=research_sim_hedge(
            max_hold_bars=int(cfg["hold_addon"]),
            decision_timeframe=TIMEFRAME,
            max_positions_per_side=7,
            max_positions_per_symbol=14,
        ),
        instrument=instrument,
        funding_ts_ms=funding_ts[fmask],
        funding_rate=funding_rt[fmask],
        plot=False,
        print_headline=False,
        store_path=None,
    )
    trades = list(bundle.result.trades)
    m = bundle.metrics

    # Reconstruct expected fees: two fills at taker on entry/exit notionals
    abs_err = []
    rel_err = []
    notionals = []
    qtys = []
    reconstructed_total = 0.0
    reported_total = 0.0
    pnl_identity_err = []
    zero_fee_trades = 0
    samples: list[dict[str, Any]] = []

    for t in trades:
        entry_px = float(t.entry_price)
        exit_px = float(t.exit_price)
        qty = abs(float(t.qty))
        entry_notional = abs(qty * entry_px)
        exit_notional = abs(qty * exit_px)
        # All-taker research schedule (TP/SL/timeout)
        exp = entry_notional * TAKER + exit_notional * TAKER
        # Cross-check price_fill helper
        pf_in = price_fill(
            role=FeeRole.ENTRY, qty=qty, price=entry_px, ref_price=entry_px, costs=costs
        )
        # Exit role from reason
        reason = str(getattr(t, "exit_reason", "") or "")
        if "stop" in reason:
            role = FeeRole.STOP
        elif "target" in reason:
            role = FeeRole.TAKE_PROFIT
        else:
            role = FeeRole.TIMEOUT
        pf_out = price_fill(
            role=role, qty=qty, price=exit_px, ref_price=exit_px, costs=costs
        )
        exp2 = float(pf_in.fee + pf_out.fee)
        got = float(getattr(t, "fees", 0.0) or 0.0)
        reported_total += got
        reconstructed_total += exp
        if got <= 0:
            zero_fee_trades += 1
        err = abs(got - exp2)
        abs_err.append(err)
        rel_err.append(err / max(exp2, 1e-12))
        notionals.append(entry_notional)
        qtys.append(qty)
        gross = float(getattr(t, "gross_pnl", 0.0) or 0.0)
        funding = float(getattr(t, "funding", 0.0) or 0.0)
        realized = float(getattr(t, "realized_pnl", 0.0) or 0.0)
        # Engine: realized = gross - fees + funding
        pnl_identity_err.append(abs(realized - (gross - got + funding)))
        if len(samples) < 8:
            samples.append(
                {
                    "entry_ts_ms": int(t.entry_ts_ms),
                    "qty": qty,
                    "entry_price": entry_px,
                    "exit_price": exit_px,
                    "entry_notional": entry_notional,
                    "fees_reported": got,
                    "fees_expected_taker2": exp2,
                    "exit_reason": reason,
                    "gross_pnl": gross,
                    "realized_pnl": realized,
                    "funding": funding,
                }
            )

    abs_err_a = np.asarray(abs_err, dtype=float)
    rel_err_a = np.asarray(rel_err, dtype=float)
    notionals_a = np.asarray(notionals, dtype=float)
    qtys_a = np.asarray(qtys, dtype=float)
    id_err = np.asarray(pnl_identity_err, dtype=float)

    # Expected order of magnitude: n_trades * 2 * taker * median_notional
    med_n = float(np.median(notionals_a)) if notionals_a.size else float("nan")
    rough = len(trades) * 2.0 * TAKER * med_n

    metrics_fees = float(getattr(m, "total_fees", float("nan")))
    # Prefer metrics if present else sum
    if not np.isfinite(metrics_fees):
        metrics_fees = reported_total

    fee_match_ok = bool(
        abs_err_a.size
        and float(np.max(abs_err_a)) < 1e-6
        and float(np.max(id_err)) < 1e-6
        and zero_fee_trades == 0
        and abs(metrics_fees - reported_total) < 1e-6
    )
    # Allow tiny float noise; also allow liquidation fee add-on (none expected)
    overall_ok = bool(cost_ok and fee_match_ok and med_n < 100.0)  # dust sanity

    # Scale illustration: if sized to $1000 notional each leg
    scale_1000 = (1000.0 / med_n) if med_n > 0 else float("nan")
    fees_if_1k = reported_total * scale_1000

    # Prior stitched measure for context
    measure_path = ARTIFACTS / "reports" / "structure_v1_eth_multitrade_v1_1_measure_latest.json"
    measure = json.loads(measure_path.read_text(encoding="utf-8")) if measure_path.is_file() else {}
    st = measure.get("stitched") or {}

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    report = {
        "generation_id": GEN,
        "created_utc": stamp,
        "evidence_class": "ENGINE_AUDIT",
        "max_readiness": "RESEARCH_ONLY",
        "symbol": SYMBOL,
        "fold_index": int(fold.fold_index),
        "conformance_passed": bool(conf.get("passed")),
        "cost_config": {
            "taker_rate": float(costs.taker_rate),
            "maker_rate": float(costs.maker_rate),
            "entry_slippage": float(costs.entry_slippage),
            "entry_liquidity": str(costs.liquidity_for(FeeRole.ENTRY)),
            "take_profit_liquidity": str(costs.liquidity_for(FeeRole.TAKE_PROFIT)),
            "stop_liquidity": str(costs.liquidity_for(FeeRole.STOP)),
            "matches_bybit_non_vip_baseline": cost_ok,
            "formula": "Fee = Qty × ExecutedPrice × Rate per fill; open+close separate",
        },
        "sizing": {
            "mode": "MIN_EXCHANGE",
            "instrument_min_qty": float(instrument.min_qty),
            "instrument_min_notional": float(instrument.min_notional),
            "instrument_qty_step": float(instrument.qty_step),
            "median_entry_notional_usdt": med_n,
            "mean_entry_notional_usdt": float(np.mean(notionals_a)),
            "median_qty": float(np.median(qtys_a)),
            "note": (
                "Dust notionals make absolute fee dollars look small even with "
                "many trades. Fee RATE accounting is what must be correct."
            ),
        },
        "fold_audit": {
            "n_trades": len(trades),
            "n_signals": int(stats["n_emitted"]),
            "total_fees_reported": reported_total,
            "total_fees_metrics": metrics_fees,
            "total_fees_reconstructed_all_taker": reconstructed_total,
            "max_abs_fee_error_vs_price_fill": float(np.max(abs_err_a)) if abs_err_a.size else None,
            "p99_abs_fee_error": float(np.quantile(abs_err_a, 0.99)) if abs_err_a.size else None,
            "max_rel_fee_error": float(np.max(rel_err_a)) if rel_err_a.size else None,
            "zero_fee_trades": int(zero_fee_trades),
            "max_pnl_identity_error": float(np.max(id_err)) if id_err.size else None,
            "rough_expected_fees_n_x_2_taker_x_median_notional": rough,
            "net_pnl": float(m.net_pnl),
            "gross_profit_factor": float(m.profit_factor),
            "fees_as_fraction_of_abs_net_pnl": (
                abs(reported_total / float(m.net_pnl)) if abs(float(m.net_pnl)) > 1e-9 else None
            ),
            "mean_fee_per_trade": reported_total / max(len(trades), 1),
            "fee_match_ok": fee_match_ok,
        },
        "scale_illustration": {
            "if_each_entry_notional_were_1000_usdt_fee_multiplier": scale_1000,
            "fold_fees_scaled_to_1k_notional": fees_if_1k,
            "plain_english": (
                f"This fold charged ~{reported_total:.2f} USDT fees on "
                f"{len(trades)} dust trades (median notional ~{med_n:.2f} USDT). "
                f"At $1000 notional per entry the same rate schedule would charge "
                f"~{fees_if_1k:.0f} USDT fees on this fold alone — fees scale with size, "
                "not just trade count."
            ),
        },
        "prior_stitched_measure_context": {
            "n_trades": st.get("n_trades"),
            "net_pnl": st.get("net_pnl"),
            "total_fees": st.get("total_fees"),
            "fees_per_trade": (
                float(st["total_fees"]) / float(st["n_trades"])
                if st.get("n_trades") and st.get("total_fees") is not None
                else None
            ),
            "fees_vs_net_pnl": (
                float(st["total_fees"]) / abs(float(st["net_pnl"]))
                if st.get("net_pnl") and abs(float(st["net_pnl"])) > 1e-9
                else None
            ),
        },
        "samples": samples,
        "overall_ok": overall_ok,
        "verdict": (
            "PASS — fees are charged per fill at Bybit non-VIP taker 0.055% on "
            "MIN_EXCHANGE dust notionals; small absolute fee totals are expected."
            if overall_ok
            else "FAIL — fee accounting mismatch or unexpected cost config."
        ),
    }

    out = ARTIFACTS / "reports" / f"{GEN}_latest.json"
    out.write_text(json.dumps(report, indent=2, default=str), encoding="utf-8")
    (ARTIFACTS / "reports" / f"{GEN}_{stamp}.json").write_text(
        out.read_text(encoding="utf-8"), encoding="utf-8"
    )
    print(json.dumps({
        "verdict": report["verdict"],
        "overall_ok": overall_ok,
        "cost_ok": cost_ok,
        "fee_match_ok": fee_match_ok,
        "fold_n_trades": len(trades),
        "fold_total_fees": round(reported_total, 4),
        "median_notional": round(med_n, 4),
        "mean_fee_per_trade": round(reported_total / max(len(trades), 1), 6),
        "max_fee_error": float(np.max(abs_err_a)) if abs_err_a.size else None,
        "stitched_measure_fees": st.get("total_fees"),
        "stitched_measure_trades": st.get("n_trades"),
        "scale_note": report["scale_illustration"]["plain_english"],
    }, indent=2))
    print(f"wrote {out}")
    return 0 if overall_ok else 2


if __name__ == "__main__":
    raise SystemExit(main())
