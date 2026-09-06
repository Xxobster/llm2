# Autonomy public-indicator hunt gen 309

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T060816Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret29_cross_up_0` | one_head_filter_pi_star | 31 | 2.5942 | 2.2927 | 0.6129 | 1.9988 | 0.0385 | 0.1613 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ret29_cross_down_0` | one_head_filter_pi_star | 28 | 2.3898 | 4.4946 | 0.7500 | 2.6113 | 0.0324 | 0.2143 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret29_cross_down_0` | one_head_filter_pi_star | 34 | 2.9092 | 2.4942 | 0.6471 | 1.8872 | 0.0318 | 0.2941 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret29_neg_at_h` | one_head_filter_pi_star | 212 | 17.3185 | 1.8174 | 0.6745 | 3.9696 | 0.0215 | 0.3679 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret29_neg_at_h` | one_head_filter_pi_star | 208 | 16.9917 | 1.8467 | 0.6779 | 3.9683 | 0.0211 | 0.3894 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret29_neg_at_h` | one_head_filter_pi_star | 169 | 13.8193 | 2.0692 | 0.6746 | 3.8930 | 0.0164 | 0.3964 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret29_cross_up_0` | one_head_filter_pi_star | 21 | 1.7923 | 2.0743 | 0.6190 | 1.2954 | 0.0161 | 0.1905 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ret29_neg_at_h` | one_head_filter_pi_star | 166 | 13.5740 | 2.0309 | 0.6747 | 3.7463 | 0.0161 | 0.3916 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret29_pos_at_h` | one_head_filter_pi_star | 210 | 17.1235 | 1.4717 | 0.6095 | 2.3661 | 0.0068 | 0.2714 | ok | RAN |
| ETHUSDT | 4 | `ret29_pos_at_h` | one_head_filter_pi_star | 174 | 14.3026 | 1.2027 | 0.5977 | 0.9955 | 0.0063 | 0.2184 | ok | RAN |
| SOLUSDT | 4 | `ret29_pos_at_h` | one_head_filter_pi_star | 212 | 17.2866 | 1.4022 | 0.6085 | 2.0725 | 0.0059 | 0.2547 | ok | RAN |
| ETHUSDT | 8 | `ret29_pos_at_h` | one_head_filter_pi_star | 167 | 13.7811 | 1.1654 | 0.5868 | 0.8360 | 0.0055 | 0.1856 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret29_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret29_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret29_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret29_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret29_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret29_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret29_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret29_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret29_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret29_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret29_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret29_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
