# Autonomy public-indicator hunt gen 945

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260826T062437Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 4 | `ema1920_below_at_h` | one_head_filter_pi_star | 10 | 1.4001 | 2.9360 | 0.7000 | 1.7370 | 0.1112 | 0.3000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1920_below_at_h` | one_head_filter_pi_star | 10 | 1.4001 | 2.9360 | 0.7000 | 1.7370 | 0.1067 | 0.3000 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema1920_below_at_h` | one_head_filter_pi_star | 323 | 26.2767 | 1.6219 | 0.6440 | 3.5842 | 0.0162 | 0.3096 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `ema1920_below_at_h` | one_head_filter_pi_star | 311 | 25.3005 | 1.5539 | 0.6399 | 3.3004 | 0.0148 | 0.3183 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema1920_above_at_h` | one_head_filter_pi_star | 61 | 5.2954 | 1.4012 | 0.5902 | 1.1957 | 0.0145 | 0.2623 | ok | RAN |
| SOLUSDT | 4 | `ema1920_below_at_h` | one_head_filter_pi_star | 275 | 22.3718 | 1.8812 | 0.6509 | 4.4106 | 0.0136 | 0.3236 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema1920_below_at_h` | one_head_filter_pi_star | 278 | 22.7323 | 1.8398 | 0.6511 | 4.2119 | 0.0128 | 0.3201 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema1920_above_at_h` | one_head_filter_pi_star | 115 | 9.3771 | 1.5767 | 0.6348 | 2.0428 | 0.0081 | 0.2522 | ok | RAN |
| SOLUSDT | 8 | `ema1920_above_at_h` | one_head_filter_pi_star | 117 | 9.5402 | 1.4448 | 0.6154 | 1.6686 | 0.0065 | 0.2564 | ok | RAN |
| ETHUSDT | 4 | `ema1920_above_at_h` | one_head_filter_pi_star | 52 | 4.5729 | 1.1027 | 0.5385 | 0.3045 | 0.0040 | 0.2500 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1920_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5935 | 0.2941 | -0.8400 | -0.0444 | 0.0588 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1920_above_at_h` | one_head_filter_pi_star | 14 | 1.1914 | 0.3194 | 0.2143 | -1.5369 | -0.0867 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1920_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1920_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1920_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1920_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1920_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1920_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1920_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1920_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1920_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1920_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1920_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1920_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
