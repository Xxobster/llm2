# Autonomy public-indicator hunt gen 1306

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T205715Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ret1160_pos_at_h` | one_head_filter_pi_star | 17 | 1.4310 | 2.4102 | 0.7647 | 1.5047 | 0.0221 | 0.2941 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1160_neg_at_h` | one_head_filter_pi_star | 329 | 26.7648 | 1.6380 | 0.6474 | 3.9315 | 0.0167 | 0.3100 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret1160_neg_at_h` | one_head_filter_pi_star | 318 | 25.9777 | 1.6162 | 0.6478 | 3.6996 | 0.0160 | 0.3239 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret1160_neg_at_h` | one_head_filter_pi_star | 334 | 27.1716 | 1.7160 | 0.6377 | 4.0776 | 0.0109 | 0.3263 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret1160_neg_at_h` | one_head_filter_pi_star | 332 | 27.0089 | 1.6879 | 0.6295 | 3.9807 | 0.0108 | 0.3193 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret1160_pos_at_h` | one_head_filter_pi_star | 39 | 3.5871 | 0.9026 | 0.4872 | -0.2856 | -0.0044 | 0.2821 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1160_pos_at_h` | one_head_filter_pi_star | 45 | 4.4180 | 0.8025 | 0.4889 | -0.6861 | -0.0107 | 0.2000 | ok | RAN |
| BTCUSDT | 4 | `ret1160_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0545 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret1160_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.3142 | 0.2222 | -1.6016 | -0.0679 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1160_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret1160_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1160_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1160_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1160_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1160_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1160_pos_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 8 | `ret1160_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1160_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1160_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret1160_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1160_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1160_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret1160_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1160_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
