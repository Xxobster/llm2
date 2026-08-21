#!/usr/bin/env python3
"""SHADOW-only 1-minute indicator parity bot (no train, no trades).

On each closed Binance USD-M Last 1m bar:

1. Upsert warehouse tip into ``market_ohlcv`` (or caller candles DB).
2. Recompute structure into a dedicated research DB and a live-path slice.
3. Diff tip ``bar_features``; ledger PASS/FAIL.

**Use only for indicator / candle tip identity.** Production 1h fleet pack
structure and ``pred_mean`` checks stay on
``scripts/ops_live_research_parity_gate.py``. After warehouse or collector heals,
re-run ``--once`` on this bot before debugging live structure packs.

Examples::

  python scripts/run_1m_indicator_parity_bot.py --once --symbol ETHUSDT
  python scripts/run_1m_indicator_parity_bot.py --loop --symbol ETHUSDT
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from llm2.live.indicator_parity_1m import (  # noqa: E402
    DEFAULT_CANDLES_DB,
    DEFAULT_LIVE_SLICE,
    DEFAULT_PARITY_LEDGER,
    DEFAULT_RESEARCH_IND,
    DEFAULT_SEED_BARS,
    TIMEFRAME,
    diff_tip,
    ensure_seed,
    init_parity_ledger,
    latest_closed_bar_open_ms,
    record_parity,
    tip_diff_to_dict,
    update_research_and_live_tips,
)
from llm2.live.micro_runner import sleep_until_next_close  # noqa: E402
from llm2.paths import TF_MS  # noqa: E402


def _one_cycle(
    *,
    symbol: str,
    seed_bars: int,
    candles_db: Path,
    live_slice: Path,
    research_ind: Path,
    parity_db: Path,
    abs_eps: float,
    seeded: bool,
    bar_ts_ms: int | None = None,
) -> tuple[bool, dict]:
    if not seeded:
        seed_rep = ensure_seed(
            symbol=symbol,
            seed_bars=seed_bars,
            candles_db=candles_db,
            live_slice=live_slice,
            research_ind=research_ind,
        )
        if not seed_rep.get("seed_ok"):
            print(
                f"FAIL phase=seed symbol={symbol.upper()} "
                f"detail={json.dumps(seed_rep, default=str)[:500]}",
                flush=True,
            )
            return False, {"phase": "seed", **seed_rep}
        bar_ts = int(bar_ts_ms if bar_ts_ms is not None else seed_rep["tip_ts_ms"])
        # Re-run tip update so seed + first cycle share the same code path.
        upd = update_research_and_live_tips(
            symbol=symbol,
            seed_bars=seed_bars,
            candles_db=candles_db,
            live_slice=live_slice,
            research_ind=research_ind,
            bar_ts_ms=bar_ts,
        )
    else:
        closed = int(
            bar_ts_ms
            if bar_ts_ms is not None
            else latest_closed_bar_open_ms(TIMEFRAME)
        )
        upd = update_research_and_live_tips(
            symbol=symbol,
            seed_bars=seed_bars,
            candles_db=candles_db,
            live_slice=live_slice,
            research_ind=research_ind,
            bar_ts_ms=closed,
        )
        bar_ts = int(upd.get("bar_ts_ms") or closed)

    if "error" in upd:
        print(
            f"FAIL phase=update symbol={symbol.upper()} "
            f"detail={json.dumps(upd, default=str)[:500]}",
            flush=True,
        )
        return False, {"phase": "update", **upd}

    d = diff_tip(
        symbol=symbol,
        ts_ms=bar_ts,
        live_slice=live_slice,
        research_ind=research_ind,
        abs_eps=abs_eps,
    )
    ok = bool(
        d.identical
        and d.ohlc_tip_equal
        and d.n_mismatch == 0
        and d.n_cols > 0
    )
    detail = {
        "update": {
            k: upd[k]
            for k in ("bar_ts_ms", "n_ohlcv", "ohlc_tip")
            if k in upd
        },
        "diff": tip_diff_to_dict(d),
    }
    record_parity(
        d,
        symbol=symbol,
        pass_ok=ok,
        detail=detail,
        path=parity_db,
    )
    bar_utc = datetime.fromtimestamp(bar_ts / 1000, tz=timezone.utc).isoformat()
    print(
        f"{'PASS' if ok else 'FAIL'} symbol={symbol.upper()} tf={TIMEFRAME} "
        f"bar={bar_utc} close_live={d.live_close} close_res={d.research_close} "
        f"n_mismatch={d.n_mismatch} max_abs={d.max_abs} tip50_eq={d.tip50_hash_equal} "
        f"n_cols={d.n_cols}",
        flush=True,
    )
    if not ok and d.first_mismatches:
        print(json.dumps({"first_mismatches": d.first_mismatches}, default=str), flush=True)
    return ok, detail


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--once", action="store_true", help="Single closed-bar check; exit 1 on FAIL")
    p.add_argument("--loop", action="store_true", help="Catch-up then every closed 1m")
    p.add_argument("--symbol", default="ETHUSDT")
    p.add_argument("--seed-bars", type=int, default=DEFAULT_SEED_BARS)
    p.add_argument("--abs-eps", type=float, default=1e-9)
    p.add_argument("--candles-db", type=Path, default=DEFAULT_CANDLES_DB)
    p.add_argument("--live-slice", type=Path, default=DEFAULT_LIVE_SLICE)
    p.add_argument("--research-ind", type=Path, default=DEFAULT_RESEARCH_IND)
    p.add_argument("--parity-db", type=Path, default=DEFAULT_PARITY_LEDGER)
    p.add_argument(
        "--force-seed",
        action="store_true",
        help="Always re-seed deep window before first cycle",
    )
    args = p.parse_args(argv)

    if not args.once and not args.loop:
        p.error("Specify --once or --loop")

    init_parity_ledger(args.parity_db)
    need_seed = bool(args.force_seed)
    if not need_seed:
        need_seed = not (
            args.live_slice.is_file()
            and args.research_ind.is_file()
            and args.candles_db.is_file()
        )

    last_done: int | None = None
    consecutive_pass = 0

    cycle_kw = dict(
        symbol=args.symbol,
        seed_bars=args.seed_bars,
        candles_db=args.candles_db,
        live_slice=args.live_slice,
        research_ind=args.research_ind,
        parity_db=args.parity_db,
        abs_eps=args.abs_eps,
    )

    if args.once:
        ok, _ = _one_cycle(
            seeded=not need_seed,
            bar_ts_ms=latest_closed_bar_open_ms(TIMEFRAME),
            **cycle_kw,
        )
        return 0 if ok else 1

    # Loop: catch-up unprocessed closed bars, then wait for next close.
    print(
        json.dumps(
            {
                "mode": "loop",
                "symbol": args.symbol.upper(),
                "timeframe": TIMEFRAME,
                "seed_bars": int(args.seed_bars),
                "live_slice": str(args.live_slice),
                "research_ind": str(args.research_ind),
                "parity_db": str(args.parity_db),
                "orders": False,
                "readiness_claim": None,
            }
        ),
        flush=True,
    )
    while True:
        latest = latest_closed_bar_open_ms(TIMEFRAME)
        if last_done is None or latest > last_done:
            # Process each closed minute from last_done+1m..latest (catch-up).
            step = int(TF_MS[TIMEFRAME])
            if last_done is None:
                targets = [latest]
            else:
                targets = list(range(last_done + step, latest + 1, step))
            for bar_ts in targets:
                ok, _ = _one_cycle(
                    seeded=not need_seed,
                    bar_ts_ms=bar_ts,
                    **cycle_kw,
                )
                need_seed = False
                last_done = bar_ts
                consecutive_pass = consecutive_pass + 1 if ok else 0
                if consecutive_pass >= 3:
                    print(
                        f"PROGRESS consecutive_pass={consecutive_pass}",
                        flush=True,
                    )
        sleep_until_next_close(TIMEFRAME, lead_sec=2.0)
        # After close + small lead residual: brief poll so kline is visible.
        time.sleep(1.5)


if __name__ == "__main__":
    raise SystemExit(main())
