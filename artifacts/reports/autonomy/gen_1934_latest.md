# Autonomy public-indicator hunt gen 1934

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T023850Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma479_below_at_h` | one_head_filter_pi_star | 191 | 15.6030 | 1.1562 | 0.5916 | 0.9346 | 0.0047 | 0.1937 | ok | RAN |
| ETHUSDT | 4 | `wma479_below_at_h` | one_head_filter_pi_star | 179 | 14.6227 | 1.1128 | 0.5810 | 0.6703 | 0.0035 | 0.2067 | ok | RAN |
| SOLUSDT | 4 | `wma479_below_at_h` | one_head_filter_pi_star | 182 | 14.8823 | 1.0697 | 0.5769 | 0.4041 | 0.0014 | 0.1538 | ok | RAN |
| SOLUSDT | 8 | `wma479_above_at_h` | one_head_filter_pi_star | 182 | 14.8404 | 1.0547 | 0.5385 | 0.3074 | 0.0010 | 0.0934 | ok | RAN |
| SOLUSDT | 4 | `wma479_above_at_h` | one_head_filter_pi_star | 184 | 15.0034 | 1.0046 | 0.5272 | 0.0270 | 0.0001 | 0.1033 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `wma479_below_at_h` | one_head_filter_pi_star | 180 | 14.7188 | 0.9646 | 0.5500 | -0.2149 | -0.0008 | 0.1667 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `wma479_above_at_h` | one_head_filter_pi_star | 193 | 15.8644 | 0.8043 | 0.5285 | -1.2864 | -0.0080 | 0.0933 | ok | RAN |
| ETHUSDT | 8 | `wma479_above_at_h` | one_head_filter_pi_star | 190 | 15.6178 | 0.7787 | 0.5316 | -1.4418 | -0.0092 | 0.0895 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma479_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5128 | 0.2778 | -1.0553 | -0.0479 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma479_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0682 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma479_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma479_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma479_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma479_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma479_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma479_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma479_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma479_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma479_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma479_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma479_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma479_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma479_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma479_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
