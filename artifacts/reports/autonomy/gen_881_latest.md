# Autonomy public-indicator hunt gen 881

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T233033Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 4 | `ema1760_below_at_h` | one_head_filter_pi_star | 10 | 1.4001 | 2.9360 | 0.7000 | 1.7370 | 0.1067 | 0.3000 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema1760_below_at_h` | one_head_filter_pi_star | 332 | 27.1214 | 1.6080 | 0.6446 | 3.6398 | 0.0162 | 0.3133 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema1760_below_at_h` | one_head_filter_pi_star | 328 | 26.6834 | 1.5841 | 0.6402 | 3.5050 | 0.0155 | 0.3110 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ema1760_below_at_h` | one_head_filter_pi_star | 263 | 21.5057 | 1.8775 | 0.6616 | 4.3700 | 0.0137 | 0.3308 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema1760_above_at_h` | one_head_filter_pi_star | 57 | 5.0126 | 1.3357 | 0.5965 | 0.8908 | 0.0123 | 0.2105 | ok | RAN |
| SOLUSDT | 8 | `ema1760_below_at_h` | one_head_filter_pi_star | 292 | 23.8771 | 1.7160 | 0.6404 | 3.9008 | 0.0117 | 0.3185 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema1760_above_at_h` | one_head_filter_pi_star | 100 | 8.1540 | 1.5728 | 0.6400 | 1.8829 | 0.0083 | 0.2700 | ok | RAN |
| SOLUSDT | 8 | `ema1760_above_at_h` | one_head_filter_pi_star | 84 | 6.8505 | 1.5643 | 0.6548 | 1.6580 | 0.0079 | 0.2619 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema1760_above_at_h` | one_head_filter_pi_star | 46 | 4.0453 | 0.8792 | 0.5217 | -0.3726 | -0.0057 | 0.2391 | ok | RAN |
| BTCUSDT | 8 | `ema1760_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.6235 | 0.3125 | -0.7441 | -0.0400 | 0.0625 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1760_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.5944 | 0.3125 | -0.8370 | -0.0472 | 0.0625 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1760_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1760_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1760_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1760_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1760_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1760_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1760_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1760_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1760_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1760_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1760_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1760_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1760_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
