# Autonomy public-indicator hunt gen 1777

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T121732Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema4000_above_at_h` | one_head_filter_pi_star | 90 | 7.3399 | 1.7291 | 0.6556 | 1.9336 | 0.0092 | 0.1111 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema4000_above_at_h` | one_head_filter_pi_star | 65 | 5.3434 | 1.5363 | 0.6462 | 1.3021 | 0.0072 | 0.1231 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema4000_below_at_h` | one_head_filter_pi_star | 296 | 24.2042 | 1.0750 | 0.5541 | 0.5336 | 0.0015 | 0.1351 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 8 | `ema4000_below_at_h` | one_head_filter_pi_star | 341 | 27.7410 | 0.9934 | 0.5601 | -0.0520 | -0.0002 | 0.1349 | ok | RAN |
| SOLUSDT | 8 | `ema4000_below_at_h` | one_head_filter_pi_star | 299 | 24.4495 | 0.9837 | 0.5318 | -0.1211 | -0.0003 | 0.1304 | ok | RAN |
| ETHUSDT | 4 | `ema4000_below_at_h` | one_head_filter_pi_star | 348 | 28.3105 | 0.9719 | 0.5575 | -0.2354 | -0.0009 | 0.1379 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema4000_above_at_h` | one_head_filter_pi_star | 31 | 9.3547 | 0.8695 | 0.5161 | -0.6167 | -0.0060 | 0.1613 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema4000_above_at_h` | one_head_filter_pi_star | 19 | 5.7336 | 0.5114 | 0.3684 | -2.3661 | -0.0284 | 0.1579 | ok | RAN |
| ETHUSDT | 4 | `ema4000_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema4000_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema4000_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema4000_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema4000_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema4000_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema4000_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema4000_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4000_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4000_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4000_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4000_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4000_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4000_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4000_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4000_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
