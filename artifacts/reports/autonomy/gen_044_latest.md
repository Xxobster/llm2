# Autonomy public-indicator hunt gen 044

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T122502Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `volosc_neg_at_h` | one_head_filter_pi_star | 34 | 2.9258 | 1.6032 | 0.6176 | 1.1371 | 0.0191 | 0.3235 | TPM<MIN | RAN |
| ETHUSDT | 8 | `volosc_neg_at_h` | one_head_filter_pi_star | 367 | 29.8562 | 1.6316 | 0.6512 | 4.0044 | 0.0175 | 0.3134 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `volosc_cross_down_0` | one_head_filter_pi_star | 380 | 30.9137 | 1.5292 | 0.6395 | 3.5078 | 0.0149 | 0.3026 | ok | RAN |
| ETHUSDT | 8 | `volosc_cross_up_0` | one_head_filter_pi_star | 57 | 5.0088 | 1.5367 | 0.6667 | 1.3920 | 0.0142 | 0.1754 | ok | RAN |
| ETHUSDT | 4 | `volosc_pos_at_h` | one_head_filter_pi_star | 357 | 29.0427 | 1.4794 | 0.6387 | 3.1084 | 0.0141 | 0.2941 | ok | RAN |
| SOLUSDT | 4 | `volosc_cross_up_0` | one_head_filter_pi_star | 52 | 4.5023 | 1.9537 | 0.6538 | 2.0234 | 0.0124 | 0.2308 | GATE_CAND | RAN |
| SOLUSDT | 8 | `volosc_cross_up_0` | one_head_filter_pi_star | 52 | 4.5023 | 1.9537 | 0.6538 | 2.0234 | 0.0116 | 0.2308 | GATE_CAND | RAN |
| SOLUSDT | 8 | `volosc_neg_at_h` | one_head_filter_pi_star | 375 | 30.5070 | 1.7184 | 0.6453 | 4.4503 | 0.0110 | 0.3253 | GATE_CAND | RAN |
| SOLUSDT | 8 | `volosc_cross_down_0` | one_head_filter_pi_star | 377 | 30.6697 | 1.7166 | 0.6393 | 4.4588 | 0.0106 | 0.3210 | GATE_CAND | RAN |
| ETHUSDT | 4 | `volosc_cross_up_0` | one_head_filter_pi_star | 52 | 4.5695 | 1.4002 | 0.6538 | 0.9841 | 0.0105 | 0.1154 | ok | RAN |
| SOLUSDT | 4 | `volosc_pos_at_h` | one_head_filter_pi_star | 364 | 29.6121 | 1.6546 | 0.6319 | 4.0060 | 0.0103 | 0.3104 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| BTCUSDT | 8 | `volosc_neg_at_h` | one_head_filter_pi_star | 27 | 2.2976 | 1.1140 | 0.4444 | 0.2277 | 0.0099 | 0.1481 | TPM<MIN | RAN |
| SOLUSDT | 4 | `volosc_neg_at_h` | one_head_filter_pi_star | 32 | 2.6259 | 1.4021 | 0.6562 | 0.8138 | 0.0069 | 0.3125 | TPM<MIN | RAN |
| ETHUSDT | 4 | `volosc_cross_down_0` | one_head_filter_pi_star | 27 | 2.5312 | 1.1730 | 0.5926 | 0.3875 | 0.0068 | 0.4074 | EBR>35% | RAN |
| BTCUSDT | 4 | `volosc_pos_at_h` | one_head_filter_pi_star | 27 | 2.2976 | 1.0729 | 0.4444 | 0.1508 | 0.0065 | 0.1481 | TPM<MIN | RAN |
| BTCUSDT | 8 | `volosc_cross_down_0` | one_head_filter_pi_star | 27 | 2.2976 | 1.0729 | 0.4444 | 0.1508 | 0.0065 | 0.1481 | TPM<MIN | RAN |
| SOLUSDT | 4 | `volosc_cross_down_0` | one_head_filter_pi_star | 29 | 2.3803 | 1.2441 | 0.6552 | 0.4975 | 0.0038 | 0.2759 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `volosc_pos_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `volosc_pos_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `volosc_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `volosc_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `volosc_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `volosc_pos_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `volosc_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
