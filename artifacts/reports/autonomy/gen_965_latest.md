# Autonomy public-indicator hunt gen 965

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260826T181502Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret189_neg_at_h` | one_head_filter_pi_star | 175 | 14.2959 | 2.1960 | 0.7029 | 4.7458 | 0.0275 | 0.3943 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret189_neg_at_h` | one_head_filter_pi_star | 165 | 13.4790 | 2.0782 | 0.6909 | 4.3058 | 0.0249 | 0.3939 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret189_neg_at_h` | one_head_filter_pi_star | 168 | 13.7375 | 2.2138 | 0.6786 | 4.1746 | 0.0168 | 0.3690 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret189_neg_at_h` | one_head_filter_pi_star | 171 | 13.9828 | 1.9609 | 0.6725 | 3.6718 | 0.0148 | 0.3684 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ret189_pos_at_h` | one_head_filter_pi_star | 200 | 16.3081 | 1.5032 | 0.6250 | 2.4307 | 0.0076 | 0.2700 | ok | RAN |
| SOLUSDT | 8 | `ret189_pos_at_h` | one_head_filter_pi_star | 196 | 15.9819 | 1.3779 | 0.6020 | 1.8658 | 0.0058 | 0.2602 | ok | RAN |
| ETHUSDT | 8 | `ret189_pos_at_h` | one_head_filter_pi_star | 191 | 15.7616 | 1.1610 | 0.5864 | 0.8498 | 0.0056 | 0.2094 | ok | RAN |
| ETHUSDT | 4 | `ret189_pos_at_h` | one_head_filter_pi_star | 199 | 16.4218 | 1.1042 | 0.5829 | 0.5904 | 0.0037 | 0.2211 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret189_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5773 | 0.2941 | -0.8964 | -0.0448 | 0.0588 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret189_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5765 | 0.2778 | -0.8994 | -0.0449 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret189_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret189_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret189_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret189_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret189_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret189_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret189_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret189_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret189_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret189_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret189_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret189_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret189_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret189_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
