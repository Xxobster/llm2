# Autonomy public-indicator hunt gen 1734

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T082216Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma448_below_at_h` | one_head_filter_pi_star | 182 | 14.8677 | 1.1716 | 0.5989 | 0.9919 | 0.0053 | 0.1868 | ok | RAN |
| ETHUSDT | 8 | `wma448_below_at_h` | one_head_filter_pi_star | 188 | 15.3579 | 1.1587 | 0.5904 | 0.9428 | 0.0049 | 0.1915 | ok | RAN |
| SOLUSDT | 8 | `wma448_below_at_h` | one_head_filter_pi_star | 177 | 14.4734 | 1.0923 | 0.5706 | 0.5151 | 0.0019 | 0.1582 | ok | RAN |
| SOLUSDT | 4 | `wma448_below_at_h` | one_head_filter_pi_star | 170 | 13.9010 | 1.0868 | 0.5824 | 0.4780 | 0.0018 | 0.1588 | ok | RAN |
| SOLUSDT | 4 | `wma448_above_at_h` | one_head_filter_pi_star | 186 | 15.1665 | 1.0209 | 0.5376 | 0.1208 | 0.0004 | 0.1022 | ok | RAN |
| SOLUSDT | 8 | `wma448_above_at_h` | one_head_filter_pi_star | 189 | 15.4111 | 1.0192 | 0.5450 | 0.1123 | 0.0003 | 0.1058 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `wma448_above_at_h` | one_head_filter_pi_star | 188 | 15.4534 | 0.8082 | 0.5372 | -1.2321 | -0.0081 | 0.0957 | ok | RAN |
| ETHUSDT | 4 | `wma448_above_at_h` | one_head_filter_pi_star | 184 | 15.1839 | 0.8035 | 0.5272 | -1.2498 | -0.0082 | 0.0924 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma448_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma448_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4116 | 0.2778 | -1.4041 | -0.0721 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma448_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma448_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma448_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma448_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma448_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma448_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma448_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma448_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma448_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma448_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma448_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma448_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma448_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma448_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
