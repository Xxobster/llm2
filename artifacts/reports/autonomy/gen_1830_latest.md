# Autonomy public-indicator hunt gen 1830

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T170756Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma463_below_at_h` | one_head_filter_pi_star | 186 | 15.1945 | 1.1604 | 0.6022 | 0.9406 | 0.0050 | 0.1935 | ok | RAN |
| ETHUSDT | 4 | `wma463_below_at_h` | one_head_filter_pi_star | 183 | 14.9494 | 1.1259 | 0.5902 | 0.7601 | 0.0040 | 0.2022 | ok | RAN |
| SOLUSDT | 8 | `wma463_below_at_h` | one_head_filter_pi_star | 170 | 13.9010 | 1.0983 | 0.5765 | 0.5293 | 0.0020 | 0.1647 | ok | RAN |
| SOLUSDT | 4 | `wma463_below_at_h` | one_head_filter_pi_star | 173 | 14.1464 | 1.0603 | 0.5723 | 0.3441 | 0.0012 | 0.1618 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `wma463_above_at_h` | one_head_filter_pi_star | 188 | 15.3296 | 0.9818 | 0.5319 | -0.1070 | -0.0003 | 0.1064 | ok | RAN |
| SOLUSDT | 4 | `wma463_above_at_h` | one_head_filter_pi_star | 183 | 14.9219 | 0.9640 | 0.5355 | -0.2117 | -0.0007 | 0.1038 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `wma463_above_at_h` | one_head_filter_pi_star | 176 | 14.5238 | 0.8025 | 0.5398 | -1.2133 | -0.0081 | 0.0852 | ok | RAN |
| ETHUSDT | 4 | `wma463_above_at_h` | one_head_filter_pi_star | 188 | 15.4534 | 0.8010 | 0.5266 | -1.2804 | -0.0082 | 0.0957 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma463_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma463_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0709 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma463_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma463_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma463_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma463_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma463_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma463_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma463_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma463_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma463_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma463_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma463_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma463_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma463_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma463_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
