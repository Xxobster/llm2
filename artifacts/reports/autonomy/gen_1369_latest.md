# Autonomy public-indicator hunt gen 1369

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260830T024717Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema2980_below_at_h` | one_head_filter_pi_star | 348 | 28.3105 | 1.5839 | 0.6408 | 3.6169 | 0.0157 | 0.3046 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema2980_below_at_h` | one_head_filter_pi_star | 345 | 28.0664 | 1.5744 | 0.6406 | 3.5692 | 0.0154 | 0.3014 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema2980_below_at_h` | one_head_filter_pi_star | 269 | 21.8837 | 1.8917 | 0.6543 | 4.3387 | 0.0135 | 0.3383 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema2980_below_at_h` | one_head_filter_pi_star | 306 | 24.8937 | 1.8632 | 0.6503 | 4.4727 | 0.0130 | 0.3268 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema2980_above_at_h` | one_head_filter_pi_star | 108 | 8.8565 | 1.7113 | 0.6389 | 2.2637 | 0.0098 | 0.2593 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema2980_above_at_h` | one_head_filter_pi_star | 98 | 8.0548 | 1.5827 | 0.6531 | 1.8547 | 0.0086 | 0.2347 | ok | RAN |
| ETHUSDT | 4 | `ema2980_above_at_h` | one_head_filter_pi_star | 41 | 4.6736 | 1.1308 | 0.5610 | 0.3855 | 0.0059 | 0.2439 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema2980_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.7186 | 0.3333 | -0.5631 | -0.0284 | 0.1111 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema2980_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema2980_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2980_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2980_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2980_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema2980_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema2980_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema2980_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema2980_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2980_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2980_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema2980_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2980_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2980_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema2980_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2980_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
