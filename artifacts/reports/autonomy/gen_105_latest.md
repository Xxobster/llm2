# Autonomy public-indicator hunt gen 105

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T162407Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret5_pos_at_h` | one_head_filter_pi_star | 11 | 0.9275 | 24.0249 | 0.8182 | 2.8339 | 0.0635 | 0.4545 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret5_neg_at_h` | one_head_filter_pi_star | 223 | 18.2171 | 1.8001 | 0.6726 | 3.8484 | 0.0207 | 0.3722 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret5_neg_at_h` | one_head_filter_pi_star | 21 | 1.9667 | 1.6713 | 0.6190 | 1.1248 | 0.0195 | 0.4286 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret5_cross_up_0` | one_head_filter_pi_star | 225 | 18.3804 | 1.7514 | 0.6711 | 3.6998 | 0.0195 | 0.3689 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret5_neg_at_h` | one_head_filter_pi_star | 165 | 13.4922 | 2.1491 | 0.6848 | 3.9824 | 0.0177 | 0.4182 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret5_cross_up_0` | one_head_filter_pi_star | 171 | 13.9828 | 2.1681 | 0.6901 | 4.0803 | 0.0173 | 0.4094 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `ret5_cross_up_0` | one_head_filter_pi_star | 11 | 1.0005 | 1.3802 | 0.5455 | 0.4966 | 0.0131 | 0.3636 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ret5_cross_down_0` | one_head_filter_pi_star | 167 | 13.7811 | 1.2140 | 0.5928 | 0.9987 | 0.0068 | 0.2096 | ok | RAN |
| ETHUSDT | 4 | `ret5_pos_at_h` | one_head_filter_pi_star | 166 | 13.6986 | 1.1839 | 0.5904 | 0.8717 | 0.0062 | 0.1988 | ok | RAN |
| SOLUSDT | 4 | `ret5_pos_at_h` | one_head_filter_pi_star | 216 | 17.6127 | 1.3987 | 0.6019 | 2.1434 | 0.0059 | 0.2454 | ok | RAN |
| SOLUSDT | 8 | `ret5_cross_down_0` | one_head_filter_pi_star | 222 | 18.1020 | 1.3618 | 0.5991 | 2.0170 | 0.0054 | 0.2432 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ret5_cross_down_0` | one_head_filter_pi_star | 16 | 1.5396 | 0.7793 | 0.4375 | -0.4845 | -0.0073 | 0.1250 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret5_cross_down_0` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret5_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret5_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `ret5_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret5_pos_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 8 | `ret5_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret5_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret5_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret5_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret5_pos_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret5_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret5_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
