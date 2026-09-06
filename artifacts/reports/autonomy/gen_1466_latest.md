# Autonomy public-indicator hunt gen 1466

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260830T233812Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ret1320_pos_at_h` | one_head_filter_pi_star | 24 | 2.0203 | 3.7861 | 0.7917 | 2.4405 | 0.0231 | 0.3750 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret1320_neg_at_h` | one_head_filter_pi_star | 345 | 28.0664 | 1.6830 | 0.6522 | 4.1347 | 0.0177 | 0.3014 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ret1320_neg_at_h` | one_head_filter_pi_star | 350 | 28.4732 | 1.6560 | 0.6571 | 4.0072 | 0.0174 | 0.3000 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret1320_pos_at_h` | one_head_filter_pi_star | 15 | 1.3237 | 2.4178 | 0.7333 | 1.4700 | 0.0159 | 0.4667 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret1320_neg_at_h` | one_head_filter_pi_star | 347 | 28.2291 | 1.6939 | 0.6369 | 4.1567 | 0.0105 | 0.3141 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret1320_neg_at_h` | one_head_filter_pi_star | 357 | 29.0427 | 1.6579 | 0.6331 | 4.0364 | 0.0100 | 0.3109 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret1320_pos_at_h` | one_head_filter_pi_star | 24 | 2.3716 | 0.9803 | 0.5000 | -0.0472 | -0.0007 | 0.0833 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1320_pos_at_h` | one_head_filter_pi_star | 17 | 3.4072 | 0.9492 | 0.5294 | -0.1302 | -0.0016 | 0.1176 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret1320_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6498 | 0.3529 | -0.6566 | -0.0283 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret1320_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4966 | 0.3158 | -1.0784 | -0.0476 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1320_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret1320_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1320_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1320_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1320_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1320_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1320_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1320_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1320_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1320_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1320_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1320_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret1320_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1320_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
