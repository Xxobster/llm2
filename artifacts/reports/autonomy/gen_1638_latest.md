# Autonomy public-indicator hunt gen 1638

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260901T214011Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma433_below_at_h` | one_head_filter_pi_star | 190 | 15.5213 | 1.1729 | 0.5895 | 1.0132 | 0.0052 | 0.1895 | ok | RAN |
| ETHUSDT | 4 | `wma433_below_at_h` | one_head_filter_pi_star | 176 | 14.3776 | 1.0831 | 0.5852 | 0.4976 | 0.0027 | 0.2045 | ok | RAN |
| SOLUSDT | 4 | `wma433_below_at_h` | one_head_filter_pi_star | 161 | 13.1651 | 1.0642 | 0.5714 | 0.3424 | 0.0013 | 0.1429 | ok | RAN |
| SOLUSDT | 8 | `wma433_below_at_h` | one_head_filter_pi_star | 175 | 14.3099 | 1.0459 | 0.5657 | 0.2595 | 0.0009 | 0.1600 | ok | RAN |
| SOLUSDT | 8 | `wma433_above_at_h` | one_head_filter_pi_star | 192 | 15.6558 | 1.0221 | 0.5469 | 0.1290 | 0.0004 | 0.1042 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `wma433_above_at_h` | one_head_filter_pi_star | 198 | 16.1450 | 0.9817 | 0.5404 | -0.1110 | -0.0003 | 0.1061 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `wma433_above_at_h` | one_head_filter_pi_star | 192 | 15.7822 | 0.8559 | 0.5312 | -0.8946 | -0.0058 | 0.0990 | ok | RAN |
| ETHUSDT | 8 | `wma433_above_at_h` | one_head_filter_pi_star | 189 | 15.5356 | 0.7952 | 0.5291 | -1.3131 | -0.0086 | 0.0899 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma433_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0682 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma433_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma433_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma433_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma433_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma433_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma433_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma433_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma433_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma433_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma433_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma433_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma433_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma433_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma433_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma433_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
