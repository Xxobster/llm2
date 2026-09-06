# Autonomy public-indicator hunt gen 449

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T141630Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema680_below_at_h` | one_head_filter_pi_star | 201 | 16.4199 | 1.9257 | 0.6716 | 3.9368 | 0.0213 | 0.3682 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema680_below_at_h` | one_head_filter_pi_star | 208 | 16.9917 | 1.7759 | 0.6635 | 3.5867 | 0.0193 | 0.3654 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema680_below_at_h` | one_head_filter_pi_star | 219 | 17.9078 | 1.8757 | 0.6667 | 3.8902 | 0.0133 | 0.3333 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema680_below_at_h` | one_head_filter_pi_star | 220 | 17.9896 | 1.7894 | 0.6545 | 3.6138 | 0.0119 | 0.3273 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema680_above_at_h` | one_head_filter_pi_star | 139 | 11.3987 | 1.7148 | 0.6475 | 2.6678 | 0.0107 | 0.3309 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ema680_above_at_h` | one_head_filter_pi_star | 153 | 12.5764 | 1.2620 | 0.6013 | 1.1946 | 0.0091 | 0.2092 | ok | RAN |
| SOLUSDT | 4 | `ema680_above_at_h` | one_head_filter_pi_star | 129 | 10.5786 | 1.5637 | 0.6279 | 2.1477 | 0.0088 | 0.3256 | ok | RAN |
| ETHUSDT | 8 | `ema680_above_at_h` | one_head_filter_pi_star | 156 | 12.8230 | 1.2385 | 0.6154 | 1.0941 | 0.0085 | 0.1987 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema680_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema680_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5765 | 0.2778 | -0.8994 | -0.0458 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema680_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema680_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema680_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema680_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema680_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema680_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema680_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema680_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema680_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema680_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema680_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema680_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema680_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema680_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
