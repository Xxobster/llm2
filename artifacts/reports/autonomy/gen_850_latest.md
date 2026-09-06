# Autonomy public-indicator hunt gen 850

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T202614Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret704_neg_at_h` | one_head_filter_pi_star | 180 | 14.7044 | 2.0672 | 0.6889 | 4.0043 | 0.0220 | 0.3722 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret704_neg_at_h` | one_head_filter_pi_star | 175 | 14.2959 | 2.0958 | 0.6971 | 4.2052 | 0.0212 | 0.3543 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret704_neg_at_h` | one_head_filter_pi_star | 210 | 17.2856 | 2.0716 | 0.6667 | 4.2075 | 0.0152 | 0.3381 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret704_neg_at_h` | one_head_filter_pi_star | 228 | 18.6438 | 1.8655 | 0.6535 | 3.8239 | 0.0133 | 0.3114 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret704_pos_at_h` | one_head_filter_pi_star | 98 | 8.0365 | 1.8643 | 0.6531 | 2.4819 | 0.0107 | 0.2653 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret704_pos_at_h` | one_head_filter_pi_star | 101 | 8.2360 | 1.6298 | 0.6535 | 2.0344 | 0.0091 | 0.2772 | ok | RAN |
| ETHUSDT | 8 | `ret704_pos_at_h` | one_head_filter_pi_star | 191 | 15.6485 | 1.2140 | 0.5864 | 1.1333 | 0.0087 | 0.2304 | ok | RAN |
| ETHUSDT | 4 | `ret704_pos_at_h` | one_head_filter_pi_star | 181 | 14.8780 | 1.0676 | 0.5580 | 0.3692 | 0.0029 | 0.2265 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret704_pos_at_h` | one_head_filter_pi_star | 12 | 1.0212 | 0.7278 | 0.3333 | -0.4412 | -0.0232 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret704_pos_at_h` | one_head_filter_pi_star | 14 | 1.1914 | 0.4848 | 0.2857 | -1.0757 | -0.0658 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret704_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret704_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret704_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret704_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret704_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret704_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret704_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret704_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret704_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret704_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret704_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret704_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret704_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret704_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
