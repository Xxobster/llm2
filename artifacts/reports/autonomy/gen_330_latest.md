# Autonomy public-indicator hunt gen 330

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T115047Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret184_neg_at_h` | one_head_filter_pi_star | 168 | 13.7241 | 2.1540 | 0.6964 | 4.5904 | 0.0269 | 0.4107 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret184_neg_at_h` | one_head_filter_pi_star | 164 | 13.3973 | 2.1797 | 0.7012 | 4.5660 | 0.0262 | 0.3780 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret184_neg_at_h` | one_head_filter_pi_star | 166 | 13.5740 | 2.1120 | 0.6687 | 3.9446 | 0.0161 | 0.3855 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret184_neg_at_h` | one_head_filter_pi_star | 166 | 13.5740 | 2.0401 | 0.6747 | 3.8304 | 0.0152 | 0.3735 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret184_pos_at_h` | one_head_filter_pi_star | 194 | 15.8188 | 1.5082 | 0.6186 | 2.3904 | 0.0078 | 0.2629 | ok | RAN |
| ETHUSDT | 4 | `ret184_pos_at_h` | one_head_filter_pi_star | 196 | 16.1742 | 1.2132 | 0.5969 | 1.1403 | 0.0072 | 0.2347 | ok | RAN |
| SOLUSDT | 4 | `ret184_pos_at_h` | one_head_filter_pi_star | 193 | 15.7373 | 1.4163 | 0.6062 | 2.0511 | 0.0067 | 0.2642 | ok | RAN |
| ETHUSDT | 8 | `ret184_pos_at_h` | one_head_filter_pi_star | 177 | 14.6063 | 1.1811 | 0.5876 | 0.9339 | 0.0060 | 0.2090 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret184_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5765 | 0.2778 | -0.8994 | -0.0441 | 0.0556 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret184_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5773 | 0.2941 | -0.8964 | -0.0456 | 0.0588 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret184_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret184_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret184_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret184_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret184_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret184_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret184_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret184_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret184_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret184_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret184_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret184_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret184_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret184_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
