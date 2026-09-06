# Autonomy public-indicator hunt gen 1578

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260901T153821Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ret1432_pos_at_h` | one_head_filter_pi_star | 27 | 2.2957 | 1.2444 | 0.5926 | 0.4982 | 0.0049 | 0.1852 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ret1432_pos_at_h` | one_head_filter_pi_star | 27 | 2.2957 | 1.2274 | 0.6296 | 0.4133 | 0.0037 | 0.1481 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ret1432_neg_at_h` | one_head_filter_pi_star | 326 | 26.5207 | 1.0435 | 0.5521 | 0.3259 | 0.0008 | 0.1319 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ret1432_neg_at_h` | one_head_filter_pi_star | 331 | 26.9275 | 1.0019 | 0.5498 | 0.0149 | 0.0000 | 0.1360 | ok | RAN |
| ETHUSDT | 4 | `ret1432_neg_at_h` | one_head_filter_pi_star | 323 | 26.2767 | 0.9605 | 0.5511 | -0.3134 | -0.0013 | 0.1424 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ret1432_neg_at_h` | one_head_filter_pi_star | 329 | 26.7648 | 0.9400 | 0.5502 | -0.4963 | -0.0020 | 0.1398 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1432_pos_at_h` | one_head_filter_pi_star | 22 | 2.1599 | 0.6827 | 0.4545 | -0.8129 | -0.0191 | 0.0909 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret1432_pos_at_h` | one_head_filter_pi_star | 12 | 1.4101 | 0.4698 | 0.4167 | -1.3918 | -0.0299 | 0.1667 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret1432_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5959 | 0.2778 | -0.8373 | -0.0411 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret1432_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4904 | 0.2778 | -1.0918 | -0.0528 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1432_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret1432_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1432_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1432_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1432_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1432_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1432_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1432_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1432_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret1432_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1432_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1432_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret1432_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1432_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
