# Autonomy public-indicator hunt gen 2309

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T014511Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret373_neg_at_h` | one_head_filter_pi_star | 170 | 13.8874 | 1.2814 | 0.6118 | 1.4630 | 0.0079 | 0.1706 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret373_neg_at_h` | one_head_filter_pi_star | 172 | 14.0508 | 1.1306 | 0.5756 | 0.7521 | 0.0040 | 0.1802 | ok | RAN |
| SOLUSDT | 8 | `ret373_pos_at_h` | one_head_filter_pi_star | 165 | 13.4542 | 1.1247 | 0.5515 | 0.6325 | 0.0024 | 0.1152 | ok | RAN |
| SOLUSDT | 4 | `ret373_neg_at_h` | one_head_filter_pi_star | 188 | 15.3729 | 1.0238 | 0.5745 | 0.1413 | 0.0005 | 0.1596 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ret373_neg_at_h` | one_head_filter_pi_star | 180 | 14.7188 | 0.9652 | 0.5722 | -0.2103 | -0.0007 | 0.1556 | ok | RAN |
| SOLUSDT | 4 | `ret373_pos_at_h` | one_head_filter_pi_star | 156 | 12.7928 | 0.9501 | 0.5192 | -0.2674 | -0.0011 | 0.1090 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ret373_pos_at_h` | one_head_filter_pi_star | 195 | 16.0287 | 0.8404 | 0.5538 | -0.9835 | -0.0064 | 0.0974 | ok | RAN |
| ETHUSDT | 4 | `ret373_pos_at_h` | one_head_filter_pi_star | 188 | 15.4534 | 0.7749 | 0.5319 | -1.3940 | -0.0096 | 0.0904 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret373_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4385 | 0.2222 | -1.2856 | -0.0591 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret373_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4385 | 0.2222 | -1.2856 | -0.0613 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret373_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret373_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret373_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret373_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret373_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret373_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret373_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret373_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret373_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret373_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret373_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret373_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret373_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret373_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
