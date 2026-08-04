# Live pack versions (rollback map)

Immutable rule: never overwrite a frozen pack in place to “upgrade” behavior.
Ship a new directory + certificate + systemd unit; leave prior packs on disk.

| version_id | pack path | execution | account | VPS service | notes |
|---|---|---|---|---|---|
| `eth_direction_single_v1` | `structure_v1_ethusdt_direction` | single-book (max 1) | Xxobster7 | `llm2-structure-eth` | Current ETH direction micro-live |
| `btc_fwd_single_v1` | `structure_v1_lgbm` | single-book | Xxobster7 | `llm2-structure-micro` | BTCUSDT fwd_return |
| `sol_direction_single_v1` | `structure_v1_solusdt_direction` | single-book | Xxobster7 | `llm2-structure-sol` | SOLUSDT direction |
| `eth_multitrade_v1` | `structure_v1_ethusdt_multitrade_v1` | multitrade K=6/side | Xxobster8 | `llm2-structure-eth-multitrade-v1` (stopped) | rolled back / superseded by v1.1 |
| `eth_multitrade_v1_1` | `structure_v1_ethusdt_multitrade_v1_1` | multitrade K=7/side | Xxobster8 | `llm2-structure-eth-multitrade-v1_1` | **active** mean_strength \| fib 1.618 \| hold 12 |

## Rollback

1. Stop current: `systemctl stop llm2-structure-eth-multitrade-v1_1`
2. Restore K=6: `systemctl disable llm2-structure-eth-multitrade-v1_1 && systemctl enable --now llm2-structure-eth-multitrade-v1` (pack still at `/opt/llm2-structure-eth-multitrade-v1`)
3. Leave Xxobster7 single-book units running (they are independent).
4. Never overwrite a frozen pack directory in place.

## Git tags

- `live/eth_multitrade_v1` — K=6 freeze
- `live/eth_multitrade_v1_1` — K=7 freeze (current Xxobster8)
