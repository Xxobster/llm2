# Autonomy public-indicator hunt gen 1650

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260901T230907Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ret1504_pos_at_h` | one_head_filter_pi_star | 16 | 1.8243 | 2.2785 | 0.7500 | 1.5485 | 0.0170 | 0.1875 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ret1504_pos_at_h` | one_head_filter_pi_star | 13 | 1.4497 | 2.2496 | 0.6923 | 1.4013 | 0.0164 | 0.0769 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret1504_pos_at_h` | one_head_filter_pi_star | 41 | 4.0253 | 1.1545 | 0.5610 | 0.4069 | 0.0073 | 0.1707 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ret1504_neg_at_h` | one_head_filter_pi_star | 335 | 27.2529 | 1.0032 | 0.5463 | 0.0249 | 0.0001 | 0.1313 | ok | RAN |
| SOLUSDT | 8 | `ret1504_neg_at_h` | one_head_filter_pi_star | 323 | 26.2767 | 0.9828 | 0.5449 | -0.1326 | -0.0003 | 0.1362 | ok | RAN |
| ETHUSDT | 4 | `ret1504_neg_at_h` | one_head_filter_pi_star | 329 | 26.7648 | 0.9803 | 0.5562 | -0.1568 | -0.0006 | 0.1429 | ok | RAN |
| ETHUSDT | 8 | `ret1504_neg_at_h` | one_head_filter_pi_star | 339 | 27.5783 | 0.9757 | 0.5575 | -0.1952 | -0.0008 | 0.1386 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ret1504_pos_at_h` | one_head_filter_pi_star | 12 | 3.7398 | 0.6736 | 0.3333 | -1.1181 | -0.0148 | 0.1667 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret1504_pos_at_h` | one_head_filter_pi_star | 14 | 1.1914 | 0.4516 | 0.2143 | -1.0364 | -0.0482 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret1504_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.3899 | 0.2353 | -1.4493 | -0.0846 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1504_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret1504_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1504_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1504_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1504_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1504_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1504_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1504_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1504_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1504_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1504_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1504_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1504_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1504_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
