# Autonomy public-indicator hunt gen 1771

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T114251Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma710_below_at_h` | one_head_filter_pi_star | 168 | 13.7241 | 1.2271 | 0.5833 | 1.2512 | 0.0065 | 0.1905 | GATE_CAND | RAN |
| ETHUSDT | 4 | `sma710_below_at_h` | one_head_filter_pi_star | 168 | 13.7241 | 1.2316 | 0.5952 | 1.2782 | 0.0064 | 0.1964 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma710_above_at_h` | one_head_filter_pi_star | 131 | 10.7426 | 1.0936 | 0.5496 | 0.4324 | 0.0018 | 0.1298 | ok | RAN |
| SOLUSDT | 8 | `sma710_above_at_h` | one_head_filter_pi_star | 126 | 10.3326 | 1.0423 | 0.5397 | 0.1982 | 0.0008 | 0.1270 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `sma710_below_at_h` | one_head_filter_pi_star | 211 | 17.1653 | 0.9523 | 0.5545 | -0.3003 | -0.0010 | 0.1374 | ok | RAN |
| SOLUSDT | 8 | `sma710_below_at_h` | one_head_filter_pi_star | 210 | 17.0839 | 0.9447 | 0.5524 | -0.3496 | -0.0012 | 0.1333 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `sma710_above_at_h` | one_head_filter_pi_star | 144 | 11.8366 | 0.8745 | 0.5694 | -0.6569 | -0.0052 | 0.1111 | ok | RAN |
| ETHUSDT | 4 | `sma710_above_at_h` | one_head_filter_pi_star | 154 | 12.6586 | 0.8405 | 0.5455 | -0.8956 | -0.0066 | 0.1169 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma710_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4641 | 0.2632 | -1.1807 | -0.0550 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma710_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.4092 | 0.2500 | -1.4181 | -0.0663 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma710_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma710_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma710_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma710_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma710_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma710_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma710_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma710_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma710_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma710_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma710_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma710_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma710_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma710_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
