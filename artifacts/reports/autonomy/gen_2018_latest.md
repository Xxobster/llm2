# Autonomy public-indicator hunt gen 2018

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T111720Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret1872_pos_at_h` | one_head_filter_pi_star | 15 | 4.5943 | 2.9120 | 0.7333 | 3.2259 | 0.0344 | 0.2000 | ok | RAN |
| ETHUSDT | 8 | `ret1872_pos_at_h` | one_head_filter_pi_star | 12 | 3.6212 | 2.1540 | 0.6667 | 2.1414 | 0.0277 | 0.1667 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ret1872_pos_at_h` | one_head_filter_pi_star | 44 | 3.6576 | 1.4088 | 0.6364 | 0.9229 | 0.0079 | 0.1818 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ret1872_pos_at_h` | one_head_filter_pi_star | 44 | 3.7038 | 1.3919 | 0.6591 | 0.8750 | 0.0062 | 0.1818 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `ret1872_neg_at_h` | one_head_filter_pi_star | 356 | 28.9613 | 0.9814 | 0.5618 | -0.1553 | -0.0006 | 0.1376 | ok | RAN |
| ETHUSDT | 8 | `ret1872_neg_at_h` | one_head_filter_pi_star | 353 | 28.7172 | 0.9796 | 0.5609 | -0.1713 | -0.0007 | 0.1360 | ok | RAN |
| SOLUSDT | 8 | `ret1872_neg_at_h` | one_head_filter_pi_star | 312 | 25.3818 | 0.9652 | 0.5353 | -0.2661 | -0.0007 | 0.1346 | ok | RAN |
| SOLUSDT | 4 | `ret1872_neg_at_h` | one_head_filter_pi_star | 316 | 25.7072 | 0.9541 | 0.5316 | -0.3555 | -0.0009 | 0.1329 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1872_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret1872_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1872_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1872_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1872_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1872_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1872_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1872_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1872_pos_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1872_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret1872_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1872_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1872_pos_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1872_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret1872_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1872_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
