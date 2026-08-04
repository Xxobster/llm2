"""LLM2 command-line interface."""

from __future__ import annotations

import argparse
import json
import sys

import numpy as np

from llm2.audit.data_audit import audit_ohlcv
from llm2.audit.predictability import audit_predictability
from llm2.data.loader import load_ohlcv
from llm2.features.guard import run_audit_for_space
from llm2.features.ohlcv_v1 import build_ohlcv_v1
from llm2.gates.v21 import V21_THRESHOLDS, evaluate_v21_gates, format_gates_table
from llm2.hunt.runner import HuntConfig, run_hunt
from llm2.paths import FORWARD_LOCKBOX_START, ensure_artifact_dirs
from llm2.registry.db import ResearchDB


def cmd_audit_data(args: argparse.Namespace) -> int:
    report = audit_ohlcv(args.symbol, args.timeframe, source=args.source)
    print(json.dumps(report.__dict__, indent=2, default=str))
    return 0 if report.passed else 1


def cmd_audit_predictability(args: argparse.Namespace) -> int:
    ohlcv = load_ohlcv(args.symbol, args.timeframe, source=args.source)
    feats = build_ohlcv_v1(ohlcv).dropna()
    y = ohlcv["close"].pct_change(args.horizon).shift(-args.horizon).reindex(feats.index).to_numpy()
    X = feats.to_numpy()
    mask = np.isfinite(y) & np.all(np.isfinite(X), axis=1)
    report = audit_predictability(X[mask], y[mask], target="fwd_return")
    print(json.dumps(report.__dict__, indent=2))
    return 0 if report.passed else 1


def cmd_diagnose(args: argparse.Namespace) -> int:
    from llm2.diagnostics.report import persist, run_diagnostics, write_report

    result = run_diagnostics(
        args.symbol,
        args.timeframe,
        train_end=args.train_end,
        external_timeframe=args.external_timeframe,
        horizons=tuple(int(h) for h in args.horizons.split(",")),
        confluence_symbols=tuple(s.strip() for s in args.confluence_symbols.split(",") if s.strip()),
        include_funding=not args.no_funding,
        seed=args.seed,
    )
    persist(result)
    path = write_report(result)

    survivors = result.survivors()
    total = sum(len(v) for v in result.families.values())
    print(f"\n{result.run_id}: {len(survivors)} of {total} effects survive FDR")
    for eff in survivors[:25]:
        print(f"  {eff.name:60s} stat={eff.statistic:+.5f} q={eff.q_value:.4f} n={eff.n}")
    print(f"\nReport: {path}")
    return 0


def cmd_wave(args: argparse.Namespace) -> int:
    from llm2.diagnostics.wave import fit_wave, period_table, phase_lead_scan

    import pandas as pd

    symbols = [s.strip().upper() for s in args.symbols.split(",") if s.strip()]
    fits: dict = {}
    closes: dict = {}
    for sym in symbols:
        close = None
        try:
            close = load_ohlcv(sym, args.timeframe, source=args.source)["close"]
        except Exception:  # noqa: BLE001
            from llm2.data.macro import load_external

            try:
                ext = load_external(sym, args.timeframe)
            except Exception as exc:  # noqa: BLE001
                print(f"  {sym}: unavailable ({exc})")
                continue
            # The macro loader hands back a completion-indexed Series for some series and
            # a frame for others; take the close either way rather than assuming.
            close = ext if isinstance(ext, pd.Series) else ext[
                "close" if "close" in ext.columns else ext.columns[0]
            ]
        fits[sym] = fit_wave(close, symbol=sym, timeframe=args.timeframe, seed=args.seed)
        closes[sym] = close
        print(f"  {fits[sym].summary()}")

    if not fits:
        print("no series could be fitted")
        return 1

    print("\n=== dominant cycle per series ===")
    print(period_table(fits).to_string(index=False))

    if args.reference in fits and len(fits) > 1:
        # Every series is refiltered at one common period. Comparing waves fitted at
        # different periods measures the difference in the filters' group delay, not a
        # lead between the markets.
        leads = phase_lead_scan(
            fits, args.reference, max_lag_bars=args.max_lag, closes=closes
        )
        survivors = [e for e in leads if e.significant]
        genuine = [e for e in leads if e.detail.get("leads_beyond_contemporaneous", 0) > 0]
        period = fits[args.reference].period_bars
        print(f"\n=== wave phase lead into {args.reference} "
              f"(all series refiltered at {period:.1f} bars) ===")
        print(f"{len(survivors)} of {len(leads)} survive FDR; "
              f"{len(genuine)} beat their own contemporaneous correlation")
        print(f"  {'pair':44s} {'lead_r':>8s} {'lag':>5s} {'lag0_r':>8s} {'q':>8s}  verdict")
        for eff in sorted(leads, key=lambda e: -abs(e.statistic))[:20]:
            lag = eff.detail.get("lag_bars", float("nan"))
            c0 = eff.detail.get("corr_lag0", float("nan"))
            q = eff.q_value if eff.q_value is not None else float("nan")
            verdict = "LEADS" if eff.detail.get("leads_beyond_contemporaneous", 0) > 0 else "co-moves"
            print(f"  {eff.name:44s} {eff.statistic:+8.3f} {lag:5.0f} {c0:+8.3f} {q:8.4f}  {verdict}")

    if args.plot:
        from llm2.diagnostics.waveplot import plot_wave

        target = args.reference if args.reference in fits else symbols[0]
        ohlcv = load_ohlcv(target, args.timeframe, source=args.source)
        df = ohlcv.tail(args.plot_bars) if args.plot_bars else ohlcv
        refit = fit_wave(df["close"], symbol=target, timeframe=args.timeframe, seed=args.seed)
        print(f"\nOpening chart for {target} ({len(df):,} bars). Close the window to continue.")
        plot_wave(df, refit, symbol=target, timeframe=args.timeframe, show=True)
    return 0


def cmd_leakage_check(args: argparse.Namespace) -> int:
    ohlcv = load_ohlcv(args.symbol, args.timeframe, source=args.source)
    if args.space == "all":
        from llm2.features.guard import audit_all_spaces

        results = audit_all_spaces(ohlcv, interval=args.timeframe, symbol=args.symbol)
        print(json.dumps({k: {"passed": v.get("passed"), "error": v.get("error")} for k, v in results.items()}, indent=2))
        return 0 if all(v.get("passed") for v in results.values() if "passed" in v) else 1
    res = run_audit_for_space(
        ohlcv, interval=args.timeframe, space=args.space, symbol=args.symbol, cuts=args.cuts
    )
    print(res["report_text"])
    return 0 if res["passed"] else 1


def cmd_hunt(args: argparse.Namespace) -> int:
    from llm2.hunt.runner import run_nested_hunt

    cfg = HuntConfig(
        generation_id=args.generation_id,
        symbol=args.symbol,
        timeframe=args.timeframe,
        target=args.target,
        feature_space=args.space,
        horizon=args.horizon,
        max_trials=args.max_trials,
        seed=args.seed,
        run_backtest=not args.no_backtest,
    )
    summary = run_nested_hunt(cfg)
    print(json.dumps(summary, indent=2, default=str))
    return 0 if summary.get("status") in ("COMPLETE", "LEGACY_SMOKE") else 1


def cmd_list_trials(args: argparse.Namespace) -> int:
    db = ResearchDB()
    trials = db.list_trials(args.generation_id)
    print(json.dumps(trials, indent=2, default=str))
    return 0


def cmd_show_gates(_args: argparse.Namespace) -> int:
    gates = evaluate_v21_gates()
    print(format_gates_table(gates))
    print("\nThresholds:", json.dumps(V21_THRESHOLDS, indent=2))
    return 0


def cmd_refresh(args: argparse.Namespace) -> int:
    from llm2.data.refresh import ensure_candles

    symbols = [s.strip().upper() for s in args.symbols.split(",") if s.strip()]
    timeframes = [t.strip().lower() for t in args.timeframes.split(",") if t.strip()]
    code = ensure_candles(symbols, timeframes, price_types=("last", "mark"), quiet=False)
    print(json.dumps({"exit_code": code, "symbols": symbols, "timeframes": timeframes}))
    return int(code)


def cmd_pipeline(args: argparse.Namespace) -> int:
    """Stage A data audit → leakage → predictability → nested hunt."""
    from llm2.hunt.runner import run_nested_hunt

    data_rep = audit_ohlcv(args.symbol, args.timeframe)
    print("DATA_AUDIT", json.dumps(data_rep.__dict__, default=str))
    if not data_rep.passed:
        return 1

    ohlcv = load_ohlcv(args.symbol, args.timeframe)
    leak = run_audit_for_space(
        ohlcv.tail(8000), interval=args.timeframe, space=args.space, symbol=args.symbol
    )
    print("LEAKAGE", "PASS" if leak["passed"] else "FAIL")
    if not leak["passed"]:
        print(leak["report_text"])
        return 1

    cfg = HuntConfig(
        generation_id=args.generation_id,
        symbol=args.symbol,
        timeframe=args.timeframe,
        target=args.target,
        feature_space=args.space,
        max_trials=args.max_trials,
    )
    summary = run_nested_hunt(cfg)
    print(json.dumps(summary, indent=2, default=str))
    return 0 if summary.get("status") == "COMPLETE" else 1


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="llm2", description="LLM2 predictability laboratory")
    sub = p.add_subparsers(dest="command", required=True)

    a = sub.add_parser("audit-data", help="Audit market OHLCV quality")
    a.add_argument("--symbol", default="BTCUSDT")
    a.add_argument("--timeframe", default="1h")
    a.add_argument("--source", default="binance")
    a.set_defaults(func=cmd_audit_data)

    b = sub.add_parser("audit-predictability", help="Surrogate null predictability audit")
    b.add_argument("--symbol", default="BTCUSDT")
    b.add_argument("--timeframe", default="1h")
    b.add_argument("--source", default="binance")
    b.add_argument("--horizon", type=int, default=1)
    b.set_defaults(func=cmd_audit_predictability)

    c = sub.add_parser("leakage-check", help="Shared leakage audit for feature space")
    c.add_argument("--symbol", default="BTCUSDT")
    c.add_argument("--timeframe", default="1h")
    c.add_argument("--source", default="binance")
    c.add_argument("--space", default="ohlcv_v1")
    c.add_argument("--cuts", type=int, default=3)
    c.set_defaults(func=cmd_leakage_check)

    h = sub.add_parser("hunt", help="Run nested walk-forward hunt generation")
    h.add_argument("--generation-id", required=True)
    h.add_argument("--symbol", default="BTCUSDT")
    h.add_argument("--timeframe", default="1h")
    h.add_argument("--source", default="binance")
    h.add_argument("--target", default="fwd_return")
    h.add_argument("--space", default="ohlcv_v1")
    h.add_argument("--horizon", type=int, default=6)
    h.add_argument("--max-trials", type=int, default=6)
    h.add_argument("--seed", type=int, default=42)
    h.add_argument("--no-backtest", action="store_true", help="Use return proxy instead of tradesim")
    h.set_defaults(func=cmd_hunt)

    r = sub.add_parser("refresh-candles", help="Refresh warehouse candles via tradesim")
    r.add_argument("--symbols", default="BTCUSDT,ETHUSDT,SOLUSDT")
    r.add_argument("--timeframes", default="5m,15m,1h,4h,1m")
    r.set_defaults(func=cmd_refresh)

    p_cmd = sub.add_parser("pipeline", help="Run Stage A/B audit then a bounded hunt")
    p_cmd.add_argument("--generation-id", required=True)
    p_cmd.add_argument("--symbol", default="BTCUSDT")
    p_cmd.add_argument("--timeframe", default="1h")
    p_cmd.add_argument("--target", default="fwd_return")
    p_cmd.add_argument("--space", default="ohlcv_v1")
    p_cmd.add_argument("--max-trials", type=int, default=6)
    p_cmd.set_defaults(func=cmd_pipeline)

    t = sub.add_parser("list-trials", help="List trials from registry")
    t.add_argument("--generation-id", default=None)
    t.set_defaults(func=cmd_list_trials)

    g = sub.add_parser("show-gates", help="Show V2.1 gate table")
    g.set_defaults(func=cmd_show_gates)

    d = sub.add_parser("diagnose", help="Descriptive structure and cross-asset diagnostics")
    d.add_argument("--symbol", default="BTCUSDT")
    d.add_argument("--timeframe", default="1h")
    d.add_argument("--external-timeframe", default=None, help="Defaults to the decision timeframe")
    d.add_argument("--train-end", default=FORWARD_LOCKBOX_START)
    d.add_argument("--horizons", default="1,6,24")
    d.add_argument("--confluence-symbols", default="DXY,SPX,VIX,XAUUSD")
    d.add_argument("--no-funding", action="store_true")
    d.add_argument("--seed", type=int, default=0)
    d.set_defaults(func=cmd_diagnose)

    w = sub.add_parser("wave", help="Fit market-strength waves and compare them across assets")
    w.add_argument("--symbols", default="BTCUSDT",
                   help="comma-separated; crypto from the market warehouse, macro from the registry")
    w.add_argument("--timeframe", default="1h")
    w.add_argument("--source", default="binance")
    w.add_argument("--reference", default="BTCUSDT", help="asset the phase lead is measured into")
    w.add_argument("--max-lag", type=int, default=48, help="maximum lead in bars to search")
    w.add_argument("--seed", type=int, default=0)
    w.add_argument("--plot", action="store_true", help="open the finplot candles+wave chart")
    w.add_argument("--plot-bars", type=int, default=3000,
                   help="bars to draw; a 15-bar cycle is invisible across 60,000 bars")
    w.set_defaults(func=cmd_wave)

    return p


def main(argv: list[str] | None = None) -> int:
    ensure_artifact_dirs()
    parser = build_parser()
    args = parser.parse_args(argv)
    return int(args.func(args))


if __name__ == "__main__":
    sys.exit(main())
