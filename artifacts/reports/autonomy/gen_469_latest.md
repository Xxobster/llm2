# Autonomy public-indicator hunt gen 469

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T155408Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret65_neg_at_h` | one_head_filter_pi_star | 194 | 15.8480 | 1.7196 | 0.6753 | 3.5660 | 0.0198 | 0.3763 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret65_neg_at_h` | one_head_filter_pi_star | 179 | 14.6370 | 2.4604 | 0.6983 | 4.7869 | 0.0190 | 0.3911 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret65_neg_at_h` | one_head_filter_pi_star | 170 | 13.9010 | 2.3703 | 0.7059 | 4.5398 | 0.0190 | 0.4059 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret65_neg_at_h` | one_head_filter_pi_star | 195 | 15.9297 | 1.6959 | 0.6615 | 3.5716 | 0.0185 | 0.3692 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `ret65_pos_at_h` | one_head_filter_pi_star | 187 | 15.3712 | 1.4042 | 0.6257 | 1.9429 | 0.0124 | 0.2353 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ret65_pos_at_h` | one_head_filter_pi_star | 177 | 14.5492 | 1.3092 | 0.6102 | 1.4864 | 0.0098 | 0.2429 | ok | RAN |
| SOLUSDT | 8 | `ret65_pos_at_h` | one_head_filter_pi_star | 193 | 15.7373 | 1.3627 | 0.6010 | 1.8685 | 0.0054 | 0.2591 | ok | RAN |
| SOLUSDT | 4 | `ret65_pos_at_h` | one_head_filter_pi_star | 204 | 16.6342 | 1.2874 | 0.5980 | 1.5568 | 0.0046 | 0.2500 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret65_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret65_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret65_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret65_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret65_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret65_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret65_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret65_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret65_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret65_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret65_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret65_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret65_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret65_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret65_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret65_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
