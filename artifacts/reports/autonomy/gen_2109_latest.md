# Autonomy public-indicator hunt gen 2109

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T232352Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret345_neg_at_h` | one_head_filter_pi_star | 162 | 13.2339 | 1.2529 | 0.6049 | 1.3338 | 0.0075 | 0.1914 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ret345_neg_at_h` | one_head_filter_pi_star | 167 | 13.6424 | 1.1931 | 0.5928 | 1.0553 | 0.0059 | 0.2036 | ok | RAN |
| SOLUSDT | 4 | `ret345_pos_at_h` | one_head_filter_pi_star | 142 | 11.6447 | 1.1687 | 0.5634 | 0.7821 | 0.0031 | 0.1197 | ok | RAN |
| SOLUSDT | 8 | `ret345_pos_at_h` | one_head_filter_pi_star | 154 | 12.5572 | 1.0973 | 0.5584 | 0.4872 | 0.0018 | 0.1169 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ret345_neg_at_h` | one_head_filter_pi_star | 214 | 17.4990 | 0.9426 | 0.5607 | -0.3790 | -0.0012 | 0.1449 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 8 | `ret345_neg_at_h` | one_head_filter_pi_star | 212 | 17.3354 | 0.9010 | 0.5425 | -0.6699 | -0.0021 | 0.1368 | ok | RAN |
| ETHUSDT | 8 | `ret345_pos_at_h` | one_head_filter_pi_star | 172 | 14.1937 | 0.8081 | 0.5465 | -1.1493 | -0.0080 | 0.0930 | ok | RAN |
| ETHUSDT | 4 | `ret345_pos_at_h` | one_head_filter_pi_star | 188 | 15.4027 | 0.7905 | 0.5372 | -1.3065 | -0.0091 | 0.0957 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret345_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4309 | 0.2632 | -1.3328 | -0.0697 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret345_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.3886 | 0.2105 | -1.5181 | -0.0754 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret345_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret345_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret345_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret345_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret345_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret345_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret345_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret345_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret345_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret345_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret345_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret345_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret345_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret345_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
