# Autonomy public-indicator hunt gen 1414

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260830T071110Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma790_below_at_h` | one_head_filter_pi_star | 188 | 15.3579 | 2.1148 | 0.6915 | 4.6209 | 0.0248 | 0.3777 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma790_below_at_h` | one_head_filter_pi_star | 201 | 16.4199 | 1.9004 | 0.6667 | 4.1636 | 0.0218 | 0.3682 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `wma790_below_at_h` | one_head_filter_pi_star | 203 | 16.5995 | 1.8203 | 0.6601 | 3.5870 | 0.0124 | 0.3251 | GATE_CAND | RAN |
| SOLUSDT | 8 | `wma790_below_at_h` | one_head_filter_pi_star | 210 | 17.1719 | 1.7880 | 0.6571 | 3.5138 | 0.0123 | 0.3333 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `wma790_above_at_h` | one_head_filter_pi_star | 156 | 12.8230 | 1.2720 | 0.6090 | 1.2895 | 0.0095 | 0.2179 | ok | RAN |
| SOLUSDT | 8 | `wma790_above_at_h` | one_head_filter_pi_star | 164 | 13.4488 | 1.5937 | 0.6159 | 2.5434 | 0.0093 | 0.2988 | ok | RAN |
| SOLUSDT | 4 | `wma790_above_at_h` | one_head_filter_pi_star | 168 | 13.6988 | 1.5493 | 0.6071 | 2.3681 | 0.0084 | 0.3036 | ok | RAN |
| ETHUSDT | 4 | `wma790_above_at_h` | one_head_filter_pi_star | 147 | 12.1306 | 1.2190 | 0.5918 | 1.0244 | 0.0077 | 0.2177 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma790_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma790_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma790_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma790_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma790_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma790_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma790_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma790_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma790_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma790_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma790_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma790_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma790_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma790_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma790_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma790_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
