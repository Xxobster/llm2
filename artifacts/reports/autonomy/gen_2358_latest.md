# Autonomy public-indicator hunt gen 2358

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T080836Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma546_below_at_h` | one_head_filter_pi_star | 179 | 14.6227 | 1.1707 | 0.5922 | 0.9523 | 0.0052 | 0.1899 | ok | RAN |
| ETHUSDT | 8 | `wma546_below_at_h` | one_head_filter_pi_star | 186 | 15.1945 | 1.1135 | 0.5914 | 0.6893 | 0.0035 | 0.1882 | ok | RAN |
| SOLUSDT | 4 | `wma546_above_at_h` | one_head_filter_pi_star | 185 | 15.0850 | 1.0420 | 0.5459 | 0.2428 | 0.0008 | 0.0973 | ok | RAN |
| SOLUSDT | 8 | `wma546_above_at_h` | one_head_filter_pi_star | 188 | 15.3296 | 1.0201 | 0.5479 | 0.1194 | 0.0004 | 0.0957 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `wma546_below_at_h` | one_head_filter_pi_star | 189 | 15.4547 | 0.9453 | 0.5450 | -0.3415 | -0.0012 | 0.1587 | ok | RAN |
| SOLUSDT | 4 | `wma546_below_at_h` | one_head_filter_pi_star | 183 | 14.9641 | 0.9399 | 0.5410 | -0.3638 | -0.0013 | 0.1585 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `wma546_above_at_h` | one_head_filter_pi_star | 188 | 15.4534 | 0.8152 | 0.5319 | -1.1969 | -0.0078 | 0.1011 | ok | RAN |
| ETHUSDT | 8 | `wma546_above_at_h` | one_head_filter_pi_star | 186 | 15.2890 | 0.7851 | 0.5269 | -1.4270 | -0.0090 | 0.0968 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma546_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma546_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0709 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma546_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma546_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma546_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma546_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma546_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma546_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma546_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma546_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma546_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma546_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma546_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma546_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma546_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma546_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
