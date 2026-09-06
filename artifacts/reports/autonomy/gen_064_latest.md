# Autonomy public-indicator hunt gen 064

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T134506Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `gap_cross_down_0` | one_head_filter_pi_star | 163 | 13.3369 | 1.7981 | 0.6503 | 3.2656 | 0.0222 | 0.3006 | GATE_CAND | RAN |
| ETHUSDT | 4 | `gap_cross_up_0` | one_head_filter_pi_star | 353 | 28.7172 | 1.5526 | 0.6374 | 3.3637 | 0.0163 | 0.3116 | GATE_CAND | RAN |
| ETHUSDT | 8 | `gap_cross_up_0` | one_head_filter_pi_star | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | GATE_CAND | RAN |
| ETHUSDT | 8 | `gap_cross_down_0` | one_head_filter_pi_star | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `gap_cross_down_0` | one_head_filter_pi_star | 118 | 9.5995 | 1.8100 | 0.6441 | 2.5741 | 0.0152 | 0.3136 | GATE_CAND | RAN |
| BTCUSDT | 4 | `gap_cross_up_0` | one_head_filter_pi_star | 12 | 1.2608 | 1.1062 | 0.5000 | 0.1685 | 0.0134 | 0.1667 | TPM<MIN | RAN |
| SOLUSDT | 4 | `gap_cross_up_0` | one_head_filter_pi_star | 128 | 10.6303 | 1.7740 | 0.6406 | 2.8170 | 0.0130 | 0.3516 | EBR>35% | RAN |
| SOLUSDT | 8 | `gap_cross_up_0` | one_head_filter_pi_star | 382 | 31.0765 | 1.6890 | 0.6387 | 4.3279 | 0.0102 | 0.3194 | GATE_CAND | RAN |
| SOLUSDT | 8 | `gap_cross_down_0` | one_head_filter_pi_star | 382 | 31.0765 | 1.6890 | 0.6387 | 4.3279 | 0.0102 | 0.3194 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| BTCUSDT | 8 | `gap_cross_up_0` | one_head_filter_pi_star | 27 | 2.2976 | 1.0729 | 0.4444 | 0.1508 | 0.0065 | 0.1481 | TPM<MIN | RAN |
| BTCUSDT | 8 | `gap_cross_down_0` | one_head_filter_pi_star | 27 | 2.2976 | 1.0729 | 0.4444 | 0.1508 | 0.0065 | 0.1481 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `gap_pos_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `gap_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `gap_pos_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `gap_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `gap_pos_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `gap_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `gap_pos_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `gap_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `gap_pos_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `gap_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `gap_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `gap_pos_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `gap_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
