# Autonomy public-indicator hunt gen 1897

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T230823Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema4300_above_at_h` | one_head_filter_pi_star | 38 | 3.5679 | 2.4496 | 0.6842 | 2.0919 | 0.0164 | 0.1053 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ema4300_above_at_h` | one_head_filter_pi_star | 81 | 6.6587 | 1.8915 | 0.6914 | 2.2086 | 0.0111 | 0.0864 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ema4300_below_at_h` | one_head_filter_pi_star | 282 | 23.0594 | 0.9729 | 0.5319 | -0.1976 | -0.0006 | 0.1383 | ok | RAN |
| SOLUSDT | 8 | `ema4300_below_at_h` | one_head_filter_pi_star | 284 | 23.2229 | 0.9679 | 0.5317 | -0.2369 | -0.0007 | 0.1338 | ok | RAN |
| ETHUSDT | 8 | `ema4300_below_at_h` | one_head_filter_pi_star | 349 | 28.3918 | 0.9690 | 0.5587 | -0.2608 | -0.0010 | 0.1347 | ok | RAN |
| ETHUSDT | 4 | `ema4300_below_at_h` | one_head_filter_pi_star | 343 | 27.9037 | 0.9621 | 0.5569 | -0.3079 | -0.0012 | 0.1370 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema4300_above_at_h` | one_head_filter_pi_star | 31 | 9.3547 | 0.8256 | 0.5161 | -0.8410 | -0.0075 | 0.0968 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema4300_above_at_h` | one_head_filter_pi_star | 35 | 10.3272 | 0.6605 | 0.4571 | -1.8389 | -0.0184 | 0.1429 | ok | RAN |
| ETHUSDT | 4 | `ema4300_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema4300_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema4300_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema4300_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema4300_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema4300_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema4300_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema4300_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4300_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4300_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4300_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4300_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4300_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4300_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4300_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4300_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
