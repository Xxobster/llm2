# Autonomy public-indicator hunt gen 365

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T175455Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret39_neg_at_h` | one_head_filter_pi_star | 202 | 16.5016 | 1.7837 | 0.6782 | 3.7724 | 0.0208 | 0.3614 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret39_neg_at_h` | one_head_filter_pi_star | 209 | 17.0734 | 1.7013 | 0.6603 | 3.5413 | 0.0190 | 0.3589 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret39_neg_at_h` | one_head_filter_pi_star | 158 | 12.9198 | 2.1358 | 0.6899 | 3.9111 | 0.0173 | 0.4051 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret39_cross_up_0` | one_head_filter_pi_star | 22 | 1.8289 | 2.0830 | 0.6364 | 1.4600 | 0.0169 | 0.2727 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ret39_neg_at_h` | one_head_filter_pi_star | 167 | 13.6557 | 1.9970 | 0.6707 | 3.6684 | 0.0160 | 0.3892 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret39_cross_down_0` | one_head_filter_pi_star | 38 | 3.1292 | 1.4241 | 0.5789 | 0.8832 | 0.0089 | 0.1842 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret39_cross_down_0` | one_head_filter_pi_star | 38 | 3.1489 | 1.2135 | 0.5263 | 0.4919 | 0.0077 | 0.1842 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ret39_pos_at_h` | one_head_filter_pi_star | 218 | 17.7758 | 1.5411 | 0.6193 | 2.6822 | 0.0075 | 0.2661 | ok | RAN |
| SOLUSDT | 8 | `ret39_pos_at_h` | one_head_filter_pi_star | 220 | 17.9389 | 1.5149 | 0.6136 | 2.6407 | 0.0073 | 0.2636 | ok | RAN |
| ETHUSDT | 8 | `ret39_pos_at_h` | one_head_filter_pi_star | 171 | 14.0560 | 1.2333 | 0.6023 | 1.1299 | 0.0072 | 0.2281 | ok | RAN |
| ETHUSDT | 4 | `ret39_pos_at_h` | one_head_filter_pi_star | 181 | 14.8780 | 1.2078 | 0.6022 | 1.0291 | 0.0068 | 0.2376 | ok | RAN |
| ETHUSDT | 8 | `ret39_cross_up_0` | one_head_filter_pi_star | 11 | 1.1919 | 1.1379 | 0.5455 | 0.2230 | 0.0051 | 0.1818 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret39_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret39_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret39_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret39_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret39_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret39_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret39_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret39_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret39_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret39_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret39_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret39_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
