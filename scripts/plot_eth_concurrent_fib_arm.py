"""One arm of the concurrent fib/clarity grid on lockbox (sealed; dual accept for Finplot)."""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

os.environ.setdefault("TRADESIM_NO_PLOT", "1")

from tradesim.ensure_source import prefer_botsgeneral_tradesim

prefer_botsgeneral_tradesim()

from tradesim.research.plot import plot_backtest  # noqa: E402

from llm2.backtest.conformance import run_conformance_check  # noqa: E402
from llm2.backtest.run import ohlcv_to_bar_series, run_strategy_backtest  # noqa: E402
from tradesim import research_margin, research_sizing, research_sim_hedge  # noqa: E402

from llm2.evidence.lockbox_guard import (  # noqa: E402
    add_lockbox_guard_args,
    require_lockbox_access,
    seal_finplot_unless_authorized,
)
from llm2.gates.evidence import research_costs_baseline  # noqa: E402
from llm2.paths import FORWARD_LOCKBOX_START  # noqa: E402
from llm2.research_policy import PolicyError  # noqa: E402

# Import hunt helpers
sys.path.insert(0, str(_ROOT / "scripts"))
from hunt_eth_concurrent_fib_clarity import (  # noqa: E402
    BASE_HOLD,
    PACK,
    SYMBOL,
    build_tiered_signals,
    prepare,
)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--clarity", default="none")
    ap.add_argument("--fib-ext", type=float, default=0.618, dest="fib_ext")
    ap.add_argument("--hold", type=int, default=12)
    ap.add_argument("--k", type=int, default=0, help="0 = unlimited")
    ap.add_argument("--start", default=FORWARD_LOCKBOX_START)
    ap.add_argument("--show", action="store_true", help="Finplot (needs dual accept).")
    ap.add_argument("--no-show", action="store_true", help="Deprecated: Finplot off by default.")
    ap.add_argument("--trade-cap", type=int, default=120)
    add_lockbox_guard_args(ap)
    args = ap.parse_args(argv)

    open_finplot = bool(args.show) and not bool(args.no_show)
    try:
        require_lockbox_access(
            experiment_id="structure_v1_eth_concurrent_fib_arm_plot",
            window_start=str(args.start),
            purpose="finplot_lockbox_open" if open_finplot else "lockbox_report_only",
            symbols=[SYMBOL],
            accepted_contamination=bool(args.i_accept_lockbox_contamination),
            open_finplot=open_finplot,
            accepted_finplot=bool(args.i_accept_finplot_lockbox),
            notes="scripts/plot_eth_concurrent_fib_arm.py",
        )
    except PolicyError as exc:
        print(f"REFUSED: {exc}", flush=True)
        return 2

    show = seal_finplot_unless_authorized(
        open_finplot=open_finplot,
        accepted_finplot=bool(args.i_accept_finplot_lockbox),
    )

    if not run_conformance_check(quiet=True).get("passed"):
        print("conformance not green")
        return 1
    if not (PACK / "model.joblib").is_file():
        raise SystemExit(f"missing {PACK}")

    from hunt_eth_concurrent_fib_clarity import (  # type: ignore
        UNLIMITED_K,
        extended_tp_offset,
        k_label,
        resolve_k,
    )

    ctx = prepare(args.start)
    k_use = resolve_k(int(args.k)) if int(args.k) > 0 else UNLIMITED_K
    tp_off = extended_tp_offset(float(args.fib_ext))
    print(f"fib_ext={args.fib_ext} -> target_offset={tp_off:.4%} K={k_label(int(args.k))}", flush=True)
    sigs, stats = build_tiered_signals(
        ctx,
        clarity=args.clarity,  # type: ignore[arg-type]
        fib_ext=float(args.fib_ext),
        hold_addon=int(args.hold),
        max_per_side=k_use,
        uniform_baseline=False,
    )
    print("build_stats", stats, flush=True)

    sim = research_sim_hedge(
        max_hold_bars=max(BASE_HOLD, int(args.hold)),
        decision_timeframe=ctx.timeframe,
        max_positions_per_side=int(k_use),
        max_positions_per_symbol=int(k_use) * 2,
    )
    label = f"clarity={args.clarity}|fib_ext={args.fib_ext}|hold={args.hold}|K={k_label(int(args.k))}"
    bundle = run_strategy_backtest(
        ctx.window,
        sigs,
        symbol=SYMBOL,
        timeframe=ctx.timeframe,
        strategy_id=f"llm2-eth-fib-plot-{args.clarity}-k{args.k}",
        touch_ohlcv=ctx.touch_win,
        touch_timeframe=ctx.touch_tf,
        costs=research_costs_baseline(),
        margin=research_margin(leverage=ctx.lev),
        sizing=research_sizing(),
        sim=sim,
        instrument=ctx.instrument,
        funding_ts_ms=ctx.funding_ts,
        funding_rate=ctx.funding_rt,
        strategy_meta={
            "name": label,
            "evidence_class": "LOCKBOX_OPENED_CONTAMINATED",
            "batch": "structure_v1_eth_fib_plot",
            "tp_offset_book3plus": tp_off,
        },
        plot=False,
        print_headline=True,
        store_path=None,
    )
    m = bundle.metrics
    if show:
        bars = ohlcv_to_bar_series(
            ctx.window.loc[ctx.window.index >= ctx.start_ts],
            symbol=SYMBOL,
            timeframe=ctx.timeframe,
        )
        plot_backtest(
            bars,
            bundle.result,
            title=(
                f"{SYMBOL} 1h | {label} LOCKBOX "
                f"BT_PnL={m.net_pnl:.2f} PF={m.profit_factor:.2f} n={m.n_trades} "
                f"TP3+={tp_off:.2%}"
            ),
            metrics=bundle.metrics,
            trade_style="boxes",
            max_zone_trades=int(args.trade_cap),
            strategy_meta={
                "name": label,
                "evidence_class": "LOCKBOX_OPENED_CONTAMINATED",
            },
            show=True,
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
