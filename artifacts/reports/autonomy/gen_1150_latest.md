# Autonomy public-indicator hunt gen 1150

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T045340Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma625_below_at_h` | one_head_filter_pi_star | 181 | 14.7860 | 2.0860 | 0.7017 | 4.5066 | 0.0249 | 0.3812 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma625_below_at_h` | one_head_filter_pi_star | 195 | 15.9297 | 2.0403 | 0.6923 | 4.6260 | 0.0237 | 0.3692 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `wma625_below_at_h` | one_head_filter_pi_star | 197 | 16.1089 | 1.8861 | 0.6599 | 3.7324 | 0.0131 | 0.3401 | GATE_CAND | RAN |
| SOLUSDT | 8 | `wma625_below_at_h` | one_head_filter_pi_star | 195 | 15.9453 | 1.8341 | 0.6564 | 3.5669 | 0.0124 | 0.3538 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `wma625_above_at_h` | one_head_filter_pi_star | 191 | 15.7000 | 1.2758 | 0.6126 | 1.4416 | 0.0094 | 0.2199 | ok | RAN |
| SOLUSDT | 4 | `wma625_above_at_h` | one_head_filter_pi_star | 191 | 15.5742 | 1.5212 | 0.6073 | 2.5169 | 0.0084 | 0.2723 | ok | RAN |
| SOLUSDT | 8 | `wma625_above_at_h` | one_head_filter_pi_star | 188 | 15.3296 | 1.5218 | 0.6117 | 2.4798 | 0.0082 | 0.2766 | ok | RAN |
| ETHUSDT | 8 | `wma625_above_at_h` | one_head_filter_pi_star | 165 | 13.6160 | 1.1712 | 0.5879 | 0.8669 | 0.0062 | 0.2121 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma625_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma625_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma625_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma625_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma625_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma625_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma625_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma625_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma625_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma625_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma625_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma625_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma625_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma625_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma625_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma625_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
