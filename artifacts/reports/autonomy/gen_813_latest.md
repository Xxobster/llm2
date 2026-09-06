# Autonomy public-indicator hunt gen 813

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T165450Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret151_neg_at_h` | one_head_filter_pi_star | 195 | 15.9297 | 1.8644 | 0.6872 | 4.1146 | 0.0214 | 0.3692 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret151_neg_at_h` | one_head_filter_pi_star | 192 | 15.6846 | 1.8692 | 0.6771 | 4.0666 | 0.0213 | 0.3750 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret151_neg_at_h` | one_head_filter_pi_star | 185 | 15.1276 | 2.1615 | 0.6865 | 4.2758 | 0.0162 | 0.3514 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret151_neg_at_h` | one_head_filter_pi_star | 190 | 15.5365 | 1.9979 | 0.6632 | 3.9739 | 0.0146 | 0.3632 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ret151_pos_at_h` | one_head_filter_pi_star | 188 | 15.5140 | 1.2464 | 0.6064 | 1.2482 | 0.0085 | 0.2181 | ok | RAN |
| ETHUSDT | 4 | `ret151_pos_at_h` | one_head_filter_pi_star | 198 | 16.3392 | 1.2435 | 0.6061 | 1.2516 | 0.0084 | 0.2323 | ok | RAN |
| SOLUSDT | 8 | `ret151_pos_at_h` | one_head_filter_pi_star | 193 | 15.7373 | 1.4300 | 0.5959 | 2.0802 | 0.0068 | 0.2746 | ok | RAN |
| SOLUSDT | 4 | `ret151_pos_at_h` | one_head_filter_pi_star | 177 | 14.5149 | 1.4108 | 0.5989 | 1.9434 | 0.0063 | 0.2712 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret151_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5834 | 0.3333 | -0.8834 | -0.0441 | 0.0556 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret151_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5834 | 0.3333 | -0.8834 | -0.0441 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret151_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret151_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret151_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret151_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret151_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret151_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret151_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret151_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret151_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret151_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret151_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret151_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret151_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret151_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
