# Autonomy public-indicator hunt gen 1626

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260901T203357Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ret1480_pos_at_h` | one_head_filter_pi_star | 21 | 1.8728 | 2.1088 | 0.7143 | 1.5255 | 0.0169 | 0.1905 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret1480_pos_at_h` | one_head_filter_pi_star | 23 | 2.2581 | 1.3869 | 0.6087 | 0.7089 | 0.0162 | 0.1304 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ret1480_pos_at_h` | one_head_filter_pi_star | 17 | 1.5161 | 1.0645 | 0.5882 | 0.1193 | 0.0012 | 0.1765 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ret1480_neg_at_h` | one_head_filter_pi_star | 328 | 26.6834 | 1.0542 | 0.5518 | 0.4053 | 0.0011 | 0.1311 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ret1480_neg_at_h` | one_head_filter_pi_star | 335 | 27.2529 | 1.0027 | 0.5522 | 0.0211 | 0.0001 | 0.1284 | ok | RAN |
| ETHUSDT | 4 | `ret1480_neg_at_h` | one_head_filter_pi_star | 322 | 26.1953 | 0.9585 | 0.5497 | -0.3339 | -0.0013 | 0.1398 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ret1480_neg_at_h` | one_head_filter_pi_star | 315 | 25.6259 | 0.9066 | 0.5429 | -0.7491 | -0.0032 | 0.1429 | ok | RAN |
| ETHUSDT | 4 | `ret1480_pos_at_h` | one_head_filter_pi_star | 33 | 3.3133 | 0.7662 | 0.4848 | -0.7184 | -0.0133 | 0.1212 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret1480_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.3783 | 0.2105 | -1.5197 | -0.0766 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret1480_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.3880 | 0.2222 | -1.4607 | -0.0781 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1480_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret1480_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1480_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1480_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1480_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1480_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1480_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1480_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1480_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1480_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1480_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1480_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1480_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1480_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
