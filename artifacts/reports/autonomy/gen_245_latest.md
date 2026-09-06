# Autonomy public-indicator hunt gen 245

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T013712Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret15_cross_up_0` | one_head_filter_pi_star | 40 | 3.2915 | 1.7795 | 0.6500 | 1.6018 | 0.0311 | 0.3000 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ret15_cross_up_0` | one_head_filter_pi_star | 17 | 1.4779 | 3.1338 | 0.7059 | 1.8119 | 0.0272 | 0.2353 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ret15_cross_down_0` | one_head_filter_pi_star | 26 | 2.1389 | 3.1316 | 0.7692 | 2.2526 | 0.0212 | 0.1923 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret15_neg_at_h` | one_head_filter_pi_star | 219 | 17.8903 | 1.7838 | 0.6758 | 3.7749 | 0.0205 | 0.3790 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret15_neg_at_h` | one_head_filter_pi_star | 217 | 17.7269 | 1.7625 | 0.6728 | 3.6902 | 0.0198 | 0.3779 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret15_neg_at_h` | one_head_filter_pi_star | 162 | 13.2469 | 2.1585 | 0.6914 | 3.9828 | 0.0175 | 0.4259 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret15_neg_at_h` | one_head_filter_pi_star | 167 | 13.6557 | 2.0841 | 0.6946 | 3.8330 | 0.0166 | 0.4072 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret15_cross_down_0` | one_head_filter_pi_star | 13 | 1.2818 | 1.6290 | 0.5385 | 0.8119 | 0.0121 | 0.3077 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ret15_pos_at_h` | one_head_filter_pi_star | 163 | 13.4510 | 1.2751 | 0.5951 | 1.2310 | 0.0084 | 0.2025 | ok | RAN |
| ETHUSDT | 4 | `ret15_cross_down_0` | one_head_filter_pi_star | 21 | 1.7402 | 1.1867 | 0.5714 | 0.3405 | 0.0067 | 0.1905 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret15_pos_at_h` | one_head_filter_pi_star | 157 | 12.9559 | 1.1984 | 0.5860 | 0.9101 | 0.0063 | 0.2102 | ok | RAN |
| SOLUSDT | 8 | `ret15_pos_at_h` | one_head_filter_pi_star | 214 | 17.4496 | 1.3853 | 0.5888 | 2.0975 | 0.0057 | 0.2570 | ok | RAN |
| SOLUSDT | 4 | `ret15_pos_at_h` | one_head_filter_pi_star | 211 | 17.2050 | 1.3744 | 0.6019 | 1.9964 | 0.0055 | 0.2417 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret15_cross_down_0` | one_head_filter_pi_star | 30 | 2.4860 | 0.7501 | 0.5333 | -0.6464 | -0.0122 | 0.1333 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret15_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret15_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret15_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `ret15_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret15_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret15_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret15_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret15_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret15_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret15_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
