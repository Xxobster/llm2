# Autonomy public-indicator hunt gen 2118

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T002922Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma508_below_at_h` | one_head_filter_pi_star | 177 | 14.4593 | 1.1634 | 0.5932 | 0.9272 | 0.0048 | 0.1864 | ok | RAN |
| ETHUSDT | 4 | `wma508_below_at_h` | one_head_filter_pi_star | 184 | 15.0311 | 1.1299 | 0.5924 | 0.7809 | 0.0041 | 0.2011 | ok | RAN |
| SOLUSDT | 8 | `wma508_above_at_h` | one_head_filter_pi_star | 179 | 14.5957 | 1.0992 | 0.5475 | 0.5392 | 0.0017 | 0.1006 | ok | RAN |
| SOLUSDT | 4 | `wma508_below_at_h` | one_head_filter_pi_star | 176 | 14.3917 | 1.0610 | 0.5739 | 0.3501 | 0.0013 | 0.1534 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `wma508_above_at_h` | one_head_filter_pi_star | 187 | 15.2481 | 0.9899 | 0.5241 | -0.0595 | -0.0002 | 0.1070 | ok | RAN |
| SOLUSDT | 8 | `wma508_below_at_h` | one_head_filter_pi_star | 186 | 15.2094 | 0.9883 | 0.5538 | -0.0711 | -0.0002 | 0.1613 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `wma508_above_at_h` | one_head_filter_pi_star | 189 | 15.5356 | 0.7958 | 0.5291 | -1.3413 | -0.0087 | 0.0952 | ok | RAN |
| ETHUSDT | 8 | `wma508_above_at_h` | one_head_filter_pi_star | 186 | 15.2890 | 0.7751 | 0.5269 | -1.4465 | -0.0096 | 0.0968 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma508_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma508_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0709 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma508_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma508_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma508_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma508_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma508_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma508_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma508_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma508_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma508_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma508_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma508_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma508_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma508_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma508_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
