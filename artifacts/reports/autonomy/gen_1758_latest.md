# Autonomy public-indicator hunt gen 1758

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T103120Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma452_below_at_h` | one_head_filter_pi_star | 187 | 15.2762 | 1.1963 | 0.5989 | 1.1311 | 0.0058 | 0.1925 | ok | RAN |
| ETHUSDT | 4 | `wma452_below_at_h` | one_head_filter_pi_star | 182 | 14.8677 | 1.0540 | 0.5769 | 0.3363 | 0.0018 | 0.1978 | ok | RAN |
| SOLUSDT | 8 | `wma452_above_at_h` | one_head_filter_pi_star | 188 | 15.3296 | 1.0710 | 0.5532 | 0.4050 | 0.0013 | 0.1011 | ok | RAN |
| SOLUSDT | 4 | `wma452_below_at_h` | one_head_filter_pi_star | 174 | 14.2281 | 1.0572 | 0.5690 | 0.3119 | 0.0012 | 0.1552 | ok | RAN |
| SOLUSDT | 8 | `wma452_below_at_h` | one_head_filter_pi_star | 170 | 13.9010 | 1.0392 | 0.5588 | 0.2198 | 0.0008 | 0.1529 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `wma452_above_at_h` | one_head_filter_pi_star | 194 | 15.8188 | 0.9953 | 0.5309 | -0.0285 | -0.0001 | 0.1082 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `wma452_above_at_h` | one_head_filter_pi_star | 189 | 15.5356 | 0.8285 | 0.5344 | -1.0850 | -0.0070 | 0.0952 | ok | RAN |
| ETHUSDT | 8 | `wma452_above_at_h` | one_head_filter_pi_star | 186 | 15.2890 | 0.7864 | 0.5323 | -1.3571 | -0.0090 | 0.0914 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma452_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma452_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4116 | 0.2778 | -1.4041 | -0.0721 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma452_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma452_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma452_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma452_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma452_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma452_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma452_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma452_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma452_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma452_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma452_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma452_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma452_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma452_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
