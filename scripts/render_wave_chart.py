"""Render the candles + market-strength-wave chart to a PNG (and optionally open it).

Usage:
    python scripts/render_wave_chart.py --symbol BTCUSDT --timeframe 1h --bars 1500
    python scripts/render_wave_chart.py --show          # interactive window instead
"""

from __future__ import annotations

import argparse
from pathlib import Path

from llm2.data.loader import load_ohlcv
from llm2.diagnostics.wave import fit_wave
from llm2.diagnostics.waveplot import plot_wave
from llm2.paths import ARTIFACTS


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--symbol", default="BTCUSDT")
    ap.add_argument("--timeframe", default="1h")
    # ~25 cycles of a 15-bar rhythm. More than that and the wave is a solid band of ink.
    ap.add_argument("--bars", type=int, default=420)
    ap.add_argument("--show", action="store_true", help="open the interactive window")
    ap.add_argument("--out", default="")
    args = ap.parse_args()

    ohlcv = load_ohlcv(args.symbol, args.timeframe).tail(args.bars)
    # The period is fitted on the full history, not on the display window: a 1,500-bar
    # slice is too short to resolve a spectrum, and refitting per window would make the
    # wave depend on how much of the chart you happen to be looking at.
    full = load_ohlcv(args.symbol, args.timeframe)
    full_fit = fit_wave(full["close"], symbol=args.symbol, timeframe=args.timeframe)
    fit = fit_wave(
        ohlcv["close"],
        symbol=args.symbol,
        timeframe=args.timeframe,
        period=full_fit.period_bars,
        n_surrogates=50,
    )
    fit.peak_ratio, fit.p_value = full_fit.peak_ratio, full_fit.p_value
    print(full_fit.summary())

    out = Path(args.out) if args.out else (
        ARTIFACTS / "reports" / "diagnostics" / f"wave_{args.symbol}_{args.timeframe}.png"
    )
    out.parent.mkdir(parents=True, exist_ok=True)

    view = plot_wave(
        ohlcv, fit, symbol=args.symbol, timeframe=args.timeframe, show=False,
        show_metrics_window=False,
    )
    fplt = view.fplt

    if args.show:
        fplt.show()
        return 0

    # Screenshot needs one event-loop turn for the scene to lay out before capture.
    def _shoot():
        with open(out, "wb") as fh:
            fplt.screenshot(fh, fmt="png")
        print(f"wrote {out}")
        fplt.close()

    fplt.timer_callback(_shoot, 1.0, single_shot=True)
    fplt.show()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
