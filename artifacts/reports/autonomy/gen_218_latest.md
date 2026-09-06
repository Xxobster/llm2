# Autonomy public-indicator hunt gen 218

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T234713Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret76_neg_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 1.8975 | 0.6878 | 4.1211 | 0.0219 | 0.3862 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret76_neg_at_h` | one_head_filter_pi_star | 191 | 15.6030 | 1.7181 | 0.6649 | 3.4543 | 0.0191 | 0.3874 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret76_neg_at_h` | one_head_filter_pi_star | 183 | 14.9641 | 2.2556 | 0.6776 | 4.5531 | 0.0171 | 0.3716 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret76_neg_at_h` | one_head_filter_pi_star | 192 | 15.7000 | 2.0802 | 0.6719 | 4.2060 | 0.0156 | 0.3594 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ret76_pos_at_h` | one_head_filter_pi_star | 190 | 15.6178 | 1.2472 | 0.6158 | 1.2561 | 0.0083 | 0.2211 | ok | RAN |
| ETHUSDT | 4 | `ret76_pos_at_h` | one_head_filter_pi_star | 192 | 15.7822 | 1.2409 | 0.6146 | 1.2601 | 0.0082 | 0.2188 | ok | RAN |
| SOLUSDT | 4 | `ret76_pos_at_h` | one_head_filter_pi_star | 189 | 15.4111 | 1.4051 | 0.6085 | 2.0429 | 0.0062 | 0.2646 | ok | RAN |
| SOLUSDT | 8 | `ret76_pos_at_h` | one_head_filter_pi_star | 187 | 15.2481 | 1.3778 | 0.6043 | 1.9337 | 0.0058 | 0.2567 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret76_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0451 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret76_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5834 | 0.3333 | -0.8834 | -0.0459 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret76_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret76_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret76_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret76_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret76_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret76_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret76_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret76_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret76_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret76_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret76_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret76_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret76_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret76_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
