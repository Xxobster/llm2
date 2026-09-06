# Autonomy public-indicator hunt gen 786

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T142328Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret640_neg_at_h` | one_head_filter_pi_star | 173 | 14.1325 | 2.1619 | 0.7110 | 4.3857 | 0.0241 | 0.3815 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret640_neg_at_h` | one_head_filter_pi_star | 219 | 17.8903 | 1.8913 | 0.6849 | 4.2388 | 0.0208 | 0.3379 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret640_neg_at_h` | one_head_filter_pi_star | 214 | 17.8029 | 1.8352 | 0.6542 | 3.7366 | 0.0141 | 0.3318 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret640_neg_at_h` | one_head_filter_pi_star | 211 | 17.2537 | 1.8100 | 0.6588 | 3.6303 | 0.0137 | 0.3175 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ret640_pos_at_h` | one_head_filter_pi_star | 95 | 7.7909 | 1.6569 | 0.6632 | 2.1008 | 0.0087 | 0.2526 | ok | RAN |
| SOLUSDT | 8 | `ret640_pos_at_h` | one_head_filter_pi_star | 105 | 8.6306 | 1.6006 | 0.6476 | 2.0629 | 0.0080 | 0.2571 | ok | RAN |
| ETHUSDT | 8 | `ret640_pos_at_h` | one_head_filter_pi_star | 173 | 14.2204 | 1.1722 | 0.5665 | 0.8665 | 0.0068 | 0.2254 | ok | RAN |
| ETHUSDT | 4 | `ret640_pos_at_h` | one_head_filter_pi_star | 154 | 12.6586 | 1.0434 | 0.5455 | 0.2273 | 0.0018 | 0.2338 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret640_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4688 | 0.2778 | -1.1839 | -0.0565 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret640_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4605 | 0.2353 | -1.1826 | -0.0595 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret640_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret640_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret640_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret640_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret640_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret640_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret640_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret640_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret640_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret640_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret640_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret640_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret640_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret640_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
