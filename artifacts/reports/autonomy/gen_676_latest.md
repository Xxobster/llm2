# Autonomy public-indicator hunt gen 676

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T052937Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema605_below_at_h` | one_head_filter_pi_star | 208 | 16.9917 | 1.9115 | 0.6779 | 4.1016 | 0.0214 | 0.3702 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema605_below_at_h` | one_head_filter_pi_star | 208 | 16.9917 | 1.8105 | 0.6683 | 3.7315 | 0.0200 | 0.3798 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema605_below_at_h` | one_head_filter_pi_star | 212 | 17.3354 | 1.8822 | 0.6651 | 3.8141 | 0.0127 | 0.3208 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema605_below_at_h` | one_head_filter_pi_star | 216 | 17.6625 | 1.7501 | 0.6481 | 3.3722 | 0.0115 | 0.3241 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema605_above_at_h` | one_head_filter_pi_star | 133 | 10.9067 | 1.7453 | 0.6391 | 2.7553 | 0.0110 | 0.3083 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema605_above_at_h` | one_head_filter_pi_star | 154 | 12.6288 | 1.7012 | 0.6364 | 2.7750 | 0.0105 | 0.3052 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ema605_above_at_h` | one_head_filter_pi_star | 156 | 12.8230 | 1.2164 | 0.5962 | 1.0124 | 0.0077 | 0.2051 | ok | RAN |
| ETHUSDT | 8 | `ema605_above_at_h` | one_head_filter_pi_star | 155 | 12.7408 | 1.2126 | 0.6129 | 1.0098 | 0.0075 | 0.2000 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema605_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5765 | 0.2778 | -0.8994 | -0.0449 | 0.0556 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema605_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5765 | 0.2778 | -0.8994 | -0.0458 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema605_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema605_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema605_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema605_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema605_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema605_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema605_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema605_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema605_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema605_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema605_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema605_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema605_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema605_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
