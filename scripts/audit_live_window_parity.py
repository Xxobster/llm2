"""Live-window parity: live decision history vs local recompute on same candles.

Compares, bar-by-bar from first live decision through last:
  - structure_v1 feature values (full warehouse vs recent_only)
  - pred_mean and gated side vs live ledger
  - single-book entry intent under max-one-position (same geometry as live)

Requires --i-accept-lockbox-contamination when the live window is after 2026-05-01.

Example:
  python scripts/audit_live_window_parity.py \\
    --pack artifacts/live_packs/structure_v1_ethusdt_direction \\
    --live-decisions artifacts/reports/_live_decisions_eth_single.json \\
    --i-accept-lockbox-contamination
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import joblib
import numpy as np
import pandas as pd

os.environ.setdefault("TRADESIM_NO_PLOT", "1")

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))
_md = Path(r"C:\projects\botsgeneral\packages\market_data\src")
if _md.is_dir() and str(_md) not in sys.path:
    sys.path.insert(0, str(_md))
_ind = Path(r"C:\projects\botsgeneral\packages\indicators\src")
if _ind.is_dir() and str(_ind) not in sys.path:
    sys.path.insert(0, str(_ind))

from tradesim.ensure_source import prefer_botsgeneral_tradesim  # noqa: E402

prefer_botsgeneral_tradesim()

from tradesim import (  # noqa: E402
    Signal,
    research_instrument,
    research_margin,
    research_sizing,
    research_sim,
    research_sim_hedge,
)

from llm2.backtest.run import run_strategy_backtest  # noqa: E402
from llm2.data.indicators import clear_indicator_cache, indicators_db_path  # noqa: E402
from llm2.data.loader import load_ohlcv  # noqa: E402
from llm2.data.macro import load_funding  # noqa: E402
from llm2.evidence.lockbox_guard import add_lockbox_guard_args, require_lockbox_access  # noqa: E402
from llm2.features.registry import build_space  # noqa: E402
from llm2.gates.evidence import leverage_from_stop, research_costs_baseline  # noqa: E402
from llm2.hunt.targets import DIRECTION_BAND, proxy_side, target_family  # noqa: E402
from llm2.live.refresh_structure import fetch_ohlcv_binance_rest  # noqa: E402
from llm2.models.base import Prediction  # noqa: E402
from llm2.paths import ARTIFACTS, FORWARD_LOCKBOX_START, MARKET_DB, ROUND_TRIP_COST, touch_timeframe  # noqa: E402
from llm2.research_policy import PolicyError  # noqa: E402
from llm2.signals.translate import predictions_to_signals  # noqa: E402
from llm2.validation.folds import index_to_ms  # noqa: E402

EXPERIMENT_ID = "live_window_parity_same_geometry"


def _rel_pct(a: float, b: float) -> float:
    if not np.isfinite(b) or abs(b) < 1e-12:
        return float("nan")
    return 100.0 * (float(a) - float(b)) / float(b)


def _default_edge(strategy: dict[str, Any]) -> float:
    family = target_family(str(strategy.get("target", "fwd_return")))
    default = DIRECTION_BAND if family == "directional" else ROUND_TRIP_COST
    edge = float(strategy.get("min_edge", default))
    if family == "directional" and abs(edge - ROUND_TRIP_COST) < 1e-12:
        edge = DIRECTION_BAND
    return edge


def refresh_local_data(symbol: str, timeframe: str) -> dict[str, Any]:
    """Pull tip candles into warehouse + recompute structure for symbol."""
    from market_data.db import ResearchCandleDB

    report: dict[str, Any] = {"symbol": symbol, "steps": []}
    db = ResearchCandleDB(MARKET_DB)
    try:
        touch_tf = touch_timeframe(timeframe, symbol)
        for tf, lim, pt in (
            (timeframe, 2000, "last_price"),
            (touch_tf, 20000, "last"),
            ("4h", 800, "last_price"),
            ("1w", 120, "last_price"),
        ):
            try:
                df = fetch_ohlcv_binance_rest(symbol, tf, limit=lim).reset_index(drop=True)
                n = db.upsert_df(
                    df,
                    source="binance",
                    symbol=symbol,
                    timeframe=tf,
                    price_type=pt,
                )
                # Keep synonym tip in sync so densest series still covers the live window.
                if tf == timeframe and pt == "last_price":
                    db.upsert_df(
                        df,
                        source="binance",
                        symbol=symbol,
                        timeframe=tf,
                        price_type="last",
                    )
                report["steps"].append(
                    {
                        "ohlcv_tf": tf,
                        "price_type": pt,
                        "upserted": int(n),
                        "last_ts_ms": int(df["ts_ms"].iloc[-1]),
                    }
                )
            except Exception as exc:  # noqa: BLE001
                report["steps"].append({"ohlcv_tf": tf, "error": f"{type(exc).__name__}: {exc}"})
    finally:
        db.close()

    try:
        # Full-history recompute + tip (short upsert alone replaces the series).
        from indicators.compute import compute_structure
        from indicators.store import IndicatorDB

        ind_db = IndicatorDB(indicators_db_path())
        try:
            tfs = (timeframe, "4h", "1w") if timeframe == "1h" else (timeframe, "1w")
            for tf in tfs:
                try:
                    wh = load_ohlcv(symbol, tf, source="binance")
                except Exception:
                    wh = pd.DataFrame()
                if len(wh) and wh.index.tz is None:
                    wh.index = wh.index.tz_localize("UTC")
                if len(wh) and "ts_ms" not in wh.columns:
                    wh = wh.copy()
                    wh["ts_ms"] = index_to_ms(wh.index)
                rest = fetch_ohlcv_binance_rest(
                    symbol, tf, limit=3000 if tf in {"1h", "4h"} else 500
                )
                cols = ["open", "high", "low", "close", "volume", "ts_ms"]
                if len(wh):
                    a = wh[cols].copy()
                    b = rest[cols].copy() if not rest.empty else a.iloc[0:0]
                    out = pd.concat([a, b]).sort_index()
                else:
                    out = rest[cols].copy() if not rest.empty else pd.DataFrame()
                if out.empty:
                    report["steps"].append({"structure_tf": tf, "error": "no_ohlcv"})
                    continue
                out = out[~out.index.duplicated(keep="last")]
                bundle = compute_structure(
                    out.reset_index(drop=True),
                    source="binance",
                    symbol=symbol.upper(),
                    timeframe=tf,
                )
                counts = ind_db.upsert_bundle(bundle)
                report["steps"].append(
                    {
                        "structure_tf": tf,
                        "n_bars": int(len(out)),
                        "first": str(out.index.min()),
                        "last": str(out.index.max()),
                        "counts": counts,
                    }
                )
        finally:
            ind_db.close()
        clear_indicator_cache()
    except Exception as exc:  # noqa: BLE001
        report["structure_error"] = f"{type(exc).__name__}: {exc}"
    clear_indicator_cache()
    return report


def load_live_decisions(path: Path) -> pd.DataFrame:
    raw = path.read_bytes()
    text = raw.decode("utf-16") if raw.startswith((b"\xff\xfe", b"\xfe\xff")) else raw.decode("utf-8")
    blob = json.loads(text)
    rows = blob.get("decisions") if isinstance(blob, dict) else blob
    df = pd.DataFrame(rows)
    if df.empty:
        return df
    df["bar_ts"] = pd.to_datetime(df["bar_ts_ms"].astype("int64"), unit="ms", utc=True)
    df = df.sort_values("bar_ts_ms").drop_duplicates("bar_ts_ms", keep="last")
    return df.reset_index(drop=True)


def compare_live_window(
    *,
    pack_dir: Path,
    live_df: pd.DataFrame,
    single_book: bool = True,
) -> dict[str, Any]:
    strategy = json.loads((pack_dir / "strategy.json").read_text(encoding="utf-8"))
    blob = joblib.load(pack_dir / "model.joblib")
    model = blob["model"]
    cols = list(blob["feature_columns"])
    symbol = str(strategy["symbol"]).upper()
    timeframe = str(strategy["timeframe"])
    family = target_family(str(strategy.get("target", "fwd_return")))
    edge = _default_edge(strategy)
    tp = float(strategy.get("tp_pct", 0.01))
    sl = float(strategy.get("sl_pct", 0.02))
    hold = int(strategy.get("horizon_bars", 6))
    lev = float(strategy.get("leverage") or leverage_from_stop(sl))

    start = pd.Timestamp(live_df["bar_ts"].iloc[0])
    end = pd.Timestamp(live_df["bar_ts"].iloc[-1]) + pd.Timedelta(milliseconds=1)

    ohlcv = load_ohlcv(symbol, timeframe)
    if ohlcv.index.tz is None:
        ohlcv.index = ohlcv.index.tz_localize("UTC")
    # Feature history through last live bar
    feat_ohlcv = ohlcv.loc[ohlcv.index <= live_df["bar_ts"].iloc[-1]].copy()
    if len(feat_ohlcv) < 50:
        raise RuntimeError(f"insufficient OHLCV for {symbol}: {len(feat_ohlcv)}")

    clear_indicator_cache()
    os.environ.pop("LLM2_INDICATORS_DB", None)
    feats_full = build_space(
        feat_ohlcv, "structure_v1", symbol=symbol, timeframe=timeframe, recent_only=False
    ).reindex(columns=cols)
    feats_livepath = build_space(
        feat_ohlcv, "structure_v1", symbol=symbol, timeframe=timeframe, recent_only=True
    ).reindex(columns=cols)

    # Fill retrace like live
    for feats in (feats_full, feats_livepath):
        if "last_retrace_pct" in feats.columns:
            feats["last_retrace_pct"] = feats["last_retrace_pct"].fillna(0.0)
        for c in feats.columns:
            if c.startswith("last_retrace_pct_"):
                feats[c] = feats[c].fillna(0.0)

    bar_rows: list[dict[str, Any]] = []
    feat_abs_max = 0.0
    feat_rel_max = 0.0
    feat_mismatch_bars = 0
    side_mismatches = 0
    pred_abs = []
    pred_rel = []

    for _, live in live_df.iterrows():
        ts = pd.Timestamp(live["bar_ts"])
        row: dict[str, Any] = {
            "bar_ts": ts.isoformat(),
            "bar_ts_ms": int(live["bar_ts_ms"]),
            "live_side": int(live["side"]),
            "live_pred_mean": float(live["pred_mean"]) if live["pred_mean"] is not None else None,
            "live_skip_reason": live.get("skip_reason"),
            "live_mark": live.get("mark"),
        }
        if ts not in feats_full.index or ts not in feats_livepath.index:
            row["status"] = "BAR_MISSING_IN_FEATURES"
            bar_rows.append(row)
            continue

        f = feats_full.loc[ts]
        l = feats_livepath.loc[ts]
        both = f.notna() & l.notna()
        if both.any():
            fa = f[both].to_numpy(dtype=float)
            la = l[both].to_numpy(dtype=float)
            d_abs = np.abs(la - fa)
            d_rel = np.abs(100.0 * (la - fa) / np.maximum(np.abs(fa), 1e-12))
            bad = (d_abs > 1e-9) & (d_rel > 1e-4)
            feat_abs_max = max(feat_abs_max, float(np.nanmax(d_abs)) if d_abs.size else 0.0)
            feat_rel_max = max(feat_rel_max, float(np.nanmax(d_rel)) if d_rel.size else 0.0)
            if bad.any():
                feat_mismatch_bars += 1
                row["feature_mismatch_cols"] = list(f.index[both][bad][:8])
            row["feature_max_abs_diff"] = float(np.nanmax(d_abs)) if d_abs.size else 0.0
            row["feature_max_rel_pct"] = float(np.nanmax(d_rel)) if d_rel.size else 0.0
        else:
            row["feature_status"] = "NO_FINITE_OVERLAP"

        # Model on full-path features (BT research path)
        x = f.reindex(cols).to_numpy(dtype=float).reshape(1, -1)
        if np.isnan(x).any():
            row["bt_status"] = "FEATURE_NAN"
            bar_rows.append(row)
            continue
        pred = model.predict(x)
        mean = float(np.asarray(pred.mean if getattr(pred, "mean", None) is not None else pred).reshape(-1)[0])
        side_raw = int(proxy_side(np.asarray([mean], dtype=float), family)[0])
        side_gated = side_raw if abs(mean) >= edge else 0
        row["bt_pred_mean"] = mean
        row["bt_side_gated"] = side_gated
        row["bt_edge"] = edge

        if row["live_pred_mean"] is not None and np.isfinite(row["live_pred_mean"]):
            pa = abs(mean - float(row["live_pred_mean"]))
            pr = abs(_rel_pct(mean, float(row["live_pred_mean"])))
            pred_abs.append(pa)
            pred_rel.append(pr)
            row["pred_mean_abs_diff"] = pa
            row["pred_mean_rel_pct"] = pr
        if int(live["side"]) != side_gated:
            # Live stores proxy_side before edge in decide_once then... actually live returns
            # side from proxy_side WITHOUT zeroing on edge in the return dict — check again.
            # decide_once: side = proxy_side(...); does NOT apply edge to returned side!
            # Edge is only used later? Looking at decide_once - it returns side without edge gate!
            # But concordance applied edge. Live may trade if |mean| < edge?
            # Actually micro_runner: if mode LIVE and side != 0 — so ungated proxy_side.
            # Direction packs min_edge=0.1 so |pred| is usually > 0.1 when side nonzero.
            side_mismatches += 1
            row["side_mismatch"] = True
        bar_rows.append(row)

    # Live decide_once returns ungated proxy_side — recompute that for fair compare
    side_match_ungated = 0
    side_match_gated = 0
    n_cmp = 0
    for row in bar_rows:
        if row.get("bt_pred_mean") is None or row.get("live_side") is None:
            continue
        n_cmp += 1
        mean = float(row["bt_pred_mean"])
        ungated = int(proxy_side(np.asarray([mean], dtype=float), family)[0])
        gated = ungated if abs(mean) >= edge else 0
        row["bt_side_ungated"] = ungated
        if ungated == int(row["live_side"]):
            side_match_ungated += 1
        if gated == int(row["live_side"]):
            side_match_gated += 1
        # Prefer ungated as live parity (decide_once behavior)
        row["side_match_live_decide_once"] = ungated == int(row["live_side"])

    # Same-geometry single-book backtest: max one position
    live_bars = [pd.Timestamp(t) for t in live_df["bar_ts"]]
    aligned = feats_full.reindex(live_bars)
    # Live zero-fills retrace; do the same before dropna so we do not discard every bar.
    if "last_retrace_pct" in aligned.columns:
        aligned["last_retrace_pct"] = aligned["last_retrace_pct"].fillna(0.0)
    for c in aligned.columns:
        if c.startswith("last_retrace_pct_"):
            aligned[c] = aligned[c].fillna(0.0)
    aligned = aligned.dropna(how="any")
    if len(aligned) == 0:
        trades = []
        skips = []
        skip_counts = Counter()
        bt_entry_note = "NO_ALIGNED_FEATURE_BARS_FOR_BT"
    else:
        ts_ms = index_to_ms(aligned.index)
        X = aligned.to_numpy(dtype=float)
        pred = model.predict(X)
        mean = np.asarray(pred.mean if getattr(pred, "mean", None) is not None else pred, dtype=float).reshape(-1)
        side = proxy_side(mean, family).astype(np.int8)
        signals = predictions_to_signals(
            ts_ms,
            Prediction(side=side, mean=mean),
            tp_pct=tp,
            sl_pct=sl,
            min_edge=edge,
        )
        signals = [
            Signal(
                ts_ms=int(s.ts_ms),
                side=s.side,
                symbol=symbol,
                stop_offset=s.stop_offset,
                target_offset=s.target_offset,
                max_hold_bars=hold,
            )
            for s in signals
        ]

        pad = pd.Timedelta(hours=max(hold + 2, 8))
        win = ohlcv.loc[
            (ohlcv.index >= start - pd.Timedelta(days=2)) & (ohlcv.index < end + pad)
        ]
        touch_tf = touch_timeframe(timeframe, symbol)
        touch = load_ohlcv(symbol, touch_tf)
        if touch.index.tz is None:
            touch.index = touch.index.tz_localize("UTC")
        touch_win = touch.loc[(touch.index >= start - pd.Timedelta(days=1)) & (touch.index < end + pad)]

        funding = load_funding(symbol)
        if funding is not None and len(funding):
            f_ts = index_to_ms(funding.index)
            f_rt = funding.to_numpy(dtype=float).reshape(-1)
            w0, w1 = int(index_to_ms(win.index)[0]), int(index_to_ms(win.index)[-1])
            fmask = (f_ts >= w0) & (f_ts <= w1)
            f_ts, f_rt = f_ts[fmask], f_rt[fmask]
        else:
            f_ts = np.asarray([], dtype=np.int64)
            f_rt = np.asarray([], dtype=float)

        sim = research_sim(
            starting_equity=10_000.0,
            max_hold_bars=hold,
            max_positions_per_symbol=1,
            allow_concurrent_positions=False,
        )
        if not single_book:
            sim = research_sim_hedge(starting_equity=10_000.0, max_hold_bars=hold)

        bundle = run_strategy_backtest(
            win,
            signals,
            symbol=symbol,
            timeframe=timeframe,
            strategy_id=f"llm2-live-window-{symbol}",
            touch_ohlcv=touch_win if len(touch_win) else None,
            touch_timeframe=touch_tf if len(touch_win) else None,
            costs=research_costs_baseline(),
            margin=research_margin(leverage=lev),
            sizing=research_sizing(),
            instrument=research_instrument(symbol),
            sim=sim,
            funding_ts_ms=f_ts if f_ts.size else None,
            funding_rate=f_rt if f_rt.size else None,
            plot=False,
            print_headline=False,
            store_path=None,
            starting_equity=10_000.0,
        )
        trades = list(bundle.result.trades)
        skips = list(getattr(bundle.result, "skips", []) or [])
        skip_counts = Counter(getattr(s, "reason", str(s)) for s in skips)
        bt_entry_note = (
            "BT uses max_positions_per_symbol=1 (same as live single-book). "
            "Expect few trades while live stays in position_already_open."
        )

    live_entry_ok = int(
        sum(
            1
            for _, r in live_df.iterrows()
            if not r.get("skip_reason") and int(r["side"]) != 0
        )
    )
    live_already_open = int(
        sum(
            1
            for _, r in live_df.iterrows()
            if str(r.get("skip_reason") or "").startswith("position_already_open")
        )
    )

    return {
        "symbol": symbol,
        "timeframe": timeframe,
        "pack": str(pack_dir),
        "live_window_start": start.isoformat(),
        "live_window_end": pd.Timestamp(live_df["bar_ts"].iloc[-1]).isoformat(),
        "n_live_decisions": int(len(live_df)),
        "geometry": "single_book_max1" if single_book else "multitrade_hedge",
        "features": {
            "source": str(indicators_db_path()),
            "n_bars_compared": int(len(live_df)),
            "n_feature_mismatch_bars": feat_mismatch_bars,
            "feature_bar_match_rate": float(1.0 - feat_mismatch_bars / max(len(live_df), 1)),
            "max_abs_diff": feat_abs_max,
            "max_rel_pct": feat_rel_max,
            "note": "full warehouse vs recent_only on same candles for each live bar",
        },
        "signals": {
            "n_compared": n_cmp,
            "side_match_rate_ungated_decide_once": float(side_match_ungated / n_cmp) if n_cmp else None,
            "side_match_rate_gated_edge": float(side_match_gated / n_cmp) if n_cmp else None,
            "pred_mean_abs_diff": {
                "n": len(pred_abs),
                "mean": float(np.mean(pred_abs)) if pred_abs else None,
                "max": float(np.max(pred_abs)) if pred_abs else None,
                "median": float(np.median(pred_abs)) if pred_abs else None,
            },
            "pred_mean_rel_pct": {
                "n": len(pred_rel),
                "mean": float(np.mean(pred_rel)) if pred_rel else None,
                "max": float(np.max(pred_rel)) if pred_rel else None,
                "median": float(np.median(pred_rel)) if pred_rel else None,
            },
            "edge": edge,
            "note": "Live decide_once returns ungated proxy_side; gated is research edge filter.",
        },
        "entries_same_geometry": {
            "live_entry_ok_bars": live_entry_ok,
            "live_position_already_open_bars": live_already_open,
            "bt_n_trades": len(trades),
            "bt_n_skips": len(skips),
            "bt_skip_reasons": dict(skip_counts),
            "bt_trades": [
                {
                    "entry_ts_ms": int(t.entry_ts_ms),
                    "exit_ts_ms": int(t.exit_ts_ms),
                    "side": int(t.side),
                    "entry_price": float(t.entry_price),
                    "exit_price": float(t.exit_price),
                    "exit_reason": str(t.exit_reason),
                }
                for t in trades
            ],
            "note": bt_entry_note,
        },
        "bars": bar_rows,
    }


def build_argparser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--pack", type=Path, required=True)
    p.add_argument("--live-decisions", type=Path, required=True)
    p.add_argument("--refresh-data", action="store_true", help="Refresh local OHLCV+structure tip")
    p.add_argument("--multitrade", action="store_true", help="Use hedge sim (not single-book max1)")
    p.add_argument("--no-refresh", action="store_true")
    add_lockbox_guard_args(p)
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_argparser().parse_args(argv)
    pack_dir = args.pack.resolve()
    live_df = load_live_decisions(args.live_decisions)
    if live_df.empty:
        raise SystemExit("no live decisions")

    start = pd.Timestamp(live_df["bar_ts"].iloc[0])
    end = pd.Timestamp(live_df["bar_ts"].iloc[-1]) + pd.Timedelta(hours=1)
    require_lockbox_access(
        experiment_id=EXPERIMENT_ID,
        window_start=start.isoformat(),
        window_end=end.isoformat(),
        purpose="live_window_indicator_signal_entry_parity",
        symbols=[json.loads((pack_dir / "strategy.json").read_text(encoding="utf-8"))["symbol"]],
        accepted_contamination=bool(args.i_accept_lockbox_contamination),
        open_finplot=False,
        accepted_finplot=False,
        notes="Same-geometry live history vs local recompute",
    )

    strategy = json.loads((pack_dir / "strategy.json").read_text(encoding="utf-8"))
    symbol = str(strategy["symbol"]).upper()
    timeframe = str(strategy["timeframe"])

    refresh_report = None
    if args.refresh_data or not args.no_refresh:
        refresh_report = refresh_local_data(symbol, timeframe)

    report = compare_live_window(
        pack_dir=pack_dir,
        live_df=live_df,
        single_book=not bool(args.multitrade),
    )
    out = {
        "experiment_id": EXPERIMENT_ID,
        "evidence_class": "LIVE_WINDOW_PARITY_DIAGNOSTIC_CONTAMINATED",
        "maximum_earned_readiness": "LIVE_STOP / RESEARCH_ONLY",
        "principal_blocker": (
            "Live-window parity is diagnostic (post-lockbox). "
            "Single-book BT uses max 1 position to match live."
        ),
        "forward_lockbox_start": FORWARD_LOCKBOX_START,
        "refresh": refresh_report,
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        **report,
    }
    # Drop full bars from stdout summary; keep in file
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    path = ARTIFACTS / "reports" / f"live_window_parity_{symbol}_{stamp}.json"
    latest = ARTIFACTS / "reports" / f"live_window_parity_{symbol}_latest.json"
    path.write_text(json.dumps(out, indent=2, default=str), encoding="utf-8")
    latest.write_text(json.dumps(out, indent=2, default=str), encoding="utf-8")

    summary = {
        "ok": report["features"]["n_feature_mismatch_bars"] == 0
        and (report["signals"]["side_match_rate_ungated_decide_once"] or 0) >= 0.99,
        "symbol": symbol,
        "n_live_decisions": report["n_live_decisions"],
        "window": [report["live_window_start"], report["live_window_end"]],
        "features": report["features"],
        "signals": report["signals"],
        "entries_same_geometry": {
            k: report["entries_same_geometry"][k]
            for k in (
                "live_entry_ok_bars",
                "live_position_already_open_bars",
                "bt_n_trades",
                "bt_n_skips",
                "bt_skip_reasons",
                "note",
            )
        },
        "report": str(path),
    }
    print(json.dumps(summary, indent=2, default=str))
    return 0 if summary["ok"] else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except PolicyError as e:
        print(json.dumps({"ok": False, "error": str(e)}), file=sys.stderr)
        raise SystemExit(2) from e
