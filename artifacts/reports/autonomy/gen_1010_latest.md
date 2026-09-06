# Autonomy public-indicator hunt gen 1010

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T113711Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret864_neg_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 2.1072 | 0.6931 | 4.4088 | 0.0234 | 0.3810 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret864_neg_at_h` | one_head_filter_pi_star | 175 | 14.2959 | 1.8414 | 0.6800 | 3.5296 | 0.0195 | 0.4057 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret864_neg_at_h` | one_head_filter_pi_star | 235 | 19.2162 | 1.9698 | 0.6511 | 4.2041 | 0.0154 | 0.3489 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret864_neg_at_h` | one_head_filter_pi_star | 241 | 19.7068 | 1.9315 | 0.6598 | 4.2408 | 0.0141 | 0.3402 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ret864_pos_at_h` | one_head_filter_pi_star | 71 | 5.8595 | 1.1822 | 0.6056 | 0.6174 | 0.0083 | 0.2394 | ok | RAN |
| SOLUSDT | 8 | `ret864_pos_at_h` | one_head_filter_pi_star | 66 | 5.4247 | 1.4778 | 0.6364 | 1.3052 | 0.0071 | 0.2121 | ok | RAN |
| ETHUSDT | 8 | `ret864_pos_at_h` | one_head_filter_pi_star | 79 | 6.5197 | 1.1468 | 0.5696 | 0.5365 | 0.0064 | 0.2278 | ok | RAN |
| SOLUSDT | 4 | `ret864_pos_at_h` | one_head_filter_pi_star | 91 | 7.5633 | 1.3920 | 0.6374 | 1.3567 | 0.0062 | 0.2747 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret864_pos_at_h` | one_head_filter_pi_star | 14 | 1.1914 | 0.5196 | 0.2857 | -0.9461 | -0.0534 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret864_pos_at_h` | one_head_filter_pi_star | 15 | 1.2765 | 0.3372 | 0.2667 | -1.4992 | -0.0936 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret864_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret864_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret864_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret864_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret864_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret864_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret864_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret864_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret864_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret864_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret864_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret864_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret864_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret864_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
