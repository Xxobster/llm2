# Autonomy public-indicator hunt gen 354

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T153559Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret208_neg_at_h` | one_head_filter_pi_star | 164 | 13.3973 | 2.1021 | 0.6951 | 4.3803 | 0.0259 | 0.4024 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret208_neg_at_h` | one_head_filter_pi_star | 177 | 14.4593 | 2.0415 | 0.7006 | 4.3487 | 0.0239 | 0.4011 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret208_neg_at_h` | one_head_filter_pi_star | 168 | 13.7375 | 2.1704 | 0.6964 | 4.1107 | 0.0165 | 0.3690 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret208_neg_at_h` | one_head_filter_pi_star | 167 | 13.6557 | 1.9497 | 0.6647 | 3.5591 | 0.0142 | 0.3772 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ret208_pos_at_h` | one_head_filter_pi_star | 170 | 13.8619 | 1.4709 | 0.6176 | 2.1098 | 0.0073 | 0.2882 | ok | RAN |
| SOLUSDT | 8 | `ret208_pos_at_h` | one_head_filter_pi_star | 188 | 15.3296 | 1.4362 | 0.6011 | 2.1112 | 0.0067 | 0.2606 | ok | RAN |
| ETHUSDT | 8 | `ret208_pos_at_h` | one_head_filter_pi_star | 193 | 15.8644 | 1.1926 | 0.5855 | 1.0370 | 0.0067 | 0.2383 | ok | RAN |
| ETHUSDT | 4 | `ret208_pos_at_h` | one_head_filter_pi_star | 195 | 16.0287 | 1.1423 | 0.5795 | 0.7577 | 0.0052 | 0.2359 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret208_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0411 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret208_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5834 | 0.3333 | -0.8834 | -0.0433 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret208_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret208_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret208_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret208_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret208_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret208_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret208_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret208_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret208_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret208_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret208_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret208_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret208_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret208_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
