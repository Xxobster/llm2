# Autonomy public-indicator hunt gen 958

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260826T075447Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma505_below_at_h` | one_head_filter_pi_star | 197 | 16.0931 | 1.9853 | 0.6954 | 4.5055 | 0.0234 | 0.3858 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma505_below_at_h` | one_head_filter_pi_star | 195 | 15.9297 | 1.9379 | 0.6872 | 4.2453 | 0.0221 | 0.3641 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma505_below_at_h` | one_head_filter_pi_star | 189 | 15.4547 | 2.0527 | 0.6825 | 4.1330 | 0.0155 | 0.3704 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `wma505_below_at_h` | one_head_filter_pi_star | 179 | 14.6370 | 2.0271 | 0.6760 | 3.9708 | 0.0149 | 0.3743 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `wma505_above_at_h` | one_head_filter_pi_star | 185 | 15.2068 | 1.2428 | 0.6054 | 1.2622 | 0.0086 | 0.2270 | ok | RAN |
| SOLUSDT | 8 | `wma505_above_at_h` | one_head_filter_pi_star | 183 | 14.9219 | 1.4148 | 0.5956 | 2.0266 | 0.0067 | 0.2623 | ok | RAN |
| ETHUSDT | 8 | `wma505_above_at_h` | one_head_filter_pi_star | 191 | 15.7000 | 1.1434 | 0.5864 | 0.7828 | 0.0052 | 0.2147 | ok | RAN |
| SOLUSDT | 4 | `wma505_above_at_h` | one_head_filter_pi_star | 199 | 16.2265 | 1.3132 | 0.5879 | 1.6433 | 0.0051 | 0.2663 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma505_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma505_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma505_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma505_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma505_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma505_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma505_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma505_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma505_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma505_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma505_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma505_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma505_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma505_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma505_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma505_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
