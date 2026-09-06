# Autonomy public-indicator hunt gen 1137

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T032036Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema2400_below_at_h` | one_head_filter_pi_star | 352 | 28.6359 | 1.6113 | 0.6449 | 3.7935 | 0.0163 | 0.2983 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `ema2400_below_at_h` | one_head_filter_pi_star | 342 | 27.8224 | 1.5495 | 0.6404 | 3.4334 | 0.0151 | 0.3041 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema2400_below_at_h` | one_head_filter_pi_star | 275 | 22.3718 | 1.8518 | 0.6509 | 4.1605 | 0.0128 | 0.3273 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema2400_below_at_h` | one_head_filter_pi_star | 278 | 22.6158 | 1.8307 | 0.6511 | 4.1597 | 0.0125 | 0.3309 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema2400_above_at_h` | one_head_filter_pi_star | 109 | 9.0593 | 1.7261 | 0.6514 | 2.4045 | 0.0105 | 0.2661 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema2400_above_at_h` | one_head_filter_pi_star | 100 | 8.2192 | 1.6829 | 0.6500 | 2.1235 | 0.0098 | 0.2700 | GATE_CAND | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema2400_above_at_h` | one_head_filter_pi_star | 15 | 4.6747 | 0.7592 | 0.4000 | -0.9306 | -0.0150 | 0.2667 | ok | RAN |
| BTCUSDT | 4 | `ema2400_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.7376 | 0.3684 | -0.5246 | -0.0265 | 0.1053 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema2400_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5765 | 0.2778 | -0.8994 | -0.0458 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema2400_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema2400_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2400_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 8 | `ema2400_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2400_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema2400_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema2400_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema2400_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema2400_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2400_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema2400_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2400_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2400_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema2400_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2400_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
