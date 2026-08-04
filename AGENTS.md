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
