# Autonomy public-indicator hunt gen 2120

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T004352Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `sma4900_above_at_h` | one_head_filter_pi_star | 46 | 4.2541 | 1.8986 | 0.5870 | 1.6477 | 0.0118 | 0.1087 | ok | RAN |
| SOLUSDT | 4 | `sma4900_above_at_h` | one_head_filter_pi_star | 52 | 4.3675 | 1.5444 | 0.5769 | 1.1553 | 0.0082 | 0.0962 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma4900_below_at_h` | one_head_filter_pi_star | 304 | 24.7310 | 1.0059 | 0.5461 | 0.0441 | 0.0001 | 0.1283 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `sma4900_below_at_h` | one_head_filter_pi_star | 334 | 27.1716 | 0.9838 | 0.5569 | -0.1309 | -0.0005 | 0.1287 | ok | RAN |
| ETHUSDT | 8 | `sma4900_below_at_h` | one_head_filter_pi_star | 340 | 27.6597 | 0.9800 | 0.5559 | -0.1615 | -0.0007 | 0.1382 | ok | RAN |
| SOLUSDT | 8 | `sma4900_below_at_h` | one_head_filter_pi_star | 305 | 24.8124 | 0.9619 | 0.5377 | -0.2880 | -0.0008 | 0.1311 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `sma4900_above_at_h` | one_head_filter_pi_star | 35 | 10.3272 | 0.8352 | 0.5143 | -0.8391 | -0.0081 | 0.1143 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 8 | `sma4900_above_at_h` | one_head_filter_pi_star | 40 | 11.8025 | 0.7081 | 0.4750 | -1.6820 | -0.0171 | 0.1750 | ok | RAN |
| ETHUSDT | 4 | `sma4900_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma4900_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma4900_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma4900_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma4900_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma4900_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma4900_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma4900_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma4900_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma4900_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma4900_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma4900_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma4900_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma4900_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma4900_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma4900_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
