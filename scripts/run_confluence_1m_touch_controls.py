"""Re-score hunt-002 15m controls with forced 1-minute touch (no OHLC fallback)."""

from __future__ import annotations

import importlib.util
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

os.environ.setdefault("TRADESIM_NO_PLOT", "1")

from tradesim.ensure_source import prefer_botsgeneral_tradesim

prefer_botsgeneral_tradesim()

from llm2.confluence.sim_arms import cached_touch, jsonable, run_limit_arm  # noqa: E402
from llm2.paths import ARTIFACTS, touch_timeframe  # noqa: E402
from llm2.pivot.strategy.score_oos import limit_price_side  # noqa: E402

_HUNT = importlib.util.spec_from_file_location(
    "hunt002", _ROOT / "scripts" / "run_confluence_autonomous_hunt_002.py"
)
hunt = importlib.util.module_from_spec(_HUNT)
assert _HUNT.loader is not None
_HUNT.loader.exec_module(hunt)

def main() -> int:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out_dir = ARTIFACTS / "reports" / "confluence"
    rows = []
    for symbol in ("ETHUSDT", "SOLUSDT", "BTCUSDT"):
        assert touch_timeframe("15m", symbol) == "1m"
        ctx = hunt._Ctx(symbol, "15m", 120_000)
        for tp, sl in ((0.005, 0.005), (0.01, 0.01)):
            mask = ctx.ctrl_mask & ctx.in_test
            if ctx.level_override is not None:
                old = ctx.sc.level_ret
                ctx.sc.level_ret = ctx.level_override
                _, is_s, lim = limit_price_side(ctx.sc, mask)
                ctx.sc.level_ret = old
            else:
                _, is_s, lim = limit_price_side(ctx.sc, mask)
            tag = f"{symbol}_15m_ctrl_tp{tp}_sl{sl}_touch1m"
            rec = run_limit_arm(
                symbol,
                ctx.sc,
                mask,
                is_s,
                lim,
                tag=tag,
                work=ctx.work_ctrl,
                max_hold=6,
                tp=tp,
                sl=sl,
            )
            rec.update(
                {
                    "symbol": symbol,
                    "tp": tp,
                    "sl": sl,
                    "touch_timeframe": "1m",
                    "n_touch_bars": int(len(cached_touch(symbol, "15m"))),
                }
            )
            print(
                f"{symbol} tp={tp} sl={sl} n={rec.get('n_trades')} PF={rec.get('profit_factor')} "
                f"ebr={rec.get('entry_bar_exit_rate')} touch={rec.get('touch_resolved_rate')} "
                f"amb={rec.get('ambiguous_rate')}",
                flush=True,
            )
            rows.append(rec)

    payload = {
        "generation_id": "confluence_1m_touch_controls",
        "stamp": stamp,
        "readiness_max": "RESEARCH_ONLY",
        "arms": rows,
    }
    path = out_dir / "autonomous_hunt_002_1m_touch_controls.json"
    path.write_text(json.dumps(jsonable(payload), indent=2), encoding="utf-8")
    md = [
        "# 15-minute controls re-scored on 1-minute touch",
        "",
        f"**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `{stamp}`.",
        "Empty touch window is refused (no Open-High-Low-Close same-bar guess).",
        "",
        "| Symbol | TP | SL | n | PF | WR | Sharpe | ebr | touch-resolved | ambiguous |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for r in rows:
        md.append(
            f"| {r['symbol']} | {r['tp']} | {r['sl']} | {r.get('n_trades')} | "
            f"{r.get('profit_factor')} | {r.get('win_rate')} | {r.get('sharpe_annualised')} | "
            f"{r.get('entry_bar_exit_rate')} | {r.get('touch_resolved_rate')} | {r.get('ambiguous_rate')} |"
        )
    (out_dir / "autonomous_hunt_002_1m_touch_controls.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print("WROTE", path, flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
