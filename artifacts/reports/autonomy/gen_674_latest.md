# Autonomy public-indicator hunt gen 674

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T052115Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret528_neg_at_h` | one_head_filter_pi_star | 164 | 13.3973 | 2.1971 | 0.7012 | 4.3878 | 0.0260 | 0.3963 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret528_neg_at_h` | one_head_filter_pi_star | 169 | 13.8058 | 2.0455 | 0.7041 | 4.1141 | 0.0249 | 0.4083 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret528_pos_at_h` | one_head_filter_pi_star | 114 | 9.4749 | 1.8576 | 0.6491 | 2.8216 | 0.0123 | 0.2895 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret528_neg_at_h` | one_head_filter_pi_star | 187 | 15.3924 | 1.7438 | 0.6578 | 3.1565 | 0.0122 | 0.3529 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret528_neg_at_h` | one_head_filter_pi_star | 213 | 17.5325 | 1.6699 | 0.6432 | 3.0659 | 0.0111 | 0.3286 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ret528_pos_at_h` | one_head_filter_pi_star | 167 | 13.7272 | 1.2734 | 0.5988 | 1.4041 | 0.0098 | 0.2335 | ok | RAN |
| SOLUSDT | 4 | `ret528_pos_at_h` | one_head_filter_pi_star | 139 | 11.5527 | 1.4039 | 0.5899 | 1.7198 | 0.0066 | 0.2950 | ok | RAN |
| ETHUSDT | 8 | `ret528_pos_at_h` | one_head_filter_pi_star | 145 | 11.9188 | 1.1130 | 0.5793 | 0.5512 | 0.0043 | 0.2276 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret528_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6020 | 0.2941 | -0.7739 | -0.0321 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret528_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5490 | 0.2632 | -1.0008 | -0.0475 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret528_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret528_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret528_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret528_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret528_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret528_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret528_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret528_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret528_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret528_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret528_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret528_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret528_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret528_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
