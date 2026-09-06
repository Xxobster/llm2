# Autonomy public-indicator hunt gen 2078

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T191017Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma502_below_at_h` | one_head_filter_pi_star | 181 | 14.7860 | 1.1526 | 0.5912 | 0.8830 | 0.0046 | 0.1823 | ok | RAN |
| ETHUSDT | 4 | `wma502_below_at_h` | one_head_filter_pi_star | 187 | 15.2762 | 1.1270 | 0.5882 | 0.7727 | 0.0040 | 0.1979 | ok | RAN |
| SOLUSDT | 8 | `wma502_above_at_h` | one_head_filter_pi_star | 176 | 14.3511 | 1.0598 | 0.5455 | 0.3235 | 0.0011 | 0.1023 | ok | RAN |
| SOLUSDT | 8 | `wma502_below_at_h` | one_head_filter_pi_star | 185 | 15.1276 | 1.0329 | 0.5622 | 0.1947 | 0.0007 | 0.1568 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `wma502_above_at_h` | one_head_filter_pi_star | 189 | 15.4111 | 0.9998 | 0.5397 | -0.0013 | -0.0000 | 0.1005 | ok | RAN |
| SOLUSDT | 4 | `wma502_below_at_h` | one_head_filter_pi_star | 190 | 15.5365 | 0.9996 | 0.5526 | -0.0020 | -0.0000 | 0.1474 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `wma502_above_at_h` | one_head_filter_pi_star | 188 | 15.4534 | 0.8079 | 0.5213 | -1.2356 | -0.0079 | 0.0957 | ok | RAN |
| ETHUSDT | 8 | `wma502_above_at_h` | one_head_filter_pi_star | 183 | 15.0424 | 0.7684 | 0.5191 | -1.4715 | -0.0095 | 0.0874 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma502_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma502_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0709 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma502_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma502_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma502_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma502_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma502_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma502_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma502_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma502_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma502_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma502_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma502_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma502_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma502_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma502_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
