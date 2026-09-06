# Autonomy public-indicator hunt gen 898

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260826T011434Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret752_neg_at_h` | one_head_filter_pi_star | 196 | 16.0114 | 2.2340 | 0.7143 | 4.5390 | 0.0245 | 0.3571 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret752_neg_at_h` | one_head_filter_pi_star | 195 | 15.9297 | 1.9849 | 0.6974 | 3.9870 | 0.0215 | 0.3641 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret752_neg_at_h` | one_head_filter_pi_star | 204 | 16.6813 | 1.9807 | 0.6765 | 3.8379 | 0.0154 | 0.3431 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret752_neg_at_h` | one_head_filter_pi_star | 213 | 17.4172 | 1.8295 | 0.6667 | 3.5572 | 0.0137 | 0.3239 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ret752_pos_at_h` | one_head_filter_pi_star | 141 | 11.5900 | 1.2501 | 0.5957 | 1.1293 | 0.0102 | 0.2411 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ret752_pos_at_h` | one_head_filter_pi_star | 67 | 5.4983 | 1.7325 | 0.6567 | 1.9376 | 0.0096 | 0.2985 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret752_pos_at_h` | one_head_filter_pi_star | 77 | 6.3190 | 1.6303 | 0.6364 | 1.9312 | 0.0095 | 0.2987 | ok | RAN |
| ETHUSDT | 8 | `ret752_pos_at_h` | one_head_filter_pi_star | 125 | 10.2748 | 1.0719 | 0.5680 | 0.3338 | 0.0031 | 0.2240 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret752_pos_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.4684 | 0.2500 | -1.1492 | -0.0565 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret752_pos_at_h` | one_head_filter_pi_star | 15 | 1.2765 | 0.3151 | 0.2000 | -1.5699 | -0.0774 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret752_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret752_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret752_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret752_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret752_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret752_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret752_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret752_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret752_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret752_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret752_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret752_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret752_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret752_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
