# Autonomy public-indicator hunt gen 1321

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T221849Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema2860_below_at_h` | one_head_filter_pi_star | 342 | 27.8224 | 1.6214 | 0.6462 | 3.6917 | 0.0164 | 0.3070 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema2860_below_at_h` | one_head_filter_pi_star | 340 | 27.6597 | 1.5871 | 0.6412 | 3.5497 | 0.0156 | 0.3059 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ema2860_below_at_h` | one_head_filter_pi_star | 279 | 22.8141 | 1.9006 | 0.6523 | 4.4425 | 0.0133 | 0.3369 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema2860_below_at_h` | one_head_filter_pi_star | 291 | 23.6734 | 1.7875 | 0.6460 | 4.0803 | 0.0120 | 0.3196 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema2860_above_at_h` | one_head_filter_pi_star | 89 | 7.3151 | 1.5304 | 0.6292 | 1.6482 | 0.0075 | 0.2360 | ok | RAN |
| SOLUSDT | 4 | `ema2860_above_at_h` | one_head_filter_pi_star | 114 | 9.3699 | 1.3691 | 0.6140 | 1.3931 | 0.0063 | 0.2456 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema2860_above_at_h` | one_head_filter_pi_star | 18 | 5.4318 | 0.6512 | 0.3889 | -1.5683 | -0.0206 | 0.2222 | ok | RAN |
| BTCUSDT | 8 | `ema2860_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.7438 | 0.4000 | -0.5121 | -0.0254 | 0.1000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema2860_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema2860_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2860_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2860_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2860_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema2860_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema2860_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema2860_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema2860_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2860_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2860_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema2860_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2860_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2860_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema2860_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2860_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
