# Autonomy public-indicator hunt gen 229

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T003225Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret11_cross_down_0` | one_head_filter_pi_star | 42 | 3.4675 | 1.9959 | 0.6429 | 1.8741 | 0.0316 | 0.2381 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret11_cross_up_0` | one_head_filter_pi_star | 32 | 2.6332 | 1.9188 | 0.6875 | 1.5563 | 0.0281 | 0.3125 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ret11_cross_down_0` | one_head_filter_pi_star | 32 | 2.8109 | 3.4518 | 0.7500 | 2.7047 | 0.0215 | 0.1250 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ret11_cross_down_0` | one_head_filter_pi_star | 13 | 1.2029 | 3.9121 | 0.8462 | 1.8092 | 0.0212 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret11_neg_at_h` | one_head_filter_pi_star | 221 | 18.0537 | 1.8331 | 0.6833 | 3.9477 | 0.0212 | 0.3710 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret11_neg_at_h` | one_head_filter_pi_star | 217 | 17.7269 | 1.7090 | 0.6682 | 3.4866 | 0.0188 | 0.3779 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret11_neg_at_h` | one_head_filter_pi_star | 163 | 13.3287 | 2.2453 | 0.6933 | 4.1637 | 0.0184 | 0.4233 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret11_neg_at_h` | one_head_filter_pi_star | 164 | 13.4104 | 2.0629 | 0.6890 | 3.7513 | 0.0166 | 0.4146 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret11_cross_up_0` | one_head_filter_pi_star | 22 | 2.1144 | 1.6967 | 0.6364 | 1.1254 | 0.0152 | 0.2273 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret11_cross_down_0` | one_head_filter_pi_star | 14 | 1.3894 | 1.2670 | 0.7143 | 0.4129 | 0.0120 | 0.2143 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ret11_pos_at_h` | one_head_filter_pi_star | 161 | 13.2859 | 1.2279 | 0.5901 | 1.0520 | 0.0071 | 0.1925 | ok | RAN |
| ETHUSDT | 8 | `ret11_pos_at_h` | one_head_filter_pi_star | 161 | 13.2859 | 1.2179 | 0.5963 | 1.0035 | 0.0070 | 0.2050 | ok | RAN |
| SOLUSDT | 4 | `ret11_pos_at_h` | one_head_filter_pi_star | 216 | 17.6127 | 1.4055 | 0.5972 | 2.1881 | 0.0060 | 0.2500 | ok | RAN |
| SOLUSDT | 8 | `ret11_pos_at_h` | one_head_filter_pi_star | 214 | 17.4496 | 1.3985 | 0.5981 | 2.1408 | 0.0059 | 0.2523 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret11_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret11_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret11_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret11_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret11_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret11_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret11_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret11_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret11_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret11_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
