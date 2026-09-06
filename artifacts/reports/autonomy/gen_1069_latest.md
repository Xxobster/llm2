# Autonomy public-indicator hunt gen 1069

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T191113Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret194_neg_at_h` | one_head_filter_pi_star | 157 | 12.8255 | 2.4819 | 0.7197 | 5.1437 | 0.0305 | 0.4204 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret194_neg_at_h` | one_head_filter_pi_star | 180 | 14.7044 | 1.9333 | 0.6889 | 4.1266 | 0.0218 | 0.3722 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret194_neg_at_h` | one_head_filter_pi_star | 170 | 13.9010 | 2.1333 | 0.6882 | 4.0092 | 0.0163 | 0.3765 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret194_neg_at_h` | one_head_filter_pi_star | 178 | 14.5552 | 2.0602 | 0.6742 | 4.0004 | 0.0154 | 0.3539 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ret194_pos_at_h` | one_head_filter_pi_star | 204 | 16.6342 | 1.4958 | 0.6127 | 2.4367 | 0.0077 | 0.2745 | ok | RAN |
| SOLUSDT | 8 | `ret194_pos_at_h` | one_head_filter_pi_star | 183 | 15.0069 | 1.4210 | 0.6175 | 2.0312 | 0.0067 | 0.2732 | ok | RAN |
| ETHUSDT | 4 | `ret194_pos_at_h` | one_head_filter_pi_star | 201 | 16.5219 | 1.1838 | 0.5920 | 0.9902 | 0.0065 | 0.2189 | ok | RAN |
| ETHUSDT | 8 | `ret194_pos_at_h` | one_head_filter_pi_star | 194 | 15.9466 | 1.1639 | 0.5928 | 0.8570 | 0.0057 | 0.2216 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret194_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0411 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret194_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5773 | 0.2941 | -0.8964 | -0.0465 | 0.0588 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret194_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret194_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret194_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret194_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret194_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret194_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret194_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret194_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret194_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret194_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret194_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret194_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret194_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret194_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
