# Autonomy public-indicator hunt gen 1374

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260830T031444Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma765_below_at_h` | one_head_filter_pi_star | 190 | 15.5213 | 2.0577 | 0.6947 | 4.4489 | 0.0239 | 0.3789 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma765_below_at_h` | one_head_filter_pi_star | 202 | 16.5016 | 2.0587 | 0.6832 | 4.6846 | 0.0237 | 0.3663 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `wma765_below_at_h` | one_head_filter_pi_star | 192 | 15.7000 | 1.9288 | 0.6823 | 3.8733 | 0.0134 | 0.3333 | GATE_CAND | RAN |
| SOLUSDT | 8 | `wma765_below_at_h` | one_head_filter_pi_star | 203 | 16.5995 | 1.8196 | 0.6700 | 3.5623 | 0.0123 | 0.3251 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `wma765_above_at_h` | one_head_filter_pi_star | 176 | 14.3511 | 1.5771 | 0.6080 | 2.5603 | 0.0093 | 0.3011 | ok | RAN |
| SOLUSDT | 8 | `wma765_above_at_h` | one_head_filter_pi_star | 167 | 13.6172 | 1.5363 | 0.6108 | 2.3360 | 0.0083 | 0.2874 | ok | RAN |
| ETHUSDT | 8 | `wma765_above_at_h` | one_head_filter_pi_star | 163 | 13.3984 | 1.2278 | 0.5951 | 1.1281 | 0.0076 | 0.2025 | ok | RAN |
| ETHUSDT | 4 | `wma765_above_at_h` | one_head_filter_pi_star | 155 | 12.7908 | 1.1863 | 0.5935 | 0.9231 | 0.0066 | 0.2129 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma765_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma765_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma765_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma765_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma765_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma765_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma765_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma765_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma765_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma765_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma765_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma765_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma765_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma765_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma765_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma765_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
