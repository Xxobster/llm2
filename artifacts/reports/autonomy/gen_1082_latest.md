# Autonomy public-indicator hunt gen 1082

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T204447Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret936_neg_at_h` | one_head_filter_pi_star | 244 | 19.9326 | 1.8274 | 0.6721 | 4.0279 | 0.0203 | 0.3566 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret936_pos_at_h` | one_head_filter_pi_star | 59 | 4.8721 | 2.6978 | 0.7458 | 3.2593 | 0.0194 | 0.2881 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret936_neg_at_h` | one_head_filter_pi_star | 282 | 22.9413 | 1.7682 | 0.6560 | 4.1701 | 0.0186 | 0.3369 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret936_neg_at_h` | one_head_filter_pi_star | 267 | 21.8640 | 1.9640 | 0.6554 | 4.4234 | 0.0138 | 0.3221 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret936_neg_at_h` | one_head_filter_pi_star | 243 | 19.8987 | 1.9685 | 0.6502 | 4.3253 | 0.0135 | 0.3374 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret936_pos_at_h` | one_head_filter_pi_star | 34 | 2.9181 | 1.7996 | 0.7059 | 1.4618 | 0.0100 | 0.2353 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ret936_pos_at_h` | one_head_filter_pi_star | 55 | 4.8367 | 1.1748 | 0.6182 | 0.5646 | 0.0081 | 0.2909 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret936_pos_at_h` | one_head_filter_pi_star | 49 | 4.3091 | 1.0010 | 0.5714 | 0.0035 | 0.0001 | 0.2653 | ok | RAN |
| BTCUSDT | 4 | `ret936_pos_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.5266 | 0.3125 | -0.9530 | -0.0516 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret936_pos_at_h` | one_head_filter_pi_star | 15 | 1.2765 | 0.3037 | 0.2000 | -1.6437 | -0.0833 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret936_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret936_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret936_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret936_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret936_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret936_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret936_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret936_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret936_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret936_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret936_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret936_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret936_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret936_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
