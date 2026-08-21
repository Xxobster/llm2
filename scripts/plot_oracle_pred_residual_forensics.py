"""Contamination forensics only: residual oracle_leaky − pred_leaky (future-swing gap).

Loads the sealed as-of HistGradientBoosting proxy series. Does NOT retrain for profit
and loss (P&L). Does NOT freeze packs. Promotion forbidden (D-058).

Optional Finplot of residual requires explicit contamination + Finplot flags
(lockbox-safe outer-only view; does not open FORWARD_LOCKBOX_START for ranking).
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from tradesim.ensure_source import prefer_botsgeneral_tradesim  # noqa: E402

prefer_botsgeneral_tradesim()

from llm2.data.loader import load_ohlcv  # noqa: E402
from llm2.paths import ARTIFACTS, FORWARD_LOCKBOX_START  # noqa: E402

OUT_DIR = ARTIFACTS / "reports" / "oracle_pred_residual_forensics_001"
SERIES_PATH = (
    ARTIFACTS / "reports" / "leaky_proxy_asof_max_001" / "leaky_asof_series.parquet"
)
OUTER0 = pd.Timestamp("2026-01-01", tz="UTC")
OUTER1 = pd.Timestamp(str(FORWARD_LOCKBOX_START))
if OUTER1.tzinfo is None:
    OUTER1 = OUTER1.tz_localize("UTC")
else:
    OUTER1 = OUTER1.tz_convert("UTC")


def _summarize(res: pd.Series) -> dict:
    x = res.dropna().to_numpy(dtype=float)
    if x.size == 0:
        return {"n": 0}
    return {
        "n": int(x.size),
        "mean": float(np.mean(x)),
        "std": float(np.std(x)),
        "mae": float(np.mean(np.abs(x))),
        "rmse": float(np.sqrt(np.mean(x * x))),
        "p05": float(np.quantile(x, 0.05)),
        "p50": float(np.quantile(x, 0.50)),
        "p95": float(np.quantile(x, 0.95)),
        "frac_abs_gt_0_25": float(np.mean(np.abs(x) > 0.25)),
        "frac_abs_gt_0_50": float(np.mean(np.abs(x) > 0.50)),
        "frac_abs_gt_1_00": float(np.mean(np.abs(x) > 1.0)),
    }


def plot_hist(res_outer: pd.Series, path: Path) -> None:
    x = res_outer.dropna().to_numpy(dtype=float)
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.hist(x, bins=80, color="#4c6a91", edgecolor="white", alpha=0.9)
    ax.axvline(0.0, color="#222", linewidth=1.0, linestyle="--")
    ax.set_title(
        "Forensics only: residual = oracle_leaky − pred_leaky (outer, causal max proxy)"
    )
    ax.set_xlabel("residual (look-ahead gap not closed by causal features)")
    ax.set_ylabel("count")
    fig.tight_layout()
    fig.savefig(path, dpi=140)
    plt.close(fig)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--show-finplot",
        action="store_true",
        help="Open residual Finplot (forensics only; never a promotion chart).",
    )
    ap.add_argument(
        "--i-accept-contamination-forensics",
        action="store_true",
        help="Required. Confirms residual is contamination forensics, not an alpha track.",
    )
    args = ap.parse_args()
    if not args.i_accept_contamination_forensics:
        print(
            "Refusing: residual chart is contamination forensics only. "
            "Pass --i-accept-contamination-forensics.",
            file=sys.stderr,
        )
        return 2
    if not SERIES_PATH.is_file():
        raise SystemExit(f"missing series parquet: {SERIES_PATH}")

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    series = pd.read_parquet(SERIES_PATH)
    idx = pd.to_datetime(series.index, utc=True)
    series = series.copy()
    series.index = idx
    need = ("oracle_leaky", "pred_leaky")
    for c in need:
        if c not in series.columns:
            raise SystemExit(f"series missing {c}")
    series["residual"] = series["oracle_leaky"] - series["pred_leaky"]
    # Align Timestamp unit to the parquet index unit (often ms).
    unit = getattr(idx, "unit", "ns")
    outer0 = OUTER0.as_unit(unit)
    outer1 = OUTER1.as_unit(unit)
    outer_mask = (idx >= outer0) & (idx < outer1)
    res_outer = series.loc[outer_mask, "residual"]
    stats = {
        "evidence_class": "CONTAMINATION_FORENSICS",
        "maximum_earned_readiness": "LIVE_STOP / RESEARCH_ONLY",
        "promotion_allowed": False,
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "series_path": str(SERIES_PATH),
        "outer_window": [str(OUTER0), str(OUTER1)],
        "residual_all": _summarize(series["residual"]),
        "residual_outer": _summarize(res_outer),
        "note": (
            "Residual is the future-swing gap under no-leakage. "
            "Do not freeze packs on pred_leaky or oracle_leaky. "
            "Do not optimize residual for profit and loss."
        ),
    }
    hist_path = OUT_DIR / "residual_histogram_outer.png"
    plot_hist(res_outer, hist_path)
    stats["histogram_png"] = str(hist_path)
    series.loc[outer_mask, ["oracle_leaky", "pred_leaky", "residual"]].to_parquet(
        OUT_DIR / "residual_outer.parquet"
    )
    latest = OUT_DIR / "oracle_pred_residual_forensics_001_latest.json"
    latest.write_text(json.dumps(stats, indent=2, default=str), encoding="utf-8")
    print(json.dumps(stats, indent=2, default=str))
    print(f"WROTE {hist_path}")
    print(f"WROTE {latest}")

    if args.show_finplot:
        import finplot as fplt  # noqa: WPS

        ohlcv = load_ohlcv("ETHUSDT", "1h")
        ohlcv = ohlcv.loc[(ohlcv.index >= OUTER0) & (ohlcv.index < OUTER1)].copy()
        res = series["residual"].reindex(ohlcv.index)
        ax, axr = fplt.create_plot(
            "Forensics: oracle_leaky − pred_leaky residual (ETHUSDT 1h outer)", rows=2
        )
        candles = ohlcv[["open", "close", "high", "low"]].copy()
        fplt.candlestick_ochl(candles, ax=ax)
        fplt.plot(res, ax=axr, legend="residual (oracle − pred)", color="#c44e52")
        fplt.add_line((ohlcv.index[0], 0.0), (ohlcv.index[-1], 0.0), color="#888", ax=axr)
        fplt.show()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
