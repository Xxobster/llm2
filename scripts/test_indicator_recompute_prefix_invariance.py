"""Does recomputing the structure indicator with more candles rewrite past rows?

This is the live path: every hour the bot recomputes the whole structure series
from candles up to now and writes the pack slice. Research computed the same
series once, later, from a longer history. If the row for bar T differs between
"computed when T was the tip" and "computed after T+k arrived", live and backtest
predictions cannot agree on anything except the newest bars.

Recomputes the indicator into a temporary warehouse at several cutoffs and
compares the model input row (and prediction) at the cutoff bar.
"""

from __future__ import annotations

import json
import os
import sys
import tempfile
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))
sys.path.insert(0, r"C:\projects\botsgeneral\packages\indicators\src")

from tradesim.ensure_source import prefer_botsgeneral_tradesim

prefer_botsgeneral_tradesim()

import joblib  # noqa: E402
import numpy as np  # noqa: E402

from indicators.compute import compute_structure  # noqa: E402
from indicators.store import IndicatorDB  # noqa: E402

from llm2.data.indicators import clear_indicator_cache  # noqa: E402
from llm2.data.loader import load_ohlcv  # noqa: E402
from llm2.features.registry import build_space  # noqa: E402
from llm2.paths import ARTIFACTS  # noqa: E402
from llm2.validation.folds import index_to_ms  # noqa: E402

SYMBOL = sys.argv[1] if len(sys.argv) > 1 else "ETHUSDT"
N_CUTOFFS = int(sys.argv[2]) if len(sys.argv) > 2 else 12
TF = "1h"
HTFS = ("1h", "4h", "1w")
PACK_NAME = {
    "ETHUSDT": "structure_v1_ethusdt_k5_double3h_v1",
    "BTCUSDT": "structure_v1_btcusdt_k5_double3h_v1",
    "SOLUSDT": "structure_v1_solusdt_k5_double3h_v1",
}[SYMBOL]

pack = ARTIFACTS / "live_packs" / PACK_NAME
strategy = json.loads((pack / "strategy.json").read_text(encoding="utf-8"))
blob = joblib.load(pack / "model.joblib")
model = blob["model"] if isinstance(blob, dict) and "model" in blob else blob
cols = list(
    (blob.get("feature_columns") if isinstance(blob, dict) else None)
    or strategy["feature_columns"]
)

series = {tf: load_ohlcv(SYMBOL, tf) for tf in HTFS}
print(f"{SYMBOL} warehouse: " + ", ".join(f"{tf} n={len(series[tf])}" for tf in HTFS))


def _predict(row) -> float:
    p = model.predict(np.asarray(row, dtype=float).reshape(1, -1))
    return float(np.asarray(p.mean if hasattr(p, "mean") else p).reshape(-1)[0])


def _feats(ohlcv):
    clear_indicator_cache()
    f = build_space(ohlcv, "structure_v1", symbol=SYMBOL, timeframe=TF, recent_only=False)
    a = f.reindex(columns=cols)
    for c in a.columns:
        if c == "last_retrace_pct" or str(c).startswith("last_retrace_pct_"):
            a[c] = a[c].fillna(0.0)
    return a.dropna()


def _build_warehouse(db_path: Path, cutoff_ts) -> None:
    ind = IndicatorDB(db_path)
    for tf in HTFS:
        o = series[tf]
        o = o.loc[o.index <= cutoff_ts]
        if len(o) < 60:
            continue
        bundle = compute_structure(
            o.reset_index(drop=True), source="binance", symbol=SYMBOL, timeframe=tf
        )
        ind.upsert_bundle(bundle)


# Control: recompute the whole series with the same code and the same candles, no
# cutoff. Comparing cutoff-recompute against *this* isolates prefix-invariance from
# "my recompute used a different history than the shipped warehouse".
tmp0 = Path(tempfile.mkdtemp(prefix="prefix_inv_ctl_"))
ctl_db = tmp0 / "ind_full.sqlite"
_build_warehouse(ctl_db, series[TF].index[-1])
os.environ["LLM2_INDICATORS_DB"] = str(ctl_db)
try:
    ref_f = _feats(series[TF])
finally:
    os.environ.pop("LLM2_INDICATORS_DB", None)
    clear_indicator_cache()

# Sanity: does the shipped research warehouse agree with the control recompute?
warehouse_f = _feats(series[TF])
common = warehouse_f.index.intersection(ref_f.index)[-N_CUTOFFS:]
n_wh_diff = int(
    sum(
        1
        for ts in common
        if any(
            abs(float(warehouse_f.loc[ts, c]) - float(ref_f.loc[ts, c])) > 1e-9
            for c in cols
        )
    )
)
print(
    f"control check: shipped warehouse vs full recompute differ on "
    f"{n_wh_diff}/{len(common)} of the last bars"
)

ref_ts = index_to_ms(ref_f.index)
ref_by = {int(t): i for i, t in enumerate(ref_ts)}
cutoffs = list(ref_f.index[-N_CUTOFFS:])

print(f"\n{'cutoff (was tip)':22s} {'live-style':>11s} {'research':>11s} {'diff':>10s}  rewritten_columns")
tmp = Path(tempfile.mkdtemp(prefix="prefix_inv_"))
n_same = 0
offenders: dict[str, int] = {}
for ts in cutoffs:
    db = tmp / f"ind_{int(ts.value // 1_000_000)}.sqlite"
    _build_warehouse(db, ts)
    os.environ["LLM2_INDICATORS_DB"] = str(db)
    o_cut = series[TF].loc[series[TF].index <= ts]
    try:
        cut_f = _feats(o_cut)
    finally:
        os.environ.pop("LLM2_INDICATORS_DB", None)
        clear_indicator_cache()
    if len(cut_f) == 0 or cut_f.index[-1] != ts:
        print(f"{str(ts)[:19]:22s}  (no feature row at cutoff)")
        continue
    row_live = cut_f.iloc[-1]
    row_res = ref_f.iloc[ref_by[int(ts.value // 1_000_000)]]
    changed = [c for c in cols if abs(float(row_live[c]) - float(row_res[c])) > 1e-9]
    for c in changed:
        offenders[c] = offenders.get(c, 0) + 1
    p_live = _predict(row_live.to_numpy())
    p_res = _predict(row_res.to_numpy())
    if abs(p_live - p_res) <= 1e-9:
        n_same += 1
    print(
        f"{str(ts)[:19]:22s} {p_live:11.5f} {p_res:11.5f} {p_live - p_res:10.5f}  "
        f"{changed[:5]}{'…' if len(changed) > 5 else ''}"
    )

print(f"\nidentical at cutoff: {n_same}/{len(cutoffs)}")
if offenders:
    print("columns rewritten by later candles (count of cutoffs):")
    for c, n in sorted(offenders.items(), key=lambda kv: -kv[1]):
        print(f"  {c:32s} {n}")
    print(
        "\nVERDICT: the indicator is NOT prefix-invariant. Research rows for bar T "
        "are rewritten once later bars arrive, so live (which only ever sees data "
        "up to T) cannot reproduce them."
    )
else:
    print("\nVERDICT: prefix-invariant — divergence must come from data or state.")
