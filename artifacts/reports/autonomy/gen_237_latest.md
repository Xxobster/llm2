# Autonomy public-indicator hunt gen 237

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T010451Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ret13_cross_up_0` | one_head_filter_pi_star | 13 | 1.1301 | 2.4211 | 0.7692 | 1.3811 | 0.0280 | 0.3846 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret13_cross_up_0` | one_head_filter_pi_star | 35 | 2.8800 | 1.5304 | 0.6286 | 1.1297 | 0.0211 | 0.2857 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret13_neg_at_h` | one_head_filter_pi_star | 219 | 17.8903 | 1.7852 | 0.6758 | 3.7847 | 0.0203 | 0.3790 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret13_neg_at_h` | one_head_filter_pi_star | 218 | 17.8086 | 1.7604 | 0.6743 | 3.7018 | 0.0198 | 0.3716 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret13_neg_at_h` | one_head_filter_pi_star | 164 | 13.4104 | 2.2356 | 0.6951 | 4.1437 | 0.0183 | 0.4207 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret13_neg_at_h` | one_head_filter_pi_star | 166 | 13.5740 | 2.0645 | 0.6867 | 3.7730 | 0.0165 | 0.4096 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret13_cross_down_0` | one_head_filter_pi_star | 39 | 3.6087 | 1.7374 | 0.6410 | 1.4242 | 0.0099 | 0.0513 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ret13_cross_up_0` | one_head_filter_pi_star | 32 | 2.7147 | 1.3982 | 0.5938 | 0.8134 | 0.0085 | 0.2188 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret13_cross_down_0` | one_head_filter_pi_star | 22 | 1.8170 | 1.2095 | 0.5909 | 0.3833 | 0.0080 | 0.1818 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret13_pos_at_h` | one_head_filter_pi_star | 161 | 13.2859 | 1.2441 | 0.5963 | 1.1175 | 0.0076 | 0.2050 | ok | RAN |
| ETHUSDT | 8 | `ret13_cross_down_0` | one_head_filter_pi_star | 42 | 3.4688 | 1.1953 | 0.5476 | 0.4734 | 0.0074 | 0.1667 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret13_pos_at_h` | one_head_filter_pi_star | 158 | 13.0384 | 1.2190 | 0.5949 | 1.0194 | 0.0069 | 0.1899 | ok | RAN |
| SOLUSDT | 8 | `ret13_pos_at_h` | one_head_filter_pi_star | 215 | 17.5312 | 1.3928 | 0.5953 | 2.1177 | 0.0058 | 0.2512 | ok | RAN |
| SOLUSDT | 4 | `ret13_pos_at_h` | one_head_filter_pi_star | 212 | 17.2866 | 1.3888 | 0.5943 | 2.0727 | 0.0057 | 0.2453 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret13_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret13_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret13_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `ret13_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret13_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret13_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret13_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret13_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret13_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret13_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
