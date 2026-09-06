# Autonomy public-indicator hunt gen 308

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T060420Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema155_below_at_h` | one_head_filter_pi_star | 193 | 15.7663 | 2.1320 | 0.7047 | 4.8908 | 0.0250 | 0.3731 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema155_below_at_h` | one_head_filter_pi_star | 192 | 15.6846 | 2.0221 | 0.6927 | 4.5160 | 0.0236 | 0.3750 | EBR>35% | RAN |
| SOLUSDT | 4 | `ema155_below_at_h` | one_head_filter_pi_star | 174 | 14.2281 | 2.3024 | 0.7011 | 4.4702 | 0.0183 | 0.3851 | EBR>35% | RAN |
| SOLUSDT | 8 | `ema155_below_at_h` | one_head_filter_pi_star | 171 | 13.9828 | 2.1194 | 0.6901 | 4.0281 | 0.0167 | 0.3860 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ema155_above_at_h` | one_head_filter_pi_star | 193 | 15.8644 | 1.1978 | 0.6010 | 1.0381 | 0.0069 | 0.2280 | ok | RAN |
| ETHUSDT | 8 | `ema155_above_at_h` | one_head_filter_pi_star | 190 | 15.6178 | 1.1582 | 0.5895 | 0.8121 | 0.0056 | 0.2263 | ok | RAN |
| SOLUSDT | 8 | `ema155_above_at_h` | one_head_filter_pi_star | 208 | 16.9604 | 1.3433 | 0.5913 | 1.7934 | 0.0053 | 0.2692 | ok | RAN |
| SOLUSDT | 4 | `ema155_above_at_h` | one_head_filter_pi_star | 200 | 16.3081 | 1.3196 | 0.5850 | 1.6812 | 0.0049 | 0.2700 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema155_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema155_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema155_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema155_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema155_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema155_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema155_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema155_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema155_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema155_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema155_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema155_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema155_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema155_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema155_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema155_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
