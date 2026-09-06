# Autonomy public-indicator hunt gen 1906

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T235734Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ret1760_pos_at_h` | one_head_filter_pi_star | 13 | 1.1158 | 5.0918 | 0.8462 | 2.2597 | 0.0366 | 0.1538 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret1760_pos_at_h` | one_head_filter_pi_star | 14 | 4.2247 | 2.2585 | 0.7143 | 2.5195 | 0.0356 | 0.2143 | ok | RAN |
| SOLUSDT | 8 | `ret1760_pos_at_h` | one_head_filter_pi_star | 19 | 1.6307 | 4.6166 | 0.8421 | 2.2957 | 0.0320 | 0.1053 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `ret1760_neg_at_h` | one_head_filter_pi_star | 353 | 28.7172 | 0.9953 | 0.5637 | -0.0391 | -0.0002 | 0.1360 | ok | RAN |
| SOLUSDT | 4 | `ret1760_neg_at_h` | one_head_filter_pi_star | 348 | 28.3105 | 0.9737 | 0.5431 | -0.2104 | -0.0005 | 0.1264 | ok | RAN |
| SOLUSDT | 8 | `ret1760_neg_at_h` | one_head_filter_pi_star | 326 | 26.5207 | 0.9479 | 0.5337 | -0.4100 | -0.0010 | 0.1319 | ok | RAN |
| ETHUSDT | 8 | `ret1760_neg_at_h` | one_head_filter_pi_star | 360 | 29.2867 | 0.9662 | 0.5583 | -0.2822 | -0.0011 | 0.1361 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ret1760_pos_at_h` | one_head_filter_pi_star | 21 | 6.3371 | 0.8685 | 0.4762 | -0.5676 | -0.0082 | 0.1905 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret1760_pos_at_h` | one_head_filter_pi_star | 10 | 1.0504 | 0.6080 | 0.4000 | -0.7254 | -0.0568 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret1760_pos_at_h` | one_head_filter_pi_star | 10 | 1.0504 | 0.2732 | 0.3000 | -1.7084 | -0.1025 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1760_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret1760_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1760_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1760_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1760_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1760_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1760_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1760_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1760_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret1760_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1760_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1760_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret1760_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1760_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
