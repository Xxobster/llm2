# Autonomy public-indicator hunt gen 2090

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T204642Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret1944_pos_at_h` | one_head_filter_pi_star | 14 | 4.2881 | 2.1813 | 0.7143 | 2.2109 | 0.0352 | 0.1429 | ok | RAN |
| SOLUSDT | 8 | `ret1944_pos_at_h` | one_head_filter_pi_star | 34 | 3.1923 | 1.3665 | 0.5882 | 0.7289 | 0.0067 | 0.1765 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ret1944_pos_at_h` | one_head_filter_pi_star | 33 | 3.1428 | 1.1127 | 0.5758 | 0.2776 | 0.0021 | 0.2121 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ret1944_neg_at_h` | one_head_filter_pi_star | 323 | 26.2767 | 1.0176 | 0.5480 | 0.1342 | 0.0003 | 0.1300 | ok | RAN |
| SOLUSDT | 8 | `ret1944_neg_at_h` | one_head_filter_pi_star | 337 | 27.4156 | 1.0063 | 0.5490 | 0.0497 | 0.0001 | 0.1306 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `ret1944_neg_at_h` | one_head_filter_pi_star | 345 | 28.0664 | 0.9924 | 0.5652 | -0.0620 | -0.0002 | 0.1362 | ok | RAN |
| ETHUSDT | 8 | `ret1944_neg_at_h` | one_head_filter_pi_star | 357 | 29.0427 | 0.9768 | 0.5602 | -0.1939 | -0.0008 | 0.1345 | ok | RAN |
| ETHUSDT | 8 | `ret1944_pos_at_h` | one_head_filter_pi_star | 16 | 4.8283 | 0.9795 | 0.5625 | -0.0723 | -0.0011 | 0.1250 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1944_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret1944_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1944_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1944_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1944_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1944_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1944_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1944_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1944_pos_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1944_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret1944_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1944_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1944_pos_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1944_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret1944_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1944_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
