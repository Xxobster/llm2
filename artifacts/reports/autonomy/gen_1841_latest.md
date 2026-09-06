# Autonomy public-indicator hunt gen 1841

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T180706Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema4160_above_at_h` | one_head_filter_pi_star | 79 | 6.4942 | 1.9231 | 0.6709 | 2.1840 | 0.0121 | 0.1266 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema4160_above_at_h` | one_head_filter_pi_star | 87 | 7.1519 | 1.4760 | 0.6437 | 1.4410 | 0.0073 | 0.1034 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema4160_below_at_h` | one_head_filter_pi_star | 318 | 26.0031 | 1.0131 | 0.5440 | 0.1001 | 0.0003 | 0.1321 | ok | RAN |
| SOLUSDT | 4 | `ema4160_below_at_h` | one_head_filter_pi_star | 290 | 23.7136 | 1.0076 | 0.5379 | 0.0556 | 0.0002 | 0.1379 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `ema4160_below_at_h` | one_head_filter_pi_star | 342 | 27.8224 | 0.9746 | 0.5585 | -0.2038 | -0.0008 | 0.1316 | ok | RAN |
| ETHUSDT | 8 | `ema4160_below_at_h` | one_head_filter_pi_star | 353 | 28.7172 | 0.9645 | 0.5581 | -0.2992 | -0.0012 | 0.1331 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema4160_above_at_h` | one_head_filter_pi_star | 33 | 9.9583 | 0.7905 | 0.4848 | -1.0465 | -0.0104 | 0.1515 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema4160_above_at_h` | one_head_filter_pi_star | 21 | 6.3371 | 0.5682 | 0.3810 | -2.1319 | -0.0221 | 0.1905 | ok | RAN |
| ETHUSDT | 4 | `ema4160_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema4160_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema4160_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema4160_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema4160_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema4160_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema4160_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema4160_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4160_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4160_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema4160_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4160_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4160_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4160_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4160_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4160_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
