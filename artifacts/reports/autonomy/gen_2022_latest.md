# Autonomy public-indicator hunt gen 2022

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T114120Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma493_below_at_h` | one_head_filter_pi_star | 182 | 14.8677 | 1.1564 | 0.5934 | 0.9152 | 0.0048 | 0.1978 | ok | RAN |
| ETHUSDT | 8 | `wma493_below_at_h` | one_head_filter_pi_star | 181 | 14.7860 | 1.1422 | 0.5912 | 0.8197 | 0.0042 | 0.1823 | ok | RAN |
| SOLUSDT | 8 | `wma493_above_at_h` | one_head_filter_pi_star | 188 | 15.3296 | 1.1034 | 0.5585 | 0.5775 | 0.0019 | 0.0957 | ok | RAN |
| SOLUSDT | 4 | `wma493_above_at_h` | one_head_filter_pi_star | 188 | 15.3296 | 1.0324 | 0.5372 | 0.1864 | 0.0006 | 0.1064 | ok | RAN |
| SOLUSDT | 8 | `wma493_below_at_h` | one_head_filter_pi_star | 175 | 14.3099 | 1.0210 | 0.5657 | 0.1219 | 0.0004 | 0.1543 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `wma493_below_at_h` | one_head_filter_pi_star | 185 | 15.1276 | 1.0023 | 0.5568 | 0.0135 | 0.0000 | 0.1514 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `wma493_above_at_h` | one_head_filter_pi_star | 185 | 15.2068 | 0.8003 | 0.5297 | -1.3001 | -0.0084 | 0.0973 | ok | RAN |
| ETHUSDT | 8 | `wma493_above_at_h` | one_head_filter_pi_star | 190 | 15.6178 | 0.7946 | 0.5368 | -1.3271 | -0.0086 | 0.0895 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma493_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma493_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma493_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma493_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma493_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma493_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma493_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma493_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma493_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma493_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma493_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma493_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma493_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma493_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma493_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma493_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
