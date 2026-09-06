# Autonomy public-indicator hunt gen 1210

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T111955Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret1064_neg_at_h` | one_head_filter_pi_star | 314 | 25.6509 | 1.6953 | 0.6561 | 4.1662 | 0.0177 | 0.3185 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ret1064_neg_at_h` | one_head_filter_pi_star | 296 | 24.1805 | 1.6832 | 0.6520 | 3.8948 | 0.0171 | 0.3176 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret1064_pos_at_h` | one_head_filter_pi_star | 37 | 3.0757 | 1.9899 | 0.7027 | 1.7720 | 0.0127 | 0.3514 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret1064_neg_at_h` | one_head_filter_pi_star | 294 | 23.9175 | 1.8465 | 0.6395 | 4.3123 | 0.0122 | 0.3231 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret1064_neg_at_h` | one_head_filter_pi_star | 291 | 23.6734 | 1.7797 | 0.6392 | 3.9863 | 0.0117 | 0.3196 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret1064_pos_at_h` | one_head_filter_pi_star | 41 | 3.4082 | 1.8386 | 0.7073 | 1.8550 | 0.0107 | 0.2683 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ret1064_pos_at_h` | one_head_filter_pi_star | 30 | 2.6812 | 1.1228 | 0.5667 | 0.2802 | 0.0058 | 0.3000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1064_pos_at_h` | one_head_filter_pi_star | 36 | 3.3112 | 1.0420 | 0.5278 | 0.1115 | 0.0023 | 0.2778 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret1064_pos_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.4075 | 0.2500 | -1.2442 | -0.0478 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret1064_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.3827 | 0.2353 | -1.3686 | -0.0540 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1064_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret1064_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1064_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1064_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1064_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1064_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1064_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1064_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1064_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1064_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1064_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1064_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1064_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1064_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
