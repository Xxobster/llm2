# Autonomy public-indicator hunt gen 985

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260827T115644Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 4 | `ema2020_below_at_h` | one_head_filter_pi_star | 10 | 1.4001 | 2.9360 | 0.7000 | 1.7370 | 0.1026 | 0.3000 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema2020_below_at_h` | one_head_filter_pi_star | 326 | 26.5207 | 1.6375 | 0.6442 | 3.6815 | 0.0167 | 0.3129 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `ema2020_below_at_h` | one_head_filter_pi_star | 315 | 25.6259 | 1.5791 | 0.6413 | 3.3678 | 0.0151 | 0.3143 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema2020_below_at_h` | one_head_filter_pi_star | 273 | 22.3234 | 1.8588 | 0.6557 | 4.3183 | 0.0134 | 0.3333 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema2020_below_at_h` | one_head_filter_pi_star | 271 | 22.1599 | 1.8641 | 0.6568 | 4.2801 | 0.0133 | 0.3247 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema2020_above_at_h` | one_head_filter_pi_star | 97 | 7.9099 | 1.7128 | 0.6598 | 2.1129 | 0.0095 | 0.2680 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema2020_above_at_h` | one_head_filter_pi_star | 101 | 8.3014 | 1.5745 | 0.6238 | 1.8911 | 0.0081 | 0.2871 | ok | RAN |
| ETHUSDT | 4 | `ema2020_above_at_h` | one_head_filter_pi_star | 47 | 4.1332 | 1.1398 | 0.5532 | 0.3729 | 0.0056 | 0.2340 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema2020_above_at_h` | one_head_filter_pi_star | 39 | 3.5279 | 0.9716 | 0.5128 | -0.0763 | -0.0013 | 0.2821 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema2020_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.6366 | 0.3125 | -0.7061 | -0.0378 | 0.0625 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema2020_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5935 | 0.2941 | -0.8400 | -0.0463 | 0.0588 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema2020_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema2020_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2020_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2020_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema2020_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema2020_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema2020_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema2020_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2020_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2020_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2020_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema2020_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2020_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
