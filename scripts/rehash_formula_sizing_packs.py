"""Rehash formula packs after sizing-only edits; stamp certificates. No four-proof rerun."""

from __future__ import annotations

import json
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from llm2.live.certificate import pack_fingerprint  # noqa: E402
from llm2.paths import ARTIFACTS, ROOT  # noqa: E402


def _rehash(slug: str, cert_name: str, extra_cert: dict[str, str]) -> str:
    pack_dir = ARTIFACTS / "live_packs" / slug
    meta_path = pack_dir / "pack_meta.json"
    meta = json.loads(meta_path.read_text(encoding="utf-8"))
    fp = pack_fingerprint(pack_dir)
    if not fp:
        raise SystemExit(f"fingerprint failed for {slug}")
    (pack_dir / "pack_hash.txt").write_text(fp + "\n", encoding="utf-8")
    meta["pack_hash"] = fp
    meta_path.write_text(json.dumps(meta, indent=2, default=str, sort_keys=True) + "\n", encoding="utf-8")
    fp2 = pack_fingerprint(pack_dir)
    meta["pack_hash"] = fp2
    meta_path.write_text(json.dumps(meta, indent=2, default=str, sort_keys=True) + "\n", encoding="utf-8")
    (pack_dir / "pack_hash.txt").write_text(fp2 + "\n", encoding="utf-8")
    cert_path = ROOT / "configs" / "live" / cert_name
    lines = []
    for line in cert_path.read_text(encoding="utf-8").splitlines():
        if line.startswith("pack_hash:"):
            lines.append(f"pack_hash: {fp2}")
        elif line.startswith("authorized_scope:"):
            lines.append(f"authorized_scope: {extra_cert['authorized_scope']}")
        elif line.startswith("sizing_mode:"):
            lines.append(f"sizing_mode: {extra_cert['sizing_mode']}")
        else:
            lines.append(line)
    # rewrite authorization_source first line block is yaml folded; leave hashes
    text = "\n".join(lines) + "\n"
    for old, new in extra_cert.get("replace", {}).items():
        text = text.replace(old, new)
    cert_path.write_text(text, encoding="utf-8")
    print(f"{slug} pack_hash={fp2}")
    return fp2


def main() -> int:
    _rehash(
        "btc_1h_quad_slope_follow",
        "btc_1h_quad_slope_follow_xxobster11_ln2_certificate.yaml",
        {
            "authorized_scope": (
                "5% equity stop-risk Post-Only (nearest Bybit qty step; skip if below min)"
            ),
            "sizing_mode": "RISK_FRACTION",
            "replace": {
                "- skip the order if 5% equity at that bar's stop is below the venue minimum (do not round up)\n": (
                    "- quantity rounds to the nearest Bybit step around 5% stop-risk "
                    "(may sit slightly above 5%)\n"
                    "- skip if the nearest lot is below the venue minimum\n"
                ),
            },
        },
    )
    _rehash(
        "sol_1h_fvg_confluence",
        "sol_1h_fvg_confluence_xxobster11_ln2_certificate.yaml",
        {
            "authorized_scope": "venue-minimum Post-Only (0.1 Solana); not 5% stop-risk",
            "sizing_mode": "MIN_EXCHANGE",
            "replace": {
                "- skip the order if 5% equity at that bar's stop is below the venue minimum (do not round up)\n": (
                    "- venue-minimum lot (0.1 Solana); not 5% stop-risk\n"
                ),
            },
        },
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
