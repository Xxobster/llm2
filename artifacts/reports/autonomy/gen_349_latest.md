# Autonomy public-indicator hunt gen 349

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T145405Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret37_neg_at_h` | one_head_filter_pi_star | 197 | 16.0931 | 1.7364 | 0.6650 | 3.5277 | 0.0195 | 0.3553 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret37_neg_at_h` | one_head_filter_pi_star | 200 | 16.3382 | 1.6245 | 0.6600 | 3.1827 | 0.0173 | 0.3500 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret37_neg_at_h` | one_head_filter_pi_star | 163 | 13.3287 | 1.9538 | 0.6687 | 3.5307 | 0.0159 | 0.3988 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret37_neg_at_h` | one_head_filter_pi_star | 166 | 13.5740 | 1.9475 | 0.6687 | 3.5397 | 0.0155 | 0.3795 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret37_cross_down_0` | one_head_filter_pi_star | 25 | 2.1337 | 1.7558 | 0.6000 | 1.1815 | 0.0146 | 0.2000 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ret37_pos_at_h` | one_head_filter_pi_star | 169 | 13.8916 | 1.3184 | 0.6213 | 1.4943 | 0.0094 | 0.2249 | ok | RAN |
| ETHUSDT | 4 | `ret37_pos_at_h` | one_head_filter_pi_star | 174 | 14.3026 | 1.2685 | 0.6092 | 1.2858 | 0.0085 | 0.2356 | ok | RAN |
| SOLUSDT | 4 | `ret37_pos_at_h` | one_head_filter_pi_star | 215 | 17.5312 | 1.5078 | 0.6140 | 2.5743 | 0.0070 | 0.2605 | ok | RAN |
| SOLUSDT | 8 | `ret37_pos_at_h` | one_head_filter_pi_star | 210 | 17.1235 | 1.4957 | 0.6095 | 2.4469 | 0.0069 | 0.2619 | ok | RAN |
| ETHUSDT | 8 | `ret37_cross_up_0` | one_head_filter_pi_star | 28 | 2.7603 | 1.0352 | 0.4643 | 0.0861 | 0.0019 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ret37_cross_up_0` | one_head_filter_pi_star | 16 | 1.4943 | 0.8013 | 0.5000 | -0.3549 | -0.0052 | 0.1250 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret37_cross_down_0` | one_head_filter_pi_star | 32 | 2.6517 | 0.8026 | 0.4375 | -0.4900 | -0.0091 | 0.1562 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret37_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret37_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret37_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret37_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret37_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret37_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret37_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret37_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret37_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret37_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret37_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret37_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
