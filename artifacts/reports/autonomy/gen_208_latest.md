# Autonomy public-indicator hunt gen 208

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T230631Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma110_below_at_h` | one_head_filter_pi_star | 204 | 16.6649 | 1.9641 | 0.6863 | 4.4537 | 0.0229 | 0.3676 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma110_below_at_h` | one_head_filter_pi_star | 201 | 16.4199 | 1.8480 | 0.6766 | 4.0091 | 0.0211 | 0.3632 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma110_below_at_h` | one_head_filter_pi_star | 171 | 13.9828 | 2.2765 | 0.6959 | 4.3767 | 0.0184 | 0.3918 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma110_below_at_h` | one_head_filter_pi_star | 171 | 13.9828 | 2.2966 | 0.7018 | 4.4425 | 0.0184 | 0.3860 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `sma110_above_at_h` | one_head_filter_pi_star | 172 | 14.1937 | 1.3318 | 0.6105 | 1.5551 | 0.0100 | 0.2035 | ok | RAN |
| ETHUSDT | 4 | `sma110_above_at_h` | one_head_filter_pi_star | 187 | 15.3712 | 1.2024 | 0.6043 | 1.0400 | 0.0068 | 0.2193 | ok | RAN |
| SOLUSDT | 8 | `sma110_above_at_h` | one_head_filter_pi_star | 205 | 16.7158 | 1.2859 | 0.5854 | 1.5287 | 0.0045 | 0.2634 | ok | RAN |
| SOLUSDT | 4 | `sma110_above_at_h` | one_head_filter_pi_star | 202 | 16.4712 | 1.2867 | 0.5990 | 1.5411 | 0.0044 | 0.2673 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma110_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma110_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma110_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma110_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma110_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma110_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma110_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma110_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma110_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 8 | `sma110_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma110_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma110_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma110_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma110_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma110_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma110_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
