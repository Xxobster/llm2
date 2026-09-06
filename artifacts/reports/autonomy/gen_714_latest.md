# Autonomy public-indicator hunt gen 714

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T081123Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret568_neg_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 2.1867 | 0.7037 | 4.6793 | 0.0242 | 0.3598 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret568_neg_at_h` | one_head_filter_pi_star | 168 | 13.7241 | 2.1419 | 0.7024 | 4.3574 | 0.0241 | 0.3750 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret568_neg_at_h` | one_head_filter_pi_star | 186 | 15.4735 | 1.8061 | 0.6613 | 3.4349 | 0.0131 | 0.3441 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret568_neg_at_h` | one_head_filter_pi_star | 210 | 17.1719 | 1.7001 | 0.6476 | 3.2085 | 0.0114 | 0.3238 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret568_pos_at_h` | one_head_filter_pi_star | 134 | 11.0137 | 1.4342 | 0.6045 | 1.8260 | 0.0067 | 0.2910 | ok | RAN |
| SOLUSDT | 4 | `ret568_pos_at_h` | one_head_filter_pi_star | 137 | 11.2603 | 1.4344 | 0.5912 | 1.7552 | 0.0064 | 0.2847 | ok | RAN |
| ETHUSDT | 4 | `ret568_pos_at_h` | one_head_filter_pi_star | 191 | 15.7000 | 1.1620 | 0.5707 | 0.8639 | 0.0062 | 0.2251 | ok | RAN |
| ETHUSDT | 8 | `ret568_pos_at_h` | one_head_filter_pi_star | 175 | 14.3848 | 1.0617 | 0.5600 | 0.3264 | 0.0024 | 0.2229 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret568_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4748 | 0.3158 | -1.1705 | -0.0538 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret568_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4442 | 0.2632 | -1.2722 | -0.0596 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret568_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret568_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret568_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret568_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret568_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret568_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret568_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret568_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret568_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret568_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret568_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret568_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret568_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret568_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
