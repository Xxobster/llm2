# Autonomy public-indicator hunt gen 977

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260826T225524Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 4 | `ema2000_below_at_h` | one_head_filter_pi_star | 10 | 1.4001 | 2.9360 | 0.7000 | 1.7370 | 0.1067 | 0.3000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema2000_below_at_h` | one_head_filter_pi_star | 9 | 1.2601 | 2.4502 | 0.6667 | 1.3795 | 0.0799 | 0.2222 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema2000_above_at_h` | one_head_filter_pi_star | 58 | 5.1006 | 1.4885 | 0.6034 | 1.2990 | 0.0180 | 0.2586 | ok | RAN |
| ETHUSDT | 4 | `ema2000_below_at_h` | one_head_filter_pi_star | 327 | 26.6021 | 1.5922 | 0.6422 | 3.5032 | 0.0157 | 0.3089 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema2000_below_at_h` | one_head_filter_pi_star | 324 | 26.3580 | 1.5911 | 0.6420 | 3.4892 | 0.0156 | 0.3056 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ema2000_below_at_h` | one_head_filter_pi_star | 259 | 21.1787 | 1.8397 | 0.6486 | 4.0427 | 0.0132 | 0.3398 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema2000_below_at_h` | one_head_filter_pi_star | 267 | 21.8328 | 1.8265 | 0.6517 | 4.0889 | 0.0128 | 0.3296 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema2000_above_at_h` | one_head_filter_pi_star | 104 | 8.4802 | 1.6311 | 0.6346 | 2.0969 | 0.0092 | 0.2596 | ok | RAN |
| SOLUSDT | 4 | `ema2000_above_at_h` | one_head_filter_pi_star | 94 | 7.7273 | 1.5816 | 0.6489 | 1.7901 | 0.0083 | 0.2766 | ok | RAN |
| ETHUSDT | 4 | `ema2000_above_at_h` | one_head_filter_pi_star | 46 | 4.0453 | 1.2062 | 0.5652 | 0.5244 | 0.0081 | 0.2826 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema2000_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5935 | 0.2941 | -0.8400 | -0.0463 | 0.0588 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema2000_above_at_h` | one_head_filter_pi_star | 13 | 1.1063 | 0.3426 | 0.2308 | -1.3975 | -0.0863 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema2000_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema2000_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2000_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2000_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema2000_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema2000_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema2000_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema2000_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2000_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2000_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2000_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2000_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
