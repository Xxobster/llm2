# Autonomy public-indicator hunt gen 2438

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T181723Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma558_below_at_h` | one_head_filter_pi_star | 188 | 15.3579 | 1.1626 | 0.5957 | 0.9464 | 0.0050 | 0.1862 | ok | RAN |
| ETHUSDT | 4 | `wma558_below_at_h` | one_head_filter_pi_star | 186 | 15.1945 | 1.1154 | 0.5860 | 0.6913 | 0.0036 | 0.1828 | ok | RAN |
| SOLUSDT | 8 | `wma558_above_at_h` | one_head_filter_pi_star | 182 | 14.8404 | 1.1148 | 0.5495 | 0.6237 | 0.0020 | 0.0989 | ok | RAN |
| SOLUSDT | 4 | `wma558_above_at_h` | one_head_filter_pi_star | 177 | 14.4326 | 1.0996 | 0.5650 | 0.5476 | 0.0018 | 0.1017 | ok | RAN |
| SOLUSDT | 4 | `wma558_below_at_h` | one_head_filter_pi_star | 183 | 14.9641 | 1.0063 | 0.5574 | 0.0377 | 0.0001 | 0.1475 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `wma558_below_at_h` | one_head_filter_pi_star | 194 | 15.8635 | 0.9714 | 0.5515 | -0.1790 | -0.0006 | 0.1598 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `wma558_above_at_h` | one_head_filter_pi_star | 187 | 15.3712 | 0.8415 | 0.5348 | -0.9995 | -0.0063 | 0.0963 | ok | RAN |
| ETHUSDT | 4 | `wma558_above_at_h` | one_head_filter_pi_star | 181 | 14.8780 | 0.8267 | 0.5359 | -1.1042 | -0.0073 | 0.0939 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma558_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0682 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma558_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma558_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma558_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma558_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma558_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma558_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma558_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma558_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma558_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma558_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma558_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma558_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma558_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma558_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma558_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
