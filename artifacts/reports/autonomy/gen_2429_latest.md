# Autonomy public-indicator hunt gen 2429

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T171330Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret390_neg_at_h` | one_head_filter_pi_star | 150 | 12.2536 | 1.3255 | 0.5933 | 1.5612 | 0.0089 | 0.1800 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ret390_neg_at_h` | one_head_filter_pi_star | 168 | 13.7241 | 1.2632 | 0.5952 | 1.4051 | 0.0078 | 0.1667 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret390_pos_at_h` | one_head_filter_pi_star | 127 | 10.4146 | 1.1538 | 0.5827 | 0.6852 | 0.0029 | 0.1260 | ok | RAN |
| SOLUSDT | 8 | `ret390_pos_at_h` | one_head_filter_pi_star | 141 | 11.5627 | 1.0397 | 0.5461 | 0.1937 | 0.0008 | 0.1206 | ok | RAN |
| SOLUSDT | 4 | `ret390_neg_at_h` | one_head_filter_pi_star | 176 | 14.3917 | 1.0042 | 0.5625 | 0.0251 | 0.0001 | 0.1477 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 8 | `ret390_neg_at_h` | one_head_filter_pi_star | 183 | 14.9641 | 0.9108 | 0.5410 | -0.5577 | -0.0019 | 0.1530 | ok | RAN |
| ETHUSDT | 8 | `ret390_pos_at_h` | one_head_filter_pi_star | 189 | 15.5356 | 0.8340 | 0.5397 | -0.9980 | -0.0070 | 0.1058 | ok | RAN |
| ETHUSDT | 4 | `ret390_pos_at_h` | one_head_filter_pi_star | 172 | 14.1382 | 0.7788 | 0.5291 | -1.3657 | -0.0096 | 0.1163 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret390_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4748 | 0.3158 | -1.1705 | -0.0528 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret390_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4142 | 0.2632 | -1.4203 | -0.0692 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret390_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret390_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret390_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret390_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret390_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret390_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret390_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret390_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret390_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret390_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret390_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret390_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret390_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret390_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
