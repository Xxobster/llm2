# Live pack versions (rollback map)

Immutable rule: never overwrite a frozen pack in place to “upgrade” behavior.
Ship a new directory + certificate + systemd unit; leave prior packs on disk.

Generated from `live_pack_versions` in research.sqlite via `llm2.evidence.pack_registry.regenerate_versions_md`. Do not hand-edit without re-running the generator after pack freezes.

| version_id | pack path | status | account | VPS service | readiness | notes |
|---|---|---|---|---|---|---|
| `btc_k5_double3h_v1` | `artifacts/live_packs/structure_v1_btcusdt_k5_double3h_v1` | LIVE_ACTIVE | Xxobster10 | `llm2-structure-btc-k5-double3h-v1` | RESEARCH_ONLY | **active** |
| `eth_15m_multitrade_wall_clock_p75_v1` | `artifacts/live_packs/structure_v1_ethusdt_15m_multitrade_wall_clock_p75_v1` | LIVE_ACTIVE | Xxobster11 | `llm2-structure-eth-15m-multitrade-wall-clock-p75-v1` | MICRO_LIVE_CANDIDATE | **active**; PF=6.485352060119762; E[r]=0.010396663555539894 |
| `eth_k5_double3h_p75_v1` | `artifacts/live_packs/structure_v1_ethusdt_k5_double3h_p75_v1` | LIVE_ACTIVE | Xxobster3 | `llm2-structure-eth-k5-double3h-p75-v1` | MICRO_LIVE_CANDIDATE | **active**; PF=7.044474928687612; E[r]=0.0064316547337478335 |
| `eth_k5_double3h_v1` | `artifacts/live_packs/structure_v1_ethusdt_k5_double3h_v1` | LIVE_ACTIVE | Xxobster6 | `llm2-structure-eth-k5-double3h-v1` | RESEARCH_ONLY | **active**; PF=4.114418041595842; E[r]=0.005206316921173494 |
| `eth_multitrade_p75_v1` | `artifacts/live_packs/structure_v1_ethusdt_multitrade_p75_v1` | LIVE_ACTIVE | Xxobster9 | `llm2-structure-eth-multitrade-p75-v1` | MICRO_LIVE_CANDIDATE | **active**; replaces eth_multitrade_v1_1; PF=6.9621444934318975; E[r]=0.00951747831620085 |
| `eth_multitrade_v1_2` | `artifacts/live_packs/structure_v1_ethusdt_multitrade_v1_2` | LIVE_ACTIVE | Xxobster8 | `llm2-structure-eth-multitrade-v1_2` | RESEARCH_ONLY | **active**; replaces eth_multitrade_v1_1 |
| `sol_k5_double3h_v1` | `artifacts/live_packs/structure_v1_solusdt_k5_double3h_v1` | LIVE_ACTIVE | Xxobster10 | `llm2-structure-sol-k5-double3h-v1` | RESEARCH_ONLY | **active** |
| `adausdt_direction` | `artifacts/live_packs/structure_v1_adausdt_direction` | FROZEN | — | `—` | RESEARCH_ONLY | — |
| `avaxusdt_direction` | `artifacts/live_packs/structure_v1_avaxusdt_direction` | FROZEN | — | `—` | RESEARCH_ONLY | — |
| `bnbusdt_direction` | `artifacts/live_packs/structure_v1_bnbusdt_direction` | FROZEN | — | `—` | RESEARCH_ONLY | — |
| `btcusdt_clarity_hold12_v1` | `artifacts/live_packs/structure_v1_btcusdt_clarity_hold12_v1` | FROZEN | — | `—` | RESEARCH_ONLY | — |
| `dogeusdt_direction` | `artifacts/live_packs/structure_v1_dogeusdt_direction` | FROZEN | — | `—` | RESEARCH_ONLY | — |
| `dotusdt_direction` | `artifacts/live_packs/structure_v1_dotusdt_direction` | FROZEN | — | `—` | RESEARCH_ONLY | — |
| `eth_multitrade_v1` | `artifacts/live_packs/structure_v1_ethusdt_multitrade_v1` | FROZEN | Xxobster8 | `llm2-structure-eth-multitrade-v1` | RESEARCH_ONLY | — |
| `eth_multitrade_v1_1` | `artifacts/live_packs/structure_v1_ethusdt_multitrade_v1_1` | FROZEN | Xxobster8 | `llm2-structure-eth-multitrade-v1_1` | RESEARCH_ONLY | replaces eth_multitrade_v1 |
| `ethusdt_clarity_hold12_v1` | `artifacts/live_packs/structure_v1_ethusdt_clarity_hold12_v1` | FROZEN | — | `—` | RESEARCH_ONLY | — |
| `ethusdt_direction` | `artifacts/live_packs/structure_v1_ethusdt_direction` | FROZEN | — | `—` | RESEARCH_ONLY | — |
| `lgbm` | `artifacts/live_packs/structure_v1_lgbm` | FROZEN | — | `—` | RESEARCH_ONLY | — |
| `linkusdt_direction` | `artifacts/live_packs/structure_v1_linkusdt_direction` | FROZEN | — | `—` | RESEARCH_ONLY | — |
| `solusdt_clarity_hold12_v1` | `artifacts/live_packs/structure_v1_solusdt_clarity_hold12_v1` | FROZEN | — | `—` | RESEARCH_ONLY | — |
| `solusdt_direction` | `artifacts/live_packs/structure_v1_solusdt_direction` | FROZEN | — | `—` | RESEARCH_ONLY | — |
| `trxusdt_direction` | `artifacts/live_packs/structure_v1_trxusdt_direction` | FROZEN | — | `—` | RESEARCH_ONLY | — |
| `vetusdt_direction` | `artifacts/live_packs/structure_v1_vetusdt_direction` | FROZEN | — | `—` | RESEARCH_ONLY | — |
| `xlmusdt_direction` | `artifacts/live_packs/structure_v1_xlmusdt_direction` | FROZEN | — | `—` | RESEARCH_ONLY | — |
| `xrpusdt_direction` | `artifacts/live_packs/structure_v1_xrpusdt_direction` | FROZEN | — | `—` | RESEARCH_ONLY | — |

## Rollback

1. Stop current active unit for that account.
2. `systemctl enable --now` the previous service (pack retained on disk).
3. Call `register_live(old_version, deployed=True)` and `register_live(new_version, deployed=False)`.
4. Never overwrite a frozen pack directory in place.

## Open metrics without resim

```python
from llm2.evidence.pack_registry import open_pack_run, primary_run_id
print(primary_run_id('eth_multitrade_v1_2'))
open_pack_run('eth_multitrade_v1_2')  # tradesim-research open --run-id …
```

_Generated 20260806T124755Z UTC._
