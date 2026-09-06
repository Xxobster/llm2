# Autonomy public-indicator hunt gen 2045

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T142609Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret335_neg_at_h` | one_head_filter_pi_star | 162 | 13.2339 | 1.2983 | 0.6111 | 1.5471 | 0.0088 | 0.2037 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret335_neg_at_h` | one_head_filter_pi_star | 151 | 12.3353 | 1.1788 | 0.5828 | 0.9518 | 0.0055 | 0.2053 | ok | RAN |
| SOLUSDT | 4 | `ret335_pos_at_h` | one_head_filter_pi_star | 176 | 14.3511 | 1.2127 | 0.5511 | 1.0690 | 0.0037 | 0.1023 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret335_pos_at_h` | one_head_filter_pi_star | 161 | 13.2028 | 1.1663 | 0.5590 | 0.8441 | 0.0031 | 0.1056 | ok | RAN |
| SOLUSDT | 4 | `ret335_neg_at_h` | one_head_filter_pi_star | 168 | 13.7375 | 1.0097 | 0.5655 | 0.0546 | 0.0002 | 0.1488 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ret335_neg_at_h` | one_head_filter_pi_star | 191 | 15.6182 | 0.9912 | 0.5654 | -0.0528 | -0.0002 | 0.1518 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ret335_pos_at_h` | one_head_filter_pi_star | 180 | 14.7958 | 0.7777 | 0.5222 | -1.3682 | -0.0097 | 0.1000 | ok | RAN |
| ETHUSDT | 4 | `ret335_pos_at_h` | one_head_filter_pi_star | 168 | 13.8094 | 0.7610 | 0.5357 | -1.4380 | -0.0103 | 0.1071 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret335_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4330 | 0.2778 | -1.3217 | -0.0706 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret335_pos_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.3937 | 0.2500 | -1.5052 | -0.0707 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret335_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret335_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret335_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret335_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret335_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret335_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret335_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret335_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret335_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret335_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret335_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret335_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret335_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret335_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
