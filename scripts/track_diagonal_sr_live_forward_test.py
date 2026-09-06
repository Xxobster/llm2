"""Track the live diagonal S/R forward test against its preregistered predictions.

Read-only. Pulls closed trades and decision records off the VPS units, computes the
statistics the preregister named, and reports which of the two hypotheses the
evidence currently favours plus any early-stop rule that has fired.

Never places, amends or cancels an order. Never restarts a unit.

Usage:

    python -u scripts/track_diagonal_sr_live_forward_test.py
    python -u scripts/track_diagonal_sr_live_forward_test.py --json
"""

from __future__ import annotations

import argparse
import json
import math
import subprocess
import sys
from pathlib import Path
from typing import Any

import yaml

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

PREREG = _ROOT / "configs" / "preregister" / "diagonal_sr_live_forward_test_001.yaml"
OUT = _ROOT / "artifacts" / "reports" / "diagonal_sr"
HOST = "root@94.156.189.76"
REMOTE_COLLECTOR = "/tmp/_fwd_collect.py"

# Runs on the VPS: reads each unit's state database plus the exchange closed-PnL
# feed, and prints one JSON blob. Kept self-contained so it can be scp'd as-is.
COLLECTOR = r'''
import json, os, sqlite3, sys

UNITS = {
    "llm2-dsr-eth-bu-1h": ("ETHUSDT", "/opt/llm2-dsr-eth-bu-1h"),
    "llm2-dsr-sol-bu-1h": ("SOLUSDT", "/opt/llm2-dsr-sol-bu-1h"),
}
out = {"units": {}}

for unit, (symbol, root) in UNITS.items():
    rec = {"symbol": symbol, "decisions": 0, "entered": 0, "stale": 0, "unstable": 0,
           "reconciles": 0, "fills": [], "errors": 0}
    state = os.path.join(root, "state", "dsr_live_state.sqlite")
    if os.path.exists(state):
        try:
            con = sqlite3.connect("file:%s?mode=ro" % state, uri=True)
            rec["decisions"] = con.execute("SELECT COUNT(*) FROM pivot_decisions").fetchone()[0]
            for (p,) in con.execute("SELECT payload_json FROM pivot_decisions"):
                try:
                    d = json.loads(p)
                except Exception:
                    continue
                if d.get("action") == "ENTER_LIMIT":
                    rec["entered"] += 1
                code = ((d.get("live_data_001") or {}).get("tip") or {}).get("code")
                if code and code != "PASS":
                    rec["stale"] += 1
            try:
                for ev, cu, pj in con.execute(
                    "SELECT event, created_utc, payload_json FROM pivot_fills"
                ):
                    rec["fills"].append({"event": ev, "utc": cu, "payload": pj[:800]})
            except Exception:
                pass
            con.close()
        except Exception as exc:
            rec["state_error"] = str(exc)[:200]
    log = os.path.join(root, "logs", "dsr_live.log")
    if os.path.exists(log):
        try:
            with open(log, "r", errors="replace") as fh:
                for line in fh:
                    if "TIP_UNSTABLE" in line:
                        rec["unstable"] += 1
                    if "RECONCILE_ADOPTED" in line or "RECONCILE_TPSL_ATTACHED" in line:
                        rec["reconciles"] += 1
                    if "Traceback" in line or "PLACE_FAIL" in line:
                        rec["errors"] += 1
        except Exception:
            pass
    out["units"][unit] = rec

# Exchange truth for realised trades.
sys.path.insert(0, "/opt/llm2-dsr-eth-bu-1h")
os.environ.setdefault("TRADING_SECRETS_ENV", "/root/.trading/secrets.env")
try:
    from llm2.live.micro_runner import _bybit_signed_request, _load_account_keys
    k, s = _load_account_keys("Xxobster4")
    closed = []
    # Bybit V5 GET takes its parameters as a signed query string, not a JSON body.
    for sym in ("ETHUSDT", "SOLUSDT"):
        r = _bybit_signed_request(
            api_key=k, api_secret=s, method="GET", path="/v5/position/closed-pnl",
            query={"category": "linear", "symbol": sym, "limit": "100"},
        )
        out.setdefault("closed_ret", {})[sym] = r.get("retMsg")
        for row in ((r.get("result") or {}).get("list") or []):
            closed.append({
                "symbol": row.get("symbol"), "side": row.get("side"),
                "qty": row.get("qty"), "avgEntryPrice": row.get("avgEntryPrice"),
                "avgExitPrice": row.get("avgExitPrice"),
                "closedPnl": row.get("closedPnl"), "orderType": row.get("orderType"),
                "createdTime": row.get("createdTime"), "updatedTime": row.get("updatedTime"),
            })
    out["closed"] = closed
    w = _bybit_signed_request(
        api_key=k, api_secret=s, method="GET", path="/v5/account/wallet-balance",
        query={"accountType": "UNIFIED"},
    )
    out["wallet_ret"] = w.get("retMsg")
    lst = (w.get("result") or {}).get("list") or [{}]
    out["equity"] = lst[0].get("totalEquity")
    out["wallet"] = lst[0].get("totalWalletBalance")
except Exception as exc:
    out["exchange_error"] = str(exc)[:300]

print(json.dumps(out))
'''

ENV = (
    "PYTHONPATH=/opt/llm2-dsr-eth-bu-1h:/opt/llm2-structure:"
    "/opt/botsgeneral/packages/live_candles/src:/opt/botsgeneral/packages/indicators/src:"
    "/opt/botsgeneral/packages/tradesim/src:/opt/botsgeneral/packages/leakage/src "
    "SHARED_CANDLES_DB=/var/lib/botsgeneral/shared_candles.db "
    "TRADING_SECRETS_ENV=/root/.trading/secrets.env TRADESIM_NO_PLOT=1"
)


def collect() -> dict[str, Any]:
    tmp = _ROOT / "artifacts" / "_tmp_fwd_collect.py"
    tmp.write_text(COLLECTOR, encoding="utf-8")
    subprocess.run(
        ["scp", "-o", "ConnectTimeout=15", str(tmp), f"{HOST}:{REMOTE_COLLECTOR}"],
        check=True, capture_output=True,
    )
    res = subprocess.run(
        ["ssh", "-o", "ConnectTimeout=20", HOST,
         f"cd /opt/llm2-dsr-eth-bu-1h && {ENV} ./venv/bin/python {REMOTE_COLLECTOR}"],
        check=True, capture_output=True, text=True,
    )
    line = next(
        (ln for ln in reversed(res.stdout.splitlines()) if ln.strip().startswith("{")), ""
    )
    if not line:
        raise RuntimeError(f"no JSON from collector: {res.stdout[-500:]} {res.stderr[-500:]}")
    return json.loads(line)


def stats(trades: list[dict]) -> dict[str, Any]:
    pnl = [float(t["closedPnl"]) for t in trades if t.get("closedPnl") not in (None, "")]
    if not pnl:
        return {"n": 0}
    wins = [p for p in pnl if p > 0]
    losses = [p for p in pnl if p < 0]
    gross_win = sum(wins)
    gross_loss = abs(sum(losses))
    pf = (gross_win / gross_loss) if gross_loss > 0 else float("inf")
    return {
        "n": len(pnl),
        "net_pnl": sum(pnl),
        "profit_factor": pf,
        "win_rate": len(wins) / len(pnl),
        "payoff_ratio": (
            (gross_win / len(wins)) / (gross_loss / len(losses))
            if wins and losses else float("nan")
        ),
        "avg_pnl": sum(pnl) / len(pnl),
        "gross_win": gross_win,
        "gross_loss": gross_loss,
    }


def hold_hours(t: dict) -> float:
    """Hold duration, or NaN when the exchange record cannot supply it.

    Bybit's closed-PnL ``createdTime`` is when the *record* was written, which for
    a closed position equals the exit. It is not the entry time, so this is only a
    usable proxy when the venue happens to carry the position's open time. The
    authoritative entry is ``entry_bar_ms`` in the unit's own ``pivot_fills``, so
    anything NaN here must be filled from there rather than guessed.
    """
    try:
        h = (int(t["updatedTime"]) - int(t["createdTime"])) / 3_600_000.0
    except Exception:
        return float("nan")
    return h if h > 0 else float("nan")


def excluded_trades(unit_rec: dict) -> list[str]:
    """Exits caused by operator intervention, not by the strategy.

    The Ethereum entry of 2026-08-26 filled during an SSL handshake timeout and was
    left unprotected; it was flattened manually under explicit authorisation. Its
    exit price reflects when a human acted, so counting it as a strategy outcome
    would contaminate the forward test in either direction.
    """
    out = []
    for f in unit_rec.get("fills") or []:
        if str(f.get("event")) in {"orphan_flattened_authorized", "reconciled_orphan_entry"}:
            out.append(str(f.get("event")))
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    cfg = yaml.safe_load(PREREG.read_text(encoding="utf-8"))
    h0 = cfg["hypotheses"]["H0_frozen_evidence_holds"]
    par = cfg["parity_checks"]
    need = int(cfg["sample"]["min_resolved_trades_per_arm_for_verdict"])

    data = collect()
    closed = data.get("closed") or []
    report: dict[str, Any] = {"equity": data.get("equity"), "wallet": data.get("wallet"),
                              "arms": {}, "alerts": []}

    for unit in cfg["units"]:
        sym = unit["symbol"]
        name = unit["unit"]
        u = (data.get("units") or {}).get(name, {})
        all_tr = [t for t in closed if t.get("symbol") == sym]
        # Operator-closed trades are not strategy outcomes.
        n_excluded = len(excluded_trades(u))
        tr = all_tr[: len(all_tr) - n_excluded] if n_excluded else all_tr
        s = stats(tr)
        holds = [h for h in (hold_hours(t) for t in tr) if not math.isnan(h)]
        # A close inside the entry hour is the live analogue of an entry-bar exit.
        # Only meaningful once holds are actually available.
        ebr_live = (
            sum(1 for h in holds if h <= 1.0) / len(holds) if holds else float("nan")
        )
        frozen = h0.get(sym, {})
        arm = {
            "unit": name,
            "decisions": u.get("decisions", 0),
            "entries_signalled": u.get("entered", 0),
            "tip_gate_blocks": u.get("stale", 0),
            "tip_unstable_events": u.get("unstable", 0),
            "reconciles": u.get("reconciles", 0),
            "errors": u.get("errors", 0),
            "resolved_trades": s.get("n", 0),
            "excluded_operator_closed": n_excluded,
            "holds_available": len(holds),
            "trades_needed_for_verdict": need,
            "live": s,
            "live_entry_bar_rate_proxy": ebr_live,
            "live_avg_hold_hours": (sum(holds) / len(holds)) if holds else float("nan"),
            "frozen": frozen,
        }

        n = s.get("n", 0)
        if n and n >= 20 and s["profit_factor"] < 0.80:
            report["alerts"].append(
                f"FWD-002 {sym}: profit factor {s['profit_factor']:.2f} < 0.80 after {n} trades"
            )
        if (not math.isnan(ebr_live) and frozen.get("entry_bar_exit_rate") is not None
                and n >= 10 and len(holds) >= 10):
            dev = abs(ebr_live - float(frozen["entry_bar_exit_rate"]))
            if dev > float(par["entry_bar_exit_rate_tolerance"]):
                report["alerts"].append(
                    f"FWD-003 {sym}: live entry-bar proxy {ebr_live:.2f} vs frozen "
                    f"{frozen['entry_bar_exit_rate']:.2f}, deviation {dev:.2f} exceeds "
                    f"{par['entry_bar_exit_rate_tolerance']}"
                )
        if u.get("reconciles", 0) > 2:
            report["alerts"].append(
                f"FWD-004 {sym}: reconciliation fired {u['reconciles']} times"
            )
        if n:
            if n >= need:
                arm["verdict"] = (
                    "supports_H0" if s["profit_factor"] >= 1.20
                    else "refutes_H0" if s["profit_factor"] < 1.10
                    else "inconclusive"
                )
            else:
                arm["verdict"] = f"pending ({n}/{need} trades)"
        else:
            arm["verdict"] = "no resolved trades yet"
        report["arms"][sym] = arm

    try:
        wallet = float(report["wallet"])
        if wallet < 19.8388 * 0.95:
            report["alerts"].append(
                f"FWD-001: wallet {wallet:.4f} is more than 5% below the 19.8388 start"
            )
    except (TypeError, ValueError):
        pass

    if args.json:
        print(json.dumps(report, indent=2, default=str))
    else:
        print("=" * 78)
        print("Diagonal S/R live forward test — preregistered tracker")
        print("=" * 78)
        print(f"account Xxobster4  equity={report['equity']}  wallet={report['wallet']}")
        for sym, a in report["arms"].items():
            f = a["frozen"]
            lv = a["live"]
            print(f"\n{sym}  [{a['unit']}]   verdict: {a['verdict']}")
            print(f"  decisions={a['decisions']} entries_signalled={a['entries_signalled']} "
                  f"tip_blocks={a['tip_gate_blocks']} unstable={a['tip_unstable_events']} "
                  f"reconciles={a['reconciles']} errors={a['errors']}")
            if a["excluded_operator_closed"]:
                print(f"  excluded {a['excluded_operator_closed']} operator-closed trade(s) "
                      "(not a strategy outcome)")
            if lv.get("n"):
                print(f"  resolved strategy trades {lv['n']}/{a['trades_needed_for_verdict']}")
                print(f"    {'':22s} {'live':>10s} {'frozen':>10s}")
                print(f"    {'profit factor':22s} {lv['profit_factor']:>10.3f} "
                      f"{f.get('profit_factor', float('nan')):>10.3f}")
                print(f"    {'win rate':22s} {lv['win_rate']:>10.3f} "
                      f"{f.get('win_rate', float('nan')):>10.3f}")
                if a["holds_available"]:
                    print(f"    {'entry-bar rate':22s} {a['live_entry_bar_rate_proxy']:>10.3f} "
                          f"{f.get('entry_bar_exit_rate', float('nan')):>10.3f}")
                    print(f"    {'avg hold (hours)':22s} {a['live_avg_hold_hours']:>10.2f} "
                          f"{f.get('avg_hold_bars', float('nan')):>10.2f}")
                else:
                    print("    entry-bar rate / hold: not yet available "
                          "(venue record carries no entry time)")
                print(f"    net PnL {lv['net_pnl']:+.4f} USDT  "
                      f"(gross win {lv['gross_win']:.4f} / gross loss {lv['gross_loss']:.4f})")
            else:
                print("  no resolved strategy trades yet")
        if report["alerts"]:
            print("\n" + "!" * 78)
            for a in report["alerts"]:
                print(f"ALERT {a}")
            print("!" * 78)
            print("Early-stop rule fired. Halting a live unit requires user authorisation.")
        else:
            print("\nNo early-stop rule fired.")

    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "live_forward_test_latest.json").write_text(
        json.dumps(report, indent=2, default=str), encoding="utf-8"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
