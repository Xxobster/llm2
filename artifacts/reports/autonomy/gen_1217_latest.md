# Autonomy public-indicator hunt gen 1217

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T115802Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 8 | `ema2600_below_at_h` | one_head_filter_pi_star | 9 | 1.2601 | 2.4502 | 0.6667 | 1.3795 | 0.0869 | 0.2222 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema2600_below_at_h` | one_head_filter_pi_star | 364 | 29.6121 | 1.6281 | 0.6484 | 3.9732 | 0.0169 | 0.2967 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema2600_below_at_h` | one_head_filter_pi_star | 334 | 27.1716 | 1.5675 | 0.6377 | 3.4275 | 0.0153 | 0.3084 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema2600_below_at_h` | one_head_filter_pi_star | 279 | 22.6972 | 1.9064 | 0.6559 | 4.4086 | 0.0132 | 0.3262 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema2600_below_at_h` | one_head_filter_pi_star | 273 | 22.2091 | 1.8801 | 0.6520 | 4.2665 | 0.0128 | 0.3223 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema2600_above_at_h` | one_head_filter_pi_star | 106 | 8.7123 | 1.6957 | 0.6604 | 2.2898 | 0.0101 | 0.2547 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema2600_above_at_h` | one_head_filter_pi_star | 96 | 7.9788 | 1.5167 | 0.6354 | 1.7300 | 0.0081 | 0.2500 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema2600_above_at_h` | one_head_filter_pi_star | 29 | 3.4078 | 0.9739 | 0.5172 | -0.0687 | -0.0012 | 0.2414 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema2600_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.7186 | 0.3333 | -0.5631 | -0.0301 | 0.1111 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema2600_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5935 | 0.2941 | -0.8400 | -0.0435 | 0.0588 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema2600_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema2600_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2600_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 8 | `ema2600_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2600_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema2600_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema2600_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema2600_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema2600_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2600_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema2600_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2600_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2600_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2600_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
