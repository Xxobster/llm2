# Autonomy public-indicator hunt gen 1718

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T064728Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma446_below_at_h` | one_head_filter_pi_star | 171 | 13.9691 | 1.1967 | 0.6023 | 1.1061 | 0.0060 | 0.1988 | ok | RAN |
| ETHUSDT | 8 | `wma446_below_at_h` | one_head_filter_pi_star | 187 | 15.2762 | 1.1560 | 0.5882 | 0.9226 | 0.0048 | 0.1979 | ok | RAN |
| SOLUSDT | 8 | `wma446_below_at_h` | one_head_filter_pi_star | 171 | 13.9828 | 1.1123 | 0.5731 | 0.6053 | 0.0023 | 0.1637 | ok | RAN |
| SOLUSDT | 8 | `wma446_above_at_h` | one_head_filter_pi_star | 189 | 15.4111 | 1.0483 | 0.5556 | 0.2768 | 0.0009 | 0.0952 | ok | RAN |
| SOLUSDT | 4 | `wma446_below_at_h` | one_head_filter_pi_star | 167 | 13.6557 | 1.0263 | 0.5689 | 0.1464 | 0.0006 | 0.1497 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `wma446_above_at_h` | one_head_filter_pi_star | 196 | 15.9819 | 0.9841 | 0.5357 | -0.0947 | -0.0003 | 0.1122 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `wma446_above_at_h` | one_head_filter_pi_star | 185 | 15.2068 | 0.8244 | 0.5297 | -1.1081 | -0.0071 | 0.0973 | ok | RAN |
| ETHUSDT | 8 | `wma446_above_at_h` | one_head_filter_pi_star | 189 | 15.5356 | 0.8206 | 0.5344 | -1.1336 | -0.0072 | 0.0952 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma446_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5128 | 0.2778 | -1.0553 | -0.0479 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma446_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0709 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma446_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma446_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma446_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma446_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma446_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma446_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma446_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma446_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma446_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma446_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma446_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma446_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma446_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma446_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
