# Live pack versions (rollback map)

Immutable rule: never overwrite a frozen pack in place to “upgrade” behavior.
Ship a new directory + certificate + systemd unit; leave prior packs on disk.

| version_id | pack path | execution | account | VPS service | notes |
|---|---|---|---|---|---|
| `eth_direction_single_v1` | `structure_v1_ethusdt_direction` | single-book (max 1) | Xxobster7 | `llm2-structure-eth` | Current ETH direction micro-live |
| `btc_fwd_single_v1` | `structure_v1_lgbm` | single-book | Xxobster7 | `llm2-structure-micro` | BTCUSDT fwd_return |
| `sol_direction_single_v1` | `structure_v1_solusdt_direction` | single-book | Xxobster7 | `llm2-structure-sol` | SOLUSDT direction |
| `eth_multitrade_v1` | `structure_v1_ethusdt_multitrade_v1` | multitrade K=6/side | Xxobster8 | `llm2-structure-eth-multitrade-v1` (stopped) | superseded |
| `eth_multitrade_v1_1` | `structure_v1_ethusdt_multitrade_v1_1` | multitrade K=7/side addon clarity | Xxobster8 | `llm2-structure-eth-multitrade-v1_1` (stopped) | rollback for v1.2 |
| `eth_multitrade_v1_2` | `structure_v1_ethusdt_multitrade_v1_2` | multitrade K=7/side **clarity_scope=all** | Xxobster8 | `llm2-structure-eth-multitrade-v1_2` | **active** mean_strength \| all \| fib 1.618 \| hold 12 |
| `eth_k5_double3h_v1` | `structure_v1_ethusdt_k5_double3h_v1` | multitrade K=5 + size×2 within 3h | Xxobster6 | `llm2-structure-eth-k5-double3h-v1` | research arm k5_double3h: mean_strength (all) \| hold12 \| TP1% uniform \| double3h |
| `btcusdt_clarity_hold12_v1` | `structure_v1_btcusdt_clarity_hold12_v1` | single-book clarity hold12 | — | **not deployed** | OUTER_SETTLE 001; parent `structure_v1_lgbm`; needs cert + user auth to swap |
| `ethusdt_clarity_hold12_v1` | `structure_v1_ethusdt_clarity_hold12_v1` | single-book clarity hold12 | — | **not deployed** | OUTER_SETTLE 001; parent direction pack; needs cert + user auth |
| `solusdt_clarity_hold12_v1` | `structure_v1_solusdt_clarity_hold12_v1` | single-book clarity hold12 | — | **not deployed** | OUTER_SETTLE 001; parent direction pack; needs cert + user auth |
| `btc_k5_double3h_v1` | `structure_v1_btcusdt_k5_double3h_v1` | multitrade K=5 + size×2 ≤3h | Xxobster10 | `llm2-structure-btc-k5-double3h-v1` | Track2 transfer; RESEARCH_TRANSFER_MICRO |
| `sol_k5_double3h_v1` | `structure_v1_solusdt_k5_double3h_v1` | multitrade K=5 + size×2 ≤3h | Xxobster10 | `llm2-structure-sol-k5-double3h-v1` | Track2 transfer; RESEARCH_TRANSFER_MICRO |

## Rollback

1. Stop current: `systemctl stop llm2-structure-eth-multitrade-v1_2`
2. Restore addon-clarity K=7: `systemctl disable llm2-structure-eth-multitrade-v1_2 && systemctl enable --now llm2-structure-eth-multitrade-v1_1` (pack still at `/opt/llm2-structure-eth-multitrade-v1_1`)
3. Or restore K=6: enable `llm2-structure-eth-multitrade-v1` instead.
4. Leave Xxobster7 single-book units running (they are independent).
5. Never overwrite a frozen pack directory in place.

## Git tags

- `live/eth_multitrade_v1` — K=6 freeze
- `live/eth_multitrade_v1_1` — K=7 addon clarity
- `live/eth_multitrade_v1_2` — K=7 clarity_scope=all (current Xxobster8)
