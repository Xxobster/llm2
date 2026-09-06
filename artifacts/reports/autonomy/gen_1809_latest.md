# Autonomy public-indicator hunt gen 1809

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T151345Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema4080_above_at_h` | one_head_filter_pi_star | 87 | 7.1356 | 1.7263 | 0.6552 | 1.9195 | 0.0095 | 0.1034 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema4080_above_at_h` | one_head_filter_pi_star | 89 | 7.3163 | 1.7064 | 0.6517 | 1.8791 | 0.0092 | 0.1124 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema4080_below_at_h` | one_head_filter_pi_star | 279 | 22.8141 | 1.0289 | 0.5412 | 0.2011 | 0.0006 | 0.1398 | ok | RAN |
| SOLUSDT | 4 | `ema4080_below_at_h` | one_head_filter_pi_star | 291 | 23.7953 | 1.0080 | 0.5361 | 0.0583 | 0.0002 | 0.1409 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `ema4080_below_at_h` | one_head_filter_pi_star | 343 | 27.9037 | 0.9915 | 0.5598 | -0.0681 | -0.0003 | 0.1341 | ok | RAN |
| ETHUSDT | 8 | `ema4080_below_at_h` | one_head_filter_pi_star | 352 | 28.6359 | 0.9789 | 0.5597 | -0.1772 | -0.0007 | 0.1335 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema4080_above_at_h` | one_head_filter_pi_star | 37 | 4.3479 | 0.8260 | 0.5135 | -0.6243 | -0.0085 | 0.1351 | ok | RAN |
| ETHUSDT | 8 | `ema4080_above_at_h` | one_head_filter_pi_star | 35 | 4.1128 | 0.7975 | 0.5143 | -0.6390 | -0.0100 | 0.1429 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema4080_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema4080_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema4080_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema4080_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema4080_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema4080_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema4080_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema4080_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4080_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4080_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4080_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4080_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4080_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4080_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4080_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4080_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
