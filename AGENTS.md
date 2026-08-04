# LLM2 agent instructions

Read and obey:

1. `.cursor/rules/trading-bot-core.mdc`
2. `docs/project_memory/TRADING_BOT_RESEARCH_STANDARD_V2.md`
3. `docs/project_memory/FROZEN_DEFAULT_GATES_V2_1.md`
4. `docs/project_memory/TRADING_PROJECT_PROFILE.md`
5. `docs/project_memory/CURRENT_STATE.md`

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
