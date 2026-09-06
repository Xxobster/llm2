# Autonomy public-indicator hunt gen 1138

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T032729Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret992_neg_at_h` | one_head_filter_pi_star | 200 | 16.3382 | 1.9874 | 0.6900 | 3.9680 | 0.0229 | 0.3850 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret992_neg_at_h` | one_head_filter_pi_star | 202 | 16.5016 | 1.9325 | 0.6832 | 4.0456 | 0.0220 | 0.3762 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret992_neg_at_h` | one_head_filter_pi_star | 273 | 22.2091 | 1.9419 | 0.6593 | 4.5828 | 0.0143 | 0.3333 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret992_neg_at_h` | one_head_filter_pi_star | 278 | 22.7648 | 1.8334 | 0.6547 | 4.1223 | 0.0124 | 0.3273 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret992_pos_at_h` | one_head_filter_pi_star | 26 | 2.2315 | 1.5668 | 0.6538 | 1.0422 | 0.0102 | 0.3077 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret992_pos_at_h` | one_head_filter_pi_star | 63 | 5.2370 | 1.6357 | 0.6984 | 1.7539 | 0.0092 | 0.2540 | ok | RAN |
| ETHUSDT | 4 | `ret992_pos_at_h` | one_head_filter_pi_star | 77 | 6.3919 | 1.0673 | 0.5714 | 0.2516 | 0.0032 | 0.2208 | ok | RAN |
| ETHUSDT | 8 | `ret992_pos_at_h` | one_head_filter_pi_star | 22 | 1.9662 | 1.0470 | 0.5455 | 0.0901 | 0.0024 | 0.3636 | EBR>35% | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret992_pos_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.3163 | 0.2500 | -1.5861 | -0.0724 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret992_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.3159 | 0.2353 | -1.5894 | -0.0725 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret992_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret992_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret992_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret992_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret992_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret992_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret992_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret992_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret992_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret992_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret992_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret992_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret992_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret992_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
