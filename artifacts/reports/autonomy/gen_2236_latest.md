# Autonomy public-indicator hunt gen 2236

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T170005Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema1073_above_at_h` | one_head_filter_pi_star | 114 | 9.2956 | 1.2330 | 0.5877 | 0.9334 | 0.0038 | 0.1228 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema1073_above_at_h` | one_head_filter_pi_star | 115 | 9.4306 | 1.2021 | 0.5913 | 0.8453 | 0.0035 | 0.1391 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema1073_above_at_h` | one_head_filter_pi_star | 137 | 11.2612 | 1.0133 | 0.5766 | 0.0648 | 0.0006 | 0.1168 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 8 | `ema1073_below_at_h` | one_head_filter_pi_star | 232 | 18.9523 | 0.9799 | 0.5517 | -0.1369 | -0.0006 | 0.1552 | ok | RAN |
| SOLUSDT | 8 | `ema1073_below_at_h` | one_head_filter_pi_star | 251 | 20.5245 | 0.9660 | 0.5378 | -0.2317 | -0.0007 | 0.1235 | ok | RAN |
| ETHUSDT | 4 | `ema1073_below_at_h` | one_head_filter_pi_star | 224 | 18.2988 | 0.9655 | 0.5491 | -0.2360 | -0.0011 | 0.1607 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 4 | `ema1073_below_at_h` | one_head_filter_pi_star | 256 | 20.9333 | 0.9086 | 0.5312 | -0.6545 | -0.0020 | 0.1289 | ok | RAN |
| ETHUSDT | 8 | `ema1073_above_at_h` | one_head_filter_pi_star | 108 | 8.8775 | 0.8914 | 0.5370 | -0.4992 | -0.0047 | 0.1574 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1073_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1073_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1073_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1073_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1073_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1073_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1073_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1073_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1073_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1073_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1073_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1073_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1073_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1073_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1073_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1073_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
