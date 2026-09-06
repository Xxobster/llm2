# Autonomy public-indicator hunt gen 1034

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T144806Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret888_neg_at_h` | one_head_filter_pi_star | 197 | 16.0931 | 1.9920 | 0.6954 | 4.1186 | 0.0224 | 0.3756 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret888_neg_at_h` | one_head_filter_pi_star | 216 | 17.6452 | 1.9071 | 0.6759 | 4.2209 | 0.0213 | 0.3750 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret888_neg_at_h` | one_head_filter_pi_star | 253 | 20.7176 | 1.8493 | 0.6482 | 3.8935 | 0.0137 | 0.3557 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret888_neg_at_h` | one_head_filter_pi_star | 261 | 21.2329 | 1.8337 | 0.6437 | 3.9421 | 0.0130 | 0.3295 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ret888_pos_at_h` | one_head_filter_pi_star | 91 | 7.5101 | 1.1759 | 0.5824 | 0.7071 | 0.0079 | 0.2308 | ok | RAN |
| SOLUSDT | 4 | `ret888_pos_at_h` | one_head_filter_pi_star | 78 | 6.4110 | 1.3338 | 0.6154 | 1.0953 | 0.0059 | 0.2564 | ok | RAN |
| SOLUSDT | 8 | `ret888_pos_at_h` | one_head_filter_pi_star | 102 | 8.3836 | 1.2819 | 0.6078 | 1.0213 | 0.0046 | 0.2549 | ok | RAN |
| ETHUSDT | 8 | `ret888_pos_at_h` | one_head_filter_pi_star | 84 | 6.9324 | 1.0707 | 0.5714 | 0.2661 | 0.0031 | 0.2381 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret888_pos_at_h` | one_head_filter_pi_star | 12 | 1.5175 | 0.6838 | 0.3333 | -0.6602 | -0.0301 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret888_pos_at_h` | one_head_filter_pi_star | 11 | 1.3911 | 0.7347 | 0.3636 | -0.5189 | -0.0306 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret888_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret888_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret888_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret888_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret888_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret888_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret888_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret888_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret888_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret888_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret888_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret888_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret888_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret888_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
