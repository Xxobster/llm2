# Autonomy public-indicator hunt gen 1397

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260830T052647Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret243_neg_at_h` | one_head_filter_pi_star | 167 | 13.6424 | 2.0004 | 0.6826 | 4.0985 | 0.0241 | 0.3832 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret243_neg_at_h` | one_head_filter_pi_star | 162 | 13.2339 | 2.0557 | 0.7037 | 4.1858 | 0.0241 | 0.3889 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret243_neg_at_h` | one_head_filter_pi_star | 198 | 16.1906 | 1.9108 | 0.6616 | 3.8305 | 0.0141 | 0.3485 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret243_neg_at_h` | one_head_filter_pi_star | 184 | 15.0458 | 1.8568 | 0.6576 | 3.6773 | 0.0127 | 0.3370 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret243_pos_at_h` | one_head_filter_pi_star | 179 | 14.5957 | 1.5257 | 0.6257 | 2.3818 | 0.0080 | 0.2849 | ok | RAN |
| SOLUSDT | 4 | `ret243_pos_at_h` | one_head_filter_pi_star | 175 | 14.2696 | 1.5164 | 0.6229 | 2.2914 | 0.0080 | 0.2800 | ok | RAN |
| ETHUSDT | 4 | `ret243_pos_at_h` | one_head_filter_pi_star | 178 | 14.6314 | 1.2121 | 0.6011 | 1.0420 | 0.0075 | 0.2303 | ok | RAN |
| ETHUSDT | 8 | `ret243_pos_at_h` | one_head_filter_pi_star | 188 | 15.4534 | 1.1419 | 0.5904 | 0.7367 | 0.0051 | 0.2287 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret243_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0411 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret243_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret243_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret243_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret243_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret243_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret243_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret243_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret243_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret243_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret243_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret243_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret243_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret243_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret243_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret243_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
