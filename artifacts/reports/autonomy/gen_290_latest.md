# Autonomy public-indicator hunt gen 290

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T044629Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret144_neg_at_h` | one_head_filter_pi_star | 186 | 15.1945 | 1.9610 | 0.6882 | 4.1554 | 0.0226 | 0.3763 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret144_neg_at_h` | one_head_filter_pi_star | 196 | 16.0114 | 1.8795 | 0.6837 | 4.0615 | 0.0217 | 0.3776 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret144_neg_at_h` | one_head_filter_pi_star | 176 | 14.3917 | 2.1409 | 0.6761 | 4.1086 | 0.0164 | 0.3750 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret144_neg_at_h` | one_head_filter_pi_star | 182 | 14.8823 | 1.9805 | 0.6648 | 3.8009 | 0.0144 | 0.3571 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ret144_pos_at_h` | one_head_filter_pi_star | 180 | 14.8539 | 1.2333 | 0.6000 | 1.1452 | 0.0081 | 0.2222 | ok | RAN |
| ETHUSDT | 4 | `ret144_pos_at_h` | one_head_filter_pi_star | 190 | 15.6791 | 1.2320 | 0.5895 | 1.2390 | 0.0080 | 0.2263 | ok | RAN |
| SOLUSDT | 4 | `ret144_pos_at_h` | one_head_filter_pi_star | 190 | 15.4927 | 1.3963 | 0.6000 | 1.9046 | 0.0062 | 0.2737 | ok | RAN |
| SOLUSDT | 8 | `ret144_pos_at_h` | one_head_filter_pi_star | 189 | 15.4111 | 1.3292 | 0.5926 | 1.6290 | 0.0055 | 0.2593 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret144_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.6964 | 0.3684 | -0.6260 | -0.0321 | 0.1053 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret144_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret144_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret144_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret144_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret144_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret144_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret144_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret144_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret144_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret144_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret144_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret144_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret144_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret144_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret144_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
