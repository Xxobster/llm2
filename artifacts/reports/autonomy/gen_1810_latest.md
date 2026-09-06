# Autonomy public-indicator hunt gen 1810

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T151920Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret1664_pos_at_h` | one_head_filter_pi_star | 14 | 4.2881 | 2.2181 | 0.6429 | 2.5346 | 0.0320 | 0.2143 | ok | RAN |
| SOLUSDT | 4 | `ret1664_pos_at_h` | one_head_filter_pi_star | 25 | 2.4080 | 2.2246 | 0.6800 | 1.7384 | 0.0143 | 0.0800 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ret1664_pos_at_h` | one_head_filter_pi_star | 23 | 2.2154 | 1.3246 | 0.6087 | 0.6245 | 0.0054 | 0.0870 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `ret1664_neg_at_h` | one_head_filter_pi_star | 351 | 28.5545 | 0.9883 | 0.5613 | -0.0971 | -0.0004 | 0.1368 | ok | RAN |
| SOLUSDT | 8 | `ret1664_neg_at_h` | one_head_filter_pi_star | 330 | 26.8461 | 0.9603 | 0.5394 | -0.3129 | -0.0008 | 0.1242 | ok | RAN |
| SOLUSDT | 4 | `ret1664_neg_at_h` | one_head_filter_pi_star | 325 | 26.4394 | 0.9516 | 0.5354 | -0.3768 | -0.0010 | 0.1231 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ret1664_neg_at_h` | one_head_filter_pi_star | 354 | 28.7986 | 0.9226 | 0.5537 | -0.6741 | -0.0027 | 0.1356 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret1664_pos_at_h` | one_head_filter_pi_star | 19 | 5.7336 | 0.6426 | 0.4211 | -1.5929 | -0.0190 | 0.2105 | ok | RAN |
| BTCUSDT | 4 | `ret1664_pos_at_h` | one_head_filter_pi_star | 10 | 1.8365 | 0.4839 | 0.3000 | -1.3413 | -0.0588 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1664_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret1664_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1664_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1664_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1664_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1664_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1664_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1664_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1664_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret1664_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1664_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1664_pos_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret1664_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret1664_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1664_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
