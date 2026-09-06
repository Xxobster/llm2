# Autonomy public-indicator hunt gen 1974

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T061946Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma486_below_at_h` | one_head_filter_pi_star | 190 | 15.5213 | 1.1752 | 0.5895 | 1.0161 | 0.0052 | 0.1842 | ok | RAN |
| ETHUSDT | 4 | `wma486_below_at_h` | one_head_filter_pi_star | 188 | 15.3579 | 1.1251 | 0.5904 | 0.7597 | 0.0039 | 0.1968 | ok | RAN |
| SOLUSDT | 8 | `wma486_above_at_h` | one_head_filter_pi_star | 180 | 14.6773 | 1.1154 | 0.5444 | 0.6218 | 0.0020 | 0.1000 | ok | RAN |
| SOLUSDT | 4 | `wma486_below_at_h` | one_head_filter_pi_star | 175 | 14.3099 | 1.0522 | 0.5657 | 0.2944 | 0.0011 | 0.1543 | ok | RAN |
| SOLUSDT | 4 | `wma486_above_at_h` | one_head_filter_pi_star | 188 | 15.3296 | 1.0308 | 0.5372 | 0.1777 | 0.0006 | 0.0957 | ok | RAN |
| SOLUSDT | 8 | `wma486_below_at_h` | one_head_filter_pi_star | 174 | 14.2281 | 1.0144 | 0.5517 | 0.0840 | 0.0003 | 0.1552 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `wma486_above_at_h` | one_head_filter_pi_star | 176 | 14.5238 | 0.8540 | 0.5341 | -0.8934 | -0.0059 | 0.0966 | ok | RAN |
| ETHUSDT | 4 | `wma486_above_at_h` | one_head_filter_pi_star | 185 | 15.2665 | 0.7873 | 0.5189 | -1.3766 | -0.0089 | 0.0973 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma486_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5128 | 0.2778 | -1.0553 | -0.0479 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma486_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0682 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma486_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma486_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma486_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma486_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma486_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma486_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma486_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma486_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma486_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma486_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma486_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma486_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma486_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma486_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
