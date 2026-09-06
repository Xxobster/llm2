# Autonomy public-indicator hunt gen 1602

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260901T181907Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ret1456_pos_at_h` | one_head_filter_pi_star | 23 | 2.0512 | 1.3021 | 0.6522 | 0.5393 | 0.0049 | 0.1739 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ret1456_pos_at_h` | one_head_filter_pi_star | 19 | 1.8715 | 1.0387 | 0.5789 | 0.0818 | 0.0008 | 0.1053 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ret1456_neg_at_h` | one_head_filter_pi_star | 316 | 25.7072 | 1.0209 | 0.5570 | 0.1563 | 0.0004 | 0.1297 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ret1456_neg_at_h` | one_head_filter_pi_star | 337 | 27.4156 | 0.9833 | 0.5460 | -0.1297 | -0.0003 | 0.1395 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ret1456_neg_at_h` | one_head_filter_pi_star | 329 | 26.7648 | 0.9304 | 0.5471 | -0.5621 | -0.0023 | 0.1368 | ok | RAN |
| ETHUSDT | 4 | `ret1456_neg_at_h` | one_head_filter_pi_star | 332 | 27.0089 | 0.9129 | 0.5452 | -0.7183 | -0.0029 | 0.1355 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1456_pos_at_h` | one_head_filter_pi_star | 29 | 2.8472 | 0.6714 | 0.5172 | -0.9250 | -0.0203 | 0.1379 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret1456_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5236 | 0.2632 | -1.0815 | -0.0561 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret1456_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.3880 | 0.2222 | -1.4607 | -0.0750 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1456_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret1456_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1456_pos_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 8 | `ret1456_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1456_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1456_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1456_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1456_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1456_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1456_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1456_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1456_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1456_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1456_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1456_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
