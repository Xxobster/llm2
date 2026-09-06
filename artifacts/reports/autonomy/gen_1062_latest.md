# Autonomy public-indicator hunt gen 1062

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T180545Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma570_below_at_h` | one_head_filter_pi_star | 188 | 15.3579 | 2.0238 | 0.6968 | 4.4915 | 0.0236 | 0.3830 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma570_below_at_h` | one_head_filter_pi_star | 194 | 15.8480 | 1.9709 | 0.6907 | 4.3662 | 0.0231 | 0.3763 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `wma570_below_at_h` | one_head_filter_pi_star | 192 | 15.7000 | 1.9289 | 0.6615 | 3.8020 | 0.0137 | 0.3542 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma570_below_at_h` | one_head_filter_pi_star | 201 | 16.4359 | 1.9120 | 0.6667 | 3.8166 | 0.0135 | 0.3632 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `wma570_above_at_h` | one_head_filter_pi_star | 191 | 15.7000 | 1.2523 | 0.6073 | 1.3170 | 0.0089 | 0.2199 | ok | RAN |
| SOLUSDT | 4 | `wma570_above_at_h` | one_head_filter_pi_star | 195 | 15.9004 | 1.5000 | 0.6051 | 2.4353 | 0.0077 | 0.2564 | ok | RAN |
| SOLUSDT | 8 | `wma570_above_at_h` | one_head_filter_pi_star | 188 | 15.3296 | 1.4646 | 0.6117 | 2.2414 | 0.0073 | 0.2606 | ok | RAN |
| ETHUSDT | 8 | `wma570_above_at_h` | one_head_filter_pi_star | 182 | 15.0189 | 1.2019 | 0.5934 | 1.0788 | 0.0072 | 0.2143 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma570_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma570_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma570_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma570_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma570_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma570_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma570_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma570_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma570_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma570_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma570_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma570_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma570_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma570_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma570_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma570_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
