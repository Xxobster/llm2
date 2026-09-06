# Autonomy public-indicator hunt gen 028

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T110843Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ao_cross_down_0` | one_head_filter_pi_star | 31 | 2.5477 | 2.6348 | 0.6129 | 1.9443 | 0.0290 | 0.3548 | EBR>35% | RAN |
| SOLUSDT | 4 | `ao_cross_down_0` | one_head_filter_pi_star | 29 | 2.3833 | 2.4276 | 0.6207 | 1.7463 | 0.0258 | 0.3793 | EBR>35% | RAN |
| ETHUSDT | 4 | `ao_neg_at_h` | one_head_filter_pi_star | 217 | 17.7269 | 1.8491 | 0.6774 | 4.0779 | 0.0215 | 0.3733 | EBR>35% | RAN |
| ETHUSDT | 4 | `ao_cross_down_0` | one_head_filter_pi_star | 54 | 4.4625 | 1.5721 | 0.6481 | 1.4150 | 0.0215 | 0.3333 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ao_neg_at_h` | one_head_filter_pi_star | 221 | 18.0537 | 1.8007 | 0.6787 | 3.8626 | 0.0207 | 0.3756 | EBR>35% | RAN |
| ETHUSDT | 8 | `ao_cross_down_0` | one_head_filter_pi_star | 57 | 4.7104 | 1.4626 | 0.6491 | 1.2686 | 0.0178 | 0.3158 | ok | RAN |
| SOLUSDT | 8 | `ao_neg_at_h` | one_head_filter_pi_star | 160 | 13.0833 | 2.1469 | 0.6875 | 3.9561 | 0.0175 | 0.4188 | EBR>35% | RAN |
| SOLUSDT | 4 | `ao_neg_at_h` | one_head_filter_pi_star | 160 | 13.0833 | 2.1335 | 0.6875 | 3.8959 | 0.0172 | 0.4313 | EBR>35% | RAN |
| ETHUSDT | 8 | `ao_cross_up_0` | one_head_filter_pi_star | 35 | 3.0387 | 1.5036 | 0.5714 | 0.9273 | 0.0156 | 0.2000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `ao_cross_up_0` | one_head_filter_pi_star | 32 | 2.7782 | 1.4585 | 0.5625 | 0.8836 | 0.0121 | 0.1875 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ao_cross_up_0` | one_head_filter_pi_star | 48 | 4.1835 | 1.5645 | 0.6042 | 1.3466 | 0.0106 | 0.1458 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ao_cross_up_0` | one_head_filter_pi_star | 46 | 4.4075 | 1.4525 | 0.5870 | 1.1517 | 0.0089 | 0.1304 | ok | RAN |
| ETHUSDT | 8 | `ao_pos_at_h` | one_head_filter_pi_star | 161 | 13.2859 | 1.1895 | 0.5901 | 0.8942 | 0.0060 | 0.1988 | ok | RAN |
| SOLUSDT | 4 | `ao_pos_at_h` | one_head_filter_pi_star | 219 | 17.8573 | 1.3688 | 0.5982 | 2.0015 | 0.0054 | 0.2374 | ok | RAN |
| SOLUSDT | 8 | `ao_pos_at_h` | one_head_filter_pi_star | 213 | 17.3681 | 1.3562 | 0.5962 | 1.9282 | 0.0052 | 0.2394 | ok | RAN |
| ETHUSDT | 4 | `ao_pos_at_h` | one_head_filter_pi_star | 159 | 13.1209 | 1.1623 | 0.5912 | 0.7786 | 0.0051 | 0.2075 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ao_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ao_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ao_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ao_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ao_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ao_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ao_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ao_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
