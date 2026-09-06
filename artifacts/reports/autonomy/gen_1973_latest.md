# Autonomy public-indicator hunt gen 1973

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T061417Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret325_neg_at_h` | one_head_filter_pi_star | 165 | 13.4790 | 1.1913 | 0.6061 | 1.0900 | 0.0061 | 0.2121 | ok | RAN |
| ETHUSDT | 4 | `ret325_neg_at_h` | one_head_filter_pi_star | 150 | 12.2536 | 1.1911 | 0.6133 | 1.0158 | 0.0060 | 0.2133 | ok | RAN |
| SOLUSDT | 4 | `ret325_pos_at_h` | one_head_filter_pi_star | 165 | 13.4542 | 1.1882 | 0.5576 | 0.9250 | 0.0033 | 0.1152 | ok | RAN |
| SOLUSDT | 8 | `ret325_pos_at_h` | one_head_filter_pi_star | 170 | 13.9408 | 1.1451 | 0.5529 | 0.7423 | 0.0026 | 0.1059 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ret325_neg_at_h` | one_head_filter_pi_star | 171 | 13.9828 | 0.9701 | 0.5673 | -0.1747 | -0.0007 | 0.1520 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 8 | `ret325_neg_at_h` | one_head_filter_pi_star | 179 | 14.5620 | 0.9089 | 0.5475 | -0.5657 | -0.0020 | 0.1508 | ok | RAN |
| ETHUSDT | 8 | `ret325_pos_at_h` | one_head_filter_pi_star | 198 | 16.2753 | 0.8017 | 0.5404 | -1.2306 | -0.0084 | 0.0960 | ok | RAN |
| ETHUSDT | 4 | `ret325_pos_at_h` | one_head_filter_pi_star | 190 | 15.6178 | 0.7448 | 0.5211 | -1.6737 | -0.0106 | 0.1105 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret325_pos_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.3937 | 0.2500 | -1.5052 | -0.0720 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret325_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.3886 | 0.2105 | -1.5181 | -0.0754 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret325_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret325_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret325_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret325_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret325_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret325_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret325_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret325_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret325_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret325_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret325_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret325_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret325_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret325_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
