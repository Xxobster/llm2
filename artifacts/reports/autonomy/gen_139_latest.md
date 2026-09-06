# Autonomy public-indicator hunt gen 139

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T183615Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `sma60_cross_up` | one_head_filter_pi_star | 23 | 1.9120 | 5.5729 | 0.6957 | 2.7256 | 0.0391 | 0.2609 | TPM<MIN | RAN |
| ETHUSDT | 8 | `sma60_below_at_h` | one_head_filter_pi_star | 213 | 17.4002 | 1.7868 | 0.6761 | 3.7574 | 0.0209 | 0.3756 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma60_below_at_h` | one_head_filter_pi_star | 208 | 16.9917 | 1.7360 | 0.6731 | 3.6397 | 0.0198 | 0.3702 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma60_below_at_h` | one_head_filter_pi_star | 162 | 13.2469 | 2.1430 | 0.6852 | 4.0258 | 0.0174 | 0.4074 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma60_below_at_h` | one_head_filter_pi_star | 158 | 12.9198 | 2.1333 | 0.6899 | 3.9087 | 0.0174 | 0.4177 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma60_cross_down` | one_head_filter_pi_star | 20 | 1.6573 | 1.5637 | 0.5500 | 0.7426 | 0.0158 | 0.2500 | TPM<MIN | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `sma60_above_at_h` | one_head_filter_pi_star | 161 | 13.2859 | 1.2986 | 0.6087 | 1.3325 | 0.0089 | 0.2174 | ok | RAN |
| ETHUSDT | 8 | `sma60_above_at_h` | one_head_filter_pi_star | 164 | 13.5335 | 1.2463 | 0.5976 | 1.1300 | 0.0074 | 0.2134 | ok | RAN |
| SOLUSDT | 4 | `sma60_above_at_h` | one_head_filter_pi_star | 215 | 17.5312 | 1.3318 | 0.5953 | 1.7762 | 0.0049 | 0.2512 | ok | RAN |
| SOLUSDT | 8 | `sma60_above_at_h` | one_head_filter_pi_star | 213 | 17.3681 | 1.3122 | 0.5915 | 1.7187 | 0.0047 | 0.2488 | ok | RAN |
| SOLUSDT | 8 | `sma60_cross_down` | one_head_filter_pi_star | 26 | 2.2191 | 1.1372 | 0.5769 | 0.2618 | 0.0028 | 0.1923 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `sma60_cross_up` | one_head_filter_pi_star | 13 | 1.3661 | 0.3886 | 0.3077 | -1.4923 | -0.0337 | 0.0769 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma60_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma60_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma60_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma60_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma60_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma60_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma60_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma60_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma60_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma60_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma60_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma60_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
