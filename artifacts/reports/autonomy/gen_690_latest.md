# Autonomy public-indicator hunt gen 690

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T062807Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret544_neg_at_h` | one_head_filter_pi_star | 182 | 14.8677 | 2.2320 | 0.7143 | 4.7854 | 0.0258 | 0.3791 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret544_neg_at_h` | one_head_filter_pi_star | 182 | 14.8677 | 2.1268 | 0.7088 | 4.4415 | 0.0244 | 0.4011 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret544_neg_at_h` | one_head_filter_pi_star | 175 | 14.4046 | 1.7298 | 0.6514 | 3.0179 | 0.0116 | 0.3486 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret544_neg_at_h` | one_head_filter_pi_star | 167 | 13.8929 | 1.6391 | 0.6347 | 2.6699 | 0.0104 | 0.3593 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ret544_pos_at_h` | one_head_filter_pi_star | 141 | 11.5900 | 1.2302 | 0.5745 | 1.0987 | 0.0084 | 0.2482 | ok | RAN |
| SOLUSDT | 8 | `ret544_pos_at_h` | one_head_filter_pi_star | 160 | 13.0465 | 1.5444 | 0.6000 | 2.2931 | 0.0082 | 0.2812 | ok | RAN |
| SOLUSDT | 4 | `ret544_pos_at_h` | one_head_filter_pi_star | 158 | 12.9568 | 1.5297 | 0.5949 | 2.2532 | 0.0079 | 0.2722 | ok | RAN |
| ETHUSDT | 8 | `ret544_pos_at_h` | one_head_filter_pi_star | 158 | 12.9874 | 1.1305 | 0.5759 | 0.6540 | 0.0051 | 0.2215 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret544_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6020 | 0.2941 | -0.7739 | -0.0321 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret544_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4442 | 0.2632 | -1.2722 | -0.0565 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret544_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret544_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret544_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret544_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret544_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret544_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret544_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret544_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret544_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret544_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret544_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret544_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret544_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret544_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
