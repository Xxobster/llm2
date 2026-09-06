# Autonomy public-indicator hunt gen 070

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T140855Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret4_neg_at_h` | one_head_filter_pi_star | 29 | 2.6377 | 5.0474 | 0.8621 | 3.1737 | 0.0800 | 0.3103 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret4_cross_up_0` | one_head_filter_pi_star | 16 | 1.8179 | 2.3848 | 0.6250 | 1.6917 | 0.0647 | 0.2500 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ret4_pos_at_h` | one_head_filter_pi_star | 14 | 1.3310 | 13.6533 | 0.7857 | 3.0630 | 0.0412 | 0.5000 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret4_pos_at_h` | one_head_filter_pi_star | 80 | 6.9193 | 2.3658 | 0.7250 | 3.3612 | 0.0323 | 0.4250 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret4_cross_up_0` | one_head_filter_pi_star | 255 | 20.8312 | 1.8944 | 0.6863 | 4.3977 | 0.0223 | 0.3608 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret4_cross_up_0` | one_head_filter_pi_star | 202 | 16.5016 | 1.7917 | 0.6683 | 3.6418 | 0.0198 | 0.3614 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret4_cross_down_0` | one_head_filter_pi_star | 270 | 22.1208 | 1.6543 | 0.6593 | 3.5574 | 0.0180 | 0.3037 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret4_cross_up_0` | one_head_filter_pi_star | 111 | 9.0766 | 2.1957 | 0.7207 | 3.2623 | 0.0162 | 0.4054 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret4_cross_up_0` | one_head_filter_pi_star | 203 | 16.5144 | 2.0750 | 0.6749 | 4.1371 | 0.0161 | 0.3842 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret4_neg_at_h` | one_head_filter_pi_star | 34 | 2.9990 | 1.9374 | 0.6176 | 1.5240 | 0.0154 | 0.2059 | TPM<MIN | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret4_pos_at_h` | one_head_filter_pi_star | 49 | 4.3311 | 2.0813 | 0.7143 | 2.2905 | 0.0146 | 0.5306 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ret4_cross_down_0` | one_head_filter_pi_star | 158 | 12.8834 | 1.5222 | 0.6203 | 2.2503 | 0.0075 | 0.2025 | ok | RAN |
| SOLUSDT | 8 | `ret4_cross_down_0` | one_head_filter_pi_star | 261 | 21.2820 | 1.4583 | 0.6130 | 2.6754 | 0.0069 | 0.3103 | ok | RAN |
| SOLUSDT | 4 | `ret4_neg_at_h` | one_head_filter_pi_star | 17 | 1.5839 | 1.2352 | 0.5882 | 0.3844 | 0.0041 | 0.0588 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret4_cross_down_0` | one_head_filter_pi_star | 156 | 12.8733 | 1.0914 | 0.5769 | 0.4460 | 0.0030 | 0.1859 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret4_cross_down_0` | one_head_filter_pi_star | 21 | 1.7871 | 0.8381 | 0.3810 | -0.3159 | -0.0149 | 0.0476 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret4_cross_down_0` | one_head_filter_pi_star | 15 | 1.2765 | 0.3490 | 0.2667 | -1.4287 | -0.0566 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret4_pos_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret4_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret4_pos_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret4_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret4_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret4_pos_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret4_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
