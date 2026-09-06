# Autonomy public-indicator hunt gen 2206

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T131716Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma522_below_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 1.0953 | 0.5820 | 0.5798 | 0.0030 | 0.1852 | ok | RAN |
| ETHUSDT | 4 | `wma522_below_at_h` | one_head_filter_pi_star | 185 | 15.1128 | 1.0675 | 0.5730 | 0.4180 | 0.0022 | 0.1892 | ok | RAN |
| SOLUSDT | 4 | `wma522_above_at_h` | one_head_filter_pi_star | 183 | 14.9219 | 1.0620 | 0.5519 | 0.3458 | 0.0011 | 0.0984 | ok | RAN |
| SOLUSDT | 8 | `wma522_above_at_h` | one_head_filter_pi_star | 186 | 15.1665 | 1.0514 | 0.5484 | 0.2880 | 0.0009 | 0.0968 | ok | RAN |
| SOLUSDT | 4 | `wma522_below_at_h` | one_head_filter_pi_star | 181 | 14.8005 | 1.0234 | 0.5691 | 0.1389 | 0.0005 | 0.1547 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `wma522_below_at_h` | one_head_filter_pi_star | 190 | 15.5365 | 0.9600 | 0.5474 | -0.2402 | -0.0009 | 0.1526 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `wma522_above_at_h` | one_head_filter_pi_star | 196 | 16.1109 | 0.8166 | 0.5306 | -1.2056 | -0.0074 | 0.0918 | ok | RAN |
| ETHUSDT | 8 | `wma522_above_at_h` | one_head_filter_pi_star | 186 | 15.3490 | 0.7852 | 0.5215 | -1.4268 | -0.0090 | 0.0860 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma522_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0682 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma522_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0709 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma522_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma522_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma522_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma522_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma522_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma522_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma522_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma522_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma522_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma522_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma522_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma522_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma522_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma522_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
