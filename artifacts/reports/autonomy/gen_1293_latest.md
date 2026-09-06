# Autonomy public-indicator hunt gen 1293

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T193012Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret228_neg_at_h` | one_head_filter_pi_star | 181 | 14.7860 | 2.3452 | 0.7238 | 5.1278 | 0.0295 | 0.3923 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret228_neg_at_h` | one_head_filter_pi_star | 164 | 13.3973 | 2.2901 | 0.7134 | 4.8626 | 0.0286 | 0.4146 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret228_neg_at_h` | one_head_filter_pi_star | 199 | 16.2724 | 2.0087 | 0.6633 | 4.1153 | 0.0143 | 0.3518 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret228_neg_at_h` | one_head_filter_pi_star | 184 | 15.0458 | 1.6774 | 0.6304 | 2.9684 | 0.0103 | 0.3424 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ret228_pos_at_h` | one_head_filter_pi_star | 190 | 15.6178 | 1.2462 | 0.6053 | 1.1953 | 0.0086 | 0.2211 | ok | RAN |
| SOLUSDT | 4 | `ret228_pos_at_h` | one_head_filter_pi_star | 182 | 14.8404 | 1.5587 | 0.6264 | 2.4985 | 0.0084 | 0.2747 | ok | RAN |
| SOLUSDT | 8 | `ret228_pos_at_h` | one_head_filter_pi_star | 174 | 14.1880 | 1.5157 | 0.6207 | 2.3102 | 0.0080 | 0.2759 | ok | RAN |
| ETHUSDT | 8 | `ret228_pos_at_h` | one_head_filter_pi_star | 191 | 15.7000 | 1.0675 | 0.5654 | 0.3551 | 0.0026 | 0.2199 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret228_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret228_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5834 | 0.3333 | -0.8834 | -0.0450 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret228_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret228_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret228_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret228_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret228_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret228_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret228_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret228_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret228_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret228_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret228_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret228_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret228_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret228_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
