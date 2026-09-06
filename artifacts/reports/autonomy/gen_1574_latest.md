# Autonomy public-indicator hunt gen 1574

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260901T151152Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma423_below_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 1.1424 | 0.5873 | 0.8548 | 0.0044 | 0.1958 | ok | RAN |
| ETHUSDT | 4 | `wma423_below_at_h` | one_head_filter_pi_star | 182 | 14.8677 | 1.1377 | 0.5934 | 0.8288 | 0.0043 | 0.1978 | ok | RAN |
| SOLUSDT | 4 | `wma423_below_at_h` | one_head_filter_pi_star | 167 | 13.6557 | 1.0802 | 0.5749 | 0.4300 | 0.0017 | 0.1557 | ok | RAN |
| SOLUSDT | 8 | `wma423_below_at_h` | one_head_filter_pi_star | 166 | 13.5740 | 1.0550 | 0.5663 | 0.3049 | 0.0012 | 0.1627 | ok | RAN |
| SOLUSDT | 4 | `wma423_above_at_h` | one_head_filter_pi_star | 193 | 15.7373 | 1.0193 | 0.5440 | 0.1147 | 0.0004 | 0.1036 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `wma423_above_at_h` | one_head_filter_pi_star | 196 | 15.9819 | 0.9771 | 0.5357 | -0.1390 | -0.0004 | 0.0969 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `wma423_above_at_h` | one_head_filter_pi_star | 183 | 15.0424 | 0.8367 | 0.5355 | -1.0200 | -0.0066 | 0.0984 | ok | RAN |
| ETHUSDT | 4 | `wma423_above_at_h` | one_head_filter_pi_star | 185 | 15.2068 | 0.8227 | 0.5243 | -1.1225 | -0.0071 | 0.0973 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma423_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma423_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0709 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma423_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma423_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma423_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma423_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma423_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma423_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma423_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma423_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma423_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma423_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma423_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma423_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma423_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma423_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
