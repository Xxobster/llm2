# Autonomy public-indicator hunt gen 1694

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T041433Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma442_below_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 1.1625 | 0.5926 | 0.9658 | 0.0049 | 0.1905 | ok | RAN |
| ETHUSDT | 4 | `wma442_below_at_h` | one_head_filter_pi_star | 186 | 15.1945 | 1.1016 | 0.5860 | 0.6284 | 0.0033 | 0.2043 | ok | RAN |
| SOLUSDT | 8 | `wma442_below_at_h` | one_head_filter_pi_star | 167 | 13.6557 | 1.1107 | 0.5749 | 0.5923 | 0.0022 | 0.1617 | ok | RAN |
| SOLUSDT | 4 | `wma442_below_at_h` | one_head_filter_pi_star | 178 | 14.5552 | 1.0818 | 0.5730 | 0.4498 | 0.0017 | 0.1573 | ok | RAN |
| SOLUSDT | 8 | `wma442_above_at_h` | one_head_filter_pi_star | 185 | 15.0850 | 1.0376 | 0.5568 | 0.2163 | 0.0007 | 0.0919 | ok | RAN |
| SOLUSDT | 4 | `wma442_above_at_h` | one_head_filter_pi_star | 188 | 15.3296 | 1.0266 | 0.5372 | 0.1528 | 0.0005 | 0.1011 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `wma442_above_at_h` | one_head_filter_pi_star | 189 | 15.5356 | 0.8535 | 0.5344 | -0.9120 | -0.0059 | 0.1005 | ok | RAN |
| ETHUSDT | 8 | `wma442_above_at_h` | one_head_filter_pi_star | 185 | 15.2068 | 0.8305 | 0.5405 | -1.0705 | -0.0069 | 0.0973 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma442_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0682 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma442_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0709 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma442_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma442_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma442_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma442_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma442_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma442_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma442_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma442_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma442_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma442_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma442_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma442_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma442_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma442_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
