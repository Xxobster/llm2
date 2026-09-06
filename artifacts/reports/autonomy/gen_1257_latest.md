# Autonomy public-indicator hunt gen 1257

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T160144Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema2700_below_at_h` | one_head_filter_pi_star | 334 | 27.1716 | 1.5818 | 0.6407 | 3.5165 | 0.0156 | 0.3054 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `ema2700_below_at_h` | one_head_filter_pi_star | 343 | 27.9037 | 1.5295 | 0.6356 | 3.3251 | 0.0146 | 0.3032 | ok | RAN |
| SOLUSDT | 8 | `ema2700_below_at_h` | one_head_filter_pi_star | 281 | 22.8599 | 1.8597 | 0.6512 | 4.2531 | 0.0129 | 0.3310 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema2700_below_at_h` | one_head_filter_pi_star | 263 | 21.3956 | 1.8400 | 0.6540 | 4.0855 | 0.0126 | 0.3422 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema2700_above_at_h` | one_head_filter_pi_star | 99 | 8.1374 | 1.8239 | 0.6768 | 2.5167 | 0.0115 | 0.2525 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema2700_above_at_h` | one_head_filter_pi_star | 99 | 8.1370 | 1.6272 | 0.6263 | 2.0018 | 0.0095 | 0.2424 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema2700_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.7186 | 0.3333 | -0.5631 | -0.0290 | 0.1111 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema2700_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5991 | 0.2941 | -0.8261 | -0.0413 | 0.0588 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema2700_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema2700_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema2700_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2700_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 8 | `ema2700_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2700_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema2700_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema2700_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema2700_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema2700_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2700_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema2700_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2700_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2700_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema2700_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2700_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
