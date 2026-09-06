# Autonomy public-indicator hunt gen 1277

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T180140Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret226_neg_at_h` | one_head_filter_pi_star | 161 | 13.1522 | 2.1387 | 0.7081 | 4.4316 | 0.0268 | 0.4099 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret226_neg_at_h` | one_head_filter_pi_star | 161 | 13.1522 | 2.0696 | 0.7019 | 4.3009 | 0.0248 | 0.3975 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret226_neg_at_h` | one_head_filter_pi_star | 175 | 14.3099 | 1.9847 | 0.6629 | 3.7777 | 0.0142 | 0.3714 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret226_neg_at_h` | one_head_filter_pi_star | 191 | 15.6182 | 1.9244 | 0.6649 | 3.7858 | 0.0131 | 0.3613 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret226_pos_at_h` | one_head_filter_pi_star | 182 | 14.9249 | 1.5943 | 0.6374 | 2.6438 | 0.0091 | 0.2747 | ok | RAN |
| SOLUSDT | 4 | `ret226_pos_at_h` | one_head_filter_pi_star | 175 | 14.2696 | 1.5388 | 0.6286 | 2.3706 | 0.0081 | 0.2800 | ok | RAN |
| ETHUSDT | 4 | `ret226_pos_at_h` | one_head_filter_pi_star | 188 | 15.4534 | 1.1646 | 0.5904 | 0.8650 | 0.0058 | 0.2234 | ok | RAN |
| ETHUSDT | 8 | `ret226_pos_at_h` | one_head_filter_pi_star | 193 | 15.8644 | 1.1429 | 0.5803 | 0.7579 | 0.0053 | 0.2332 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret226_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5834 | 0.3333 | -0.8834 | -0.0433 | 0.0556 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret226_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret226_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret226_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret226_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret226_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret226_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret226_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret226_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret226_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret226_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret226_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret226_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret226_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret226_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret226_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
