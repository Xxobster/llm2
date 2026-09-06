# Autonomy public-indicator hunt gen 2526

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260906T035229Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma572_below_at_h` | one_head_filter_pi_star | 186 | 15.1945 | 1.1320 | 0.5914 | 0.7785 | 0.0041 | 0.1935 | ok | RAN |
| ETHUSDT | 4 | `wma572_below_at_h` | one_head_filter_pi_star | 186 | 15.1945 | 1.0745 | 0.5806 | 0.4643 | 0.0024 | 0.1882 | ok | RAN |
| SOLUSDT | 8 | `wma572_above_at_h` | one_head_filter_pi_star | 189 | 15.4111 | 1.0616 | 0.5503 | 0.3537 | 0.0011 | 0.1005 | ok | RAN |
| SOLUSDT | 4 | `wma572_above_at_h` | one_head_filter_pi_star | 183 | 14.9219 | 1.0473 | 0.5464 | 0.2733 | 0.0009 | 0.1038 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `wma572_below_at_h` | one_head_filter_pi_star | 185 | 15.1276 | 0.9860 | 0.5568 | -0.0842 | -0.0003 | 0.1568 | ok | RAN |
| SOLUSDT | 4 | `wma572_below_at_h` | one_head_filter_pi_star | 185 | 15.1276 | 0.9505 | 0.5459 | -0.3040 | -0.0011 | 0.1405 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `wma572_above_at_h` | one_head_filter_pi_star | 186 | 15.2890 | 0.8542 | 0.5430 | -0.9101 | -0.0058 | 0.0968 | ok | RAN |
| ETHUSDT | 4 | `wma572_above_at_h` | one_head_filter_pi_star | 190 | 15.6791 | 0.8336 | 0.5316 | -1.0593 | -0.0068 | 0.0947 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma572_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0682 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma572_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma572_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma572_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma572_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma572_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma572_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma572_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma572_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma572_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma572_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma572_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma572_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma572_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma572_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma572_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
