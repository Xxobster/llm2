# Autonomy public-indicator hunt gen 1834

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T173045Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 8 | `ret1688_neg_at_h` | one_head_filter_pi_star | 11 | 1.5401 | 3.0362 | 0.6364 | 1.7838 | 0.1085 | 0.0909 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ret1688_pos_at_h` | one_head_filter_pi_star | 27 | 2.2444 | 3.0457 | 0.7407 | 2.1239 | 0.0210 | 0.1481 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ret1688_pos_at_h` | one_head_filter_pi_star | 27 | 2.2444 | 2.6436 | 0.7407 | 1.8953 | 0.0185 | 0.1852 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 8 | `ret1688_pos_at_h` | one_head_filter_pi_star | 19 | 5.7336 | 1.0013 | 0.4737 | 0.0050 | 0.0001 | 0.2105 | ok | RAN |
| SOLUSDT | 8 | `ret1688_neg_at_h` | one_head_filter_pi_star | 296 | 24.0802 | 0.9888 | 0.5405 | -0.0817 | -0.0002 | 0.1318 | ok | RAN |
| SOLUSDT | 4 | `ret1688_neg_at_h` | one_head_filter_pi_star | 306 | 24.8937 | 0.9828 | 0.5392 | -0.1269 | -0.0003 | 0.1275 | ok | RAN |
| ETHUSDT | 4 | `ret1688_pos_at_h` | one_head_filter_pi_star | 23 | 6.9406 | 0.9802 | 0.5217 | -0.0825 | -0.0009 | 0.1739 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ret1688_neg_at_h` | one_head_filter_pi_star | 359 | 29.2054 | 0.9360 | 0.5543 | -0.5467 | -0.0022 | 0.1365 | ok | RAN |
| ETHUSDT | 8 | `ret1688_neg_at_h` | one_head_filter_pi_star | 351 | 28.5545 | 0.9342 | 0.5499 | -0.5625 | -0.0022 | 0.1368 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1688_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret1688_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1688_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1688_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1688_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1688_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1688_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1688_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1688_pos_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret1688_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret1688_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1688_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1688_pos_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret1688_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1688_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
