# Autonomy public-indicator hunt gen 565

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T221330Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret89_neg_at_h` | one_head_filter_pi_star | 191 | 15.6030 | 1.8673 | 0.6754 | 3.9773 | 0.0220 | 0.3770 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret89_neg_at_h` | one_head_filter_pi_star | 197 | 16.0931 | 1.8798 | 0.6751 | 4.1139 | 0.0215 | 0.3655 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret89_neg_at_h` | one_head_filter_pi_star | 188 | 15.3729 | 2.2170 | 0.6755 | 4.4656 | 0.0167 | 0.3617 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret89_neg_at_h` | one_head_filter_pi_star | 185 | 15.1276 | 2.1672 | 0.6757 | 4.2789 | 0.0163 | 0.3622 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ret89_pos_at_h` | one_head_filter_pi_star | 189 | 15.5356 | 1.2554 | 0.6138 | 1.2344 | 0.0086 | 0.2222 | ok | RAN |
| ETHUSDT | 4 | `ret89_pos_at_h` | one_head_filter_pi_star | 182 | 14.9602 | 1.2132 | 0.6154 | 1.0905 | 0.0073 | 0.2253 | ok | RAN |
| SOLUSDT | 8 | `ret89_pos_at_h` | one_head_filter_pi_star | 184 | 15.0034 | 1.3801 | 0.6033 | 1.9183 | 0.0060 | 0.2663 | ok | RAN |
| SOLUSDT | 4 | `ret89_pos_at_h` | one_head_filter_pi_star | 193 | 15.7373 | 1.3362 | 0.5959 | 1.7516 | 0.0054 | 0.2539 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret89_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret89_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret89_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret89_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret89_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret89_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret89_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret89_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret89_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret89_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret89_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret89_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret89_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret89_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret89_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret89_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
