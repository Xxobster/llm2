# Autonomy public-indicator hunt gen 1909

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T001344Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret316_neg_at_h` | one_head_filter_pi_star | 157 | 12.8255 | 1.2936 | 0.6115 | 1.4611 | 0.0085 | 0.2102 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret316_neg_at_h` | one_head_filter_pi_star | 169 | 13.8058 | 1.2273 | 0.6154 | 1.2368 | 0.0066 | 0.1893 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret316_pos_at_h` | one_head_filter_pi_star | 183 | 14.9219 | 1.0917 | 0.5410 | 0.5127 | 0.0017 | 0.1093 | ok | RAN |
| SOLUSDT | 8 | `ret316_pos_at_h` | one_head_filter_pi_star | 142 | 11.6447 | 1.0780 | 0.5423 | 0.3831 | 0.0015 | 0.1197 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ret316_neg_at_h` | one_head_filter_pi_star | 186 | 15.2094 | 1.0024 | 0.5645 | 0.0142 | 0.0000 | 0.1452 | ok | RAN |
| SOLUSDT | 8 | `ret316_neg_at_h` | one_head_filter_pi_star | 173 | 14.1464 | 0.9756 | 0.5549 | -0.1441 | -0.0005 | 0.1503 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ret316_pos_at_h` | one_head_filter_pi_star | 141 | 11.6355 | 0.8308 | 0.5319 | -0.9044 | -0.0072 | 0.0993 | ok | RAN |
| ETHUSDT | 4 | `ret316_pos_at_h` | one_head_filter_pi_star | 181 | 14.8780 | 0.7899 | 0.5359 | -1.3154 | -0.0090 | 0.0939 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret316_pos_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.6417 | 0.3125 | -0.6719 | -0.0328 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret316_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4142 | 0.2632 | -1.4203 | -0.0718 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret316_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret316_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret316_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret316_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret316_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret316_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret316_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret316_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret316_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret316_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret316_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret316_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret316_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret316_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
