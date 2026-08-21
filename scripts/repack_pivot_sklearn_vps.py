"""Re-serialize pivot tip packs under the runtime scikit-learn (VPS 1.7.2).

Loads model.joblib, rebuilds LabelEncoder / IsotonicRegression with the current
sklearn, dumps again, refreshes pack_hash + live certificate pack_hash.
Does not retrain trees. Run on the VPS that serves live.
"""

from __future__ import annotations

import json
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

import joblib
import numpy as np
import sklearn
from sklearn.isotonic import IsotonicRegression
from sklearn.preprocessing import LabelEncoder

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from llm2.live.certificate import pack_fingerprint  # noqa: E402

PACKS = (
    Path("/opt/llm2-pivot-sol-geo-p75-w4/pack"),
    Path("/opt/llm2-pivot-eth-p75-ctrl-atr-w4/pack"),
)
CERTS = {
    "pivot_sol_geo_tp1_sl1_p75_w4": Path(
        "/opt/llm2-pivot-sol-geo-p75-w4/certificate.yaml"
    ),
    "pivot_eth_p75_ctrl_atr_w4": Path(
        "/opt/llm2-pivot-eth-p75-ctrl-atr-w4/certificate.yaml"
    ),
}


def _rebuild_label_encoder(old: LabelEncoder) -> LabelEncoder:
    new = LabelEncoder()
    classes = np.asarray(getattr(old, "classes_"))
    new.fit(classes)
    return new


def _rebuild_isotonic(old: IsotonicRegression) -> IsotonicRegression:
    x = np.asarray(getattr(old, "X_thresholds_"), dtype=float)
    y = np.asarray(getattr(old, "y_thresholds_"), dtype=float)
    out_of_bounds = getattr(old, "out_of_bounds", "clip")
    increasing = bool(getattr(old, "increasing_", True))
    y_min = getattr(old, "y_min", 0.0)
    y_max = getattr(old, "y_max", 1.0)
    new = IsotonicRegression(
        increasing=increasing,
        out_of_bounds=out_of_bounds,
        y_min=y_min,
        y_max=y_max,
    )
    new.fit(x, y)
    return new


def _rebuild_calibrator(obj):
    if isinstance(obj, IsotonicRegression):
        return _rebuild_isotonic(obj)
    if isinstance(obj, LabelEncoder):
        return _rebuild_label_encoder(obj)
    if isinstance(obj, tuple) and len(obj) == 2 and isinstance(obj[0], str):
        kind, model = obj
        return (kind, _rebuild_calibrator(model))
    if isinstance(obj, dict):
        return {k: _rebuild_calibrator(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [_rebuild_calibrator(v) for v in obj]
    return obj


def _update_cert(path: Path, pack_hash: str) -> None:
    import yaml

    raw = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    raw["pack_hash"] = pack_hash
    raw["notes"] = (
        str(raw.get("notes") or "")
        + f"\nsklearn_repack utc={datetime.now(timezone.utc).isoformat()} "
        f"sklearn={sklearn.__version__}"
    ).strip()
    path.write_text(yaml.safe_dump(raw, sort_keys=False), encoding="utf-8")


def _rebuild_lgbm_label_encoder(model) -> None:
    le = getattr(model, "_le", None)
    if isinstance(le, LabelEncoder):
        model._le = _rebuild_label_encoder(le)


def repack(pack: Path) -> str:
    model_path = pack / "model.joblib"
    bak = pack / f"model.joblib.bak_pre_sklearn_{sklearn.__version__}"
    if not bak.is_file():
        shutil.copy2(model_path, bak)
    blob = joblib.load(model_path)
    rebuilt = _rebuild_calibrator(blob)
    if isinstance(rebuilt, dict):
        for key in ("cal_any", "cal_high", "any_model", "high_model", "level_model"):
            if key not in rebuilt:
                continue
            if key in ("cal_any", "cal_high"):
                rebuilt[key] = _rebuild_calibrator(rebuilt[key])
            else:
                _rebuild_lgbm_label_encoder(rebuilt[key])
    joblib.dump(rebuilt, model_path)
    fp = pack_fingerprint(pack)
    assert fp
    (pack / "pack_hash.txt").write_text(fp + "\n", encoding="utf-8")
    meta_path = pack / "pack_meta.json"
    if meta_path.is_file():
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
        meta["pack_hash"] = fp
        meta["sklearn_runtime"] = sklearn.__version__
        meta["sklearn_repacked_utc"] = datetime.now(timezone.utc).strftime(
            "%Y-%m-%dT%H:%M:%SZ"
        )
        meta_path.write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")
        fp = pack_fingerprint(pack)
        assert fp
        meta["pack_hash"] = fp
        meta_path.write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")
        (pack / "pack_hash.txt").write_text(fp + "\n", encoding="utf-8")
    name = pack.parent.name.replace("llm2-", "").replace("-", "_")
    # map unit dir → cert
    if "sol" in pack.parent.name:
        _update_cert(CERTS["pivot_sol_geo_tp1_sl1_p75_w4"], fp)
    else:
        _update_cert(CERTS["pivot_eth_p75_ctrl_atr_w4"], fp)
    print(json.dumps({"pack": str(pack), "hash": fp, "sklearn": sklearn.__version__}))
    return fp


def main() -> int:
    print("sklearn", sklearn.__version__)
    for pack in PACKS:
        repack(pack)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
