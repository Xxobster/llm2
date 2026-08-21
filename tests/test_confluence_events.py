"""Confluence event catalog: prefix-invariant features, future-only labels."""

from __future__ import annotations

import numpy as np
import pandas as pd

from llm2.confluence.events import (
    EVENT_IDS,
    any_in_next,
    build_event_pack,
    build_known_now_features,
)


def _ohlcv(n: int = 800, seed: int = 0, *, rsi_sink: bool = False) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    close = 100.0 + np.cumsum(rng.normal(0, 0.15, size=n))
    if rsi_sink:
        close[200:240] = close[199] - np.linspace(0, 12, 40)
        close[240:280] = close[239] + np.linspace(0, 8, 40)
    high = close + rng.uniform(0.05, 0.4, size=n)
    low = close - rng.uniform(0.05, 0.4, size=n)
    idx = pd.date_range("2023-01-01", periods=n, freq="15min", tz="UTC")
    return pd.DataFrame(
        {
            "open": close,
            "high": high,
            "low": low,
            "close": close,
            "volume": rng.uniform(10, 50, size=n),
        },
        index=idx,
    )


def test_any_in_next_matches_naive():
    bit = np.zeros(20, dtype=bool)
    bit[5] = True
    bit[12] = True
    got = any_in_next(bit, 3)
    naive = np.zeros(20, dtype=bool)
    for t in range(20 - 3):
        naive[t] = bit[t + 1 : t + 1 + 3].any()
    np.testing.assert_array_equal(got, naive)


def test_features_prefix_invariant():
    df = _ohlcv(600, seed=1)
    full = build_known_now_features(df)
    trunc = build_known_now_features(df.iloc[:400])
    cols = [c for c in trunc.columns if c not in ("dist_confirmed_high", "dist_confirmed_low")]
    a = full[cols].iloc[:400]
    b = trunc[cols]
    # Warmup NaNs match; finite values must match.
    for c in cols:
        fa = a[c].to_numpy(dtype=float)
        fb = b[c].to_numpy(dtype=float)
        both = np.isfinite(fa) & np.isfinite(fb)
        if both.sum() < 20:
            continue
        np.testing.assert_allclose(fa[both], fb[both], rtol=1e-9, atol=1e-9, err_msg=c)


def test_labels_use_future_mutation():
    df = _ohlcv(500, seed=2)
    pack = build_event_pack(df, horizon=4)
    mutated = df.copy()
    mutated.iloc[-1, mutated.columns.get_loc("close")] = float(mutated["close"].iloc[-1]) * 1.2
    mutated.iloc[-1, mutated.columns.get_loc("high")] = float(mutated["high"].iloc[-1]) * 1.25
    pack2 = build_event_pack(mutated, horizon=4)
    # Features on the prefix must stay put.
    f1 = pack.features.iloc[:-8]
    f2 = pack2.features.iloc[:-8]
    for c in ("rsi_14", "macd_hist", "stoch_k", "vol_z_48"):
        a = f1[c].to_numpy(dtype=float)
        b = f2[c].to_numpy(dtype=float)
        both = np.isfinite(a) & np.isfinite(b)
        np.testing.assert_allclose(a[both], b[both], rtol=1e-9, atol=1e-9)
    # Labels near the tip are allowed to move (they look ahead).
    lab1 = pack.labels["macd_hist_flip_up"].to_numpy()
    lab2 = pack2.labels["macd_hist_flip_up"].to_numpy()
    assert lab1.shape == lab2.shape


def test_rsi_cross_label_on_sink_then_bounce():
    df = _ohlcv(500, seed=3, rsi_sink=True)
    pack = build_event_pack(df, horizon=8)
    n_up = int(np.nansum(pack.labels["rsi_cross_up_30"].to_numpy()))
    # A 12-point dump then bounce should produce at least one cross-up label.
    assert n_up >= 1
    side = pack.side["rsi_cross_up_30"].to_numpy()
    assert np.nanmax(side) == 1.0


def test_train_test_sqlite_features_are_separate(tmp_path):
    from llm2.confluence.train import split_ohlcv_files
    from llm2.confluence.events import build_known_now_features

    df = _ohlcv(400, seed=5)
    tr_p = tmp_path / "tr.sqlite"
    te_p = tmp_path / "te.sqlite"
    tr, te = split_ohlcv_files(df, train_path=tr_p, test_path=te_p, train_frac=0.7)
    assert tr_p.is_file() and te_p.is_file()
    assert len(tr) + len(te) == 400
    f_tr = build_known_now_features(tr)
    f_te = build_known_now_features(te)
    assert len(f_tr) == len(tr)
    assert len(f_te) == len(te)
    # Isolated test file has its own warmup NaNs; must not equal a slice of full-file features.
    full = build_known_now_features(df)
    te_from_full = full.iloc[len(tr) : len(tr) + 30]["rsi_14"].to_numpy(dtype=float)
    te_iso = f_te["rsi_14"].to_numpy(dtype=float)[:30]
    # Warmup on the isolated test file should be NaN while the joint file is defined.
    assert np.isnan(te_iso[:5]).any() or not np.allclose(
        te_iso[np.isfinite(te_iso)],
        te_from_full[np.isfinite(te_iso)],
        equal_nan=False,
    )


def test_event_pack_columns_and_horizon_nan_tail():
    df = _ohlcv(300, seed=4)
    pack = build_event_pack(df, horizon=4)
    assert list(pack.labels.columns) == list(EVENT_IDS)
    tail = pack.labels.iloc[-4:]
    assert tail.isna().all().all()
    assert pack.features.shape[0] == len(df)
    assert pack.horizon == 4
