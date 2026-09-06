# Autonomy public-indicator hunt gen 2350

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T070710Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma544_below_at_h` | one_head_filter_pi_star | 186 | 15.1945 | 1.1309 | 0.5860 | 0.7830 | 0.0041 | 0.1882 | ok | RAN |
| ETHUSDT | 4 | `wma544_below_at_h` | one_head_filter_pi_star | 188 | 15.3579 | 1.0888 | 0.5798 | 0.5521 | 0.0028 | 0.1915 | ok | RAN |
| SOLUSDT | 8 | `wma544_above_at_h` | one_head_filter_pi_star | 183 | 14.9219 | 1.0941 | 0.5574 | 0.5244 | 0.0017 | 0.0984 | ok | RAN |
| SOLUSDT | 4 | `wma544_above_at_h` | one_head_filter_pi_star | 183 | 14.9219 | 1.0935 | 0.5519 | 0.5090 | 0.0017 | 0.1038 | ok | RAN |
| SOLUSDT | 4 | `wma544_below_at_h` | one_head_filter_pi_star | 192 | 15.7000 | 1.0099 | 0.5573 | 0.0590 | 0.0002 | 0.1562 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `wma544_below_at_h` | one_head_filter_pi_star | 186 | 15.2094 | 0.9722 | 0.5538 | -0.1648 | -0.0006 | 0.1613 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `wma544_above_at_h` | one_head_filter_pi_star | 187 | 15.3712 | 0.8333 | 0.5294 | -1.0602 | -0.0067 | 0.0909 | ok | RAN |
| ETHUSDT | 4 | `wma544_above_at_h` | one_head_filter_pi_star | 192 | 15.7822 | 0.8064 | 0.5312 | -1.2690 | -0.0082 | 0.0938 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma544_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma544_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0709 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma544_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma544_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma544_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma544_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma544_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma544_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma544_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma544_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma544_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma544_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma544_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma544_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma544_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma544_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
