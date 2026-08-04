"""Cross-asset relationships: does anything outside crypto lead crypto?

The scan is deliberately built so that a non-tradeable answer cannot be mistaken for a
tradeable one. Every predictor is a trailing window of an external series that is fully
knowable at the decision bar, and every target is a forward window of the crypto series
that starts at that bar. Contemporaneous overlap is measured separately and labelled, so a
strong same-bar co-movement (which is what a naive correlation matrix mostly shows) can
never be read as a signal.

Multiplicity is not optional here. Roughly 30 external series times 4 predictor windows
times 3 forecast horizons is about 360 tests; at a nominal five percent level pure noise
delivers around 18 "findings".
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from llm2.data.macro import build_external_panel
from llm2.diagnostics.stats import Effect, apply_fdr, circular_shift_null_corr, safe_corr

DEFAULT_WINDOWS = (1, 6, 24, 96)
DEFAULT_HORIZONS = (1, 6, 24)


def _log_returns(level: pd.Series, window: int) -> pd.Series:
    # A few warehouse series go non-positive (the 10y-2y spread inverts; WTI printed
    # negative in April 2020). Those observations have no log return, so they become NaN
    # rather than a silent invalid-value warning or a fabricated number.
    positive = level.where(level > 0)
    return np.log(positive).diff(window)


NORMALISATION_WINDOW = 24 * 90  # roughly a quarter of hourly bars


def predictor_from(
    level: pd.Series, window: int, *, stationary_level: bool, norm_window: int = NORMALISATION_WINDOW
) -> pd.Series:
    """Trailing predictor for one external series, knowable at the decision bar.

    A price becomes its log return over the window. A yield, volatility index, term spread,
    sentiment index or funding rate carries its information in the level, so differencing it
    would discard exactly the crowding or stress reading that makes it worth having. Those
    are instead expressed as a trailing z-score: the level relative to its own recent norm.

    The z-score matters for more than interpretation. Raw funding rate over seven years is
    so persistent that a unit-root test cannot reject, which makes a correlation against it
    statistically unreliable. "Funding is high relative to the last quarter" is both the
    more meaningful question and a well-behaved stationary one.
    """
    if not stationary_level:
        return _log_returns(level, window)

    smoothed = level.rolling(window, min_periods=max(1, window // 2)).mean()
    ref_mean = smoothed.rolling(norm_window, min_periods=norm_window // 4).mean()
    ref_std = smoothed.rolling(norm_window, min_periods=norm_window // 4).std()
    return (smoothed - ref_mean) / ref_std.replace(0, np.nan)


def _forward_log_return(close: pd.Series, horizon: int) -> pd.Series:
    log_c = np.log(close.replace(0, np.nan))
    return log_c.shift(-horizon) - log_c


def external_panel_for(
    ohlcv: pd.DataFrame, symbols: list[str], timeframe: str, *, max_age_hours: float | None = None
) -> pd.DataFrame:
    """Causally aligned external levels on the crypto decision index."""
    max_age = pd.Timedelta(hours=max_age_hours) if max_age_hours is not None else None
    return build_external_panel(
        pd.DatetimeIndex(ohlcv.index), symbols, timeframe, max_age=max_age, include_age=True
    )


def lead_lag_scan(
    ohlcv: pd.DataFrame,
    panel: pd.DataFrame,
    *,
    windows: tuple[int, ...] = DEFAULT_WINDOWS,
    horizons: tuple[int, ...] = DEFAULT_HORIZONS,
    method: str = "spearman",
    min_rows: int = 2000,
    level_columns: set[str] | None = None,
) -> list[Effect]:
    """Does a trailing external move predict the crypto move that follows it?

    ``method="spearman"`` by default: cross-asset relationships are frequently monotone but
    not linear, and rank correlation is not dominated by a handful of crisis days the way
    Pearson is.
    """
    from llm2.data.macro import stationary_level_columns

    levels = stationary_level_columns() if level_columns is None else level_columns
    close = ohlcv["close"]
    value_cols = [c for c in panel.columns if not c.endswith("__age_sec")]
    effects: list[Effect] = []

    forwards = {h: _forward_log_return(close, h) for h in horizons}

    for sym in value_cols:
        level = panel[sym]
        if level.notna().sum() < min_rows:
            continue
        for w in windows:
            ext_ret = predictor_from(level, w, stationary_level=sym in levels)
            if ext_ret.notna().sum() < min_rows:
                continue
            x = _rank_if_needed(ext_ret, method)
            for h, fwd in forwards.items():
                aligned = pd.DataFrame({"x": x, "y": _rank_if_needed(fwd, method)}).dropna()
                if len(aligned) < min_rows:
                    continue
                try:
                    eff = circular_shift_null_corr(aligned["x"].to_numpy(), aligned["y"].to_numpy())
                except ValueError:
                    # Too persistent for the circular null to be trustworthy. Record it as
                    # untested rather than dropping it silently or aborting the scan: an
                    # absent row would be indistinguishable from a tested null result.
                    eff = Effect(
                        name="",
                        statistic=float("nan"),
                        n=int(len(aligned)),
                        detail={"untested_reason": 1.0},
                    )
                eff.name = f"{sym}|trail{w}->fwd{h}"
                eff.detail.update({"window": float(w), "horizon": float(h)})
                effects.append(eff)

    return apply_fdr(effects)


def _rank_if_needed(series: pd.Series, method: str) -> pd.Series:
    if method != "spearman":
        return series
    return series.rank(pct=True)


def contemporaneous_scan(
    ohlcv: pd.DataFrame,
    panel: pd.DataFrame,
    *,
    windows: tuple[int, ...] = DEFAULT_WINDOWS,
    method: str = "spearman",
) -> list[Effect]:
    """Same-bar co-movement. Context only: this cannot be traded and is never a signal.

    Reported because it is the number people usually quote, and seeing it next to the
    lead-lag result is the clearest way to show that the two are unrelated in magnitude.
    """
    close = ohlcv["close"]
    value_cols = [c for c in panel.columns if not c.endswith("__age_sec")]
    effects: list[Effect] = []

    for sym in value_cols:
        for w in windows:
            crypto = _log_returns(close, w)
            ext = _log_returns(panel[sym], w)
            frame = pd.DataFrame({"a": crypto, "b": ext}).dropna()
            if len(frame) < 2000:
                continue
            effects.append(
                Effect(
                    name=f"{sym}|contemporaneous_w{w}_NOT_TRADEABLE",
                    statistic=safe_corr(frame["a"].to_numpy(), frame["b"].to_numpy(), method=method),
                    n=int(len(frame)),
                    detail={"window": float(w)},
                )
            )
    return effects


def regime_conditional_correlation(
    ohlcv: pd.DataFrame,
    panel: pd.DataFrame,
    *,
    symbols: tuple[str, ...] = ("SPX", "DXY", "VIX", "XAUUSD"),
    window: int = 24,
    horizon: int = 6,
    regime_col: str = "VIX",
) -> list[Effect]:
    """Does a cross-asset lead flip sign between calm and stressed regimes?

    A relationship that reverses across regimes averages to nothing unconditionally, which
    is one of the few ways real structure can survive an unconditional scan undetected.
    """
    close = ohlcv["close"]
    fwd = _forward_log_return(close, horizon)
    effects: list[Effect] = []

    if regime_col not in panel.columns:
        return effects
    regime_level = panel[regime_col]
    try:
        regime = pd.qcut(regime_level, 3, labels=["calm", "normal", "stressed"])
    except (ValueError, IndexError):
        return effects

    for sym in symbols:
        if sym not in panel.columns:
            continue
        ext_ret = _log_returns(panel[sym], window)
        frame = pd.DataFrame({"x": ext_ret, "y": fwd, "regime": regime}).dropna()
        for key, grp in frame.groupby("regime", observed=True):
            if len(grp) < 1500:
                continue
            eff = circular_shift_null_corr(grp["x"].to_numpy(), grp["y"].to_numpy())
            eff.name = f"{sym}|trail{window}->fwd{horizon}|{regime_col}={key}"
            eff.detail.update({"regime": str(key)})
            effects.append(eff)

    return apply_fdr(effects)


def transfer_entropy(
    source: np.ndarray,
    target: np.ndarray,
    *,
    n_bins: int = 4,
    n_surrogates: int = 200,
    seed: int = 0,
) -> Effect:
    """Directional, nonlinear information flow from ``source`` to ``target``.

    Transfer entropy asks how much knowing the source's past reduces uncertainty about the
    target's next value *beyond* what the target's own past already tells you. Unlike
    correlation it captures nonlinear and asymmetric dependence, which matters because a
    cross-asset lead may only operate in the tails.

    The estimate is biased upward in finite samples, so the reported statistic is the excess
    over a circular-shift null rather than the raw value.
    """
    src = np.asarray(source, dtype=float)
    tgt = np.asarray(target, dtype=float)
    mask = np.isfinite(src) & np.isfinite(tgt)
    src, tgt = src[mask], tgt[mask]
    n = src.size
    if n < 2000:
        return Effect(name="transfer_entropy", statistic=float("nan"), n=int(n))

    raw = _transfer_entropy_binned(src, tgt, n_bins)
    rng = np.random.default_rng(seed)
    shifts = rng.integers(n // 20, n - n // 20, size=n_surrogates)
    null = np.array([_transfer_entropy_binned(np.roll(src, int(s)), tgt, n_bins) for s in shifts])
    null = null[np.isfinite(null)]

    if null.size < 20 or not np.isfinite(raw):
        return Effect(name="transfer_entropy", statistic=float(raw), n=int(n))

    p = float((1.0 + np.sum(null >= raw)) / (1.0 + null.size))
    return Effect(
        name="transfer_entropy",
        statistic=float(raw - np.mean(null)),
        n=int(n),
        p_value=p,
        detail={"raw_nats": float(raw), "null_mean": float(np.mean(null))},
    )


def _transfer_entropy_binned(source: np.ndarray, target: np.ndarray, n_bins: int) -> float:
    """T(source -> target) with quantile binning and lag 1, computed from joint counts."""
    n = min(source.size, target.size)
    if n < 100:
        return float("nan")

    s_past = _quantile_bin(source[:-1], n_bins)
    t_past = _quantile_bin(target[:-1], n_bins)
    t_next = _quantile_bin(target[1:], n_bins)
    if s_past is None or t_past is None or t_next is None:
        return float("nan")

    # Joint counts over (t_next, t_past, s_past) as a dense 3-D histogram.
    flat = (t_next * n_bins + t_past) * n_bins + s_past
    counts = np.bincount(flat, minlength=n_bins**3).astype(float).reshape(n_bins, n_bins, n_bins)
    total = counts.sum()
    if total <= 0:
        return float("nan")

    p_ftp = counts / total  # p(next, past, source)
    p_tp = p_ftp.sum(axis=0)  # p(past, source)
    p_ft = p_ftp.sum(axis=2)  # p(next, past)
    p_t = p_ftp.sum(axis=(0, 2))  # p(past)

    with np.errstate(divide="ignore", invalid="ignore"):
        num = p_ftp / p_tp[None, :, :]
        den = (p_ft / p_t[None, :])[:, :, None]
        ratio = num / den
        term = p_ftp * np.log(ratio)
    return float(np.nansum(term[np.isfinite(term)]))


def _quantile_bin(x: np.ndarray, n_bins: int) -> np.ndarray | None:
    edges = np.quantile(x[np.isfinite(x)], np.linspace(0, 1, n_bins + 1)[1:-1])
    if np.unique(edges).size < edges.size:
        return None
    return np.clip(np.searchsorted(edges, x), 0, n_bins - 1).astype(np.int64)


def transfer_entropy_scan(
    ohlcv: pd.DataFrame,
    panel: pd.DataFrame,
    *,
    window: int = 6,
    horizon: int = 6,
    n_surrogates: int = 100,
    max_symbols: int | None = None,
) -> list[Effect]:
    """Transfer entropy from each external series to the crypto forward return."""
    close = ohlcv["close"]
    fwd = _forward_log_return(close, horizon)
    value_cols = [c for c in panel.columns if not c.endswith("__age_sec")]
    if max_symbols is not None:
        value_cols = value_cols[:max_symbols]

    effects: list[Effect] = []
    for sym in value_cols:
        ext_ret = _log_returns(panel[sym], window)
        frame = pd.DataFrame({"x": ext_ret, "y": fwd}).dropna()
        if len(frame) < 3000:
            continue
        eff = transfer_entropy(
            frame["x"].to_numpy(), frame["y"].to_numpy(), n_surrogates=n_surrogates, seed=abs(hash(sym)) % 9999
        )
        eff.name = f"{sym}|transfer_entropy_w{window}->fwd{horizon}"
        effects.append(eff)
    return apply_fdr(effects)


def correlation_stability(
    ohlcv: pd.DataFrame,
    panel: pd.DataFrame,
    *,
    symbols: tuple[str, ...] = ("SPX", "DXY", "XAUUSD", "VIX"),
    window: int = 24,
    roll: int = 24 * 90,
) -> pd.DataFrame:
    """Rolling contemporaneous correlation, to show how unstable these couplings are.

    Context for interpretation: a full-sample correlation that swings between strongly
    positive and strongly negative across sub-periods is not a stable relationship even if
    its average is significantly non-zero.
    """
    crypto = _log_returns(ohlcv["close"], window)
    out = {}
    for sym in symbols:
        if sym not in panel.columns:
            continue
        out[sym] = crypto.rolling(roll, min_periods=roll // 2).corr(_log_returns(panel[sym], window))
    return pd.DataFrame(out, index=ohlcv.index)
