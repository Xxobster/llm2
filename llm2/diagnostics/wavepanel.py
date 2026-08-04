"""Cross-series wave panel: does any external series' wave channel lead the traded symbol's?

Two admission tiers, and nothing else is allowed into the panel:

**Tier A — open.** Crypto closes, volume, funding, open interest where available, and the
exogenous macro series already vetted in :mod:`llm2.data.macro`. These are admitted by
*kind* rather than by name, because the warehouse's Tier A universe is large and growing.

**Tier B — closed list.** A small, named, justified set of *derived* series: RSI(14),
realised volatility, signed-volume imbalance, return-run length, ATR-normalised
displacement. Each carries a one-line justification in :data:`TIER_B_REGISTRY` for why it is
not a linear transform of price, and :func:`admit_series` refuses anything not on the list.

**Why linear price filters are excluded outright.** A simple moving average, an EMA, a MACD
line or a Bollinger midline is a linear filter of the same close price the wave itself is
built from. Admitting one into an "external" lead-lag panel would let a smoothed, lagged copy
of the traded symbol's own price stand in as if it were independent information — the
cleanest possible way to manufacture a spurious lead, and structurally the same failure mode
that ``phase_lead_scan`` in :mod:`llm2.diagnostics.wave` was built to catch for mismatched
filters. ``admit_series`` refuses these by name-pattern and by an explicit ``kind`` tag, not
merely by omission from the registry.

**Clustering happens on RAW returns, never on the wave.** Two near-duplicate series (two
vendors' dollar index, a perp and its underlying spot) correlate just as strongly in their
unfiltered returns as in any wave built from them, so redundancy is removed before the wave
is ever computed, at the representation that is easiest to reason about and cannot itself be
an artefact of the filter under test.

**Every lead is scanned on four channels** — level (the wave itself), amplitude,
phase-locking (``cos(phase)``, since raw phase is circular and does not correlate honestly),
and impulse (the wave's own one-bar derivative) — all refiltered at one *forced common
period* per :func:`llm2.diagnostics.wave.phase_lead_scan`'s rule, and every result carries
three controls: a self-lead (the reference symbol against itself at a different period, per
:func:`llm2.research_policy.require_estimator_self_control`), a raw-return benchmark, and a
circular-shift surrogate p-value. When the raw-return benchmark disagrees with the wave-based
lead by finding a comparably strong effect on its own, the raw-return reading is preferred:
it is the simpler, harder-to-fool measurement.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from llm2.diagnostics.stats import Effect, apply_fdr, circular_shift_max_lag_null
from llm2.diagnostics.wave import causal_wave
from llm2.diagnostics.wave_mining_guard import forbid_analytic_import
from llm2.research_policy import (
    EstimatorResult,
    prefer_raw_return_when_disagreement,
    require_estimator_self_control,
)

forbid_analytic_import(globals())


class RejectedSeriesError(RuntimeError):
    """A panel series is a linear price filter, or is not on the closed Tier B list."""


TIER_A_KINDS: frozenset[str] = frozenset({"close", "volume", "funding", "open_interest", "macro"})

# name -> (kind, justification). This is the entire closed Tier B list; nothing else is
# admitted under a Tier B kind.
TIER_B_REGISTRY: dict[str, tuple[str, str]] = {
    "rsi_14": (
        "oscillator",
        "a bounded momentum oscillator built from average up/down moves, not a linear "
        "filter of price and not expressible as one (it involves a ratio and a rescale)",
    ),
    "realised_vol": (
        "volatility",
        "a second-moment statistic (trailing standard deviation of returns), not a price "
        "level or any linear transform of one",
    ),
    "signed_volume_imbalance": (
        "orderflow",
        "sign(return) * volume: an order-flow statistic, not a function of price levels",
    ),
    "return_run_length": (
        "momentum",
        "count of consecutive same-sign returns: a nonlinear, path-dependent statistic",
    ),
    "atr_normalised_displacement": (
        "volatility",
        "price displacement scaled by Average True Range: the ATR denominator makes this a "
        "nonlinear function of the recent price path, not a linear filter of price itself",
    ),
}

_LINEAR_FILTER_MARKERS: tuple[str, ...] = ("sma", "ema", "macd", "bollinger", "bb_mid", "bbands_mid")


def admit_series(name: str, kind: str) -> None:
    """Refuse a linear price filter outright, and refuse anything off the closed lists.

    Checked in this order: name/kind pattern for a linear filter first (so a Tier B name
    that happens to collide with a filter marker is still rejected), then Tier A kind
    membership, then exact Tier B registry membership including a kind match.
    """
    lowered = name.lower()
    if kind == "linear_price_filter" or any(marker in lowered for marker in _LINEAR_FILTER_MARKERS):
        raise RejectedSeriesError(
            f"{name!r} looks like a linear price filter (SMA/EMA/MACD/Bollinger mid). These "
            "are excluded from the wave panel by design — see the wavepanel module docstring."
        )
    if kind in TIER_A_KINDS:
        return
    if name not in TIER_B_REGISTRY:
        raise RejectedSeriesError(
            f"{name!r} is not a Tier A kind ({sorted(TIER_A_KINDS)}) and is not in the closed "
            f"Tier B registry ({sorted(TIER_B_REGISTRY)}). Add it with a justification before "
            "admitting it."
        )
    registered_kind, _justification = TIER_B_REGISTRY[name]
    if registered_kind != kind:
        raise RejectedSeriesError(
            f"{name!r} is registered under kind {registered_kind!r}, not {kind!r}."
        )


# --------------------------------------------------------------------------------------
# Clustering on raw returns
# --------------------------------------------------------------------------------------


def cluster_by_raw_return_correlation(
    returns: pd.DataFrame, *, threshold: float = 0.9
) -> tuple[list[list[str]], dict[str, str]]:
    """Group series whose RAW returns correlate at |rho| >= threshold; keep one per group.

    The survivor of each cluster is the member with the most non-missing observations, ties
    broken alphabetically — deterministic and independent of column order, so re-running the
    scan with the panel built in a different order cannot change which name survives.
    """
    cols = list(returns.columns)
    n = len(cols)
    corr = returns.corr(min_periods=200).to_numpy() if n else np.zeros((0, 0))
    parent = list(range(n))

    def find(i: int) -> int:
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    def union(i: int, j: int) -> None:
        ri, rj = find(i), find(j)
        if ri != rj:
            parent[ri] = rj

    for i in range(n):
        for j in range(i + 1, n):
            rho = corr[i, j]
            if np.isfinite(rho) and abs(rho) >= threshold:
                union(i, j)

    groups: dict[int, list[str]] = {}
    for i, name in enumerate(cols):
        groups.setdefault(find(i), []).append(name)

    coverage = returns.notna().sum()
    clusters: list[list[str]] = []
    representative: dict[str, str] = {}
    for members in groups.values():
        ordered = sorted(members, key=lambda m: (-int(coverage[m]), m))
        clusters.append(ordered)
        for m in ordered:
            representative[m] = ordered[0]
    return clusters, representative


# --------------------------------------------------------------------------------------
# Wave channels and the ordered-pair lead scan
# --------------------------------------------------------------------------------------

CHANNELS: tuple[str, ...] = ("level", "amplitude", "phase_locking", "impulse")
SELF_LEAD_PERIOD_RATIO = 1.6  # a different-enough period to expose pure filter artefact
MIN_PAIR_ROWS = 1000


def _channel_series(
    close: pd.Series, period: float, channel: str, *, log_price: bool = True
) -> pd.Series:
    """Wave-decompose a series. Price-like levels are logged; already-stationary levels are not."""
    x = pd.to_numeric(close, errors="coerce")
    if log_price:
        x = np.log(x.where(x > 0))
    x = x.interpolate(limit_direction="both")
    wave, amp, phase = causal_wave(x, period)
    if channel == "level":
        return wave
    if channel == "amplitude":
        return amp
    if channel == "phase_locking":
        return np.cos(phase)
    if channel == "impulse":
        return wave.diff()
    raise ValueError(f"unknown channel {channel!r}")


def ordered_pair_lead_scan(
    reference_close: pd.Series,
    reference_symbol: str,
    external_closes: dict[str, pd.Series],
    *,
    period: float,
    channels: tuple[str, ...] = CHANNELS,
    max_lag_bars: int = 48,
    log_price_flags: dict[str, bool] | None = None,
    external_returns: dict[str, pd.Series] | None = None,
) -> list[Effect]:
    """Ordered-pair lead scan at a forced common period, on four wave channels.

    Significance uses :func:`circular_shift_max_lag_null` so the lag search is paid for.
    Contemporaneous co-movement (lag-0 stronger than any positive lag) is reported but
    marked ``leads_beyond_contemporaneous=0`` and is not a lead claim. When the wave channel
    and the raw-return benchmark disagree, ``prefer_raw_return_when_disagreement`` decides.

    ``log_price_flags`` defaults to True (log then wave). Set False for already-stationary
    levels such as funding rate, VIX, RSI. ``external_returns`` supplies the raw-return
    benchmark when the series is not a price (e.g. funding level itself, or RSI diff).
    """
    effects: list[Effect] = []
    flags = log_price_flags or {}
    ret_overrides = external_returns or {}
    ref_returns = np.log(reference_close.replace(0, np.nan)).diff()
    self_period = period * SELF_LEAD_PERIOD_RATIO

    for channel in channels:
        ref_chan = _channel_series(reference_close, period, channel, log_price=True).dropna()
        self_chan = _channel_series(
            reference_close, self_period, channel, log_price=True
        ).dropna()

        for sym, close in external_closes.items():
            if sym == reference_symbol:
                continue
            use_log = flags.get(sym, True)
            ext_chan = _channel_series(close, period, channel, log_price=use_log).dropna()
            joined = pd.DataFrame({"ref": ref_chan, "ext": ext_chan}).dropna()
            if len(joined) < MIN_PAIR_ROWS:
                continue

            try:
                lead_eff = circular_shift_max_lag_null(
                    joined["ref"].to_numpy(),
                    joined["ext"].to_numpy(),
                    max_lag=max_lag_bars,
                    n_null=200,
                    seed=(hash((sym, channel)) % (2**31)),
                )
                best_corr = float(lead_eff.statistic)
                best_lag = int(lead_eff.detail.get("lag_bars", 0))
                corr0 = float(lead_eff.detail.get("corr_lag0", float("nan")))
                leads = bool(lead_eff.detail.get("leads_beyond_contemporaneous", 0.0))
                p_value = lead_eff.p_value
            except ValueError:
                best_corr, best_lag, corr0, leads, p_value = (
                    float("nan"),
                    0,
                    float("nan"),
                    False,
                    float("nan"),
                )

            self_joined = pd.DataFrame({"ref": ref_chan, "ext": self_chan}).dropna()
            self_corr = float("nan")
            if len(self_joined) >= MIN_PAIR_ROWS:
                try:
                    self_eff = circular_shift_max_lag_null(
                        self_joined["ref"].to_numpy(),
                        self_joined["ext"].to_numpy(),
                        max_lag=max_lag_bars,
                        n_null=150,
                        seed=1,
                    )
                    self_corr = float(self_eff.statistic)
                except ValueError:
                    self_corr = float("nan")

            if sym in ret_overrides:
                ext_returns = ret_overrides[sym]
            elif use_log:
                ext_returns = np.log(close.replace(0, np.nan)).diff()
            else:
                ext_returns = close.diff()
            raw_joined = pd.DataFrame({"ref": ref_returns, "ext": ext_returns}).dropna()
            raw_corr, raw_lag, raw_p = float("nan"), 0, float("nan")
            if len(raw_joined) >= MIN_PAIR_ROWS:
                try:
                    raw_eff = circular_shift_max_lag_null(
                        raw_joined["ref"].to_numpy(),
                        raw_joined["ext"].to_numpy(),
                        max_lag=max_lag_bars,
                        n_null=200,
                        seed=(hash((sym, "raw")) % (2**31)),
                    )
                    raw_corr = float(raw_eff.statistic)
                    raw_lag = int(raw_eff.detail.get("lag_bars", 0))
                    raw_p = float(raw_eff.p_value)
                except ValueError:
                    pass

            self_control_passed = True
            try:
                require_estimator_self_control(
                    EstimatorResult(
                        name=f"wavepanel_lead|{channel}|{sym}->{reference_symbol}",
                        statistic=float(best_corr) if np.isfinite(best_corr) else 0.0,
                        self_control_statistic=float(self_corr) if np.isfinite(self_corr) else None,
                        self_control_description=(
                            f"{reference_symbol} at period {period:.1f} vs {self_period:.1f}, "
                            f"channel={channel}"
                        )
                        if np.isfinite(self_corr)
                        else "",
                    )
                )
            except Exception:
                self_control_passed = False

            wave_sig = bool(np.isfinite(p_value) and p_value <= 0.05 and leads)
            raw_sig = bool(np.isfinite(raw_p) and raw_p <= 0.05)
            verdict = prefer_raw_return_when_disagreement(
                wave_statistic=best_corr if np.isfinite(best_corr) else 0.0,
                raw_return_statistic=raw_corr if np.isfinite(raw_corr) else 0.0,
                wave_significant=wave_sig,
                raw_significant=raw_sig,
                name=f"{channel}|{sym}",
            )

            effects.append(
                Effect(
                    name=f"wavepanel_lead|{channel}|{sym}->{reference_symbol}",
                    statistic=float(best_corr) if np.isfinite(best_corr) else float("nan"),
                    n=int(len(joined)),
                    # Non-leads (lag-0 dominant) keep the p-value for diagnostics but are
                    # not eligible as lead claims; FDR still sees them.
                    p_value=p_value if leads else max(p_value if np.isfinite(p_value) else 1.0, 0.99),
                    detail={
                        "lag_bars": float(best_lag),
                        "corr_lag0": corr0,
                        "leads_beyond_contemporaneous": float(leads),
                        "channel": channel,
                        "self_control_statistic": float(self_corr) if np.isfinite(self_corr) else float("nan"),
                        "self_control_passed": float(self_control_passed),
                        "raw_return_corr": float(raw_corr) if np.isfinite(raw_corr) else float("nan"),
                        "raw_return_lag": float(raw_lag),
                        "raw_return_p": float(raw_p) if np.isfinite(raw_p) else float("nan"),
                        # verdict codes: 0=wave-only discarded, 1=both, 2=raw only, 3=neither, 4=wave only
                        "verdict_code": {
                            "raw_preferred_wave_discarded": 0.0,
                            "raw_and_wave": 1.0,
                            "raw_only": 2.0,
                            "neither": 3.0,
                            "wave": 4.0,
                        }.get(verdict, 3.0),
                        "prefer_raw_return_reading": float(
                            verdict in ("raw_preferred_wave_discarded", "raw_and_wave", "raw_only")
                        ),
                        "common_period_bars": float(period),
                        "null_max_over_lags": 1.0,
                    },
                )
            )
    return apply_fdr(effects)


def run_wave_panel_scan(
    close_panel: dict[str, pd.Series],
    return_panel: pd.DataFrame,
    reference_symbol: str,
    admitted_kinds: dict[str, str],
    *,
    period: float,
    cluster_threshold: float = 0.9,
    max_lag_bars: int = 48,
    log_price_flags: dict[str, bool] | None = None,
) -> tuple[list[Effect], list[list[str]]]:
    """Admit, cluster, then ordered-pair-lead-scan a panel against ``reference_symbol``.

    ``close_panel`` supplies levels for wave construction; ``return_panel`` must hold the
    corresponding RAW, already-stationary series (log-returns for prices, the plain level
    or first difference for funding / oscillators) used for clustering. Both must share
    ``admitted_kinds``' keys.
    """
    for name, kind in admitted_kinds.items():
        admit_series(name, kind)

    clusters, representative = cluster_by_raw_return_correlation(return_panel, threshold=cluster_threshold)
    reps = sorted(set(representative.values()))
    external = {
        name: close_panel[name] for name in reps if name != reference_symbol and name in close_panel
    }
    ext_returns = {
        name: return_panel[name]
        for name in external
        if name in return_panel.columns
    }

    effects = ordered_pair_lead_scan(
        close_panel[reference_symbol],
        reference_symbol,
        external,
        period=period,
        max_lag_bars=max_lag_bars,
        log_price_flags=log_price_flags,
        external_returns=ext_returns,
    )
    return effects, clusters
