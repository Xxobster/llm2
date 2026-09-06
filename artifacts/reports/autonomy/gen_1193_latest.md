# Autonomy public-indicator hunt gen 1193

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T093739Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema2540_below_at_h` | one_head_filter_pi_star | 345 | 28.0664 | 1.6657 | 0.6522 | 3.9287 | 0.0174 | 0.3101 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema2540_below_at_h` | one_head_filter_pi_star | 342 | 27.8224 | 1.6093 | 0.6404 | 3.6594 | 0.0161 | 0.3041 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema2540_below_at_h` | one_head_filter_pi_star | 280 | 22.7786 | 1.8925 | 0.6536 | 4.4136 | 0.0133 | 0.3250 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema2540_below_at_h` | one_head_filter_pi_star | 273 | 22.2091 | 1.8331 | 0.6520 | 4.1101 | 0.0128 | 0.3297 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema2540_above_at_h` | one_head_filter_pi_star | 107 | 8.8931 | 1.6051 | 0.6355 | 2.0823 | 0.0095 | 0.2617 | ok | RAN |
| SOLUSDT | 4 | `ema2540_above_at_h` | one_head_filter_pi_star | 109 | 8.9385 | 1.5873 | 0.6330 | 2.0332 | 0.0091 | 0.2752 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema2540_above_at_h` | one_head_filter_pi_star | 12 | 3.6212 | 0.5569 | 0.3333 | -1.7622 | -0.0292 | 0.2500 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema2540_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.7186 | 0.3333 | -0.5631 | -0.0301 | 0.1111 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema2540_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5935 | 0.2941 | -0.8400 | -0.0454 | 0.0588 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema2540_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 4 | `ema2540_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema2540_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2540_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2540_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema2540_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema2540_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema2540_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema2540_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2540_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema2540_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2540_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2540_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema2540_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2540_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
