# Autonomy public-indicator hunt gen 2485

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T233401Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret404_neg_at_h` | one_head_filter_pi_star | 156 | 12.7438 | 1.2772 | 0.6154 | 1.3741 | 0.0082 | 0.1923 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret404_neg_at_h` | one_head_filter_pi_star | 159 | 12.9888 | 1.2439 | 0.5912 | 1.2723 | 0.0071 | 0.1887 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret404_pos_at_h` | one_head_filter_pi_star | 115 | 9.5585 | 1.1452 | 0.5826 | 0.6164 | 0.0028 | 0.1130 | ok | RAN |
| SOLUSDT | 4 | `ret404_pos_at_h` | one_head_filter_pi_star | 159 | 12.9649 | 1.1174 | 0.5535 | 0.6016 | 0.0023 | 0.1195 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ret404_neg_at_h` | one_head_filter_pi_star | 186 | 15.2094 | 0.9875 | 0.5591 | -0.0737 | -0.0003 | 0.1505 | ok | RAN |
| SOLUSDT | 4 | `ret404_neg_at_h` | one_head_filter_pi_star | 170 | 13.9010 | 0.9635 | 0.5706 | -0.2126 | -0.0008 | 0.1412 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ret404_pos_at_h` | one_head_filter_pi_star | 175 | 14.3848 | 0.8600 | 0.5429 | -0.8414 | -0.0058 | 0.1029 | ok | RAN |
| ETHUSDT | 4 | `ret404_pos_at_h` | one_head_filter_pi_star | 177 | 14.5492 | 0.7991 | 0.5311 | -1.2544 | -0.0088 | 0.1130 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret404_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4442 | 0.2632 | -1.2722 | -0.0565 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret404_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4309 | 0.2632 | -1.3328 | -0.0658 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret404_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret404_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret404_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret404_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret404_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret404_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret404_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret404_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret404_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret404_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret404_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret404_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret404_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret404_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
