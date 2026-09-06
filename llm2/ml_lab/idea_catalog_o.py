"""Hunt 018 causal ideas: more textbook oscillators (not a 016/017 retune).

Every signal is +1 / 0 / −1 from completed bars only. Thresholds are module
constants, not searched on profit factor.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from llm2.autonomy.public_formulas import (
    awesome_oscillator,
    chande_momentum,
    demarker,
    ehlers_fisher,
    force_index,
    mass_index,
    trix_line,
    ultimate_oscillator,
)
from llm2.ml_lab.causal_math import bar_return, sign_nz

UO_HI = 70.0
UO_LO = 30.0
DEM_HI = 0.70
DEM_LO = 0.30
CMO_HI = 50.0
CMO_LO = -50.0
FISH_HI = 2.0
FISH_LO = -2.0
MASS_BULGE = 27.0
MASS_SETUP = 26.5
MASS_LOOK = 25
MASS_FADE_N = 9

IDEA_IDS_O: tuple[str, ...] = (
    "ultimate_osc_fade",
    "trix_sign_follow",
    "force_index_flip",
    "demarker_fade",
    "chande_mom_fade",
    "ehlers_fisher_fade",
    "awesome_osc_flip",
    "mass_index_revert",
)


def _sign_flip(x: np.ndarray) -> np.ndarray:
    prev = np.roll(x, 1)
    prev[0] = np.nan
    out = np.zeros(x.size, dtype=np.float64)
    flip = np.isfinite(x) & np.isfinite(prev) & (np.sign(x) != np.sign(prev)) & (x != 0)
    out[flip] = sign_nz(x)[flip]
    return out


def ultimate_osc_fade(ohlcv: pd.DataFrame, timeframe: str | None = None) -> np.ndarray:
    """Fade Larry Williams Ultimate Oscillator at 70 / 30."""
    del timeframe
    uo = ultimate_oscillator(
        ohlcv["high"].to_numpy(dtype=float),
        ohlcv["low"].to_numpy(dtype=float),
        ohlcv["close"].to_numpy(dtype=float),
    )
    out = np.zeros(uo.size, dtype=np.float64)
    out[np.isfinite(uo) & (uo >= UO_HI)] = -1.0
    out[np.isfinite(uo) & (uo <= UO_LO)] = 1.0
    return out


def trix_sign_follow(ohlcv: pd.DataFrame, timeframe: str | None = None) -> np.ndarray:
    """Follow a new sign of the triple-smoothed exponential rate of change (TRIX)."""
    del timeframe
    return _sign_flip(trix_line(ohlcv["close"].to_numpy(dtype=float), period=15))


def force_index_flip(ohlcv: pd.DataFrame, timeframe: str | None = None) -> np.ndarray:
    """Follow a new sign of Elder Force Index (13-bar exponential of price change times volume)."""
    del timeframe
    fi = force_index(
        ohlcv["close"].to_numpy(dtype=float),
        ohlcv["volume"].to_numpy(dtype=float),
        period=13,
    )
    return _sign_flip(fi)


def demarker_fade(ohlcv: pd.DataFrame, timeframe: str | None = None) -> np.ndarray:
    """Fade Tom DeMark DeMarker at 0.70 / 0.30."""
    del timeframe
    dm = demarker(
        ohlcv["high"].to_numpy(dtype=float),
        ohlcv["low"].to_numpy(dtype=float),
        period=14,
    )
    out = np.zeros(dm.size, dtype=np.float64)
    out[np.isfinite(dm) & (dm >= DEM_HI)] = -1.0
    out[np.isfinite(dm) & (dm <= DEM_LO)] = 1.0
    return out


def chande_mom_fade(ohlcv: pd.DataFrame, timeframe: str | None = None) -> np.ndarray:
    """Fade Tushar Chande Momentum Oscillator at +50 / −50."""
    del timeframe
    cmo = chande_momentum(ohlcv["close"].to_numpy(dtype=float), period=14)
    out = np.zeros(cmo.size, dtype=np.float64)
    out[np.isfinite(cmo) & (cmo >= CMO_HI)] = -1.0
    out[np.isfinite(cmo) & (cmo <= CMO_LO)] = 1.0
    return out


def ehlers_fisher_fade(ohlcv: pd.DataFrame, timeframe: str | None = None) -> np.ndarray:
    """Fade John Ehlers Fisher Transform of the median price at +2 / −2."""
    del timeframe
    fish = ehlers_fisher(
        ohlcv["high"].to_numpy(dtype=float),
        ohlcv["low"].to_numpy(dtype=float),
        period=10,
    )
    out = np.zeros(fish.size, dtype=np.float64)
    out[np.isfinite(fish) & (fish >= FISH_HI)] = -1.0
    out[np.isfinite(fish) & (fish <= FISH_LO)] = 1.0
    return out


def awesome_osc_flip(ohlcv: pd.DataFrame, timeframe: str | None = None) -> np.ndarray:
    """Follow a new sign of Bill Williams Awesome Oscillator (SMA5 − SMA34 of midpoint)."""
    del timeframe
    ao = awesome_oscillator(
        ohlcv["high"].to_numpy(dtype=float),
        ohlcv["low"].to_numpy(dtype=float),
    )
    return _sign_flip(ao)


def mass_index_revert(ohlcv: pd.DataFrame, timeframe: str | None = None) -> np.ndarray:
    """Fade the 9-bar close move when Dorsey Mass Index drops back through 26.5 after a 27 bulge."""
    del timeframe
    h = ohlcv["high"].to_numpy(dtype=float)
    l = ohlcv["low"].to_numpy(dtype=float)
    c = ohlcv["close"].to_numpy(dtype=float)
    mi = mass_index(h, l, ema_n=9, sum_n=25)
    prev = np.roll(mi, 1)
    prev[0] = np.nan
    had_bulge = (
        pd.Series(np.where(np.isfinite(mi) & (mi >= MASS_BULGE), 1.0, 0.0))
        .rolling(MASS_LOOK, min_periods=1)
        .max()
        .to_numpy(dtype=float)
    )
    drop = np.isfinite(mi) & np.isfinite(prev) & (mi < MASS_SETUP) & (prev >= MASS_SETUP) & (had_bulge >= 1.0)
    past = np.roll(c, MASS_FADE_N)
    past[:MASS_FADE_N] = np.nan
    move = c - past
    out = np.zeros(c.size, dtype=np.float64)
    out[drop & np.isfinite(move)] = -sign_nz(move)[drop & np.isfinite(move)]
    return out


def signals_o(ohlcv: pd.DataFrame, timeframe: str) -> dict[str, np.ndarray]:
    return {
        "ultimate_osc_fade": ultimate_osc_fade(ohlcv, timeframe),
        "trix_sign_follow": trix_sign_follow(ohlcv, timeframe),
        "force_index_flip": force_index_flip(ohlcv, timeframe),
        "demarker_fade": demarker_fade(ohlcv, timeframe),
        "chande_mom_fade": chande_mom_fade(ohlcv, timeframe),
        "ehlers_fisher_fade": ehlers_fisher_fade(ohlcv, timeframe),
        "awesome_osc_flip": awesome_osc_flip(ohlcv, timeframe),
        "mass_index_revert": mass_index_revert(ohlcv, timeframe),
    }


def build_features_for_guard(ohlcv: pd.DataFrame, **kwargs) -> pd.DataFrame:
    """Dense causal state for leakage (not the sparse ±1 fires)."""
    del kwargs
    h = ohlcv["high"].to_numpy(dtype=float)
    l = ohlcv["low"].to_numpy(dtype=float)
    c = ohlcv["close"].to_numpy(dtype=float)
    v = ohlcv["volume"].to_numpy(dtype=float)
    return pd.DataFrame(
        {
            "bar_return": bar_return(c),
            "ultimate_osc": ultimate_oscillator(h, l, c),
            "trix": trix_line(c, period=15),
            "force_index": force_index(c, v, period=13),
            "demarker": demarker(h, l, period=14),
            "chande_mom": chande_momentum(c, period=14),
            "ehlers_fisher": ehlers_fisher(h, l, period=10),
            "mass_index": mass_index(h, l, ema_n=9, sum_n=25),
        },
        index=ohlcv.index,
    )
