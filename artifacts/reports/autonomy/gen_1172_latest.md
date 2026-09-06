# Autonomy public-indicator hunt gen 1172

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T073101Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema924_below_at_h` | one_head_filter_pi_star | 245 | 20.0143 | 1.8174 | 0.6571 | 4.0213 | 0.0192 | 0.3388 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema924_below_at_h` | one_head_filter_pi_star | 233 | 19.0340 | 1.7980 | 0.6652 | 3.7708 | 0.0189 | 0.3562 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema924_below_at_h` | one_head_filter_pi_star | 260 | 21.2604 | 1.8460 | 0.6500 | 4.1289 | 0.0127 | 0.3077 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema924_above_at_h` | one_head_filter_pi_star | 128 | 10.5636 | 1.3580 | 0.6172 | 1.4733 | 0.0126 | 0.2266 | ok | RAN |
| SOLUSDT | 4 | `ema924_below_at_h` | one_head_filter_pi_star | 255 | 20.8516 | 1.7668 | 0.6471 | 3.8196 | 0.0119 | 0.3059 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema924_above_at_h` | one_head_filter_pi_star | 123 | 10.0295 | 1.7104 | 0.6341 | 2.3963 | 0.0103 | 0.3171 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema924_above_at_h` | one_head_filter_pi_star | 132 | 10.7633 | 1.4858 | 0.6136 | 2.0056 | 0.0075 | 0.3106 | ok | RAN |
| ETHUSDT | 4 | `ema924_above_at_h` | one_head_filter_pi_star | 136 | 11.1790 | 1.1362 | 0.5882 | 0.6517 | 0.0054 | 0.2206 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema924_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6498 | 0.3529 | -0.6566 | -0.0313 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema924_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0516 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema924_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema924_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema924_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema924_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema924_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema924_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema924_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema924_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema924_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema924_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema924_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema924_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema924_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema924_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
