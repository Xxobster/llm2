# Autonomy public-indicator hunt gen 2390

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T123741Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma551_below_at_h` | one_head_filter_pi_star | 182 | 14.8677 | 1.1643 | 0.5934 | 0.9439 | 0.0049 | 0.1868 | ok | RAN |
| ETHUSDT | 8 | `wma551_below_at_h` | one_head_filter_pi_star | 185 | 15.1128 | 1.1431 | 0.5892 | 0.8604 | 0.0044 | 0.1892 | ok | RAN |
| SOLUSDT | 4 | `wma551_below_at_h` | one_head_filter_pi_star | 184 | 15.0458 | 1.0616 | 0.5761 | 0.3567 | 0.0012 | 0.1467 | ok | RAN |
| SOLUSDT | 8 | `wma551_above_at_h` | one_head_filter_pi_star | 187 | 15.2481 | 1.0466 | 0.5455 | 0.2644 | 0.0008 | 0.0963 | ok | RAN |
| SOLUSDT | 4 | `wma551_above_at_h` | one_head_filter_pi_star | 185 | 15.0850 | 1.0219 | 0.5351 | 0.1278 | 0.0004 | 0.1027 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `wma551_below_at_h` | one_head_filter_pi_star | 192 | 15.7000 | 0.9881 | 0.5573 | -0.0734 | -0.0003 | 0.1615 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `wma551_above_at_h` | one_head_filter_pi_star | 178 | 14.6888 | 0.8501 | 0.5393 | -0.9147 | -0.0060 | 0.0899 | ok | RAN |
| ETHUSDT | 4 | `wma551_above_at_h` | one_head_filter_pi_star | 185 | 15.2665 | 0.8257 | 0.5297 | -1.1013 | -0.0072 | 0.0865 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma551_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0682 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma551_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma551_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma551_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma551_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma551_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma551_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma551_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma551_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma551_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma551_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma551_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma551_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma551_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma551_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma551_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
