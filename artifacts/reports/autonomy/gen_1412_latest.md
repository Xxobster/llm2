# Autonomy public-indicator hunt gen 1412

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260830T065959Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema959_below_at_h` | one_head_filter_pi_star | 229 | 18.7072 | 1.8172 | 0.6638 | 3.8015 | 0.0192 | 0.3581 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema959_below_at_h` | one_head_filter_pi_star | 235 | 19.1973 | 1.7099 | 0.6553 | 3.5539 | 0.0174 | 0.3447 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema959_below_at_h` | one_head_filter_pi_star | 257 | 21.0151 | 1.8127 | 0.6537 | 4.0274 | 0.0127 | 0.3074 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema959_above_at_h` | one_head_filter_pi_star | 133 | 10.8449 | 1.7698 | 0.6316 | 2.6616 | 0.0109 | 0.3008 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema959_below_at_h` | one_head_filter_pi_star | 265 | 21.6693 | 1.6195 | 0.6302 | 3.3009 | 0.0103 | 0.3132 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema959_above_at_h` | one_head_filter_pi_star | 122 | 9.9479 | 1.5677 | 0.6230 | 2.0603 | 0.0082 | 0.3279 | ok | RAN |
| ETHUSDT | 8 | `ema959_above_at_h` | one_head_filter_pi_star | 131 | 10.8112 | 1.1829 | 0.5954 | 0.8383 | 0.0070 | 0.2290 | ok | RAN |
| ETHUSDT | 4 | `ema959_above_at_h` | one_head_filter_pi_star | 112 | 9.2432 | 1.1517 | 0.5714 | 0.6396 | 0.0058 | 0.2143 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema959_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6498 | 0.3529 | -0.6566 | -0.0294 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema959_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0526 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema959_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema959_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema959_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema959_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema959_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema959_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema959_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema959_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema959_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema959_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema959_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema959_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema959_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema959_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
