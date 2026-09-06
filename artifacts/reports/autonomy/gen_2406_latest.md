# Autonomy public-indicator hunt gen 2406

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T143248Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma553_below_at_h` | one_head_filter_pi_star | 179 | 14.6227 | 1.1896 | 0.5978 | 1.1037 | 0.0058 | 0.1955 | ok | RAN |
| ETHUSDT | 4 | `wma553_below_at_h` | one_head_filter_pi_star | 186 | 15.1945 | 1.1535 | 0.5914 | 0.9115 | 0.0047 | 0.1882 | ok | RAN |
| SOLUSDT | 8 | `wma553_above_at_h` | one_head_filter_pi_star | 189 | 15.4111 | 1.0384 | 0.5450 | 0.2267 | 0.0007 | 0.1005 | ok | RAN |
| SOLUSDT | 4 | `wma553_above_at_h` | one_head_filter_pi_star | 184 | 15.0034 | 1.0182 | 0.5380 | 0.1056 | 0.0003 | 0.1033 | ok | RAN |
| SOLUSDT | 4 | `wma553_below_at_h` | one_head_filter_pi_star | 185 | 15.1276 | 1.0095 | 0.5568 | 0.0565 | 0.0002 | 0.1514 | ok | RAN |
| SOLUSDT | 8 | `wma553_below_at_h` | one_head_filter_pi_star | 195 | 15.9453 | 1.0066 | 0.5590 | 0.0409 | 0.0001 | 0.1590 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `wma553_above_at_h` | one_head_filter_pi_star | 185 | 15.2068 | 0.8341 | 0.5405 | -1.0642 | -0.0068 | 0.0973 | ok | RAN |
| ETHUSDT | 4 | `wma553_above_at_h` | one_head_filter_pi_star | 191 | 15.7000 | 0.8028 | 0.5183 | -1.3002 | -0.0083 | 0.0942 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma553_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0682 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma553_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma553_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma553_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma553_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma553_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma553_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma553_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma553_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma553_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma553_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma553_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma553_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma553_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma553_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma553_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
