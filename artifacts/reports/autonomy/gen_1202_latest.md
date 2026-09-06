# Autonomy public-indicator hunt gen 1202

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T102740Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret1056_neg_at_h` | one_head_filter_pi_star | 284 | 23.2002 | 1.7564 | 0.6549 | 4.0209 | 0.0185 | 0.3310 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ret1056_neg_at_h` | one_head_filter_pi_star | 307 | 25.0791 | 1.7060 | 0.6547 | 4.1252 | 0.0180 | 0.3192 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret1056_neg_at_h` | one_head_filter_pi_star | 287 | 23.4682 | 1.9259 | 0.6481 | 4.5212 | 0.0131 | 0.3240 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret1056_neg_at_h` | one_head_filter_pi_star | 291 | 23.7953 | 1.8603 | 0.6495 | 4.4744 | 0.0127 | 0.3127 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ret1056_pos_at_h` | one_head_filter_pi_star | 41 | 3.4082 | 1.4956 | 0.6585 | 1.2270 | 0.0085 | 0.2927 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ret1056_pos_at_h` | one_head_filter_pi_star | 27 | 2.3779 | 1.5046 | 0.6667 | 0.9918 | 0.0071 | 0.2963 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret1056_pos_at_h` | one_head_filter_pi_star | 53 | 4.7368 | 0.9572 | 0.5283 | -0.1444 | -0.0026 | 0.2642 | ok | RAN |
| BTCUSDT | 4 | `ret1056_pos_at_h` | one_head_filter_pi_star | 13 | 1.1063 | 0.4649 | 0.3077 | -1.0012 | -0.0466 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret1056_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.3497 | 0.2941 | -1.4502 | -0.0623 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1056_pos_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret1056_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret1056_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1056_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1056_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1056_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1056_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1056_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1056_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1056_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret1056_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1056_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1056_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret1056_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1056_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
