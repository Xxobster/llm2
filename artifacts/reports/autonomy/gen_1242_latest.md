# Autonomy public-indicator hunt gen 1242

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T143756Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret1096_neg_at_h` | one_head_filter_pi_star | 287 | 23.4453 | 1.7158 | 0.6551 | 4.0119 | 0.0175 | 0.3310 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret1096_neg_at_h` | one_head_filter_pi_star | 294 | 24.0171 | 1.6648 | 0.6497 | 3.8478 | 0.0165 | 0.3299 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret1096_neg_at_h` | one_head_filter_pi_star | 318 | 26.0031 | 1.7120 | 0.6352 | 3.9671 | 0.0112 | 0.3239 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret1096_neg_at_h` | one_head_filter_pi_star | 287 | 23.4682 | 1.6733 | 0.6307 | 3.6227 | 0.0108 | 0.3240 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ret1096_pos_at_h` | one_head_filter_pi_star | 19 | 1.7741 | 1.6092 | 0.7368 | 0.9483 | 0.0085 | 0.2105 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1096_pos_at_h` | one_head_filter_pi_star | 13 | 1.2763 | 1.1407 | 0.5385 | 0.2380 | 0.0065 | 0.5385 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret1096_pos_at_h` | one_head_filter_pi_star | 32 | 2.7208 | 1.3534 | 0.6562 | 0.7453 | 0.0057 | 0.2500 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret1096_pos_at_h` | one_head_filter_pi_star | 40 | 3.7442 | 0.8687 | 0.5250 | -0.3920 | -0.0072 | 0.2250 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret1096_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.3092 | 0.2353 | -1.6326 | -0.0707 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret1096_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.3092 | 0.2353 | -1.6326 | -0.0778 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1096_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret1096_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1096_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1096_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1096_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1096_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1096_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1096_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1096_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret1096_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1096_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1096_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret1096_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1096_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
