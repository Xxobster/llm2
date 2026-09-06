# Autonomy public-indicator hunt gen 2019

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T112250Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma743_below_at_h` | one_head_filter_pi_star | 183 | 14.9494 | 1.2224 | 0.5902 | 1.2679 | 0.0064 | 0.1803 | GATE_CAND | RAN |
| ETHUSDT | 4 | `sma743_below_at_h` | one_head_filter_pi_star | 168 | 13.7241 | 1.1758 | 0.5833 | 0.9886 | 0.0050 | 0.1964 | ok | RAN |
| SOLUSDT | 4 | `sma743_above_at_h` | one_head_filter_pi_star | 130 | 10.6606 | 1.0694 | 0.5462 | 0.3242 | 0.0013 | 0.1231 | ok | RAN |
| SOLUSDT | 8 | `sma743_above_at_h` | one_head_filter_pi_star | 137 | 11.2347 | 1.0605 | 0.5474 | 0.2967 | 0.0012 | 0.1168 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `sma743_below_at_h` | one_head_filter_pi_star | 204 | 16.6813 | 0.9276 | 0.5490 | -0.4573 | -0.0016 | 0.1275 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 8 | `sma743_below_at_h` | one_head_filter_pi_star | 201 | 16.3517 | 0.8761 | 0.5373 | -0.7918 | -0.0027 | 0.1294 | ok | RAN |
| ETHUSDT | 4 | `sma743_above_at_h` | one_head_filter_pi_star | 151 | 12.4120 | 0.8606 | 0.5629 | -0.7533 | -0.0059 | 0.1060 | ok | RAN |
| ETHUSDT | 8 | `sma743_above_at_h` | one_head_filter_pi_star | 162 | 13.3162 | 0.8504 | 0.5494 | -0.8583 | -0.0062 | 0.1049 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma743_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0545 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma743_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0566 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma743_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma743_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma743_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma743_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma743_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma743_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma743_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma743_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma743_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma743_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma743_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma743_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma743_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma743_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
