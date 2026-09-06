# Autonomy public-indicator hunt gen 1373

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260830T030905Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret239_neg_at_h` | one_head_filter_pi_star | 172 | 14.0508 | 2.0536 | 0.6977 | 4.1313 | 0.0251 | 0.3605 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret239_neg_at_h` | one_head_filter_pi_star | 171 | 13.9691 | 1.9825 | 0.6901 | 4.0893 | 0.0242 | 0.3801 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret239_neg_at_h` | one_head_filter_pi_star | 197 | 16.1089 | 1.9411 | 0.6548 | 3.9127 | 0.0139 | 0.3350 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret239_neg_at_h` | one_head_filter_pi_star | 196 | 16.0271 | 1.8317 | 0.6531 | 3.5982 | 0.0131 | 0.3418 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ret239_pos_at_h` | one_head_filter_pi_star | 174 | 14.3026 | 1.2479 | 0.6092 | 1.2279 | 0.0086 | 0.2299 | ok | RAN |
| SOLUSDT | 8 | `ret239_pos_at_h` | one_head_filter_pi_star | 175 | 14.2696 | 1.4808 | 0.6171 | 2.1991 | 0.0073 | 0.2743 | ok | RAN |
| SOLUSDT | 4 | `ret239_pos_at_h` | one_head_filter_pi_star | 190 | 15.4927 | 1.4662 | 0.6105 | 2.1594 | 0.0070 | 0.2737 | ok | RAN |
| ETHUSDT | 8 | `ret239_pos_at_h` | one_head_filter_pi_star | 161 | 13.2859 | 1.1624 | 0.5963 | 0.7897 | 0.0058 | 0.2112 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret239_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0397 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret239_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret239_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret239_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret239_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret239_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret239_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret239_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret239_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret239_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret239_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret239_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret239_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret239_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret239_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret239_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
