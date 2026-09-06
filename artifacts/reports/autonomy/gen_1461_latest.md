# Autonomy public-indicator hunt gen 1461

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260830T225812Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret252_neg_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 2.1306 | 0.7090 | 4.7820 | 0.0256 | 0.3651 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret252_neg_at_h` | one_head_filter_pi_star | 176 | 14.3776 | 2.0827 | 0.6989 | 4.2226 | 0.0251 | 0.3807 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret252_neg_at_h` | one_head_filter_pi_star | 174 | 14.2281 | 2.0610 | 0.6667 | 3.9067 | 0.0151 | 0.3621 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret252_neg_at_h` | one_head_filter_pi_star | 189 | 15.4547 | 1.8289 | 0.6561 | 3.4971 | 0.0127 | 0.3598 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ret252_pos_at_h` | one_head_filter_pi_star | 190 | 15.4927 | 1.5880 | 0.6263 | 2.7053 | 0.0091 | 0.2737 | ok | RAN |
| SOLUSDT | 8 | `ret252_pos_at_h` | one_head_filter_pi_star | 180 | 14.6773 | 1.5208 | 0.6278 | 2.3522 | 0.0080 | 0.2778 | ok | RAN |
| ETHUSDT | 4 | `ret252_pos_at_h` | one_head_filter_pi_star | 190 | 15.6178 | 1.1884 | 0.6053 | 0.9781 | 0.0066 | 0.2263 | ok | RAN |
| ETHUSDT | 8 | `ret252_pos_at_h` | one_head_filter_pi_star | 173 | 14.2204 | 1.1449 | 0.5954 | 0.7270 | 0.0053 | 0.2312 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret252_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.6188 | 0.3684 | -0.7870 | -0.0371 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret252_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5834 | 0.3333 | -0.8834 | -0.0441 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret252_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret252_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret252_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret252_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret252_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret252_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret252_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret252_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret252_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret252_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret252_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret252_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret252_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret252_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
