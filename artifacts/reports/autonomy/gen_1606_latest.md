# Autonomy public-indicator hunt gen 1606

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260901T184447Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma428_below_at_h` | one_head_filter_pi_star | 188 | 15.3579 | 1.1543 | 0.5851 | 0.9155 | 0.0048 | 0.1862 | ok | RAN |
| ETHUSDT | 4 | `wma428_below_at_h` | one_head_filter_pi_star | 175 | 14.2959 | 1.1135 | 0.5886 | 0.6678 | 0.0036 | 0.2000 | ok | RAN |
| SOLUSDT | 8 | `wma428_below_at_h` | one_head_filter_pi_star | 167 | 13.6557 | 1.0942 | 0.5689 | 0.5155 | 0.0019 | 0.1677 | ok | RAN |
| SOLUSDT | 4 | `wma428_below_at_h` | one_head_filter_pi_star | 174 | 14.2281 | 1.0668 | 0.5690 | 0.3738 | 0.0014 | 0.1609 | ok | RAN |
| SOLUSDT | 4 | `wma428_above_at_h` | one_head_filter_pi_star | 189 | 15.4111 | 1.0059 | 0.5397 | 0.0345 | 0.0001 | 0.1058 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `wma428_above_at_h` | one_head_filter_pi_star | 177 | 14.4326 | 0.9940 | 0.5424 | -0.0349 | -0.0001 | 0.1073 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `wma428_above_at_h` | one_head_filter_pi_star | 180 | 14.7958 | 0.8463 | 0.5389 | -0.9482 | -0.0062 | 0.1000 | ok | RAN |
| ETHUSDT | 8 | `wma428_above_at_h` | one_head_filter_pi_star | 185 | 15.2068 | 0.8418 | 0.5405 | -0.9905 | -0.0064 | 0.0919 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma428_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0709 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma428_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0722 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma428_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma428_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma428_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma428_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma428_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma428_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma428_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma428_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma428_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma428_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma428_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma428_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma428_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma428_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
