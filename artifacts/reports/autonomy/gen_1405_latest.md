# Autonomy public-indicator hunt gen 1405

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260830T062106Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret244_neg_at_h` | one_head_filter_pi_star | 177 | 14.4593 | 1.9579 | 0.6836 | 4.0409 | 0.0233 | 0.3672 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret244_neg_at_h` | one_head_filter_pi_star | 178 | 14.5410 | 1.8952 | 0.6854 | 3.9586 | 0.0221 | 0.3708 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret244_neg_at_h` | one_head_filter_pi_star | 177 | 14.4734 | 1.8988 | 0.6497 | 3.6309 | 0.0137 | 0.3559 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret244_neg_at_h` | one_head_filter_pi_star | 182 | 14.8823 | 1.8849 | 0.6484 | 3.6711 | 0.0130 | 0.3462 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ret244_pos_at_h` | one_head_filter_pi_star | 168 | 13.6988 | 1.5613 | 0.6190 | 2.4292 | 0.0086 | 0.2857 | ok | RAN |
| ETHUSDT | 4 | `ret244_pos_at_h` | one_head_filter_pi_star | 187 | 15.3712 | 1.2349 | 0.6043 | 1.2058 | 0.0084 | 0.2567 | ok | RAN |
| SOLUSDT | 8 | `ret244_pos_at_h` | one_head_filter_pi_star | 185 | 15.0850 | 1.5050 | 0.6216 | 2.3414 | 0.0078 | 0.2811 | ok | RAN |
| ETHUSDT | 8 | `ret244_pos_at_h` | one_head_filter_pi_star | 184 | 15.1246 | 1.2029 | 0.5978 | 1.0130 | 0.0070 | 0.2174 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret244_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret244_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0451 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret244_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret244_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret244_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret244_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret244_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret244_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret244_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret244_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret244_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret244_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret244_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret244_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret244_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret244_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
