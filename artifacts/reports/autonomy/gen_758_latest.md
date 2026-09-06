# Autonomy public-indicator hunt gen 758

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T112343Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma380_below_at_h` | one_head_filter_pi_star | 187 | 15.2762 | 2.0404 | 0.7005 | 4.5767 | 0.0239 | 0.3904 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma380_below_at_h` | one_head_filter_pi_star | 186 | 15.1945 | 1.8848 | 0.6882 | 4.0619 | 0.0215 | 0.3817 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma380_below_at_h` | one_head_filter_pi_star | 182 | 14.8823 | 2.2486 | 0.6978 | 4.4595 | 0.0174 | 0.3791 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma380_below_at_h` | one_head_filter_pi_star | 172 | 14.0646 | 2.1954 | 0.6919 | 4.1507 | 0.0168 | 0.3779 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `wma380_above_at_h` | one_head_filter_pi_star | 191 | 15.7000 | 1.2602 | 0.6021 | 1.3602 | 0.0089 | 0.2251 | ok | RAN |
| ETHUSDT | 4 | `wma380_above_at_h` | one_head_filter_pi_star | 202 | 16.6041 | 1.2039 | 0.5990 | 1.0837 | 0.0072 | 0.2277 | ok | RAN |
| SOLUSDT | 8 | `wma380_above_at_h` | one_head_filter_pi_star | 200 | 16.3081 | 1.4394 | 0.6050 | 2.2112 | 0.0067 | 0.2550 | ok | RAN |
| SOLUSDT | 4 | `wma380_above_at_h` | one_head_filter_pi_star | 203 | 16.5527 | 1.3603 | 0.6010 | 1.8673 | 0.0058 | 0.2660 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma380_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma380_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma380_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma380_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma380_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma380_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma380_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma380_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma380_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma380_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma380_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma380_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma380_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma380_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma380_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma380_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
