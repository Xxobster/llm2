# Autonomy public-indicator hunt gen 1033

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T144111Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 4 | `ema2140_below_at_h` | one_head_filter_pi_star | 9 | 1.2601 | 2.9118 | 0.6667 | 1.7154 | 0.1146 | 0.3333 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema2140_below_at_h` | one_head_filter_pi_star | 341 | 27.7410 | 1.6005 | 0.6422 | 3.6536 | 0.0158 | 0.3050 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema2140_below_at_h` | one_head_filter_pi_star | 341 | 27.7410 | 1.5726 | 0.6393 | 3.5177 | 0.0154 | 0.3021 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema2140_below_at_h` | one_head_filter_pi_star | 280 | 22.8958 | 1.7874 | 0.6500 | 4.0684 | 0.0124 | 0.3214 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema2140_below_at_h` | one_head_filter_pi_star | 294 | 23.9175 | 1.7478 | 0.6395 | 3.9969 | 0.0118 | 0.3197 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ema2140_above_at_h` | one_head_filter_pi_star | 53 | 4.6608 | 1.2409 | 0.5660 | 0.6611 | 0.0097 | 0.2453 | ok | RAN |
| SOLUSDT | 8 | `ema2140_above_at_h` | one_head_filter_pi_star | 109 | 8.9589 | 1.7055 | 0.6514 | 2.2836 | 0.0095 | 0.2477 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema2140_above_at_h` | one_head_filter_pi_star | 110 | 9.0411 | 1.5167 | 0.6364 | 1.8080 | 0.0074 | 0.2636 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema2140_above_at_h` | one_head_filter_pi_star | 35 | 3.2192 | 0.9088 | 0.4857 | -0.2474 | -0.0046 | 0.2857 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema2140_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.5944 | 0.3125 | -0.8370 | -0.0472 | 0.0625 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema2140_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.5944 | 0.3125 | -0.8370 | -0.0472 | 0.0625 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema2140_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema2140_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2140_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2140_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema2140_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema2140_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema2140_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema2140_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2140_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2140_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2140_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema2140_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2140_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
