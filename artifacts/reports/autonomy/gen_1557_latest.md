# Autonomy public-indicator hunt gen 1557

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260831T080820Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret266_neg_at_h` | one_head_filter_pi_star | 149 | 12.1719 | 2.3624 | 0.7181 | 4.5470 | 0.0289 | 0.4161 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret266_neg_at_h` | one_head_filter_pi_star | 172 | 14.0508 | 2.0819 | 0.7035 | 4.4284 | 0.0252 | 0.3779 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret266_neg_at_h` | one_head_filter_pi_star | 186 | 15.2094 | 1.8995 | 0.6667 | 3.7118 | 0.0129 | 0.3387 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret266_neg_at_h` | one_head_filter_pi_star | 182 | 14.8823 | 1.8300 | 0.6703 | 3.5481 | 0.0127 | 0.3352 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ret266_pos_at_h` | one_head_filter_pi_star | 178 | 14.5142 | 1.5717 | 0.6180 | 2.5071 | 0.0095 | 0.2809 | ok | RAN |
| SOLUSDT | 8 | `ret266_pos_at_h` | one_head_filter_pi_star | 178 | 14.5969 | 1.5564 | 0.6236 | 2.4517 | 0.0088 | 0.2865 | ok | RAN |
| ETHUSDT | 8 | `ret266_pos_at_h` | one_head_filter_pi_star | 184 | 15.1246 | 1.2440 | 0.6087 | 1.2407 | 0.0084 | 0.2120 | ok | RAN |
| ETHUSDT | 4 | `ret266_pos_at_h` | one_head_filter_pi_star | 176 | 14.4670 | 1.1685 | 0.5966 | 0.8655 | 0.0059 | 0.2159 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret266_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0411 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret266_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret266_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret266_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret266_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret266_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret266_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret266_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret266_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret266_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret266_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret266_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret266_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret266_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret266_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret266_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
