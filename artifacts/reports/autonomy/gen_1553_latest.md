# Autonomy public-indicator hunt gen 1553

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260831T074559Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema3440_below_at_h` | one_head_filter_pi_star | 349 | 28.3918 | 1.6097 | 0.6447 | 3.7122 | 0.0161 | 0.2980 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema3440_below_at_h` | one_head_filter_pi_star | 351 | 28.5545 | 1.6080 | 0.6439 | 3.6960 | 0.0160 | 0.2991 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ema3440_above_at_h` | one_head_filter_pi_star | 74 | 6.0832 | 2.2333 | 0.6892 | 2.6285 | 0.0144 | 0.2432 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema3440_below_at_h` | one_head_filter_pi_star | 303 | 24.7766 | 1.7855 | 0.6436 | 4.2531 | 0.0120 | 0.3267 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema3440_below_at_h` | one_head_filter_pi_star | 296 | 24.0802 | 1.7511 | 0.6351 | 3.9560 | 0.0116 | 0.3345 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema3440_above_at_h` | one_head_filter_pi_star | 96 | 7.8904 | 1.9159 | 0.6667 | 2.5263 | 0.0112 | 0.2188 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema3440_above_at_h` | one_head_filter_pi_star | 33 | 3.8778 | 0.9545 | 0.5152 | -0.1265 | -0.0021 | 0.2424 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema3440_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 4 | `ema3440_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema3440_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema3440_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema3440_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema3440_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema3440_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema3440_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema3440_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema3440_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema3440_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema3440_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema3440_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema3440_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema3440_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema3440_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema3440_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
