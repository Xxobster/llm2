# Autonomy public-indicator hunt gen 1318

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T220246Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma730_below_at_h` | one_head_filter_pi_star | 186 | 15.1945 | 2.1203 | 0.6935 | 4.5830 | 0.0242 | 0.3817 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma730_below_at_h` | one_head_filter_pi_star | 197 | 16.0931 | 1.9610 | 0.6751 | 4.2853 | 0.0222 | 0.3706 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `wma730_below_at_h` | one_head_filter_pi_star | 187 | 15.2912 | 1.8741 | 0.6791 | 3.6067 | 0.0127 | 0.3476 | GATE_CAND | RAN |
| SOLUSDT | 4 | `wma730_below_at_h` | one_head_filter_pi_star | 200 | 16.3542 | 1.8089 | 0.6650 | 3.5805 | 0.0122 | 0.3350 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `wma730_above_at_h` | one_head_filter_pi_star | 163 | 13.2911 | 1.6364 | 0.6196 | 2.6297 | 0.0096 | 0.2883 | ok | RAN |
| SOLUSDT | 4 | `wma730_above_at_h` | one_head_filter_pi_star | 156 | 12.7928 | 1.5933 | 0.6218 | 2.4608 | 0.0094 | 0.3077 | ok | RAN |
| ETHUSDT | 8 | `wma730_above_at_h` | one_head_filter_pi_star | 177 | 14.5492 | 1.2244 | 0.5932 | 1.1232 | 0.0079 | 0.1977 | ok | RAN |
| ETHUSDT | 4 | `wma730_above_at_h` | one_head_filter_pi_star | 181 | 14.9364 | 1.1727 | 0.5912 | 0.8946 | 0.0063 | 0.2210 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma730_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma730_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma730_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma730_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma730_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma730_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma730_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma730_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma730_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma730_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma730_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma730_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma730_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma730_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma730_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma730_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
