"""Freeze hunt-009 / hunt-012 formula live packs + four-proof + certificates.

Readiness remains RESEARCH_ONLY. Nested 2022–2026 settle FAIL is stamped on
the certificate. User-authorized 5% equity stop-risk Post-Only test on
live-network-2.

    python -u scripts/build_formula_live_packs.py --authorize
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

os.environ.setdefault("TRADESIM_NO_PLOT", "1")

from llm2.data.loader import load_ohlcv  # noqa: E402
from llm2.evidence.four_proof_formula import run_four_proof_gate_formula  # noqa: E402
from llm2.gates.evidence import (  # noqa: E402
    DEFAULT_LEVERAGE_HAIRCUT,
    DEFAULT_MARK_BUFFER,
    DEFAULT_MM_BUFFER,
    leverage_ceiling_from_stop,
    leverage_from_stop,
)
from llm2.live.certificate import pack_fingerprint  # noqa: E402
from llm2.ml_lab.live_guards import (  # noqa: E402
    BTC_QUAD_SLOPE_SPEC,
    SOL_FVG_CONFLUENCE_SPEC,
)
from llm2.paths import ARTIFACTS, FORWARD_LOCKBOX_START, ROOT  # noqa: E402
from llm2.research_policy import MIN_SIZE_EQUITY_CAVEAT, PolicyError  # noqa: E402
from llm2.sizing_policy import (  # noqa: E402
    DEFAULT_STOP_RISK_FRACTION,
    SIZING_MODE_MIN_EXCHANGE,
    SIZING_MODE_RISK_FRACTION,
)

PACK_ROOT = ARTIFACTS / "live_packs"
CERT_DIR = ROOT / "configs" / "live"

SOL_INSTRUMENT = {
    "symbol": "SOLUSDT",
    "tick_size": 0.01,
    "qty_step": 0.1,
    "min_qty": 0.1,
    "min_notional": 5.0,
    "max_qty": 96000.0,
    "max_leverage": 100.0,
    "source": "bybit_v5_instruments-info_20260901",
}

BTC_INSTRUMENT_FALLBACK = {
    "symbol": "BTCUSDT",
    "tick_size": 0.10,
    "qty_step": 0.001,
    "min_qty": 0.001,
    "min_notional": 5.0,
    "max_qty": 1190.0,
    "max_leverage": 100.0,
    "source": "bybit_v5_fallback_20260904",
}


def fetch_bybit_linear_instrument(symbol: str) -> dict[str, Any]:
    url = (
        "https://api.bybit.com/v5/market/instruments-info"
        f"?category=linear&symbol={symbol}"
    )
    with urllib.request.urlopen(url, timeout=20) as resp:
        payload = json.loads(resp.read().decode("utf-8"))
    rows = list((payload.get("result") or {}).get("list") or [])
    if not rows:
        raise RuntimeError(f"no Bybit instrument row for {symbol}")
    row = rows[0]
    lot = row.get("lotSizeFilter") or {}
    px = row.get("priceFilter") or {}
    lev = row.get("leverageFilter") or {}
    return {
        "symbol": symbol,
        "tick_size": float(px.get("tickSize") or 0.1),
        "qty_step": float(lot.get("qtyStep") or 0.001),
        "min_qty": float(lot.get("minOrderQty") or lot.get("qtyStep") or 0.001),
        "min_notional": float(lot.get("minNotionalValue") or 5.0),
        "max_qty": float(lot.get("maxOrderQty") or 1e9),
        "max_leverage": float(lev.get("maxLeverage") or 100.0),
        "source": "bybit_v5_instruments-info_live_fetch",
    }


def _write_pack(
    *,
    spec: dict[str, Any],
    slug: str,
    arm_id: str,
    instrument: dict[str, Any],
    family: str,
    space: str,
    side: str,
    readiness_note: str,
    blockers: list[str],
    account: str,
    vps_host: str,
    authorized_from: str,
    expires: str,
    authorize: bool,
    tip_bars: int,
    cert_name: str,
    authorization_source: str,
    evidence_class: str = "inner_screen_before_2022_plus_nested_fail_2022_2026",
    readme_settle: str = "Not Shadow-Ready. Nested 2022–2026 settle FAIL.",
    intended_account: str | None = None,
    sizing: dict[str, Any] | None = None,
    authorized_scope: str = (
        "5% equity stop-risk Post-Only (floor to Bybit qty step; skip if below min)"
    ),
    readme_size: str = "Size = 5% of equity at that bar's stop, floored to the venue step. ",
) -> str:
    sl_cap = float(spec["sl_cap"])
    lev = leverage_from_stop(sl_cap)
    lev_ceiling = leverage_ceiling_from_stop(sl_cap)
    if abs(lev - 13.0) > 1e-9:
        raise PolicyError(f"expected 13× from 3% cap, got {lev}")
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    pack_dir = PACK_ROOT / slug
    pack_dir.mkdir(parents=True, exist_ok=True)

    strategy: dict[str, Any] = {
        "arm_id": arm_id,
        "strategy_id": slug,
        "family": family,
        "space": space,
        "symbol": spec["symbol"],
        "timeframe": spec["timeframe"],
        "idea": spec["idea"],
        "catalog": spec["catalog"],
        "side": side,
        "entry": spec["entry"],
        "expired_entry": spec["expired_entry"],
        "k_sl": float(spec["k_sl"]),
        "tp_ratio": float(spec["tp_ratio"]),
        "sl_cap": sl_cap,
        "work_bars": int(spec["work_bars"]),
        "max_hold_bars": int(spec["max_hold_bars"]),
        "leverage": float(lev),
        "leverage_derivation": {
            "sl_pct": sl_cap,
            "note": "Leverage from the 3% stop cap (worst-case Average True Range stop).",
            "mm_buffer": DEFAULT_MM_BUFFER,
            "mark_buffer": DEFAULT_MARK_BUFFER,
            "ceiling_floor_1_over_denom": int(lev_ceiling),
            "haircut": DEFAULT_LEVERAGE_HAIRCUT,
            "leverage_used_live_and_backtest": float(lev),
        },
        "risk_fraction": float(DEFAULT_STOP_RISK_FRACTION),
        "sizing": sizing
        or {
            "mode": SIZING_MODE_RISK_FRACTION,
            "risk_fraction": float(DEFAULT_STOP_RISK_FRACTION),
            "size_mult": 1.0,
            "note": (
                "qty = floor((equity * 0.05) / (price * bar_sl) / qty_step) * qty_step; "
                "skip if below venue min."
            ),
        },
        "signal_module": "llm2.ml_lab.live_signal:tip_signal",
        "runner": "llm2.live.ema_stack_runner",
        "instrument": instrument,
        "htf_context_used": False,
        "session_filter": None,
        "frozen_at_utc": stamp,
        "readiness_max": "RESEARCH_ONLY",
        "promotion_allowed": False,
    }
    (pack_dir / "strategy.json").write_text(
        json.dumps(strategy, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )

    meta = {
        "strategy_id": slug,
        "arm_id": arm_id,
        "space": space,
        "status": "FROZEN_LIVE_PACK",
        "readiness": "RESEARCH_ONLY",
        "readiness_note": readiness_note,
        "evidence_class": evidence_class,
        "evidence_window_end": str(FORWARD_LOCKBOX_START),
        "min_size_equity_caveat": MIN_SIZE_EQUITY_CAVEAT,
        "frozen_at_utc": stamp,
    }
    (pack_dir / "pack_meta.json").write_text(
        json.dumps(meta, indent=2, default=str, sort_keys=True) + "\n", encoding="utf-8"
    )

    print(f"=== FOUR_PROOF_GATE_V1 {spec['symbol']} {spec['timeframe']} {spec['idea']} ===", flush=True)
    ohlcv = load_ohlcv(str(spec["symbol"]), str(spec["timeframe"]))
    summary = run_four_proof_gate_formula(spec=spec, ohlcv=ohlcv, tip_bars=int(tip_bars))
    (pack_dir / "four_proof_summary.json").write_text(
        json.dumps(summary, indent=2, default=str, sort_keys=True) + "\n", encoding="utf-8"
    )
    if not summary["ok"]:
        raise PolicyError(
            f"FOUR_PROOF_GATE_V1 FAILED: {summary['proofs_ok']}. Refusing certificate."
        )

    meta["evidence"] = {
        "four_proof_hashes": summary["artifact_hashes"],
        "four_proof_ok": True,
        "four_proof_summary_sha256": summary["summary_sha256"],
        "four_proof_artifact_dir": summary["artifact_dir"],
        "four_proof_stamp": summary["stamp"],
    }
    meta["four_proof_ok"] = True
    meta["four_proof_hashes"] = summary["artifact_hashes"]
    (pack_dir / "pack_meta.json").write_text(
        json.dumps(meta, indent=2, default=str, sort_keys=True) + "\n", encoding="utf-8"
    )
    (pack_dir / "README.md").write_text(
        f"# {slug}\n\n"
        f"{spec['symbol']} {spec['timeframe']} `{spec['idea']}`. "
        "Post-Only entry, cancel if no touch. "
        "Stop = clip(1.5 × Average True Range %, 0.4%, 3%). Leverage 13× from the 3% cap. "
        f"{readme_size}"
        f"{readme_settle}\n",
        encoding="utf-8",
    )

    fp = pack_fingerprint(pack_dir)
    if not fp:
        raise PolicyError("pack fingerprint failed")
    (pack_dir / "pack_hash.txt").write_text(fp + "\n", encoding="utf-8")
    meta["pack_hash"] = fp
    (pack_dir / "pack_meta.json").write_text(
        json.dumps(meta, indent=2, default=str, sort_keys=True) + "\n", encoding="utf-8"
    )
    fp2 = pack_fingerprint(pack_dir)
    meta["pack_hash"] = fp2
    (pack_dir / "pack_meta.json").write_text(
        json.dumps(meta, indent=2, default=str, sort_keys=True) + "\n", encoding="utf-8"
    )
    (pack_dir / "pack_hash.txt").write_text(fp2 + "\n", encoding="utf-8")

    if authorize:
        cert_path = CERT_DIR / cert_name
        created = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        hashes = summary["artifact_hashes"]
        blocker_yaml = "\n".join(f"- {b}" for b in blockers)
        cert_path.write_text(
            f"""strategy_id: {slug}
arm_id: {arm_id}
status: AUTHORIZED
authorized_by_user: true
authorized_scope: {authorized_scope}
authorization_source: >-
  {authorization_source}
vps_host: {vps_host}
account_ref: {account}
intended_account_ref: {intended_account or account}
pack_path: artifacts/live_packs/{slug}
pack_hash: {fp2}
authorized_from_utc: '{authorized_from}T00:00:00Z'
expires_utc: '{expires}T00:00:00Z'
created_utc: '{created}'
symbol: {spec['symbol']}
timeframe: {spec['timeframe']}
idea: {spec['idea']}
leverage: {float(lev)}
risk_fraction: {float(DEFAULT_STOP_RISK_FRACTION)}
sizing_mode: {SIZING_MODE_RISK_FRACTION}
four_proof_ok: true
four_proof_hashes:
  builder_responsiveness: {hashes.get("builder_responsiveness")}
  recompute_prefix: {hashes.get("recompute_prefix")}
  no_live_feature_fill: {hashes.get("no_live_feature_fill")}
  layer_a_pred_identity: {hashes.get("layer_a_pred_identity")}
research_readiness: RESEARCH_ONLY (not SHADOW_READY)
blockers_acknowledged:
{blocker_yaml}
""",
            encoding="utf-8",
        )
        print(f"CERT {cert_path}", flush=True)

    print(f"PACK {pack_dir} hash={fp2}", flush=True)
    return fp2


def build(args: argparse.Namespace) -> int:
    try:
        btc_inst = fetch_bybit_linear_instrument("BTCUSDT")
    except Exception as exc:  # noqa: BLE001
        print(f"BTC instrument fetch failed ({type(exc).__name__}); using fallback", flush=True)
        btc_inst = dict(BTC_INSTRUMENT_FALLBACK)

    auth_src = (
        "user chat 2026-09-04: run Bitcoin 1h slope-follow and Solana 1h Fair Value Gap "
        "confluence on 212.73.150.178, free Xxobster, 5% equity as risk, Post-Only, "
        "adapt bots start date, calculate leverage"
    )
    nested = (
        "nested stitched 2022-01-01..2026-05-01 FAIL "
        "(Bitcoin profit factor 0.977; Solana profit factor 0.865) — operational fill test only"
    )
    common_blockers = [
        nested,
        "no Gate C all-taker stress on these packs",
        "inner screen before 2022-01-01 is not Shadow-Ready",
        "unfilled Post-Only cancels and stays flat",
    ]

    _write_pack(
        spec=dict(BTC_QUAD_SLOPE_SPEC),
        slug="btc_1h_quad_slope_follow",
        arm_id="BTCUSDT|1h|quad_slope_follow|atr1.5|slcap0.03",
        instrument=btc_inst,
        family="ml_lab_causal_math",
        space="ml_lab_catalog_f_v1",
        side="both",
        readiness_note=(
            "Hunt 009 inner screen n=426 profit factor 1.505 Sharpe 2.00 entry-bar 0.063. "
            "Nested 2022–2026 profit factor 0.977 FAIL. User-authorized 5% equity stop-risk "
            "Post-Only live test only."
        ),
        blockers=common_blockers
        + [
            "quantity rounds to the nearest Bybit step around 5% stop-risk (may sit slightly above 5%)",
            "skip if the nearest lot is below the venue minimum",
            "fill rate ~27% on working limit",
            "two-sided: long if bit >= +0.5, short if bit <= -0.5",
        ],
        account=args.btc_account,
        vps_host=args.vps_host,
        authorized_from=args.authorized_from,
        expires=args.expires,
        authorize=args.authorize,
        tip_bars=args.tip_bars,
        cert_name="btc_1h_quad_slope_follow_xxobster11_ln2_certificate.yaml",
        authorization_source=auth_src,
        sizing={
            "mode": SIZING_MODE_RISK_FRACTION,
            "risk_fraction": float(DEFAULT_STOP_RISK_FRACTION),
            "qty_round": "nearest",
            "size_mult": 1.0,
            "note": (
                "qty = nearest((equity * 0.05) / (price * bar_sl) / qty_step) * qty_step; "
                "skip if below venue min."
            ),
        },
        authorized_scope=(
            "5% equity stop-risk Post-Only (nearest Bybit qty step; skip if below min)"
        ),
        readme_size=(
            "Size = 5% of equity at that bar's stop, rounded to the nearest venue step. "
        ),
    )
    _write_pack(
        spec=dict(SOL_FVG_CONFLUENCE_SPEC),
        slug="sol_1h_fvg_confluence",
        arm_id="SOLUSDT|1h|fvg_confluence|atr1.5|slcap0.03",
        instrument=SOL_INSTRUMENT,
        family="ml_lab_fvg",
        space="ml_lab_catalog_i_v1",
        side="long",
        readiness_note=(
            "Hunt 012 inner screen n=189 profit factor 1.374 Sharpe 1.62 entry-bar 0.106. "
            "Nested 2022–2026 profit factor 0.865 FAIL. User-authorized venue-minimum "
            "Post-Only live test only."
        ),
        blockers=common_blockers
        + [
            "venue-minimum lot (0.1 Solana); not 5% stop-risk",
            "fill rate ~37% on working limit",
            "long-only",
        ],
        account=args.sol_account,
        vps_host=args.vps_host,
        authorized_from=args.authorized_from,
        expires=args.expires,
        authorize=args.authorize,
        tip_bars=args.tip_bars,
        cert_name="sol_1h_fvg_confluence_xxobster11_ln2_certificate.yaml",
        authorization_source=auth_src,
        sizing={
            "mode": SIZING_MODE_MIN_EXCHANGE,
            "note": "Venue-minimum lot (0.1 Solana). User 2026-09-04: keep minimum size for now.",
            "size_mult": 1.0,
        },
        authorized_scope="venue-minimum Post-Only (0.1 Solana); not 5% stop-risk",
        readme_size="Size = venue minimum (0.1 Solana). ",
    )
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--btc-account", default="Xxobster11")
    ap.add_argument("--sol-account", default="Xxobster11")
    ap.add_argument("--vps-host", default="212.73.150.178")
    ap.add_argument("--authorized-from", default="2026-09-04")
    ap.add_argument("--expires", default="2026-10-04")
    ap.add_argument("--tip-bars", type=int, default=24)
    ap.add_argument("--authorize", action="store_true")
    return build(ap.parse_args())


if __name__ == "__main__":
    raise SystemExit(main())
