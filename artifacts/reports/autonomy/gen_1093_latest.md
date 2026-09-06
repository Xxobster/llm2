# Autonomy public-indicator hunt gen 1093

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T220732Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret199_neg_at_h` | one_head_filter_pi_star | 162 | 13.2339 | 2.1070 | 0.6975 | 4.4304 | 0.0248 | 0.3889 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret199_neg_at_h` | one_head_filter_pi_star | 181 | 14.7860 | 1.9894 | 0.6906 | 4.3273 | 0.0229 | 0.3702 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret199_neg_at_h` | one_head_filter_pi_star | 156 | 12.7563 | 1.9553 | 0.6667 | 3.4449 | 0.0145 | 0.3654 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret199_neg_at_h` | one_head_filter_pi_star | 170 | 13.9010 | 1.8879 | 0.6647 | 3.4313 | 0.0133 | 0.3647 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret199_pos_at_h` | one_head_filter_pi_star | 179 | 14.5957 | 1.5576 | 0.6201 | 2.5002 | 0.0083 | 0.2626 | ok | RAN |
| SOLUSDT | 4 | `ret199_pos_at_h` | one_head_filter_pi_star | 195 | 15.9004 | 1.4422 | 0.6051 | 2.1250 | 0.0069 | 0.2615 | ok | RAN |
| ETHUSDT | 4 | `ret199_pos_at_h` | one_head_filter_pi_star | 191 | 15.7000 | 1.1901 | 0.5864 | 1.0159 | 0.0067 | 0.2304 | ok | RAN |
| ETHUSDT | 8 | `ret199_pos_at_h` | one_head_filter_pi_star | 204 | 16.7685 | 1.1373 | 0.5882 | 0.7445 | 0.0050 | 0.2108 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret199_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.6894 | 0.3158 | -0.6415 | -0.0323 | 0.1053 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret199_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5773 | 0.2941 | -0.8964 | -0.0448 | 0.0588 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret199_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret199_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret199_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret199_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret199_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret199_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret199_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret199_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret199_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret199_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret199_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret199_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret199_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret199_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
