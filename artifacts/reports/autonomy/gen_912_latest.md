# Autonomy public-indicator hunt gen 912

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260826T024334Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 4 | `sma1880_below_at_h` | one_head_filter_pi_star | 10 | 1.4001 | 2.9360 | 0.7000 | 1.7370 | 0.1213 | 0.3000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma1880_below_at_h` | one_head_filter_pi_star | 325 | 26.5495 | 1.5913 | 0.6431 | 3.5778 | 0.0159 | 0.3138 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma1880_above_at_h` | one_head_filter_pi_star | 63 | 5.2370 | 2.2684 | 0.7143 | 2.6175 | 0.0158 | 0.3016 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma1880_above_at_h` | one_head_filter_pi_star | 57 | 4.7382 | 2.1307 | 0.7018 | 2.4774 | 0.0156 | 0.3158 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `sma1880_below_at_h` | one_head_filter_pi_star | 311 | 25.4059 | 1.5761 | 0.6431 | 3.3941 | 0.0152 | 0.3183 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma1880_below_at_h` | one_head_filter_pi_star | 297 | 24.1615 | 1.7953 | 0.6397 | 4.1984 | 0.0118 | 0.3131 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma1880_below_at_h` | one_head_filter_pi_star | 301 | 24.4869 | 1.7379 | 0.6379 | 3.9992 | 0.0113 | 0.3123 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `sma1880_above_at_h` | one_head_filter_pi_star | 49 | 4.3091 | 1.0747 | 0.5714 | 0.2215 | 0.0033 | 0.2449 | ok | RAN |
| ETHUSDT | 8 | `sma1880_above_at_h` | one_head_filter_pi_star | 52 | 4.7039 | 1.0409 | 0.5385 | 0.1372 | 0.0018 | 0.2500 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma1880_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.3172 | 0.1875 | -1.5524 | -0.0750 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma1880_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma1880_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1880_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1880_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1880_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1880_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1880_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1880_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1880_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1880_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1880_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1880_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma1880_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1880_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
