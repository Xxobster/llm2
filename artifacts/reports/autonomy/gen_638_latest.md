# Autonomy public-indicator hunt gen 638

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T025710Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma305_below_at_h` | one_head_filter_pi_star | 182 | 14.8677 | 2.0977 | 0.7033 | 4.6552 | 0.0242 | 0.3846 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma305_below_at_h` | one_head_filter_pi_star | 184 | 15.0311 | 2.0650 | 0.7065 | 4.6352 | 0.0240 | 0.3859 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma305_below_at_h` | one_head_filter_pi_star | 171 | 13.9828 | 2.2066 | 0.6901 | 4.2157 | 0.0172 | 0.3743 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma305_below_at_h` | one_head_filter_pi_star | 176 | 14.3917 | 2.1884 | 0.6932 | 4.2437 | 0.0171 | 0.3693 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `wma305_above_at_h` | one_head_filter_pi_star | 185 | 15.2665 | 1.2799 | 0.6054 | 1.4234 | 0.0094 | 0.2270 | ok | RAN |
| ETHUSDT | 4 | `wma305_above_at_h` | one_head_filter_pi_star | 196 | 16.1109 | 1.2723 | 0.6020 | 1.3471 | 0.0093 | 0.2245 | ok | RAN |
| SOLUSDT | 4 | `wma305_above_at_h` | one_head_filter_pi_star | 202 | 16.4712 | 1.3550 | 0.5941 | 1.8358 | 0.0055 | 0.2624 | ok | RAN |
| SOLUSDT | 8 | `wma305_above_at_h` | one_head_filter_pi_star | 196 | 15.9819 | 1.3127 | 0.5918 | 1.6394 | 0.0049 | 0.2602 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma305_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma305_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0451 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma305_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma305_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma305_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma305_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma305_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma305_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma305_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma305_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma305_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma305_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma305_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma305_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma305_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma305_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
