# Autonomy public-indicator hunt gen 2506

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260906T014653Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ret2360_pos_at_h` | one_head_filter_pi_star | 34 | 3.3099 | 1.9850 | 0.6176 | 1.6756 | 0.0143 | 0.0588 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ret2360_pos_at_h` | one_head_filter_pi_star | 32 | 3.1152 | 1.4838 | 0.5625 | 0.9501 | 0.0077 | 0.0625 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ret2360_neg_at_h` | one_head_filter_pi_star | 336 | 27.3343 | 1.0115 | 0.5446 | 0.0907 | 0.0002 | 0.1339 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ret2360_neg_at_h` | one_head_filter_pi_star | 342 | 27.8224 | 0.9716 | 0.5351 | -0.2281 | -0.0006 | 0.1374 | ok | RAN |
| ETHUSDT | 8 | `ret2360_neg_at_h` | one_head_filter_pi_star | 371 | 30.1816 | 0.9636 | 0.5606 | -0.3077 | -0.0012 | 0.1402 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ret2360_neg_at_h` | one_head_filter_pi_star | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret2360_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.6281 | 0.3158 | -0.8186 | -0.0428 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret2360_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.6281 | 0.3158 | -0.8186 | -0.0428 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret2360_pos_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret2360_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret2360_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret2360_pos_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret2360_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret2360_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret2360_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret2360_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret2360_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret2360_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret2360_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret2360_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret2360_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret2360_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret2360_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret2360_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
