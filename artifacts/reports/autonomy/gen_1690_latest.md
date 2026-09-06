# Autonomy public-indicator hunt gen 1690

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T034733Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret1544_pos_at_h` | one_head_filter_pi_star | 13 | 1.5276 | 1.6843 | 0.6923 | 0.9701 | 0.0224 | 0.3077 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ret1544_neg_at_h` | one_head_filter_pi_star | 330 | 26.8461 | 1.0383 | 0.5515 | 0.2897 | 0.0007 | 0.1273 | ok | RAN |
| SOLUSDT | 8 | `ret1544_neg_at_h` | one_head_filter_pi_star | 325 | 26.4394 | 1.0116 | 0.5477 | 0.0886 | 0.0002 | 0.1354 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ret1544_neg_at_h` | one_head_filter_pi_star | 340 | 27.6597 | 0.9239 | 0.5471 | -0.6351 | -0.0026 | 0.1353 | ok | RAN |
| ETHUSDT | 4 | `ret1544_neg_at_h` | one_head_filter_pi_star | 343 | 27.9037 | 0.9132 | 0.5481 | -0.7305 | -0.0029 | 0.1370 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret1544_pos_at_h` | one_head_filter_pi_star | 12 | 1.0212 | 0.4886 | 0.2500 | -0.9003 | -0.0436 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret1544_pos_at_h` | one_head_filter_pi_star | 12 | 3.7398 | 0.3757 | 0.3333 | -2.6647 | -0.0563 | 0.3333 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret1544_pos_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.4129 | 0.2500 | -1.3276 | -0.0719 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1544_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret1544_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1544_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1544_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1544_pos_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `ret1544_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1544_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1544_pos_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 8 | `ret1544_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1544_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1544_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret1544_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1544_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1544_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret1544_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1544_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
