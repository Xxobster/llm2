# Autonomy public-indicator hunt gen 1881

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T214227Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema4260_above_at_h` | one_head_filter_pi_star | 70 | 5.7544 | 1.9251 | 0.6857 | 2.1068 | 0.0122 | 0.1143 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema4260_above_at_h` | one_head_filter_pi_star | 49 | 4.5432 | 1.9195 | 0.6531 | 1.6434 | 0.0103 | 0.1224 | ok | RAN |
| ETHUSDT | 4 | `ema4260_above_at_h` | one_head_filter_pi_star | 35 | 10.3272 | 1.0028 | 0.5429 | 0.0127 | 0.0001 | 0.1714 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ema4260_below_at_h` | one_head_filter_pi_star | 281 | 22.9776 | 0.9796 | 0.5338 | -0.1481 | -0.0004 | 0.1281 | ok | RAN |
| ETHUSDT | 8 | `ema4260_below_at_h` | one_head_filter_pi_star | 350 | 28.4732 | 0.9812 | 0.5600 | -0.1541 | -0.0006 | 0.1371 | ok | RAN |
| SOLUSDT | 4 | `ema4260_below_at_h` | one_head_filter_pi_star | 313 | 25.5943 | 0.9671 | 0.5335 | -0.2513 | -0.0007 | 0.1310 | ok | RAN |
| ETHUSDT | 4 | `ema4260_below_at_h` | one_head_filter_pi_star | 342 | 27.8224 | 0.9582 | 0.5556 | -0.3399 | -0.0014 | 0.1374 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema4260_above_at_h` | one_head_filter_pi_star | 30 | 9.0530 | 0.7763 | 0.4667 | -1.0539 | -0.0121 | 0.1667 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema4260_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema4260_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema4260_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema4260_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema4260_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema4260_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema4260_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema4260_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4260_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4260_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4260_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4260_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4260_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4260_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4260_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4260_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
