# Autonomy public-indicator hunt gen 2249

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T183250Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema5180_above_at_h` | one_head_filter_pi_star | 62 | 5.0968 | 2.1174 | 0.6774 | 2.2387 | 0.0137 | 0.0968 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema5180_above_at_h` | one_head_filter_pi_star | 67 | 5.5078 | 1.7811 | 0.6418 | 1.8558 | 0.0106 | 0.1045 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ema5180_below_at_h` | one_head_filter_pi_star | 310 | 25.3490 | 0.9868 | 0.5387 | -0.1003 | -0.0003 | 0.1355 | ok | RAN |
| SOLUSDT | 4 | `ema5180_below_at_h` | one_head_filter_pi_star | 313 | 25.5943 | 0.9627 | 0.5304 | -0.2902 | -0.0008 | 0.1310 | ok | RAN |
| ETHUSDT | 8 | `ema5180_below_at_h` | one_head_filter_pi_star | 341 | 27.7410 | 0.9642 | 0.5572 | -0.2882 | -0.0012 | 0.1349 | ok | RAN |
| ETHUSDT | 4 | `ema5180_below_at_h` | one_head_filter_pi_star | 345 | 28.0664 | 0.9599 | 0.5565 | -0.3304 | -0.0013 | 0.1362 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema5180_above_at_h` | one_head_filter_pi_star | 45 | 13.1346 | 0.8633 | 0.5111 | -0.8740 | -0.0074 | 0.1333 | ok | RAN |
| ETHUSDT | 4 | `ema5180_above_at_h` | one_head_filter_pi_star | 36 | 10.8636 | 0.8074 | 0.5000 | -1.0129 | -0.0093 | 0.0833 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema5180_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5593 | 0.2941 | -0.9437 | -0.0506 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema5180_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5593 | 0.2941 | -0.9437 | -0.0527 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema5180_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema5180_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5180_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5180_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5180_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5180_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5180_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5180_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5180_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5180_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5180_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5180_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5180_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5180_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
