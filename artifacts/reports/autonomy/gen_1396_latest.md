# Autonomy public-indicator hunt gen 1396

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260830T051938Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema957_below_at_h` | one_head_filter_pi_star | 221 | 18.0537 | 1.8361 | 0.6606 | 3.8182 | 0.0195 | 0.3575 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema957_below_at_h` | one_head_filter_pi_star | 225 | 18.3804 | 1.7027 | 0.6489 | 3.5112 | 0.0169 | 0.3378 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `ema957_above_at_h` | one_head_filter_pi_star | 135 | 11.0968 | 1.3844 | 0.6148 | 1.6413 | 0.0136 | 0.2370 | ok | RAN |
| SOLUSDT | 4 | `ema957_below_at_h` | one_head_filter_pi_star | 249 | 20.3609 | 1.8298 | 0.6506 | 3.9687 | 0.0124 | 0.3052 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema957_below_at_h` | one_head_filter_pi_star | 259 | 21.1787 | 1.7902 | 0.6448 | 3.9347 | 0.0122 | 0.3089 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema957_above_at_h` | one_head_filter_pi_star | 122 | 9.9479 | 1.7295 | 0.6311 | 2.4932 | 0.0105 | 0.3033 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema957_above_at_h` | one_head_filter_pi_star | 128 | 10.4372 | 1.6668 | 0.6406 | 2.4258 | 0.0102 | 0.3125 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ema957_above_at_h` | one_head_filter_pi_star | 120 | 9.9034 | 1.2421 | 0.6000 | 1.0099 | 0.0091 | 0.2167 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema957_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6498 | 0.3529 | -0.6566 | -0.0294 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema957_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema957_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema957_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema957_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema957_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema957_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema957_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema957_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema957_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema957_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema957_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema957_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema957_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema957_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema957_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
