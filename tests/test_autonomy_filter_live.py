"""Autonomy predicted-filter live path (pivot control AND P(event) >= pi*)."""

from __future__ import annotations

from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from sklearn.dummy import DummyClassifier

from llm2.autonomy.filter_head import predict_filter_proba, score_filter_tip
from llm2.gates.evidence import leverage_from_stop
from llm2.live.pivot_runner import load_pack, tip_decide
from llm2.pivot.strategy.ev import net_bracket_magnitudes


def _ohlcv(n: int = 80) -> pd.DataFrame:
    idx = pd.date_range("2024-01-01", periods=n, freq="15min", tz="UTC")
    close = 100.0 + np.linspace(0.0, 2.0, n)
    return pd.DataFrame(
        {
            "open": close,
            "high": close + 0.3,
            "low": close - 0.3,
            "close": close,
            "volume": np.full(n, 10.0),
        },
        index=idx,
    )


def test_leverage_1pct_is_29x() -> None:
    assert leverage_from_stop(0.01) == 29.0


def test_pi_star_1pct_bracket() -> None:
    mag = net_bracket_magnitudes(0.01, 0.01)
    assert 0.53 < mag.pi_star < 0.55


def test_predict_filter_proba_clips() -> None:
    x = np.array([[0.0], [1.0]])
    y = np.array([0, 1])
    model = DummyClassifier(strategy="constant", constant=1)
    model.fit(x, y)
    p = predict_filter_proba(model, None, np.array([[0.2]]))
    assert p.shape == (1,)
    assert 0.0 < float(p[0]) <= 1.0


def test_score_filter_tip_refuses_nan(monkeypatch) -> None:
    def _fake(_ohlcv):
        return pd.DataFrame({"a": [1.0, np.nan]}, index=_ohlcv.index[-2:])

    import llm2.autonomy.filter_head as fh

    monkeypatch.setattr(fh, "build_features_for_guard", _fake)
    model = DummyClassifier(strategy="constant", constant=1)
    model.fit(np.array([[0.0], [1.0]]), np.array([0, 1]))
    out = score_filter_tip(_ohlcv(5), feature_columns=["a"], model=model, iso=None)
    assert out["ok"] is False
    assert out["reason"] == "nan_features"
    assert "a" in out["nan_cols"]


def test_load_pack_merges_filter_head(tmp_path: Path) -> None:
    model = DummyClassifier(strategy="constant", constant=1)
    model.fit(np.array([[0.0], [1.0]]), np.array([0, 1]))
    (tmp_path / "strategy.json").write_text(
        '{"symbol":"SOLUSDT","timeframe":"15m","feature_pack":"level_vsa",'
        '"tp_pct":0.01,"sl_pct":0.01,"work_bars":5,"max_hold_bars":6,'
        '"leverage":29.0,"arm_id":"t","filter":{"event":"sma540_below_at_h"}}',
        encoding="utf-8",
    )
    joblib.dump({"any_model": model, "cal_any": None, "thr_any": 0.35, "feature_columns": ["x"]}, tmp_path / "model.joblib")
    joblib.dump({"model": model, "iso": None, "feature_columns": ["a"], "pi_star": 0.5375}, tmp_path / "filter_head.joblib")
    strat, blob = load_pack(tmp_path)
    assert strat["filter"]["event"] == "sma540_below_at_h"
    assert blob["filter_head"]["pi_star"] == 0.5375


def test_tip_decide_filter_blocks_when_below_pi_star(monkeypatch) -> None:
    n = 80
    ohlcv = _ohlcv(n)
    cols = ["c0"]
    feats = pd.DataFrame({"c0": np.ones(n)}, index=ohlcv.index)
    monkeypatch.setattr("llm2.live.pivot_runner.build_feature_frame", lambda *_a, **_k: feats)

    class _Any:
        def predict_proba(self, x):  # noqa: ANN001
            return np.array([[0.1, 0.9]])

    blob = {
        "feature_columns": cols,
        "any_model": _Any(),
        "cal_any": ("identity", None),
        "thr_any": 0.35,
        "high_model": None,
        "level_model": None,
        "filter_head": {
            "model": object(),
            "iso": None,
            "feature_columns": ["a"],
            "pi_star": 0.5375,
        },
    }
    monkeypatch.setattr(
        "llm2.autonomy.filter_head.score_filter_tip",
        lambda *_a, **_k: {"ok": True, "reason": "scored", "nan_cols": [], "p_event": 0.40},
    )
    strat = {
        "symbol": "SOLUSDT",
        "timeframe": "15m",
        "feature_pack": "level_vsa",
        "tp_pct": 0.01,
        "sl_pct": 0.01,
        "work_bars": 5,
        "max_hold_bars": 6,
        "leverage": 29.0,
        "arm_id": "t",
        "level_mode": "ret",
        "limit_level": "atr_clip",
        "filter": {
            "generation": "376",
            "event": "sma540_below_at_h",
            "horizon_bars": 4,
            "pi_star": 0.5375,
        },
    }
    dec = tip_decide(ohlcv=ohlcv, strategy=strat, blob=blob)
    assert dec["action"] == "FLAT"
    assert dec["reason"] == "filter_below_pi_star"
    assert dec["p_any"] >= 0.35
    assert dec["filter"]["passed"] is False


def test_tip_decide_filter_enters_when_both_pass(monkeypatch) -> None:
    n = 80
    ohlcv = _ohlcv(n)
    cols = ["c0"]
    feats = pd.DataFrame({"c0": np.ones(n)}, index=ohlcv.index)
    monkeypatch.setattr("llm2.live.pivot_runner.build_feature_frame", lambda *_a, **_k: feats)

    class _Any:
        def predict_proba(self, x):  # noqa: ANN001
            return np.array([[0.1, 0.9]])

    blob = {
        "feature_columns": cols,
        "any_model": _Any(),
        "cal_any": ("identity", None),
        "thr_any": 0.35,
        "high_model": None,
        "level_model": None,
        "filter_head": {"model": object(), "iso": None, "feature_columns": ["a"]},
    }
    monkeypatch.setattr(
        "llm2.autonomy.filter_head.score_filter_tip",
        lambda *_a, **_k: {"ok": True, "reason": "scored", "nan_cols": [], "p_event": 0.70},
    )
    strat = {
        "symbol": "ETHUSDT",
        "timeframe": "15m",
        "feature_pack": "level_vsa",
        "tp_pct": 0.01,
        "sl_pct": 0.01,
        "work_bars": 4,
        "max_hold_bars": 6,
        "leverage": 29.0,
        "arm_id": "t",
        "level_mode": "atr",
        "filter": {
            "generation": "705",
            "event": "ema1320_below_at_h",
            "horizon_bars": 4,
            "pi_star": 0.5375,
        },
    }
    dec = tip_decide(ohlcv=ohlcv, strategy=strat, blob=blob)
    assert dec["action"] == "ENTER_LIMIT"
    assert dec["reason"] == "p75_and_filter"
    assert dec["filter"]["passed"] is True
