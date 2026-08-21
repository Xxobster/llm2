"""Layer A lite: compare live-path (recent_only + pack slice) vs full warehouse features.

Default window ends at FORWARD_LOCKBOX_START (no contamination).
Reports per-column max abs / relative % deviation on overlapping bars.
"""

from __future__ import annotations

import argparse
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

from llm2.data.indicators import clear_indicator_cache, indicators_db_path  # noqa: E402
from llm2.data.loader import load_ohlcv  # noqa: E402
from llm2.evidence.lockbox_guard import add_lockbox_guard_args, require_lockbox_access  # noqa: E402
from llm2.features.registry import build_space  # noqa: E402
from llm2.paths import ARTIFACTS, FORWARD_LOCKBOX_START  # noqa: E402
from llm2.research_policy import PolicyError  # noqa: E402
from llm2.validation.folds import index_to_ms  # noqa: E402

EXPERIMENT_ID = "live_bt_indicator_parity_layer_a"


def _rel_pct(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    denom = np.maximum(np.abs(b), 1e-12)
    return 100.0 * (a - b) / denom


def compare_features(
    *,
    pack_dir: Path,
    start: pd.Timestamp,
    end: pd.Timestamp,
    abs_eps: float = 1e-9,
    rel_eps_pct: float = 1e-4,
) -> dict:
    strategy = json.loads((pack_dir / "strategy.json").read_text(encoding="utf-8"))
    symbol = str(strategy["symbol"]).upper()
    timeframe = str(strategy["timeframe"])
    cols = list(strategy.get("feature_columns") or [])
    if not cols:
        import joblib

        cols = list(joblib.load(pack_dir / "model.joblib")["feature_columns"])

    ohlcv = load_ohlcv(symbol, timeframe)
    if ohlcv.index.tz is None:
        ohlcv.index = ohlcv.index.tz_localize("UTC")
    # Need history before start for vol/HTF; evaluate overlap in [start, end)
    feat_ohlcv = ohlcv.loc[ohlcv.index < end].copy()

    clear_indicator_cache()
    os.environ.pop("LLM2_INDICATORS_DB", None)
    full = build_space(feat_ohlcv, "structure_v1", symbol=symbol, timeframe=timeframe, recent_only=False)
    full = full.reindex(columns=cols)

    # Primary drift risk: recent_only on the SAME warehouse (not the pack slice).
    # Pack slices are often tip-only and cannot rebuild multi-year overlap.
    clear_indicator_cache()
    live = build_space(
        feat_ohlcv,
        "structure_v1",
        symbol=symbol,
        timeframe=timeframe,
        recent_only=True,
    )
    live = live.reindex(columns=cols)
    live_src = str(indicators_db_path()) + " (recent_only=True)"

    # Optional: pack-slice tip check on last N bars only
    slice_db = pack_dir / "indicators_live_slice.sqlite"
    slice_tip = None
    if slice_db.is_file():
        try:
            os.environ["LLM2_INDICATORS_DB"] = str(slice_db.resolve())
            clear_indicator_cache()
            tip_ohlcv = feat_ohlcv.tail(500)
            tip_full = full.reindex(tip_ohlcv.index)
            tip_live = build_space(
                tip_ohlcv,
                "structure_v1",
                symbol=symbol,
                timeframe=timeframe,
                recent_only=True,
            ).reindex(columns=cols)
            tip_live = tip_live.reindex(tip_full.index)
            last = tip_full.dropna(how="all").index[-1] if len(tip_full.dropna(how="all")) else None
            if last is not None and last in tip_live.index and tip_live.loc[last].notna().any():
                fa = tip_full.loc[last].to_numpy(dtype=float)
                la = tip_live.loc[last].to_numpy(dtype=float)
                ok = np.isfinite(fa) & np.isfinite(la)
                d_abs = np.abs(la[ok] - fa[ok]) if ok.any() else np.asarray([])
                slice_tip = {
                    "slice_db": str(slice_db),
                    "tip_bar": str(last),
                    "n_finite_cols": int(ok.sum()),
                    "max_abs_diff": float(np.nanmax(d_abs)) if d_abs.size else None,
                    "n_mismatch_cols": int(np.sum(d_abs > abs_eps)) if d_abs.size else None,
                }
        except Exception as exc:  # noqa: BLE001
            slice_tip = {"slice_db": str(slice_db), "error": f"{type(exc).__name__}: {exc}"}
        finally:
            os.environ.pop("LLM2_INDICATORS_DB", None)
            clear_indicator_cache()

    # Overlap window
    mask = (full.index >= start) & (full.index < end)
    f = full.loc[mask]
    l = live.reindex(f.index)
    both = f.notna() & l.notna()

    per_col = []
    mismatch_bars = 0
    n_bars = int(len(f))
    for c in cols:
        fa = f[c].to_numpy(dtype=float)
        la = l[c].to_numpy(dtype=float)
        ok = both[c].to_numpy()
        if not ok.any():
            per_col.append({"column": c, "n_overlap": 0, "status": "NO_OVERLAP"})
            continue
        d_abs = np.abs(la[ok] - fa[ok])
        d_rel = np.abs(_rel_pct(la[ok], fa[ok]))
        n_bad = int(np.sum((d_abs > abs_eps) & (d_rel > rel_eps_pct)))
        if n_bad:
            mismatch_bars = max(mismatch_bars, n_bad)
        per_col.append(
            {
                "column": c,
                "n_overlap": int(ok.sum()),
                "n_mismatch": n_bad,
                "mismatch_rate": float(n_bad / ok.sum()),
                "max_abs_diff": float(np.nanmax(d_abs)) if d_abs.size else None,
                "max_rel_pct": float(np.nanmax(d_rel)) if d_rel.size else None,
                "median_abs_diff": float(np.nanmedian(d_abs)) if d_abs.size else None,
            }
        )

    # Bar-level: any column mismatch
    bar_bad = np.zeros(n_bars, dtype=bool)
    for c in cols:
        fa = f[c].to_numpy(dtype=float)
        la = l[c].to_numpy(dtype=float)
        ok = both[c].to_numpy()
        bad = ok & (np.abs(la - fa) > abs_eps) & (np.abs(_rel_pct(la, fa)) > rel_eps_pct)
        bar_bad |= bad
    n_bad_bars = int(bar_bad.sum())

    # pred_mean / side optional if model present
    signal = None
    model_path = pack_dir / "model.joblib"
    if model_path.is_file() and n_bars > 0:
        import joblib

        from llm2.hunt.targets import DIRECTION_BAND, proxy_side, target_family
        from llm2.paths import ROUND_TRIP_COST

        blob = joblib.load(model_path)
        model = blob["model"]
        # dropna rows for model
        aligned_f = f.dropna()
        aligned_l = l.reindex(aligned_f.index).dropna()
        common = aligned_f.index.intersection(aligned_l.index)
        if len(common) > 0:
            Xf = aligned_f.loc[common].to_numpy(dtype=float)
            Xl = aligned_l.loc[common].to_numpy(dtype=float)
            pf = model.predict(Xf)
            pl = model.predict(Xl)
            mf = np.asarray(pf.mean if getattr(pf, "mean", None) is not None else pf, dtype=float).reshape(-1)
            ml = np.asarray(pl.mean if getattr(pl, "mean", None) is not None else pl, dtype=float).reshape(-1)
            family = target_family(str(strategy.get("target", "fwd_return")))
            edge = float(strategy.get("min_edge", DIRECTION_BAND if family == "directional" else ROUND_TRIP_COST))
            if family == "directional" and abs(edge - ROUND_TRIP_COST) < 1e-12:
                edge = DIRECTION_BAND
            sf = proxy_side(mf, family)
            sl_ = proxy_side(ml, family)
            sf = np.where(np.abs(mf) >= edge, sf, 0)
            sl_ = np.where(np.abs(ml) >= edge, sl_, 0)
            signal = {
                "n_bars": int(len(common)),
                "pred_mean_max_abs_diff": float(np.nanmax(np.abs(ml - mf))),
                "pred_mean_max_rel_pct": float(np.nanmax(np.abs(_rel_pct(ml, mf)))),
                "side_match_rate": float(np.mean(sf == sl_)),
                "n_side_mismatch": int(np.sum(sf != sl_)),
            }

    worst = sorted(
        [c for c in per_col if c.get("n_mismatch", 0) > 0],
        key=lambda x: (-x.get("mismatch_rate", 0), -x.get("max_rel_pct") or 0),
    )[:15]

    return {
        "pack": str(pack_dir),
        "symbol": symbol,
        "timeframe": timeframe,
        "live_feature_source": live_src,
        "warehouse_db": str(indicators_db_path()),
        "pack_slice_tip": slice_tip,
        "window_start": start.isoformat(),
        "window_end_exclusive": end.isoformat(),
        "n_bars": n_bars,
        "n_mismatch_bars": n_bad_bars,
        "bar_match_rate": float(1.0 - n_bad_bars / n_bars) if n_bars else None,
        "abs_eps": abs_eps,
        "rel_eps_pct": rel_eps_pct,
        "worst_columns": worst,
        "n_columns_with_mismatch": sum(1 for c in per_col if c.get("n_mismatch", 0) > 0),
        "n_columns": len(cols),
        "signal": signal,
        "per_column": per_col,
    }


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--pack",
        type=Path,
        default=ARTIFACTS / "live_packs" / "structure_v1_ethusdt_direction",
    )
    ap.add_argument("--start", default="2025-10-01")
    ap.add_argument("--end", default=FORWARD_LOCKBOX_START)
    add_lockbox_guard_args(ap)
    args = ap.parse_args(argv)

    start = pd.Timestamp(args.start, tz="UTC")
    end = pd.Timestamp(args.end, tz="UTC")
    peek = require_lockbox_access(
        experiment_id=EXPERIMENT_ID,
        window_start=start.isoformat(),
        window_end=end.isoformat(),
        purpose="indicator_live_path_vs_full_warehouse",
        accepted_contamination=bool(args.i_accept_lockbox_contamination),
        open_finplot=False,
        accepted_finplot=False,
    )
    report = compare_features(pack_dir=args.pack.resolve(), start=start, end=end)
    evidence = (
        "LIVE_BT_INDICATOR_PARITY"
        if peek is None
        else "LIVE_BT_INDICATOR_PARITY_CONTAMINATED"
    )
    out = {
        "experiment_id": EXPERIMENT_ID,
        "evidence_class": evidence,
        "maximum_earned_readiness": "LIVE_STOP / RESEARCH_ONLY",
        "principal_blocker": (
            "Indicator parity is a calculation check only; does not authorize live."
            if report["n_mismatch_bars"] == 0
            else "Feature mismatch between live path and full warehouse — stop and fix before trusting signals."
        ),
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        **report,
    }
    out_dir = ARTIFACTS / "reports"
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    path = out_dir / f"live_bt_indicator_parity_{stamp}.json"
    latest = out_dir / "live_bt_indicator_parity_latest.json"
    text = json.dumps(out, indent=2, default=lambda x: None if isinstance(x, float) and not np.isfinite(x) else x)
    path.write_text(text, encoding="utf-8")
    latest.write_text(text, encoding="utf-8")
    print(
        json.dumps(
            {
                "ok": report["n_mismatch_bars"] == 0,
                "evidence_class": evidence,
                "n_bars": report["n_bars"],
                "n_mismatch_bars": report["n_mismatch_bars"],
                "bar_match_rate": report["bar_match_rate"],
                "n_columns_with_mismatch": report["n_columns_with_mismatch"],
                "signal": report["signal"],
                "worst_columns": report["worst_columns"][:5],
                "report": str(path),
            },
            indent=2,
        )
    )
    return 0 if report["n_mismatch_bars"] == 0 else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except PolicyError as exc:
        print(json.dumps({"ok": False, "error": str(exc)}), file=sys.stderr)
        raise SystemExit(2) from exc
