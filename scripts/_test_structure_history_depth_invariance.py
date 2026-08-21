"""Is the structure feature tip invariant to how much history precedes it?

Live fetches a bounded candle window; research uses the full warehouse. If the
tip feature vector depends on the length of the preceding history, live and
backtest can never agree, whatever else is fixed.

Recomputes the same evaluation bars from several history depths and reports the
first depth at which the tip stops moving.
"""

from __future__ import annotations

import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from tradesim.ensure_source import prefer_botsgeneral_tradesim

prefer_botsgeneral_tradesim()

import joblib  # noqa: E402
import json  # noqa: E402
import numpy as np  # noqa: E402

from llm2.data.loader import load_ohlcv  # noqa: E402
from llm2.features.registry import build_space  # noqa: E402
from llm2.paths import ARTIFACTS  # noqa: E402
from llm2.validation.folds import index_to_ms  # noqa: E402

SYMBOL = sys.argv[1] if len(sys.argv) > 1 else "ETHUSDT"
TF = "1h"
PACK = ARTIFACTS / "live_packs" / "structure_v1_ethusdt_k5_double3h_v1"
DEPTHS = [1_000, 2_000, 5_000, 10_000, 20_000, 40_000, None]
N_EVAL = 24

strategy = json.loads((PACK / "strategy.json").read_text(encoding="utf-8"))
blob = joblib.load(PACK / "model.joblib")
model = blob["model"] if isinstance(blob, dict) and "model" in blob else blob
cols = list(
    (blob.get("feature_columns") if isinstance(blob, dict) else None)
    or strategy["feature_columns"]
)

full = load_ohlcv(SYMBOL, TF)
print(f"{SYMBOL} {TF} warehouse bars={len(full)} tip={full.index[-1]}")


def tip_preds(depth: int | None) -> tuple[np.ndarray, np.ndarray]:
    o = full if depth is None else full.iloc[-int(depth) :]
    f = build_space(o, "structure_v1", symbol=SYMBOL, timeframe=TF, recent_only=False)
    a = f.reindex(columns=cols)
    for c in a.columns:
        if c == "last_retrace_pct" or str(c).startswith("last_retrace_pct_"):
            a[c] = a[c].fillna(0.0)
    v = a.dropna().iloc[-N_EVAL:]
    p = model.predict(v.to_numpy(dtype=float))
    m = np.asarray(p.mean if hasattr(p, "mean") else p, dtype=float).reshape(-1)
    return index_to_ms(v.index), m, v


ref_ts, ref_m, ref_v = tip_preds(None)
print(f"reference = full history, eval bars {len(ref_ts)}")
print(f"{'depth':>8s} {'max|dpred|':>12s} {'n_diff':>7s}  worst_features")
for d in DEPTHS:
    if d is None:
        continue
    ts, m, v = tip_preds(d)
    common = np.intersect1d(ts, ref_ts)
    i_a = np.searchsorted(ts, common)
    i_b = np.searchsorted(ref_ts, common)
    dp = np.abs(m[i_a] - ref_m[i_b])
    gaps = {}
    for c in cols:
        ga = np.abs(
            v[c].to_numpy(dtype=float)[i_a] - ref_v[c].to_numpy(dtype=float)[i_b]
        ).max()
        if ga > 1e-9:
            gaps[c] = float(ga)
    worst = sorted(gaps.items(), key=lambda kv: -kv[1])[:5]
    print(
        f"{d:8d} {float(dp.max()):12.6f} {int((dp > 1e-9).sum()):7d}  "
        f"{[(k, round(val, 5)) for k, val in worst]}"
    )
