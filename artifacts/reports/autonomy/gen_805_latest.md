# Autonomy public-indicator hunt gen 805

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T161027Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret149_neg_at_h` | one_head_filter_pi_star | 198 | 16.1748 | 2.0125 | 0.6919 | 4.5642 | 0.0238 | 0.3737 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret149_neg_at_h` | one_head_filter_pi_star | 183 | 14.9494 | 1.7903 | 0.6721 | 3.7590 | 0.0199 | 0.3716 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret149_neg_at_h` | one_head_filter_pi_star | 177 | 14.4734 | 2.1039 | 0.6723 | 4.0700 | 0.0156 | 0.3729 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret149_neg_at_h` | one_head_filter_pi_star | 195 | 15.9453 | 2.0292 | 0.6718 | 4.0920 | 0.0149 | 0.3538 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ret149_pos_at_h` | one_head_filter_pi_star | 177 | 14.6063 | 1.1841 | 0.5932 | 0.9406 | 0.0066 | 0.2147 | ok | RAN |
| ETHUSDT | 4 | `ret149_pos_at_h` | one_head_filter_pi_star | 193 | 15.8048 | 1.1775 | 0.6010 | 0.9449 | 0.0062 | 0.2280 | ok | RAN |
| SOLUSDT | 4 | `ret149_pos_at_h` | one_head_filter_pi_star | 183 | 14.9219 | 1.3891 | 0.6011 | 1.8781 | 0.0061 | 0.2678 | ok | RAN |
| SOLUSDT | 8 | `ret149_pos_at_h` | one_head_filter_pi_star | 179 | 14.5957 | 1.3174 | 0.5754 | 1.5320 | 0.0052 | 0.2514 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret149_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret149_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret149_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret149_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret149_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret149_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret149_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret149_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret149_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret149_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret149_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret149_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret149_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret149_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret149_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret149_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
