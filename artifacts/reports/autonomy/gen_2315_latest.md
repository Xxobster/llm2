# Autonomy public-indicator hunt gen 2315

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T022910Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma782_below_at_h` | one_head_filter_pi_star | 177 | 14.4593 | 1.2146 | 0.5876 | 1.1964 | 0.0060 | 0.1638 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma782_above_at_h` | one_head_filter_pi_star | 119 | 9.7586 | 1.2430 | 0.5882 | 0.9983 | 0.0043 | 0.1345 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma782_below_at_h` | one_head_filter_pi_star | 196 | 16.0114 | 1.1461 | 0.5816 | 0.8624 | 0.0043 | 0.1684 | ok | RAN |
| SOLUSDT | 4 | `sma782_above_at_h` | one_head_filter_pi_star | 148 | 12.1367 | 1.0820 | 0.5541 | 0.4113 | 0.0015 | 0.1216 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `sma782_below_at_h` | one_head_filter_pi_star | 200 | 16.3542 | 0.9623 | 0.5600 | -0.2319 | -0.0008 | 0.1400 | ok | RAN |
| SOLUSDT | 4 | `sma782_below_at_h` | one_head_filter_pi_star | 200 | 16.3542 | 0.9414 | 0.5450 | -0.3614 | -0.0012 | 0.1300 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `sma782_above_at_h` | one_head_filter_pi_star | 169 | 13.8916 | 0.8981 | 0.5621 | -0.5566 | -0.0042 | 0.1065 | ok | RAN |
| ETHUSDT | 4 | `sma782_above_at_h` | one_head_filter_pi_star | 137 | 11.2612 | 0.8904 | 0.5620 | -0.5503 | -0.0046 | 0.1168 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma782_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0545 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma782_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0545 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma782_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma782_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma782_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma782_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma782_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma782_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma782_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma782_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma782_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma782_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma782_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma782_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma782_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma782_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
