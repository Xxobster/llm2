# Autonomy public-indicator hunt gen 242

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T012407Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret92_neg_at_h` | one_head_filter_pi_star | 195 | 15.9297 | 1.8382 | 0.6615 | 3.7806 | 0.0206 | 0.3692 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret92_neg_at_h` | one_head_filter_pi_star | 204 | 16.6649 | 1.7587 | 0.6569 | 3.7504 | 0.0194 | 0.3529 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret92_neg_at_h` | one_head_filter_pi_star | 190 | 15.5365 | 2.2667 | 0.6789 | 4.5794 | 0.0173 | 0.3579 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret92_neg_at_h` | one_head_filter_pi_star | 175 | 14.3099 | 2.0321 | 0.6629 | 3.7791 | 0.0153 | 0.3657 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret92_pos_at_h` | one_head_filter_pi_star | 170 | 14.0286 | 1.4327 | 0.6471 | 1.9890 | 0.0140 | 0.2412 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ret92_pos_at_h` | one_head_filter_pi_star | 187 | 15.3712 | 1.2941 | 0.6257 | 1.4144 | 0.0097 | 0.2299 | ok | RAN |
| SOLUSDT | 4 | `ret92_pos_at_h` | one_head_filter_pi_star | 184 | 15.0034 | 1.3741 | 0.5978 | 1.8754 | 0.0059 | 0.2609 | ok | RAN |
| SOLUSDT | 8 | `ret92_pos_at_h` | one_head_filter_pi_star | 182 | 14.8404 | 1.3564 | 0.5934 | 1.8049 | 0.0057 | 0.2527 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret92_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret92_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5765 | 0.2778 | -0.8994 | -0.0458 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret92_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret92_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret92_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret92_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret92_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret92_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret92_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret92_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret92_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret92_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret92_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret92_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret92_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret92_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
