# Autonomy public-indicator hunt gen 971

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260826T205848Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma648_below_at_h` | one_head_filter_pi_star | 182 | 14.8677 | 2.0101 | 0.6868 | 4.1792 | 0.0235 | 0.3956 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma648_below_at_h` | one_head_filter_pi_star | 183 | 14.9494 | 1.9583 | 0.6776 | 4.0828 | 0.0224 | 0.3934 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma648_below_at_h` | one_head_filter_pi_star | 202 | 16.5177 | 1.8713 | 0.6683 | 3.7897 | 0.0129 | 0.3317 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma648_below_at_h` | one_head_filter_pi_star | 210 | 17.1719 | 1.8107 | 0.6714 | 3.5602 | 0.0124 | 0.3238 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `sma648_above_at_h` | one_head_filter_pi_star | 143 | 11.7267 | 1.6227 | 0.6154 | 2.4186 | 0.0094 | 0.3217 | ok | RAN |
| SOLUSDT | 8 | `sma648_above_at_h` | one_head_filter_pi_star | 147 | 12.0547 | 1.5727 | 0.6190 | 2.3305 | 0.0091 | 0.3197 | ok | RAN |
| ETHUSDT | 8 | `sma648_above_at_h` | one_head_filter_pi_star | 162 | 13.3162 | 1.2233 | 0.6173 | 1.0970 | 0.0082 | 0.2222 | ok | RAN |
| ETHUSDT | 4 | `sma648_above_at_h` | one_head_filter_pi_star | 158 | 12.9874 | 1.2051 | 0.6013 | 0.9993 | 0.0074 | 0.2215 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma648_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5795 | 0.3000 | -0.8976 | -0.0424 | 0.0500 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma648_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma648_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma648_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma648_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma648_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma648_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma648_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma648_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma648_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma648_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma648_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma648_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma648_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma648_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma648_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
