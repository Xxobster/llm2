# Autonomy public-indicator hunt gen 131

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T180507Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma100_below_at_h` | one_head_filter_pi_star | 199 | 16.2565 | 1.8804 | 0.6834 | 4.1495 | 0.0217 | 0.3719 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma100_below_at_h` | one_head_filter_pi_star | 208 | 16.9917 | 1.7778 | 0.6731 | 3.9001 | 0.0203 | 0.3558 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma100_cross_up` | one_head_filter_pi_star | 12 | 1.1180 | 2.6199 | 0.6667 | 1.4393 | 0.0199 | 0.2500 | TPM<MIN | RAN |
| SOLUSDT | 8 | `sma100_below_at_h` | one_head_filter_pi_star | 171 | 13.9828 | 2.2863 | 0.6959 | 4.4080 | 0.0186 | 0.3977 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma100_below_at_h` | one_head_filter_pi_star | 168 | 13.7375 | 2.2563 | 0.6964 | 4.3048 | 0.0182 | 0.3988 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `sma100_above_at_h` | one_head_filter_pi_star | 180 | 14.7958 | 1.3323 | 0.6111 | 1.5692 | 0.0103 | 0.2333 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `sma100_above_at_h` | one_head_filter_pi_star | 183 | 15.0424 | 1.2905 | 0.6120 | 1.3898 | 0.0094 | 0.2131 | ok | RAN |
| SOLUSDT | 8 | `sma100_above_at_h` | one_head_filter_pi_star | 212 | 17.2866 | 1.3188 | 0.5943 | 1.6940 | 0.0048 | 0.2547 | ok | RAN |
| SOLUSDT | 4 | `sma100_above_at_h` | one_head_filter_pi_star | 199 | 16.2265 | 1.2779 | 0.5930 | 1.4881 | 0.0043 | 0.2613 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma100_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma100_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma100_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma100_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma100_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma100_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma100_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma100_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma100_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma100_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma100_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma100_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma100_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma100_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma100_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
