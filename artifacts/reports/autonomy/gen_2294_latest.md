# Autonomy public-indicator hunt gen 2294

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T235900Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma536_below_at_h` | one_head_filter_pi_star | 188 | 15.3579 | 1.1071 | 0.5851 | 0.6481 | 0.0033 | 0.1862 | ok | RAN |
| SOLUSDT | 8 | `wma536_above_at_h` | one_head_filter_pi_star | 181 | 14.7588 | 1.1702 | 0.5580 | 0.9038 | 0.0030 | 0.0994 | ok | RAN |
| ETHUSDT | 8 | `wma536_below_at_h` | one_head_filter_pi_star | 188 | 15.3579 | 1.0445 | 0.5745 | 0.2798 | 0.0015 | 0.1862 | ok | RAN |
| SOLUSDT | 8 | `wma536_below_at_h` | one_head_filter_pi_star | 184 | 15.0458 | 1.0400 | 0.5652 | 0.2353 | 0.0008 | 0.1576 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `wma536_below_at_h` | one_head_filter_pi_star | 180 | 14.7188 | 0.9960 | 0.5611 | -0.0238 | -0.0001 | 0.1556 | ok | RAN |
| SOLUSDT | 4 | `wma536_above_at_h` | one_head_filter_pi_star | 196 | 15.9819 | 0.9630 | 0.5306 | -0.2247 | -0.0007 | 0.1020 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `wma536_above_at_h` | one_head_filter_pi_star | 181 | 14.9364 | 0.8308 | 0.5304 | -1.0584 | -0.0068 | 0.0939 | ok | RAN |
| ETHUSDT | 4 | `wma536_above_at_h` | one_head_filter_pi_star | 181 | 14.8780 | 0.8060 | 0.5304 | -1.2278 | -0.0083 | 0.0939 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma536_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma536_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0709 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma536_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma536_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma536_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma536_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma536_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma536_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma536_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma536_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma536_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma536_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma536_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma536_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma536_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma536_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
