# Autonomy public-indicator hunt gen 1410

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260830T064850Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret1264_neg_at_h` | one_head_filter_pi_star | 344 | 27.9851 | 1.6807 | 0.6570 | 4.1629 | 0.0176 | 0.3052 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret1264_pos_at_h` | one_head_filter_pi_star | 14 | 1.5612 | 2.2250 | 0.6429 | 1.4386 | 0.0173 | 0.5000 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret1264_neg_at_h` | one_head_filter_pi_star | 326 | 26.5207 | 1.6319 | 0.6503 | 3.8397 | 0.0166 | 0.3190 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret1264_pos_at_h` | one_head_filter_pi_star | 25 | 2.2062 | 2.2572 | 0.7200 | 1.6810 | 0.0147 | 0.4400 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret1264_neg_at_h` | one_head_filter_pi_star | 343 | 27.9037 | 1.7343 | 0.6385 | 4.2515 | 0.0110 | 0.3149 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret1264_neg_at_h` | one_head_filter_pi_star | 344 | 27.9851 | 1.6746 | 0.6337 | 4.0400 | 0.0104 | 0.3081 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ret1264_pos_at_h` | one_head_filter_pi_star | 44 | 4.2444 | 1.0779 | 0.5455 | 0.2288 | 0.0031 | 0.2500 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1264_pos_at_h` | one_head_filter_pi_star | 42 | 3.8630 | 0.9227 | 0.5000 | -0.2281 | -0.0038 | 0.2381 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret1264_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4641 | 0.2632 | -1.1807 | -0.0503 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret1264_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4350 | 0.2632 | -1.2693 | -0.0549 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1264_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret1264_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1264_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1264_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1264_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1264_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1264_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1264_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1264_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1264_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1264_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1264_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1264_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1264_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
