# Autonomy public-indicator hunt gen 421

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T070950Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret53_neg_at_h` | one_head_filter_pi_star | 193 | 15.7663 | 1.7381 | 0.6684 | 3.5728 | 0.0201 | 0.3627 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret53_neg_at_h` | one_head_filter_pi_star | 198 | 16.1748 | 1.7116 | 0.6768 | 3.5224 | 0.0198 | 0.3586 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret53_neg_at_h` | one_head_filter_pi_star | 168 | 13.7375 | 2.2505 | 0.7024 | 4.3004 | 0.0183 | 0.4048 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret53_neg_at_h` | one_head_filter_pi_star | 171 | 13.9828 | 2.1343 | 0.6901 | 4.1100 | 0.0173 | 0.3918 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `ret53_pos_at_h` | one_head_filter_pi_star | 186 | 15.2890 | 1.3646 | 0.6075 | 1.7100 | 0.0109 | 0.2312 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ret53_pos_at_h` | one_head_filter_pi_star | 182 | 14.9602 | 1.2934 | 0.5989 | 1.4263 | 0.0093 | 0.2363 | ok | RAN |
| SOLUSDT | 8 | `ret53_pos_at_h` | one_head_filter_pi_star | 202 | 16.4712 | 1.5099 | 0.6188 | 2.5521 | 0.0072 | 0.2624 | ok | RAN |
| ETHUSDT | 8 | `ret53_cross_down_0` | one_head_filter_pi_star | 13 | 1.4730 | 1.1562 | 0.5385 | 0.2551 | 0.0064 | 0.0769 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ret53_pos_at_h` | one_head_filter_pi_star | 206 | 16.7973 | 1.3714 | 0.5874 | 1.9733 | 0.0056 | 0.2524 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret53_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.7517 | 0.3333 | -0.4636 | -0.0208 | 0.0556 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret53_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret53_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret53_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret53_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret53_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret53_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret53_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 8 | `ret53_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret53_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret53_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret53_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret53_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret53_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret53_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
