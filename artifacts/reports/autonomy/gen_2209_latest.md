# Autonomy public-indicator hunt gen 2209

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T134149Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema5080_above_at_h` | one_head_filter_pi_star | 53 | 4.3569 | 1.9081 | 0.6604 | 1.8292 | 0.0129 | 0.1132 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema5080_above_at_h` | one_head_filter_pi_star | 55 | 5.0995 | 1.9314 | 0.6727 | 1.8737 | 0.0125 | 0.1091 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 8 | `ema5080_below_at_h` | one_head_filter_pi_star | 348 | 28.3105 | 0.9981 | 0.5632 | -0.0154 | -0.0001 | 0.1351 | ok | RAN |
| SOLUSDT | 8 | `ema5080_below_at_h` | one_head_filter_pi_star | 318 | 26.0031 | 0.9557 | 0.5314 | -0.3440 | -0.0009 | 0.1321 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 4 | `ema5080_below_at_h` | one_head_filter_pi_star | 320 | 26.1667 | 0.9202 | 0.5250 | -0.6393 | -0.0017 | 0.1313 | ok | RAN |
| ETHUSDT | 4 | `ema5080_below_at_h` | one_head_filter_pi_star | 345 | 28.0664 | 0.9386 | 0.5536 | -0.5190 | -0.0021 | 0.1362 | ok | RAN |
| ETHUSDT | 8 | `ema5080_above_at_h` | one_head_filter_pi_star | 42 | 4.9354 | 0.9158 | 0.5238 | -0.2771 | -0.0040 | 0.1429 | ok | RAN |
| ETHUSDT | 4 | `ema5080_above_at_h` | one_head_filter_pi_star | 38 | 11.4671 | 0.7747 | 0.5000 | -1.2177 | -0.0111 | 0.1316 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema5080_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5593 | 0.2941 | -0.9437 | -0.0527 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema5080_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5593 | 0.2941 | -0.9437 | -0.0550 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema5080_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema5080_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5080_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5080_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5080_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5080_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5080_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5080_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5080_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5080_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5080_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5080_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5080_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5080_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
