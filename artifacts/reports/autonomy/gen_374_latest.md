# Autonomy public-indicator hunt gen 374

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T201853Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma140_below_at_h` | one_head_filter_pi_star | 197 | 16.0931 | 2.0470 | 0.6954 | 4.6446 | 0.0242 | 0.3655 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma140_below_at_h` | one_head_filter_pi_star | 204 | 16.6649 | 1.7764 | 0.6765 | 3.7776 | 0.0201 | 0.3676 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma140_below_at_h` | one_head_filter_pi_star | 169 | 13.8193 | 2.3162 | 0.6982 | 4.4536 | 0.0190 | 0.4024 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma140_below_at_h` | one_head_filter_pi_star | 171 | 13.9828 | 2.2934 | 0.6959 | 4.4109 | 0.0186 | 0.3977 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `wma140_above_at_h` | one_head_filter_pi_star | 176 | 14.5238 | 1.3123 | 0.6136 | 1.4242 | 0.0097 | 0.2273 | ok | RAN |
| ETHUSDT | 4 | `wma140_above_at_h` | one_head_filter_pi_star | 182 | 14.9602 | 1.2990 | 0.6099 | 1.4339 | 0.0094 | 0.2253 | ok | RAN |
| SOLUSDT | 8 | `wma140_above_at_h` | one_head_filter_pi_star | 209 | 17.0419 | 1.3036 | 0.5885 | 1.6219 | 0.0046 | 0.2536 | ok | RAN |
| SOLUSDT | 4 | `wma140_above_at_h` | one_head_filter_pi_star | 203 | 16.5527 | 1.2770 | 0.5862 | 1.4966 | 0.0043 | 0.2562 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma140_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma140_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma140_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma140_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma140_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 8 | `wma140_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `wma140_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma140_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma140_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma140_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma140_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma140_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma140_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma140_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma140_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma140_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
