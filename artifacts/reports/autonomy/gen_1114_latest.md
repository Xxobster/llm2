# Autonomy public-indicator hunt gen 1114

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T004503Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret968_neg_at_h` | one_head_filter_pi_star | 201 | 16.4199 | 1.8826 | 0.6866 | 3.8156 | 0.0219 | 0.3980 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret968_neg_at_h` | one_head_filter_pi_star | 238 | 19.4424 | 1.7270 | 0.6597 | 3.7475 | 0.0181 | 0.3487 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret968_neg_at_h` | one_head_filter_pi_star | 266 | 21.7510 | 1.9078 | 0.6429 | 4.3012 | 0.0133 | 0.3346 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret968_neg_at_h` | one_head_filter_pi_star | 275 | 22.4870 | 1.8508 | 0.6509 | 4.1343 | 0.0132 | 0.3236 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret968_pos_at_h` | one_head_filter_pi_star | 69 | 5.8058 | 1.3026 | 0.6377 | 0.9580 | 0.0119 | 0.2174 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ret968_pos_at_h` | one_head_filter_pi_star | 19 | 1.9582 | 1.4588 | 0.5789 | 0.7626 | 0.0082 | 0.2105 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret968_pos_at_h` | one_head_filter_pi_star | 62 | 5.4523 | 1.1120 | 0.5806 | 0.3775 | 0.0050 | 0.2258 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ret968_pos_at_h` | one_head_filter_pi_star | 14 | 1.4590 | 1.0373 | 0.5000 | 0.0599 | 0.0006 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret968_pos_at_h` | one_head_filter_pi_star | 15 | 1.2765 | 0.4398 | 0.2667 | -1.1347 | -0.0480 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret968_pos_at_h` | one_head_filter_pi_star | 14 | 1.1914 | 0.3630 | 0.2857 | -1.3526 | -0.0690 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret968_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret968_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret968_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret968_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret968_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret968_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret968_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret968_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret968_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret968_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret968_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret968_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret968_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret968_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
