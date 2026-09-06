# Autonomy public-indicator hunt gen 1213

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T113627Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret217_neg_at_h` | one_head_filter_pi_star | 156 | 12.7438 | 2.3237 | 0.7115 | 4.6979 | 0.0294 | 0.4295 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret217_neg_at_h` | one_head_filter_pi_star | 175 | 14.2959 | 2.2783 | 0.7143 | 5.0075 | 0.0277 | 0.4057 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret217_neg_at_h` | one_head_filter_pi_star | 189 | 15.4703 | 1.9588 | 0.6667 | 3.8675 | 0.0143 | 0.3704 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret217_neg_at_h` | one_head_filter_pi_star | 188 | 15.3729 | 1.8537 | 0.6543 | 3.5786 | 0.0135 | 0.3777 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret217_pos_at_h` | one_head_filter_pi_star | 168 | 13.6988 | 1.5452 | 0.6131 | 2.3916 | 0.0081 | 0.2917 | ok | RAN |
| ETHUSDT | 4 | `ret217_pos_at_h` | one_head_filter_pi_star | 193 | 15.8644 | 1.2157 | 0.5959 | 1.0862 | 0.0073 | 0.2280 | ok | RAN |
| SOLUSDT | 4 | `ret217_pos_at_h` | one_head_filter_pi_star | 168 | 13.6988 | 1.4657 | 0.6071 | 2.0989 | 0.0071 | 0.2917 | ok | RAN |
| ETHUSDT | 8 | `ret217_pos_at_h` | one_head_filter_pi_star | 206 | 16.9329 | 1.1436 | 0.5825 | 0.7654 | 0.0050 | 0.2233 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret217_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5834 | 0.3333 | -0.8834 | -0.0450 | 0.0556 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret217_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5773 | 0.2941 | -0.8964 | -0.0465 | 0.0588 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret217_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret217_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret217_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret217_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret217_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret217_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret217_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret217_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret217_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret217_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret217_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret217_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret217_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret217_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
