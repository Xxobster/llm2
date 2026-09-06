# Autonomy public-indicator hunt gen 933

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260826T050558Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret181_neg_at_h` | one_head_filter_pi_star | 167 | 13.6424 | 2.1970 | 0.7066 | 4.6811 | 0.0265 | 0.3952 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret181_neg_at_h` | one_head_filter_pi_star | 180 | 14.7044 | 2.0063 | 0.6944 | 4.3384 | 0.0239 | 0.3944 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret181_neg_at_h` | one_head_filter_pi_star | 171 | 13.9828 | 2.0817 | 0.6725 | 3.9549 | 0.0157 | 0.3626 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret181_neg_at_h` | one_head_filter_pi_star | 169 | 13.8193 | 2.0364 | 0.6746 | 3.8072 | 0.0155 | 0.3787 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ret181_pos_at_h` | one_head_filter_pi_star | 190 | 15.6791 | 1.2501 | 0.5895 | 1.2770 | 0.0083 | 0.2211 | ok | RAN |
| SOLUSDT | 4 | `ret181_pos_at_h` | one_head_filter_pi_star | 188 | 15.3296 | 1.5492 | 0.6223 | 2.5292 | 0.0083 | 0.2660 | ok | RAN |
| SOLUSDT | 8 | `ret181_pos_at_h` | one_head_filter_pi_star | 206 | 16.7973 | 1.4723 | 0.6117 | 2.3376 | 0.0073 | 0.2573 | ok | RAN |
| ETHUSDT | 8 | `ret181_pos_at_h` | one_head_filter_pi_star | 196 | 16.1742 | 1.1441 | 0.5765 | 0.7831 | 0.0050 | 0.2143 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret181_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5765 | 0.2778 | -0.8994 | -0.0441 | 0.0556 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret181_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5773 | 0.2941 | -0.8964 | -0.0465 | 0.0588 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret181_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret181_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret181_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret181_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret181_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret181_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret181_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret181_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret181_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret181_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret181_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret181_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret181_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret181_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
