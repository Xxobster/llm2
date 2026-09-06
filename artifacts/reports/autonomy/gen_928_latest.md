# Autonomy public-indicator hunt gen 928

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260826T043147Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `sma1920_below_at_h` | one_head_filter_pi_star | 333 | 27.0902 | 1.5556 | 0.6396 | 3.4317 | 0.0152 | 0.3033 | GATE_CAND | RAN |
| ETHUSDT | 4 | `sma1920_below_at_h` | one_head_filter_pi_star | 326 | 26.5207 | 1.5672 | 0.6380 | 3.4303 | 0.0150 | 0.3098 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma1920_below_at_h` | one_head_filter_pi_star | 309 | 25.1378 | 1.8709 | 0.6472 | 4.4836 | 0.0128 | 0.3301 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma1920_above_at_h` | one_head_filter_pi_star | 62 | 5.1539 | 1.8466 | 0.6452 | 2.1154 | 0.0125 | 0.2903 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma1920_below_at_h` | one_head_filter_pi_star | 300 | 24.4056 | 1.7526 | 0.6333 | 3.9549 | 0.0113 | 0.3200 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma1920_above_at_h` | one_head_filter_pi_star | 57 | 4.7382 | 1.6912 | 0.6667 | 1.6919 | 0.0107 | 0.3158 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `sma1920_above_at_h` | one_head_filter_pi_star | 47 | 4.2516 | 1.1766 | 0.5745 | 0.4848 | 0.0072 | 0.2553 | ok | RAN |
| ETHUSDT | 4 | `sma1920_above_at_h` | one_head_filter_pi_star | 53 | 4.6410 | 1.0496 | 0.5472 | 0.1500 | 0.0020 | 0.2075 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma1920_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.4722 | 0.2500 | -1.1303 | -0.0579 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma1920_above_at_h` | one_head_filter_pi_star | 14 | 1.1914 | 0.4988 | 0.2857 | -1.0212 | -0.0608 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma1920_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma1920_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1920_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1920_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1920_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1920_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1920_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1920_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1920_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma1920_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1920_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1920_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma1920_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1920_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
