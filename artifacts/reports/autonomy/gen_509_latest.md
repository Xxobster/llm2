# Autonomy public-indicator hunt gen 509

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T183002Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret75_neg_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 1.8420 | 0.6772 | 3.9768 | 0.0215 | 0.3810 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret75_neg_at_h` | one_head_filter_pi_star | 198 | 16.1748 | 1.7807 | 0.6717 | 3.6893 | 0.0199 | 0.3737 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret75_neg_at_h` | one_head_filter_pi_star | 188 | 15.3729 | 2.2673 | 0.6809 | 4.5218 | 0.0173 | 0.3670 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret75_neg_at_h` | one_head_filter_pi_star | 175 | 14.3099 | 2.1005 | 0.6686 | 3.9916 | 0.0159 | 0.3771 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `ret75_pos_at_h` | one_head_filter_pi_star | 189 | 15.5356 | 1.3340 | 0.6190 | 1.6594 | 0.0108 | 0.2275 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ret75_pos_at_h` | one_head_filter_pi_star | 185 | 15.2068 | 1.2435 | 0.6108 | 1.2581 | 0.0082 | 0.2270 | ok | RAN |
| SOLUSDT | 8 | `ret75_pos_at_h` | one_head_filter_pi_star | 189 | 15.4111 | 1.4927 | 0.6190 | 2.4125 | 0.0073 | 0.2593 | ok | RAN |
| SOLUSDT | 4 | `ret75_pos_at_h` | one_head_filter_pi_star | 191 | 15.5742 | 1.4518 | 0.6126 | 2.2464 | 0.0068 | 0.2670 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret75_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret75_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5834 | 0.3333 | -0.8834 | -0.0450 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret75_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret75_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret75_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret75_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret75_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret75_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret75_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret75_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret75_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret75_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret75_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret75_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret75_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret75_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
