# Autonomy public-indicator hunt gen 1754

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T100938Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ret1608_pos_at_h` | one_head_filter_pi_star | 16 | 1.3836 | 1.5202 | 0.6875 | 0.7687 | 0.0094 | 0.2500 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ret1608_pos_at_h` | one_head_filter_pi_star | 14 | 1.5962 | 1.5524 | 0.6429 | 0.8382 | 0.0087 | 0.2857 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `ret1608_neg_at_h` | one_head_filter_pi_star | 348 | 28.3105 | 0.9950 | 0.5603 | -0.0410 | -0.0002 | 0.1379 | ok | RAN |
| SOLUSDT | 4 | `ret1608_neg_at_h` | one_head_filter_pi_star | 337 | 27.4156 | 0.9744 | 0.5430 | -0.2007 | -0.0005 | 0.1276 | ok | RAN |
| SOLUSDT | 8 | `ret1608_neg_at_h` | one_head_filter_pi_star | 343 | 27.9037 | 0.9634 | 0.5394 | -0.2933 | -0.0007 | 0.1283 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ret1608_neg_at_h` | one_head_filter_pi_star | 349 | 28.3918 | 0.9373 | 0.5530 | -0.5330 | -0.0021 | 0.1375 | ok | RAN |
| ETHUSDT | 4 | `ret1608_pos_at_h` | one_head_filter_pi_star | 26 | 3.0553 | 0.9419 | 0.5385 | -0.1567 | -0.0030 | 0.1923 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret1608_pos_at_h` | one_head_filter_pi_star | 10 | 1.8365 | 0.5174 | 0.3000 | -1.1822 | -0.0498 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret1608_pos_at_h` | one_head_filter_pi_star | 10 | 1.0504 | 0.3734 | 0.3000 | -1.3143 | -0.0739 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1608_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret1608_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1608_pos_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 8 | `ret1608_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1608_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1608_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1608_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1608_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1608_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1608_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret1608_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1608_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1608_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret1608_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1608_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
