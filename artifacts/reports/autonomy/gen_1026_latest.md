# Autonomy public-indicator hunt gen 1026

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T134919Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret880_neg_at_h` | one_head_filter_pi_star | 201 | 16.4199 | 1.9026 | 0.6766 | 3.8121 | 0.0205 | 0.3682 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret880_neg_at_h` | one_head_filter_pi_star | 228 | 18.6255 | 1.8008 | 0.6623 | 3.8356 | 0.0188 | 0.3596 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret880_neg_at_h` | one_head_filter_pi_star | 220 | 17.9896 | 2.0160 | 0.6682 | 4.1252 | 0.0156 | 0.3455 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret880_neg_at_h` | one_head_filter_pi_star | 243 | 19.8703 | 1.9113 | 0.6502 | 4.0170 | 0.0144 | 0.3621 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret880_pos_at_h` | one_head_filter_pi_star | 80 | 6.6023 | 1.2627 | 0.6000 | 0.9080 | 0.0109 | 0.2250 | ok | RAN |
| ETHUSDT | 8 | `ret880_pos_at_h` | one_head_filter_pi_star | 84 | 6.9730 | 1.2537 | 0.6071 | 0.8879 | 0.0101 | 0.2262 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret880_pos_at_h` | one_head_filter_pi_star | 94 | 7.6648 | 1.6553 | 0.6277 | 1.9884 | 0.0085 | 0.2340 | ok | RAN |
| SOLUSDT | 4 | `ret880_pos_at_h` | one_head_filter_pi_star | 67 | 5.5686 | 1.1945 | 0.5821 | 0.6601 | 0.0031 | 0.1642 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret880_pos_at_h` | one_head_filter_pi_star | 12 | 1.0212 | 0.4560 | 0.2500 | -1.0181 | -0.0551 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret880_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret880_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret880_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret880_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret880_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret880_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret880_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret880_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret880_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret880_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret880_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret880_pos_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret880_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret880_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret880_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
