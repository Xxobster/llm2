# Autonomy public-indicator hunt gen 1020

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T130848Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema902_below_at_h` | one_head_filter_pi_star | 197 | 16.0931 | 2.1079 | 0.6904 | 4.3464 | 0.0233 | 0.3807 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema902_below_at_h` | one_head_filter_pi_star | 238 | 19.4424 | 1.8389 | 0.6681 | 4.0885 | 0.0202 | 0.3487 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ema902_below_at_h` | one_head_filter_pi_star | 258 | 21.0969 | 1.8201 | 0.6473 | 3.9907 | 0.0123 | 0.3101 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema902_below_at_h` | one_head_filter_pi_star | 255 | 20.8516 | 1.7275 | 0.6431 | 3.6785 | 0.0115 | 0.3098 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema902_above_at_h` | one_head_filter_pi_star | 118 | 9.8073 | 1.6583 | 0.6441 | 2.3481 | 0.0101 | 0.3220 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema902_above_at_h` | one_head_filter_pi_star | 123 | 10.0295 | 1.6672 | 0.6341 | 2.2958 | 0.0096 | 0.3252 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema902_above_at_h` | one_head_filter_pi_star | 141 | 11.5900 | 1.2071 | 0.5887 | 0.9438 | 0.0080 | 0.2340 | ok | RAN |
| ETHUSDT | 4 | `ema902_above_at_h` | one_head_filter_pi_star | 128 | 10.5214 | 1.1965 | 0.6016 | 0.8792 | 0.0073 | 0.2344 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema902_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0516 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema902_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4605 | 0.2353 | -1.1826 | -0.0583 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema902_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema902_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema902_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema902_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema902_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema902_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema902_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema902_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema902_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema902_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema902_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema902_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema902_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema902_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
