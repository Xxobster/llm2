"""A–B / B–C distance-factor similarity on confirmed swing triples.

Your theory, stated as a test: take three consecutive confirmed swings A → B → C, measure
the absolute price distances ``|B−A|`` and ``|C−B|``, form the factor ``f = |BC| / |AB|``,
and ask whether historically similar factor values share the same forward price behaviour.

**Why confirmed swings, not the pretty wave.** The causal market-strength wave lags; its
extrema are filter artefacts as often as market turns. Confirmed warehouse swings already
separate ``pivot_ts_ms`` from ``confirm_ts_ms`` and pass the confirmation-time audit. The
factor is knowable only when C is confirmed — never at B.

Two complementary arms run under one false-discovery correction:

1. **Bucket arm.** Registered factor bins (classical ratios + placebos). Conditional mean
   forward return in each bin, Newey-West, vs unconditional baseline.
2. **Similarity arm.** For each completed triple, find the ``k`` nearest historical
   factors from the *training* pool only; predict the neighbours' mean forward return;
   report correlation of prediction vs realisation.

A placebo shuffles factors across events (same dates, wrong factors). If shuffled factors
predict as well, the ratio is decoration.

A second, separately labelled arm repeats the same factor scan on **causal-wave extrema**
(peaks/troughs of ``causal_wave``, confirmed one bar after the turn). That arm is
descriptive of the orange wave; it does not replace warehouse legs for tradeable claims.

Nothing here selects a strategy. Readiness stays RESEARCH_ONLY.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd

from llm2.data.indicators import INDICATORS_DB, SWING_LEFT, SWING_RIGHT, _default_source
from llm2.diagnostics.stats import Effect, apply_fdr, newey_west_tstat, normal_two_sided_p, safe_corr
from llm2.diagnostics.structure import forward_log_return
from llm2.diagnostics.wave import causal_wave, fit_period_in_window
from llm2.research_policy import LevelClaim, require_placebo_arm, require_warehouse_legs_for_abc

# Classical ratio claims + deliberately unremarkable placebos (D-017 pattern).
CLASSICAL_FACTORS = (0.500, 0.618, 0.786, 1.000, 1.272, 1.618)
PLACEBO_FACTORS = (0.350, 0.450, 0.720, 0.900, 1.150, 1.400)
FACTOR_TOL = 0.05  # |f - target| <= tol counts as "similar" to a named ratio
MIN_EVENTS = 40
K_NEIGHBOURS = (10, 50)
HORIZONS = (6, 24, 96)


@dataclass(frozen=True)
class AbcTriple:
    """One completed A→B→C swing triple, knowable at ``confirm_ts_ms`` of C."""

    confirm_ts_ms: int
    a_price: float
    b_price: float
    c_price: float
    ab_abs: float
    bc_abs: float
    factor: float  # bc / ab
    ca_factor: float  # |C−A| / |B−A| — classical "C vs A" when meaningful
    ab_dir: int  # +1 up, -1 down
    bc_dir: int
    pattern: str  # e.g. "up_down", "down_up"


def load_legs(
    symbol: str,
    timeframe: str,
    *,
    source: str | None = None,
) -> pd.DataFrame:
    """Confirmed swing legs from the warehouse, chronological by end (confirmation) time."""
    import sqlite3

    require_warehouse_legs_for_abc("indicators.legs")
    if not INDICATORS_DB.is_file():
        raise FileNotFoundError(f"Indicator warehouse missing: {INDICATORS_DB}")
    src = source or _default_source(symbol)
    conn = sqlite3.connect(f"file:{INDICATORS_DB}?mode=ro", uri=True, timeout=120.0)
    try:
        conn.execute("PRAGMA busy_timeout=120000")
        df = pd.read_sql(
            "SELECT * FROM legs WHERE symbol = ? AND timeframe = ? AND source = ? "
            "AND swing_left = ? AND swing_right = ? ORDER BY end_ts_ms, leg_id",
            conn,
            params=(symbol.upper(), timeframe, src, SWING_LEFT, SWING_RIGHT),
        )
    finally:
        conn.close()
    if df.empty:
        raise ValueError(f"No legs for {symbol} {timeframe} source={src}")
    return df


def causal_wave_extrema(
    close: pd.Series,
    *,
    period: float | None = None,
    min_sep: int | None = None,
) -> pd.DataFrame:
    """Peaks and troughs of the causal wave, confirmed one bar after the turn.

    An extremum at bar ``i`` is knowable only at bar ``i+1`` (needs the next sample to see
    the turn). Rows are stamped with ``confirm_time`` = index[i+1] and ``price`` = close[i]
    (price at the extremum bar, not the confirmation bar).
    """
    c = pd.to_numeric(close, errors="coerce")
    log_c = np.log(c.where(c > 0))
    ret = log_c.diff().dropna().to_numpy()
    if period is None:
        period, _, _ = fit_period_in_window(ret, n_surrogates=80, seed=0)
    if not np.isfinite(period) or period <= 2:
        return pd.DataFrame()
    wave, _, _ = causal_wave(log_c, float(period))
    w = wave.to_numpy(dtype=float)
    sep = int(min_sep if min_sep is not None else max(2, round(period / 4)))
    # Turn confirmed at i (>=2): extremum at i-1.
    left = w[1:-1]
    prev = w[:-2]
    nxt = w[2:]
    is_peak = np.isfinite(left) & np.isfinite(prev) & np.isfinite(nxt) & (left > prev) & (left > nxt)
    is_trough = np.isfinite(left) & np.isfinite(prev) & np.isfinite(nxt) & (left < prev) & (left < nxt)
    # indices in full series for extremum bar
    ext_i = np.flatnonzero(is_peak | is_trough) + 1
    kinds = np.where(is_peak[ext_i - 1], "peak", "trough")
    # Enforce min separation and alternation
    kept_i: list[int] = []
    kept_k: list[str] = []
    last_i, last_k = -10**9, ""
    for i, k in zip(ext_i.tolist(), kinds.tolist(), strict=True):
        if i - last_i < sep:
            continue
        if k == last_k:
            # replace prior extremum if this one is more extreme
            if not kept_i:
                continue
            pi = kept_i[-1]
            if k == "peak" and w[i] >= w[pi]:
                kept_i[-1], kept_k[-1] = i, k
                last_i, last_k = i, k
            elif k == "trough" and w[i] <= w[pi]:
                kept_i[-1], kept_k[-1] = i, k
                last_i, last_k = i, k
            continue
        kept_i.append(i)
        kept_k.append(k)
        last_i, last_k = i, k

    if len(kept_i) < 3:
        return pd.DataFrame()
    idx = close.index
    prices = c.to_numpy(dtype=float)
    rows = []
    for i, k in zip(kept_i, kept_k, strict=True):
        confirm_i = i + 1
        if confirm_i >= len(idx):
            continue
        rows.append(
            {
                "extremum_i": i,
                "confirm_i": confirm_i,
                "kind": k,
                "price": float(prices[i]),
                "confirm_time": idx[confirm_i],
                "confirm_ts_ms": int(idx[confirm_i].timestamp() * 1000),
            }
        )
    return pd.DataFrame(rows)


def build_abc_triples_from_extrema(extrema: pd.DataFrame) -> pd.DataFrame:
    """A→B→C from consecutive alternating causal-wave extrema."""
    if len(extrema) < 3:
        return pd.DataFrame()
    a = extrema.iloc[:-2].reset_index(drop=True)
    b = extrema.iloc[1:-1].reset_index(drop=True)
    c = extrema.iloc[2:].reset_index(drop=True)
    # Require alternation A≠B≠C kinds
    ok = (a["kind"].to_numpy() != b["kind"].to_numpy()) & (
        b["kind"].to_numpy() != c["kind"].to_numpy()
    )
    a, b, c = a.loc[ok], b.loc[ok], c.loc[ok]
    a_price = a["price"].to_numpy(dtype=float)
    b_price = b["price"].to_numpy(dtype=float)
    c_price = c["price"].to_numpy(dtype=float)
    ab_abs = np.abs(b_price - a_price)
    bc_abs = np.abs(c_price - b_price)
    with np.errstate(divide="ignore", invalid="ignore"):
        factor = np.where(ab_abs > 0, bc_abs / ab_abs, np.nan)
        ca_factor = np.where(ab_abs > 0, np.abs(c_price - a_price) / ab_abs, np.nan)
    ab_dir = np.where(b_price > a_price, 1, -1)
    bc_dir = np.where(c_price > b_price, 1, -1)
    pattern = np.where(
        (ab_dir > 0) & (bc_dir < 0),
        "up_down",
        np.where((ab_dir < 0) & (bc_dir > 0), "down_up", "same_dir"),
    )
    out = pd.DataFrame(
        {
            "confirm_ts_ms": c["confirm_ts_ms"].to_numpy(),
            "confirm_time": c["confirm_time"].to_numpy(),
            "a_price": a_price,
            "b_price": b_price,
            "c_price": c_price,
            "ab_abs": ab_abs,
            "bc_abs": bc_abs,
            "factor": factor,
            "ca_factor": ca_factor,
            "ab_dir": ab_dir,
            "bc_dir": bc_dir,
            "pattern": pattern,
            "ab_kind": "wave",
            "bc_kind": "wave",
            "ab_len_pct": ab_abs / np.maximum(a_price, 1e-12),
            "bc_len_pct": bc_abs / np.maximum(b_price, 1e-12),
            "geometry": "causal_wave_extrema",
        }
    )
    out = out[np.isfinite(out["factor"]) & (out["ab_abs"] > 0) & (out["pattern"] != "same_dir")]
    return out.reset_index(drop=True)


def build_abc_triples(legs: pd.DataFrame) -> pd.DataFrame:
    """Consecutive legs share endpoint B: leg_i is A→B, leg_{i+1} is B→C.

    The factor is knowable at ``end_ts_ms`` of the second leg (confirmation of C).
    """
    if len(legs) < 2:
        return pd.DataFrame()

    a_end = legs["end_swing_id"].to_numpy()
    b_start = legs["start_swing_id"].to_numpy()
    # Vectorised join: leg i pairs with leg i+1 when end of i == start of i+1.
    match = a_end[:-1] == b_start[1:]
    i0 = np.flatnonzero(match)
    i1 = i0 + 1

    a_price = legs["start_price"].to_numpy(dtype=float)[i0]
    b_price = legs["end_price"].to_numpy(dtype=float)[i0]
    c_price = legs["end_price"].to_numpy(dtype=float)[i1]
    ab_abs = np.abs(b_price - a_price)
    bc_abs = np.abs(c_price - b_price)
    ca_abs = np.abs(c_price - a_price)
    with np.errstate(divide="ignore", invalid="ignore"):
        factor = np.where(ab_abs > 0, bc_abs / ab_abs, np.nan)
        ca_factor = np.where(ab_abs > 0, ca_abs / ab_abs, np.nan)

    ab_dir = np.where(b_price > a_price, 1, -1)
    bc_dir = np.where(c_price > b_price, 1, -1)
    pattern = np.where(
        (ab_dir > 0) & (bc_dir < 0),
        "up_down",
        np.where((ab_dir < 0) & (bc_dir > 0), "down_up", "same_dir"),
    )

    out = pd.DataFrame(
        {
            "confirm_ts_ms": legs["end_ts_ms"].to_numpy()[i1],
            "a_price": a_price,
            "b_price": b_price,
            "c_price": c_price,
            "ab_abs": ab_abs,
            "bc_abs": bc_abs,
            "factor": factor,
            "ca_factor": ca_factor,
            "ab_dir": ab_dir,
            "bc_dir": bc_dir,
            "pattern": pattern,
            "ab_kind": legs["kind"].to_numpy()[i0],
            "bc_kind": legs["kind"].to_numpy()[i1],
            "ab_len_pct": legs["length_pct"].to_numpy(dtype=float)[i0],
            "bc_len_pct": legs["length_pct"].to_numpy(dtype=float)[i1],
        }
    )
    out = out[np.isfinite(out["factor"]) & (out["ab_abs"] > 0) & (out["pattern"] != "same_dir")]
    out["confirm_time"] = pd.to_datetime(out["confirm_ts_ms"], unit="ms", utc=True)
    return out.reset_index(drop=True)


def _align_forward(
    triples: pd.DataFrame, close: pd.Series, horizon: int
) -> tuple[np.ndarray, np.ndarray]:
    """Forward log return from the bar on which C is confirmed."""
    fwd = forward_log_return(close, horizon)
    # Map confirm time → nearest bar at or before confirm (bar open convention).
    conf = triples["confirm_time"]
    # reindex with asof: for each confirm, take last close bar <= confirm
    close_idx = close.index.sort_values()
    pos = close_idx.searchsorted(conf, side="right") - 1
    valid = pos >= 0
    pos = np.clip(pos, 0, len(close_idx) - 1)
    times = close_idx[pos]
    values = fwd.reindex(times).to_numpy(dtype=float)
    factors = triples["factor"].to_numpy(dtype=float)
    # Invalidate rows whose mapped bar is after confirm (should not happen) or NaN fwd
    ok = valid & np.isfinite(values) & np.isfinite(factors)
    # Also require the mapped timestamp is not after confirm
    ok &= times <= conf.to_numpy()
    return factors[ok], values[ok]


def _bucket_effects(
    factors: np.ndarray,
    fwd: np.ndarray,
    *,
    targets: tuple[float, ...],
    label: str,
    horizon: int,
    pattern_mask: np.ndarray | None = None,
) -> list[Effect]:
    baseline = float(np.nanmean(fwd))
    effects: list[Effect] = []
    f = factors if pattern_mask is None else factors[pattern_mask]
    y = fwd if pattern_mask is None else fwd[pattern_mask]
    for target in targets:
        near = np.abs(f - target) <= FACTOR_TOL
        if near.sum() < MIN_EVENTS:
            continue
        excess = y[near] - baseline
        mean_ex, t_stat = newey_west_tstat(excess, lags=horizon)
        effects.append(
            Effect(
                name=f"abc_factor|{label}|{target:.3f}|fwd{horizon}",
                statistic=float(mean_ex),
                n=int(near.sum()),
                p_value=normal_two_sided_p(t_stat),
                detail={
                    "t_hac": float(t_stat),
                    "excess_bps": float(mean_ex * 1e4),
                    "raw_mean_bps": float(np.nanmean(y[near]) * 1e4),
                    "uncond_mean_bps": float(baseline * 1e4),
                    "target_factor": float(target),
                    "mean_factor": float(np.nanmean(f[near])),
                    "horizon": float(horizon),
                },
            )
        )
    return effects


def _similarity_effect(
    factors: np.ndarray,
    fwd: np.ndarray,
    *,
    k: int,
    horizon: int,
    train_frac: float = 0.7,
) -> Effect | None:
    """Causal k-NN on factor: neighbours only from earlier events (prefix pool)."""
    n = factors.size
    if n < max(200, k * 4):
        return None
    # Expanding-window neighbours: for query i, pool is 0..i-1 (past only).
    # Vectorised via sorting is hard with expanding pools; chunked matmul on a
    # chronological split approximates: train pool for all OOS queries.
    cut = int(n * train_frac)
    if cut < k + 10 or n - cut < 50:
        return None
    train_f = factors[:cut]
    train_y = fwd[:cut]
    test_f = factors[cut:]
    test_y = fwd[cut:]
    # Distances: |test_f[:, None] - train_f[None, :]|
    dist = np.abs(test_f[:, None] - train_f[None, :])
    nn = np.argpartition(dist, kth=k - 1, axis=1)[:, :k]
    # Distance-weighted mean of neighbour outcomes
    rows = np.arange(len(test_f))[:, None]
    d = np.take_along_axis(dist, nn, axis=1)
    w = 1.0 / (d + 1e-6)
    w = w / w.sum(axis=1, keepdims=True)
    neigh_y = train_y[nn]
    pred = (w * neigh_y).sum(axis=1)
    corr = safe_corr(pred, test_y)
    # Correlation p-value via NW on the product proxy is awkward; use simple t on Fisher
    # transform with effective n = test size / horizon overlap factor.
    if not np.isfinite(corr) or len(test_y) < 30:
        return None
    # Conservative: treat effective n as n / horizon
    n_eff = max(10.0, len(test_y) / max(1, horizon))
    # Fisher z
    z = 0.5 * np.log((1 + np.clip(corr, -0.999, 0.999)) / (1 - np.clip(corr, -0.999, 0.999)))
    t_stat = z * np.sqrt(n_eff)
    return Effect(
        name=f"abc_factor|knn_k{k}|fwd{horizon}",
        statistic=float(corr),
        n=int(len(test_y)),
        p_value=normal_two_sided_p(float(t_stat)),
        detail={
            "corr_pred_vs_realised": float(corr),
            "k": float(k),
            "horizon": float(horizon),
            "n_train": float(cut),
            "mean_abs_error_bps": float(np.nanmean(np.abs(pred - test_y)) * 1e4),
        },
    )


def _placebo_knn(
    factors: np.ndarray,
    fwd: np.ndarray,
    *,
    k: int,
    horizon: int,
    seed: int = 0,
) -> Effect | None:
    """Same k-NN after shuffling factors — must not beat the real arm."""
    rng = np.random.default_rng(seed)
    shuffled = factors.copy()
    rng.shuffle(shuffled)
    eff = _similarity_effect(shuffled, fwd, k=k, horizon=horizon)
    if eff is None:
        return None
    return Effect(
        name=f"abc_factor|PLACEBO_knn_k{k}|fwd{horizon}",
        statistic=eff.statistic,
        n=eff.n,
        p_value=eff.p_value,
        detail={**eff.detail, "placebo": 1.0},
    )


def _score_abc_triples(
    triples: pd.DataFrame,
    close: pd.Series,
    *,
    horizons: tuple[int, ...] = HORIZONS,
    name_prefix: str = "abc_factor",
) -> list[Effect]:
    """Shared scoring for warehouse-leg and causal-wave-extrema triples."""
    effects: list[Effect] = []
    for horizon in horizons:
        factors, fwd = _align_forward(triples, close, horizon)
        if factors.size < MIN_EVENTS * 2:
            continue

        for label, targets in (("classical", CLASSICAL_FACTORS), ("placebo", PLACEBO_FACTORS)):
            for e in _bucket_effects(
                factors, fwd, targets=targets, label=label, horizon=horizon
            ):
                e.name = e.name.replace("abc_factor|", f"{name_prefix}|", 1)
                effects.append(e)

        for k in K_NEIGHBOURS:
            knn = _similarity_effect(factors, fwd, k=k, horizon=horizon)
            if knn is not None:
                knn.name = knn.name.replace("abc_factor|", f"{name_prefix}|", 1)
                effects.append(knn)
            plac = _placebo_knn(factors, fwd, k=k, horizon=horizon, seed=horizon * 17 + k)
            if plac is not None:
                plac.name = plac.name.replace("abc_factor|", f"{name_prefix}|", 1)
                effects.append(plac)

        corr = safe_corr(factors, fwd)
        if np.isfinite(corr) and factors.size >= MIN_EVENTS:
            x = factors - factors.mean()
            y = fwd - fwd.mean()
            beta = float(np.dot(x, y) / (np.dot(x, x) + 1e-18))
            _, t_m = newey_west_tstat(x * y, lags=horizon)
            effects.append(
                Effect(
                    name=f"{name_prefix}|linear_corr|fwd{horizon}",
                    statistic=float(corr),
                    n=int(factors.size),
                    p_value=normal_two_sided_p(t_m),
                    detail={
                        "corr": float(corr),
                        "beta": beta,
                        "t_hac_moment": float(t_m),
                        "mean_factor": float(np.nanmean(factors)),
                        "median_factor": float(np.nanmedian(factors)),
                        "horizon": float(horizon),
                    },
                )
            )

        conf = triples["confirm_time"]
        close_idx = close.index.sort_values()
        pos = close_idx.searchsorted(conf, side="right") - 1
        valid = (pos >= 0) & (pos < len(close_idx))
        pos = np.clip(pos, 0, len(close_idx) - 1)
        times = close_idx[pos]
        fwd_s = forward_log_return(close, horizon).reindex(times).to_numpy(dtype=float)
        bc_dir = triples["bc_dir"].to_numpy(dtype=float)
        f_all = triples["factor"].to_numpy(dtype=float)
        ok = valid & np.isfinite(fwd_s) & np.isfinite(f_all) & (times <= conf.to_numpy())
        signed = fwd_s[ok] * bc_dir[ok]
        f_ok = f_all[ok]
        for target, tag in ((1.000, "equal"), (0.618, "0618"), (1.618, "1618")):
            near = np.abs(f_ok - target) <= FACTOR_TOL
            if near.sum() < MIN_EVENTS:
                continue
            mean_ex, t_stat = newey_west_tstat(signed[near], lags=horizon)
            effects.append(
                Effect(
                    name=f"{name_prefix}|bc_continuation|{tag}|fwd{horizon}",
                    statistic=float(mean_ex),
                    n=int(near.sum()),
                    p_value=normal_two_sided_p(t_stat),
                    detail={
                        "excess_bps": float(mean_ex * 1e4),
                        "target_factor": float(target),
                        "horizon": float(horizon),
                        "hit_rate": float(np.mean(signed[near] > 0)),
                    },
                )
            )
    return effects


def run_abc_factor_study(
    ohlcv: pd.DataFrame,
    symbol: str,
    timeframe: str,
    *,
    horizons: tuple[int, ...] = HORIZONS,
    source: str | None = None,
) -> list[Effect]:
    """Warehouse-leg A–B / B–C factor scan (primary, tradeable geometry)."""
    require_placebo_arm(
        LevelClaim(
            name="abc_distance_factor",
            real_ratios=CLASSICAL_FACTORS,
            placebo_ratios=PLACEBO_FACTORS,
            anchors="confirmed consecutive swing triples A→B→C from indicators.legs",
            proximity_band=f"|factor - target| <= {FACTOR_TOL}",
        )
    )
    legs = load_legs(symbol, timeframe, source=source)
    triples = build_abc_triples(legs)
    if len(triples) < MIN_EVENTS * 2:
        return []
    return apply_fdr(
        _score_abc_triples(triples, ohlcv["close"].astype(float), horizons=horizons)
    )


def run_abc_factor_study_wave_extrema(
    ohlcv: pd.DataFrame,
    *,
    horizons: tuple[int, ...] = HORIZONS,
    period: float | None = None,
) -> list[Effect]:
    """Same factor scan on causal-wave extrema — separate arm, not warehouse legs.

    Labelled ``abc_wave|*`` so it cannot be confused with the tradeable swing geometry.
    """
    require_placebo_arm(
        LevelClaim(
            name="abc_wave_extrema_factor",
            real_ratios=CLASSICAL_FACTORS,
            placebo_ratios=PLACEBO_FACTORS,
            anchors="causal_wave peaks/troughs confirmed one bar after the turn",
            proximity_band=f"|factor - target| <= {FACTOR_TOL}",
        )
    )
    close = ohlcv["close"].astype(float)
    extrema = causal_wave_extrema(close, period=period)
    triples = build_abc_triples_from_extrema(extrema)
    if len(triples) < MIN_EVENTS * 2:
        return []
    return apply_fdr(
        _score_abc_triples(
            triples, close, horizons=horizons, name_prefix="abc_wave"
        )
    )


def factor_summary(triples: pd.DataFrame) -> dict[str, float]:
    """Descriptive stats of the factor distribution (no forward returns)."""
    f = triples["factor"].to_numpy(dtype=float)
    f = f[np.isfinite(f)]
    return {
        "n_triples": float(f.size),
        "mean": float(np.mean(f)),
        "median": float(np.median(f)),
        "p10": float(np.quantile(f, 0.10)),
        "p90": float(np.quantile(f, 0.90)),
        "frac_near_1.0": float(np.mean(np.abs(f - 1.0) <= FACTOR_TOL)),
        "frac_near_0.618": float(np.mean(np.abs(f - 0.618) <= FACTOR_TOL)),
        "frac_near_1.618": float(np.mean(np.abs(f - 1.618) <= FACTOR_TOL)),
    }
