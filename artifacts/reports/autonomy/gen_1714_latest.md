# Autonomy public-indicator hunt gen 1714

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T062224Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ret1568_pos_at_h` | one_head_filter_pi_star | 22 | 2.1015 | 1.3041 | 0.6364 | 0.6604 | 0.0055 | 0.1364 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ret1568_neg_at_h` | one_head_filter_pi_star | 348 | 28.3105 | 0.9871 | 0.5460 | -0.1023 | -0.0003 | 0.1322 | ok | RAN |
| SOLUSDT | 8 | `ret1568_neg_at_h` | one_head_filter_pi_star | 338 | 27.4970 | 0.9701 | 0.5414 | -0.2362 | -0.0006 | 0.1302 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ret1568_neg_at_h` | one_head_filter_pi_star | 332 | 27.0089 | 0.9213 | 0.5452 | -0.6593 | -0.0026 | 0.1386 | ok | RAN |
| ETHUSDT | 4 | `ret1568_neg_at_h` | one_head_filter_pi_star | 337 | 27.4156 | 0.9053 | 0.5460 | -0.8105 | -0.0032 | 0.1395 | ok | RAN |
| SOLUSDT | 4 | `ret1568_pos_at_h` | one_head_filter_pi_star | 14 | 1.3373 | 0.7860 | 0.5714 | -0.3523 | -0.0061 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1568_pos_at_h` | one_head_filter_pi_star | 17 | 5.1300 | 0.6880 | 0.4706 | -1.3105 | -0.0176 | 0.1765 | ok | RAN |
| BTCUSDT | 8 | `ret1568_pos_at_h` | one_head_filter_pi_star | 12 | 1.2604 | 0.6823 | 0.3333 | -0.5869 | -0.0277 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret1568_pos_at_h` | one_head_filter_pi_star | 18 | 2.1152 | 0.5313 | 0.4444 | -1.3142 | -0.0289 | 0.1667 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1568_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret1568_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1568_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1568_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1568_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1568_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1568_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1568_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1568_pos_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret1568_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret1568_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1568_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1568_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1568_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1568_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
