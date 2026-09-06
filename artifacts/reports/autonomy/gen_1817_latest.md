# Autonomy public-indicator hunt gen 1817

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T155708Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema4100_above_at_h` | one_head_filter_pi_star | 67 | 5.5078 | 1.9624 | 0.6866 | 2.0211 | 0.0110 | 0.1045 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema4100_above_at_h` | one_head_filter_pi_star | 90 | 7.3399 | 1.4343 | 0.6111 | 1.2854 | 0.0059 | 0.1000 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema4100_below_at_h` | one_head_filter_pi_star | 341 | 27.7410 | 1.0075 | 0.5630 | 0.0587 | 0.0002 | 0.1349 | ok | RAN |
| SOLUSDT | 4 | `ema4100_below_at_h` | one_head_filter_pi_star | 312 | 25.5125 | 1.0056 | 0.5449 | 0.0419 | 0.0001 | 0.1410 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `ema4100_below_at_h` | one_head_filter_pi_star | 346 | 28.1478 | 0.9714 | 0.5578 | -0.2372 | -0.0009 | 0.1358 | ok | RAN |
| SOLUSDT | 8 | `ema4100_below_at_h` | one_head_filter_pi_star | 312 | 25.3818 | 0.9332 | 0.5224 | -0.5183 | -0.0014 | 0.1346 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema4100_above_at_h` | one_head_filter_pi_star | 37 | 11.1653 | 0.8738 | 0.5135 | -0.7068 | -0.0063 | 0.1622 | ok | RAN |
| ETHUSDT | 8 | `ema4100_above_at_h` | one_head_filter_pi_star | 34 | 10.2600 | 0.7923 | 0.5000 | -1.0308 | -0.0100 | 0.1176 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema4100_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema4100_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema4100_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema4100_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema4100_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema4100_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema4100_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema4100_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4100_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4100_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema4100_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4100_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4100_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4100_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4100_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4100_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
