# Autonomy public-indicator hunt gen 602

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T004000Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret456_neg_at_h` | one_head_filter_pi_star | 155 | 12.6621 | 2.3137 | 0.7161 | 4.4493 | 0.0281 | 0.4065 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret456_neg_at_h` | one_head_filter_pi_star | 153 | 12.4987 | 2.1406 | 0.7059 | 4.2245 | 0.0262 | 0.3791 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret456_neg_at_h` | one_head_filter_pi_star | 206 | 16.7585 | 1.7005 | 0.6505 | 3.2420 | 0.0107 | 0.3252 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret456_neg_at_h` | one_head_filter_pi_star | 195 | 15.8636 | 1.6393 | 0.6462 | 2.9218 | 0.0103 | 0.3385 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ret456_pos_at_h` | one_head_filter_pi_star | 151 | 12.3827 | 1.5456 | 0.6093 | 2.2213 | 0.0088 | 0.2980 | ok | RAN |
| SOLUSDT | 8 | `ret456_pos_at_h` | one_head_filter_pi_star | 147 | 12.0547 | 1.5127 | 0.6054 | 2.1260 | 0.0085 | 0.3129 | ok | RAN |
| ETHUSDT | 4 | `ret456_pos_at_h` | one_head_filter_pi_star | 154 | 12.6586 | 1.1956 | 0.5909 | 0.9683 | 0.0073 | 0.2143 | ok | RAN |
| ETHUSDT | 8 | `ret456_pos_at_h` | one_head_filter_pi_star | 211 | 17.2870 | 1.1942 | 0.5972 | 1.0658 | 0.0071 | 0.2370 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret456_pos_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5547 | 0.3000 | -0.9879 | -0.0437 | 0.0500 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret456_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5490 | 0.2632 | -1.0008 | -0.0475 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret456_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret456_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret456_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret456_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret456_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret456_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret456_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret456_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret456_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret456_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret456_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret456_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret456_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret456_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
