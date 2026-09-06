# Autonomy public-indicator hunt gen 1678

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T015141Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma439_below_at_h` | one_head_filter_pi_star | 182 | 14.8677 | 1.1929 | 0.6044 | 1.1170 | 0.0058 | 0.1978 | ok | RAN |
| ETHUSDT | 4 | `wma439_below_at_h` | one_head_filter_pi_star | 182 | 14.8677 | 1.1211 | 0.5934 | 0.7120 | 0.0037 | 0.1868 | ok | RAN |
| SOLUSDT | 8 | `wma439_below_at_h` | one_head_filter_pi_star | 169 | 13.8193 | 1.0697 | 0.5680 | 0.3821 | 0.0014 | 0.1538 | ok | RAN |
| SOLUSDT | 4 | `wma439_below_at_h` | one_head_filter_pi_star | 173 | 14.1464 | 1.0677 | 0.5723 | 0.3765 | 0.0014 | 0.1561 | ok | RAN |
| SOLUSDT | 4 | `wma439_above_at_h` | one_head_filter_pi_star | 183 | 14.9219 | 1.0456 | 0.5355 | 0.2536 | 0.0008 | 0.1093 | ok | RAN |
| SOLUSDT | 8 | `wma439_above_at_h` | one_head_filter_pi_star | 183 | 14.9219 | 1.0301 | 0.5410 | 0.1752 | 0.0005 | 0.0984 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `wma439_above_at_h` | one_head_filter_pi_star | 190 | 15.6178 | 0.8704 | 0.5316 | -0.7948 | -0.0052 | 0.0947 | ok | RAN |
| ETHUSDT | 8 | `wma439_above_at_h` | one_head_filter_pi_star | 187 | 15.3712 | 0.8066 | 0.5348 | -1.2170 | -0.0079 | 0.0909 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma439_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5128 | 0.2778 | -1.0553 | -0.0470 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma439_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma439_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma439_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma439_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma439_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma439_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma439_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma439_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma439_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma439_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma439_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma439_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma439_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma439_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma439_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
