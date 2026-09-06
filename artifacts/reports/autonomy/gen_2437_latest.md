# Autonomy public-indicator hunt gen 2437

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T181008Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret391_neg_at_h` | one_head_filter_pi_star | 160 | 13.0705 | 1.2645 | 0.5938 | 1.3932 | 0.0083 | 0.1875 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ret391_neg_at_h` | one_head_filter_pi_star | 168 | 13.7241 | 1.2341 | 0.6131 | 1.2551 | 0.0070 | 0.1845 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret391_pos_at_h` | one_head_filter_pi_star | 122 | 10.0046 | 1.1256 | 0.5656 | 0.5502 | 0.0022 | 0.1148 | ok | RAN |
| SOLUSDT | 8 | `ret391_pos_at_h` | one_head_filter_pi_star | 122 | 10.0046 | 1.1053 | 0.5656 | 0.4637 | 0.0019 | 0.0984 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ret391_neg_at_h` | one_head_filter_pi_star | 181 | 14.7247 | 0.9785 | 0.5635 | -0.1317 | -0.0004 | 0.1326 | ok | RAN |
| SOLUSDT | 8 | `ret391_neg_at_h` | one_head_filter_pi_star | 172 | 14.0646 | 0.9517 | 0.5523 | -0.2900 | -0.0010 | 0.1512 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ret391_pos_at_h` | one_head_filter_pi_star | 178 | 14.6314 | 0.7876 | 0.5337 | -1.3084 | -0.0094 | 0.1124 | ok | RAN |
| ETHUSDT | 8 | `ret391_pos_at_h` | one_head_filter_pi_star | 184 | 15.1246 | 0.7747 | 0.5326 | -1.4457 | -0.0098 | 0.1141 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret391_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4442 | 0.2632 | -1.2722 | -0.0585 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret391_pos_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.4092 | 0.2500 | -1.4181 | -0.0675 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret391_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret391_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret391_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret391_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret391_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret391_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret391_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret391_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret391_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret391_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret391_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret391_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret391_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret391_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
