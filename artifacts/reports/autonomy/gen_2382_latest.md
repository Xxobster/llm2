# Autonomy public-indicator hunt gen 2382

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T113216Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma549_below_at_h` | one_head_filter_pi_star | 184 | 15.0311 | 1.1488 | 0.5924 | 0.8702 | 0.0046 | 0.1902 | ok | RAN |
| ETHUSDT | 4 | `wma549_below_at_h` | one_head_filter_pi_star | 183 | 14.9494 | 1.1395 | 0.5902 | 0.8278 | 0.0043 | 0.1913 | ok | RAN |
| SOLUSDT | 4 | `wma549_above_at_h` | one_head_filter_pi_star | 190 | 15.4927 | 1.1589 | 0.5632 | 0.8758 | 0.0028 | 0.1000 | ok | RAN |
| SOLUSDT | 8 | `wma549_above_at_h` | one_head_filter_pi_star | 190 | 15.4927 | 1.1102 | 0.5526 | 0.6207 | 0.0019 | 0.0947 | ok | RAN |
| SOLUSDT | 8 | `wma549_below_at_h` | one_head_filter_pi_star | 185 | 15.1276 | 1.0054 | 0.5622 | 0.0322 | 0.0001 | 0.1514 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `wma549_below_at_h` | one_head_filter_pi_star | 180 | 14.7188 | 0.9853 | 0.5500 | -0.0894 | -0.0003 | 0.1556 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `wma549_above_at_h` | one_head_filter_pi_star | 181 | 14.8780 | 0.8434 | 0.5359 | -0.9823 | -0.0064 | 0.0994 | ok | RAN |
| ETHUSDT | 4 | `wma549_above_at_h` | one_head_filter_pi_star | 186 | 15.3490 | 0.7840 | 0.5269 | -1.4195 | -0.0092 | 0.0914 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma549_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0682 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma549_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0709 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma549_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma549_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma549_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma549_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma549_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma549_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma549_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma549_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma549_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma549_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma549_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma549_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma549_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma549_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
