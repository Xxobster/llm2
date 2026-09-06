# Autonomy public-indicator hunt gen 1443

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260830T201046Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma665_below_at_h` | one_head_filter_pi_star | 190 | 15.5213 | 2.1484 | 0.7000 | 4.6529 | 0.0258 | 0.3947 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma665_below_at_h` | one_head_filter_pi_star | 184 | 15.0311 | 1.9522 | 0.6685 | 4.0317 | 0.0217 | 0.3804 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma665_below_at_h` | one_head_filter_pi_star | 203 | 16.5144 | 1.8167 | 0.6650 | 3.4835 | 0.0122 | 0.3251 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma665_below_at_h` | one_head_filter_pi_star | 203 | 16.5995 | 1.7463 | 0.6552 | 3.3792 | 0.0117 | 0.3300 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma665_above_at_h` | one_head_filter_pi_star | 148 | 12.1367 | 1.5417 | 0.6149 | 2.2436 | 0.0089 | 0.3176 | ok | RAN |
| SOLUSDT | 4 | `sma665_above_at_h` | one_head_filter_pi_star | 114 | 9.3486 | 1.5223 | 0.6053 | 1.9411 | 0.0081 | 0.3333 | ok | RAN |
| ETHUSDT | 8 | `sma665_above_at_h` | one_head_filter_pi_star | 170 | 13.9738 | 1.2159 | 0.6059 | 1.0784 | 0.0079 | 0.2353 | ok | RAN |
| ETHUSDT | 4 | `sma665_above_at_h` | one_head_filter_pi_star | 162 | 13.3162 | 1.0810 | 0.5741 | 0.4296 | 0.0031 | 0.2099 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma665_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5795 | 0.3000 | -0.8976 | -0.0424 | 0.0500 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma665_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5765 | 0.2778 | -0.8994 | -0.0449 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma665_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma665_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma665_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma665_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma665_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma665_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma665_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma665_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma665_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma665_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma665_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma665_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma665_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma665_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
