# Autonomy public-indicator hunt gen 1147

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T042829Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma619_below_at_h` | one_head_filter_pi_star | 192 | 15.6846 | 2.0452 | 0.6875 | 4.4363 | 0.0239 | 0.3854 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma619_below_at_h` | one_head_filter_pi_star | 201 | 16.4199 | 1.9099 | 0.6716 | 4.1046 | 0.0217 | 0.3682 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma619_below_at_h` | one_head_filter_pi_star | 192 | 15.7000 | 1.7700 | 0.6667 | 3.3942 | 0.0120 | 0.3281 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma619_below_at_h` | one_head_filter_pi_star | 186 | 15.2094 | 1.7752 | 0.6667 | 3.3083 | 0.0115 | 0.3441 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma619_above_at_h` | one_head_filter_pi_star | 146 | 11.9727 | 1.6462 | 0.6233 | 2.5292 | 0.0098 | 0.3219 | ok | RAN |
| SOLUSDT | 4 | `sma619_above_at_h` | one_head_filter_pi_star | 145 | 11.8907 | 1.5556 | 0.6138 | 2.2048 | 0.0088 | 0.3310 | ok | RAN |
| ETHUSDT | 4 | `sma619_above_at_h` | one_head_filter_pi_star | 183 | 15.0424 | 1.1259 | 0.5956 | 0.6624 | 0.0048 | 0.2131 | ok | RAN |
| ETHUSDT | 8 | `sma619_above_at_h` | one_head_filter_pi_star | 187 | 15.3712 | 1.1250 | 0.5989 | 0.6695 | 0.0047 | 0.2139 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma619_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5795 | 0.3000 | -0.8976 | -0.0424 | 0.0500 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma619_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma619_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma619_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma619_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma619_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma619_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma619_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma619_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma619_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma619_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma619_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma619_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma619_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma619_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma619_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
