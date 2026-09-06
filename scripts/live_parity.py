#!/usr/bin/env python3
"""One-command live vs backtest parity for this repo's pivot units.

Scope: LLM2 pivot bots only
  live-network-1 (ln1 / 94.x): Xxobster7 ETH+SOL 15m 1%/1%
  live-network-2 (ln2 / 212.x): Xxobster8 1%/1% and Xxobster9 0.5%/0.5%

Does not deploy, restart, or change size/leverage. Live window is after
Forward Lockbox Start (2026-05-01), so this run stamps a contaminated peek.

  python scripts/live_parity.py --i-accept-lockbox-contamination
  python scripts/live_parity.py --i-accept-lockbox-contamination --skip-fetch
  python scripts/live_parity.py --i-accept-lockbox-contamination --host ln2 --plot
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from llm2.evidence.lockbox_guard import add_lockbox_guard_args, require_lockbox_access
from llm2.paths import ARTIFACTS

REPORTS = ARTIFACTS / "reports"
OUT = REPORTS / "live_parity_latest.json"
LN1_DUMP = REPORTS / "_xx7_pivot_live_full.json"
LN1_15M = REPORTS / "_vps_15m_eth_sol.json"
LN2_DUMP = REPORTS / "_ln2_xx89_pivot_live.json"
LN2_15M = REPORTS / "_ln2_15m_eth_sol.json"
LN1_AUDIT = REPORTS / "audit_llm2_pivot_live_vs_bt_latest.json"
LN2_AUDIT = REPORTS / "audit_llm2_pivot_ln2_xx89_live_vs_bt_latest.json"


def run(cmd: list[str], *, check: bool = True) -> subprocess.CompletedProcess:
    print("+", " ".join(cmd), flush=True)
    return subprocess.run(cmd, cwd=str(ROOT), check=check)


def _ssh_dump(host: str, script: Path, remote_files: list[tuple[str, Path]]) -> None:
    remote_py = f"/tmp/{script.name}"
    run(["scp", str(script), f"{host}:{remote_py}"])
    run(["ssh", host, f"sed -i 's/\\r$//' {remote_py} && python3 {remote_py}"])
    for remote, local in remote_files:
        local.parent.mkdir(parents=True, exist_ok=True)
        run(["scp", f"{host}:{remote}", str(local)])


def pull_ln1() -> None:
    _ssh_dump(
        "ln1",
        ROOT / "scripts" / "dump_pivot_live_ln1.py",
        [
            ("/tmp/xx7_pivot_live_full.json", LN1_DUMP),
            ("/tmp/vps_15m_eth_sol.json", LN1_15M),
        ],
    )


def pull_ln2() -> None:
    _ssh_dump(
        "ln2",
        ROOT / "scripts" / "dump_pivot_live_ln2.py",
        [
            ("/tmp/ln2_xx89_pivot_live.json", LN2_DUMP),
            ("/tmp/ln2_15m_eth_sol.json", LN2_15M),
        ],
    )


def ingest_vps_15m_dumps() -> None:
    """When Binance REST is blocked, upsert Virtual Private Server 15-minute Last into the warehouse."""
    from tradesim.ensure_source import prefer_botsgeneral_tradesim

    prefer_botsgeneral_tradesim()
    from market_data.db import ResearchCandleDB
    from llm2.paths import MARKET_DB
    import pandas as pd

    db = ResearchCandleDB(MARKET_DB)
    n_total = 0
    for path in (LN1_15M, LN2_15M):
        if not path.is_file():
            continue
        blob = json.loads(path.read_text(encoding="utf-8"))
        for key, sym in (("ETHUSDT_15m", "ETHUSDT"), ("SOLUSDT_15m", "SOLUSDT")):
            rows = blob.get(key) or []
            if not rows:
                continue
            df = pd.DataFrame(rows)
            n = db.upsert_df(
                df,
                source="binance",
                symbol=sym,
                timeframe="15m",
                price_type="last",
                product="USDⓈ-M",
                source_endpoint="vps_shared_candles_fallback",
            )
            n_total += int(n)
            print(f"ingest {path.name} {sym} upserted={n}", flush=True)
    db.close()
    print(f"ingest_vps_15m_dumps total_upserted={n_total}", flush=True)


def refresh_candles() -> None:
    # Bounded live-window Last+Mark (from 2026-08-01). Do not call full-history
    # ensure_candles here: 1-minute ETH+SOL last+mark can run silently for tens of minutes.
    proc = run(
        [sys.executable, "-u", str(ROOT / "scripts" / "_fetch_pivot_last_mark.py")],
        check=False,
    )
    if proc.returncode == 0:
        return
    print("Binance REST failed — falling back to VPS 15-minute Last dumps", flush=True)
    ingest_vps_15m_dumps()


def run_audit(script: str) -> None:
    run(
        [
            sys.executable,
            "-u",
            str(ROOT / "scripts" / script),
            "--i-accept-lockbox-contamination",
        ]
    )


def _as_pct(rate) -> float | None:
    if rate is None:
        return None
    v = float(rate)
    return v * 100.0 if v <= 1.0000001 else v


def _fmt_pct(value: float | None) -> str:
    if value is None:
        return "n/a"
    if abs(value - round(value)) < 0.05:
        return f"{int(round(value))}%"
    return f"{value:.1f}%"


def arm_closeness(arm: dict) -> dict:
    """Four-aspect closeness for one pivot unit (bot).

    Candles: Open-High-Low-Close match_rate.
    Calculations: p_any match (the score used to decide), not bitwise feature equality.
    Signals: action_match_rate.
    Entries/exits: paired fills same-side + slip-ok; fill prices from entry_slip_frac.
    """
    candles = arm.get("candles") or {}
    replay = arm.get("replay") or {}
    fills = arm.get("fills") or {}
    pairs = fills.get("pairs") or []
    logic: list[float] = []
    fill_parts: list[float] = []
    for pair in pairs:
        logic.append(1.0 if pair.get("same_side") else 0.0)
        if pair.get("entry_slip_ok") is not None:
            logic.append(1.0 if pair.get("entry_slip_ok") else 0.0)
        slip = pair.get("entry_slip_frac")
        if slip is not None:
            fill_parts.append(max(0.0, 1.0 - abs(float(slip))))
    entries = (100.0 * sum(logic) / len(logic)) if logic else None
    fill_pct = (100.0 * sum(fill_parts) / len(fill_parts)) if fill_parts else None
    candles_pct = _as_pct(candles.get("match_rate"))
    calc_pct = _as_pct(replay.get("p_any_match_rate"))
    sig_pct = _as_pct(replay.get("action_match_rate"))
    present = [x for x in (candles_pct, calc_pct, sig_pct, entries) if x is not None]
    return {
        "candles_pct": candles_pct,
        "calculations_pct": calc_pct,
        "signals_pct": sig_pct,
        "entries_exits_pct": entries,
        "fill_price_pct": fill_pct,
        "overall_pct": (sum(present) / len(present)) if present else None,
    }


def _mean_closeness(rows: list[dict]) -> dict:
    keys = (
        "candles_pct",
        "calculations_pct",
        "signals_pct",
        "entries_exits_pct",
        "fill_price_pct",
        "overall_pct",
    )
    out: dict = {}
    for key in keys:
        vals = [float(r[key]) for r in rows if r.get(key) is not None]
        out[key] = (sum(vals) / len(vals)) if vals else None
    return out


def _format_glimpse(rows: list[dict], *, title: str) -> str:
    headers = ("bot", "candles", "calculations", "signals", "entries/exits", "fill prices")
    body = []
    for row in rows:
        body.append(
            (
                str(row.get("label") or ""),
                _fmt_pct(row.get("candles_pct")),
                _fmt_pct(row.get("calculations_pct")),
                _fmt_pct(row.get("signals_pct")),
                _fmt_pct(row.get("entries_exits_pct")),
                _fmt_pct(row.get("fill_price_pct")),
            )
        )
    widths = [len(h) for h in headers]
    for line in body:
        for i, cell in enumerate(line):
            widths[i] = max(widths[i], len(cell))
    widths[0] = max(widths[0], 12)

    def _fmt(line: tuple[str, ...]) -> str:
        return "  ".join(cell.ljust(widths[i]) for i, cell in enumerate(line))

    out = [title, _fmt(headers), _fmt(tuple("-" * w for w in widths))]
    out.extend(_fmt(line) for line in body)
    return "\n".join(out)


def _arm_rows(audit: dict, *, default_account: str | None = None) -> list[dict]:
    rows = []
    for a in audit.get("arms") or []:
        replay = a.get("replay") or {}
        candles = a.get("candles") or {}
        counts = a.get("live_counts") or {}
        fills = a.get("fills") or {}
        c = arm_closeness(a)
        rows.append(
            {
                "name": a.get("name") or a.get("unit"),
                "account": a.get("account") or default_account,
                "unit": a.get("unit"),
                "symbol": a.get("symbol"),
                "candle_match_rate": candles.get("match_rate"),
                "action_match": f"{replay.get('action_match')}/{replay.get('n_replayed')}",
                "p_any_match": f"{replay.get('p_any_match')}/{replay.get('n_replayed')}",
                "enter": counts.get("ENTER_LIMIT"),
                "filled": counts.get("filled"),
                "live_fills": fills.get("n_live_fills"),
                "replay_pass": replay.get("pass"),
                "candle_pass": candles.get("pass"),
                "closeness": c,
                "missed": a.get("missed") or {},
            }
        )
    return rows


def write_sitrep(hosts: list[str]) -> dict:
    ln1 = json.loads(LN1_AUDIT.read_text(encoding="utf-8")) if LN1_AUDIT.is_file() and "ln1" in hosts else {}
    ln2 = json.loads(LN2_AUDIT.read_text(encoding="utf-8")) if LN2_AUDIT.is_file() and "ln2" in hosts else {}
    blockers = []
    for label, blob in (("ln1", ln1), ("ln2", ln2)):
        if not blob:
            continue
        b = str(blob.get("principal_blocker") or "")
        if b and not b.lower().startswith("none"):
            blockers.append(f"{label}: {b}")
    material = False
    for blob in (ln1, ln2):
        for a in blob.get("arms") or []:
            if a.get("replay") and a["replay"].get("pass") is False:
                material = True
            if a.get("candles") and a["candles"].get("pass") is False:
                material = True
    sitrep = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "maximum_earned_readiness": "LIVE_STOP / RESEARCH_ONLY",
        "evidence_class": "LIVE_BT_PIVOT_RECONCILE_CONTAMINATED",
        "principal_blocker": "; ".join(blockers) if blockers else "none — live signals match backtest on fetched tips",
        "material_logic_bug": material,
        "hosts": hosts,
        "ln1": {
            "blocker": ln1.get("principal_blocker"),
            "arms": _arm_rows(ln1, default_account="Xxobster7"),
            "report": str(LN1_AUDIT) if ln1 else None,
            "markdown": str(LN1_AUDIT.with_suffix(".md")) if ln1 else None,
        },
        "ln2": {
            "blocker": ln2.get("principal_blocker"),
            "arms": _arm_rows(ln2),
            "report": str(LN2_AUDIT) if ln2 else None,
            "markdown": str(LN2_AUDIT.with_suffix(".md")) if ln2 else None,
        },
    }
    OUT.write_text(json.dumps(sitrep, indent=2) + "\n", encoding="utf-8")
    return sitrep


def print_verdict(sitrep: dict) -> int:
    print("\n======== LIVE PARITY SITREP ========", flush=True)
    print("Generated:", sitrep["generated_utc"], flush=True)
    print("Report:", OUT, flush=True)
    print("Maximum earned readiness:", sitrep["maximum_earned_readiness"], flush=True)
    print("Evidence class:", sitrep["evidence_class"], flush=True)
    print("Principal blocker:", sitrep["principal_blocker"], flush=True)
    print("Material logic bug:", sitrep["material_logic_bug"], flush=True)

    by_account: dict[str, list[dict]] = {}
    for host in ("ln1", "ln2"):
        blob = sitrep.get(host) or {}
        for a in blob.get("arms") or []:
            acc = a.get("account") or host
            by_account.setdefault(acc, []).append(a)

    glimpse: list[dict] = []
    for acc, arms in by_account.items():
        scores = [a.get("closeness") or {} for a in arms]
        for a in arms:
            c = a.get("closeness") or {}
            glimpse.append({"label": f"{acc} {a.get('unit')}", **c})
        glimpse.append({"label": f"ACCOUNT {acc} mean", **_mean_closeness(scores)})
    if glimpse:
        print(
            "\n"
            + _format_glimpse(
                glimpse,
                title="CLOSENESS  live vs backtest  (logic %; fill prices allow designed slip)",
            ),
            flush=True,
        )

    print("\nMISSED  backtest ENTER that live did not take", flush=True)
    print(
        "bot                                       missed_signals  replay_FLAT_vs_BT_ENTER  no_live_row  missed_trades  unfilled_ENTER  extra_BT_fills",
        flush=True,
    )
    for host in ("ln1", "ln2"):
        blob = sitrep.get(host) or {}
        for a in blob.get("arms") or []:
            m = a.get("missed") or {}
            label = f"{a.get('account') or ''} {a.get('unit')}".strip()
            print(
                f"  {label:<41} "
                f"{m.get('n_missed_signals', 0):>14} "
                f"{m.get('n_replay_bt_enter_live_not', 0):>23} "
                f"{m.get('n_bt_enter_no_live_row', 0):>12} "
                f"{m.get('n_missed_trades', 0):>14} "
                f"{m.get('n_live_enter_unfilled', 0):>15} "
                f"{m.get('n_extra_bt_trades', 0):>15}",
                flush=True,
            )
            for f in (m.get("replay_bt_enter_live_not") or [])[:6]:
                print(
                    f"    signal {f.get('utc')} live={f.get('live_action')} bt={f.get('bt_action')}",
                    flush=True,
                )
            for t in (m.get("bt_enter_no_live_row") or [])[:6]:
                print(f"    no-row {t}", flush=True)

    for host in ("ln1", "ln2"):
        blob = sitrep.get(host) or {}
        if not blob.get("arms"):
            continue
        print(f"\n-- {host} --", flush=True)
        print(" blocker:", blob.get("blocker"), flush=True)
        for a in blob["arms"]:
            c = a.get("closeness") or {}
            print(
                f"  {a.get('account') or ''} {a.get('unit')} "
                f"candles={_fmt_pct(c.get('candles_pct'))} "
                f"calculations={_fmt_pct(c.get('calculations_pct'))} "
                f"signals={_fmt_pct(c.get('signals_pct'))} "
                f"entries/exits={_fmt_pct(c.get('entries_exits_pct'))} "
                f"ENTER={a.get('enter')} filled={a.get('filled')}",
                flush=True,
            )
        if blob.get("markdown"):
            print(" markdown:", blob["markdown"], flush=True)
    if sitrep.get("material_logic_bug"):
        print("\nACTION: live vs backtest action/candle mismatch — investigate (do not retune TP/SL).", flush=True)
        return 2
    print("\nOK: no material signal/candle bug. Extra backtest fills vs data-unsafe cancels are operational.", flush=True)
    return 0


def maybe_plot() -> None:
    plot = ROOT / "scripts" / "plot_xx8_eth_account_closed_finplot.py"
    if not plot.is_file():
        print("plot script missing — skip", flush=True)
        return
    subprocess.Popen(
        [
            sys.executable,
            "-u",
            str(plot),
            "--i-accept-lockbox-contamination",
            "--i-accept-finplot-lockbox",
            "--show",
        ],
        cwd=str(ROOT),
    )


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    add_lockbox_guard_args(ap)
    ap.add_argument("--host", choices=("ln1", "ln2", "both"), default="both")
    ap.add_argument("--skip-fetch", action="store_true")
    ap.add_argument("--skip-pull", action="store_true")
    ap.add_argument("--skip-candles", action="store_true")
    ap.add_argument("--plot", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args(argv)
    hosts = ["ln1", "ln2"] if args.host == "both" else [args.host]
    require_lockbox_access(
        experiment_id="live_parity",
        window_start="2026-08-12",
        window_end=datetime.now(timezone.utc).date().isoformat(),
        purpose="live_vs_bt_pivot_fleet",
        symbols=["ETHUSDT", "SOLUSDT"],
        accepted_contamination=bool(args.i_accept_lockbox_contamination),
    )
    print("live_parity scope: LLM2 pivot", " ".join(hosts), flush=True)
    steps: list[tuple[str, object]] = []
    if not args.skip_fetch and not args.skip_pull:
        if "ln1" in hosts:
            steps.append(("pull_ln1", pull_ln1))
        if "ln2" in hosts:
            steps.append(("pull_ln2", pull_ln2))
    if not args.skip_fetch and not args.skip_candles:
        steps.append(("refresh_candles_15m_1m", refresh_candles))
    if "ln1" in hosts:
        steps.append(("audit_ln1", lambda: run_audit("audit_llm2_pivot_live_vs_bt.py")))
    if "ln2" in hosts:
        steps.append(("audit_ln2", lambda: run_audit("audit_llm2_pivot_ln2_xx89_live_vs_bt.py")))
    if args.dry_run:
        for name, _ in steps:
            print(" would:", name, flush=True)
        return 0
    for name, fn in steps:
        print(f"--- {name} ---", flush=True)
        fn()
    sitrep = write_sitrep(hosts)
    code = print_verdict(sitrep)
    if args.plot:
        print("--- plot ---", flush=True)
        maybe_plot()
    return code


if __name__ == "__main__":
    raise SystemExit(main())
