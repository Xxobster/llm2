# Autonomy public-indicator hunt gen 285

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T042401Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret23_cross_up_0` | one_head_filter_pi_star | 12 | 1.0042 | 3.3994 | 0.6667 | 1.7153 | 0.0628 | 0.0833 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret23_cross_down_0` | one_head_filter_pi_star | 12 | 1.1719 | 4.4628 | 0.6667 | 2.1959 | 0.0471 | 0.4167 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret23_cross_up_0` | one_head_filter_pi_star | 31 | 2.5942 | 1.7445 | 0.5484 | 1.2670 | 0.0279 | 0.2258 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ret23_cross_down_0` | one_head_filter_pi_star | 27 | 2.2788 | 2.5657 | 0.7037 | 1.9111 | 0.0221 | 0.1852 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret23_neg_at_h` | one_head_filter_pi_star | 214 | 17.4818 | 1.8586 | 0.6776 | 4.0453 | 0.0215 | 0.3925 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret23_neg_at_h` | one_head_filter_pi_star | 227 | 18.5438 | 1.8136 | 0.6696 | 3.9873 | 0.0210 | 0.3656 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret23_cross_down_0` | one_head_filter_pi_star | 35 | 2.8896 | 1.6830 | 0.6286 | 1.2751 | 0.0207 | 0.2571 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ret23_neg_at_h` | one_head_filter_pi_star | 166 | 13.5740 | 2.2215 | 0.6928 | 4.1977 | 0.0183 | 0.4157 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret23_neg_at_h` | one_head_filter_pi_star | 171 | 13.9828 | 2.1624 | 0.6901 | 4.0922 | 0.0179 | 0.4035 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret23_cross_up_0` | one_head_filter_pi_star | 28 | 2.3898 | 1.8746 | 0.6071 | 1.3147 | 0.0131 | 0.2500 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ret23_pos_at_h` | one_head_filter_pi_star | 154 | 12.7083 | 1.1965 | 0.6039 | 0.9319 | 0.0061 | 0.1948 | ok | RAN |
| SOLUSDT | 4 | `ret23_pos_at_h` | one_head_filter_pi_star | 211 | 17.2050 | 1.3850 | 0.5972 | 2.0577 | 0.0057 | 0.2464 | ok | RAN |
| SOLUSDT | 8 | `ret23_pos_at_h` | one_head_filter_pi_star | 211 | 17.2050 | 1.3514 | 0.5972 | 1.8996 | 0.0052 | 0.2559 | ok | RAN |
| ETHUSDT | 4 | `ret23_pos_at_h` | one_head_filter_pi_star | 164 | 13.5335 | 1.1228 | 0.5915 | 0.6111 | 0.0041 | 0.1829 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret23_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret23_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ret23_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret23_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret23_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret23_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret23_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret23_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret23_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret23_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
