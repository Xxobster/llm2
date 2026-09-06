# Autonomy public-indicator hunt gen 542

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T204351Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma245_below_at_h` | one_head_filter_pi_star | 183 | 14.9494 | 2.1254 | 0.7104 | 4.7863 | 0.0252 | 0.3880 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma245_below_at_h` | one_head_filter_pi_star | 180 | 14.7044 | 1.9618 | 0.6944 | 4.2778 | 0.0220 | 0.3778 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma245_below_at_h` | one_head_filter_pi_star | 163 | 13.3287 | 2.2789 | 0.6994 | 4.2881 | 0.0178 | 0.3988 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma245_below_at_h` | one_head_filter_pi_star | 176 | 14.3917 | 2.2069 | 0.6932 | 4.2763 | 0.0174 | 0.3807 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `wma245_above_at_h` | one_head_filter_pi_star | 190 | 15.6791 | 1.2388 | 0.5947 | 1.2126 | 0.0082 | 0.2211 | ok | RAN |
| ETHUSDT | 4 | `wma245_above_at_h` | one_head_filter_pi_star | 191 | 15.7616 | 1.2140 | 0.6021 | 1.1077 | 0.0075 | 0.2356 | ok | RAN |
| SOLUSDT | 8 | `wma245_above_at_h` | one_head_filter_pi_star | 208 | 16.9604 | 1.3352 | 0.5913 | 1.7743 | 0.0052 | 0.2644 | ok | RAN |
| SOLUSDT | 4 | `wma245_above_at_h` | one_head_filter_pi_star | 201 | 16.3896 | 1.3153 | 0.5871 | 1.6317 | 0.0049 | 0.2587 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma245_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma245_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma245_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma245_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma245_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma245_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma245_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma245_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma245_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma245_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma245_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma245_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma245_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma245_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma245_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma245_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
