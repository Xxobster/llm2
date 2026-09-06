# Autonomy public-indicator hunt gen 733

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T093419Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret131_neg_at_h` | one_head_filter_pi_star | 188 | 15.3579 | 2.0145 | 0.6915 | 4.4328 | 0.0241 | 0.3777 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret131_neg_at_h` | one_head_filter_pi_star | 182 | 14.8677 | 1.9696 | 0.6868 | 4.0415 | 0.0234 | 0.3791 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret131_neg_at_h` | one_head_filter_pi_star | 174 | 14.2281 | 2.1977 | 0.6897 | 4.1819 | 0.0166 | 0.3621 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret131_neg_at_h` | one_head_filter_pi_star | 173 | 14.1464 | 2.1425 | 0.6763 | 4.0823 | 0.0162 | 0.3757 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `ret131_pos_at_h` | one_head_filter_pi_star | 183 | 15.1014 | 1.3409 | 0.6120 | 1.6859 | 0.0115 | 0.2240 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ret131_pos_at_h` | one_head_filter_pi_star | 185 | 15.2665 | 1.2942 | 0.6162 | 1.5246 | 0.0098 | 0.2270 | ok | RAN |
| SOLUSDT | 8 | `ret131_pos_at_h` | one_head_filter_pi_star | 196 | 15.9819 | 1.4142 | 0.5969 | 2.0577 | 0.0067 | 0.2653 | ok | RAN |
| SOLUSDT | 4 | `ret131_pos_at_h` | one_head_filter_pi_star | 195 | 15.9004 | 1.3774 | 0.6000 | 1.8980 | 0.0060 | 0.2615 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret131_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret131_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret131_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret131_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret131_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret131_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret131_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret131_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret131_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret131_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret131_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret131_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret131_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret131_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret131_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret131_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
