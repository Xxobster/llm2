# Autonomy public-indicator hunt gen 2278

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T220231Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma533_below_at_h` | one_head_filter_pi_star | 186 | 15.1945 | 1.1047 | 0.5806 | 0.6381 | 0.0033 | 0.1935 | ok | RAN |
| ETHUSDT | 8 | `wma533_below_at_h` | one_head_filter_pi_star | 196 | 16.0114 | 1.0822 | 0.5765 | 0.5164 | 0.0026 | 0.1786 | ok | RAN |
| SOLUSDT | 8 | `wma533_above_at_h` | one_head_filter_pi_star | 194 | 15.8188 | 1.0806 | 0.5464 | 0.4700 | 0.0015 | 0.0979 | ok | RAN |
| SOLUSDT | 4 | `wma533_above_at_h` | one_head_filter_pi_star | 184 | 15.0034 | 1.0527 | 0.5435 | 0.2998 | 0.0010 | 0.0978 | ok | RAN |
| SOLUSDT | 4 | `wma533_below_at_h` | one_head_filter_pi_star | 181 | 14.8005 | 1.0195 | 0.5635 | 0.1152 | 0.0004 | 0.1492 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `wma533_below_at_h` | one_head_filter_pi_star | 188 | 15.3729 | 0.9887 | 0.5585 | -0.0685 | -0.0002 | 0.1596 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `wma533_above_at_h` | one_head_filter_pi_star | 184 | 15.1246 | 0.8367 | 0.5326 | -1.0313 | -0.0066 | 0.0924 | ok | RAN |
| ETHUSDT | 8 | `wma533_above_at_h` | one_head_filter_pi_star | 179 | 14.7136 | 0.8274 | 0.5363 | -1.0870 | -0.0070 | 0.0950 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma533_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma533_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0709 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma533_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma533_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma533_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma533_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma533_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma533_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma533_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma533_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma533_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma533_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma533_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma533_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma533_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma533_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
