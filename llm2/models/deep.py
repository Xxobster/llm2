"""Deep learning predictors — neuralforecast optional; local torch MLP always available."""

from __future__ import annotations

import numpy as np

from llm2.models.base import Prediction

_NEURALFORECAST_AVAILABLE = False
try:
    import neuralforecast  # noqa: F401

    _NEURALFORECAST_AVAILABLE = True
except Exception:  # noqa: BLE001 — version conflicts should not break import
    pass

_TORCH_AVAILABLE = False
try:
    import torch
    import torch.nn as nn

    _TORCH_AVAILABLE = True
except ImportError:
    pass


def neuralforecast_available() -> bool:
    return _NEURALFORECAST_AVAILABLE


def torch_available() -> bool:
    return _TORCH_AVAILABLE


class TorchMLPPredictor:
    """Small multilayer perceptron for tabular lagged features (GPU if available)."""

    name = "torch_mlp"

    def __init__(
        self,
        hidden: int = 64,
        epochs: int = 20,
        lr: float = 1e-3,
        batch_size: int = 512,
    ) -> None:
        if not _TORCH_AVAILABLE:
            raise ImportError("torch required")
        self.hidden = hidden
        self.epochs = epochs
        self.lr = lr
        self.batch_size = batch_size
        self._model: nn.Module | None = None
        self._device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    def fit(self, X: np.ndarray, y: np.ndarray) -> "TorchMLPPredictor":
        mask = np.isfinite(y) & np.all(np.isfinite(X), axis=1)
        Xs = X[mask].astype(np.float32)
        ys = y[mask].astype(np.float32)
        if len(Xs) < 50:
            self._mean = float(np.nanmean(y))
            self._model = None
            return self
        self._mean = float(ys.mean())
        self._std_x = Xs.std(axis=0) + 1e-6
        self._mean_x = Xs.mean(axis=0)
        Xs_n = (Xs - self._mean_x) / self._std_x

        in_dim = Xs_n.shape[1]
        hidden = self.hidden

        class MLP(nn.Module):
            def __init__(self, in_features: int, hidden_dim: int) -> None:
                super().__init__()
                self.net = nn.Sequential(
                    nn.Linear(in_features, hidden_dim),
                    nn.ReLU(),
                    nn.Linear(hidden_dim, hidden_dim),
                    nn.ReLU(),
                    nn.Linear(hidden_dim, 1),
                )

            def forward(self, x):  # noqa: ANN001
                return self.net(x).squeeze(-1)

        model = MLP(in_dim, hidden).to(self._device)
        opt = torch.optim.Adam(model.parameters(), lr=self.lr)
        loss_fn = nn.MSELoss()
        xt = torch.from_numpy(Xs_n).to(self._device)
        yt = torch.from_numpy(ys).to(self._device)
        n = len(xt)
        model.train()
        for _ in range(self.epochs):
            perm = torch.randperm(n, device=self._device)
            for start in range(0, n, self.batch_size):
                idx = perm[start : start + self.batch_size]
                pred = model(xt[idx])
                loss = loss_fn(pred, yt[idx])
                opt.zero_grad()
                loss.backward()
                opt.step()
        model.eval()
        self._model = model
        return self

    def predict(self, X: np.ndarray) -> Prediction:
        if self._model is None:
            arr = np.full(len(X), getattr(self, "_mean", 0.0), dtype=float)
            return Prediction(mean=arr, q50=arr)
        import torch

        Xs = np.nan_to_num(X.astype(np.float32), nan=0.0)
        Xs_n = (Xs - self._mean_x) / self._std_x
        with torch.no_grad():
            pred = self._model(torch.from_numpy(Xs_n).to(self._device)).cpu().numpy()
        return Prediction(mean=pred.astype(float), q50=pred.astype(float))


class NeuralForecastPredictor:
    name = "neuralforecast"
    available = _NEURALFORECAST_AVAILABLE

    def __init__(self, model_name: str = "NHITS", horizon: int = 1) -> None:
        if not self.available:
            raise ImportError("neuralforecast optional dependency not installed/compatible")
        self.model_name = model_name
        self.horizon = horizon
        self._fitted = False

    def fit(self, X: np.ndarray, y: np.ndarray) -> "NeuralForecastPredictor":
        # Fallback mean until a dedicated NF panel adapter is wired per series
        _ = X
        self._fitted = True
        self._mean = float(np.nanmean(y))
        return self

    def predict(self, X: np.ndarray) -> Prediction:
        if not self._fitted:
            raise RuntimeError("Model not fit")
        arr = np.full(len(X), getattr(self, "_mean", 0.0), dtype=float)
        return Prediction(mean=arr, q50=arr)


class PatchTSTLitePredictor(TorchMLPPredictor):
    """Alias: until full PatchTST is wired, use the torch MLP on lagged features."""

    name = "patchtst_lite"
