# Autonomy public-indicator hunt gen 1450

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260830T215048Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret1304_neg_at_h` | one_head_filter_pi_star | 342 | 27.8224 | 1.6959 | 0.6550 | 4.1670 | 0.0182 | 0.3099 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret1304_pos_at_h` | one_head_filter_pi_star | 21 | 1.7677 | 2.5219 | 0.7619 | 1.6818 | 0.0174 | 0.4762 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret1304_neg_at_h` | one_head_filter_pi_star | 345 | 28.0664 | 1.5984 | 0.6493 | 3.8060 | 0.0163 | 0.3072 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret1304_pos_at_h` | one_head_filter_pi_star | 14 | 1.2355 | 1.9461 | 0.7143 | 1.0773 | 0.0128 | 0.3571 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret1304_neg_at_h` | one_head_filter_pi_star | 343 | 27.9037 | 1.7666 | 0.6414 | 4.4862 | 0.0113 | 0.3236 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret1304_neg_at_h` | one_head_filter_pi_star | 336 | 27.3343 | 1.6921 | 0.6339 | 4.0121 | 0.0106 | 0.3125 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1304_pos_at_h` | one_head_filter_pi_star | 21 | 4.2089 | 0.9426 | 0.5238 | -0.1824 | -0.0027 | 0.2857 | ok | RAN |
| ETHUSDT | 8 | `ret1304_pos_at_h` | one_head_filter_pi_star | 27 | 2.8972 | 0.7562 | 0.4815 | -0.6782 | -0.0108 | 0.1852 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret1304_pos_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.6250 | 0.3125 | -0.7038 | -0.0291 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret1304_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4777 | 0.2778 | -1.1199 | -0.0511 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1304_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret1304_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1304_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1304_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1304_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1304_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1304_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1304_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1304_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1304_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1304_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1304_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1304_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1304_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
