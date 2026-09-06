# Autonomy public-indicator hunt gen 1329

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T230204Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `ema2880_below_at_h` | one_head_filter_pi_star | 335 | 27.2529 | 1.5480 | 0.6358 | 3.3613 | 0.0148 | 0.3015 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema2880_below_at_h` | one_head_filter_pi_star | 283 | 23.1412 | 1.9931 | 0.6572 | 4.8145 | 0.0145 | 0.3322 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema2880_below_at_h` | one_head_filter_pi_star | 340 | 27.6597 | 1.5222 | 0.6353 | 3.2306 | 0.0143 | 0.3029 | ok | RAN |
| SOLUSDT | 8 | `ema2880_below_at_h` | one_head_filter_pi_star | 277 | 22.5345 | 1.8704 | 0.6570 | 4.3078 | 0.0130 | 0.3321 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema2880_above_at_h` | one_head_filter_pi_star | 98 | 8.0548 | 1.6670 | 0.6531 | 2.1024 | 0.0094 | 0.2551 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema2880_above_at_h` | one_head_filter_pi_star | 94 | 7.7260 | 1.6345 | 0.6596 | 1.9682 | 0.0090 | 0.2340 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema2880_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.7248 | 0.3684 | -0.5505 | -0.0273 | 0.1053 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema2880_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema2880_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema2880_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2880_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 8 | `ema2880_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2880_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema2880_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema2880_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema2880_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema2880_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2880_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2880_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema2880_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2880_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2880_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema2880_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2880_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
