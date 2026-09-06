# Autonomy public-indicator hunt gen 1862

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T195806Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma468_below_at_h` | one_head_filter_pi_star | 187 | 15.2762 | 1.1807 | 0.5936 | 1.0530 | 0.0055 | 0.1979 | ok | RAN |
| ETHUSDT | 4 | `wma468_below_at_h` | one_head_filter_pi_star | 174 | 14.2142 | 1.1711 | 0.5977 | 0.9817 | 0.0052 | 0.2011 | ok | RAN |
| SOLUSDT | 4 | `wma468_below_at_h` | one_head_filter_pi_star | 174 | 14.2281 | 1.0655 | 0.5747 | 0.3666 | 0.0013 | 0.1609 | ok | RAN |
| SOLUSDT | 8 | `wma468_below_at_h` | one_head_filter_pi_star | 168 | 13.7375 | 1.0487 | 0.5655 | 0.2707 | 0.0010 | 0.1667 | ok | RAN |
| SOLUSDT | 4 | `wma468_above_at_h` | one_head_filter_pi_star | 187 | 15.2481 | 1.0263 | 0.5455 | 0.1506 | 0.0005 | 0.1016 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `wma468_above_at_h` | one_head_filter_pi_star | 179 | 14.5957 | 0.9790 | 0.5251 | -0.1235 | -0.0004 | 0.1006 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `wma468_above_at_h` | one_head_filter_pi_star | 186 | 15.2890 | 0.8080 | 0.5376 | -1.2256 | -0.0079 | 0.0914 | ok | RAN |
| ETHUSDT | 4 | `wma468_above_at_h` | one_head_filter_pi_star | 191 | 15.7000 | 0.7930 | 0.5236 | -1.3435 | -0.0085 | 0.0942 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma468_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5128 | 0.2778 | -1.0553 | -0.0461 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma468_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0682 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma468_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma468_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma468_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma468_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma468_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma468_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma468_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma468_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma468_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma468_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma468_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma468_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma468_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma468_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
