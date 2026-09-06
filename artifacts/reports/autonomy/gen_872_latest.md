# Autonomy public-indicator hunt gen 872

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T223427Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 4 | `sma1780_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 3.3760 | 0.7000 | 1.9329 | 0.1424 | 0.4000 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma1780_above_at_h` | one_head_filter_pi_star | 52 | 4.3226 | 2.2760 | 0.7308 | 2.5744 | 0.0162 | 0.3462 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma1780_below_at_h` | one_head_filter_pi_star | 314 | 25.5445 | 1.6255 | 0.6497 | 3.6572 | 0.0162 | 0.3153 | GATE_CAND | RAN |
| ETHUSDT | 4 | `sma1780_below_at_h` | one_head_filter_pi_star | 304 | 24.8340 | 1.6457 | 0.6480 | 3.6523 | 0.0161 | 0.3158 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `sma1780_above_at_h` | one_head_filter_pi_star | 61 | 5.1975 | 1.3326 | 0.5902 | 0.8984 | 0.0124 | 0.2295 | ok | RAN |
| SOLUSDT | 8 | `sma1780_above_at_h` | one_head_filter_pi_star | 67 | 5.5695 | 1.8430 | 0.7015 | 2.0269 | 0.0121 | 0.3284 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma1780_below_at_h` | one_head_filter_pi_star | 301 | 24.4869 | 1.8634 | 0.6445 | 4.3504 | 0.0121 | 0.3156 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma1780_below_at_h` | one_head_filter_pi_star | 320 | 26.0326 | 1.7308 | 0.6344 | 4.0017 | 0.0111 | 0.3187 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `sma1780_above_at_h` | one_head_filter_pi_star | 60 | 4.9517 | 1.0609 | 0.5500 | 0.1936 | 0.0026 | 0.2167 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma1780_above_at_h` | one_head_filter_pi_star | 15 | 1.2765 | 0.4980 | 0.2667 | -1.0243 | -0.0556 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma1780_above_at_h` | one_head_filter_pi_star | 14 | 1.1914 | 0.3194 | 0.2143 | -1.5369 | -0.0867 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma1780_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma1780_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1780_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1780_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1780_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1780_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1780_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1780_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1780_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1780_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1780_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma1780_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1780_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
