"""Release gates that must pass before a hunt may escalate or quote numbers."""

from __future__ import annotations

import numpy as np

from llm2.hunt.targets import proxy_side, target_family
from llm2.paths import ROUND_TRIP_COST

FAMILIES = ("fwd_return", "quantile", "direction", "xs_rank", "volatility", "vol_ratio")


def _proxy_pf(side: np.ndarray, realized_ret: np.ndarray) -> float:
    ret = realized_ret * side - ROUND_TRIP_COST * (side != 0)
    wins = float(np.nansum(ret[ret > 0]))
    losses = float(-np.nansum(ret[ret < 0]))
    if losses > 0:
        return wins / losses
    if wins > 0:
        return 2.0
    return 0.0


def _skill(pred: np.ndarray, y: np.ndarray, train_mean: float) -> float:
    mae = float(np.nanmean(np.abs(y - pred)))
    mae_base = float(np.nanmean(np.abs(y - train_mean)))
    return float(mae_base / mae) if mae > 1e-12 else 0.0


def constant_predictor_scores() -> dict[str, float]:
    """Return the constant-predictor score for every target family (must be <= 1.0)."""
    rng = np.random.default_rng(0)
    n = 2000
    realized = rng.normal(0.0, 0.01, size=n)
    out: dict[str, float] = {}
    for target in FAMILIES:
        family = target_family(target)
        if family == "return":
            y = realized.copy()
            const = np.full(n, float(np.mean(y[:1000])))
            out[target] = _proxy_pf(proxy_side(const, family), realized)
        elif family == "directional":
            const = np.zeros(n)
            out[target] = _proxy_pf(proxy_side(const, family), realized)
        elif family == "rank":
            const = np.full(n, 0.5)
            out[target] = _proxy_pf(proxy_side(const, family), realized)
        else:
            y = np.abs(rng.normal(0.03, 0.02, size=n))
            train_mean = float(np.mean(y[:1000]))
            const = np.full(n, train_mean)
            out[target] = _skill(const[1000:], y[1000:], train_mean)
    return out


def require_constant_predictor_invariant(*, tol: float = 1e-9) -> dict[str, float]:
    """Fail closed if a constant predictor can score above 1.0 on any family.

    This is the standing guard against the units-bug class that produced the false
    Tier-2 at Profit Factor 2988. Cheaper than another false candidate review.
    """
    scores = constant_predictor_scores()
    bad = {k: v for k, v in scores.items() if v > 1.0 + tol}
    if bad:
        raise RuntimeError(
            "constant-predictor release gate FAILED — scoring units are unsafe: "
            + ", ".join(f"{k}={v:.4f}" for k, v in bad.items())
        )
    return scores


def require_predictability_gate_discriminates(*, alpha: float = 0.05) -> dict[str, float]:
    """Fail closed if the Stage-B gate cannot both pass and fail on known data.

    The gate previously probed with a constant predictor and returned False for every
    dataset, capping 148 generations at tier 0 while looking like a research verdict
    (D-013). A gate that cannot reject is not a conservative gate, it is a broken one.
    """
    from llm2.audit.predictability import audit_predictability, required_surrogates_per_family
    from llm2.audit.surrogates import list_surrogates

    n = 3000
    rng = np.random.default_rng(20250803)
    X = rng.normal(size=(n, 6))
    draws = required_surrogates_per_family(alpha, len(list_surrogates()))

    signal = audit_predictability(
        X,
        0.8 * X[:, 0] + rng.normal(0.0, 0.4, size=n),
        target="release_gate_signal",
        n_surrogates=draws,
        alpha=alpha,
        probes=("ridge",),
    )
    noise = audit_predictability(
        X,
        rng.normal(size=n),
        target="release_gate_noise",
        n_surrogates=draws,
        alpha=alpha,
        probes=("ridge",),
    )

    if not signal.passed:
        raise RuntimeError(
            "predictability release gate FAILED — a known linear signal did not pass: "
            + signal.summary()
        )
    if noise.passed:
        raise RuntimeError(
            "predictability release gate FAILED — pure noise passed: " + noise.summary()
        )
    return {"signal_score": signal.real_score, "noise_p": noise.p_value}
