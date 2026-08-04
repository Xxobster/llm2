"""One-shot sealed lockbox validation for expansion pairs (prereg final_001).

- Freezes missing direction packs with train cut < FORWARD_LOCKBOX_START.
- Runs tradesim lockbox once (no multi-arm, no Finplot by default).
- Appends peeks; quotes settle PF for promotion, lockbox as diagnostic only.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

os.environ.setdefault("TRADESIM_NO_PLOT", "1")

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

import yaml  # noqa: E402

from llm2.evidence.lockbox_guard import require_lockbox_access  # noqa: E402
from llm2.evidence.peek_log import append_peek  # noqa: E402
from llm2.paths import ARTIFACTS, FORWARD_LOCKBOX_START, ROOT  # noqa: E402
from llm2.research_policy import (  # noqa: E402
    EXPANSION_LOCKBOX_FINAL_GENERATION,
    PolicyError,
    refuse_already_peeked_on_expansion_pristine_set,
    refuse_expansion_lockbox_multi_arm,
)
from llm2.validation.folds import OUTER_FOLD_RANGES  # noqa: E402

GENERATION = EXPANSION_LOCKBOX_FINAL_GENERATION
PREREG = ROOT / "configs" / "preregister" / f"{GENERATION}.yaml"
SETTLE_DEFAULT = (
    ARTIFACTS / "reports" / "structure_v1_expansion_settle_20260803T181235Z.json"
)


def refuse_multi_arm(argv: list[str]) -> None:
    """CLI wrapper used by tests and main."""
    refuse_expansion_lockbox_multi_arm(argv=argv, generation_id=GENERATION)


def load_prereg(path: Path = PREREG) -> dict[str, Any]:
    if not path.is_file():
        raise SystemExit(f"prereg missing: {path}")
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def pack_path(symbol: str, target: str = "direction") -> Path:
    return ARTIFACTS / "live_packs" / f"structure_v1_{symbol.lower()}_{target}"


def ensure_pack(symbol: str, target: str = "direction") -> Path:
    pack = pack_path(symbol, target)
    if (pack / "model.joblib").is_file() and (pack / "strategy.json").is_file():
        return pack
    print(f"FREEZE pack {symbol} {target} …", flush=True)
    cmd = [
        sys.executable,
        str(ROOT / "scripts" / "build_structure_symbol_pack.py"),
        "--symbol",
        symbol,
        "--target",
        target,
    ]
    env = os.environ.copy()
    env["PYTHONPATH"] = str(ROOT) + os.pathsep + env.get("PYTHONPATH", "")
    subprocess.check_call(cmd, cwd=str(ROOT), env=env)
    return pack


def assert_pack_train_cut(pack: Path) -> dict[str, Any]:
    """Fail closed if pack strategy admits training into the lockbox."""
    import pandas as pd

    strat = json.loads((pack / "strategy.json").read_text(encoding="utf-8"))
    trained = str(strat.get("trained_until_exclusive") or strat.get("trained_until") or "")
    lockbox = str(strat.get("lockbox_start") or FORWARD_LOCKBOX_START)
    notes = {
        "strategy_id": strat.get("strategy_id"),
        "trained_until_exclusive": trained,
        "lockbox_start": lockbox,
        "symbol": strat.get("symbol"),
    }
    if trained:
        t = pd.Timestamp(trained, tz="UTC")
        lock = pd.Timestamp(lockbox, tz="UTC")
        if t >= lock:
            raise PolicyError(
                f"pack {pack} trained_until {trained} reaches into lockbox {lockbox}"
            )
    last_oos = OUTER_FOLD_RANGES[-1][0]
    notes["expected_trained_before"] = last_oos
    notes["train_cut_ok"] = True
    return notes


def _import_run_one():
    path = ROOT / "scripts" / "plot_structure_lockbox.py"
    spec = importlib.util.spec_from_file_location("plot_structure_lockbox", path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    sys.modules["plot_structure_lockbox"] = mod
    spec.loader.exec_module(mod)
    return mod._run_one


def settle_pf_map(settle_path: Path) -> dict[tuple[str, str], float]:
    if not settle_path.is_file():
        return {}
    d = json.loads(settle_path.read_text(encoding="utf-8"))
    out: dict[tuple[str, str], float] = {}
    for c in d.get("combos") or []:
        if str(c.get("overall")) != "PASS":
            continue
        sym = str(c.get("symbol") or "").upper()
        tgt = str(c.get("target") or "")
        try:
            out[(sym, tgt)] = float(c.get("pooled_pf"))
        except (TypeError, ValueError):
            continue
    return out


def main(argv: list[str] | None = None) -> int:
    argv = list(argv if argv is not None else sys.argv[1:])
    refuse_multi_arm(argv)

    ap = argparse.ArgumentParser(description=f"{GENERATION} one-shot lockbox")
    ap.add_argument("--prereg", type=Path, default=PREREG)
    ap.add_argument("--settle", type=Path, default=SETTLE_DEFAULT)
    ap.add_argument("--start", default=FORWARD_LOCKBOX_START)
    ap.add_argument(
        "--symbols",
        default="",
        help="comma list; default = pristine_candidates from prereg",
    )
    ap.add_argument(
        "--skip-freeze",
        action="store_true",
        help="do not call build_structure_symbol_pack (require existing packs)",
    )
    ap.add_argument(
        "--i-accept-lockbox-contamination",
        action="store_true",
        dest="i_accept_lockbox_contamination",
        help=(
            "Required to re-open lockbox after the first sealed one-shot. "
            "First run with matching frozen prereg is authorized without this flag."
        ),
    )
    args = ap.parse_args(argv)

    prereg = load_prereg(args.prereg)
    if str(prereg.get("generation_id")) != GENERATION:
        raise SystemExit(f"prereg generation_id mismatch: {prereg.get('generation_id')}")

    settle_pfs = settle_pf_map(args.settle)
    cands = prereg.get("pristine_candidates") or []
    if args.symbols.strip():
        want = {s.strip().upper() for s in args.symbols.split(",") if s.strip()}
        symbols = [str(c["symbol"]).upper() for c in cands if str(c["symbol"]).upper() in want]
        if not symbols:
            # Allow explicit list only if none are already excluded
            symbols = sorted(want)
    else:
        symbols = [str(c["symbol"]).upper() for c in cands]

    for s in symbols:
        refuse_already_peeked_on_expansion_pristine_set(symbol=s, generation_id=GENERATION)

    # Prereg-backed first open is intentional; re-runs still need explicit accept.
    from llm2.evidence.peek_log import read_peeks

    prior = {r.get("experiment_id") for r in read_peeks()}
    already_ran = GENERATION in prior
    accepted = (not already_ran) or bool(args.i_accept_lockbox_contamination)
    try:
        require_lockbox_access(
            experiment_id=GENERATION,
            window_start=str(args.start),
            purpose="one_shot_expansion_lockbox_batch",
            symbols=symbols,
            n_arms=1,
            accepted_contamination=accepted,
            open_finplot=False,
            notes=(
                "prereg structure_v1_expansion_lockbox_final_001; Finplot never opened"
                + ("; re-run" if already_ran else "; first_authorized_prereg_open")
            ),
        )
    except PolicyError as exc:
        print(f"REFUSED: {exc}", flush=True)
        return 2

    from llm2.backtest.conformance import run_conformance_check

    conf = run_conformance_check(quiet=True)
    if not conf.get("passed"):
        print("CONFORMANCE_FAIL", conf, flush=True)
        return 2

    run_one = _import_run_one()
    results: list[dict[str, Any]] = []
    for sym in symbols:
        if not args.skip_freeze:
            pack = ensure_pack(sym, "direction")
        else:
            pack = pack_path(sym, "direction")
            if not (pack / "model.joblib").is_file():
                raise SystemExit(f"missing pack {pack}")
        cut = assert_pack_train_cut(pack)
        print(f"LOCKBOX {sym} pack={pack}", flush=True)
        try:
            row = run_one(
                symbol=sym,
                pack_dir=pack,
                start=str(args.start),
                trade_cap=120,
                store=False,
                show=False,
            )
        except Exception as exc:  # noqa: BLE001
            row = {
                "symbol": sym,
                "error": f"{type(exc).__name__}: {exc}",
                "evidence_class": "LOCKBOX_OPEN_FAILED",
            }
        row["train_cut"] = cut
        row["settle_pooled_pf"] = settle_pfs.get((sym, "direction"))
        row["promotion_quote"] = "outer_fold_settle_only"
        row["lockbox_role"] = "diagnostic_one_shot_final"
        results.append(row)
        append_peek(
            experiment_id=f"{GENERATION}_{sym}",
            window_start=str(args.start),
            window_end=str(row.get("data_end") or "unknown"),
            purpose="one_shot_expansion_lockbox",
            arms=f"single_book tp=1% sl=2% hold=6 pack={pack.name}",
            n_arms=1,
            evidence_class="LOCKBOX_OPENED_CONTAMINATED",
            notes=f"generation={GENERATION}; settle_pf={row.get('settle_pooled_pf')}",
        )

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    payload = {
        "generation_id": GENERATION,
        "prereg": str(args.prereg.relative_to(ROOT)).replace("\\", "/"),
        "lockbox_start": str(args.start),
        "stamped_utc": stamp,
        "evidence_class": "LOCKBOX_OPENED_CONTAMINATED",
        "note": (
            "One-shot sealed expansion lockbox. Before this run symbols were pristine "
            "candidates; after this run the window is peeeed for these packs. "
            "Quote promotion from settle outer-OOS pooled PF, not lockbox PF."
        ),
        "quotable": "settle_pooled_pf fields + expansion_settle report",
        "decision": "D-037",
        "results": results,
        "min_size_equity_caveat": True,
    }
    out = ARTIFACTS / "reports" / f"{GENERATION}_{stamp}.json"
    latest = ARTIFACTS / "reports" / f"{GENERATION}_latest.json"
    ARTIFACTS.joinpath("reports").mkdir(parents=True, exist_ok=True)
    text = json.dumps(payload, indent=2, default=str) + "\n"
    out.write_text(text, encoding="utf-8")
    latest.write_text(text, encoding="utf-8")

    append_peek(
        experiment_id=f"{GENERATION}_done",
        window_start=str(args.start),
        window_end=stamp,
        purpose="one_shot_expansion_lockbox_batch",
        arms=symbols,
        n_arms=len(symbols),
        evidence_class="LOCKBOX_OPENED_CONTAMINATED",
        notes=str(out.name),
    )

    print(f"wrote {out}", flush=True)
    ok = [r for r in results if "error" not in r]
    bad = [r for r in results if "error" in r]
    print(f"ok={len(ok)} failed={len(bad)}", flush=True)
    for r in ok:
        print(
            f"  {r['symbol']} n={r.get('n_trades')} pf={r.get('profit_factor')} "
            f"settle_pf={r.get('settle_pooled_pf')}",
            flush=True,
        )
    for r in bad:
        print(f"  FAIL {r['symbol']} {r.get('error')}", flush=True)
    return 0 if not bad else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except PolicyError as exc:
        print(f"REFUSED: {exc}", flush=True)
        raise SystemExit(2) from exc
