# Autonomy public-indicator hunt gen 773

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T130337Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret141_neg_at_h` | one_head_filter_pi_star | 186 | 15.1945 | 1.9605 | 0.6828 | 4.3063 | 0.0225 | 0.3710 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret141_neg_at_h` | one_head_filter_pi_star | 199 | 16.2565 | 1.8001 | 0.6633 | 3.8731 | 0.0205 | 0.3618 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret141_neg_at_h` | one_head_filter_pi_star | 196 | 16.0271 | 2.1899 | 0.6837 | 4.5579 | 0.0165 | 0.3622 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret141_neg_at_h` | one_head_filter_pi_star | 173 | 14.1464 | 2.1007 | 0.6821 | 3.9368 | 0.0155 | 0.3642 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ret141_pos_at_h` | one_head_filter_pi_star | 174 | 14.3587 | 1.2890 | 0.6092 | 1.4263 | 0.0096 | 0.2184 | ok | RAN |
| ETHUSDT | 4 | `ret141_pos_at_h` | one_head_filter_pi_star | 180 | 14.8539 | 1.2483 | 0.6000 | 1.2745 | 0.0087 | 0.2167 | ok | RAN |
| SOLUSDT | 4 | `ret141_pos_at_h` | one_head_filter_pi_star | 201 | 16.3896 | 1.4054 | 0.6020 | 2.0361 | 0.0065 | 0.2736 | ok | RAN |
| SOLUSDT | 8 | `ret141_pos_at_h` | one_head_filter_pi_star | 195 | 15.9004 | 1.3713 | 0.6000 | 1.8671 | 0.0060 | 0.2667 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret141_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret141_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret141_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret141_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret141_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret141_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret141_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret141_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret141_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret141_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret141_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret141_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret141_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret141_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret141_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret141_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
