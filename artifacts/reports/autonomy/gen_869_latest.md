# Autonomy public-indicator hunt gen 869

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T221749Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret165_neg_at_h` | one_head_filter_pi_star | 182 | 14.8677 | 2.0479 | 0.6923 | 4.4097 | 0.0257 | 0.4011 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret165_neg_at_h` | one_head_filter_pi_star | 187 | 15.2762 | 1.9151 | 0.6845 | 4.1254 | 0.0229 | 0.3957 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret165_neg_at_h` | one_head_filter_pi_star | 165 | 13.4922 | 2.1739 | 0.6788 | 4.1171 | 0.0165 | 0.3818 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret165_neg_at_h` | one_head_filter_pi_star | 163 | 13.3287 | 2.0210 | 0.6687 | 3.7407 | 0.0153 | 0.3865 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ret165_pos_at_h` | one_head_filter_pi_star | 199 | 16.4218 | 1.2390 | 0.6030 | 1.2584 | 0.0079 | 0.2111 | ok | RAN |
| SOLUSDT | 4 | `ret165_pos_at_h` | one_head_filter_pi_star | 201 | 16.3896 | 1.4596 | 0.6119 | 2.2534 | 0.0070 | 0.2637 | ok | RAN |
| SOLUSDT | 8 | `ret165_pos_at_h` | one_head_filter_pi_star | 190 | 15.4927 | 1.4386 | 0.6053 | 2.1244 | 0.0069 | 0.2579 | ok | RAN |
| ETHUSDT | 8 | `ret165_pos_at_h` | one_head_filter_pi_star | 187 | 15.4315 | 1.1867 | 0.5989 | 0.9862 | 0.0066 | 0.2086 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret165_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5773 | 0.2941 | -0.8964 | -0.0456 | 0.0588 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret165_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5773 | 0.2941 | -0.8964 | -0.0475 | 0.0588 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret165_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret165_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret165_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret165_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret165_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret165_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret165_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret165_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret165_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret165_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret165_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret165_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret165_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret165_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
