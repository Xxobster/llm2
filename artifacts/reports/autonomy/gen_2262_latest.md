# Autonomy public-indicator hunt gen 2262

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T200711Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma531_below_at_h` | one_head_filter_pi_star | 184 | 15.0311 | 1.1439 | 0.5924 | 0.8452 | 0.0044 | 0.1902 | ok | RAN |
| ETHUSDT | 8 | `wma531_below_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 1.0884 | 0.5820 | 0.5429 | 0.0028 | 0.1852 | ok | RAN |
| SOLUSDT | 8 | `wma531_above_at_h` | one_head_filter_pi_star | 193 | 15.7373 | 1.0569 | 0.5544 | 0.3324 | 0.0011 | 0.0933 | ok | RAN |
| SOLUSDT | 4 | `wma531_above_at_h` | one_head_filter_pi_star | 180 | 14.6773 | 1.0209 | 0.5444 | 0.1194 | 0.0004 | 0.1000 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `wma531_below_at_h` | one_head_filter_pi_star | 190 | 15.5365 | 0.9860 | 0.5526 | -0.0859 | -0.0003 | 0.1526 | ok | RAN |
| SOLUSDT | 8 | `wma531_below_at_h` | one_head_filter_pi_star | 196 | 16.0271 | 0.9779 | 0.5510 | -0.1374 | -0.0005 | 0.1531 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `wma531_above_at_h` | one_head_filter_pi_star | 189 | 15.5356 | 0.8203 | 0.5238 | -1.1528 | -0.0074 | 0.0952 | ok | RAN |
| ETHUSDT | 4 | `wma531_above_at_h` | one_head_filter_pi_star | 189 | 15.5356 | 0.8040 | 0.5238 | -1.2707 | -0.0085 | 0.1005 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma531_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0682 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma531_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0709 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma531_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma531_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma531_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma531_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma531_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma531_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma531_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma531_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma531_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma531_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma531_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma531_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma531_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma531_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
