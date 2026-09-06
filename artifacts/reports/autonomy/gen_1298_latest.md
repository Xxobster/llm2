# Autonomy public-indicator hunt gen 1298

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T200453Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret1152_neg_at_h` | one_head_filter_pi_star | 335 | 27.2529 | 1.6606 | 0.6567 | 3.9509 | 0.0173 | 0.3075 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret1152_neg_at_h` | one_head_filter_pi_star | 329 | 26.7648 | 1.6605 | 0.6535 | 3.9035 | 0.0170 | 0.3131 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret1152_neg_at_h` | one_head_filter_pi_star | 344 | 27.9851 | 1.6885 | 0.6337 | 4.0635 | 0.0108 | 0.3227 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ret1152_neg_at_h` | one_head_filter_pi_star | 341 | 27.7410 | 1.6251 | 0.6276 | 3.7061 | 0.0098 | 0.3255 | ok | RAN |
| SOLUSDT | 4 | `ret1152_pos_at_h` | one_head_filter_pi_star | 21 | 1.7677 | 1.5187 | 0.6667 | 0.8377 | 0.0086 | 0.2381 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ret1152_pos_at_h` | one_head_filter_pi_star | 18 | 1.6020 | 1.0378 | 0.5556 | 0.0682 | 0.0006 | 0.1667 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1152_pos_at_h` | one_head_filter_pi_star | 43 | 4.0145 | 0.9904 | 0.4884 | -0.0276 | -0.0004 | 0.2558 | ok | RAN |
| ETHUSDT | 8 | `ret1152_pos_at_h` | one_head_filter_pi_star | 37 | 3.4543 | 0.8720 | 0.4865 | -0.3690 | -0.0054 | 0.2973 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret1152_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.3159 | 0.2353 | -1.5894 | -0.0686 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret1152_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.3159 | 0.2353 | -1.5894 | -0.0712 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1152_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret1152_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1152_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1152_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1152_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1152_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1152_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1152_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1152_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1152_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1152_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1152_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1152_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1152_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
