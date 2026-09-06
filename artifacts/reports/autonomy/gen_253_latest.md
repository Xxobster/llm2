# Autonomy public-indicator hunt gen 253

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T021003Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ret17_cross_up_0` | one_head_filter_pi_star | 20 | 1.6880 | 3.8589 | 0.7000 | 2.1568 | 0.0275 | 0.2500 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret17_cross_up_0` | one_head_filter_pi_star | 30 | 2.4686 | 1.4811 | 0.5333 | 0.8813 | 0.0218 | 0.3000 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ret17_cross_down_0` | one_head_filter_pi_star | 35 | 3.2385 | 3.0244 | 0.7429 | 2.7016 | 0.0216 | 0.2286 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret17_neg_at_h` | one_head_filter_pi_star | 220 | 17.9720 | 1.7613 | 0.6773 | 3.6579 | 0.0195 | 0.3773 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret17_neg_at_h` | one_head_filter_pi_star | 225 | 18.3804 | 1.7104 | 0.6667 | 3.5256 | 0.0192 | 0.3689 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret17_neg_at_h` | one_head_filter_pi_star | 164 | 13.4104 | 2.2014 | 0.7012 | 4.1126 | 0.0181 | 0.4207 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret17_neg_at_h` | one_head_filter_pi_star | 167 | 13.6557 | 2.1267 | 0.6946 | 3.9645 | 0.0172 | 0.4192 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ret17_pos_at_h` | one_head_filter_pi_star | 162 | 13.3685 | 1.2839 | 0.5988 | 1.3071 | 0.0086 | 0.2037 | ok | RAN |
| ETHUSDT | 8 | `ret17_pos_at_h` | one_head_filter_pi_star | 157 | 12.9559 | 1.1902 | 0.5924 | 0.8909 | 0.0061 | 0.1975 | ok | RAN |
| SOLUSDT | 8 | `ret17_pos_at_h` | one_head_filter_pi_star | 215 | 17.5312 | 1.4114 | 0.5953 | 2.1912 | 0.0060 | 0.2419 | ok | RAN |
| SOLUSDT | 4 | `ret17_pos_at_h` | one_head_filter_pi_star | 212 | 17.2866 | 1.3930 | 0.5991 | 2.0937 | 0.0057 | 0.2547 | ok | RAN |
| ETHUSDT | 8 | `ret17_cross_down_0` | one_head_filter_pi_star | 48 | 3.9644 | 1.0390 | 0.5417 | 0.1104 | 0.0019 | 0.2292 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret17_cross_down_0` | one_head_filter_pi_star | 13 | 1.7226 | 0.8495 | 0.6154 | -0.3011 | -0.0076 | 0.0769 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret17_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret17_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret17_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret17_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `ret17_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret17_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret17_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret17_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret17_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret17_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret17_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
