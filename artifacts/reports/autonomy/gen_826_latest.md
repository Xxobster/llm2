# Autonomy public-indicator hunt gen 826

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T180702Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret680_neg_at_h` | one_head_filter_pi_star | 168 | 13.7241 | 2.0286 | 0.6905 | 3.8731 | 0.0216 | 0.3869 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret680_neg_at_h` | one_head_filter_pi_star | 177 | 14.4593 | 1.9900 | 0.6949 | 3.8317 | 0.0209 | 0.3672 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret680_neg_at_h` | one_head_filter_pi_star | 193 | 15.8863 | 2.0551 | 0.6788 | 3.9363 | 0.0163 | 0.3420 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret680_neg_at_h` | one_head_filter_pi_star | 228 | 18.6438 | 1.9655 | 0.6667 | 4.1428 | 0.0147 | 0.3377 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ret680_pos_at_h` | one_head_filter_pi_star | 140 | 11.5078 | 1.2286 | 0.5929 | 1.0441 | 0.0092 | 0.2500 | ok | RAN |
| SOLUSDT | 4 | `ret680_pos_at_h` | one_head_filter_pi_star | 104 | 8.5285 | 1.5941 | 0.6346 | 2.1206 | 0.0084 | 0.2308 | ok | RAN |
| SOLUSDT | 8 | `ret680_pos_at_h` | one_head_filter_pi_star | 113 | 9.2141 | 1.5501 | 0.6460 | 1.9352 | 0.0078 | 0.2478 | ok | RAN |
| ETHUSDT | 8 | `ret680_pos_at_h` | one_head_filter_pi_star | 145 | 11.9188 | 1.1187 | 0.5724 | 0.5432 | 0.0048 | 0.2276 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret680_pos_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.4741 | 0.2500 | -1.1218 | -0.0599 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret680_pos_at_h` | one_head_filter_pi_star | 15 | 1.2765 | 0.4748 | 0.2667 | -1.1188 | -0.0611 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret680_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret680_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret680_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret680_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret680_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret680_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret680_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret680_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret680_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret680_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret680_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret680_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret680_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret680_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
