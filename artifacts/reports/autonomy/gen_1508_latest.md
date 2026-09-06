# Autonomy public-indicator hunt gen 1508

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260831T033152Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 4 | `ema973_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 3.3760 | 0.7000 | 1.9329 | 0.1310 | 0.4000 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema973_below_at_h` | one_head_filter_pi_star | 228 | 18.6255 | 1.8360 | 0.6623 | 3.9279 | 0.0190 | 0.3421 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema973_below_at_h` | one_head_filter_pi_star | 244 | 19.9326 | 1.7456 | 0.6557 | 3.7886 | 0.0184 | 0.3402 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema973_below_at_h` | one_head_filter_pi_star | 245 | 20.0339 | 1.7777 | 0.6490 | 3.8004 | 0.0122 | 0.3102 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema973_above_at_h` | one_head_filter_pi_star | 142 | 11.7180 | 1.3298 | 0.6127 | 1.4245 | 0.0120 | 0.2254 | ok | RAN |
| SOLUSDT | 4 | `ema973_below_at_h` | one_head_filter_pi_star | 251 | 20.5245 | 1.7376 | 0.6454 | 3.6908 | 0.0118 | 0.3108 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema973_above_at_h` | one_head_filter_pi_star | 122 | 10.1398 | 1.7342 | 0.6557 | 2.4914 | 0.0109 | 0.3361 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema973_above_at_h` | one_head_filter_pi_star | 125 | 10.1925 | 1.5543 | 0.6240 | 2.0590 | 0.0084 | 0.2960 | ok | RAN |
| ETHUSDT | 4 | `ema973_above_at_h` | one_head_filter_pi_star | 120 | 9.9034 | 1.0489 | 0.5667 | 0.2249 | 0.0020 | 0.2000 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema973_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0547 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema973_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0559 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema973_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema973_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema973_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema973_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema973_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema973_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema973_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema973_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema973_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema973_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema973_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema973_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema973_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
