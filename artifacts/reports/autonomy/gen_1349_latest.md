# Autonomy public-indicator hunt gen 1349

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260830T005441Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret236_neg_at_h` | one_head_filter_pi_star | 180 | 14.7044 | 2.1801 | 0.7111 | 4.6274 | 0.0264 | 0.3889 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret236_neg_at_h` | one_head_filter_pi_star | 179 | 14.6227 | 2.0221 | 0.6872 | 4.2675 | 0.0242 | 0.3575 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret236_neg_at_h` | one_head_filter_pi_star | 203 | 16.5995 | 1.8968 | 0.6552 | 3.8765 | 0.0133 | 0.3498 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret236_neg_at_h` | one_head_filter_pi_star | 186 | 15.2094 | 1.8432 | 0.6559 | 3.5819 | 0.0129 | 0.3441 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ret236_pos_at_h` | one_head_filter_pi_star | 189 | 15.5356 | 1.2298 | 0.6032 | 1.1735 | 0.0082 | 0.2328 | ok | RAN |
| SOLUSDT | 4 | `ret236_pos_at_h` | one_head_filter_pi_star | 170 | 13.8619 | 1.4960 | 0.6118 | 2.1992 | 0.0076 | 0.2824 | ok | RAN |
| SOLUSDT | 8 | `ret236_pos_at_h` | one_head_filter_pi_star | 175 | 14.2696 | 1.4610 | 0.6114 | 2.0955 | 0.0073 | 0.2743 | ok | RAN |
| ETHUSDT | 8 | `ret236_pos_at_h` | one_head_filter_pi_star | 164 | 13.4806 | 1.1644 | 0.6037 | 0.8316 | 0.0062 | 0.2317 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret236_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret236_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret236_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret236_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret236_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret236_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret236_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret236_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret236_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret236_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret236_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret236_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret236_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret236_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret236_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret236_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
