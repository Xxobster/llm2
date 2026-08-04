"""Predictability audit: does a real learner on X beat the same learner on surrogate labels?

This is a permutation test, not a score threshold. The real pipeline and every surrogate
pipeline are identical in every respect except that the surrogate has had the structure
linking ``X`` to ``y`` destroyed, so any difference in out-of-sample skill is attributable
to that structure.

History: the previous implementation probed with ``HistoricalMeanBaseline``, which ignores
``X`` and predicts a constant. Its ``r2_like`` was therefore exactly 0 by construction while
the pass condition required ``> 1e-6``, making the gate unconditionally false. It capped
every trial in the project at tier 0 and blocked every tradesim escalation. See D-013.
"""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np

from llm2.audit.surrogates import apply_surrogate, list_surrogates

# A probe has to be able to express the structure we are asking about. Ridge answers "is
# there a linear relationship", gradient boosting answers "is there any low-order
# interaction". Taking the max over probes is a biased statistic, which is fine precisely
# because the surrogate arm is scored with the identical max.
DEFAULT_PROBES = ("ridge", "lgbm")

MIN_TRAIN_ROWS = 200
MIN_TEST_ROWS = 100


def required_draws(alpha: float) -> int:
    """Minimum surrogate draws for an add-one permutation p-value to reach ``alpha``."""
    return int(np.ceil(1.0 / alpha)) - 1


def required_surrogates_per_family(alpha: float, n_families: int) -> int:
    """Per-family draw count needed so the pooled null can resolve ``alpha``."""
    return int(np.ceil(required_draws(alpha) / max(1, n_families)))


@dataclass
class PredictabilityReport:
    target: str
    metric_name: str
    real_score: float
    surrogate_scores: dict[str, float]
    passed: bool
    p_value: float = 1.0
    n_surrogate_draws: int = 0
    surrogate_max: float = float("nan")
    surrogate_q95: float = float("nan")
    per_probe_real: dict[str, float] = field(default_factory=dict)
    reason: str = ""

    def summary(self) -> str:
        return (
            f"real={self.real_score:+.5f} p={self.p_value:.4f} "
            f"surr_q95={self.surrogate_q95:+.5f} surr_max={self.surrogate_max:+.5f} "
            f"draws={self.n_surrogate_draws} passed={self.passed}"
            + (f" reason={self.reason}" if self.reason else "")
        )


def oos_skill(y_test: np.ndarray, y_pred: np.ndarray, train_mean: float) -> float:
    """Out-of-sample R^2 against a constant predictor fitted on the training slice.

    Zero means "no better than always predicting the training mean". A constant predictor
    scores exactly 0 here, which is what makes this metric safe as a permutation statistic.
    """
    mask = np.isfinite(y_test) & np.isfinite(y_pred)
    if mask.sum() < 5:
        return float("nan")
    y_t = y_test[mask]
    err_model = float(np.mean((y_t - y_pred[mask]) ** 2))
    err_base = float(np.mean((y_t - train_mean) ** 2))
    if err_base <= 1e-18:
        return float("nan")
    return float(1.0 - err_model / err_base)


def _fit_predict(probe: str, X_tr: np.ndarray, y_tr: np.ndarray, X_te: np.ndarray) -> np.ndarray | None:
    """Fit one probe and return test predictions, or None if the probe is unavailable."""
    if probe == "ridge":
        from sklearn.linear_model import Ridge
        from sklearn.pipeline import make_pipeline
        from sklearn.preprocessing import StandardScaler

        # Standardisation is fitted inside the training slice only. Without it, ridge on a
        # feature pack mixing EMA levels (~1e4) with log returns (~1e-3) is dominated by
        # scale rather than information.
        model = make_pipeline(StandardScaler(), Ridge(alpha=1.0))
        model.fit(X_tr, y_tr)
        return np.asarray(model.predict(X_te), dtype=float)

    if probe == "lgbm":
        try:
            import lightgbm as lgb
        except ImportError:
            return None
        model = lgb.LGBMRegressor(
            n_estimators=120,
            num_leaves=15,
            learning_rate=0.05,
            min_child_samples=50,
            subsample=0.8,
            subsample_freq=1,
            colsample_bytree=0.8,
            verbosity=-1,
            n_jobs=1,
        )
        model.fit(X_tr, y_tr)
        return np.asarray(model.predict(X_te), dtype=float)

    raise ValueError(f"unknown probe: {probe}")


def _best_skill(
    X_tr: np.ndarray,
    y_tr: np.ndarray,
    X_te: np.ndarray,
    y_te: np.ndarray,
    probes: tuple[str, ...],
) -> tuple[float, dict[str, float]]:
    """Max out-of-sample skill across probes, plus the per-probe breakdown."""
    train_mean = float(np.mean(y_tr))
    per_probe: dict[str, float] = {}
    for probe in probes:
        try:
            pred = _fit_predict(probe, X_tr, y_tr, X_te)
        except Exception:  # noqa: BLE001 - a probe that cannot fit contributes no evidence
            pred = None
        if pred is None:
            continue
        per_probe[probe] = oos_skill(y_te, pred, train_mean)
    finite = [v for v in per_probe.values() if np.isfinite(v)]
    best = max(finite) if finite else float("nan")
    return best, per_probe


def _clean(X: np.ndarray, y: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Drop rows with any non-finite feature or label, preserving chronological order."""
    X = np.asarray(X, dtype=float)
    y = np.asarray(y, dtype=float)
    if X.ndim == 1:
        X = X.reshape(-1, 1)
    mask = np.isfinite(y) & np.all(np.isfinite(X), axis=1)
    return X[mask], y[mask]


def audit_predictability(
    X: np.ndarray,
    y: np.ndarray,
    *,
    target: str = "fwd_return",
    n_surrogates: int = 20,
    seed: int = 42,
    train_frac: float = 0.7,
    alpha: float = 0.05,
    probes: tuple[str, ...] = DEFAULT_PROBES,
) -> PredictabilityReport:
    """Permutation test for learnable structure between ``X`` and ``y``.

    ``n_surrogates`` draws are taken per surrogate family. The real arm and every surrogate
    arm use the same chronological split, the same probes and the same skill metric.
    """
    rng = np.random.default_rng(seed)
    X_c, y_c = _clean(X, y)
    n = len(y_c)

    cut = int(n * train_frac)
    if cut < MIN_TRAIN_ROWS or (n - cut) < MIN_TEST_ROWS:
        return PredictabilityReport(
            target=target,
            metric_name="oos_r2_permutation",
            real_score=float("nan"),
            surrogate_scores={},
            passed=False,
            reason=f"insufficient rows (n={n}, train={cut}, test={n - cut})",
        )
    if float(np.std(y_c)) <= 1e-18:
        return PredictabilityReport(
            target=target,
            metric_name="oos_r2_permutation",
            real_score=float("nan"),
            surrogate_scores={},
            passed=False,
            reason="degenerate label (zero variance)",
        )

    X_tr, X_te = X_c[:cut], X_c[cut:]
    y_tr, y_te = y_c[:cut], y_c[cut:]

    real_score, per_probe_real = _best_skill(X_tr, y_tr, X_te, y_te, probes)
    if not np.isfinite(real_score):
        return PredictabilityReport(
            target=target,
            metric_name="oos_r2_permutation",
            real_score=float("nan"),
            surrogate_scores={},
            passed=False,
            per_probe_real=per_probe_real,
            reason="no probe produced a finite score",
        )

    # Surrogates are applied to the whole label series before the split, so the surrogate
    # arm sees exactly the same split geometry as the real arm.
    draws: list[float] = []
    surrogate_scores: dict[str, float] = {}
    for name in list_surrogates():
        family: list[float] = []
        for _ in range(n_surrogates):
            y_s = apply_surrogate(y_c, name, rng=rng)
            y_s = np.asarray(y_s, dtype=float)
            if not np.all(np.isfinite(y_s)):
                y_s = np.where(np.isfinite(y_s), y_s, float(np.nanmean(y_s)))
            score, _ = _best_skill(X_tr, y_s[:cut], X_te, y_s[cut:], probes)
            if np.isfinite(score):
                family.append(score)
        if family:
            surrogate_scores[name] = float(np.mean(family))
            draws.extend(family)

    if not draws:
        return PredictabilityReport(
            target=target,
            metric_name="oos_r2_permutation",
            real_score=real_score,
            surrogate_scores={},
            passed=False,
            per_probe_real=per_probe_real,
            reason="no surrogate draw produced a finite score",
        )

    arr = np.asarray(draws, dtype=float)
    # Add-one empirical p-value: the real arm is counted as one of its own null draws, which
    # keeps the test conservative and stops p from ever being exactly zero.
    p_value = float((1.0 + np.sum(arr >= real_score)) / (1.0 + arr.size))

    # The smallest p this many draws can express is 1/(1+draws). If that floor is above
    # alpha the test cannot reject however strong the signal is, and reporting "did not
    # pass" would repeat the D-013 mistake of presenting a structural impossibility as a
    # negative result.
    floor = 1.0 / (1.0 + arr.size)
    if floor > alpha:
        return PredictabilityReport(
            target=target,
            metric_name="oos_r2_permutation",
            real_score=real_score,
            surrogate_scores=surrogate_scores,
            passed=False,
            p_value=p_value,
            n_surrogate_draws=int(arr.size),
            surrogate_max=float(np.max(arr)),
            surrogate_q95=float(np.quantile(arr, 0.95)),
            per_probe_real=per_probe_real,
            reason=(
                f"underpowered: {arr.size} draws can only resolve p>={floor:.4f} "
                f"at alpha={alpha}; need at least {required_draws(alpha)} draws"
            ),
        )

    passed = bool(p_value <= alpha)

    return PredictabilityReport(
        target=target,
        metric_name="oos_r2_permutation",
        real_score=real_score,
        surrogate_scores=surrogate_scores,
        passed=passed,
        p_value=p_value,
        n_surrogate_draws=int(arr.size),
        surrogate_max=float(np.max(arr)),
        surrogate_q95=float(np.quantile(arr, 0.95)),
        per_probe_real=per_probe_real,
    )


# Retained for callers that scored a prediction directly against label variance.
def score_regression(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    mask = np.isfinite(y_true) & np.isfinite(y_pred)
    if mask.sum() < 5:
        return float("nan")
    err = y_true[mask] - y_pred[mask]
    return float(1.0 - np.mean(err**2) / (np.var(y_true[mask]) + 1e-12))
