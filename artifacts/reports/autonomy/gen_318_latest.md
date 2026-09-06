# Autonomy public-indicator hunt gen 318

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T064703Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `wma105_cross_up` | one_head_filter_pi_star | 22 | 1.8331 | 3.9408 | 0.6364 | 2.3323 | 0.0296 | 0.1818 | TPM<MIN | RAN |
| ETHUSDT | 8 | `wma105_below_at_h` | one_head_filter_pi_star | 201 | 16.4199 | 1.8310 | 0.6816 | 3.9852 | 0.0212 | 0.3682 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma105_below_at_h` | one_head_filter_pi_star | 201 | 16.4199 | 1.8012 | 0.6816 | 3.8791 | 0.0210 | 0.3632 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma105_below_at_h` | one_head_filter_pi_star | 168 | 13.7375 | 2.3057 | 0.6964 | 4.4012 | 0.0192 | 0.4107 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma105_below_at_h` | one_head_filter_pi_star | 162 | 13.2469 | 2.2255 | 0.6975 | 4.1234 | 0.0183 | 0.4198 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `wma105_cross_down` | one_head_filter_pi_star | 30 | 2.7877 | 1.7782 | 0.6667 | 1.3166 | 0.0116 | 0.1000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma105_above_at_h` | one_head_filter_pi_star | 181 | 14.8780 | 1.3727 | 0.6133 | 1.7301 | 0.0111 | 0.2320 | ok | RAN |
| ETHUSDT | 8 | `wma105_above_at_h` | one_head_filter_pi_star | 180 | 14.7958 | 1.3455 | 0.6111 | 1.5801 | 0.0105 | 0.2278 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `wma105_cross_down` | one_head_filter_pi_star | 32 | 2.6517 | 1.1941 | 0.5312 | 0.4440 | 0.0069 | 0.2812 | TPM<MIN | RAN |
| SOLUSDT | 8 | `wma105_above_at_h` | one_head_filter_pi_star | 216 | 17.6127 | 1.3675 | 0.6019 | 1.9372 | 0.0054 | 0.2500 | ok | RAN |
| SOLUSDT | 4 | `wma105_above_at_h` | one_head_filter_pi_star | 212 | 17.2866 | 1.3237 | 0.5943 | 1.7286 | 0.0048 | 0.2500 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `wma105_cross_up` | one_head_filter_pi_star | 23 | 1.9959 | 0.9138 | 0.5217 | -0.1811 | -0.0033 | 0.2609 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma105_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma105_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma105_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma105_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma105_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma105_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma105_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma105_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma105_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma105_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma105_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma105_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
