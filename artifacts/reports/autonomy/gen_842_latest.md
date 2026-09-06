# Autonomy public-indicator hunt gen 842

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T193858Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret696_neg_at_h` | one_head_filter_pi_star | 169 | 13.8058 | 2.0535 | 0.6982 | 3.9775 | 0.0224 | 0.3550 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret696_neg_at_h` | one_head_filter_pi_star | 164 | 13.3973 | 2.0763 | 0.6768 | 3.9771 | 0.0214 | 0.3659 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret696_neg_at_h` | one_head_filter_pi_star | 225 | 18.3984 | 1.9877 | 0.6622 | 4.0928 | 0.0150 | 0.3333 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret696_neg_at_h` | one_head_filter_pi_star | 229 | 18.7255 | 1.7915 | 0.6507 | 3.6008 | 0.0130 | 0.3275 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret696_pos_at_h` | one_head_filter_pi_star | 105 | 8.6105 | 1.6378 | 0.6381 | 2.2080 | 0.0093 | 0.2571 | ok | RAN |
| ETHUSDT | 8 | `ret696_pos_at_h` | one_head_filter_pi_star | 156 | 12.8230 | 1.2174 | 0.5962 | 1.0270 | 0.0089 | 0.2372 | ok | RAN |
| SOLUSDT | 4 | `ret696_pos_at_h` | one_head_filter_pi_star | 120 | 9.8406 | 1.4868 | 0.6250 | 1.8784 | 0.0079 | 0.2750 | ok | RAN |
| ETHUSDT | 4 | `ret696_pos_at_h` | one_head_filter_pi_star | 161 | 13.2340 | 1.0949 | 0.5776 | 0.4874 | 0.0041 | 0.2298 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret696_pos_at_h` | one_head_filter_pi_star | 14 | 1.1914 | 0.6181 | 0.2857 | -0.7156 | -0.0374 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret696_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret696_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret696_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret696_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret696_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret696_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret696_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret696_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret696_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret696_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret696_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret696_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret696_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret696_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret696_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
