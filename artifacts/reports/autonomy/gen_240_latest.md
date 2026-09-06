# Autonomy public-indicator hunt gen 240

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T011609Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma180_below_at_h` | one_head_filter_pi_star | 183 | 14.9494 | 2.0684 | 0.7049 | 4.6515 | 0.0247 | 0.3825 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma180_below_at_h` | one_head_filter_pi_star | 192 | 15.6846 | 1.7813 | 0.6771 | 3.7841 | 0.0198 | 0.3646 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma180_below_at_h` | one_head_filter_pi_star | 174 | 14.2281 | 2.2341 | 0.6954 | 4.3414 | 0.0174 | 0.3793 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma180_below_at_h` | one_head_filter_pi_star | 170 | 13.9010 | 2.2225 | 0.6941 | 4.2039 | 0.0172 | 0.3824 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `sma180_above_at_h` | one_head_filter_pi_star | 198 | 16.3392 | 1.3681 | 0.6162 | 1.8025 | 0.0117 | 0.2323 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `sma180_above_at_h` | one_head_filter_pi_star | 189 | 15.5965 | 1.2474 | 0.5979 | 1.2361 | 0.0084 | 0.2222 | ok | RAN |
| SOLUSDT | 4 | `sma180_above_at_h` | one_head_filter_pi_star | 203 | 16.5527 | 1.3814 | 0.6010 | 1.9520 | 0.0059 | 0.2611 | ok | RAN |
| SOLUSDT | 8 | `sma180_above_at_h` | one_head_filter_pi_star | 196 | 15.9819 | 1.2907 | 0.5867 | 1.5442 | 0.0047 | 0.2551 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma180_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma180_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma180_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma180_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma180_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma180_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma180_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma180_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma180_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma180_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma180_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma180_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma180_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma180_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma180_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma180_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
