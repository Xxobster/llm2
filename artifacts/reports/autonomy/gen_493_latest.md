# Autonomy public-indicator hunt gen 493

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T172724Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret71_neg_at_h` | one_head_filter_pi_star | 187 | 15.2762 | 1.7850 | 0.6791 | 3.6503 | 0.0199 | 0.3797 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret71_neg_at_h` | one_head_filter_pi_star | 192 | 15.6846 | 1.7396 | 0.6667 | 3.7178 | 0.0194 | 0.3802 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret71_neg_at_h` | one_head_filter_pi_star | 178 | 14.5552 | 2.2798 | 0.6854 | 4.4560 | 0.0173 | 0.3764 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret71_neg_at_h` | one_head_filter_pi_star | 188 | 15.3729 | 2.1162 | 0.6755 | 4.2479 | 0.0163 | 0.3723 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `ret71_pos_at_h` | one_head_filter_pi_star | 191 | 15.7000 | 1.3440 | 0.6126 | 1.6893 | 0.0113 | 0.2251 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ret71_pos_at_h` | one_head_filter_pi_star | 181 | 14.8780 | 1.2777 | 0.6188 | 1.3875 | 0.0090 | 0.2210 | ok | RAN |
| SOLUSDT | 4 | `ret71_pos_at_h` | one_head_filter_pi_star | 191 | 15.5742 | 1.4211 | 0.6073 | 2.1319 | 0.0064 | 0.2513 | ok | RAN |
| SOLUSDT | 8 | `ret71_pos_at_h` | one_head_filter_pi_star | 192 | 15.6558 | 1.4192 | 0.6146 | 2.1085 | 0.0064 | 0.2552 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret71_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret71_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5834 | 0.3333 | -0.8834 | -0.0450 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret71_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret71_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret71_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret71_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret71_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret71_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret71_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret71_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret71_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret71_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret71_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret71_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret71_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret71_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
