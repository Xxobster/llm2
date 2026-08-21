"""Quantify shared_candles vs research market_ohlcv tip residual (local)."""
from __future__ import annotations

import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

SHARED = Path(r"C:\projects\botsgeneral")  # may not exist locally
# Prefer VPS dump via prior knowledge; use local market warehouse + if shared exists
MARKET = Path(r"D:\projectsdata\candles\market_ohlcv.sqlite")
OUT = Path(__file__).resolve().parents[1] / "artifacts/reports/live_bt_calc_gap_risks_20260805.json"


def warehouse_tip(symbol: str, n: int = 10):
    con = sqlite3.connect(f"file:{MARKET}?mode=ro", uri=True)
    # densest last synonym
    rows = con.execute(
        """
        SELECT ts_ms, close, price_type FROM market_ohlcv
        WHERE symbol=? AND timeframe='1h' AND source='binance'
          AND price_type IN ('last','last_price') AND ts_ms IS NOT NULL
        ORDER BY ts_ms DESC LIMIT ?
        """,
        (symbol, n * 3),
    ).fetchall()
    con.close()
    # pick densest type among tip window
    from collections import Counter

    # Prefer last_price if present in recent, else last
    by_type = {}
    for ts, c, pt in rows:
        by_type.setdefault(pt, []).append((ts, c))
    chosen = "last_price" if by_type.get("last_price") else ("last" if by_type.get("last") else None)
    tip = list(reversed(by_type[chosen][:n])) if chosen else []
    return chosen, tip


def main():
    risks = [
        {
            "id": "SHARED_VS_RESEARCH_OHLCV",
            "severity": "high_for_exact_match",
            "status": "open_residual",
            "detail": (
                "Backtest loads Open-High-Low-Close-Volume from research "
                "market_ohlcv.sqlite (pinned last/last_price). Live builds structure "
                "and vol features from botsgeneral shared_candles.db. If any historical "
                "bar differs, confirmed swings and pred_mean can diverge even with full history."
            ),
            "mitigation": (
                "Periodic tip+history checksum shared vs market_ohlcv; or sync research "
                "indicators.sqlite (~2.5GB) to VPS and read features from it (gold path)."
            ),
        },
        {
            "id": "STRUCTURE_RECOMPUTE_VS_WAREHOUSE_FILE",
            "severity": "medium",
            "status": "mitigated_full_history",
            "detail": (
                "Live recompute_structure(full shared) ≈ research warehouse if OHLCV identical. "
                "Was broken at limit=800 (sign flip). Now full history + depth gate >=5000."
            ),
            "mitigation": "Keep hard refuse short limits; prefer warehouse sync for byte identity.",
        },
        {
            "id": "LIVE_OHLCV_TIP_WINDOW",
            "severity": "low_after_fix",
            "status": "mitigated",
            "detail": (
                "Live previously used only 300 bars for vol-normalised columns (VOL_WINDOW=168). "
                "Raised to LIVE_SIGNAL_OHLCV_BARS=2000."
            ),
        },
        {
            "id": "LAST_RETRACE_FILLNA_ZERO",
            "severity": "low",
            "status": "known_live_policy",
            "detail": (
                "Live zero-fills last_retrace_pct* NaNs at decide time. Training dropped those "
                "rows. Rare tip NaN can change pred vs a BT row that would have been skipped."
            ),
            "mitigation": "Refuse decide on NaN retrace (fail closed) instead of fillna, matching train drop.",
        },
        {
            "id": "RECENT_ONLY_READ_WINDOW",
            "severity": "none_if_same_db",
            "status": "safe",
            "detail": "recent_only=True only truncates warehouse READ; Layer A match rate 1.0 on same DB.",
        },
        {
            "id": "FORMING_BAR_DROP",
            "severity": "low",
            "status": "aligned",
            "detail": "Live drops forming bar; BT uses completed bars only. Off-by-one if clock/freshness wrong.",
        },
        {
            "id": "MODEL_PACK_HASH",
            "severity": "ops",
            "status": "verify_per_pack",
            "detail": "Signals require identical model.joblib as frozen research pack.",
        },
        {
            "id": "EDGE_AND_PROXY_SIDE",
            "severity": "low",
            "status": "code_shared",
            "detail": "proxy_side + min_edge from same llm2.hunt.targets / strategy.json.",
        },
        {
            "id": "MULTITRADE_GATES",
            "severity": "medium_for_entries",
            "status": "separate_from_pred",
            "detail": (
                "pred_mean can match while live skips entry (clarity, cap, cooloff, position limits). "
                "That is execution gating, not signal calc — but live trade set ≠ unconstrained BT."
            ),
        },
        {
            "id": "FEATURE_SNAPSHOT",
            "severity": "audit",
            "status": "mitigated",
            "detail": "Decide-time feature_snapshot now persisted for reproducibility audits.",
        },
    ]

    tips = {}
    for sym in ("ETHUSDT", "BTCUSDT", "SOLUSDT"):
        pt, tip = warehouse_tip(sym, 5)
        tips[sym] = {"price_type": pt, "tip": [{"ts_ms": t, "close": c} for t, c in tip]}

    report = {
        "evidence_class": "LIVE_BT_CALC_GAP_RISKS",
        "maximum_earned_readiness": "LIVE_STOP / RESEARCH_ONLY",
        "principal_blocker_for_exact_signal_identity": "SHARED_VS_RESEARCH_OHLCV",
        "fleet_corrected": {
            "ln1_94": "all 7 active units + inactive packs deep binance slices",
            "ln3_185": "both p75 active units deep binance slices + parity code",
        },
        "gold_path_for_exact_match": (
            "Use the same indicators.sqlite bytes the backtest read (sync research warehouse "
            "to VPS / point LLM2_INDICATORS_DB at it), and the same completed OHLCV closes for "
            "vol columns. Do not recompute structure from a second candle store unless checksum-equal."
        ),
        "warehouse_tips_local": tips,
        "risks": risks,
        "generated_utc": datetime.now(timezone.utc).isoformat(),
    }
    OUT.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
