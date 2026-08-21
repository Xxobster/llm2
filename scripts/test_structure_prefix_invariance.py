"""Prefix-invariance of structure_v1: does bar T change when future bars arrive?

Live computes bar T from candles up to T. Research recomputes the whole history
later, so if a row at T is rewritten once later bars confirm a swing, live and
backtest can never agree on anything except the newest bars — and the research
number is look-ahead.

For each cutoff T: rebuild features from OHLCV truncated at T and compare the row
at T with the same row from the full series.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from tradesim.ensure_source import prefer_botsgeneral_tradesim

prefer_botsgeneral_tradesim()

import joblib  # noqa: E402
import numpy as np  # noqa: E402

from llm2.data.loader import load_ohlcv  # noqa: E402
from llm2.features.registry import build_space  # noqa: E402
from llm2.paths import ARTIFACTS  # noqa: E402
from llm2.validation.folds import index_to_ms  # noqa: E402

SYMBOL = sys.argv[1] if len(sys.argv) > 1 else "ETHUSDT"
TF = "1h"
PACK_NAME = {
    "ETHUSDT": "structure_v1_ethusdt_k5_double3h_v1",
    "BTCUSDT": "structure_v1_btcusdt_k5_double3h_v1",
    "SOLUSDT": "structure_v1_solusdt_k5_double3h_v1",
}[SYMBOL]
N_CUTOFFS = int(sys.argv[2]) if len(sys.argv) > 2 else 30

pack = ARTIFACTS / "live_packs" / PACK_NAME
strategy = json.loads((pack / "strategy.json").read_text(encoding="utf-8"))
blob = joblib.load(pack / "model.joblib")
model = blob["model"] if isinstance(blob, dict) and "model" in blob else blob
cols = list(
    (blob.get("feature_columns") if isinstance(blob, dict) else None)
    or strategy["feature_columns"]
)

full_ohlcv = load_ohlcv(SYMBOL, TF)
print(f"{SYMBOL} {TF} bars={len(full_ohlcv)} tip={full_ohlcv.index[-1]}")


def feats_for(ohlcv):
    f = build_space(ohlcv, "structure_v1", symbol=SYMBOL, timeframe=TF, recent_only=False)
    a = f.reindex(columns=cols)
    for c in a.columns:
        if c == "last_retrace_pct" or str(c).startswith("last_retrace_pct_"):
            a[c] = a[c].fillna(0.0)
    return a.dropna()


full_f = feats_for(full_ohlcv)
p = model.predict(full_f.to_numpy(dtype=float))
full_pred = np.asarray(p.mean if hasattr(p, "mean") else p, dtype=float).reshape(-1)
full_ts = index_to_ms(full_f.index)
full_by = {int(t): i for i, t in enumerate(full_ts)}

cut_ts = [int(t) for t in full_ts[-N_CUTOFFS:]]
print(f"\n{'cutoff_bar_utc':22s} {'trunc_pred':>11s} {'full_pred':>11s} {'diff':>10s}  changed_features")
n_same = 0
offenders: dict[str, int] = {}
for t in cut_ts:
    cut = full_ohlcv.loc[full_ohlcv.index <= full_f.index[full_by[t]]]
    tf_ = feats_for(cut)
    if len(tf_) == 0 or index_to_ms(tf_.index)[-1] != t:
        print(f"{str(tf_.index[-1] if len(tf_) else '-'):22s}  (no row at cutoff)")
        continue
    row_t = tf_.iloc[-1]
    row_f = full_f.iloc[full_by[t]]
    pt = model.predict(row_t.to_numpy(dtype=float).reshape(1, -1))
    pt = float(np.asarray(pt.mean if hasattr(pt, "mean") else pt).reshape(-1)[0])
    pf_ = float(full_pred[full_by[t]])
    changed = [
        c
        for c in cols
        if abs(float(row_t[c]) - float(row_f[c])) > 1e-9
    ]
    for c in changed:
        offenders[c] = offenders.get(c, 0) + 1
    if abs(pt - pf_) <= 1e-9:
        n_same += 1
    print(
        f"{str(tf_.index[-1])[:19]:22s} {pt:11.5f} {pf_:11.5f} {pt - pf_:10.5f}  "
        f"{changed[:6]}{'…' if len(changed) > 6 else ''}"
    )

print(f"\nprefix-invariant bars: {n_same}/{len(cut_ts)}")
print("columns that change when future bars arrive (count):")
for c, n in sorted(offenders.items(), key=lambda kv: -kv[1]):
    print(f"  {c:32s} {n}")
if n_same != len(cut_ts):
    print("\nVERDICT: structure_v1 is NOT prefix-invariant -> research rows are")
    print("rewritten by later bars; live can never reproduce them.")
else:
    print("\nVERDICT: prefix-invariant.")
