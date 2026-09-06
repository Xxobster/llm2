# Autonomy public-indicator hunt gen 2331

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T042319Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma784_below_at_h` | one_head_filter_pi_star | 174 | 14.2142 | 1.2607 | 0.6092 | 1.3483 | 0.0072 | 0.1897 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma784_below_at_h` | one_head_filter_pi_star | 181 | 14.7860 | 1.2231 | 0.5856 | 1.2296 | 0.0064 | 0.1768 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma784_above_at_h` | one_head_filter_pi_star | 126 | 10.3326 | 1.1741 | 0.5714 | 0.7480 | 0.0030 | 0.1190 | ok | RAN |
| SOLUSDT | 8 | `sma784_above_at_h` | one_head_filter_pi_star | 130 | 10.6849 | 1.1188 | 0.5538 | 0.5513 | 0.0022 | 0.1231 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `sma784_below_at_h` | one_head_filter_pi_star | 211 | 17.2537 | 0.9875 | 0.5640 | -0.0777 | -0.0003 | 0.1280 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 8 | `sma784_below_at_h` | one_head_filter_pi_star | 201 | 16.4359 | 0.9135 | 0.5522 | -0.5466 | -0.0019 | 0.1343 | ok | RAN |
| ETHUSDT | 8 | `sma784_above_at_h` | one_head_filter_pi_star | 164 | 13.4806 | 0.8274 | 0.5427 | -0.9800 | -0.0072 | 0.1098 | ok | RAN |
| ETHUSDT | 4 | `sma784_above_at_h` | one_head_filter_pi_star | 146 | 12.0010 | 0.7626 | 0.5274 | -1.3271 | -0.0107 | 0.0959 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma784_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4581 | 0.2222 | -1.1942 | -0.0546 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma784_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0670 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma784_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma784_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma784_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma784_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma784_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma784_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma784_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma784_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma784_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma784_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma784_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma784_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma784_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma784_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
