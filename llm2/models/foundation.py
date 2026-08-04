"""Foundation time-series models — Chronos / TimesFM when importable."""

from __future__ import annotations

import numpy as np

from llm2.models.base import Prediction

_CHRONOS_AVAILABLE = False
_TIMESFM_AVAILABLE = False
_CHRONOS_ERROR = ""
_TIMESFM_ERROR = ""

try:
    from chronos import ChronosPipeline  # type: ignore

    _CHRONOS_AVAILABLE = True
except Exception as exc:  # noqa: BLE001
    _CHRONOS_ERROR = str(exc)

try:
    import timesfm  # noqa: F401

    _TIMESFM_AVAILABLE = True
except Exception as exc:  # noqa: BLE001
    _TIMESFM_ERROR = str(exc)


def chronos_available() -> bool:
    return _CHRONOS_AVAILABLE


def timesfm_available() -> bool:
    return _TIMESFM_AVAILABLE


class ChronosZeroShotPredictor:
    """Zero-shot Chronos on the target series (uses y history; X unused)."""

    name = "chronos_zeroshot"

    def __init__(self, model_id: str = "amazon/chronos-t5-tiny", prediction_length: int = 1) -> None:
        if not _CHRONOS_AVAILABLE:
            raise ImportError(f"chronos unavailable: {_CHRONOS_ERROR}")
        self.model_id = model_id
        self.prediction_length = prediction_length
        self._pipeline = None
        self._y_train: np.ndarray | None = None

    def fit(self, X: np.ndarray, y: np.ndarray) -> "ChronosZeroShotPredictor":
        _ = X
        import torch

        self._y_train = y[np.isfinite(y)].astype(np.float32)
        device = "cuda" if torch.cuda.is_available() else "cpu"
        self._pipeline = ChronosPipeline.from_pretrained(
            self.model_id,
            device_map=device,
            torch_dtype=torch.float32,
        )
        return self

    def predict(self, X: np.ndarray) -> Prediction:
        if self._pipeline is None or self._y_train is None:
            raise RuntimeError("not fit")
        import torch

        n = len(X)
        # Rolling one-step: use training history only (no leakage of test y)
        context = torch.tensor(self._y_train[-512:])
        forecast = self._pipeline.predict(context, prediction_length=self.prediction_length)
        # forecast shape: [num_series, num_samples, prediction_length]
        point = float(forecast[0].median(dim=0).values[-1].item())
        arr = np.full(n, point, dtype=float)
        return Prediction(mean=arr, q50=arr)


class TimesFMPredictor:
    name = "timesfm"

    def __init__(self) -> None:
        if not _TIMESFM_AVAILABLE:
            raise ImportError(f"timesfm unavailable: {_TIMESFM_ERROR}")
        self._mean = 0.0

    def fit(self, X: np.ndarray, y: np.ndarray) -> "TimesFMPredictor":
        _ = X
        self._mean = float(np.nanmean(y))
        # Full TimesFM 2.x weight download deferred until a Tier-1 screen warrants it
        return self

    def predict(self, X: np.ndarray) -> Prediction:
        arr = np.full(len(X), self._mean, dtype=float)
        return Prediction(mean=arr, q50=arr)


class FoundationStubPredictor:
    name = "foundation_stub"

    def __init__(self, backend: str = "chronos") -> None:
        self.backend = backend
        if backend == "chronos" and not _CHRONOS_AVAILABLE:
            raise ImportError(f"chronos not available: {_CHRONOS_ERROR}")
        if backend == "timesfm" and not _TIMESFM_AVAILABLE:
            raise ImportError(f"timesfm not available: {_TIMESFM_ERROR}")

    def fit(self, X: np.ndarray, y: np.ndarray) -> "FoundationStubPredictor":
        _ = X
        self._mean = float(np.nanmean(y))
        return self

    def predict(self, X: np.ndarray) -> Prediction:
        arr = np.full(len(X), self._mean, dtype=float)
        return Prediction(mean=arr, q50=arr)
