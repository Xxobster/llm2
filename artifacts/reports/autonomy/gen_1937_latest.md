# Autonomy public-indicator hunt gen 1937

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T025544Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema4400_above_at_h` | one_head_filter_pi_star | 43 | 4.0373 | 2.8460 | 0.6977 | 2.4828 | 0.0174 | 0.1395 | ok | RAN |
| SOLUSDT | 8 | `ema4400_above_at_h` | one_head_filter_pi_star | 61 | 5.0145 | 1.8347 | 0.6393 | 1.7861 | 0.0106 | 0.1148 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ema4400_below_at_h` | one_head_filter_pi_star | 319 | 26.0849 | 0.9913 | 0.5392 | -0.0663 | -0.0002 | 0.1411 | ok | RAN |
| SOLUSDT | 8 | `ema4400_below_at_h` | one_head_filter_pi_star | 318 | 26.0031 | 0.9721 | 0.5346 | -0.2173 | -0.0006 | 0.1321 | ok | RAN |
| ETHUSDT | 8 | `ema4400_below_at_h` | one_head_filter_pi_star | 349 | 28.3918 | 0.9624 | 0.5587 | -0.3166 | -0.0013 | 0.1347 | ok | RAN |
| ETHUSDT | 4 | `ema4400_below_at_h` | one_head_filter_pi_star | 343 | 27.9037 | 0.9583 | 0.5569 | -0.3427 | -0.0014 | 0.1370 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema4400_above_at_h` | one_head_filter_pi_star | 33 | 9.9583 | 0.9107 | 0.5152 | -0.4362 | -0.0045 | 0.1515 | ok | RAN |
| ETHUSDT | 4 | `ema4400_above_at_h` | one_head_filter_pi_star | 30 | 8.8519 | 0.8773 | 0.5000 | -0.5613 | -0.0059 | 0.1333 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema4400_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema4400_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema4400_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema4400_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema4400_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema4400_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema4400_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema4400_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4400_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4400_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4400_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4400_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4400_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4400_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4400_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4400_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
