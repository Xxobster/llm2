# Autonomy public-indicator hunt gen 2402

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T140421Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ret2256_pos_at_h` | one_head_filter_pi_star | 27 | 2.3629 | 2.4352 | 0.6296 | 1.8885 | 0.0170 | 0.1481 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ret2256_pos_at_h` | one_head_filter_pi_star | 26 | 2.3534 | 1.1131 | 0.5385 | 0.2396 | 0.0022 | 0.1538 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret2256_neg_at_h` | one_head_filter_pi_star | 352 | 28.6359 | 1.0311 | 0.5682 | 0.2473 | 0.0010 | 0.1335 | ok | RAN |
| SOLUSDT | 8 | `ret2256_neg_at_h` | one_head_filter_pi_star | 345 | 28.0664 | 1.0204 | 0.5507 | 0.1603 | 0.0004 | 0.1333 | ok | RAN |
| SOLUSDT | 4 | `ret2256_neg_at_h` | one_head_filter_pi_star | 343 | 28.0474 | 1.0070 | 0.5510 | 0.0556 | 0.0001 | 0.1341 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 8 | `ret2256_neg_at_h` | one_head_filter_pi_star | 345 | 28.0664 | 0.9985 | 0.5565 | -0.0120 | -0.0000 | 0.1362 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret2256_pos_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.5855 | 0.3125 | -0.8513 | -0.0454 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret2256_pos_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.5855 | 0.3125 | -0.8513 | -0.0463 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret2256_pos_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret2256_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret2256_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret2256_pos_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret2256_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret2256_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret2256_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret2256_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret2256_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret2256_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret2256_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret2256_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret2256_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret2256_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret2256_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret2256_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
