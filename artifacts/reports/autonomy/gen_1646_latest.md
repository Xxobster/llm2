# Autonomy public-indicator hunt gen 1646

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260901T224700Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma434_below_at_h` | one_head_filter_pi_star | 186 | 15.1945 | 1.1956 | 0.5968 | 1.1314 | 0.0059 | 0.1882 | ok | RAN |
| ETHUSDT | 4 | `wma434_below_at_h` | one_head_filter_pi_star | 184 | 15.0311 | 1.1245 | 0.5924 | 0.7474 | 0.0038 | 0.1902 | ok | RAN |
| SOLUSDT | 8 | `wma434_below_at_h` | one_head_filter_pi_star | 173 | 14.1464 | 1.1367 | 0.5780 | 0.7313 | 0.0027 | 0.1676 | ok | RAN |
| SOLUSDT | 8 | `wma434_above_at_h` | one_head_filter_pi_star | 187 | 15.2481 | 1.0454 | 0.5455 | 0.2616 | 0.0008 | 0.1016 | ok | RAN |
| SOLUSDT | 4 | `wma434_below_at_h` | one_head_filter_pi_star | 172 | 14.0646 | 1.0256 | 0.5640 | 0.1449 | 0.0005 | 0.1570 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `wma434_above_at_h` | one_head_filter_pi_star | 188 | 15.3296 | 0.9767 | 0.5319 | -0.1361 | -0.0004 | 0.1064 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `wma434_above_at_h` | one_head_filter_pi_star | 186 | 15.2890 | 0.8468 | 0.5269 | -0.9444 | -0.0061 | 0.1022 | ok | RAN |
| ETHUSDT | 8 | `wma434_above_at_h` | one_head_filter_pi_star | 193 | 15.8644 | 0.7673 | 0.5233 | -1.5420 | -0.0098 | 0.0881 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma434_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma434_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma434_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma434_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma434_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma434_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma434_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma434_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma434_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma434_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma434_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma434_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma434_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma434_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma434_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma434_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
