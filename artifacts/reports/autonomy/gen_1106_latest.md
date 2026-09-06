# Autonomy public-indicator hunt gen 1106

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T234836Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret960_neg_at_h` | one_head_filter_pi_star | 218 | 17.8086 | 1.8456 | 0.6835 | 3.8565 | 0.0209 | 0.3716 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret960_neg_at_h` | one_head_filter_pi_star | 281 | 22.9551 | 1.7516 | 0.6548 | 4.1923 | 0.0185 | 0.3381 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret960_neg_at_h` | one_head_filter_pi_star | 264 | 21.5875 | 1.8940 | 0.6515 | 4.2721 | 0.0137 | 0.3295 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret960_neg_at_h` | one_head_filter_pi_star | 271 | 22.1599 | 1.8558 | 0.6458 | 4.0475 | 0.0129 | 0.3210 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret960_pos_at_h` | one_head_filter_pi_star | 69 | 5.8058 | 1.3036 | 0.6087 | 0.9625 | 0.0123 | 0.2029 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ret960_pos_at_h` | one_head_filter_pi_star | 54 | 4.6393 | 1.5373 | 0.6481 | 1.3750 | 0.0078 | 0.2963 | ok | RAN |
| SOLUSDT | 8 | `ret960_pos_at_h` | one_head_filter_pi_star | 53 | 4.3562 | 1.4873 | 0.6415 | 1.2157 | 0.0067 | 0.2264 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret960_pos_at_h` | one_head_filter_pi_star | 51 | 4.4850 | 0.9947 | 0.5686 | -0.0162 | -0.0003 | 0.3137 | ok | RAN |
| BTCUSDT | 4 | `ret960_pos_at_h` | one_head_filter_pi_star | 15 | 1.2765 | 0.3384 | 0.2667 | -1.4922 | -0.0786 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret960_pos_at_h` | one_head_filter_pi_star | 14 | 1.1914 | 0.3556 | 0.2857 | -1.3912 | -0.0863 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret960_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret960_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret960_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret960_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret960_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret960_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret960_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret960_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret960_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret960_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret960_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret960_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret960_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret960_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
