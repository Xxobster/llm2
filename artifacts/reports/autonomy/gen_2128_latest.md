# Autonomy public-indicator hunt gen 2128

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T014055Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `sma4920_above_at_h` | one_head_filter_pi_star | 48 | 4.0315 | 2.2815 | 0.6042 | 2.0177 | 0.0154 | 0.0833 | ok | RAN |
| SOLUSDT | 4 | `sma4920_above_at_h` | one_head_filter_pi_star | 44 | 3.6955 | 1.5463 | 0.5455 | 1.0812 | 0.0084 | 0.0909 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `sma4920_below_at_h` | one_head_filter_pi_star | 336 | 27.3343 | 0.9746 | 0.5565 | -0.2045 | -0.0008 | 0.1339 | ok | RAN |
| SOLUSDT | 4 | `sma4920_below_at_h` | one_head_filter_pi_star | 295 | 23.9988 | 0.9587 | 0.5356 | -0.3083 | -0.0009 | 0.1356 | ok | RAN |
| SOLUSDT | 8 | `sma4920_below_at_h` | one_head_filter_pi_star | 301 | 24.4869 | 0.9569 | 0.5316 | -0.3258 | -0.0009 | 0.1362 | ok | RAN |
| ETHUSDT | 8 | `sma4920_below_at_h` | one_head_filter_pi_star | 334 | 27.1716 | 0.9680 | 0.5539 | -0.2552 | -0.0010 | 0.1317 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `sma4920_above_at_h` | one_head_filter_pi_star | 37 | 10.9173 | 0.8022 | 0.4865 | -1.1287 | -0.0105 | 0.1351 | ok | RAN |
| ETHUSDT | 8 | `sma4920_above_at_h` | one_head_filter_pi_star | 44 | 12.9827 | 0.8148 | 0.5000 | -1.1610 | -0.0110 | 0.1591 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma4920_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma4920_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma4920_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma4920_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma4920_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma4920_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma4920_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma4920_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma4920_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma4920_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma4920_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma4920_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma4920_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma4920_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma4920_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma4920_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
