# Autonomy public-indicator hunt gen 1706

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T053314Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ret1560_pos_at_h` | one_head_filter_pi_star | 13 | 1.6380 | 3.6398 | 0.7692 | 2.2511 | 0.0270 | 0.0769 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ret1560_neg_at_h` | one_head_filter_pi_star | 346 | 28.1478 | 0.9675 | 0.5376 | -0.2612 | -0.0006 | 0.1301 | ok | RAN |
| SOLUSDT | 8 | `ret1560_neg_at_h` | one_head_filter_pi_star | 329 | 26.7648 | 0.9442 | 0.5350 | -0.4350 | -0.0011 | 0.1368 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ret1560_neg_at_h` | one_head_filter_pi_star | 329 | 26.7648 | 0.9233 | 0.5441 | -0.6301 | -0.0026 | 0.1398 | ok | RAN |
| ETHUSDT | 4 | `ret1560_neg_at_h` | one_head_filter_pi_star | 333 | 27.0902 | 0.9215 | 0.5435 | -0.6483 | -0.0026 | 0.1381 | ok | RAN |
| ETHUSDT | 4 | `ret1560_pos_at_h` | one_head_filter_pi_star | 29 | 3.4078 | 0.9412 | 0.5172 | -0.1603 | -0.0029 | 0.1724 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret1560_pos_at_h` | one_head_filter_pi_star | 11 | 0.9361 | 0.4897 | 0.2727 | -0.8965 | -0.0495 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret1560_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.3880 | 0.2222 | -1.4607 | -0.0815 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1560_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret1560_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1560_pos_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 8 | `ret1560_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1560_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1560_pos_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `ret1560_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1560_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1560_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1560_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1560_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1560_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1560_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1560_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1560_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1560_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
