# Autonomy public-indicator hunt gen 802

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T155305Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret656_neg_at_h` | one_head_filter_pi_star | 195 | 15.9297 | 1.8695 | 0.6667 | 3.9736 | 0.0199 | 0.3590 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret656_neg_at_h` | one_head_filter_pi_star | 182 | 14.8677 | 1.7858 | 0.6648 | 3.4779 | 0.0178 | 0.3462 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret656_neg_at_h` | one_head_filter_pi_star | 233 | 19.0526 | 2.0181 | 0.6781 | 4.3663 | 0.0162 | 0.3391 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret656_neg_at_h` | one_head_filter_pi_star | 212 | 17.4502 | 1.9632 | 0.6698 | 3.9114 | 0.0154 | 0.3396 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ret656_pos_at_h` | one_head_filter_pi_star | 115 | 9.4306 | 1.6480 | 0.6696 | 2.3113 | 0.0090 | 0.2783 | ok | RAN |
| SOLUSDT | 8 | `ret656_pos_at_h` | one_head_filter_pi_star | 114 | 9.3554 | 1.6245 | 0.6491 | 2.1437 | 0.0086 | 0.2632 | ok | RAN |
| ETHUSDT | 8 | `ret656_pos_at_h` | one_head_filter_pi_star | 133 | 10.9324 | 1.1188 | 0.5865 | 0.5845 | 0.0051 | 0.2556 | ok | RAN |
| ETHUSDT | 4 | `ret656_pos_at_h` | one_head_filter_pi_star | 135 | 11.0968 | 1.0543 | 0.5630 | 0.2598 | 0.0023 | 0.2444 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret656_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4777 | 0.2778 | -1.1199 | -0.0562 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret656_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4385 | 0.2222 | -1.2856 | -0.0664 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret656_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret656_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret656_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret656_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret656_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret656_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret656_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret656_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret656_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret656_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret656_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret656_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret656_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret656_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
