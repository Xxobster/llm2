# Autonomy public-indicator hunt gen 1090

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T214705Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret944_neg_at_h` | one_head_filter_pi_star | 261 | 21.3213 | 1.7728 | 0.6590 | 4.0490 | 0.0193 | 0.3525 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret944_neg_at_h` | one_head_filter_pi_star | 278 | 22.7101 | 1.6841 | 0.6439 | 3.8388 | 0.0169 | 0.3309 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret944_neg_at_h` | one_head_filter_pi_star | 261 | 21.3727 | 2.0852 | 0.6667 | 4.8435 | 0.0153 | 0.3218 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret944_pos_at_h` | one_head_filter_pi_star | 59 | 4.8493 | 1.9058 | 0.6780 | 2.0939 | 0.0123 | 0.2712 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret944_neg_at_h` | one_head_filter_pi_star | 281 | 22.9776 | 1.8067 | 0.6441 | 3.9945 | 0.0120 | 0.3274 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ret944_pos_at_h` | one_head_filter_pi_star | 51 | 4.2395 | 1.5603 | 0.6863 | 1.3196 | 0.0090 | 0.2549 | ok | RAN |
| ETHUSDT | 8 | `ret944_pos_at_h` | one_head_filter_pi_star | 66 | 5.8041 | 1.1532 | 0.6212 | 0.5373 | 0.0071 | 0.2273 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret944_pos_at_h` | one_head_filter_pi_star | 48 | 4.2211 | 0.8959 | 0.5208 | -0.3331 | -0.0055 | 0.2292 | ok | RAN |
| BTCUSDT | 4 | `ret944_pos_at_h` | one_head_filter_pi_star | 14 | 1.1914 | 0.3896 | 0.2143 | -1.3080 | -0.0582 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret944_pos_at_h` | one_head_filter_pi_star | 15 | 1.2765 | 0.4612 | 0.3333 | -1.0941 | -0.0602 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret944_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret944_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret944_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret944_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret944_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret944_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret944_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret944_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret944_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret944_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret944_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret944_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret944_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret944_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
