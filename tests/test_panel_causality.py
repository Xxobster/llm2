"""Confirmation-time / truncation audits for peer-panel feature spaces.

``crosspair_v1`` and ``xs_v1`` load peer closes from the warehouse. A green leakage report
on the traded symbol's OHLCV does not prove those peer columns are causal: truncating the
traded series leaves the peer database untouched. These tests rebuild the panel from
truncated peer histories and require the values through the cutoff to match.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from llm2.data.loader import load_ohlcv
from llm2.data.panel import build_close_panel, clear_panel_cache
from llm2.features.crosspair_v1 import build_crosspair_v1
from llm2.features.xs_v1 import build_xs_v1


@pytest.fixture(autouse=True)
def _clear_cache():
    clear_panel_cache()
    yield
    clear_panel_cache()


def test_close_panel_truncation_is_prefix_invariant():
    """Values through a cutoff must not depend on peer bars after the cutoff."""
    symbols = ["BTCUSDT", "ETHUSDT", "SOLUSDT"]
    tf = "1h"
    full = build_close_panel(symbols, tf)
    assert len(full) > 5000

    cut = full.index[len(full) // 2]
    clear_panel_cache()

    # Rebuild each peer from OHLCV truncated at the cutoff, then form the panel by hand.
    truncated = {}
    for sym in symbols:
        raw = load_ohlcv(sym, tf)
        truncated[sym] = raw.loc[:cut, "close"].rename(sym)
    hand = pd.concat(truncated.values(), axis=1).sort_index().ffill()

    common = full.loc[:cut].dropna(how="all").index.intersection(hand.dropna(how="all").index)
    # Skip the first day of warm-up where ffill may still be empty on one side.
    common = common[24:]
    a = full.loc[common]
    b = hand.loc[common]
    delta = (a - b).abs().to_numpy()
    assert np.nanmax(delta) < 1e-9, "peer panel at the cutoff saw future peer bars"


def test_crosspair_features_are_stable_under_peer_truncation():
    ohlcv = load_ohlcv("BTCUSDT", "1h").iloc[:8000]
    cut = ohlcv.index[6000]
    head = ohlcv.loc[:cut]

    clear_panel_cache()
    full_feats = build_crosspair_v1(ohlcv, symbol="BTCUSDT")
    clear_panel_cache()
    head_feats = build_crosspair_v1(head, symbol="BTCUSDT")

    common = head_feats.dropna(how="all").index.intersection(
        full_feats.loc[:cut].dropna(how="all").index
    )[100:]
    a = head_feats.loc[common]
    b = full_feats.loc[common]
    # Columns present in both (peer coverage can differ only after the cut).
    cols = [c for c in a.columns if c in b.columns]
    delta = (a[cols] - b[cols]).abs().to_numpy()
    assert np.nanmax(delta) < 1e-9


def test_xs_features_are_stable_under_peer_truncation():
    ohlcv = load_ohlcv("BTCUSDT", "1h").iloc[:8000]
    cut = ohlcv.index[6000]
    head = ohlcv.loc[:cut]
    peers = ["BTCUSDT", "ETHUSDT", "SOLUSDT", "BNBUSDT"]

    clear_panel_cache()
    full_feats = build_xs_v1(ohlcv, symbol="BTCUSDT", symbols=peers)
    clear_panel_cache()
    head_feats = build_xs_v1(head, symbol="BTCUSDT", symbols=peers)

    common = head_feats.dropna(how="all").index.intersection(
        full_feats.loc[:cut].dropna(how="all").index
    )[150:]
    a = head_feats.loc[common]
    b = full_feats.loc[common]
    cols = [c for c in a.columns if c in b.columns]
    delta = (a[cols] - b[cols]).abs().to_numpy()
    assert np.nanmax(delta) < 1e-9
