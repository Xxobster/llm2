# Autonomy public-indicator hunt gen 880

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T232332Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `sma1800_above_at_h` | one_head_filter_pi_star | 52 | 4.3226 | 2.6152 | 0.7115 | 2.9855 | 0.0185 | 0.3077 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma1800_above_at_h` | one_head_filter_pi_star | 56 | 4.6551 | 2.7490 | 0.7500 | 3.1048 | 0.0178 | 0.3393 | GATE_CAND | RAN |
| ETHUSDT | 4 | `sma1800_below_at_h` | one_head_filter_pi_star | 311 | 25.4059 | 1.5901 | 0.6431 | 3.4952 | 0.0155 | 0.3151 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `sma1800_below_at_h` | one_head_filter_pi_star | 301 | 24.5889 | 1.5710 | 0.6412 | 3.3386 | 0.0148 | 0.3223 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma1800_below_at_h` | one_head_filter_pi_star | 301 | 24.4869 | 1.8102 | 0.6412 | 4.2970 | 0.0120 | 0.3123 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma1800_below_at_h` | one_head_filter_pi_star | 298 | 24.2429 | 1.7589 | 0.6376 | 4.0000 | 0.0114 | 0.3154 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `sma1800_above_at_h` | one_head_filter_pi_star | 57 | 5.0126 | 1.1521 | 0.5614 | 0.4725 | 0.0063 | 0.2456 | ok | RAN |
| ETHUSDT | 4 | `sma1800_above_at_h` | one_head_filter_pi_star | 54 | 4.6010 | 1.1171 | 0.5556 | 0.3513 | 0.0050 | 0.2222 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma1800_above_at_h` | one_head_filter_pi_star | 14 | 1.1914 | 0.4988 | 0.2857 | -1.0212 | -0.0543 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma1800_above_at_h` | one_head_filter_pi_star | 15 | 1.2765 | 0.4959 | 0.2667 | -1.0328 | -0.0573 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma1800_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma1800_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1800_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1800_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1800_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1800_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1800_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1800_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1800_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma1800_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1800_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1800_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma1800_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1800_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
