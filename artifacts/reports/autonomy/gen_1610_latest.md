# Autonomy public-indicator hunt gen 1610

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260901T190600Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ret1464_pos_at_h` | one_head_filter_pi_star | 21 | 1.8728 | 1.9025 | 0.7143 | 1.1893 | 0.0106 | 0.1905 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ret1464_pos_at_h` | one_head_filter_pi_star | 21 | 1.8728 | 1.5278 | 0.6667 | 0.8411 | 0.0079 | 0.1905 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret1464_pos_at_h` | one_head_filter_pi_star | 13 | 4.0082 | 1.1312 | 0.6154 | 0.3719 | 0.0043 | 0.0769 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ret1464_neg_at_h` | one_head_filter_pi_star | 340 | 27.6597 | 1.0015 | 0.5441 | 0.0115 | 0.0000 | 0.1353 | ok | RAN |
| SOLUSDT | 4 | `ret1464_neg_at_h` | one_head_filter_pi_star | 334 | 27.1716 | 0.9861 | 0.5479 | -0.1097 | -0.0003 | 0.1377 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ret1464_neg_at_h` | one_head_filter_pi_star | 330 | 26.8461 | 0.9358 | 0.5485 | -0.5222 | -0.0021 | 0.1364 | ok | RAN |
| ETHUSDT | 4 | `ret1464_neg_at_h` | one_head_filter_pi_star | 317 | 25.7886 | 0.9145 | 0.5426 | -0.6908 | -0.0029 | 0.1420 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret1464_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5236 | 0.2632 | -1.0815 | -0.0621 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret1464_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.3880 | 0.2222 | -1.4607 | -0.0798 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1464_pos_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 4 | `ret1464_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret1464_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1464_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1464_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1464_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1464_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1464_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1464_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1464_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1464_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1464_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1464_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1464_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1464_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
