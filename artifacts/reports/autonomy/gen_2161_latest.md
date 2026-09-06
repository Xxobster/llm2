# Autonomy public-indicator hunt gen 2161

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T064943Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema4960_above_at_h` | one_head_filter_pi_star | 56 | 4.6035 | 1.9497 | 0.6607 | 1.8722 | 0.0121 | 0.1071 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema4960_above_at_h` | one_head_filter_pi_star | 53 | 4.5534 | 1.5629 | 0.6415 | 1.1781 | 0.0081 | 0.1132 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema4960_above_at_h` | one_head_filter_pi_star | 35 | 10.5618 | 1.1168 | 0.5714 | 0.5250 | 0.0052 | 0.1429 | ok | RAN |
| ETHUSDT | 8 | `ema4960_above_at_h` | one_head_filter_pi_star | 29 | 8.9414 | 1.1162 | 0.5517 | 0.4609 | 0.0050 | 0.1379 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ema4960_below_at_h` | one_head_filter_pi_star | 320 | 26.1667 | 0.9949 | 0.5375 | -0.0389 | -0.0001 | 0.1344 | ok | RAN |
| ETHUSDT | 8 | `ema4960_below_at_h` | one_head_filter_pi_star | 346 | 28.1478 | 0.9872 | 0.5607 | -0.1034 | -0.0004 | 0.1358 | ok | RAN |
| SOLUSDT | 4 | `ema4960_below_at_h` | one_head_filter_pi_star | 312 | 25.5125 | 0.9441 | 0.5288 | -0.4333 | -0.0012 | 0.1314 | ok | RAN |
| ETHUSDT | 4 | `ema4960_below_at_h` | one_head_filter_pi_star | 347 | 28.2291 | 0.9619 | 0.5562 | -0.3179 | -0.0013 | 0.1354 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema4960_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5593 | 0.2941 | -0.9437 | -0.0550 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema4960_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5261 | 0.2778 | -1.0707 | -0.0602 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema4960_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema4960_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema4960_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema4960_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema4960_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema4960_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema4960_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema4960_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4960_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4960_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4960_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4960_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4960_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4960_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
