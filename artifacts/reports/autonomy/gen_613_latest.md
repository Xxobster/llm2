# Autonomy public-indicator hunt gen 613

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T012122Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret101_neg_at_h` | one_head_filter_pi_star | 190 | 15.5213 | 1.9303 | 0.6842 | 4.2417 | 0.0228 | 0.3684 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret101_neg_at_h` | one_head_filter_pi_star | 198 | 16.1748 | 1.7843 | 0.6616 | 3.7453 | 0.0197 | 0.3636 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret101_neg_at_h` | one_head_filter_pi_star | 168 | 13.7375 | 2.1475 | 0.6726 | 4.0502 | 0.0165 | 0.3750 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret101_neg_at_h` | one_head_filter_pi_star | 161 | 13.2032 | 2.1564 | 0.6770 | 3.9362 | 0.0162 | 0.3727 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `ret101_pos_at_h` | one_head_filter_pi_star | 177 | 14.6063 | 1.4542 | 0.6384 | 2.0735 | 0.0139 | 0.2429 | ok | RAN |
| ETHUSDT | 8 | `ret101_pos_at_h` | one_head_filter_pi_star | 179 | 14.7713 | 1.3963 | 0.6369 | 1.8215 | 0.0129 | 0.2346 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ret101_pos_at_h` | one_head_filter_pi_star | 189 | 15.4111 | 1.4186 | 0.6085 | 2.0981 | 0.0066 | 0.2646 | ok | RAN |
| SOLUSDT | 8 | `ret101_pos_at_h` | one_head_filter_pi_star | 192 | 15.6558 | 1.3384 | 0.5938 | 1.7504 | 0.0054 | 0.2604 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret101_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret101_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret101_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret101_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret101_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret101_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret101_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret101_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret101_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret101_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret101_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret101_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret101_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret101_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret101_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret101_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
