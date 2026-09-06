# Autonomy public-indicator hunt gen 1411

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260830T065427Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma661_below_at_h` | one_head_filter_pi_star | 187 | 15.2762 | 2.1147 | 0.6952 | 4.6033 | 0.0256 | 0.3797 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma661_below_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 2.1314 | 0.6878 | 4.7201 | 0.0252 | 0.3810 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma661_below_at_h` | one_head_filter_pi_star | 195 | 15.9453 | 1.8324 | 0.6667 | 3.5819 | 0.0126 | 0.3282 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma661_below_at_h` | one_head_filter_pi_star | 208 | 17.0083 | 1.8010 | 0.6683 | 3.5302 | 0.0122 | 0.3173 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma661_above_at_h` | one_head_filter_pi_star | 157 | 12.8748 | 1.5693 | 0.6242 | 2.3927 | 0.0091 | 0.3121 | ok | RAN |
| SOLUSDT | 4 | `sma661_above_at_h` | one_head_filter_pi_star | 146 | 11.9727 | 1.5698 | 0.6233 | 2.3248 | 0.0090 | 0.3288 | ok | RAN |
| ETHUSDT | 8 | `sma661_above_at_h` | one_head_filter_pi_star | 164 | 13.4806 | 1.2058 | 0.6098 | 1.0171 | 0.0074 | 0.2256 | ok | RAN |
| ETHUSDT | 4 | `sma661_above_at_h` | one_head_filter_pi_star | 148 | 12.1654 | 1.1099 | 0.5811 | 0.5356 | 0.0043 | 0.2162 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma661_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5795 | 0.3000 | -0.8976 | -0.0424 | 0.0500 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma661_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma661_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma661_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma661_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma661_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma661_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma661_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma661_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma661_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma661_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma661_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma661_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma661_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma661_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma661_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
