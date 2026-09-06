# Autonomy public-indicator hunt gen 861

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T213011Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret163_neg_at_h` | one_head_filter_pi_star | 182 | 14.8677 | 2.1597 | 0.7088 | 4.7328 | 0.0268 | 0.3901 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret163_neg_at_h` | one_head_filter_pi_star | 194 | 15.8480 | 1.9858 | 0.6959 | 4.4311 | 0.0242 | 0.3866 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret163_neg_at_h` | one_head_filter_pi_star | 168 | 13.7375 | 2.1887 | 0.6845 | 4.1758 | 0.0166 | 0.3750 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret163_neg_at_h` | one_head_filter_pi_star | 173 | 14.1464 | 2.1002 | 0.6763 | 4.0514 | 0.0160 | 0.3815 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret163_pos_at_h` | one_head_filter_pi_star | 181 | 14.7588 | 1.4036 | 0.5967 | 1.9406 | 0.0063 | 0.2652 | ok | RAN |
| SOLUSDT | 4 | `ret163_pos_at_h` | one_head_filter_pi_star | 184 | 15.0034 | 1.3488 | 0.5978 | 1.7199 | 0.0056 | 0.2663 | ok | RAN |
| ETHUSDT | 4 | `ret163_pos_at_h` | one_head_filter_pi_star | 202 | 16.6041 | 1.1389 | 0.5842 | 0.7597 | 0.0049 | 0.2129 | ok | RAN |
| ETHUSDT | 8 | `ret163_pos_at_h` | one_head_filter_pi_star | 189 | 15.5965 | 1.1327 | 0.5873 | 0.7081 | 0.0046 | 0.2011 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret163_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5834 | 0.3333 | -0.8834 | -0.0450 | 0.0556 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret163_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5773 | 0.2941 | -0.8964 | -0.0465 | 0.0588 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret163_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret163_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret163_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret163_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret163_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret163_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret163_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret163_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret163_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret163_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret163_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret163_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret163_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret163_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
