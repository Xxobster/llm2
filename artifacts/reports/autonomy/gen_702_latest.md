# Autonomy public-indicator hunt gen 702

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T071847Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma345_below_at_h` | one_head_filter_pi_star | 187 | 15.2762 | 2.0840 | 0.7059 | 4.7011 | 0.0245 | 0.3797 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma345_below_at_h` | one_head_filter_pi_star | 184 | 15.0311 | 1.8902 | 0.6848 | 4.0814 | 0.0214 | 0.3913 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma345_below_at_h` | one_head_filter_pi_star | 171 | 13.9828 | 2.3175 | 0.7018 | 4.4564 | 0.0183 | 0.3918 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma345_below_at_h` | one_head_filter_pi_star | 173 | 14.1464 | 2.2248 | 0.6936 | 4.2424 | 0.0169 | 0.3699 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `wma345_above_at_h` | one_head_filter_pi_star | 191 | 15.7000 | 1.2726 | 0.6021 | 1.4139 | 0.0092 | 0.2199 | ok | RAN |
| ETHUSDT | 4 | `wma345_above_at_h` | one_head_filter_pi_star | 194 | 16.0092 | 1.1879 | 0.5876 | 1.0112 | 0.0067 | 0.2165 | ok | RAN |
| SOLUSDT | 4 | `wma345_above_at_h` | one_head_filter_pi_star | 201 | 16.3896 | 1.3674 | 0.5970 | 1.8949 | 0.0059 | 0.2637 | ok | RAN |
| SOLUSDT | 8 | `wma345_above_at_h` | one_head_filter_pi_star | 195 | 15.9004 | 1.3615 | 0.5949 | 1.8674 | 0.0057 | 0.2564 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma345_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma345_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma345_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma345_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma345_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma345_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma345_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma345_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma345_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma345_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma345_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma345_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma345_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma345_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma345_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma345_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
