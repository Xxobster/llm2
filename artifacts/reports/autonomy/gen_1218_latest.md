# Autonomy public-indicator hunt gen 1218

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T120344Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret1072_neg_at_h` | one_head_filter_pi_star | 316 | 25.7072 | 1.7267 | 0.6582 | 4.2484 | 0.0181 | 0.3101 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret1072_neg_at_h` | one_head_filter_pi_star | 299 | 24.4256 | 1.6819 | 0.6488 | 3.9151 | 0.0173 | 0.3311 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ret1072_pos_at_h` | one_head_filter_pi_star | 15 | 1.4822 | 1.3161 | 0.5333 | 0.4863 | 0.0157 | 0.4000 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret1072_pos_at_h` | one_head_filter_pi_star | 43 | 3.5745 | 1.9946 | 0.7209 | 1.8501 | 0.0128 | 0.3256 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ret1072_neg_at_h` | one_head_filter_pi_star | 285 | 23.3047 | 1.7448 | 0.6421 | 3.9750 | 0.0117 | 0.3193 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret1072_neg_at_h` | one_head_filter_pi_star | 304 | 24.7310 | 1.7695 | 0.6382 | 4.0614 | 0.0114 | 0.3191 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ret1072_pos_at_h` | one_head_filter_pi_star | 45 | 3.7876 | 1.4432 | 0.6444 | 1.1064 | 0.0072 | 0.3111 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret1072_pos_at_h` | one_head_filter_pi_star | 13 | 1.2763 | 0.9844 | 0.5385 | -0.0256 | -0.0009 | 0.4615 | EBR>35% | RAN |
| BTCUSDT | 8 | `ret1072_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.3827 | 0.2353 | -1.3686 | -0.0530 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret1072_pos_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.3447 | 0.3125 | -1.4779 | -0.0701 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1072_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret1072_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1072_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1072_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1072_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1072_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1072_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1072_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1072_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret1072_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1072_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1072_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1072_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1072_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
