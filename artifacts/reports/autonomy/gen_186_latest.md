# Autonomy public-indicator hunt gen 186

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T213945Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret80_neg_at_h` | one_head_filter_pi_star | 192 | 15.6846 | 1.9125 | 0.6823 | 4.2204 | 0.0219 | 0.3698 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret80_neg_at_h` | one_head_filter_pi_star | 196 | 16.0114 | 1.8369 | 0.6684 | 3.8906 | 0.0206 | 0.3724 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret80_neg_at_h` | one_head_filter_pi_star | 182 | 14.8823 | 2.1759 | 0.6758 | 4.2578 | 0.0167 | 0.3681 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret80_neg_at_h` | one_head_filter_pi_star | 178 | 14.5552 | 2.0994 | 0.6685 | 4.0046 | 0.0153 | 0.3596 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ret80_pos_at_h` | one_head_filter_pi_star | 196 | 16.1109 | 1.2878 | 0.6173 | 1.4365 | 0.0096 | 0.2194 | ok | RAN |
| ETHUSDT | 4 | `ret80_pos_at_h` | one_head_filter_pi_star | 187 | 15.3712 | 1.2749 | 0.6150 | 1.3772 | 0.0092 | 0.2299 | ok | RAN |
| SOLUSDT | 4 | `ret80_pos_at_h` | one_head_filter_pi_star | 200 | 16.3081 | 1.4696 | 0.6150 | 2.3397 | 0.0072 | 0.2650 | ok | RAN |
| SOLUSDT | 8 | `ret80_pos_at_h` | one_head_filter_pi_star | 196 | 15.9819 | 1.4635 | 0.6173 | 2.3426 | 0.0070 | 0.2602 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret80_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret80_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0451 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret80_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret80_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret80_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret80_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret80_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret80_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret80_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret80_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret80_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret80_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret80_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret80_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret80_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret80_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
