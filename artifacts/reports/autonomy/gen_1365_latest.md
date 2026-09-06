# Autonomy public-indicator hunt gen 1365

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260830T022448Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret238_neg_at_h` | one_head_filter_pi_star | 168 | 13.7241 | 2.2267 | 0.7083 | 4.7518 | 0.0270 | 0.3810 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret238_neg_at_h` | one_head_filter_pi_star | 162 | 13.2339 | 2.0090 | 0.6975 | 4.0737 | 0.0247 | 0.3951 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret238_neg_at_h` | one_head_filter_pi_star | 200 | 16.3542 | 1.9165 | 0.6600 | 3.8747 | 0.0136 | 0.3350 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret238_neg_at_h` | one_head_filter_pi_star | 200 | 16.3542 | 1.8559 | 0.6550 | 3.6264 | 0.0132 | 0.3500 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ret238_pos_at_h` | one_head_filter_pi_star | 175 | 14.2696 | 1.5087 | 0.6171 | 2.2629 | 0.0077 | 0.2743 | ok | RAN |
| ETHUSDT | 8 | `ret238_pos_at_h` | one_head_filter_pi_star | 181 | 14.8780 | 1.1948 | 0.5912 | 0.9899 | 0.0070 | 0.2210 | ok | RAN |
| SOLUSDT | 8 | `ret238_pos_at_h` | one_head_filter_pi_star | 174 | 14.1880 | 1.4009 | 0.5977 | 1.8810 | 0.0063 | 0.2816 | ok | RAN |
| ETHUSDT | 4 | `ret238_pos_at_h` | one_head_filter_pi_star | 191 | 15.7000 | 1.1661 | 0.5916 | 0.8538 | 0.0060 | 0.2356 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret238_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0418 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret238_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret238_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret238_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret238_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret238_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret238_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret238_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret238_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret238_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret238_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret238_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret238_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret238_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret238_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret238_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
