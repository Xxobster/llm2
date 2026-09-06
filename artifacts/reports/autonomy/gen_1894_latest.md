# Autonomy public-indicator hunt gen 1894

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T225217Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma473_below_at_h` | one_head_filter_pi_star | 181 | 14.7860 | 1.1267 | 0.5912 | 0.7620 | 0.0040 | 0.1989 | ok | RAN |
| ETHUSDT | 8 | `wma473_below_at_h` | one_head_filter_pi_star | 181 | 14.7860 | 1.1203 | 0.5856 | 0.7056 | 0.0037 | 0.1934 | ok | RAN |
| SOLUSDT | 4 | `wma473_below_at_h` | one_head_filter_pi_star | 174 | 14.2281 | 1.0528 | 0.5690 | 0.2897 | 0.0011 | 0.1609 | ok | RAN |
| SOLUSDT | 8 | `wma473_below_at_h` | one_head_filter_pi_star | 174 | 14.2281 | 1.0364 | 0.5690 | 0.2065 | 0.0008 | 0.1667 | ok | RAN |
| SOLUSDT | 8 | `wma473_above_at_h` | one_head_filter_pi_star | 185 | 15.0850 | 1.0374 | 0.5405 | 0.2129 | 0.0007 | 0.0973 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `wma473_above_at_h` | one_head_filter_pi_star | 193 | 15.7373 | 0.9910 | 0.5337 | -0.0538 | -0.0002 | 0.0984 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `wma473_above_at_h` | one_head_filter_pi_star | 190 | 15.6178 | 0.8168 | 0.5316 | -1.1718 | -0.0074 | 0.1000 | ok | RAN |
| ETHUSDT | 8 | `wma473_above_at_h` | one_head_filter_pi_star | 184 | 15.1246 | 0.7961 | 0.5380 | -1.3185 | -0.0087 | 0.0978 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma473_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma473_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma473_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma473_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma473_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma473_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma473_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma473_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma473_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma473_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma473_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma473_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma473_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma473_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma473_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma473_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
