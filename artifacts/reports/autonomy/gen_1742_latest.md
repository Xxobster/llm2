# Autonomy public-indicator hunt gen 1742

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T090504Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma449_below_at_h` | one_head_filter_pi_star | 181 | 14.7860 | 1.1965 | 0.6022 | 1.1218 | 0.0059 | 0.1934 | ok | RAN |
| ETHUSDT | 4 | `wma449_below_at_h` | one_head_filter_pi_star | 188 | 15.3579 | 1.1140 | 0.5904 | 0.6952 | 0.0036 | 0.1968 | ok | RAN |
| SOLUSDT | 8 | `wma449_below_at_h` | one_head_filter_pi_star | 165 | 13.4922 | 1.1138 | 0.5818 | 0.6032 | 0.0023 | 0.1636 | ok | RAN |
| SOLUSDT | 4 | `wma449_below_at_h` | one_head_filter_pi_star | 170 | 13.9010 | 1.0186 | 0.5706 | 0.1019 | 0.0004 | 0.1529 | ok | RAN |
| SOLUSDT | 8 | `wma449_above_at_h` | one_head_filter_pi_star | 192 | 15.6558 | 1.0214 | 0.5521 | 0.1247 | 0.0004 | 0.1042 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `wma449_above_at_h` | one_head_filter_pi_star | 196 | 15.9819 | 0.9273 | 0.5306 | -0.4487 | -0.0014 | 0.1071 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `wma449_above_at_h` | one_head_filter_pi_star | 190 | 15.6178 | 0.8235 | 0.5263 | -1.1231 | -0.0071 | 0.0947 | ok | RAN |
| ETHUSDT | 8 | `wma449_above_at_h` | one_head_filter_pi_star | 193 | 15.8644 | 0.7720 | 0.5233 | -1.5030 | -0.0096 | 0.0881 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma449_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma449_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma449_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma449_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma449_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma449_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma449_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma449_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma449_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma449_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma449_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma449_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma449_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma449_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma449_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma449_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
