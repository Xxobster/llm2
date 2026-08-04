"""Candles with the market-strength wave drawn over them.

Rendered through ``tradesim.research.plot.plot_backtest`` rather than a private finplot
call, because that is the shared plotting path and it already carries the dark theme, the
time inspector and the metrics window. It has no candles-only mode, so a trade-free
``SimResult`` is passed and the equity pane sits flat at the top; the wave lives on the
price pane and in two extra panes below it.

What is on the chart:

- **price pane** — candles, the non-causal wave, and the causal wave, offset back onto the
  price scale so the shape is readable against the bars.
- **pane 2** — amplitude of both waves. This is the "strength" reading: a large amplitude
  means the rhythm is currently pronounced, a small one means it has faded.
- **pane 3** — causal phase, wrapped to [-pi, pi]. Rising through zero is the cycle low.

The two waves are drawn together on purpose. The non-causal one turns exactly at the highs
and lows, which is what makes cycle analysis look compelling in a screenshot; the causal one
is the same cycle computed without seeing the future, and the visible gap between them is
the honest measure of how much of that appeal is hindsight.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from llm2.diagnostics.wave import WaveFit, fit_wave

# finplot draws in the price units of the pane it is given, so a wave centred on zero has
# to be lifted onto the price scale. The amplitude is deliberately modest: a wave scaled to
# fill the pane hides the candles it is supposed to be explaining.
WAVE_DISPLAY_FRACTION = 0.18

# A 15-bar cycle across 1,500 bars is a hundred cycles of solid ink. Roughly 25 cycles is
# the most that stays legible, which is what the default bar count in the render script
# targets.
BASELINE_PERIODS = 4.0


def _to_price_scale(
    wave: pd.Series, close: pd.Series, fraction: float, period: float
) -> pd.Series:
    """Centre a zero-mean wave on a slow trend and scale it into price units.

    The baseline is a moving average several cycles long, so the drawn line oscillates
    *around* the trend rather than tracking price. A fast baseline would make the wave sit
    on top of the candles and look far more informative than it is.
    """
    w = wave.reindex(close.index)
    scale = float(np.nanstd(w.to_numpy()))
    if not np.isfinite(scale) or scale <= 0:
        return w
    price_span = float(np.nanpercentile(close, 95) - np.nanpercentile(close, 5))
    win = max(2, int(round(period * BASELINE_PERIODS)))
    baseline = close.rolling(win, min_periods=1).mean()
    return baseline + (w / scale) * price_span * fraction * 0.5


def plot_wave(
    ohlcv: pd.DataFrame,
    fit: WaveFit | None = None,
    *,
    symbol: str = "BTCUSDT",
    timeframe: str = "1h",
    max_bars: int = 0,
    show: bool = True,
    show_metrics_window: bool = False,
):
    """Open the candle chart with the wave overlaid.

    ``max_bars`` clips to the most recent N bars; 0 shows the full period. A 15-bar cycle
    across 60,000 hourly bars is invisible at full zoom, so a few thousand bars is usually
    the readable choice for inspecting the wave itself.
    """
    from tradesim.ensure_source import prefer_botsgeneral_tradesim

    prefer_botsgeneral_tradesim()
    import tradesim
    from tradesim import SimResult
    from tradesim.research.plot import plot_backtest

    if "botsgeneral" not in tradesim.__file__:
        raise RuntimeError(f"tradesim is not the botsgeneral copy: {tradesim.__file__}")

    from llm2.backtest.run import ohlcv_to_bar_series

    df = ohlcv.sort_index()
    if max_bars and max_bars > 0:
        df = df.tail(max_bars)
    if fit is None:
        fit = fit_wave(df["close"], symbol=symbol, timeframe=timeframe)

    close = pd.to_numeric(df["close"], errors="coerce")
    p = fit.period_bars
    analytic = _to_price_scale(fit.analytic_wave, close, WAVE_DISPLAY_FRACTION, p)
    causal = _to_price_scale(fit.causal_wave, close, WAVE_DISPLAY_FRACTION, p)
    amp_a = fit.analytic_amplitude.reindex(close.index)
    amp_c = fit.causal_amplitude.reindex(close.index)
    phase_c = fit.causal_phase.reindex(close.index)

    # Both filters ring for a few cycles at the start. That transient is an artefact of
    # switching the filter on, and left in it dwarfs the real amplitude and rescales the
    # whole pane around a number that means nothing.
    warm = int(round(p * 6))
    for s in (analytic, causal, amp_a, amp_c, phase_c):
        s.iloc[:warm] = np.nan

    bars = ohlcv_to_bar_series(df, symbol=symbol, timeframe=timeframe)
    # No trades: this is a diagnostic chart, not a backtest. ``plot_backtest`` has no
    # candles-only mode, so an empty result gives an inert equity pane at the top and the
    # price pane carries everything that matters.
    empty_eq = pd.DataFrame({"ts_ms": pd.Series(dtype="int64"), "equity": pd.Series(dtype=float)})
    empty = SimResult(
        run_id="wave-diagnostic",
        trades=(),
        fills=(),
        funding_charges=(),
        skips=(),
        skip_counts={},
        equity=empty_eq,
        daily_equity=empty_eq,
        liquidation_status="none",
        starting_equity=0.0,
        ending_equity=0.0,
        config_digest="wave-diagnostic",
        meta={"kind": "diagnostic_wave_overlay", "not_a_backtest": True},
    )

    def draw(view):
        fplt = view.fplt
        idx = close.index
        fplt.plot(idx, analytic.to_numpy(), ax=view.ax_price, color="#00d4ff", width=1,
                  legend=f"wave {fit.period_bars:.1f}b (NON-CAUSAL, display only)")
        fplt.plot(idx, causal.to_numpy(), ax=view.ax_price, color="#ff9f1c", width=1,
                  legend="wave (causal, tradeable form)")

        fplt.plot(idx, amp_a.to_numpy(), ax=view.extra_axes[0], color="#00d4ff",
                  legend="amplitude (non-causal)")
        fplt.plot(idx, amp_c.to_numpy(), ax=view.extra_axes[0], color="#ff9f1c",
                  legend="amplitude (causal) = market strength")

        fplt.plot(idx, phase_c.to_numpy(), ax=view.extra_axes[1], color="#ff9f1c",
                  legend="causal phase (rising through 0 = cycle low)")
        fplt.add_line((idx[0], 0.0), (idx[-1], 0.0), ax=view.extra_axes[1],
                      color="#666666", style="--")

    title = (
        f"{symbol} {timeframe} — market strength wave | period {fit.period_bars:.1f} bars, "
        f"peak {fit.peak_ratio:.2f}x AR(1) null, p={fit.p_value:.4f} | "
        f"causal vs non-causal corr {fit.corr_causal_vs_analytic:.2f}, "
        f"lag {fit.phase_lag_bars:.0f} bars"
    )
    return plot_backtest(
        bars,
        empty,
        title=title,
        max_bars=0,
        show=show,
        show_metrics_window=show_metrics_window,
        extra_rows=2,
        extra_row_heights=[0.35, 0.25],
        on_axes=draw,
    )
