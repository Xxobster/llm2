# Autonomy public-indicator hunt gen 762

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T114758Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret616_neg_at_h` | one_head_filter_pi_star | 168 | 13.7241 | 2.3180 | 0.7083 | 4.7925 | 0.0264 | 0.3929 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret616_neg_at_h` | one_head_filter_pi_star | 181 | 14.7860 | 2.2429 | 0.7182 | 4.8301 | 0.0255 | 0.3646 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret616_neg_at_h` | one_head_filter_pi_star | 230 | 18.8073 | 1.8174 | 0.6435 | 3.8233 | 0.0134 | 0.3217 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret616_neg_at_h` | one_head_filter_pi_star | 221 | 18.0714 | 1.8187 | 0.6471 | 3.7315 | 0.0134 | 0.3303 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ret616_pos_at_h` | one_head_filter_pi_star | 104 | 8.6442 | 1.7384 | 0.6442 | 2.3663 | 0.0091 | 0.2500 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret616_pos_at_h` | one_head_filter_pi_star | 136 | 11.0901 | 1.5060 | 0.6103 | 1.9344 | 0.0072 | 0.2794 | ok | RAN |
| ETHUSDT | 4 | `ret616_pos_at_h` | one_head_filter_pi_star | 150 | 12.3298 | 1.1441 | 0.5733 | 0.6911 | 0.0059 | 0.2333 | ok | RAN |
| ETHUSDT | 8 | `ret616_pos_at_h` | one_head_filter_pi_star | 175 | 14.3848 | 1.1058 | 0.5600 | 0.5608 | 0.0044 | 0.2457 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret616_pos_at_h` | one_head_filter_pi_star | 15 | 1.2765 | 0.7035 | 0.3333 | -0.5130 | -0.0271 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret616_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4385 | 0.2222 | -1.2856 | -0.0638 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret616_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret616_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret616_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret616_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret616_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret616_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret616_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret616_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret616_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret616_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret616_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret616_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret616_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret616_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
