# Autonomy public-indicator hunt gen 1657

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260901T234952Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema3700_above_at_h` | one_head_filter_pi_star | 92 | 7.5457 | 1.4903 | 0.6304 | 1.4961 | 0.0069 | 0.0761 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema3700_above_at_h` | one_head_filter_pi_star | 97 | 7.9107 | 1.3562 | 0.6186 | 1.1637 | 0.0057 | 0.1237 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema3700_below_at_h` | one_head_filter_pi_star | 297 | 24.2859 | 1.0544 | 0.5488 | 0.3897 | 0.0011 | 0.1347 | ok | RAN |
| ETHUSDT | 8 | `ema3700_below_at_h` | one_head_filter_pi_star | 341 | 27.7410 | 1.0076 | 0.5630 | 0.0598 | 0.0002 | 0.1349 | ok | RAN |
| SOLUSDT | 8 | `ema3700_below_at_h` | one_head_filter_pi_star | 271 | 22.1599 | 1.0083 | 0.5351 | 0.0590 | 0.0002 | 0.1402 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `ema3700_below_at_h` | one_head_filter_pi_star | 338 | 27.4970 | 0.9733 | 0.5562 | -0.2120 | -0.0009 | 0.1361 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema3700_above_at_h` | one_head_filter_pi_star | 39 | 4.5829 | 0.9019 | 0.5385 | -0.3470 | -0.0045 | 0.1282 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema3700_above_at_h` | one_head_filter_pi_star | 36 | 10.6222 | 0.6853 | 0.4722 | -1.7227 | -0.0172 | 0.1389 | ok | RAN |
| ETHUSDT | 4 | `ema3700_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema3700_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema3700_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema3700_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema3700_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema3700_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema3700_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema3700_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema3700_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema3700_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema3700_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema3700_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema3700_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema3700_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema3700_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema3700_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
