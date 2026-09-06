# Autonomy public-indicator hunt gen 1570

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260901T144444Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ret1424_pos_at_h` | one_head_filter_pi_star | 21 | 1.7855 | 1.5320 | 0.6667 | 0.7997 | 0.0105 | 0.1429 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ret1424_pos_at_h` | one_head_filter_pi_star | 19 | 1.6155 | 1.0622 | 0.5789 | 0.1121 | 0.0013 | 0.1579 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ret1424_neg_at_h` | one_head_filter_pi_star | 320 | 26.0326 | 1.0236 | 0.5500 | 0.1784 | 0.0005 | 0.1344 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ret1424_neg_at_h` | one_head_filter_pi_star | 321 | 26.1140 | 1.0006 | 0.5452 | 0.0045 | 0.0000 | 0.1371 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ret1424_neg_at_h` | one_head_filter_pi_star | 326 | 26.5207 | 0.9400 | 0.5491 | -0.4880 | -0.0020 | 0.1380 | ok | RAN |
| ETHUSDT | 4 | `ret1424_neg_at_h` | one_head_filter_pi_star | 312 | 25.3818 | 0.9076 | 0.5449 | -0.7379 | -0.0031 | 0.1410 | ok | RAN |
| ETHUSDT | 4 | `ret1424_pos_at_h` | one_head_filter_pi_star | 35 | 3.3763 | 0.8202 | 0.5429 | -0.5517 | -0.0093 | 0.1143 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret1424_pos_at_h` | one_head_filter_pi_star | 14 | 1.6451 | 0.7081 | 0.5000 | -0.6867 | -0.0134 | 0.0714 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret1424_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6372 | 0.2941 | -0.6851 | -0.0295 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret1424_pos_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.6126 | 0.2500 | -0.7324 | -0.0321 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1424_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret1424_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1424_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1424_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1424_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1424_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1424_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1424_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1424_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret1424_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1424_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1424_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret1424_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1424_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
