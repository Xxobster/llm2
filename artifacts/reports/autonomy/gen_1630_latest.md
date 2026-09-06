# Autonomy public-indicator hunt gen 1630

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260901T205602Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma432_below_at_h` | one_head_filter_pi_star | 188 | 15.3579 | 1.1613 | 0.5957 | 0.9721 | 0.0049 | 0.1915 | ok | RAN |
| ETHUSDT | 8 | `wma432_below_at_h` | one_head_filter_pi_star | 188 | 15.3579 | 1.1069 | 0.5851 | 0.6503 | 0.0034 | 0.1915 | ok | RAN |
| SOLUSDT | 4 | `wma432_below_at_h` | one_head_filter_pi_star | 179 | 14.6370 | 1.0705 | 0.5698 | 0.3905 | 0.0015 | 0.1508 | ok | RAN |
| SOLUSDT | 8 | `wma432_below_at_h` | one_head_filter_pi_star | 171 | 13.9828 | 1.0704 | 0.5731 | 0.3927 | 0.0015 | 0.1696 | ok | RAN |
| SOLUSDT | 4 | `wma432_above_at_h` | one_head_filter_pi_star | 190 | 15.4927 | 1.0228 | 0.5474 | 0.1319 | 0.0004 | 0.1053 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `wma432_above_at_h` | one_head_filter_pi_star | 185 | 15.0850 | 0.9815 | 0.5459 | -0.1095 | -0.0003 | 0.1027 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `wma432_above_at_h` | one_head_filter_pi_star | 179 | 14.7136 | 0.8426 | 0.5363 | -0.9719 | -0.0063 | 0.1006 | ok | RAN |
| ETHUSDT | 8 | `wma432_above_at_h` | one_head_filter_pi_star | 181 | 14.8780 | 0.8184 | 0.5304 | -1.1329 | -0.0073 | 0.0939 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma432_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5128 | 0.2778 | -1.0553 | -0.0479 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma432_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0682 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma432_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma432_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma432_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma432_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma432_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma432_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma432_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma432_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma432_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma432_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma432_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma432_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma432_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma432_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
