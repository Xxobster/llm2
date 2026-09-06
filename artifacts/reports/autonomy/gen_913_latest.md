# Autonomy public-indicator hunt gen 913

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260826T025059Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 8 | `ema1840_below_at_h` | one_head_filter_pi_star | 10 | 1.4001 | 2.9360 | 0.7000 | 1.7370 | 0.1112 | 0.3000 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema1840_below_at_h` | one_head_filter_pi_star | 338 | 27.4970 | 1.6303 | 0.6450 | 3.7853 | 0.0168 | 0.3077 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema1840_below_at_h` | one_head_filter_pi_star | 320 | 26.0326 | 1.6003 | 0.6406 | 3.5310 | 0.0157 | 0.3063 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema1840_below_at_h` | one_head_filter_pi_star | 269 | 21.9964 | 1.8491 | 0.6506 | 4.2801 | 0.0134 | 0.3123 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema1840_below_at_h` | one_head_filter_pi_star | 268 | 21.9146 | 1.8357 | 0.6530 | 4.0953 | 0.0132 | 0.3358 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema1840_above_at_h` | one_head_filter_pi_star | 80 | 6.5243 | 1.8583 | 0.6750 | 2.2623 | 0.0108 | 0.2250 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema1840_above_at_h` | one_head_filter_pi_star | 92 | 7.5629 | 1.5825 | 0.6522 | 1.8194 | 0.0087 | 0.2609 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1840_above_at_h` | one_head_filter_pi_star | 50 | 4.3970 | 0.9828 | 0.5600 | -0.0529 | -0.0007 | 0.2200 | ok | RAN |
| ETHUSDT | 8 | `ema1840_above_at_h` | one_head_filter_pi_star | 21 | 2.0258 | 0.5288 | 0.3333 | -1.2255 | -0.0255 | 0.1905 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1840_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5935 | 0.2941 | -0.8400 | -0.0444 | 0.0588 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1840_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.5944 | 0.3125 | -0.8370 | -0.0493 | 0.0625 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1840_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1840_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1840_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1840_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1840_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1840_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1840_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1840_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1840_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1840_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1840_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1840_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1840_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
