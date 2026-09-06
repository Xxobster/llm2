# Autonomy public-indicator hunt gen 2502

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260906T012208Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma568_below_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 1.1877 | 0.6085 | 1.0957 | 0.0056 | 0.1905 | ok | RAN |
| ETHUSDT | 4 | `wma568_below_at_h` | one_head_filter_pi_star | 191 | 15.6030 | 1.1419 | 0.5916 | 0.8575 | 0.0043 | 0.1832 | ok | RAN |
| SOLUSDT | 8 | `wma568_above_at_h` | one_head_filter_pi_star | 181 | 14.7588 | 1.0332 | 0.5359 | 0.1915 | 0.0006 | 0.1050 | ok | RAN |
| SOLUSDT | 4 | `wma568_above_at_h` | one_head_filter_pi_star | 189 | 15.4111 | 1.0234 | 0.5450 | 0.1387 | 0.0004 | 0.1005 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `wma568_below_at_h` | one_head_filter_pi_star | 192 | 15.7000 | 0.9789 | 0.5469 | -0.1299 | -0.0004 | 0.1458 | ok | RAN |
| SOLUSDT | 8 | `wma568_below_at_h` | one_head_filter_pi_star | 195 | 15.9453 | 0.9442 | 0.5385 | -0.3520 | -0.0012 | 0.1590 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `wma568_above_at_h` | one_head_filter_pi_star | 179 | 14.7136 | 0.8637 | 0.5531 | -0.8482 | -0.0054 | 0.1006 | ok | RAN |
| ETHUSDT | 4 | `wma568_above_at_h` | one_head_filter_pi_star | 186 | 15.2890 | 0.8652 | 0.5430 | -0.8347 | -0.0055 | 0.0968 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma568_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma568_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma568_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma568_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma568_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma568_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma568_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma568_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma568_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma568_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma568_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma568_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma568_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma568_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma568_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma568_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
