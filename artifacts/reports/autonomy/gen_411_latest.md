# Autonomy public-indicator hunt gen 411

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T044618Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma184_below_at_h` | one_head_filter_pi_star | 184 | 15.0311 | 1.9799 | 0.6957 | 4.3984 | 0.0234 | 0.3859 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma184_below_at_h` | one_head_filter_pi_star | 190 | 15.5213 | 1.8966 | 0.6895 | 4.0834 | 0.0215 | 0.3737 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma184_below_at_h` | one_head_filter_pi_star | 169 | 13.8193 | 2.2645 | 0.6982 | 4.3086 | 0.0176 | 0.3846 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma184_below_at_h` | one_head_filter_pi_star | 180 | 14.7188 | 2.2186 | 0.6944 | 4.3274 | 0.0173 | 0.3778 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `sma184_above_at_h` | one_head_filter_pi_star | 190 | 15.6791 | 1.2596 | 0.6000 | 1.3007 | 0.0087 | 0.2211 | ok | RAN |
| ETHUSDT | 8 | `sma184_above_at_h` | one_head_filter_pi_star | 195 | 16.0287 | 1.2168 | 0.6000 | 1.1212 | 0.0074 | 0.2256 | ok | RAN |
| SOLUSDT | 4 | `sma184_above_at_h` | one_head_filter_pi_star | 207 | 16.8789 | 1.3925 | 0.5990 | 2.0216 | 0.0061 | 0.2609 | ok | RAN |
| SOLUSDT | 8 | `sma184_above_at_h` | one_head_filter_pi_star | 202 | 16.4712 | 1.3307 | 0.5891 | 1.7287 | 0.0052 | 0.2673 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma184_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma184_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma184_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma184_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma184_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma184_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma184_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma184_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma184_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma184_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma184_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma184_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma184_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma184_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma184_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma184_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
