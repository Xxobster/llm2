# Autonomy public-indicator hunt gen 658

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T041634Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret512_neg_at_h` | one_head_filter_pi_star | 139 | 11.3550 | 2.7018 | 0.7410 | 5.1751 | 0.0321 | 0.4460 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret512_neg_at_h` | one_head_filter_pi_star | 154 | 12.5804 | 2.1449 | 0.7078 | 4.1283 | 0.0253 | 0.3896 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret512_neg_at_h` | one_head_filter_pi_star | 182 | 14.8823 | 1.7976 | 0.6703 | 3.2613 | 0.0123 | 0.3462 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret512_neg_at_h` | one_head_filter_pi_star | 183 | 15.0631 | 1.7168 | 0.6612 | 3.0648 | 0.0116 | 0.3443 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret512_pos_at_h` | one_head_filter_pi_star | 156 | 12.9656 | 1.6214 | 0.6026 | 2.6307 | 0.0096 | 0.2756 | ok | RAN |
| SOLUSDT | 4 | `ret512_pos_at_h` | one_head_filter_pi_star | 96 | 7.9793 | 1.5562 | 0.6146 | 1.8531 | 0.0083 | 0.2396 | ok | RAN |
| ETHUSDT | 8 | `ret512_pos_at_h` | one_head_filter_pi_star | 147 | 12.0832 | 1.1826 | 0.5918 | 0.8631 | 0.0068 | 0.2313 | ok | RAN |
| ETHUSDT | 4 | `ret512_pos_at_h` | one_head_filter_pi_star | 169 | 13.8916 | 1.1149 | 0.5680 | 0.6255 | 0.0045 | 0.2426 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret512_pos_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5547 | 0.3000 | -0.9879 | -0.0437 | 0.0500 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret512_pos_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5547 | 0.3000 | -0.9879 | -0.0437 | 0.0500 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret512_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret512_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret512_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret512_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret512_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret512_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret512_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret512_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret512_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret512_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret512_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret512_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret512_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret512_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
