# Autonomy public-indicator hunt gen 2086

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T201256Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma503_below_at_h` | one_head_filter_pi_star | 190 | 15.5213 | 1.1181 | 0.5789 | 0.7176 | 0.0037 | 0.1789 | ok | RAN |
| ETHUSDT | 4 | `wma503_below_at_h` | one_head_filter_pi_star | 178 | 14.5410 | 1.0857 | 0.5843 | 0.5145 | 0.0028 | 0.2022 | ok | RAN |
| SOLUSDT | 8 | `wma503_above_at_h` | one_head_filter_pi_star | 182 | 14.8404 | 1.0676 | 0.5495 | 0.3782 | 0.0012 | 0.0934 | ok | RAN |
| SOLUSDT | 8 | `wma503_below_at_h` | one_head_filter_pi_star | 169 | 13.8193 | 1.0200 | 0.5562 | 0.1131 | 0.0004 | 0.1598 | ok | RAN |
| SOLUSDT | 4 | `wma503_below_at_h` | one_head_filter_pi_star | 175 | 14.3099 | 1.0045 | 0.5600 | 0.0264 | 0.0001 | 0.1486 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `wma503_above_at_h` | one_head_filter_pi_star | 189 | 15.4111 | 0.9855 | 0.5344 | -0.0856 | -0.0003 | 0.1005 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `wma503_above_at_h` | one_head_filter_pi_star | 192 | 15.7822 | 0.8086 | 0.5312 | -1.2529 | -0.0078 | 0.0938 | ok | RAN |
| ETHUSDT | 4 | `wma503_above_at_h` | one_head_filter_pi_star | 191 | 15.7000 | 0.7908 | 0.5183 | -1.3754 | -0.0087 | 0.0942 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma503_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5128 | 0.2778 | -1.0553 | -0.0470 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma503_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma503_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma503_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma503_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma503_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma503_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma503_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma503_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma503_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma503_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma503_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma503_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma503_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma503_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma503_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
