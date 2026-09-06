# Autonomy public-indicator hunt gen 837

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T191037Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret157_neg_at_h` | one_head_filter_pi_star | 182 | 14.8677 | 2.0134 | 0.6978 | 4.4230 | 0.0244 | 0.3736 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret157_neg_at_h` | one_head_filter_pi_star | 186 | 15.1945 | 1.9900 | 0.6989 | 4.4566 | 0.0241 | 0.3871 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret157_neg_at_h` | one_head_filter_pi_star | 177 | 14.4734 | 2.1713 | 0.6836 | 4.2401 | 0.0163 | 0.3616 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret157_neg_at_h` | one_head_filter_pi_star | 186 | 15.2094 | 2.0593 | 0.6720 | 4.0900 | 0.0154 | 0.3656 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ret157_pos_at_h` | one_head_filter_pi_star | 197 | 16.1931 | 1.2132 | 0.5990 | 1.1186 | 0.0071 | 0.2234 | ok | RAN |
| SOLUSDT | 8 | `ret157_pos_at_h` | one_head_filter_pi_star | 188 | 15.3296 | 1.3969 | 0.6011 | 1.9659 | 0.0064 | 0.2660 | ok | RAN |
| ETHUSDT | 8 | `ret157_pos_at_h` | one_head_filter_pi_star | 190 | 15.6791 | 1.1758 | 0.5895 | 0.9492 | 0.0061 | 0.2211 | ok | RAN |
| SOLUSDT | 4 | `ret157_pos_at_h` | one_head_filter_pi_star | 184 | 15.0034 | 1.3478 | 0.5870 | 1.7027 | 0.0056 | 0.2609 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret157_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5834 | 0.3333 | -0.8834 | -0.0441 | 0.0556 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret157_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5773 | 0.2941 | -0.8964 | -0.0448 | 0.0588 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret157_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret157_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret157_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret157_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret157_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret157_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret157_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret157_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret157_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret157_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret157_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret157_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret157_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret157_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
