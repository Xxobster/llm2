"""Position occupancy: concurrent open longs vs shorts on outer OOS."""

from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path

import numpy as np
import pandas as pd

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from scripts.run_live_fleet_concordance import FLEET, predict_sides  # noqa: E402
from llm2.live.multitrade import decide_entry_gate  # noqa: E402
from llm2.paths import ARTIFACTS, FORWARD_LOCKBOX_START  # noqa: E402
from llm2.validation.folds import OUTER_FOLD_RANGES  # noqa: E402


def single_book_open_side(df: pd.DataFrame, max_hold: int = 6) -> pd.Series:
    """Occupied side each bar: +1, -1, or 0."""
    sides = df["side"].to_numpy(dtype=int)
    n = len(sides)
    open_side = np.zeros(n, dtype=np.int8)
    busy_until = -1
    curr = 0
    for i in range(n):
        if i >= busy_until:
            curr = 0
        if curr == 0 and sides[i] != 0:
            curr = int(np.sign(sides[i]))
            busy_until = i + max_hold
        open_side[i] = curr
    return pd.Series(open_side, index=df.index)


def multitrade_open_counts(df: pd.DataFrame, mt_cfg: dict) -> tuple[pd.Series, pd.Series]:
    """Per-bar count of open long books and short books (simplified hold)."""
    sides = df["side"].to_numpy(dtype=int)
    means = df["mean"].to_numpy(dtype=float)
    n = len(sides)
    n_long = np.zeros(n, dtype=np.int16)
    n_short = np.zeros(n, dtype=np.int16)
    opens_long: list[int] = []
    opens_short: list[int] = []
    hist: list[float] = []
    for i in range(n):
        opens_long = [e for e in opens_long if e > i]
        opens_short = [e for e in opens_short if e > i]
        s = int(sides[i])
        if s != 0:
            n_open = len(opens_long) if s > 0 else len(opens_short)
            gate = decide_entry_gate(
                side=s,
                pred_mean=float(means[i]),
                n_open_same_side=n_open,
                strength_hist=hist,
                cfg=mt_cfg,
            )
            if gate.get("append_strength") or gate.get("allow"):
                hist.append(abs(float(means[i])))
                if len(hist) > int(mt_cfg["mean_lookback"]) * 4:
                    hist = hist[-int(mt_cfg["mean_lookback"]) * 4 :]
            if gate.get("allow"):
                hold = int(gate.get("max_hold_bars", mt_cfg["base_hold"]))
                exit_i = i + max(1, hold)
                if s > 0:
                    opens_long.append(exit_i)
                else:
                    opens_short.append(exit_i)
        n_long[i] = len(opens_long)
        n_short[i] = len(opens_short)
    return (
        pd.Series(n_long, index=df.index, name="n_long"),
        pd.Series(n_short, index=df.index, name="n_short"),
    )


def main() -> int:
    start = pd.Timestamp(OUTER_FOLD_RANGES[0][0], tz="UTC")
    end = pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC")
    acct = {b["bot_id"]: b["account"] for b in FLEET}
    results: dict = {}
    occ: dict = {}

    for bot in FLEET:
        pack = Path(bot["pack"])
        if not (pack / "model.joblib").is_file():
            continue
        print(f"sim {bot['bot_id']}", flush=True)
        df, meta = predict_sides(pack_dir=pack, start=start, end=end)
        mt = meta.get("multitrade")
        if mt:
            nl, ns = multitrade_open_counts(df, mt)
        else:
            oside = single_book_open_side(df, max_hold=6)
            nl = (oside > 0).astype(int)
            ns = (oside < 0).astype(int)
        occ[bot["bot_id"]] = (nl, ns, meta)
        results[bot["bot_id"]] = {
            "symbol": meta["symbol"],
            "account": bot["account"],
            "pct_time_long_open": float((nl > 0).mean()),
            "pct_time_short_open": float((ns > 0).mean()),
            "pct_time_both_sides_open": float(((nl > 0) & (ns > 0)).mean()),
            "mean_open_longs": float(nl.mean()),
            "mean_open_shorts": float(ns.mean()),
            "max_open_longs": int(nl.max()),
            "max_open_shorts": int(ns.max()),
        }

    xx7 = [bid for bid in occ if acct.get(bid) == "Xxobster7"]
    common = None
    for bid in xx7:
        common = (
            occ[bid][0].index
            if common is None
            else common.intersection(occ[bid][0].index)
        )
    assert common is not None

    n_long = pd.Series(0, index=common, dtype=int)
    n_short = pd.Series(0, index=common, dtype=int)
    for bid in xx7:
        nl, ns, _ = occ[bid]
        n_long = n_long + nl.reindex(common).fillna(0).astype(int)
        n_short = n_short + ns.reindex(common).fillna(0).astype(int)

    both = (n_long > 0) & (n_short > 0)
    n = len(common)
    pairs = list(zip(n_long[both].to_numpy(), n_short[both].to_numpy()))
    top = sorted(Counter(pairs).items(), key=lambda x: -x[1])[:25]

    all_ids = list(occ.keys())
    common2 = None
    for bid in all_ids:
        common2 = (
            occ[bid][0].index
            if common2 is None
            else common2.intersection(occ[bid][0].index)
        )
    assert common2 is not None
    n_long2 = pd.Series(0, index=common2, dtype=int)
    n_short2 = pd.Series(0, index=common2, dtype=int)
    for bid in all_ids:
        nl, ns, _ = occ[bid]
        n_long2 = n_long2 + nl.reindex(common2).fillna(0).astype(int)
        n_short2 = n_short2 + ns.reindex(common2).fillna(0).astype(int)
    both2 = (n_long2 > 0) & (n_short2 > 0)
    n2 = len(common2)
    pairs2 = list(zip(n_long2[both2].to_numpy(), n_short2[both2].to_numpy()))
    top2 = sorted(Counter(pairs2).items(), key=lambda x: -x[1])[:25]

    eth_mt = None
    for bid in all_ids:
        if "multitrade" in bid:
            nl, ns, _ = occ[bid]
            eth_mt = {
                "bot_id": bid,
                "pct_time_long_and_short_both_open": float(((nl > 0) & (ns > 0)).mean()),
                "n_bars_both": int(((nl > 0) & (ns > 0)).sum()),
                "n_bars": int(len(nl)),
                "mean_longs_when_both": float(nl[(nl > 0) & (ns > 0)].mean())
                if ((nl > 0) & (ns > 0)).any()
                else 0.0,
                "mean_shorts_when_both": float(ns[(nl > 0) & (ns > 0)].mean())
                if ((nl > 0) & (ns > 0)).any()
                else 0.0,
            }

    out = {
        "window": [str(start), str(end)],
        "caveat": (
            "Occupancy uses simplified max-hold (6h single-book; multitrade hold from "
            "gate). Not full Take Profit / Stop Loss exit path. Outer OOS only."
        ),
        "per_bot": results,
        "xxobster7_fleet_open": {
            "n_bars": n,
            "pct_time_any_long_open": float((n_long > 0).mean()),
            "pct_time_any_short_open": float((n_short > 0).mean()),
            "pct_time_long_and_short_both_open": float(both.mean()),
            "n_bars_long_and_short_both_open": int(both.sum()),
            "mean_open_longs_when_both": float(n_long[both].mean()) if both.any() else 0,
            "mean_open_shorts_when_both": float(n_short[both].mean())
            if both.any()
            else 0,
            "mean_total_books_when_both": float((n_long + n_short)[both].mean())
            if both.any()
            else 0,
            "mean_open_longs_all_bars": float(n_long.mean()),
            "mean_open_shorts_all_bars": float(n_short.mean()),
            "max_open_longs": int(n_long.max()),
            "max_open_shorts": int(n_short.max()),
            "top_long_short_count_pairs_when_both": [
                {
                    "n_long": int(a),
                    "n_short": int(b),
                    "bars": int(c),
                    "pct_of_both": float(c / both.sum()),
                }
                for (a, b), c in top
            ],
            "long_hist_all": {
                str(k): int(v) for k, v in zip(*np.unique(n_long, return_counts=True))
            },
            "short_hist_all": {
                str(k): int(v) for k, v in zip(*np.unique(n_short, return_counts=True))
            },
        },
        "full_live_fleet_incl_eth_multitrade": {
            "n_bars": n2,
            "pct_time_long_and_short_both_open": float(both2.mean()),
            "n_bars_long_and_short_both_open": int(both2.sum()),
            "mean_open_longs_when_both": float(n_long2[both2].mean())
            if both2.any()
            else 0,
            "mean_open_shorts_when_both": float(n_short2[both2].mean())
            if both2.any()
            else 0,
            "mean_total_books_when_both": float((n_long2 + n_short2)[both2].mean())
            if both2.any()
            else 0,
            "mean_open_longs_all_bars": float(n_long2.mean()),
            "mean_open_shorts_all_bars": float(n_short2.mean()),
            "max_open_longs": int(n_long2.max()),
            "max_open_shorts": int(n_short2.max()),
            "top_long_short_count_pairs_when_both": [
                {
                    "n_long": int(a),
                    "n_short": int(b),
                    "bars": int(c),
                    "pct_of_both": float(c / both2.sum()),
                }
                for (a, b), c in top2
            ],
        },
        "eth_multitrade_alone_both_sides": eth_mt,
    }

    path = ARTIFACTS / "reports" / "live_fleet_open_long_short_overlap_latest.json"
    path.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out["xxobster7_fleet_open"], indent=2))
    print("--- full fleet ---")
    print(json.dumps(out["full_live_fleet_incl_eth_multitrade"], indent=2))
    print("--- eth multi alone ---")
    print(json.dumps(eth_mt, indent=2))
    print("wrote", path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
