# Autonomy public-indicator hunt gen 1130

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T023329Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret984_neg_at_h` | one_head_filter_pi_star | 201 | 16.4199 | 1.8943 | 0.6766 | 3.7029 | 0.0207 | 0.3682 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret984_neg_at_h` | one_head_filter_pi_star | 200 | 16.3382 | 1.8602 | 0.6800 | 3.5892 | 0.0206 | 0.3800 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret984_neg_at_h` | one_head_filter_pi_star | 265 | 21.5583 | 1.9105 | 0.6604 | 4.3248 | 0.0136 | 0.3358 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret984_neg_at_h` | one_head_filter_pi_star | 292 | 23.7548 | 1.7365 | 0.6301 | 3.9468 | 0.0113 | 0.3253 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ret984_pos_at_h` | one_head_filter_pi_star | 44 | 3.6170 | 1.5789 | 0.6818 | 1.2683 | 0.0085 | 0.2955 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ret984_pos_at_h` | one_head_filter_pi_star | 40 | 3.2882 | 1.5764 | 0.6500 | 1.1763 | 0.0080 | 0.2750 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret984_pos_at_h` | one_head_filter_pi_star | 83 | 6.8499 | 1.1110 | 0.5783 | 0.3950 | 0.0048 | 0.2169 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret984_pos_at_h` | one_head_filter_pi_star | 44 | 3.7490 | 0.9416 | 0.5455 | -0.1705 | -0.0027 | 0.2500 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret984_pos_at_h` | one_head_filter_pi_star | 15 | 1.2765 | 0.3318 | 0.2667 | -1.4856 | -0.0731 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret984_pos_at_h` | one_head_filter_pi_star | 14 | 1.1914 | 0.3194 | 0.2143 | -1.5369 | -0.0791 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret984_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret984_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret984_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret984_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret984_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret984_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret984_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret984_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret984_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret984_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret984_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret984_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret984_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret984_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
