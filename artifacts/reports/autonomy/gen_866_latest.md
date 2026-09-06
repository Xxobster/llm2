# Autonomy public-indicator hunt gen 866

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T220111Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret720_neg_at_h` | one_head_filter_pi_star | 168 | 13.7241 | 2.2969 | 0.7083 | 4.5043 | 0.0245 | 0.3690 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret720_neg_at_h` | one_head_filter_pi_star | 164 | 13.3973 | 2.2188 | 0.7012 | 4.2116 | 0.0225 | 0.3598 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret720_neg_at_h` | one_head_filter_pi_star | 212 | 17.3354 | 1.8759 | 0.6651 | 3.6960 | 0.0138 | 0.3302 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret720_neg_at_h` | one_head_filter_pi_star | 199 | 16.2724 | 1.7942 | 0.6583 | 3.3316 | 0.0130 | 0.3367 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret720_pos_at_h` | one_head_filter_pi_star | 105 | 8.6105 | 1.4055 | 0.6000 | 1.5333 | 0.0061 | 0.2286 | ok | RAN |
| SOLUSDT | 4 | `ret720_pos_at_h` | one_head_filter_pi_star | 115 | 9.4306 | 1.3309 | 0.6000 | 1.3461 | 0.0055 | 0.2696 | ok | RAN |
| ETHUSDT | 8 | `ret720_pos_at_h` | one_head_filter_pi_star | 160 | 13.1518 | 1.1009 | 0.5687 | 0.4957 | 0.0043 | 0.2375 | ok | RAN |
| ETHUSDT | 4 | `ret720_pos_at_h` | one_head_filter_pi_star | 158 | 12.9874 | 1.0926 | 0.5696 | 0.4676 | 0.0039 | 0.2215 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret720_pos_at_h` | one_head_filter_pi_star | 15 | 1.2765 | 0.5407 | 0.3333 | -0.8823 | -0.0455 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret720_pos_at_h` | one_head_filter_pi_star | 13 | 1.1063 | 0.5370 | 0.3077 | -0.8842 | -0.0498 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret720_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret720_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret720_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret720_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret720_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret720_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret720_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret720_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret720_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret720_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret720_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret720_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret720_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret720_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
