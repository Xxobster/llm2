# LLM2 agent instructions

Read and obey:

1. `.cursor/rules/trading-bot-core.mdc`
2. `.cursor/rules/long-batch-job-watchdog.mdc`
3. `.cursor/rules/continuous-services-always-on.mdc`
4. `docs/project_memory/TRADING_BOT_RESEARCH_STANDARD_V2.md`
5. `docs/project_memory/FROZEN_DEFAULT_GATES_V2_1.md`
6. `docs/project_memory/PROCESS_SUPERVISION_AND_CANDLE_FRESHNESS.md`
7. `docs/project_memory/TRADING_PROJECT_PROFILE.md`
8. `docs/project_memory/CURRENT_STATE.md`

## Engines

```python
from tradesim.ensure_source import prefer_botsgeneral_tradesim
prefer_botsgeneral_tradesim()
from leakage.ensure_source import prefer_botsgeneral_leakage
prefer_botsgeneral_leakage()
```

Refuse if `tradesim.__file__` / `leakage.__file__` lack `botsgeneral`.

## Default posture

`LIVE_STOP / RESEARCH_ONLY`. Alert the user only for Tier ≥ 2 gate candidates. Keep hunting.

**Maker-first fees:** prefer Post-Only / resting limit on entry, take-profit and stop-loss so the strategy pays as little fee as the venue allows. Use taker (market / crossing limit / stop-market) only when there is no choice (Post-Only cancelled, gap-through, max-hold, liquidation). Charge maker 0.02% on resting legs and still report the all-taker stress. Live must not run cheaper than the frozen pack.

**1-minute fill clock (`EXEC-021`):** any decision timeframe *places* the order. Then walk 1-minute bars: **entry = first 1-minute that touches the limit, at the limit price** (not the 4-hour/1-hour open). Take-profit/stop arm only after that fill. A 1-minute path that prints take-profit 103 before buy limit 98 is **not a win**. Same 15-minute/1-hour/4-hour candle after a real fill is allowed. See `TRADING_BOT_RESEARCH_STANDARD_V2.md` §9.6.1.

## Process classes (mandatory)

- **Long batch (finite, local, >~10 min):** run under `scripts/watchdog_run.ps1` with `python -u`. Restart on crash/stall (bounded). Verify process id — do not trust a frozen terminal `status: running`.
- **Continuous (infinite):** candle collectors, trading/shadow bots, poker bots must **always run** when authorized (`systemd` + restart). Process present ≠ healthy.
- **Candle tip (`LIVE-DATA-001`):** before every decision, local last closed candle must match exchange **server time** expected tip. Collector/fetch errors (even 15m only) ⇒ fail closed (no new entries; keep protective exits). See `PROCESS_SUPERVISION_AND_CANDLE_FRESHNESS.md`.

## FOUR_PROOF_GATE_V1 (mandatory before train / pack freeze / live authorize)

A green shared `leakage` report alone is **illegal** evidence for warehouse-backed
spaces (`structure_v1`, `macro_v1`, …). Before any train, hunt fold, pack freeze, or
live certificate authorization, all four proofs must be green and hashed:

| # | Proof | What it catches |
|---|---|---|
| 1 | **builder_responsiveness** (`CAUS-WAREHOUSE-001`) | Builder ignores candles / reads external cache |
| 2 | **recompute_prefix** | Warehouse recomputed from handed candles is prefix-invariant |
| 3 | **no_live_feature_fill** | Live invents values (`fillna(0)`) research never scored |
| 4 | **layer_a_pred_identity** | Shadow audit builder ≠ train/live feature path |

API: `llm2.evidence.four_proof.run_four_proof_gate` → attach via
`attach_four_proof_to_pack`. `register_freeze` and live certificates **refuse**
without `evidence.four_proof_hashes` + `four_proof_ok=true`.

Live↔backtest `pred_mean` / side mismatch is a **hard stop** (same class as a failed
gate). Stop optimization; do not freeze or deploy until Layer A is identically zero.

## Ops parity gates (anytime)

| Name | Script | Scope |
|---|---|---|
| **Fleet Live Signal Parity** | `scripts/ops_fleet_live_signal_parity.py` | All active bots ln1+ln3: last 1h live `pred_mean` vs local BT |
| Ops Live Research Parity (single unit) | `scripts/ops_live_research_parity_gate.py` | One unit deep tip + pack + `pred_mean` |
| 1m Indicator Parity Bot | `scripts/run_1m_indicator_parity_bot.py` | Indicator tip identity only (no model) |

None of these promote readiness. Update `FLEET_REGISTRY` in the fleet script when units change.

## Lockbox / Finplot (D-038)

- Outer-fold and settle scripts first. Do **not** peep `FORWARD_LOCKBOX_START`
  (2026-05-01+) for charts or multi-arm ranking.
- New lockbox tools must call `add_lockbox_guard_args` + `require_lockbox_access`
  from `llm2.evidence.lockbox_guard`.
- Finplot needs **both** `--i-accept-lockbox-contamination` and
  `--i-accept-finplot-lockbox` (plus `--show`). Default is report-only.
- Never set `LLM2_I_ACCEPT_LOCKBOX_CONTAMINATION` or `LLM2_I_ACCEPT_FINPLOT_LOCKBOX`
  permanently in shell profiles, systemd unit files, or VPS env.
- Contamination authority: `artifacts/evidence/peek_log.jsonl` — copying DB paths
  does not reseal.
- Fleet signal concurrence (outer OOS only):
  `scripts/run_live_fleet_concordance.py`
