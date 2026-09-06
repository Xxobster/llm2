# Autonomy public-indicator hunt gen 936

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260826T052520Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma1940_below_at_h` | one_head_filter_pi_star | 324 | 26.3580 | 1.6045 | 0.6420 | 3.6591 | 0.0160 | 0.3056 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma1940_above_at_h` | one_head_filter_pi_star | 61 | 5.0708 | 2.0215 | 0.7213 | 2.3923 | 0.0139 | 0.2787 | GATE_CAND | RAN |
| ETHUSDT | 4 | `sma1940_below_at_h` | one_head_filter_pi_star | 312 | 25.4875 | 1.5186 | 0.6378 | 3.0729 | 0.0138 | 0.3109 | ok | RAN |
| SOLUSDT | 8 | `sma1940_below_at_h` | one_head_filter_pi_star | 288 | 23.4294 | 1.8974 | 0.6528 | 4.5143 | 0.0131 | 0.3125 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma1940_below_at_h` | one_head_filter_pi_star | 282 | 22.9413 | 1.8192 | 0.6418 | 4.2254 | 0.0122 | 0.3156 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma1940_above_at_h` | one_head_filter_pi_star | 66 | 5.4864 | 1.6431 | 0.6818 | 1.6206 | 0.0102 | 0.3182 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `sma1940_above_at_h` | one_head_filter_pi_star | 44 | 3.9802 | 1.2091 | 0.5682 | 0.5562 | 0.0081 | 0.2727 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma1940_above_at_h` | one_head_filter_pi_star | 43 | 3.8897 | 0.9295 | 0.5349 | -0.2083 | -0.0030 | 0.2093 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma1940_above_at_h` | one_head_filter_pi_star | 14 | 1.1914 | 0.3194 | 0.2143 | -1.5369 | -0.0846 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma1940_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma1940_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1940_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1940_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1940_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1940_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1940_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1940_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1940_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1940_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma1940_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1940_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1940_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma1940_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1940_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
