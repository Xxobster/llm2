# Autonomy public-indicator hunt gen 2144

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T035906Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `sma4960_above_at_h` | one_head_filter_pi_star | 62 | 5.2446 | 1.9926 | 0.6290 | 1.9826 | 0.0123 | 0.1129 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma4960_above_at_h` | one_head_filter_pi_star | 50 | 4.1995 | 1.4436 | 0.5800 | 0.9535 | 0.0064 | 0.1200 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma4960_above_at_h` | one_head_filter_pi_star | 38 | 11.2124 | 1.0598 | 0.5526 | 0.2879 | 0.0029 | 0.1579 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `sma4960_below_at_h` | one_head_filter_pi_star | 298 | 24.2429 | 1.0014 | 0.5369 | 0.0103 | 0.0000 | 0.1376 | ok | RAN |
| SOLUSDT | 8 | `sma4960_below_at_h` | one_head_filter_pi_star | 314 | 25.5445 | 0.9861 | 0.5414 | -0.1053 | -0.0003 | 0.1306 | ok | RAN |
| ETHUSDT | 8 | `sma4960_below_at_h` | one_head_filter_pi_star | 341 | 27.7410 | 0.9840 | 0.5572 | -0.1290 | -0.0005 | 0.1320 | ok | RAN |
| ETHUSDT | 4 | `sma4960_below_at_h` | one_head_filter_pi_star | 334 | 27.1716 | 0.9730 | 0.5569 | -0.2189 | -0.0009 | 0.1347 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `sma4960_above_at_h` | one_head_filter_pi_star | 41 | 12.0975 | 0.8737 | 0.5122 | -0.6739 | -0.0072 | 0.1707 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma4960_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma4960_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma4960_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma4960_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma4960_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma4960_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma4960_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma4960_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma4960_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma4960_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma4960_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma4960_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma4960_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma4960_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma4960_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma4960_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
