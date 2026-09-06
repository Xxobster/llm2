# Autonomy public-indicator hunt gen 2430

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T172035Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma557_below_at_h` | one_head_filter_pi_star | 180 | 14.7044 | 1.1680 | 0.5944 | 0.9740 | 0.0051 | 0.1889 | ok | RAN |
| ETHUSDT | 4 | `wma557_below_at_h` | one_head_filter_pi_star | 180 | 14.7044 | 1.1431 | 0.5889 | 0.8327 | 0.0044 | 0.1889 | ok | RAN |
| SOLUSDT | 4 | `wma557_above_at_h` | one_head_filter_pi_star | 184 | 15.0034 | 1.0777 | 0.5543 | 0.4396 | 0.0014 | 0.0978 | ok | RAN |
| SOLUSDT | 8 | `wma557_above_at_h` | one_head_filter_pi_star | 183 | 14.9219 | 1.0657 | 0.5519 | 0.3727 | 0.0012 | 0.0984 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `wma557_below_at_h` | one_head_filter_pi_star | 189 | 15.4547 | 0.9785 | 0.5556 | -0.1317 | -0.0005 | 0.1640 | ok | RAN |
| SOLUSDT | 4 | `wma557_below_at_h` | one_head_filter_pi_star | 186 | 15.2094 | 0.9488 | 0.5484 | -0.3150 | -0.0011 | 0.1452 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `wma557_above_at_h` | one_head_filter_pi_star | 180 | 14.7958 | 0.8694 | 0.5444 | -0.8017 | -0.0054 | 0.0944 | ok | RAN |
| ETHUSDT | 8 | `wma557_above_at_h` | one_head_filter_pi_star | 187 | 15.3712 | 0.8208 | 0.5348 | -1.1631 | -0.0075 | 0.0963 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma557_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma557_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma557_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma557_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma557_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma557_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma557_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma557_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma557_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma557_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma557_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma557_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma557_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma557_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma557_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma557_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
