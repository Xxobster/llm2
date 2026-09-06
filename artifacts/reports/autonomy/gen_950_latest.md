# Autonomy public-indicator hunt gen 950

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260826T070132Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma500_below_at_h` | one_head_filter_pi_star | 190 | 15.5213 | 2.0051 | 0.6947 | 4.3760 | 0.0237 | 0.3947 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma500_below_at_h` | one_head_filter_pi_star | 196 | 16.0114 | 1.8988 | 0.6888 | 4.2025 | 0.0219 | 0.3827 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma500_below_at_h` | one_head_filter_pi_star | 185 | 15.1276 | 2.0674 | 0.6811 | 4.1303 | 0.0154 | 0.3676 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma500_below_at_h` | one_head_filter_pi_star | 183 | 14.9641 | 2.0524 | 0.6776 | 4.0627 | 0.0153 | 0.3770 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `wma500_above_at_h` | one_head_filter_pi_star | 185 | 15.2068 | 1.2317 | 0.6000 | 1.1665 | 0.0080 | 0.2162 | ok | RAN |
| SOLUSDT | 4 | `wma500_above_at_h` | one_head_filter_pi_star | 188 | 15.3296 | 1.4108 | 0.6011 | 2.0210 | 0.0066 | 0.2660 | ok | RAN |
| ETHUSDT | 4 | `wma500_above_at_h` | one_head_filter_pi_star | 186 | 15.3490 | 1.1783 | 0.5968 | 0.9600 | 0.0064 | 0.2151 | ok | RAN |
| SOLUSDT | 8 | `wma500_above_at_h` | one_head_filter_pi_star | 188 | 15.3296 | 1.4018 | 0.6011 | 1.9980 | 0.0063 | 0.2606 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma500_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.7517 | 0.3333 | -0.4636 | -0.0208 | 0.0556 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma500_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma500_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma500_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma500_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma500_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma500_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma500_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma500_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma500_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma500_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma500_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma500_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma500_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma500_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma500_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
