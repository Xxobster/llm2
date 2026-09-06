# Autonomy public-indicator hunt gen 1818

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T160233Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret1672_pos_at_h` | one_head_filter_pi_star | 14 | 4.2247 | 1.3673 | 0.5714 | 1.0574 | 0.0132 | 0.2143 | ok | RAN |
| ETHUSDT | 8 | `ret1672_pos_at_h` | one_head_filter_pi_star | 13 | 4.1142 | 1.4823 | 0.5385 | 1.1494 | 0.0124 | 0.2308 | ok | RAN |
| SOLUSDT | 4 | `ret1672_pos_at_h` | one_head_filter_pi_star | 31 | 2.9106 | 1.8168 | 0.6452 | 1.3515 | 0.0116 | 0.1613 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ret1672_pos_at_h` | one_head_filter_pi_star | 33 | 3.1786 | 1.5923 | 0.6364 | 1.1215 | 0.0103 | 0.1212 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ret1672_neg_at_h` | one_head_filter_pi_star | 333 | 27.0902 | 0.9864 | 0.5435 | -0.1052 | -0.0003 | 0.1231 | ok | RAN |
| SOLUSDT | 4 | `ret1672_neg_at_h` | one_head_filter_pi_star | 304 | 24.7310 | 0.9740 | 0.5395 | -0.1920 | -0.0005 | 0.1283 | ok | RAN |
| ETHUSDT | 4 | `ret1672_neg_at_h` | one_head_filter_pi_star | 347 | 28.2291 | 0.9658 | 0.5562 | -0.2897 | -0.0011 | 0.1354 | ok | RAN |
| ETHUSDT | 8 | `ret1672_neg_at_h` | one_head_filter_pi_star | 359 | 29.2054 | 0.9627 | 0.5571 | -0.3125 | -0.0013 | 0.1337 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret1672_pos_at_h` | one_head_filter_pi_star | 10 | 1.8365 | 0.5174 | 0.3000 | -1.1822 | -0.0549 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1672_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret1672_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1672_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1672_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1672_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1672_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1672_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1672_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1672_pos_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret1672_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret1672_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1672_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1672_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret1672_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1672_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
