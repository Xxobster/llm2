# Autonomy public-indicator hunt gen 2454

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T200739Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma561_below_at_h` | one_head_filter_pi_star | 178 | 14.5410 | 1.1738 | 0.6011 | 1.0049 | 0.0052 | 0.1966 | ok | RAN |
| ETHUSDT | 4 | `wma561_below_at_h` | one_head_filter_pi_star | 177 | 14.4593 | 1.1191 | 0.5876 | 0.6987 | 0.0037 | 0.1921 | ok | RAN |
| SOLUSDT | 4 | `wma561_above_at_h` | one_head_filter_pi_star | 180 | 14.6773 | 1.1480 | 0.5611 | 0.7970 | 0.0026 | 0.1056 | ok | RAN |
| SOLUSDT | 8 | `wma561_above_at_h` | one_head_filter_pi_star | 187 | 15.2481 | 1.0290 | 0.5348 | 0.1678 | 0.0005 | 0.0963 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `wma561_below_at_h` | one_head_filter_pi_star | 191 | 15.6182 | 0.9765 | 0.5497 | -0.1457 | -0.0005 | 0.1466 | ok | RAN |
| SOLUSDT | 8 | `wma561_below_at_h` | one_head_filter_pi_star | 193 | 15.7818 | 0.9720 | 0.5440 | -0.1740 | -0.0006 | 0.1606 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `wma561_above_at_h` | one_head_filter_pi_star | 191 | 15.7000 | 0.8361 | 0.5288 | -1.0410 | -0.0068 | 0.0995 | ok | RAN |
| ETHUSDT | 8 | `wma561_above_at_h` | one_head_filter_pi_star | 187 | 15.3712 | 0.8330 | 0.5294 | -1.0581 | -0.0069 | 0.1016 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma561_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0682 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma561_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma561_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma561_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma561_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma561_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma561_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma561_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma561_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma561_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma561_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma561_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma561_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma561_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma561_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma561_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
