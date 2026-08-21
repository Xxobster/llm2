"""Bar-by-bar live pred_mean vs local recompute for one unit (diagnosis helper)."""

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
from llm2.hunt.targets import proxy_side, target_family  # noqa: E402
from llm2.paths import ARTIFACTS  # noqa: E402
from llm2.validation.folds import index_to_ms  # noqa: E402

KEY = sys.argv[1] if len(sys.argv) > 1 else "llm2-structure-eth-k5-double3h-v1"
PACK = sys.argv[2] if len(sys.argv) > 2 else "structure_v1_ethusdt_k5_double3h_v1"

led = json.loads(
    (ARTIFACTS / "reports" / "_llm2_ln1_all_unit_ledgers.json").read_text(encoding="utf-8")
)[KEY]
pack = ARTIFACTS / "live_packs" / PACK
strategy = json.loads((pack / "strategy.json").read_text(encoding="utf-8"))
blob = joblib.load(pack / "model.joblib")
model = blob["model"] if isinstance(blob, dict) and "model" in blob else blob
cols = list((blob.get("feature_columns") if isinstance(blob, dict) else None) or strategy["feature_columns"])
symbol, tf = strategy["symbol"], strategy["timeframe"]
family = target_family(str(strategy.get("target")))

decs = sorted(led["decisions"], key=lambda d: d["bar_ts_ms"])
first, last = decs[0]["bar_ts_ms"], decs[-1]["bar_ts_ms"]

o = load_ohlcv(symbol, tf)
ms = index_to_ms(o.index)
o = o.loc[(ms >= first - 900 * 3_600_000) & (ms <= last + 3_600_000)].copy()
feats = build_space(o, "structure_v1", symbol=symbol, timeframe=tf, recent_only=False)
al = feats.reindex(columns=cols)
for c in al.columns:
    if c == "last_retrace_pct" or str(c).startswith("last_retrace_pct_"):
        al[c] = al[c].fillna(0.0)
v = al.dropna()
p = model.predict(v.to_numpy(dtype=float))
mean = np.asarray(p.mean if hasattr(p, "mean") else p, dtype=float).reshape(-1)
side = proxy_side(mean, family)
by = {int(t): (mean[i], int(side[i])) for i, t in enumerate(index_to_ms(v.index))}

print(f"{KEY}  {symbol} {tf} target={strategy.get('target')} cols={len(cols)}")
print(f"{'bar_utc':22s} {'live':>9s} {'local':>9s} {'diff':>9s} {'lsd':>4s} {'bsd':>4s}  snap")
n_ok = 0
for d in decs:
    t = int(d["bar_ts_ms"])
    lv = d.get("pred_mean")
    if lv is None or t not in by:
        continue
    lc, sd = by[t]
    diff = lc - float(lv)
    if abs(diff) <= 1e-9:
        n_ok += 1
    det = d.get("detail") or {}
    snap = "Y" if (det.get("feature_snapshot") or {}).get("sha256") else "-"
    print(
        f"{d['bar_utc'][:19]:22s} {float(lv):9.5f} {lc:9.5f} {diff:9.5f} "
        f"{int(d.get('side') or 0):4d} {sd:4d}  {snap}"
    )
print(f"identical={n_ok}/{sum(1 for d in decs if d.get('pred_mean') is not None)}")
