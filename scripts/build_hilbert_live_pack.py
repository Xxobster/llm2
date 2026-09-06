"""Freeze Solana 1-hour Hilbert always-fade live pack + four-proof + certificate.

Readiness remains RESEARCH_ONLY. Nested 2022–2026 settle is a subset PASS
(not Shadow-Ready). User-authorized 5% equity stop-risk Post-Only test on
live-network-1 (94.156.189.76), account Xxobster3.

    python -u scripts/build_hilbert_live_pack.py --authorize
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))
sys.path.insert(0, str(_ROOT / "scripts"))

from build_formula_live_packs import SOL_INSTRUMENT, _write_pack  # noqa: E402
from llm2.ml_lab.live_guards import SOL_HILBERT_AMP_FADE_SPEC  # noqa: E402
from llm2.sizing_policy import DEFAULT_STOP_RISK_FRACTION, SIZING_MODE_RISK_FRACTION  # noqa: E402


def build(args: argparse.Namespace) -> int:
    auth_src = (
        "user chat 2026-09-04: find a free Xxobster account and run Solana 1h "
        "hilbert_amp_fade on vps 94.x (94.156.189.76); 5% of equity as risk at "
        "that bar's stop (nearest venue step, not the exchange minimum lot); "
        "Post-Only; adapt bots start, leverage 13x"
    )
    blockers = [
        (
            "nested stitched 2022-01-01..2026-05-01 subset PASS "
            "(n=726, ~14.0/month, profit factor 1.266, Sharpe 1.242, "
            "Heteroskedasticity-and-Autocorrelation-Consistent Sharpe 1.322, "
            "entry-bar 0.088, 6/6 positive folds) — operational fill-test only; "
            "not Shadow-Ready"
        ),
        "no Deflated Sharpe / dependence-aware bootstrap / Probability of Backtest Overfitting on this pack",
        "no Gate C all-taker stress on this pack",
        "lockbox 2026-05-01+ still sealed",
        "unfilled Post-Only cancels and stays flat",
        "skip the order if 5% equity at that bar's stop is below the venue minimum (do not round up)",
        "two-sided: fade signed 3-bar return when Hilbert envelope z >= 1.5",
        "nested subset PASS is not a Frozen Default Gates V2.1 overall PASS",
    ]
    _write_pack(
        spec=dict(SOL_HILBERT_AMP_FADE_SPEC),
        slug="sol_1h_hilbert_amp_fade",
        arm_id="SOLUSDT|1h|hilbert_amp_fade|atr1.5|slcap0.03",
        instrument=SOL_INSTRUMENT,
        family="ml_lab_causal_math",
        space="ml_lab_catalog_j_v1",
        side="both",
        readiness_note=(
            "Hunt 013 inner screen n=337 profit factor 1.310 entry-bar 0.223 ~21.8/month. "
            "Nested 2022–2026 n=726 profit factor 1.266 Sharpe 1.242 HAC 1.322 "
            "entry-bar 0.088 6/6 folds subset PASS. Still not Shadow-Ready. "
            "User-authorized 5% equity stop-risk Post-Only live test only."
        ),
        blockers=blockers,
        account=args.account,
        vps_host=args.vps_host,
        authorized_from=args.authorized_from,
        expires=args.expires,
        authorize=args.authorize,
        tip_bars=args.tip_bars,
        cert_name="sol_1h_hilbert_amp_fade_xxobster3_ln1_certificate.yaml",
        authorization_source=auth_src,
        evidence_class="inner_screen_before_2022_plus_nested_subset_pass_2022_2026",
        readme_settle=(
            "Not Shadow-Ready. Nested 2022–2026 settle is a subset PASS "
            "(profit factor 1.266, Sharpe 1.242). Fill-test, not a promotion."
        ),
        intended_account=args.account,
        sizing={
            "mode": SIZING_MODE_RISK_FRACTION,
            "risk_fraction": float(DEFAULT_STOP_RISK_FRACTION),
            "size_mult": 1.0,
            "qty_round": "nearest",
            "note": (
                "qty = nearest((equity * 0.05) / (price * bar_sl) / qty_step) * qty_step; "
                "skip if below venue min. Discrete step may sit slightly above or below 5%. "
                "Not the exchange minimum lot."
            ),
        },
        authorized_scope=(
            "5% equity stop-risk Post-Only (nearest Bybit qty step; skip if below min; "
            "not venue-minimum size)"
        ),
        readme_size=(
            "Size = 5% of equity at that bar's stop, nearest venue step "
            "(not the exchange minimum lot). "
        ),
    )
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--account", default="Xxobster3")
    ap.add_argument("--vps-host", default="94.156.189.76")
    ap.add_argument("--authorized-from", default="2026-09-04")
    ap.add_argument("--expires", default="2026-10-04")
    ap.add_argument("--tip-bars", type=int, default=24)
    ap.add_argument("--authorize", action="store_true")
    return build(ap.parse_args())


if __name__ == "__main__":
    raise SystemExit(main())
