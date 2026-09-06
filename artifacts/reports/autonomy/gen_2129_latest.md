# Autonomy public-indicator hunt gen 2129

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T014802Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema4880_above_at_h` | one_head_filter_pi_star | 66 | 5.4256 | 1.8327 | 0.6667 | 1.8857 | 0.0113 | 0.1061 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema4880_above_at_h` | one_head_filter_pi_star | 57 | 4.7382 | 1.5543 | 0.6316 | 1.2386 | 0.0088 | 0.0877 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema4880_above_at_h` | one_head_filter_pi_star | 30 | 9.0530 | 1.2013 | 0.5667 | 0.7788 | 0.0080 | 0.1333 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ema4880_below_at_h` | one_head_filter_pi_star | 309 | 25.2672 | 0.9949 | 0.5372 | -0.0379 | -0.0001 | 0.1327 | ok | RAN |
| SOLUSDT | 4 | `ema4880_below_at_h` | one_head_filter_pi_star | 307 | 25.1037 | 0.9690 | 0.5342 | -0.2354 | -0.0007 | 0.1336 | ok | RAN |
| ETHUSDT | 8 | `ema4880_below_at_h` | one_head_filter_pi_star | 346 | 28.1478 | 0.9720 | 0.5578 | -0.2294 | -0.0009 | 0.1358 | ok | RAN |
| ETHUSDT | 4 | `ema4880_below_at_h` | one_head_filter_pi_star | 345 | 28.0664 | 0.9580 | 0.5565 | -0.3436 | -0.0014 | 0.1362 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema4880_above_at_h` | one_head_filter_pi_star | 37 | 10.7995 | 0.9593 | 0.5405 | -0.2220 | -0.0019 | 0.1622 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema4880_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5593 | 0.2941 | -0.9437 | -0.0562 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema4880_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5593 | 0.2941 | -0.9437 | -0.0562 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema4880_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema4880_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema4880_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema4880_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema4880_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema4880_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema4880_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema4880_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4880_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4880_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4880_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4880_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4880_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4880_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
