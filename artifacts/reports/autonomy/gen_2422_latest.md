# Autonomy public-indicator hunt gen 2422

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T162236Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma556_below_at_h` | one_head_filter_pi_star | 184 | 15.0311 | 1.1653 | 0.5978 | 0.9798 | 0.0050 | 0.1957 | ok | RAN |
| ETHUSDT | 4 | `wma556_below_at_h` | one_head_filter_pi_star | 186 | 15.1945 | 1.1297 | 0.5860 | 0.7752 | 0.0039 | 0.1882 | ok | RAN |
| SOLUSDT | 8 | `wma556_above_at_h` | one_head_filter_pi_star | 182 | 14.8404 | 1.0622 | 0.5440 | 0.3487 | 0.0012 | 0.0989 | ok | RAN |
| SOLUSDT | 4 | `wma556_above_at_h` | one_head_filter_pi_star | 189 | 15.4111 | 1.0246 | 0.5503 | 0.1447 | 0.0005 | 0.1005 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `wma556_below_at_h` | one_head_filter_pi_star | 190 | 15.5365 | 0.9926 | 0.5526 | -0.0442 | -0.0002 | 0.1474 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 8 | `wma556_below_at_h` | one_head_filter_pi_star | 189 | 15.4547 | 0.9185 | 0.5397 | -0.4997 | -0.0018 | 0.1534 | ok | RAN |
| ETHUSDT | 8 | `wma556_above_at_h` | one_head_filter_pi_star | 185 | 15.2068 | 0.8541 | 0.5297 | -0.8971 | -0.0058 | 0.1027 | ok | RAN |
| ETHUSDT | 4 | `wma556_above_at_h` | one_head_filter_pi_star | 186 | 15.2890 | 0.8400 | 0.5430 | -1.0100 | -0.0065 | 0.0914 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma556_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma556_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma556_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma556_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma556_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma556_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma556_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma556_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma556_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma556_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma556_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma556_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma556_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma556_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma556_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma556_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
