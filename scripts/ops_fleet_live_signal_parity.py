#!/usr/bin/env python3
"""ops_fleet_live_signal_parity — Fleet Live Signal Parity gate.

**Name (human):** Fleet Live Signal Parity
**Evidence class:** ``OPS_FLEET_LIVE_SIGNAL_PARITY``
**Scope:** For every active structure unit on ln1 (94.x) and ln3 (185.x), compare
the unit's last 1h decision ``pred_mean`` + side to a local warehouse recompute
using the matching frozen live pack + research ``indicators.sqlite``.

Diagnostic ops check only — ``LIVE_STOP / RESEARCH_ONLY``. No orders.
Does **not** replace single-unit ``ops_live_research_parity_gate.py`` (deep tip +
feature snapshot for one unit) or the 1m indicator diagnostic bot.

Run anytime (after a closed 1h bar is ideal)::

  python scripts/ops_fleet_live_signal_parity.py
  python scripts/ops_fleet_live_signal_parity.py --host ln1
  python scripts/ops_fleet_live_signal_parity.py --bar-ts-ms 1785934800000
  python scripts/ops_fleet_live_signal_parity.py --strict-indicators

Reports:
  artifacts/reports/ops_fleet_live_signal_parity_latest.json
  artifacts/reports/ops_fleet_live_signal_parity_<stamp>.json
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.ops_live_research_parity_gate import (  # noqa: E402
    compare_pack_tip_to_research,
    pull_live_decision,
    recompute_pred_mean,
)

# --- Stable naming -----------------------------------------------------------
GATE_NAME = "Fleet Live Signal Parity"
EVIDENCE_CLASS = "OPS_FLEET_LIVE_SIGNAL_PARITY"
REPORT_STEM = "ops_fleet_live_signal_parity"
REPORTS = ROOT / "artifacts" / "reports"
PACKS = ROOT / "artifacts" / "live_packs"
TF_MS_1H = 3_600_000
PRED_ABS_EPS = 1e-6

# Active fleet registry: edit here when adding/removing units or packs.
# host aliases: ln1 = 94.x fleet host; ln3 = 185.x p75 host.
FLEET_REGISTRY: list[dict] = [
    # ln1 94.x
    {
        "host": "ln1",
        "host_class": "94.x",
        "unit": "llm2-structure-eth",
        "pack": "structure_v1_ethusdt_direction",
        "symbol": "ETHUSDT",
    },
    {
        "host": "ln1",
        "host_class": "94.x",
        "unit": "llm2-structure-sol",
        "pack": "structure_v1_solusdt_direction",
        "symbol": "SOLUSDT",
    },
    {
        "host": "ln1",
        "host_class": "94.x",
        "unit": "llm2-structure-micro",
        "pack": "structure_v1_lgbm",
        "symbol": "BTCUSDT",
    },
    {
        "host": "ln1",
        "host_class": "94.x",
        "unit": "llm2-structure-eth-k5-double3h-v1",
        "pack": "structure_v1_ethusdt_k5_double3h_v1",
        "symbol": "ETHUSDT",
    },
    {
        "host": "ln1",
        "host_class": "94.x",
        "unit": "llm2-structure-btc-k5-double3h-v1",
        "pack": "structure_v1_btcusdt_k5_double3h_v1",
        "symbol": "BTCUSDT",
    },
    {
        "host": "ln1",
        "host_class": "94.x",
        "unit": "llm2-structure-sol-k5-double3h-v1",
        "pack": "structure_v1_solusdt_k5_double3h_v1",
        "symbol": "SOLUSDT",
    },
    {
        "host": "ln1",
        "host_class": "94.x",
        "unit": "llm2-structure-eth-multitrade-v1_2",
        "pack": "structure_v1_ethusdt_multitrade_v1_2",
        "symbol": "ETHUSDT",
    },
    # ln3 185.x
    {
        "host": "ln3",
        "host_class": "185.x",
        "unit": "llm2-structure-eth-k5-double3h-p75-v1",
        "pack": "structure_v1_ethusdt_k5_double3h_p75_v1",
        "symbol": "ETHUSDT",
    },
    {
        "host": "ln3",
        "host_class": "185.x",
        "unit": "llm2-structure-eth-multitrade-p75-v1",
        "pack": "structure_v1_ethusdt_multitrade_p75_v1",
        "symbol": "ETHUSDT",
    },
    {
        "host": "ln3",
        "host_class": "185.x",
        "unit": "llm2-structure-eth-15m-multitrade-wall-clock-p75-v1",
        "pack": "structure_v1_ethusdt_15m_multitrade_wall_clock_p75_v1",
        "symbol": "ETHUSDT",
        "timeframe": "15m",
    },
]

# Hard fail on these (exit 1). Soft diagnostic items stay in blockers but do not fail.
HARD_BLOCKERS = {
    "SIDE_MISMATCH",
    "PRED_MEAN_MISMATCH",
    "RECOMPUTE_FAILED",
    "LIVE_DECISION_MISSING",
    "local_pack_missing",
    "TARGET_BAR_MISSING",
}


def latest_closed_1h_ms(now_ms: int | None = None) -> int:
    now = int(now_ms if now_ms is not None else time.time() * 1000)
    forming = (now // TF_MS_1H) * TF_MS_1H
    return int(forming - TF_MS_1H)


def symbol_from_pack(pack_dir: Path, default: str) -> str:
    strat = pack_dir / "strategy.json"
    if strat.is_file():
        try:
            s = json.loads(strat.read_text(encoding="utf-8"))
            if s.get("symbol"):
                return str(s["symbol"]).upper()
        except Exception:
            pass
    return default.upper()


def audit_one(
    cfg: dict,
    *,
    bar_ts_ms: int | None,
    require_target_bar: bool,
    strict_indicators: bool,
    pred_eps: float,
) -> dict:
    host = cfg["host"]
    unit = cfg["unit"]
    pack_dir = PACKS / cfg["pack"]
    symbol = symbol_from_pack(pack_dir, cfg["symbol"])
    timeframe = str(cfg.get("timeframe") or "1h")
    if pack_dir.is_dir() and (pack_dir / "strategy.json").is_file():
        try:
            timeframe = str(
                json.loads((pack_dir / "strategy.json").read_text(encoding="utf-8")).get(
                    "timeframe"
                )
                or timeframe
            )
        except Exception:
            pass
    row_out: dict = {
        "host": host,
        "host_class": cfg.get("host_class")
        or ("94.x" if host == "ln1" else "185.x" if host == "ln3" else host),
        "unit": unit,
        "pack": cfg["pack"],
        "symbol": symbol,
        "timeframe": timeframe,
        "local_pack_ok": pack_dir.is_dir() and (pack_dir / "model.joblib").is_file(),
    }
    if not row_out["local_pack_ok"]:
        row_out["error"] = "local_pack_missing"
        row_out["blockers"] = ["local_pack_missing"]
        row_out["ok"] = False
        return row_out

    try:
        live = pull_live_decision(host, unit, bar_ts_ms=bar_ts_ms)
    except Exception as e:
        row_out["error"] = f"live_pull_failed:{e}"
        row_out["blockers"] = ["LIVE_PULL_FAILED"]
        row_out["ok"] = False
        return row_out

    if not live.get("row"):
        if require_target_bar:
            row_out["error"] = "TARGET_BAR_MISSING"
            row_out["blockers"] = ["TARGET_BAR_MISSING"]
            row_out["ok"] = False
            return row_out
        try:
            live = pull_live_decision(host, unit, bar_ts_ms=None)
        except Exception as e:
            row_out["error"] = f"live_pull_latest_failed:{e}"
            row_out["blockers"] = ["LIVE_PULL_FAILED"]
            row_out["ok"] = False
            return row_out
        row_out["note"] = "no_row_for_target_bar_used_latest"

    if not live.get("row"):
        row_out["error"] = "LIVE_DECISION_MISSING"
        row_out["blockers"] = ["LIVE_DECISION_MISSING"]
        row_out["ok"] = False
        return row_out

    dec = live["row"]
    bar_ts = int(dec["bar_ts_ms"])
    live_pred = float(dec["pred_mean"])
    live_side = int(dec["side"]) if dec["side"] is not None else None
    bar_utc = datetime.fromtimestamp(bar_ts / 1000, tz=timezone.utc).isoformat()

    recompute = recompute_pred_mean(
        pack_dir=pack_dir,
        symbol=symbol,
        timeframe=timeframe,
        bar_ts_ms=bar_ts,
    )

    pack_row = live.get("pack_decision_row") or live.get("pack_tip_row")
    ind_cmp = None
    if pack_row:
        ind_cmp = compare_pack_tip_to_research(
            pack_row, symbol=symbol, ts_ms=bar_ts, timeframe=timeframe
        )

    blockers: list[str] = []
    soft: list[str] = []

    if recompute.get("error"):
        blockers.append(str(recompute["error"]))
    if recompute.get("pred_mean") is None:
        blockers.append("RECOMPUTE_FAILED")
        abs_diff = None
        side_match = None
        pred_match = None
    else:
        abs_diff = abs(float(recompute["pred_mean"]) - live_pred)
        side_match = int(recompute["side"]) == live_side
        pred_match = abs_diff < pred_eps
        if not side_match:
            blockers.append("SIDE_MISMATCH")
        if not pred_match:
            blockers.append("PRED_MEAN_MISMATCH")

    if ind_cmp is not None and ind_cmp.get("identical") is False:
        if strict_indicators:
            blockers.append("INDICATOR_PACK_NE_RESEARCH")
        else:
            soft.append("INDICATOR_PACK_NE_RESEARCH")

    hard = [b for b in blockers if b in HARD_BLOCKERS or b not in soft]
    # Only hard failures define ok=False for signal identity
    signal_ok = (
        recompute.get("pred_mean") is not None
        and not recompute.get("error")
        and abs_diff is not None
        and abs_diff < pred_eps
        and side_match is True
    )
    if require_target_bar and bar_ts_ms is not None and bar_ts != int(bar_ts_ms):
        blockers.append("TARGET_BAR_MISSING")
        signal_ok = False

    row_out.update(
        {
            "bar_ts_ms": bar_ts,
            "bar_utc": bar_utc,
            "live_pred_mean": live_pred,
            "live_side": live_side,
            "live_decided_utc": dec.get("decided_utc"),
            "warehouse_pred_mean": recompute.get("pred_mean"),
            "warehouse_side": recompute.get("side"),
            "recompute_error": recompute.get("error"),
            "abs_diff": abs_diff,
            "side_match": side_match,
            "pred_match": pred_match,
            "pack_1h_max_ts": (live.get("pack_1h") or {}).get("max_ts"),
            "indicators_identical": None if ind_cmp is None else ind_cmp.get("identical"),
            "indicators_n_mismatch": None if ind_cmp is None else ind_cmp.get("n_mismatch"),
            "blockers": blockers,
            "soft_blockers": soft,
            "ok": bool(signal_ok) and not (
                strict_indicators and "INDICATOR_PACK_NE_RESEARCH" in blockers
            ),
        }
    )
    return row_out


def select_fleet(*, hosts: list[str] | None, units: list[str] | None) -> list[dict]:
    rows = list(FLEET_REGISTRY)
    if hosts:
        want = {h.lower() for h in hosts}
        rows = [r for r in rows if r["host"].lower() in want]
    if units:
        want_u = {u.replace(".service", "").lower() for u in units}
        rows = [r for r in rows if r["unit"].lower() in want_u]
    return rows


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description=f"{GATE_NAME} ({EVIDENCE_CLASS}): live pred_mean vs local BT for the fleet."
    )
    ap.add_argument(
        "--host",
        action="append",
        dest="hosts",
        metavar="HOST",
        help="Restrict to host alias (repeatable). Default: all registry hosts (ln1, ln3).",
    )
    ap.add_argument(
        "--unit",
        action="append",
        dest="units",
        metavar="UNIT",
        help="Restrict to unit name (repeatable).",
    )
    ap.add_argument(
        "--bar-ts-ms",
        type=int,
        default=None,
        help="Decision bar open ms. Default: latest fully closed 1h bar.",
    )
    ap.add_argument(
        "--require-target-bar",
        action="store_true",
        help="FAIL if a unit has no decision for the target bar (no latest-fallback).",
    )
    ap.add_argument(
        "--strict-indicators",
        action="store_true",
        help="Treat pack tip vs research bar_features mismatch as a hard fail.",
    )
    ap.add_argument(
        "--pred-eps",
        type=float,
        default=PRED_ABS_EPS,
        help=f"Abs |live-bt| threshold for pred_mean match (default {PRED_ABS_EPS}).",
    )
    ap.add_argument(
        "--list-fleet",
        action="store_true",
        help="Print fleet registry and exit.",
    )
    args = ap.parse_args(argv)

    if args.list_fleet:
        print(json.dumps({"gate": GATE_NAME, "fleet": FLEET_REGISTRY}, indent=2))
        return 0

    fleet = select_fleet(hosts=args.hosts, units=args.units)
    if not fleet:
        print("ERROR: empty fleet selection", file=sys.stderr)
        return 2

    closed = int(args.bar_ts_ms) if args.bar_ts_ms is not None else latest_closed_1h_ms()
    closed_utc = datetime.fromtimestamp(closed / 1000, tz=timezone.utc).isoformat()

    out: dict = {
        "gate_name": GATE_NAME,
        "evidence_class": EVIDENCE_CLASS,
        "maximum_earned_readiness": "LIVE_STOP / RESEARCH_ONLY",
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "target_closed_1h_bar_utc": closed_utc,
        "target_closed_1h_bar_ts_ms": closed,
        "require_target_bar": bool(args.require_target_bar),
        "strict_indicators": bool(args.strict_indicators),
        "pred_eps": float(args.pred_eps),
        "note": (
            "Compares each unit's decision on the target closed 1h bar (or latest "
            "if missing and not --require-target-bar) to local warehouse recompute "
            "with the matching frozen pack. Does not claim readiness. "
            "Single-unit deep tip audit: ops_live_research_parity_gate.py. "
            "1m indicator-only: run_1m_indicator_parity_bot.py."
        ),
        "results": [],
    }

    for cfg in fleet:
        print(f"… {cfg['host']} {cfg['unit']}", flush=True)
        try:
            res = audit_one(
                cfg,
                bar_ts_ms=closed,
                require_target_bar=bool(args.require_target_bar),
                strict_indicators=bool(args.strict_indicators),
                pred_eps=float(args.pred_eps),
            )
        except Exception as e:
            res = {
                "host": cfg["host"],
                "unit": cfg["unit"],
                "pack": cfg["pack"],
                "error": str(e),
                "blockers": ["EXCEPTION"],
                "ok": False,
            }
        out["results"].append(res)
        status = "PASS" if res.get("ok") else "FAIL"
        print(
            f"{status} {cfg['host']} ({cfg.get('host_class','')}) {cfg['unit']} "
            f"bar={res.get('bar_utc')} "
            f"live={res.get('live_pred_mean')} "
            f"bt={res.get('warehouse_pred_mean')} "
            f"side_live={res.get('live_side')} "
            f"side_bt={res.get('warehouse_side')} "
            f"blockers={res.get('blockers') or res.get('error')} "
            f"soft={res.get('soft_blockers')}",
            flush=True,
        )

    n = len(out["results"])
    n_ok = sum(1 for r in out["results"] if r.get("ok"))
    soft_only = [
        r["unit"]
        for r in out["results"]
        if r.get("ok") and r.get("soft_blockers")
    ]
    out["summary"] = {
        "gate_name": GATE_NAME,
        "n_units": n,
        "n_pass": n_ok,
        "n_fail": n - n_ok,
        "all_pred_match": n_ok == n and n > 0,
        "units_with_soft_indicator_mismatch": soft_only,
    }
    fails = [r for r in out["results"] if not r.get("ok")]
    out["principal_blocker"] = None
    if fails:
        out["principal_blocker"] = fails[0].get("blockers") or fails[0].get("error")

    # Live↔backtest prediction mismatch is a hard stop (same class as a failed gate).
    n_pred_mismatch = sum(
        1
        for r in out["results"]
        if "PRED_MEAN_MISMATCH" in (r.get("blockers") or [])
        or "SIDE_MISMATCH" in (r.get("blockers") or [])
    )
    out["summary"]["n_bars_pred_differ"] = int(n_pred_mismatch)
    out["summary"]["pred_mismatch_hard_stop"] = n_pred_mismatch > 0

    REPORTS.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    path = REPORTS / f"{REPORT_STEM}_{stamp}.json"
    latest = REPORTS / f"{REPORT_STEM}_latest.json"
    # Keep legacy path for older pointers.
    legacy = REPORTS / "fleet_live_vs_local_pred_latest.json"
    blob = json.dumps(out, indent=2, default=str)
    path.write_text(blob, encoding="utf-8")
    latest.write_text(blob, encoding="utf-8")
    legacy.write_text(blob, encoding="utf-8")
    print(json.dumps(out["summary"], indent=2), flush=True)
    print(f"WROTE {latest}", flush=True)
    if n_pred_mismatch > 0:
        from llm2.evidence.four_proof import refuse_pred_mismatch_hard_stop

        try:
            refuse_pred_mismatch_hard_stop(
                n_bars_pred_differ=n_pred_mismatch,
                context=EVIDENCE_CLASS,
            )
        except Exception as exc:  # noqa: BLE001 — PolicyError
            print(f"HARD_STOP {exc}", flush=True)
            return 2
    return 0 if out["summary"]["all_pred_match"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
