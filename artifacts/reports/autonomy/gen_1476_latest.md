# Autonomy public-indicator hunt gen 1476

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260831T003352Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 8 | `ema969_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 3.3760 | 0.7000 | 1.9329 | 0.1424 | 0.4000 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema969_below_at_h` | one_head_filter_pi_star | 215 | 17.5635 | 1.9147 | 0.6651 | 3.9590 | 0.0210 | 0.3721 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema969_below_at_h` | one_head_filter_pi_star | 235 | 19.1973 | 1.7220 | 0.6511 | 3.6532 | 0.0177 | 0.3447 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema969_below_at_h` | one_head_filter_pi_star | 259 | 21.1787 | 1.7929 | 0.6486 | 3.9448 | 0.0124 | 0.3089 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema969_below_at_h` | one_head_filter_pi_star | 249 | 20.3609 | 1.7281 | 0.6466 | 3.6484 | 0.0115 | 0.2972 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema969_above_at_h` | one_head_filter_pi_star | 123 | 10.1096 | 1.7431 | 0.6667 | 2.5287 | 0.0110 | 0.3089 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ema969_above_at_h` | one_head_filter_pi_star | 138 | 11.3434 | 1.2455 | 0.5942 | 1.0903 | 0.0092 | 0.2174 | ok | RAN |
| SOLUSDT | 8 | `ema969_above_at_h` | one_head_filter_pi_star | 123 | 10.0295 | 1.5611 | 0.6260 | 2.0612 | 0.0087 | 0.3008 | ok | RAN |
| ETHUSDT | 4 | `ema969_above_at_h` | one_head_filter_pi_star | 133 | 10.9753 | 1.1104 | 0.5714 | 0.5157 | 0.0045 | 0.2105 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema969_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6498 | 0.3529 | -0.6566 | -0.0294 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema969_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6498 | 0.3529 | -0.6566 | -0.0307 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema969_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema969_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema969_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema969_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema969_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema969_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema969_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema969_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema969_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema969_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema969_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema969_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema969_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
