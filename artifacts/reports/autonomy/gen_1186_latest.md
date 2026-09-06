# Autonomy public-indicator hunt gen 1186

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T085835Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret1040_neg_at_h` | one_head_filter_pi_star | 283 | 23.1185 | 1.7506 | 0.6572 | 4.0882 | 0.0180 | 0.3322 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ret1040_neg_at_h` | one_head_filter_pi_star | 283 | 23.1185 | 1.7128 | 0.6537 | 3.9663 | 0.0175 | 0.3322 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret1040_pos_at_h` | one_head_filter_pi_star | 42 | 3.4913 | 1.8813 | 0.7381 | 1.7730 | 0.0118 | 0.3571 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret1040_neg_at_h` | one_head_filter_pi_star | 293 | 23.8361 | 1.7643 | 0.6348 | 4.0440 | 0.0114 | 0.3140 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret1040_neg_at_h` | one_head_filter_pi_star | 306 | 24.8937 | 1.7310 | 0.6340 | 4.0010 | 0.0112 | 0.3170 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret1040_pos_at_h` | one_head_filter_pi_star | 53 | 4.3470 | 1.6136 | 0.6792 | 1.3961 | 0.0086 | 0.2642 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1040_pos_at_h` | one_head_filter_pi_star | 70 | 5.9924 | 1.0133 | 0.5571 | 0.0482 | 0.0007 | 0.2143 | ok | RAN |
| ETHUSDT | 8 | `ret1040_pos_at_h` | one_head_filter_pi_star | 43 | 3.8431 | 0.9081 | 0.5581 | -0.2813 | -0.0051 | 0.2558 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret1040_pos_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.3096 | 0.2500 | -1.6294 | -0.0747 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret1040_pos_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.3096 | 0.2500 | -1.6294 | -0.0793 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1040_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret1040_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1040_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1040_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1040_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1040_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1040_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1040_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1040_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1040_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1040_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1040_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret1040_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1040_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
