# Autonomy public-indicator hunt gen 691

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T063222Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma418_below_at_h` | one_head_filter_pi_star | 186 | 15.1945 | 2.0411 | 0.6989 | 4.6045 | 0.0244 | 0.3978 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma418_below_at_h` | one_head_filter_pi_star | 192 | 15.6846 | 1.9550 | 0.6979 | 4.3038 | 0.0223 | 0.3750 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma418_below_at_h` | one_head_filter_pi_star | 187 | 15.2912 | 1.9583 | 0.6738 | 3.8695 | 0.0138 | 0.3583 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma418_below_at_h` | one_head_filter_pi_star | 194 | 15.8635 | 1.8857 | 0.6546 | 3.6247 | 0.0131 | 0.3660 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma418_above_at_h` | one_head_filter_pi_star | 180 | 14.7958 | 1.2944 | 0.5944 | 1.4634 | 0.0101 | 0.2222 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma418_above_at_h` | one_head_filter_pi_star | 179 | 14.5957 | 1.5729 | 0.6089 | 2.5844 | 0.0090 | 0.2682 | ok | RAN |
| ETHUSDT | 8 | `sma418_above_at_h` | one_head_filter_pi_star | 185 | 15.2068 | 1.2540 | 0.6000 | 1.2886 | 0.0089 | 0.2108 | ok | RAN |
| SOLUSDT | 4 | `sma418_above_at_h` | one_head_filter_pi_star | 195 | 15.9004 | 1.4438 | 0.6000 | 2.1927 | 0.0073 | 0.2615 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma418_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5795 | 0.3000 | -0.8976 | -0.0432 | 0.0500 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma418_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma418_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma418_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma418_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma418_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma418_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma418_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma418_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma418_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma418_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma418_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma418_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma418_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma418_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma418_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
