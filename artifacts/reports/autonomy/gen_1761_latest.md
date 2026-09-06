# Autonomy public-indicator hunt gen 1761

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T104723Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema3960_above_at_h` | one_head_filter_pi_star | 80 | 6.5765 | 2.1065 | 0.6750 | 2.4722 | 0.0132 | 0.1000 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema3960_above_at_h` | one_head_filter_pi_star | 86 | 7.0697 | 1.6061 | 0.6628 | 1.6855 | 0.0082 | 0.1047 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema3960_below_at_h` | one_head_filter_pi_star | 286 | 23.3865 | 1.0275 | 0.5385 | 0.2003 | 0.0006 | 0.1294 | ok | RAN |
| SOLUSDT | 8 | `ema3960_below_at_h` | one_head_filter_pi_star | 299 | 24.4495 | 1.0104 | 0.5418 | 0.0774 | 0.0002 | 0.1338 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 8 | `ema3960_below_at_h` | one_head_filter_pi_star | 334 | 27.1716 | 0.9534 | 0.5539 | -0.3672 | -0.0015 | 0.1377 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema3960_below_at_h` | one_head_filter_pi_star | 350 | 28.4732 | 0.9474 | 0.5543 | -0.4439 | -0.0018 | 0.1343 | ok | RAN |
| ETHUSDT | 8 | `ema3960_above_at_h` | one_head_filter_pi_star | 23 | 6.9406 | 0.6630 | 0.4348 | -1.4868 | -0.0161 | 0.1304 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema3960_above_at_h` | one_head_filter_pi_star | 37 | 10.9173 | 0.6625 | 0.4595 | -1.8456 | -0.0198 | 0.1351 | ok | RAN |
| ETHUSDT | 4 | `ema3960_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema3960_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema3960_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema3960_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema3960_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema3960_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema3960_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema3960_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema3960_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema3960_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema3960_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema3960_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema3960_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema3960_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema3960_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema3960_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
