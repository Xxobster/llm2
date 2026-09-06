# Autonomy public-indicator hunt gen 677

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T053339Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret117_neg_at_h` | one_head_filter_pi_star | 199 | 16.2565 | 1.8053 | 0.6784 | 3.8911 | 0.0204 | 0.3668 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret117_neg_at_h` | one_head_filter_pi_star | 187 | 15.2762 | 1.8054 | 0.6791 | 3.8724 | 0.0202 | 0.3636 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret117_neg_at_h` | one_head_filter_pi_star | 184 | 15.0458 | 2.3318 | 0.7011 | 4.6534 | 0.0177 | 0.3696 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret117_neg_at_h` | one_head_filter_pi_star | 191 | 15.6182 | 2.2434 | 0.6859 | 4.5376 | 0.0169 | 0.3560 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `ret117_pos_at_h` | one_head_filter_pi_star | 174 | 14.3587 | 1.4013 | 0.6437 | 1.8478 | 0.0128 | 0.2356 | ok | RAN |
| ETHUSDT | 4 | `ret117_pos_at_h` | one_head_filter_pi_star | 201 | 16.5868 | 1.3159 | 0.6169 | 1.5460 | 0.0105 | 0.2438 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ret117_pos_at_h` | one_head_filter_pi_star | 176 | 14.3511 | 1.3806 | 0.6023 | 1.9012 | 0.0063 | 0.2614 | ok | RAN |
| SOLUSDT | 8 | `ret117_pos_at_h` | one_head_filter_pi_star | 175 | 14.2696 | 1.3699 | 0.5943 | 1.7986 | 0.0062 | 0.2629 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret117_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret117_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5773 | 0.2941 | -0.8964 | -0.0475 | 0.0588 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret117_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret117_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 8 | `ret117_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret117_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `ret117_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret117_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret117_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret117_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret117_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret117_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret117_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret117_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret117_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret117_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
