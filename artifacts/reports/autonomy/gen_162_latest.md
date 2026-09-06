# Autonomy public-indicator hunt gen 162

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T200655Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret72_neg_at_h` | one_head_filter_pi_star | 192 | 15.6846 | 1.7829 | 0.6719 | 3.8601 | 0.0203 | 0.3802 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret72_neg_at_h` | one_head_filter_pi_star | 195 | 15.9297 | 1.6997 | 0.6615 | 3.3993 | 0.0181 | 0.3692 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret72_neg_at_h` | one_head_filter_pi_star | 189 | 15.4547 | 2.1100 | 0.6720 | 4.2982 | 0.0163 | 0.3757 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret72_neg_at_h` | one_head_filter_pi_star | 193 | 15.7818 | 2.1425 | 0.6736 | 4.3467 | 0.0161 | 0.3731 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `ret72_pos_at_h` | one_head_filter_pi_star | 189 | 15.5356 | 1.3157 | 0.6190 | 1.5797 | 0.0102 | 0.2275 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ret72_pos_at_h` | one_head_filter_pi_star | 179 | 14.7136 | 1.3061 | 0.6201 | 1.5009 | 0.0100 | 0.2346 | ok | RAN |
| SOLUSDT | 4 | `ret72_pos_at_h` | one_head_filter_pi_star | 182 | 14.8404 | 1.3875 | 0.6044 | 1.9420 | 0.0060 | 0.2582 | ok | RAN |
| SOLUSDT | 8 | `ret72_pos_at_h` | one_head_filter_pi_star | 194 | 15.8188 | 1.3458 | 0.6082 | 1.7928 | 0.0056 | 0.2629 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret72_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret72_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5834 | 0.3333 | -0.8834 | -0.0450 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret72_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret72_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret72_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret72_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret72_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret72_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret72_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret72_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret72_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret72_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret72_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret72_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret72_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret72_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
