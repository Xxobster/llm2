# Autonomy public-indicator hunt gen 2313

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T021437Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema5340_above_at_h` | one_head_filter_pi_star | 53 | 4.9140 | 2.1062 | 0.6604 | 2.2270 | 0.0130 | 0.1132 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema5340_above_at_h` | one_head_filter_pi_star | 49 | 4.5432 | 1.8368 | 0.6327 | 1.6442 | 0.0110 | 0.1020 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `ema5340_below_at_h` | one_head_filter_pi_star | 352 | 28.6359 | 0.9873 | 0.5597 | -0.1037 | -0.0004 | 0.1420 | ok | RAN |
| SOLUSDT | 8 | `ema5340_below_at_h` | one_head_filter_pi_star | 330 | 26.8461 | 0.9761 | 0.5364 | -0.1880 | -0.0005 | 0.1303 | ok | RAN |
| SOLUSDT | 4 | `ema5340_below_at_h` | one_head_filter_pi_star | 324 | 26.4938 | 0.9678 | 0.5370 | -0.2508 | -0.0007 | 0.1296 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema5340_below_at_h` | one_head_filter_pi_star | 336 | 27.3343 | 0.9313 | 0.5506 | -0.5610 | -0.0023 | 0.1369 | ok | RAN |
| ETHUSDT | 4 | `ema5340_above_at_h` | one_head_filter_pi_star | 41 | 6.9835 | 0.8481 | 0.5122 | -0.6655 | -0.0073 | 0.1463 | ok | RAN |
| ETHUSDT | 8 | `ema5340_above_at_h` | one_head_filter_pi_star | 43 | 12.5508 | 0.7734 | 0.4884 | -1.3566 | -0.0117 | 0.1628 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema5340_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5593 | 0.2941 | -0.9437 | -0.0538 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema5340_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5261 | 0.2778 | -1.0707 | -0.0567 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema5340_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema5340_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5340_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5340_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5340_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5340_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5340_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5340_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5340_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5340_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5340_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5340_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5340_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5340_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
