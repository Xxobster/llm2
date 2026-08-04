"""Collapse the dollar and commodity complex into one factor, and test it once.

Thirty-one external series produced zero linear survivors and one correlated factor block.
The marginal series was worth less than the multiplicity penalty it added, so the response
is not another series — it is to stop treating the block as thirty-one hypotheses.

The dollar complex is not thirty-one independent things. DXY, EURUSD, GBPUSD, USDJPY,
USDCHF, USDCAD, AUDUSD and NZDUSD are largely one number seen from eight angles, and gold,
silver, copper and oil load on the same dollar move plus a growth component. Testing each
separately spends the entire false-discovery budget on redundancy: eight tests of the same
underlying variable are eight chances to get lucky and eight divisions of the threshold.

So this module extracts a single factor from the block and asks **one** question of it.
One hypothesis, one p-value, no correction needed. If a dollar factor has no predictive
relationship with crypto, that is a clean and final answer for the whole complex.

Construction rules that matter:

- Sign alignment. USDJPY rising and EURUSD rising mean opposite things about the dollar.
  Quote-currency pairs are inverted so every input increases when the dollar strengthens,
  otherwise the first principal component is mostly a quoting convention.
- Returns, not levels. Levels are non-stationary and their principal components are
  dominated by trends that produce spurious regressions.
- The loadings are fitted **inside each training fold** and applied unchanged out of
  sample. A factor fitted on the full history is a look-ahead the size of the sample.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from llm2.diagnostics.stats import Effect, apply_fdr, newey_west_tstat, normal_two_sided_p

# Sign convention: +1 means the series rises when the US dollar strengthens.
DOLLAR_BLOCK: dict[str, int] = {
    "DXY": +1,
    "EURUSD": -1,
    "GBPUSD": -1,
    "AUDUSD": -1,
    "NZDUSD": -1,
    "USDJPY": +1,
    "USDCHF": +1,
    "USDCAD": +1,
}

COMMODITY_BLOCK: dict[str, int] = {
    "XAUUSD": -1,
    "XAGUSD": -1,
    "COPPER": -1,
    "WTI": -1,
    "BRENT": -1,
}


def _load_block(block: dict[str, int], timeframe: str) -> pd.DataFrame:
    from llm2.data.macro import load_external

    cols = {}
    for sym, sign in block.items():
        try:
            raw = load_external(sym, timeframe)
        except Exception:  # noqa: BLE001
            continue
        s = raw if isinstance(raw, pd.Series) else raw[
            "close" if "close" in raw.columns else raw.columns[0]
        ]
        s = pd.to_numeric(s, errors="coerce")
        cols[sym] = sign * np.log(s.where(s > 0)).diff()
    return pd.DataFrame(cols).dropna(how="all")


def fit_factor(returns: pd.DataFrame) -> tuple[np.ndarray, float]:
    """First principal component of a return block, as loadings and variance explained.

    Standardising first matters: without it the component is dominated by whichever series
    happens to be most volatile rather than by the shared move.
    """
    X = returns.to_numpy(dtype=float)
    mu, sd = np.nanmean(X, axis=0), np.nanstd(X, axis=0)
    sd[sd <= 0] = 1.0
    Z = np.nan_to_num((X - mu) / sd)
    _, s, vt = np.linalg.svd(Z, full_matrices=False)
    load = vt[0]
    # Orient so the factor is positive when the block as a whole rises, which after the
    # sign alignment above means "the dollar strengthened".
    if load.sum() < 0:
        load = -load
    explained = float(s[0] ** 2 / np.sum(s**2))
    return load, explained


def dollar_factor_test(
    ohlcv: pd.DataFrame,
    *,
    timeframe: str = "1h",
    horizons: tuple[int, ...] = (6, 24),
    n_folds: int = 5,
) -> list[Effect]:
    """One hypothesis: does a fold-fitted dollar factor forecast crypto returns?

    Returns at most ``len(horizons) * 2`` effects — the factor's own predictive relationship
    and a redundancy diagnostic — rather than the eight-to-thirteen that testing each series
    separately would produce. False-discovery control is still applied across the handful
    that remain.
    """
    dollar = _load_block(DOLLAR_BLOCK, timeframe)
    commodity = _load_block(COMMODITY_BLOCK, timeframe)
    if dollar.shape[1] < 3:
        return []

    block = dollar.join(commodity, how="outer") if not commodity.empty else dollar
    block = block.replace([np.inf, -np.inf], np.nan).dropna()
    if len(block) < 5000:
        return []

    crypto_ret = np.log(pd.to_numeric(ohlcv["close"], errors="coerce")).diff()
    joined = block.join(crypto_ret.rename("y"), how="inner").dropna()
    if len(joined) < 5000:
        return []

    feat_cols = [c for c in joined.columns if c != "y"]
    effects: list[Effect] = []

    # How much of the block really is one thing? If the first component explains most of
    # the variance, testing the members separately was never thirteen hypotheses.
    _, explained_full = fit_factor(joined[feat_cols])
    effects.append(
        Effect(
            name="dollar_block|variance_explained_by_first_factor",
            statistic=float(explained_full),
            n=int(len(joined)),
            detail={
                "n_series": len(feat_cols),
                "interpretation": (
                    "share of the block's variance carried by a single factor; "
                    "high values mean the separate series were redundant hypotheses"
                ),
            },
        )
    )

    # Chronological folds. Loadings are fitted on the training part of each fold only.
    bounds = np.linspace(0, len(joined), n_folds + 1).astype(int)
    for h in horizons:
        fwd = (
            np.log(pd.to_numeric(ohlcv["close"], errors="coerce"))
            .diff(h)
            .shift(-h)
            .reindex(joined.index)
        )
        oos_factor: list[np.ndarray] = []
        oos_y: list[np.ndarray] = []
        for k in range(1, n_folds):
            tr = slice(bounds[0], bounds[k])
            te = slice(bounds[k], bounds[k + 1])
            train = joined[feat_cols].iloc[tr]
            if len(train) < 1000:
                continue
            load, _ = fit_factor(train)
            mu = train.to_numpy().mean(axis=0)
            sd = train.to_numpy().std(axis=0)
            sd[sd <= 0] = 1.0
            test = joined[feat_cols].iloc[te].to_numpy()
            f = np.nan_to_num((test - mu) / sd) @ load
            y = fwd.iloc[te].to_numpy(dtype=float)
            ok = np.isfinite(f) & np.isfinite(y)
            oos_factor.append(f[ok])
            oos_y.append(y[ok])

        if not oos_factor:
            continue
        f_all = np.concatenate(oos_factor)
        y_all = np.concatenate(oos_y)
        if f_all.size < 1000:
            continue

        corr = float(np.corrcoef(f_all, y_all)[0, 1])
        # Overlapping forward returns are mechanically autocorrelated, so the significance
        # of a correlation between them needs HAC standard errors, not the textbook formula.
        fz = (f_all - f_all.mean()) / (f_all.std() or 1.0)
        yz = (y_all - y_all.mean()) / (y_all.std() or 1.0)
        # The mean of the standardised cross-product is the correlation, so a HAC t-test on
        # that product is a correlation test with the overlap accounted for.
        _, t_stat = newey_west_tstat(fz * yz, lags=max(1, h))
        p_val = normal_two_sided_p(t_stat)
        effects.append(
            Effect(
                name=f"dollar_factor|fwd{h}",
                statistic=corr,
                n=int(f_all.size),
                p_value=p_val,
                detail={
                    "horizon": h,
                    "nw_t": t_stat,
                    "r_squared": corr**2,
                    "loadings_fitted": "inside each training fold only",
                    "hypotheses_replaced": len(feat_cols),
                },
            )
        )
    return apply_fdr(effects)
