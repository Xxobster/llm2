# Autonomy public-indicator hunt gen 893

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260826T004350Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret171_neg_at_h` | one_head_filter_pi_star | 167 | 13.6424 | 2.3699 | 0.7186 | 5.0207 | 0.0293 | 0.3892 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret171_neg_at_h` | one_head_filter_pi_star | 183 | 14.9494 | 1.9497 | 0.6885 | 4.2930 | 0.0237 | 0.3880 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret171_neg_at_h` | one_head_filter_pi_star | 164 | 13.4104 | 2.1301 | 0.6707 | 4.0227 | 0.0159 | 0.3720 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret171_neg_at_h` | one_head_filter_pi_star | 167 | 13.6557 | 1.9709 | 0.6707 | 3.6172 | 0.0146 | 0.3772 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ret171_pos_at_h` | one_head_filter_pi_star | 207 | 17.0819 | 1.2138 | 0.5990 | 1.1898 | 0.0072 | 0.2222 | ok | RAN |
| SOLUSDT | 4 | `ret171_pos_at_h` | one_head_filter_pi_star | 206 | 16.7973 | 1.4493 | 0.6068 | 2.2371 | 0.0070 | 0.2573 | ok | RAN |
| SOLUSDT | 8 | `ret171_pos_at_h` | one_head_filter_pi_star | 196 | 15.9819 | 1.3812 | 0.5969 | 1.9130 | 0.0061 | 0.2653 | ok | RAN |
| ETHUSDT | 8 | `ret171_pos_at_h` | one_head_filter_pi_star | 197 | 16.2567 | 1.1802 | 0.5888 | 0.9748 | 0.0061 | 0.2183 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret171_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.6903 | 0.3333 | -0.6386 | -0.0334 | 0.1111 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret171_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5773 | 0.2941 | -0.8964 | -0.0456 | 0.0588 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret171_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret171_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret171_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret171_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret171_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret171_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret171_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret171_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret171_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret171_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret171_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret171_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret171_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret171_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
