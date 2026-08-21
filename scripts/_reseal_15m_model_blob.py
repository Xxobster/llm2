"""Rewrite 15m pack model.joblib as {model, feature_columns, ...} and reseal hash."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import joblib

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from llm2.live.certificate import load_certificate, pack_fingerprint  # noqa: E402

DST = _ROOT / "artifacts" / "live_packs" / "structure_v1_ethusdt_15m_multitrade_wall_clock_p75_v1"
CERT = (
    _ROOT
    / "configs"
    / "live"
    / "structure_v1_ethusdt_15m_multitrade_wall_clock_p75_v1_certificate.yaml"
)


def main() -> int:
    strat = json.loads((DST / "strategy.json").read_text(encoding="utf-8"))
    raw = joblib.load(DST / "model.joblib")
    model = raw["model"] if isinstance(raw, dict) and "model" in raw else raw
    blob = {
        "model": model,
        "feature_columns": list(strat["feature_columns"]),
        "model_name": "lgbm_regressor",
        "trained_until": strat.get("trained_until_exclusive"),
        "n_train": None,
        "symbol": strat["symbol"],
        "target": strat.get("target", "direction"),
    }
    joblib.dump(blob, DST / "model.joblib")
    for name in ("certificate.yaml", "pack_hash.txt"):
        p = DST / name
        if p.is_file():
            p.unlink()
    fp = pack_fingerprint(DST)
    if not fp:
        raise RuntimeError("fingerprint failed")
    (DST / "pack_hash.txt").write_text(fp + "\n", encoding="utf-8", newline="\n")
    text = CERT.read_text(encoding="utf-8")
    CERT.write_text(
        re.sub(r"pack_hash:.*", f"pack_hash: {fp}", text),
        encoding="utf-8",
        newline="\n",
    )
    cert = load_certificate(CERT)
    if not cert.is_deployable or cert.pack_hash != fp:
        raise RuntimeError("cert seal failed")
    print(json.dumps({"pack_hash": fp, "n_cols": len(blob["feature_columns"])}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
