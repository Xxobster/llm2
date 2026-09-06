# Autonomy public-indicator hunt gen 1413

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260830T070531Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret245_neg_at_h` | one_head_filter_pi_star | 173 | 14.1325 | 2.0374 | 0.6936 | 4.2613 | 0.0250 | 0.3757 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret245_neg_at_h` | one_head_filter_pi_star | 170 | 13.8874 | 1.9962 | 0.6882 | 3.9507 | 0.0238 | 0.3824 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret245_neg_at_h` | one_head_filter_pi_star | 184 | 15.0458 | 1.9473 | 0.6576 | 3.8105 | 0.0138 | 0.3478 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret245_neg_at_h` | one_head_filter_pi_star | 180 | 14.7188 | 1.8850 | 0.6500 | 3.5124 | 0.0137 | 0.3500 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ret245_pos_at_h` | one_head_filter_pi_star | 173 | 14.1065 | 1.6030 | 0.6301 | 2.6412 | 0.0093 | 0.2832 | ok | RAN |
| ETHUSDT | 8 | `ret245_pos_at_h` | one_head_filter_pi_star | 159 | 13.1209 | 1.2710 | 0.6038 | 1.2535 | 0.0091 | 0.2264 | ok | RAN |
| SOLUSDT | 8 | `ret245_pos_at_h` | one_head_filter_pi_star | 172 | 14.0249 | 1.5047 | 0.6105 | 2.2194 | 0.0077 | 0.2907 | ok | RAN |
| ETHUSDT | 4 | `ret245_pos_at_h` | one_head_filter_pi_star | 160 | 13.1518 | 1.1997 | 0.6062 | 0.9728 | 0.0074 | 0.2437 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret245_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret245_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret245_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret245_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret245_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret245_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret245_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret245_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret245_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret245_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret245_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret245_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret245_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret245_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret245_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret245_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
