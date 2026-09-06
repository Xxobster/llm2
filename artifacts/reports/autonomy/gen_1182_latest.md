# Autonomy public-indicator hunt gen 1182

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T083156Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma645_below_at_h` | one_head_filter_pi_star | 181 | 14.7860 | 2.0862 | 0.7017 | 4.5296 | 0.0246 | 0.3702 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma645_below_at_h` | one_head_filter_pi_star | 190 | 15.5213 | 2.0714 | 0.6947 | 4.5761 | 0.0242 | 0.3789 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `wma645_below_at_h` | one_head_filter_pi_star | 191 | 15.6182 | 1.9555 | 0.6859 | 3.8752 | 0.0138 | 0.3560 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma645_below_at_h` | one_head_filter_pi_star | 202 | 16.5177 | 1.7719 | 0.6535 | 3.4803 | 0.0122 | 0.3416 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `wma645_above_at_h` | one_head_filter_pi_star | 183 | 14.9219 | 1.5497 | 0.6066 | 2.5253 | 0.0086 | 0.2787 | ok | RAN |
| SOLUSDT | 4 | `wma645_above_at_h` | one_head_filter_pi_star | 185 | 15.0850 | 1.5217 | 0.6108 | 2.4215 | 0.0081 | 0.2757 | ok | RAN |
| ETHUSDT | 8 | `wma645_above_at_h` | one_head_filter_pi_star | 189 | 15.5356 | 1.2147 | 0.6138 | 1.1297 | 0.0078 | 0.2275 | ok | RAN |
| ETHUSDT | 4 | `wma645_above_at_h` | one_head_filter_pi_star | 183 | 15.1014 | 1.1728 | 0.5956 | 0.9327 | 0.0063 | 0.2131 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma645_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma645_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma645_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma645_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma645_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma645_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma645_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma645_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma645_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma645_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma645_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma645_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma645_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma645_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma645_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma645_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
