# Autonomy public-indicator hunt gen 1025

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T134233Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 4 | `ema2120_below_at_h` | one_head_filter_pi_star | 10 | 1.4001 | 2.9360 | 0.7000 | 1.7370 | 0.1026 | 0.3000 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema2120_below_at_h` | one_head_filter_pi_star | 338 | 27.4970 | 1.6219 | 0.6420 | 3.6838 | 0.0164 | 0.3047 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `ema2120_below_at_h` | one_head_filter_pi_star | 346 | 28.1478 | 1.5536 | 0.6387 | 3.5103 | 0.0152 | 0.3006 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema2120_below_at_h` | one_head_filter_pi_star | 256 | 20.8261 | 1.9371 | 0.6562 | 4.3299 | 0.0140 | 0.3281 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema2120_below_at_h` | one_head_filter_pi_star | 284 | 23.2229 | 1.8062 | 0.6514 | 4.0883 | 0.0127 | 0.3275 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema2120_above_at_h` | one_head_filter_pi_star | 118 | 9.6218 | 1.5922 | 0.6441 | 2.1375 | 0.0086 | 0.2458 | ok | RAN |
| SOLUSDT | 4 | `ema2120_above_at_h` | one_head_filter_pi_star | 114 | 9.3699 | 1.4911 | 0.6404 | 1.7446 | 0.0071 | 0.2368 | ok | RAN |
| ETHUSDT | 8 | `ema2120_above_at_h` | one_head_filter_pi_star | 31 | 2.9018 | 1.1618 | 0.5806 | 0.3531 | 0.0067 | 0.2903 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema2120_above_at_h` | one_head_filter_pi_star | 14 | 4.3631 | 0.8450 | 0.3571 | -0.5409 | -0.0081 | 0.2143 | ok | RAN |
| BTCUSDT | 8 | `ema2120_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5935 | 0.2941 | -0.8400 | -0.0463 | 0.0588 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema2120_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.4384 | 0.2500 | -1.2254 | -0.0627 | 0.0625 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema2120_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema2120_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2120_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2120_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema2120_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema2120_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema2120_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema2120_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2120_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2120_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2120_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema2120_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2120_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
