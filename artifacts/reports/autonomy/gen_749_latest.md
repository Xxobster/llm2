# Autonomy public-indicator hunt gen 749

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T104404Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret135_neg_at_h` | one_head_filter_pi_star | 204 | 16.6649 | 1.9325 | 0.6814 | 4.2456 | 0.0224 | 0.3725 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret135_neg_at_h` | one_head_filter_pi_star | 194 | 15.8480 | 1.8747 | 0.6753 | 3.9452 | 0.0214 | 0.3557 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret135_neg_at_h` | one_head_filter_pi_star | 187 | 15.2912 | 2.1316 | 0.6898 | 4.2895 | 0.0162 | 0.3690 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret135_neg_at_h` | one_head_filter_pi_star | 185 | 15.1276 | 2.0878 | 0.6811 | 4.1204 | 0.0154 | 0.3622 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `ret135_pos_at_h` | one_head_filter_pi_star | 177 | 14.6063 | 1.3021 | 0.6045 | 1.4922 | 0.0103 | 0.2316 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ret135_pos_at_h` | one_head_filter_pi_star | 189 | 15.5965 | 1.2934 | 0.6190 | 1.4406 | 0.0097 | 0.2222 | ok | RAN |
| SOLUSDT | 8 | `ret135_pos_at_h` | one_head_filter_pi_star | 191 | 15.5742 | 1.3759 | 0.6021 | 1.8862 | 0.0061 | 0.2513 | ok | RAN |
| SOLUSDT | 4 | `ret135_pos_at_h` | one_head_filter_pi_star | 196 | 15.9819 | 1.3590 | 0.5969 | 1.8332 | 0.0057 | 0.2551 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret135_pos_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.6954 | 0.3500 | -0.6289 | -0.0317 | 0.1000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret135_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret135_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret135_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret135_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret135_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret135_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret135_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret135_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret135_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret135_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret135_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret135_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret135_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret135_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret135_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
