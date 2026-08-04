"""Falsification controls for transfer-entropy findings.

Linear correlation found nothing across the external panel; transfer entropy found
something. That contrast is interesting only if the something survives three controls that
kill the known failure modes of the estimator.

1. **Block shuffle.** Recompute after shuffling the *source* in blocks long enough to keep
   its own volatility clustering but destroy its timing against the target. If the measured
   flow survives, the estimator is reporting bias or shared volatility structure, not a lead.
2. **Volatility standardisation.** Divide both series by their own trailing volatility and
   recompute. Most mutual information in financial series lives in the volatility envelope.
   If the signal disappears here, what was found is "markets are volatile at the same time",
   which is already known and cannot be traded with a directional bet.
3. **Sign-only.** Recompute using only the sign of each return. This strips magnitude
   entirely. Directional information should survive; a volatility artefact should not.

A finding that fails all three is closed. A finding that survives all three is the *one*
cross-asset interaction worth registering — and it still needs a matched-control event study
before it is called an edge.
"""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np
import pandas as pd

from llm2.diagnostics.crossasset import transfer_entropy
from llm2.diagnostics.stats import Effect, apply_fdr


@dataclass
class FalsificationReport:
    """One source → target pair under the three controls."""

    source: str
    target: str
    window: int
    horizon: int
    baseline: Effect
    block_shuffle: Effect
    vol_standardised: Effect
    sign_only: Effect
    detail: dict = field(default_factory=dict)

    @property
    def survives_block_shuffle(self) -> bool:
        """The finding is timing-dependent: shuffling the source kills it.

        If the block-shuffled source still produces a significant transfer entropy, the
        estimator is reporting bias or a property of the marginal distributions, not a lead.
        """
        return self.baseline.significant and not self.block_shuffle.significant

    @property
    def survives_vol_standardisation(self) -> bool:
        """The finding is not just shared volatility: it remains after scaling by trailing vol."""
        return self.baseline.significant and self.vol_standardised.significant

    @property
    def survives_sign_only(self) -> bool:
        """The finding is directional: it remains when only the sign of each return is kept."""
        return self.baseline.significant and self.sign_only.significant

    @property
    def survives_all_three(self) -> bool:
        return (
            self.survives_block_shuffle
            and self.survives_vol_standardisation
            and self.survives_sign_only
        )

    @property
    def survives_any(self) -> bool:
        return (
            self.survives_block_shuffle
            or self.survives_vol_standardisation
            or self.survives_sign_only
        )

    def summary(self) -> str:
        def _fmt(e: Effect, *, role: str) -> str:
            q = e.q_value if e.q_value is not None else float("nan")
            return f"stat={e.statistic:+.4f} q={q:.4f} sig={e.significant} [{role}]"

        if not self.baseline.significant:
            verdict = "NO BASELINE — nothing to falsify"
        elif self.survives_all_three:
            verdict = "SURVIVES — register as one interaction hypothesis"
        elif self.survives_any:
            parts = []
            if self.survives_block_shuffle:
                parts.append("timing")
            if self.survives_vol_standardisation:
                parts.append("not-just-vol")
            if self.survives_sign_only:
                parts.append("directional")
            verdict = f"PARTIAL — survives {', '.join(parts)} only"
        else:
            verdict = "CLOSED — estimator artefact or shared volatility"

        return (
            f"{self.source}->{self.target} w{self.window}->fwd{self.horizon}: {verdict}\n"
            f"  baseline         {_fmt(self.baseline, role='must be sig')}\n"
            f"  block_shuffle    {_fmt(self.block_shuffle, role='must NOT be sig to survive')}\n"
            f"  vol_standardised {_fmt(self.vol_standardised, role='must stay sig to survive')}\n"
            f"  sign_only        {_fmt(self.sign_only, role='must stay sig to survive')}"
        )


def _block_shuffle(x: np.ndarray, *, block: int, seed: int) -> np.ndarray:
    """Shuffle contiguous blocks. Preserves short-run autocorrelation and vol clustering."""
    n = len(x)
    if block < 2 or block >= n:
        rng = np.random.default_rng(seed)
        return rng.permutation(x)
    n_blocks = int(np.ceil(n / block))
    pads = n_blocks * block - n
    padded = np.concatenate([x, np.full(pads, np.nan)]) if pads else x.copy()
    blocks = padded.reshape(n_blocks, block)
    rng = np.random.default_rng(seed)
    rng.shuffle(blocks, axis=0)
    return blocks.ravel()[:n]


def _vol_standardise(x: pd.Series, *, window: int = 168) -> pd.Series:
    sigma = x.rolling(window, min_periods=max(20, window // 4)).std().shift(1)
    return x / sigma.replace(0, np.nan)


def falsify_transfer_entropy(
    source: pd.Series,
    target: pd.Series,
    *,
    source_name: str = "source",
    target_name: str = "target",
    window: int = 6,
    horizon: int = 6,
    n_surrogates: int = 100,
    block: int = 168,
    seed: int = 0,
) -> FalsificationReport:
    """Run the three controls on one aligned source/target pair.

    ``source`` and ``target`` are expected to already be the series that enter the
    transfer-entropy calculation (typically trailing log returns and a forward return).
    """
    frame = pd.DataFrame({"x": source, "y": target}).dropna()
    x = frame["x"].to_numpy(dtype=float)
    y = frame["y"].to_numpy(dtype=float)

    baseline = transfer_entropy(x, y, n_surrogates=n_surrogates, seed=seed)
    baseline.name = f"{source_name}|TE_baseline_w{window}->fwd{horizon}"

    shuffled = _block_shuffle(x, block=block, seed=seed + 1)
    block_eff = transfer_entropy(shuffled, y, n_surrogates=n_surrogates, seed=seed + 2)
    block_eff.name = f"{source_name}|TE_block_shuffle_w{window}->fwd{horizon}"

    xs = _vol_standardise(frame["x"]).to_numpy()
    ys = _vol_standardise(frame["y"]).to_numpy()
    ok = np.isfinite(xs) & np.isfinite(ys)
    vol_eff = transfer_entropy(xs[ok], ys[ok], n_surrogates=n_surrogates, seed=seed + 3)
    vol_eff.name = f"{source_name}|TE_vol_std_w{window}->fwd{horizon}"

    sign_eff = transfer_entropy(
        np.sign(x), np.sign(y), n_surrogates=n_surrogates, seed=seed + 4
    )
    sign_eff.name = f"{source_name}|TE_sign_only_w{window}->fwd{horizon}"

    return FalsificationReport(
        source=source_name,
        target=target_name,
        window=window,
        horizon=horizon,
        baseline=baseline,
        block_shuffle=block_eff,
        vol_standardised=vol_eff,
        sign_only=sign_eff,
        detail={"n": int(len(frame)), "block_bars": block},
    )


def falsify_panel(
    ohlcv: pd.DataFrame,
    panel: pd.DataFrame,
    *,
    window: int = 6,
    horizon: int = 6,
    n_surrogates: int = 100,
    max_symbols: int | None = None,
    seed: int = 0,
) -> list[FalsificationReport]:
    """Apply the three controls to every external series against the crypto forward return."""
    from llm2.diagnostics.crossasset import _forward_log_return, _log_returns

    close = ohlcv["close"]
    fwd = _forward_log_return(close, horizon)
    value_cols = [c for c in panel.columns if not c.endswith("__age_sec")]
    if max_symbols is not None:
        value_cols = value_cols[:max_symbols]

    reports: list[FalsificationReport] = []
    for i, sym in enumerate(value_cols):
        ext = _log_returns(panel[sym], window)
        frame = pd.DataFrame({"x": ext, "y": fwd}).dropna()
        if len(frame) < 3000:
            continue
        reports.append(
            falsify_transfer_entropy(
                frame["x"],
                frame["y"],
                source_name=sym,
                target_name="crypto_fwd",
                window=window,
                horizon=horizon,
                n_surrogates=n_surrogates,
                seed=seed + i * 17,
            )
        )

    # FDR across every control of every pair, so a single lucky survival does not look like
    # a panel of survivors.
    flat: list[Effect] = []
    for r in reports:
        flat.extend([r.baseline, r.block_shuffle, r.vol_standardised, r.sign_only])
    apply_fdr(flat)
    return reports
