# LLM2 — Predictability Laboratory

Research stack for causal feature engineering, seven prediction targets, and
tradesim-conformant backtesting with frozen V2.1 readiness gates.

## Warehouse

- Market data: `D:\projectsdata\candles\market_ohlcv.sqlite`
- Artifacts: `artifacts/` (fold parquets, SQLite registry, reports)

## Quick start

```powershell
python -m venv .venv
.venv\Scripts\pip install -e ".[dev]"
llm2 audit-data --symbol BTCUSDT --timeframe 1h
llm2 leakage-check --symbol BTCUSDT --timeframe 1h --space ohlcv_v1
pytest tests/
```

## Targets

`first_touch`, `fwd_return`, `direction`, `quantiles`, `volatility`, `regime`, `xs_rank`

## Engines

Before importing shared engines:

```python
from tradesim.ensure_source import prefer_botsgeneral_tradesim
from leakage.ensure_source import prefer_botsgeneral_leakage
prefer_botsgeneral_tradesim()
prefer_botsgeneral_leakage()
```

## Readiness

Default state: `LIVE_STOP / RESEARCH_ONLY`. Historical research alone earns at most `SHADOW_READY`.
