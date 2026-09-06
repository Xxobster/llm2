# Autonomy public-indicator hunt gen 146

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T190332Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret6_neg_at_h` | one_head_filter_pi_star | 24 | 2.1710 | 3.8924 | 0.7083 | 2.5495 | 0.0425 | 0.2083 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret6_neg_at_h` | one_head_filter_pi_star | 221 | 18.0537 | 1.7670 | 0.6742 | 3.6702 | 0.0199 | 0.3710 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret6_cross_up_0` | one_head_filter_pi_star | 221 | 18.0537 | 1.7104 | 0.6697 | 3.4770 | 0.0189 | 0.3756 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret6_cross_up_0` | one_head_filter_pi_star | 168 | 13.7375 | 2.2314 | 0.6964 | 4.1620 | 0.0179 | 0.4167 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret6_neg_at_h` | one_head_filter_pi_star | 165 | 13.4922 | 2.1471 | 0.6848 | 3.9779 | 0.0175 | 0.4182 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ret6_cross_down_0` | one_head_filter_pi_star | 168 | 13.8636 | 1.2500 | 0.6012 | 1.1525 | 0.0078 | 0.2143 | ok | RAN |
| ETHUSDT | 4 | `ret6_pos_at_h` | one_head_filter_pi_star | 163 | 13.4510 | 1.2299 | 0.5951 | 1.0538 | 0.0073 | 0.2025 | ok | RAN |
| SOLUSDT | 8 | `ret6_cross_down_0` | one_head_filter_pi_star | 217 | 17.6943 | 1.3841 | 0.5991 | 2.0635 | 0.0056 | 0.2488 | ok | RAN |
| SOLUSDT | 4 | `ret6_pos_at_h` | one_head_filter_pi_star | 216 | 17.6127 | 1.3703 | 0.5972 | 2.0159 | 0.0055 | 0.2454 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret6_cross_down_0` | one_head_filter_pi_star | 19 | 1.6169 | 0.6588 | 0.3158 | -0.6893 | -0.0355 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret6_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret6_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 4 | `ret6_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 8 | `ret6_pos_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret6_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret6_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 8 | `ret6_pos_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret6_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret6_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret6_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret6_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret6_pos_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret6_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret6_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
