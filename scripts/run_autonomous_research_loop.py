"""Autonomous public-indicator research loop.

RESEARCH_ONLY. Continues through a generation queue until
`artifacts/autonomy/STOP` exists. Auto-extends unused public windows
so the queue does not go idle.

Hard rules: no leakage, tradesim from botsgeneral, entry-bar exit <= 35%,
trades/month in [4, 40], pre-lockbox ranking only, no VPS deploy.
Does not scrape TradingView or paste third-party Pine.
"""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import yaml

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from llm2.autonomy.auto_windows import ensure_queue_depth  # noqa: E402
from llm2.autonomy.policy import (  # noqa: E402
    STATUS_REL,
    STOP_REL,
    is_gate_candidate,
    rank_key,
)
from llm2.registry.ledger import append_ledger  # noqa: E402

QUEUE = _ROOT / "configs" / "autonomy" / "research_loop_v1.yaml"
PREREG_DIR = _ROOT / "configs" / "preregister"
STATE = _ROOT / "artifacts" / "autonomy" / "loop_state.json"
STOP = _ROOT / STOP_REL
STATUS = _ROOT / STATUS_REL
ALERT = _ROOT / "artifacts" / "autonomy" / "ALERT.md"


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _load_queue() -> dict:
    return yaml.safe_load(QUEUE.read_text(encoding="utf-8")) or {}


def _discover_generations(cfg: dict) -> list[dict]:
    """Merge YAML queue with any frozen autonomy_gen_* preregisters on disk."""
    gens = list(cfg.get("generations") or [])
    by_id: dict[str, dict] = {str(g["id"]): g for g in gens}
    for path in sorted(PREREG_DIR.glob("autonomy_gen_*_public_indicators.yaml")):
        parts = path.stem.split("_")
        if len(parts) < 3:
            continue
        gid = parts[2]
        if gid in by_id:
            continue
        by_id[gid] = {
            "id": gid,
            "title": path.stem,
            "preregister": str(path.relative_to(_ROOT)).replace("\\", "/"),
            "script": "scripts/run_autonomy_public_indicator_hunt.py",
            "args": ["--gen", gid],
            "report_json": f"artifacts/reports/autonomy/gen_{gid}_latest.json",
        }
    return [by_id[k] for k in sorted(by_id, key=lambda x: (len(x), x))]


def _load_state() -> dict:
    if STATE.exists():
        return json.loads(STATE.read_text(encoding="utf-8"))
    return {"completed": [], "gate_candidates": [], "started_utc": None}


def _save_state(state: dict) -> None:
    STATE.parent.mkdir(parents=True, exist_ok=True)
    STATE.write_text(json.dumps(state, indent=2), encoding="utf-8")


def _write_status(state: dict, msg: str) -> None:
    STATUS.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Autonomy research loop status",
        "",
        f"Updated (UTC): {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        f"**Message:** {msg}",
        "",
        f"- Completed generations: {state.get('completed')}",
        f"- Gate candidates: {len(state.get('gate_candidates') or [])}",
        f"- STOP file present: {STOP.exists()}",
        "",
        "Create `artifacts/autonomy/STOP` (empty file) to halt the loop cleanly.",
        "No live deploy from this loop. Max readiness remains `LIVE_STOP / RESEARCH_ONLY`",
        "until a frozen certificate + explicit host/account authorization.",
        "",
    ]
    for c in state.get("gate_candidates") or []:
        lines.append(
            f"- CANDIDATE `{c.get('gen')}` `{c.get('arm_id')}` "
            f"PF={c.get('profit_factor')} n={c.get('n_trades')} "
            f"ebr={c.get('entry_bar_exit_rate')} tpm={c.get('trades_per_month')}"
        )
    STATUS.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _write_alert(kind: str, body: str) -> None:
    ALERT.parent.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    ALERT.write_text(
        f"# Autonomy ALERT ({kind})\n\nUpdated (UTC): {ts}\n\n{body.strip()}\n",
        encoding="utf-8",
    )
    print(f"ALERT kind={kind}", flush=True)


def _seal_prereg(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    digest = _sha(path)
    if "preregister_sha256_at_run:" not in text:
        path.write_text(
            text.rstrip() + f"\n\npreregister_sha256_at_run: {digest}\n", encoding="utf-8"
        )
        digest = _sha(path)
    return digest


def _run_generation(gen: dict) -> int:
    script = _ROOT / gen["script"]
    args = [sys.executable, "-u", str(script)]
    for a in gen.get("args") or []:
        args.append(str(a))
    print("+", " ".join(args), flush=True)
    return int(subprocess.call(args, cwd=str(_ROOT)))


def _harvest_candidates(gen: dict, state: dict) -> None:
    report = _ROOT / gen["report_json"]
    if not report.exists():
        return
    data = json.loads(report.read_text(encoding="utf-8"))
    arms = data.get("arms") or []
    controls = {
        a["symbol"]: a
        for a in arms
        if a.get("mode") == "control" and a.get("status") == "RAN"
    }
    found = []
    for a in sorted(arms, key=rank_key):
        ctrl = controls.get(a.get("symbol"))
        if is_gate_candidate(a, ctrl):
            rec = {
                "gen": gen["id"],
                "arm_id": a.get("arm_id") or a.get("tag"),
                "symbol": a.get("symbol"),
                "event": a.get("event"),
                "profit_factor": a.get("profit_factor"),
                "win_rate": a.get("win_rate"),
                "sharpe_annualised": a.get("sharpe_annualised"),
                "expectancy_intent_all": a.get("expectancy_intent_all"),
                "n_trades": a.get("n_trades"),
                "trades_per_month": a.get("trades_per_month"),
                "entry_bar_exit_rate": a.get("entry_bar_exit_rate"),
                "control_pf": (ctrl or {}).get("profit_factor"),
            }
            found.append(rec)
            state.setdefault("gate_candidates", []).append(rec)
    if found:
        append_ledger(
            "AUTONOMY_GATE_CANDIDATE gen={gid} n={n} first={arm}".format(
                gid=gen["id"], n=len(found), arm=found[0]["arm_id"]
            ),
            tier=2,
        )
        print(f"GATE_CANDIDATES gen={gen['id']} n={len(found)}", flush=True)
        lines = [
            f"**Gate-passing filter(s) in generation {gen['id']}.**",
            "Still `LIVE_STOP / RESEARCH_ONLY` — not live, no deploy.",
            "",
        ]
        for c in found:
            lines.append(
                f"- `{c.get('arm_id')}` PF={c.get('profit_factor')} "
                f"vs control {c.get('control_pf')} n={c.get('n_trades')} "
                f"ebr={c.get('entry_bar_exit_rate')} tpm={c.get('trades_per_month')} "
                f"Sharpe={c.get('sharpe_annualised')}"
            )
        _write_alert("GATE_CANDIDATE", "\n".join(lines))
    else:
        append_ledger(
            f"AUTONOMY_GEN_DONE gen={gen['id']} promoted=none failure_is_success",
            tier=0,
        )
        print(f"no gate candidates gen={gen['id']}", flush=True)


def main() -> int:
    cfg = _load_queue()
    state = _load_state()
    if not state.get("started_utc"):
        state["started_utc"] = datetime.now(timezone.utc).isoformat()
        _save_state(state)
    append_ledger("AUTONOMY_RESEARCH_LOOP start", tier=0)
    _write_status(state, "loop started")

    while True:
        cfg = _load_queue()
        generations = _discover_generations(cfg)
        if STOP.exists():
            _write_status(state, "STOP file present — exiting cleanly")
            append_ledger("AUTONOMY_RESEARCH_LOOP stopped by STOP file", tier=0)
            return 0
        pending = [g for g in generations if g["id"] not in state.get("completed", [])]
        ae = cfg.get("auto_extend") or {}
        auto_on = ae.get("enabled", True) is not False
        if auto_on and len(pending) <= int(ae.get("min_remaining") or 12):
            added = ensure_queue_depth(
                min_remaining=int(ae.get("min_remaining") or 12),
                batch=int(ae.get("batch") or 8),
            )
            if added:
                print(
                    f"auto-froze generations {added[0]}..{added[-1]} n={len(added)}",
                    flush=True,
                )
                continue
        if pending and state.get("queue_exhausted_alerted"):
            state["queue_exhausted_alerted"] = False
            _save_state(state)
        if not pending:
            _write_status(state, "queue empty after auto-extend — freeze failed; retrying")
            n_cand = len(state.get("gate_candidates") or [])
            if not state.get("queue_exhausted_alerted"):
                _write_alert(
                    "QUEUE_EXTEND_FAILED",
                    "Auto-extend of unused public windows failed. "
                    f"Gate candidates so far: {n_cand}. "
                    "Not a TradingView scrape. Create `artifacts/autonomy/STOP` to halt.",
                )
                state["queue_exhausted_alerted"] = True
                _save_state(state)
            print(
                f"queue empty after auto-extend utc={datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')} "
                f"candidates={n_cand}",
                flush=True,
            )
            time.sleep(int(cfg.get("idle_poll_sec") or 15))
            continue
        gen = pending[0]
        print(f"=== autonomy generation {gen['id']} ===", flush=True)
        _write_status(state, f"running generation {gen['id']}")
        prereg = _ROOT / gen["preregister"]
        if not prereg.is_file():
            raise SystemExit(f"missing preregister {prereg}")
        digest = _seal_prereg(prereg)
        print(f"preregister_sha256={digest}", flush=True)
        rc = _run_generation(gen)
        if rc != 0:
            print(f"generation {gen['id']} exited {rc} — will retry after pause", flush=True)
            _write_status(state, f"generation {gen['id']} failed rc={rc}; retrying")
            time.sleep(60)
            continue
        _harvest_candidates(gen, state)
        state.setdefault("completed", []).append(gen["id"])
        _save_state(state)
        _write_status(state, f"completed generation {gen['id']}")
        # If we found candidates, keep going to deepen later gens; do not deploy.
        time.sleep(int(cfg.get("pause_between_gen_sec") or 10))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
