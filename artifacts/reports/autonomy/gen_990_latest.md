# Autonomy public-indicator hunt gen 990

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260827T183335Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma525_below_at_h` | one_head_filter_pi_star | 190 | 15.5213 | 1.9692 | 0.6947 | 4.3742 | 0.0233 | 0.3895 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma525_below_at_h` | one_head_filter_pi_star | 196 | 16.0114 | 1.9314 | 0.6837 | 4.2371 | 0.0220 | 0.3673 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `wma525_below_at_h` | one_head_filter_pi_star | 186 | 15.2094 | 2.0285 | 0.6828 | 4.0612 | 0.0149 | 0.3710 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma525_below_at_h` | one_head_filter_pi_star | 186 | 15.2094 | 2.0342 | 0.6828 | 4.0586 | 0.0148 | 0.3602 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `wma525_above_at_h` | one_head_filter_pi_star | 184 | 15.1246 | 1.2813 | 0.6087 | 1.4322 | 0.0097 | 0.2228 | ok | RAN |
| SOLUSDT | 8 | `wma525_above_at_h` | one_head_filter_pi_star | 189 | 15.4111 | 1.5409 | 0.6032 | 2.5317 | 0.0083 | 0.2593 | ok | RAN |
| SOLUSDT | 4 | `wma525_above_at_h` | one_head_filter_pi_star | 191 | 15.5742 | 1.5376 | 0.6126 | 2.5333 | 0.0082 | 0.2618 | ok | RAN |
| ETHUSDT | 4 | `wma525_above_at_h` | one_head_filter_pi_star | 188 | 15.4534 | 1.2003 | 0.5957 | 1.0619 | 0.0072 | 0.2234 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma525_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma525_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma525_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma525_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma525_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma525_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma525_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma525_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma525_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma525_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma525_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma525_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma525_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma525_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma525_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma525_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
