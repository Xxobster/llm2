# Autonomy public-indicator hunt gen 589

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T234910Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret95_neg_at_h` | one_head_filter_pi_star | 190 | 15.5213 | 1.8288 | 0.6684 | 3.8751 | 0.0210 | 0.3789 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret95_neg_at_h` | one_head_filter_pi_star | 205 | 16.7466 | 1.8120 | 0.6585 | 3.9965 | 0.0207 | 0.3610 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret95_neg_at_h` | one_head_filter_pi_star | 185 | 15.1276 | 2.1925 | 0.6757 | 4.3520 | 0.0166 | 0.3676 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret95_neg_at_h` | one_head_filter_pi_star | 180 | 14.7188 | 2.0776 | 0.6667 | 3.9643 | 0.0155 | 0.3667 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `ret95_pos_at_h` | one_head_filter_pi_star | 170 | 14.0286 | 1.3502 | 0.6294 | 1.6787 | 0.0116 | 0.2294 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ret95_pos_at_h` | one_head_filter_pi_star | 185 | 15.2068 | 1.2436 | 0.6162 | 1.2231 | 0.0082 | 0.2270 | ok | RAN |
| SOLUSDT | 4 | `ret95_pos_at_h` | one_head_filter_pi_star | 188 | 15.3296 | 1.4026 | 0.6064 | 2.0228 | 0.0063 | 0.2606 | ok | RAN |
| SOLUSDT | 8 | `ret95_pos_at_h` | one_head_filter_pi_star | 183 | 14.9219 | 1.3491 | 0.5956 | 1.7658 | 0.0056 | 0.2568 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret95_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret95_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret95_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret95_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret95_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret95_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret95_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret95_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret95_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret95_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret95_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret95_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret95_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret95_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret95_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret95_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
