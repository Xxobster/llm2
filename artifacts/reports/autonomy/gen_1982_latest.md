# Autonomy public-indicator hunt gen 1982

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T070340Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma487_below_at_h` | one_head_filter_pi_star | 182 | 14.8677 | 1.1343 | 0.5879 | 0.8024 | 0.0042 | 0.2088 | ok | RAN |
| ETHUSDT | 8 | `wma487_below_at_h` | one_head_filter_pi_star | 185 | 15.1128 | 1.1188 | 0.5892 | 0.7125 | 0.0036 | 0.1838 | ok | RAN |
| SOLUSDT | 4 | `wma487_below_at_h` | one_head_filter_pi_star | 177 | 14.4734 | 1.0646 | 0.5706 | 0.3688 | 0.0013 | 0.1582 | ok | RAN |
| SOLUSDT | 8 | `wma487_above_at_h` | one_head_filter_pi_star | 182 | 14.8404 | 1.0256 | 0.5385 | 0.1467 | 0.0005 | 0.1044 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `wma487_above_at_h` | one_head_filter_pi_star | 184 | 15.0034 | 0.9804 | 0.5380 | -0.1156 | -0.0004 | 0.1087 | ok | RAN |
| SOLUSDT | 8 | `wma487_below_at_h` | one_head_filter_pi_star | 181 | 14.8005 | 0.9622 | 0.5470 | -0.2293 | -0.0008 | 0.1602 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `wma487_above_at_h` | one_head_filter_pi_star | 183 | 15.1014 | 0.8083 | 0.5301 | -1.2252 | -0.0079 | 0.0929 | ok | RAN |
| ETHUSDT | 8 | `wma487_above_at_h` | one_head_filter_pi_star | 192 | 15.7822 | 0.7921 | 0.5260 | -1.3576 | -0.0086 | 0.0938 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma487_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5128 | 0.2778 | -1.0553 | -0.0479 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma487_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma487_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma487_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma487_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma487_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma487_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma487_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma487_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma487_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma487_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma487_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma487_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma487_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma487_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma487_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
