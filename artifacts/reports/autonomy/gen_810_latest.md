# Autonomy public-indicator hunt gen 810

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T163909Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret664_neg_at_h` | one_head_filter_pi_star | 173 | 14.1325 | 1.9164 | 0.6763 | 3.7357 | 0.0198 | 0.3642 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret664_neg_at_h` | one_head_filter_pi_star | 201 | 16.4199 | 1.8310 | 0.6667 | 3.6171 | 0.0192 | 0.3632 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret664_neg_at_h` | one_head_filter_pi_star | 198 | 16.2978 | 2.0275 | 0.6717 | 4.0554 | 0.0171 | 0.3434 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret664_neg_at_h` | one_head_filter_pi_star | 195 | 16.0509 | 1.9667 | 0.6667 | 3.7552 | 0.0153 | 0.3282 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret664_pos_at_h` | one_head_filter_pi_star | 106 | 8.7123 | 2.1499 | 0.7075 | 3.2871 | 0.0133 | 0.2925 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret664_pos_at_h` | one_head_filter_pi_star | 106 | 8.7128 | 1.7152 | 0.6698 | 2.2774 | 0.0093 | 0.2453 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret664_pos_at_h` | one_head_filter_pi_star | 154 | 12.6586 | 1.2482 | 0.5909 | 1.1967 | 0.0093 | 0.2338 | ok | RAN |
| ETHUSDT | 4 | `ret664_pos_at_h` | one_head_filter_pi_star | 164 | 13.4806 | 1.1363 | 0.5671 | 0.6863 | 0.0057 | 0.2134 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret664_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0588 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret664_pos_at_h` | one_head_filter_pi_star | 14 | 1.1914 | 0.5092 | 0.2857 | -0.9832 | -0.0597 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret664_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret664_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret664_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret664_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret664_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret664_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret664_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret664_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret664_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret664_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret664_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret664_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret664_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret664_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
