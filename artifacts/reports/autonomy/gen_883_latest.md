# Autonomy public-indicator hunt gen 883

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T234413Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma576_below_at_h` | one_head_filter_pi_star | 179 | 14.6227 | 2.0215 | 0.6927 | 4.2748 | 0.0241 | 0.4078 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma576_below_at_h` | one_head_filter_pi_star | 192 | 15.6846 | 2.0440 | 0.6875 | 4.4510 | 0.0234 | 0.3802 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma576_below_at_h` | one_head_filter_pi_star | 198 | 16.1906 | 1.9536 | 0.6869 | 3.9760 | 0.0140 | 0.3333 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma576_below_at_h` | one_head_filter_pi_star | 200 | 16.3542 | 1.7527 | 0.6600 | 3.4132 | 0.0113 | 0.3400 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `sma576_above_at_h` | one_head_filter_pi_star | 151 | 12.4607 | 1.2815 | 0.6026 | 1.3024 | 0.0099 | 0.2318 | ok | RAN |
| SOLUSDT | 4 | `sma576_above_at_h` | one_head_filter_pi_star | 146 | 11.9727 | 1.5503 | 0.6164 | 2.1864 | 0.0085 | 0.2945 | ok | RAN |
| ETHUSDT | 4 | `sma576_above_at_h` | one_head_filter_pi_star | 155 | 12.7908 | 1.2128 | 0.5935 | 1.0411 | 0.0078 | 0.2194 | ok | RAN |
| SOLUSDT | 8 | `sma576_above_at_h` | one_head_filter_pi_star | 156 | 12.7928 | 1.4108 | 0.5833 | 1.8369 | 0.0066 | 0.2885 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma576_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma576_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma576_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma576_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma576_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma576_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma576_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma576_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma576_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma576_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma576_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma576_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma576_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma576_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma576_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma576_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
