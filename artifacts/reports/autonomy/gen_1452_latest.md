# Autonomy public-indicator hunt gen 1452

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260830T220658Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema966_below_at_h` | one_head_filter_pi_star | 234 | 19.1157 | 1.8539 | 0.6667 | 4.0264 | 0.0199 | 0.3504 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema966_below_at_h` | one_head_filter_pi_star | 236 | 19.2790 | 1.8377 | 0.6610 | 3.9316 | 0.0197 | 0.3432 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ema966_below_at_h` | one_head_filter_pi_star | 257 | 21.0151 | 1.7251 | 0.6381 | 3.6426 | 0.0115 | 0.3074 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema966_below_at_h` | one_head_filter_pi_star | 264 | 21.5875 | 1.6741 | 0.6364 | 3.5750 | 0.0110 | 0.3106 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema966_above_at_h` | one_head_filter_pi_star | 137 | 11.1710 | 1.7262 | 0.6350 | 2.5921 | 0.0104 | 0.3212 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema966_above_at_h` | one_head_filter_pi_star | 126 | 10.2741 | 1.6346 | 0.6270 | 2.2943 | 0.0092 | 0.2937 | ok | RAN |
| ETHUSDT | 8 | `ema966_above_at_h` | one_head_filter_pi_star | 123 | 10.1510 | 1.1694 | 0.5935 | 0.7392 | 0.0066 | 0.2195 | ok | RAN |
| ETHUSDT | 4 | `ema966_above_at_h` | one_head_filter_pi_star | 132 | 10.8502 | 1.0904 | 0.5682 | 0.4265 | 0.0037 | 0.2045 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema966_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6498 | 0.3529 | -0.6566 | -0.0300 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema966_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0516 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema966_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema966_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema966_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema966_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema966_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema966_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema966_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema966_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema966_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema966_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema966_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema966_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema966_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema966_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
