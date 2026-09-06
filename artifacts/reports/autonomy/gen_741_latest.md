# Autonomy public-indicator hunt gen 741

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T100917Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret133_neg_at_h` | one_head_filter_pi_star | 195 | 15.9297 | 1.8801 | 0.6769 | 4.0403 | 0.0217 | 0.3590 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret133_neg_at_h` | one_head_filter_pi_star | 179 | 14.6227 | 1.7503 | 0.6648 | 3.5244 | 0.0191 | 0.3575 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret133_neg_at_h` | one_head_filter_pi_star | 180 | 14.7188 | 2.0523 | 0.6778 | 3.9940 | 0.0153 | 0.3611 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret133_neg_at_h` | one_head_filter_pi_star | 174 | 14.2281 | 2.0255 | 0.6724 | 3.8370 | 0.0150 | 0.3678 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ret133_pos_at_h` | one_head_filter_pi_star | 187 | 15.4315 | 1.2694 | 0.6096 | 1.3823 | 0.0092 | 0.2353 | ok | RAN |
| ETHUSDT | 4 | `ret133_pos_at_h` | one_head_filter_pi_star | 187 | 15.4315 | 1.2692 | 0.6043 | 1.3662 | 0.0091 | 0.2246 | ok | RAN |
| SOLUSDT | 8 | `ret133_pos_at_h` | one_head_filter_pi_star | 191 | 15.5742 | 1.3466 | 0.5916 | 1.7486 | 0.0057 | 0.2618 | ok | RAN |
| SOLUSDT | 4 | `ret133_pos_at_h` | one_head_filter_pi_star | 182 | 14.8404 | 1.2931 | 0.5934 | 1.4835 | 0.0049 | 0.2637 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret133_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret133_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret133_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret133_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret133_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret133_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `ret133_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret133_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret133_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret133_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret133_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret133_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret133_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret133_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret133_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret133_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
