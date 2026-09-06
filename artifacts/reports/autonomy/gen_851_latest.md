# Autonomy public-indicator hunt gen 851

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T203228Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma552_below_at_h` | one_head_filter_pi_star | 183 | 14.9494 | 2.1406 | 0.6940 | 4.6598 | 0.0259 | 0.3934 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma552_below_at_h` | one_head_filter_pi_star | 177 | 14.4593 | 2.0628 | 0.6949 | 4.3918 | 0.0241 | 0.4068 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma552_below_at_h` | one_head_filter_pi_star | 199 | 16.2724 | 1.8735 | 0.6683 | 3.6953 | 0.0130 | 0.3266 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma552_below_at_h` | one_head_filter_pi_star | 198 | 16.1906 | 1.8127 | 0.6667 | 3.5983 | 0.0125 | 0.3434 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma552_above_at_h` | one_head_filter_pi_star | 177 | 14.5149 | 1.6719 | 0.6328 | 2.9072 | 0.0102 | 0.2938 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma552_above_at_h` | one_head_filter_pi_star | 175 | 14.2696 | 1.6561 | 0.6229 | 2.7792 | 0.0095 | 0.2800 | ok | RAN |
| ETHUSDT | 8 | `sma552_above_at_h` | one_head_filter_pi_star | 159 | 13.1209 | 1.1940 | 0.5975 | 0.9662 | 0.0071 | 0.2264 | ok | RAN |
| ETHUSDT | 4 | `sma552_above_at_h` | one_head_filter_pi_star | 164 | 13.5335 | 1.1399 | 0.5915 | 0.6975 | 0.0052 | 0.2317 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma552_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma552_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma552_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma552_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma552_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma552_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma552_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma552_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma552_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma552_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma552_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma552_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma552_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma552_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma552_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma552_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
