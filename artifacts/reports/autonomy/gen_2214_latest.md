# Autonomy public-indicator hunt gen 2214

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T142012Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma523_below_at_h` | one_head_filter_pi_star | 186 | 15.1945 | 1.1135 | 0.5914 | 0.6883 | 0.0036 | 0.1989 | ok | RAN |
| ETHUSDT | 8 | `wma523_below_at_h` | one_head_filter_pi_star | 190 | 15.5213 | 1.0841 | 0.5842 | 0.5154 | 0.0026 | 0.1789 | ok | RAN |
| SOLUSDT | 4 | `wma523_below_at_h` | one_head_filter_pi_star | 183 | 14.9641 | 1.0330 | 0.5628 | 0.1888 | 0.0007 | 0.1530 | ok | RAN |
| SOLUSDT | 8 | `wma523_above_at_h` | one_head_filter_pi_star | 189 | 15.4111 | 1.0240 | 0.5397 | 0.1402 | 0.0004 | 0.1005 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `wma523_below_at_h` | one_head_filter_pi_star | 177 | 14.4734 | 0.9941 | 0.5593 | -0.0347 | -0.0001 | 0.1525 | ok | RAN |
| SOLUSDT | 4 | `wma523_above_at_h` | one_head_filter_pi_star | 194 | 15.8188 | 0.9716 | 0.5309 | -0.1730 | -0.0005 | 0.1031 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `wma523_above_at_h` | one_head_filter_pi_star | 198 | 16.2753 | 0.8001 | 0.5253 | -1.3069 | -0.0083 | 0.0960 | ok | RAN |
| ETHUSDT | 8 | `wma523_above_at_h` | one_head_filter_pi_star | 191 | 15.7000 | 0.7932 | 0.5288 | -1.3660 | -0.0087 | 0.0942 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma523_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma523_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma523_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma523_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma523_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma523_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma523_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma523_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma523_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma523_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma523_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma523_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma523_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma523_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma523_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma523_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
