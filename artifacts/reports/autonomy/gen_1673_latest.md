# Autonomy public-indicator hunt gen 1673

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T011310Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema3740_above_at_h` | one_head_filter_pi_star | 90 | 7.3985 | 1.5211 | 0.6444 | 1.5535 | 0.0073 | 0.1222 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema3740_above_at_h` | one_head_filter_pi_star | 87 | 7.1390 | 1.4311 | 0.6552 | 1.2832 | 0.0060 | 0.1034 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema3740_below_at_h` | one_head_filter_pi_star | 279 | 22.8141 | 1.0243 | 0.5412 | 0.1713 | 0.0005 | 0.1362 | ok | RAN |
| SOLUSDT | 4 | `ema3740_below_at_h` | one_head_filter_pi_star | 290 | 23.7136 | 1.0161 | 0.5448 | 0.1151 | 0.0003 | 0.1276 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `ema3740_below_at_h` | one_head_filter_pi_star | 345 | 28.0664 | 0.9869 | 0.5594 | -0.1069 | -0.0004 | 0.1333 | ok | RAN |
| ETHUSDT | 8 | `ema3740_below_at_h` | one_head_filter_pi_star | 340 | 27.6597 | 0.9627 | 0.5559 | -0.3012 | -0.0012 | 0.1353 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema3740_above_at_h` | one_head_filter_pi_star | 35 | 4.1128 | 0.7217 | 0.4857 | -0.9613 | -0.0146 | 0.1429 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema3740_above_at_h` | one_head_filter_pi_star | 30 | 9.0530 | 0.6777 | 0.4667 | -1.5614 | -0.0169 | 0.1333 | ok | RAN |
| ETHUSDT | 4 | `ema3740_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema3740_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema3740_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema3740_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema3740_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema3740_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema3740_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema3740_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema3740_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema3740_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema3740_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema3740_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema3740_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema3740_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema3740_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema3740_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
