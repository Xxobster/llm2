# Autonomy public-indicator hunt gen 1300

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T202116Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema943_below_at_h` | one_head_filter_pi_star | 225 | 18.3804 | 1.7422 | 0.6622 | 3.7215 | 0.0182 | 0.3556 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema943_below_at_h` | one_head_filter_pi_star | 239 | 19.5241 | 1.7319 | 0.6485 | 3.7031 | 0.0182 | 0.3347 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `ema943_above_at_h` | one_head_filter_pi_star | 133 | 10.9763 | 1.3581 | 0.6241 | 1.5038 | 0.0126 | 0.2331 | ok | RAN |
| SOLUSDT | 8 | `ema943_below_at_h` | one_head_filter_pi_star | 228 | 18.6438 | 1.8137 | 0.6579 | 3.7596 | 0.0123 | 0.3114 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema943_above_at_h` | one_head_filter_pi_star | 133 | 10.8449 | 1.8084 | 0.6541 | 2.7800 | 0.0115 | 0.3233 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema943_below_at_h` | one_head_filter_pi_star | 243 | 19.8703 | 1.7098 | 0.6461 | 3.5592 | 0.0113 | 0.3086 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema943_above_at_h` | one_head_filter_pi_star | 125 | 10.1925 | 1.6754 | 0.6400 | 2.4221 | 0.0098 | 0.3120 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema943_above_at_h` | one_head_filter_pi_star | 121 | 9.9859 | 1.1129 | 0.5868 | 0.5091 | 0.0046 | 0.1983 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema943_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6498 | 0.3529 | -0.6566 | -0.0288 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema943_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema943_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema943_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema943_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema943_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema943_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema943_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema943_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema943_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema943_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema943_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema943_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema943_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema943_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema943_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
