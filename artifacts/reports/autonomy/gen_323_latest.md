# Autonomy public-indicator hunt gen 323

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T105252Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma112_below_at_h` | one_head_filter_pi_star | 198 | 16.1748 | 1.9760 | 0.6919 | 4.5080 | 0.0233 | 0.3737 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma112_below_at_h` | one_head_filter_pi_star | 198 | 16.1748 | 1.9752 | 0.6869 | 4.4698 | 0.0231 | 0.3636 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma112_below_at_h` | one_head_filter_pi_star | 178 | 14.5552 | 2.3120 | 0.6966 | 4.5464 | 0.0186 | 0.3820 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma112_below_at_h` | one_head_filter_pi_star | 173 | 14.1464 | 2.2635 | 0.6994 | 4.3686 | 0.0181 | 0.3873 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma112_cross_up` | one_head_filter_pi_star | 18 | 1.5292 | 2.4949 | 0.7222 | 1.5032 | 0.0170 | 0.1667 | TPM<MIN | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `sma112_above_at_h` | one_head_filter_pi_star | 182 | 14.9602 | 1.2814 | 0.6099 | 1.3706 | 0.0090 | 0.2143 | ok | RAN |
| ETHUSDT | 8 | `sma112_above_at_h` | one_head_filter_pi_star | 179 | 14.7713 | 1.2366 | 0.6034 | 1.1744 | 0.0077 | 0.2067 | ok | RAN |
| SOLUSDT | 4 | `sma112_above_at_h` | one_head_filter_pi_star | 205 | 16.7158 | 1.3111 | 0.5951 | 1.6397 | 0.0047 | 0.2634 | ok | RAN |
| SOLUSDT | 8 | `sma112_above_at_h` | one_head_filter_pi_star | 199 | 16.2265 | 1.2756 | 0.5879 | 1.4790 | 0.0043 | 0.2663 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma112_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma112_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma112_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma112_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma112_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma112_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma112_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma112_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma112_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma112_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma112_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma112_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma112_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma112_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma112_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
