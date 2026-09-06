# Autonomy public-indicator hunt gen 1226

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T124731Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret1080_neg_at_h` | one_head_filter_pi_star | 318 | 25.8699 | 1.7064 | 0.6541 | 4.2017 | 0.0180 | 0.3208 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret1080_neg_at_h` | one_head_filter_pi_star | 304 | 24.7310 | 1.7379 | 0.6579 | 4.1963 | 0.0180 | 0.3257 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret1080_pos_at_h` | one_head_filter_pi_star | 44 | 3.7489 | 2.1418 | 0.6818 | 2.0897 | 0.0144 | 0.2045 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ret1080_neg_at_h` | one_head_filter_pi_star | 294 | 24.0406 | 1.8301 | 0.6463 | 4.2975 | 0.0127 | 0.3367 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret1080_neg_at_h` | one_head_filter_pi_star | 289 | 23.6318 | 1.7999 | 0.6471 | 4.1515 | 0.0123 | 0.3149 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ret1080_pos_at_h` | one_head_filter_pi_star | 49 | 3.9957 | 1.1792 | 0.5918 | 0.4910 | 0.0028 | 0.1837 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret1080_pos_at_h` | one_head_filter_pi_star | 20 | 1.8507 | 0.8540 | 0.4500 | -0.3080 | -0.0085 | 0.3500 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1080_pos_at_h` | one_head_filter_pi_star | 14 | 1.3745 | 0.6683 | 0.4286 | -0.6760 | -0.0213 | 0.4286 | EBR>35% | RAN |
| BTCUSDT | 8 | `ret1080_pos_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.4075 | 0.2500 | -1.2442 | -0.0478 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret1080_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.3008 | 0.2222 | -1.6957 | -0.0723 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1080_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret1080_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1080_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1080_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1080_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1080_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1080_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1080_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1080_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1080_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1080_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1080_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1080_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1080_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
