# Autonomy public-indicator hunt gen 957

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260826T074810Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret187_neg_at_h` | one_head_filter_pi_star | 165 | 13.4790 | 2.0810 | 0.7091 | 4.4251 | 0.0250 | 0.4061 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret187_neg_at_h` | one_head_filter_pi_star | 177 | 14.4593 | 1.9289 | 0.6836 | 4.0149 | 0.0224 | 0.3785 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret187_neg_at_h` | one_head_filter_pi_star | 173 | 14.1464 | 1.9635 | 0.6590 | 3.6691 | 0.0141 | 0.3584 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret187_neg_at_h` | one_head_filter_pi_star | 172 | 14.0646 | 1.8735 | 0.6570 | 3.4016 | 0.0135 | 0.3663 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ret187_pos_at_h` | one_head_filter_pi_star | 191 | 15.7000 | 1.2218 | 0.5969 | 1.1552 | 0.0074 | 0.2251 | ok | RAN |
| SOLUSDT | 4 | `ret187_pos_at_h` | one_head_filter_pi_star | 206 | 16.7973 | 1.4613 | 0.6117 | 2.2759 | 0.0070 | 0.2670 | ok | RAN |
| SOLUSDT | 8 | `ret187_pos_at_h` | one_head_filter_pi_star | 211 | 17.2050 | 1.4073 | 0.6066 | 2.0845 | 0.0065 | 0.2512 | ok | RAN |
| ETHUSDT | 8 | `ret187_pos_at_h` | one_head_filter_pi_star | 205 | 16.7875 | 1.1531 | 0.5854 | 0.8660 | 0.0054 | 0.2244 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret187_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5765 | 0.2778 | -0.8994 | -0.0449 | 0.0556 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret187_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5773 | 0.2941 | -0.8964 | -0.0465 | 0.0588 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret187_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret187_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret187_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret187_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret187_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret187_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret187_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret187_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret187_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret187_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret187_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret187_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret187_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret187_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
