# Autonomy public-indicator hunt gen 1918

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T010335Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma477_below_at_h` | one_head_filter_pi_star | 186 | 15.1945 | 1.1785 | 0.6022 | 1.0355 | 0.0054 | 0.1935 | ok | RAN |
| ETHUSDT | 4 | `wma477_below_at_h` | one_head_filter_pi_star | 187 | 15.2762 | 1.1220 | 0.5882 | 0.7466 | 0.0038 | 0.1979 | ok | RAN |
| SOLUSDT | 4 | `wma477_below_at_h` | one_head_filter_pi_star | 174 | 14.2281 | 1.0352 | 0.5632 | 0.2037 | 0.0007 | 0.1609 | ok | RAN |
| SOLUSDT | 8 | `wma477_above_at_h` | one_head_filter_pi_star | 187 | 15.2481 | 1.0145 | 0.5455 | 0.0833 | 0.0003 | 0.0963 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `wma477_above_at_h` | one_head_filter_pi_star | 195 | 15.9004 | 0.9925 | 0.5436 | -0.0452 | -0.0001 | 0.1077 | ok | RAN |
| SOLUSDT | 8 | `wma477_below_at_h` | one_head_filter_pi_star | 184 | 15.0458 | 0.9885 | 0.5489 | -0.0692 | -0.0002 | 0.1630 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `wma477_above_at_h` | one_head_filter_pi_star | 177 | 14.5492 | 0.8437 | 0.5424 | -0.9633 | -0.0063 | 0.1017 | ok | RAN |
| ETHUSDT | 4 | `wma477_above_at_h` | one_head_filter_pi_star | 194 | 15.9466 | 0.8183 | 0.5361 | -1.1853 | -0.0074 | 0.0928 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma477_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0682 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma477_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0709 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma477_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma477_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma477_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma477_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma477_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma477_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma477_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma477_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma477_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma477_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma477_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma477_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma477_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma477_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
