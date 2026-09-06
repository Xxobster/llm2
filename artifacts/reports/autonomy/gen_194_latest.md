# Autonomy public-indicator hunt gen 194

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T221017Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret88_neg_at_h` | one_head_filter_pi_star | 196 | 16.0114 | 1.9021 | 0.6684 | 4.1436 | 0.0219 | 0.3724 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret88_neg_at_h` | one_head_filter_pi_star | 199 | 16.2565 | 1.7953 | 0.6683 | 3.8300 | 0.0202 | 0.3668 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret88_neg_at_h` | one_head_filter_pi_star | 184 | 15.0458 | 2.1964 | 0.6739 | 4.3282 | 0.0166 | 0.3641 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret88_neg_at_h` | one_head_filter_pi_star | 189 | 15.4547 | 2.2014 | 0.6825 | 4.3685 | 0.0164 | 0.3545 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ret88_pos_at_h` | one_head_filter_pi_star | 189 | 15.5356 | 1.2928 | 0.6243 | 1.4469 | 0.0095 | 0.2275 | ok | RAN |
| ETHUSDT | 4 | `ret88_pos_at_h` | one_head_filter_pi_star | 184 | 15.1246 | 1.1910 | 0.6087 | 0.9943 | 0.0065 | 0.2174 | ok | RAN |
| SOLUSDT | 8 | `ret88_pos_at_h` | one_head_filter_pi_star | 195 | 15.9004 | 1.3836 | 0.6051 | 1.9447 | 0.0062 | 0.2718 | ok | RAN |
| SOLUSDT | 4 | `ret88_pos_at_h` | one_head_filter_pi_star | 191 | 15.5742 | 1.3632 | 0.6021 | 1.8710 | 0.0059 | 0.2565 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret88_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret88_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret88_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret88_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret88_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret88_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret88_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret88_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret88_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret88_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret88_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret88_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret88_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret88_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret88_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret88_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
