"""Print summary + compact JSON for canvas embed."""

from __future__ import annotations

import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "artifacts" / "reports" / "structure_v1_pred_mean_edge_sweep_001_latest.json"
OUT = ROOT / "artifacts" / "reports" / "structure_v1_pred_mean_edge_sweep_001_canvas.json"


def f(x):
    if x is None:
        return None
    try:
        v = float(x)
    except (TypeError, ValueError):
        return None
    if not math.isfinite(v):
        return None
    return v


def main() -> int:
    d = json.loads(SRC.read_text(encoding="utf-8"))
    rows = []
    for p in d["packs"]:
        if p.get("error"):
            continue
        live = bool((p.get("live") or {}).get("live_active"))
        for ek, m in (p.get("edges") or {}).items():
            rows.append(
                {
                    "version_id": p.get("version_id"),
                    "pack": p.get("pack"),
                    "symbol": p.get("symbol"),
                    "target": p.get("target"),
                    "mode": p.get("mode"),
                    "live": live,
                    "account": (p.get("live") or {}).get("account"),
                    "service": (p.get("live") or {}).get("service"),
                    "edge": f(m.get("pred_mean_edge")),
                    "n": int(m.get("n_trades") or 0),
                    "pf": f(m.get("profit_factor")),
                    "eru": f(m.get("expectancy_return_units")),
                    "eru_pct": (f(m.get("expectancy_return_units")) or 0) * 100
                    if f(m.get("expectancy_return_units")) is not None
                    else None,
                    "wr": f(m.get("win_rate")),
                    "net_pnl": f(m.get("net_pnl")),
                    "default": bool(m.get("is_pack_default_edge")),
                    "n_liq": int(m.get("n_liquidations") or 0),
                }
            )
    # filter n>0 for charts
    with_trades = [r for r in rows if r["n"] > 0 and r["eru"] is not None]
    top_eru = sorted(with_trades, key=lambda r: r["eru"] or -1e9, reverse=True)[:20]
    top_pf = sorted(
        [r for r in with_trades if r["n"] >= 50 and r["pf"] is not None],
        key=lambda r: r["pf"] or -1,
        reverse=True,
    )[:20]
    # per pack best and default
    by_pack = {}
    for r in with_trades:
        by_pack.setdefault(r["version_id"], []).append(r)
    best_per = []
    default_per = []
    for vid, items in by_pack.items():
        best = max(items, key=lambda r: r["eru"] or -1e9)
        best_per.append(best)
        pack_rows = [x for x in rows if x["version_id"] == vid]
        # live edge baseline for direction is 0.10
        base = None
        for x in pack_rows:
            if x.get("default") or (
                abs((x.get("edge") or 0) - 0.10) < 1e-9 and x["target"] == "direction"
            ):
                base = x
                break
        if base is None and pack_rows:
            # pack min edge cell
            edges_sorted = sorted(pack_rows, key=lambda r: r["edge"] or 99)
            base = edges_sorted[0]
        if base:
            default_per.append(base)
    best_per.sort(key=lambda r: r["eru"] or -1e9, reverse=True)

    # heatmap matrix: packs × edges for E[r]%
    edges = sorted({r["edge"] for r in rows if r["edge"] is not None})
    packs_order = sorted(
        {r["version_id"] for r in rows},
        key=lambda v: (
            0 if any(x["live"] and x["version_id"] == v for x in rows) else 1,
            v,
        ),
    )
    heat = []
    for vid in packs_order:
        cells = []
        for e in edges:
            hit = next(
                (r for r in rows if r["version_id"] == vid and abs((r["edge"] or -1) - e) < 1e-9),
                None,
            )
            cells.append(
                {
                    "edge": e,
                    "eru_pct": hit.get("eru_pct") if hit else None,
                    "pf": hit.get("pf") if hit else None,
                    "n": hit.get("n") if hit else 0,
                }
            )
        live_any = any(r["live"] and r["version_id"] == vid for r in rows)
        heat.append({"version_id": vid, "live": live_any, "cells": cells})

    # live packs at live edge 0.10 (or nearest default)
    live_rows = [r for r in rows if r["live"]]
    live_at_default = []
    for vid in sorted({r["version_id"] for r in live_rows}):
        cand = [r for r in live_rows if r["version_id"] == vid]
        pref = [r for r in cand if abs((r["edge"] or 0) - 0.10) < 1e-9]
        pick = pref[0] if pref else min(cand, key=lambda r: r["edge"] or 99)
        live_at_default.append(pick)

    payload = {
        "generation_id": d["generation_id"],
        "created_utc": d["created_utc"],
        "note": d.get("note"),
        "hard_end": d.get("hard_end_exclusive"),
        "edges": edges,
        "n_cells": len(rows),
        "n_with_trades": len(with_trades),
        "top_eru": top_eru,
        "top_pf": top_pf,
        "best_per_pack": best_per,
        "live_at_edge_0_10": live_at_default,
        "heatmap": heat,
        "all_rows": rows,
    }
    OUT.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print("wrote", OUT)
    print("LIVE at ~0.10:")
    for r in live_at_default:
        print(
            f"  LIVE {r['account']} {r['version_id'][:42]} e={r['edge']} n={r['n']} "
            f"eru%={(r['eru_pct'] or 0):.3f} pf={r['pf']}"
        )
    print("TOP E[r]:")
    for r in top_eru[:10]:
        print(
            f"  {'LIVE' if r['live'] else 'froz'} e={r['edge']} {r['version_id'][:36]} "
            f"n={r['n']} eru%={(r['eru_pct'] or 0):.3f} pf={r['pf']}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
