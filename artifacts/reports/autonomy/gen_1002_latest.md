# Autonomy public-indicator hunt gen 1002

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T103325Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret856_neg_at_h` | one_head_filter_pi_star | 148 | 12.0902 | 2.2501 | 0.7095 | 4.0227 | 0.0253 | 0.4324 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret856_neg_at_h` | one_head_filter_pi_star | 195 | 15.9297 | 2.1800 | 0.7128 | 4.5918 | 0.0246 | 0.3949 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret856_neg_at_h` | one_head_filter_pi_star | 230 | 18.8073 | 2.0704 | 0.6739 | 4.3603 | 0.0161 | 0.3478 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret856_neg_at_h` | one_head_filter_pi_star | 231 | 18.8891 | 2.0289 | 0.6667 | 4.2730 | 0.0156 | 0.3420 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ret856_pos_at_h` | one_head_filter_pi_star | 86 | 7.0974 | 1.1769 | 0.5930 | 0.6692 | 0.0078 | 0.2558 | ok | RAN |
| SOLUSDT | 4 | `ret856_pos_at_h` | one_head_filter_pi_star | 83 | 6.8064 | 1.4930 | 0.6506 | 1.6196 | 0.0074 | 0.2651 | ok | RAN |
| ETHUSDT | 4 | `ret856_pos_at_h` | one_head_filter_pi_star | 104 | 8.5487 | 1.1227 | 0.5673 | 0.5330 | 0.0057 | 0.2596 | ok | RAN |
| SOLUSDT | 8 | `ret856_pos_at_h` | one_head_filter_pi_star | 93 | 7.6797 | 1.3708 | 0.6344 | 1.3182 | 0.0055 | 0.2473 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret856_pos_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.8880 | 0.4375 | -0.1856 | -0.0086 | 0.0625 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret856_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.8312 | 0.4118 | -0.2971 | -0.0139 | 0.0588 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret856_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret856_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret856_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret856_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret856_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret856_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret856_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret856_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret856_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret856_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret856_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret856_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret856_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret856_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
