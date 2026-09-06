# Autonomy public-indicator hunt gen 1794

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T135215Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret1648_pos_at_h` | one_head_filter_pi_star | 13 | 3.9818 | 2.6907 | 0.7692 | 2.7640 | 0.0304 | 0.1538 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ret1648_pos_at_h` | one_head_filter_pi_star | 22 | 1.8882 | 2.6612 | 0.7727 | 1.9173 | 0.0194 | 0.1364 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ret1648_pos_at_h` | one_head_filter_pi_star | 18 | 1.7523 | 2.7541 | 0.7222 | 1.8764 | 0.0171 | 0.1667 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ret1648_neg_at_h` | one_head_filter_pi_star | 333 | 27.0902 | 0.9743 | 0.5405 | -0.2002 | -0.0005 | 0.1261 | ok | RAN |
| SOLUSDT | 4 | `ret1648_neg_at_h` | one_head_filter_pi_star | 345 | 28.0664 | 0.9663 | 0.5391 | -0.2704 | -0.0007 | 0.1304 | ok | RAN |
| ETHUSDT | 8 | `ret1648_neg_at_h` | one_head_filter_pi_star | 353 | 28.7172 | 0.9578 | 0.5581 | -0.3594 | -0.0014 | 0.1360 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ret1648_neg_at_h` | one_head_filter_pi_star | 354 | 28.7986 | 0.9352 | 0.5537 | -0.5630 | -0.0022 | 0.1356 | ok | RAN |
| ETHUSDT | 8 | `ret1648_pos_at_h` | one_head_filter_pi_star | 24 | 7.2424 | 0.8967 | 0.5000 | -0.4300 | -0.0053 | 0.1667 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret1648_pos_at_h` | one_head_filter_pi_star | 11 | 2.0201 | 0.4800 | 0.2727 | -1.3628 | -0.0561 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1648_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret1648_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1648_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1648_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1648_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1648_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1648_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1648_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1648_pos_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret1648_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret1648_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1648_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1648_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret1648_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1648_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
