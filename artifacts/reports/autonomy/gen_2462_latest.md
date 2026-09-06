# Autonomy public-indicator hunt gen 2462

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T210126Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma562_below_at_h` | one_head_filter_pi_star | 182 | 14.8677 | 1.1873 | 0.5989 | 1.0834 | 0.0056 | 0.1868 | ok | RAN |
| ETHUSDT | 8 | `wma562_below_at_h` | one_head_filter_pi_star | 183 | 14.9494 | 1.1403 | 0.5902 | 0.8189 | 0.0043 | 0.1858 | ok | RAN |
| SOLUSDT | 8 | `wma562_above_at_h` | one_head_filter_pi_star | 189 | 15.4111 | 1.1121 | 0.5450 | 0.6233 | 0.0020 | 0.0952 | ok | RAN |
| SOLUSDT | 4 | `wma562_above_at_h` | one_head_filter_pi_star | 185 | 15.0850 | 1.0856 | 0.5568 | 0.4826 | 0.0016 | 0.1027 | ok | RAN |
| SOLUSDT | 8 | `wma562_below_at_h` | one_head_filter_pi_star | 195 | 15.9453 | 1.0141 | 0.5590 | 0.0864 | 0.0003 | 0.1538 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `wma562_below_at_h` | one_head_filter_pi_star | 196 | 16.0271 | 0.9756 | 0.5561 | -0.1525 | -0.0005 | 0.1480 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `wma562_above_at_h` | one_head_filter_pi_star | 187 | 15.3712 | 0.8796 | 0.5455 | -0.7335 | -0.0049 | 0.1016 | ok | RAN |
| ETHUSDT | 8 | `wma562_above_at_h` | one_head_filter_pi_star | 190 | 15.6178 | 0.8010 | 0.5316 | -1.3155 | -0.0084 | 0.1000 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma562_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0709 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma562_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0709 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma562_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma562_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma562_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma562_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma562_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma562_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma562_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma562_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma562_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma562_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma562_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma562_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma562_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma562_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
