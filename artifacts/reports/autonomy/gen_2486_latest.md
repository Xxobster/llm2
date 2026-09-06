# Autonomy public-indicator hunt gen 2486

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T234043Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma566_below_at_h` | one_head_filter_pi_star | 186 | 15.1945 | 1.1497 | 0.5860 | 0.8993 | 0.0046 | 0.1935 | ok | RAN |
| ETHUSDT | 4 | `wma566_below_at_h` | one_head_filter_pi_star | 175 | 14.2959 | 1.1422 | 0.5886 | 0.8219 | 0.0043 | 0.1886 | ok | RAN |
| SOLUSDT | 4 | `wma566_above_at_h` | one_head_filter_pi_star | 192 | 15.6558 | 1.0781 | 0.5469 | 0.4525 | 0.0014 | 0.0990 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `wma566_above_at_h` | one_head_filter_pi_star | 186 | 15.1665 | 1.0004 | 0.5323 | 0.0024 | 0.0000 | 0.0968 | ok | RAN |
| SOLUSDT | 8 | `wma566_below_at_h` | one_head_filter_pi_star | 186 | 15.2094 | 0.9617 | 0.5430 | -0.2353 | -0.0008 | 0.1667 | ok | RAN |
| SOLUSDT | 4 | `wma566_below_at_h` | one_head_filter_pi_star | 196 | 16.0271 | 0.9521 | 0.5510 | -0.2925 | -0.0010 | 0.1429 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `wma566_above_at_h` | one_head_filter_pi_star | 180 | 14.8539 | 0.8549 | 0.5389 | -0.9068 | -0.0059 | 0.0944 | ok | RAN |
| ETHUSDT | 8 | `wma566_above_at_h` | one_head_filter_pi_star | 183 | 15.0424 | 0.8297 | 0.5355 | -1.0880 | -0.0069 | 0.0984 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma566_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0682 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma566_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma566_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma566_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma566_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma566_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma566_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma566_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma566_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma566_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma566_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma566_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma566_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma566_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma566_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma566_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
