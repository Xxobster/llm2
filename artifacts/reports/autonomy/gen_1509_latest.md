# Autonomy public-indicator hunt gen 1509

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260831T033727Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret259_neg_at_h` | one_head_filter_pi_star | 168 | 13.7241 | 2.1816 | 0.6964 | 4.3552 | 0.0262 | 0.3869 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret259_neg_at_h` | one_head_filter_pi_star | 172 | 14.0508 | 2.0293 | 0.6802 | 4.3307 | 0.0247 | 0.3895 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret259_neg_at_h` | one_head_filter_pi_star | 177 | 14.5693 | 2.0043 | 0.6780 | 3.8790 | 0.0151 | 0.3616 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret259_neg_at_h` | one_head_filter_pi_star | 184 | 15.0458 | 1.8793 | 0.6630 | 3.5851 | 0.0136 | 0.3587 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret259_pos_at_h` | one_head_filter_pi_star | 172 | 14.1048 | 1.4794 | 0.5988 | 2.1294 | 0.0077 | 0.2907 | ok | RAN |
| SOLUSDT | 4 | `ret259_pos_at_h` | one_head_filter_pi_star | 164 | 13.4488 | 1.4765 | 0.5976 | 2.1423 | 0.0075 | 0.2866 | ok | RAN |
| ETHUSDT | 8 | `ret259_pos_at_h` | one_head_filter_pi_star | 174 | 14.3026 | 1.2077 | 0.5977 | 1.0284 | 0.0069 | 0.2184 | ok | RAN |
| ETHUSDT | 4 | `ret259_pos_at_h` | one_head_filter_pi_star | 184 | 15.1246 | 1.1697 | 0.5924 | 0.8769 | 0.0059 | 0.2174 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret259_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0418 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret259_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret259_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret259_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret259_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret259_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret259_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret259_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret259_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret259_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret259_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret259_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret259_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret259_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret259_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret259_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
