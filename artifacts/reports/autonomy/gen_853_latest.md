# Autonomy public-indicator hunt gen 853

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T204423Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret161_neg_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 2.0687 | 0.7037 | 4.6581 | 0.0252 | 0.3810 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret161_neg_at_h` | one_head_filter_pi_star | 174 | 14.2142 | 2.0468 | 0.6954 | 4.5334 | 0.0252 | 0.4138 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret161_neg_at_h` | one_head_filter_pi_star | 172 | 14.0646 | 2.1988 | 0.6802 | 4.2624 | 0.0169 | 0.3837 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret161_neg_at_h` | one_head_filter_pi_star | 165 | 13.4922 | 2.1129 | 0.6788 | 3.9479 | 0.0164 | 0.3697 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ret161_pos_at_h` | one_head_filter_pi_star | 196 | 15.9819 | 1.4190 | 0.6020 | 2.0911 | 0.0068 | 0.2653 | ok | RAN |
| ETHUSDT | 8 | `ret161_pos_at_h` | one_head_filter_pi_star | 189 | 15.5965 | 1.1865 | 0.5926 | 0.9807 | 0.0066 | 0.2169 | ok | RAN |
| ETHUSDT | 4 | `ret161_pos_at_h` | one_head_filter_pi_star | 196 | 16.1742 | 1.1616 | 0.5918 | 0.8651 | 0.0056 | 0.2092 | ok | RAN |
| SOLUSDT | 8 | `ret161_pos_at_h` | one_head_filter_pi_star | 195 | 15.9004 | 1.3412 | 0.5897 | 1.6982 | 0.0055 | 0.2615 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret161_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret161_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5773 | 0.2941 | -0.8964 | -0.0456 | 0.0588 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret161_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret161_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret161_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret161_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret161_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret161_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret161_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret161_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret161_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret161_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret161_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret161_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret161_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret161_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
