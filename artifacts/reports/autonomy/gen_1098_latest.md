# Autonomy public-indicator hunt gen 1098

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T224958Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret952_neg_at_h` | one_head_filter_pi_star | 149 | 12.2528 | 2.2051 | 0.7114 | 3.9534 | 0.0252 | 0.4362 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret952_neg_at_h` | one_head_filter_pi_star | 273 | 22.3016 | 1.7692 | 0.6593 | 4.1764 | 0.0185 | 0.3297 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret952_neg_at_h` | one_head_filter_pi_star | 247 | 20.1974 | 2.0942 | 0.6721 | 4.7778 | 0.0156 | 0.3360 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret952_neg_at_h` | one_head_filter_pi_star | 261 | 21.2329 | 2.0867 | 0.6628 | 4.7341 | 0.0149 | 0.3257 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret952_pos_at_h` | one_head_filter_pi_star | 50 | 4.1564 | 2.2519 | 0.7200 | 2.3649 | 0.0145 | 0.2800 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ret952_pos_at_h` | one_head_filter_pi_star | 69 | 5.6945 | 1.2205 | 0.6087 | 0.7178 | 0.0090 | 0.2319 | ok | RAN |
| ETHUSDT | 4 | `ret952_pos_at_h` | one_head_filter_pi_star | 63 | 5.3932 | 1.1778 | 0.6032 | 0.5774 | 0.0079 | 0.2222 | ok | RAN |
| SOLUSDT | 4 | `ret952_pos_at_h` | one_head_filter_pi_star | 29 | 2.8232 | 1.4582 | 0.6552 | 0.9389 | 0.0070 | 0.2414 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret952_pos_at_h` | one_head_filter_pi_star | 12 | 1.0212 | 0.5188 | 0.3333 | -0.8440 | -0.0400 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret952_pos_at_h` | one_head_filter_pi_star | 14 | 1.1914 | 0.4998 | 0.3571 | -0.9472 | -0.0481 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret952_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret952_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret952_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret952_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret952_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret952_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret952_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret952_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret952_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret952_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret952_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret952_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret952_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret952_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
