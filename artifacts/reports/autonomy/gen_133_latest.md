# Autonomy public-indicator hunt gen 133

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T181313Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret32_cross_up_0` | one_head_filter_pi_star | 24 | 2.0084 | 2.7436 | 0.6667 | 2.0539 | 0.0426 | 0.2083 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret32_neg_at_h` | one_head_filter_pi_star | 205 | 16.7466 | 1.8210 | 0.6732 | 3.9120 | 0.0213 | 0.3756 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret32_neg_at_h` | one_head_filter_pi_star | 209 | 17.0734 | 1.7892 | 0.6651 | 3.7938 | 0.0206 | 0.3541 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret32_neg_at_h` | one_head_filter_pi_star | 166 | 13.5740 | 2.1071 | 0.6867 | 3.9672 | 0.0166 | 0.4036 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret32_cross_down_0` | one_head_filter_pi_star | 42 | 3.4803 | 1.5286 | 0.5476 | 1.1291 | 0.0163 | 0.2619 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ret32_neg_at_h` | one_head_filter_pi_star | 164 | 13.4104 | 1.9887 | 0.6707 | 3.6553 | 0.0159 | 0.4024 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ret32_pos_at_h` | one_head_filter_pi_star | 170 | 13.9738 | 1.2376 | 0.6059 | 1.1660 | 0.0073 | 0.2235 | ok | RAN |
| SOLUSDT | 4 | `ret32_pos_at_h` | one_head_filter_pi_star | 218 | 17.7758 | 1.5222 | 0.6147 | 2.5904 | 0.0073 | 0.2523 | ok | RAN |
| ETHUSDT | 8 | `ret32_pos_at_h` | one_head_filter_pi_star | 166 | 13.6986 | 1.1943 | 0.6024 | 0.9436 | 0.0062 | 0.2108 | ok | RAN |
| SOLUSDT | 8 | `ret32_pos_at_h` | one_head_filter_pi_star | 210 | 17.1235 | 1.4124 | 0.6048 | 2.1117 | 0.0061 | 0.2571 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret32_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret32_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret32_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret32_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret32_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret32_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret32_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret32_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret32_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret32_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret32_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret32_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret32_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret32_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
